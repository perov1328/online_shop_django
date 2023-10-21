from django.shortcuts import render, reverse, HttpResponseRedirect
from catalog.models import Category, Product, Blog
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from pytils.translit import slugify


# Create your views here.

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории наших товаров',
    }


class ContactsView(TemplateView):
    template_name = 'catalog/contact.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"{name} ({phone}): {message}")

        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Полный список наших товаров'
    }


class ProductsCategoryListView(ListView):

    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Товары из категории: {category_item.name}'

        return context_data


class ProductDetailView(DetailView):

    model = Product


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    # success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list')