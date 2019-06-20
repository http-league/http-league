from django.urls import path
from . import views

urlpatterns = [
    # // TODO: SET UP HOME VIEW
    path('', views.home, name='home'),

    # // TODO: SET UP BLOG VIEW
    path('blog/', views.blog_index, name='blog'),
    # TODO: POSTING BLOG Posts
    #  // TODO: SET UP MAIN_ABOUT VIEW
    path('about/', views.about, name='main_about'),

    # // TODO: SETUP category view
    #     path('category/<int:category_id>/', views.category_detail, name='category'),

    # Sites

    # // TODO: SETUP Site Views
    path('sites/<int:site_id>/', views.sites_detail, name='sites_detail'),
    path('sites/create/', views.SiteCreate.as_view(), name='sites_create'),
    path('sites/<int:pk>/update/', views.SiteUpdate.as_view(), name='sites_update'),
    path('sites/<int:pk>/delete/', views.SiteDelete.as_view(), name='sites_delete'),

    # # Comments
    # TODO Create an add comment view
    # path('submissions/<int:submission_id>/add_comment/', views.add_comment, name='add_comment'),

    # path(comment/create/', views.CommentCreate.as_view(), name='comments_create'),
    # path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    # path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),

    # Login/Profile paths
    # path('profile/', views.view_profile, name='view_profile'),
    # path('profile/edit', views.edit_profile, name='edit_profile'),
    # path('login', views.login, name'login'),
    # path('accounts/signup', views.signup, name='signup'),

    # # Submissions/Community
    path('submissions/', views.SubmissionList.as_view(), name='submission_index'),

    # TODO Create a Submission_detail view
    path('submissions/<int:submission_id>/',
         views.submissions_detail, name='submission_detail'),

    path('submissions/create/', views.SubmissionCreate.as_view(),
         name='submission_create'),

    path('submissions/<int:pk>/delete/',
         views.SubmissionDelete.as_view(), name='submission_delete'),
    # OTHER

    # TODO Create a success_delete view
    # path('success/', views.success_delete, name='success'),

    path('sites/<int:site_id>/add_site_photo/',
         views.add_site_photo, name='add_site_photo'),

    path('submissions/<int:submission_id>/add_sub_photo/',
         views.add_sub_photo, name='add_sub_photo'),
]
