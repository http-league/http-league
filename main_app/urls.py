from django.urls import path
from . import views

urlpatterns = [
    # TODO: SET UP HOME VIEW  -- done
    path('', views.home, name='home'),

    # TODO: SET UP BLOG VIEW --
    path('blog/', views.blog_index, name='blog'),

    #  TODO: SET UP MAIN_ABOUT VIEW --
    path('about/', views.about, name='main_about'),


    # path('category/<int:category_id>/', views.category_detail, name='category'),

   
    # # Sites
    path('sites/<int:sites_id>/', views.sites_detail, name='detail'),
    # path('sites/<int:site_id/create/', views.SiteCreate.as_view(), name='sites_create'),
    # path('sites/<int:pk>/update/', views.SiteUpdate.as_view(), name='sites_update'),
    # path('sites/<int:pk>/delete/', views.SiteDelete.as_view(), name='sites_delete'),

    # # Comments
    # path('comment/<int:comment_id/create/', views.CommentCreate.as_view(), name='comments_create'),
    # path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    # path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),

    ## Login/Profile paths
    # path('profile/', views.view_profile, name='view_profile'),
    # path('profile/edit', views.edit_profile, name='edit_profile'),
    # path('login', views.login, name'login'),
    # path('accounts/signup', views.signup, name='signup'),

    # Submission
]
