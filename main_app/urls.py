from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_index, name='blog'),
    path('about/', views.about, name='about'),
    path('sites/<int:site_id>/', views.sites_detail, name='detail'),
    # path('categories/<int:category_id>/', views.category_detail, name='category'),

    # path(r'^(?P<username>.+)/$', views.profile, name='profile'),

    # # Sites
    # path('sites/<int:site_id/create/', views.SiteCreate.as_view(), name='sites_create'),
    # path('sites/<int:pk>/update/', views.SiteUpdate.as_view(), name='sites_update'),
    # path('sites/<int:pk>/delete/', views.SiteDelete.as_view(), name='sites_delete'),

    # # Comments
    # path('comment/<int:comment_id/create/', views.CommentCreate.as_view(), name='comments_create'),
    # path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    # path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),
]
