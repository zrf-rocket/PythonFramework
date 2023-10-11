from django.urls import path
from . import views

# namespace
app_name = "tasks"

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blogs'),
    path('blog/article/<int:id>', views.article_detail, name='article_detail'),
    # 使用CBV重写上面的FBV
    # ListView
    path('blog_c/', views.IndexView.as_view(), name='index_c'),
    path('blog_c_v2/', views.CustomIndexView.as_view(), name='index_c_v21'),
    path('blog_c_v3/', views.CustomIndexView2.as_view(), name='index_c_v3'),
    # DetailView
    path('blog_detail/<int:pk>', views.ArticleDetailView.as_view(), name='blog_detail'),
    path('blog_detail2/<int:pk>', views.CustomArticleDetailView.as_view(), name='blog_detail2'),
    path('blog_detail3/<int:pk>', views.CustomArticleDetailView2.as_view(), name='blog_detail3'),
    # CreateView
    path('blog_create/', views.ArticleCreateView.as_view(), name='blog_create'),
    # UpdateView
    path('blog_update/<int:pk>', views.ArticleUpdateView.as_view(), name='blog_update'),
    # DeleteView
    path('blog_delete/<int:pk>', views.ArticleDeleteView.as_view(), name='blog_delete'),
    path('blog_delete2/<int:pk>', views.CustomArticleDeleteView.as_view(), name='blog_delete2'),

]
