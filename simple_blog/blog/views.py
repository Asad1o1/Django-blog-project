from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.regex_helper import flatten_result
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.


class HomePage(ListView):
    model = models.Post
    template_name = "home.html"
    ordering = ['-published']
    # ordering = ['-id']

    def get_context_data(self, **kwargs):
        category_menu = models.Category.objects.all()
        context = super(HomePage, self).get_context_data(**kwargs)
        context["category_menu"] = category_menu
        return context


class ArticleDetailView(DetailView):
    model = models.Post
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        category_menu = models.Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        like = get_object_or_404(models.Post, id=self.kwargs['pk'])
        total_likes = like.total_like()

        liked = False
        if like.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["total_like"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    form_class = forms.PostForm
    model = models.Post
    template_name = 'add_post.html'
    # fields = '__all__'


class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.EditPostForm
    template_name = 'edit_post.html'
    # fields = ('title', 'body')


class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = models.Category
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, name):
    category_posts = models.Post.objects.filter(category=name)
    return render(request, 'categories.html', {'name': name.title(), 'category_posts': category_posts, })


def CategoryListView(request):
    category_list_menu = models.Category.objects.all()
    return render(request, 'category_list.html', {'category_list_menu': category_list_menu})


def LikeView(request, pk):
    post = get_object_or_404(models.Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:  
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class AddCommentView(CreateView):
    form_class = forms.CommentForm
    model = models.Comment
    template_name = 'comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

    