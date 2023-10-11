from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Task, Article


def index(request):
    return HttpResponse("this is django view demo")


def task_list(request):
    """
    任务清单
    """
    # 获取Task对象列表
    tasks = Task.objects.all()
    # 指定渲染模板并向模板传递数据
    return render(request, "mvt_design/task_list.html", {"tasks": tasks})


def blog(request):
    """
    展示所有文章
    :param request:
    :return:
    """
    latest_articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/article_list.html', {'latest_articles': latest_articles})


def article_detail(request, id):
    """
    根据文章ID展示文章
    :param request:
    :param id:
    :return:
    """
    article = get_object_or_404(Article, pk=id)
    return render(request, 'blog/article_detail.html', {'article': article})



# 使用通用类视图
from django.views.generic import ListView
from django.utils import timezone

class IndexView(ListView):
    model = Article
    template_name = 'blog/article_object_list.html'
    # 如果此处不指定template_name，则默认会调用app_name下面的article_object_list.html 即'mvt_design/article_object_list.html'


class CustomIndexView(ListView):
    """
    自定义ListView
    """
    # 按照日期升序
    queryset = Article.objects.all().order_by('pub_date')
    template_name = 'blog/article_object_list_v2.html'
    context_object_name = 'latest_articles'

    def get_context_data(self, **kwargs):
        context = super(CustomIndexView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['view_type'] = 'ListView'
        return context


class CustomIndexView2(ListView):
    """
    自定义ListView 控制查询属于自己的内容
    """
    template_name = 'blog/article_object_list_v2.html'
    context_object_name = 'latest_articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(CustomIndexView2, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['view_type'] = 'ListView'
        return context



from django.views.generic import DetailView

class ArticleDetailView(DetailView):
    """
    展示具体对象的详细信息
    """
    model = Article
    template_name = 'blog/article_detail.html'

class CustomArticleDetailView(DetailView):
    """
    重写get_context_data方法
    """
    queryset = Article.objects.all().order_by('pub_date')
    template_name = 'blog/article_detail_v2.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(CustomArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

from django.http import Http404

class CustomArticleDetailView2(DetailView):
    """
    控制只允许查看自己的文章，重写get_object方法
    """
    queryset = Article.objects.all().order_by('pub_date')
    template_name = 'blog/article_detail_v2.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super(CustomArticleDetailView2, self).get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        context = super(CustomArticleDetailView2, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



from django.views.generic.edit import (CreateView, UpdateView, DeleteView, FormView, ProcessFormView)

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body', 'author', 'create_date']
    # 此处template_name默认会选择'mvt_design/article_form.html'，所以此处不需要显示指定


from .forms import ArticleCreateForm
class CustomArticleCreateView(CreateView):
    """
    自定义CreateView
    """
    model = Article
    template_name = 'mvt_design/article_form.html'
    form_class = ArticleCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CustomArticleCreateView, self).form_valid(form)



class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body', 'create_date']
    template_name = 'mvt_design/article_update_form.html'


from .forms import ArticleUpdateForm
class CustomArticleUpdateView(UpdateView):
    model = Article
    template_name = ''
    form_class = ArticleUpdateForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CustomArticleUpdateView, self).form_valid(form)



from .forms import ContactForm

class ContactView(FormView):
    template_name = 'mvt_design/contact.html'  # 默认也为 'mvt_design/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        :param form:
        :return:
        """
        form.send_email()
        return super(ContactView, self).form_valid(form)


from django.urls import reverse_lazy

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('tasks:index_c_v21')


class CustomArticleDeleteView(DeleteView):
    # 定义模型的名称
    model = Article
    # 成功删除对象后的返回的URL
    success_url = reverse_lazy('tasks:index_c_v21') #返回到文章列表中

    def get_queryset(self):
        """
        筛选出用户自己的文章进行删除
        :return:
        """
        return self.model.objects.filter(author=self.request.user)# 此处是self.request.user不是self.request.user.username
