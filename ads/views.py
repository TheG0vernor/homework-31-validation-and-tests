import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Category, Ad
from ads.serializers import AdListSerializer, AdRetrieveSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroySerializer
from ads.permission import AdPermission


def root(request):
    return JsonResponse({
        "status": "ok"
    })


# Views Ads:


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        q_category_ads = request.GET.get('cat', None)
        q_text_in_ads = request.GET.get('text', None)
        q_location_ads = request.GET.get('location', None)
        q_price_from = request.GET.get('price_from', None)
        q_price_to = request.GET.get('price_to', None)

        if q_category_ads:
            self.queryset = self.queryset.filter(
                category_id__in=q_category_ads
            )
        if q_text_in_ads:
            self.queryset = self.queryset.filter(
                name__contains=q_text_in_ads
            )
        if q_location_ads:
            self.queryset = self.queryset.filter(
                author__locations__name__icontains=q_location_ads
            )
        if q_price_from and q_price_to:
            self.queryset = self.queryset.filter(
                price__range=(q_price_from, q_price_to)
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdRetrieveSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, AdPermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):  # добавление изображений
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({'id': self.object.id,
                             "name": self.object.name,
                             "author_id": self.object.author_id,
                             "author": self.object.author.first_name,
                             "price": self.object.price,
                             "description": self.object.description,
                             "is_published": self.object.is_published,
                             'category_id': self.object.category_id,
                             "image": self.object.image.url if self.object.image else None},
                            json_dumps_params={'ensure_ascii': False})


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [IsAuthenticated, AdPermission]


# Views Categories:


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        self.object_list = self.object_list.order_by('name')  # сортировка категорий

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"],
        )

        try:
            category.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data['name']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({"id": self.object.id,
                             'name': self.object.name}, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({'status': 'ok'})
