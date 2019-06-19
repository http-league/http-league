from django.urls import path
from . import views

urlpatterns = [
    # // TODO: SET UP HOME VIEW
    path('', views.home, name='home'),

    # // TODO: SET UP BLOG VIEW
    path('blog/', views.blog_index, name='blog'),

    #  // TODO: SET UP MAIN_ABOUT VIEW
    path('about/', views.about, name='main_about'),

    # // TODO: SETUP category view
    path('category/<int:category_id>/', views.category_detail, name='category'),

   
    # # Sites

    # // TODO: SETUP Site Views
    path('sites/<int:site_id>/', views.sites_detail, name='detail'),
    path('sites/create/',
         views.SiteCreate.as_view(), name='sites_create'),
    path('sites/<int:pk>/update/', views.SiteUpdate.as_view(), name='sites_update'),
    path('sites/<int:pk>/delete/', views.SiteDelete.as_view(), name='sites_delete'),



    # # Comments
    # TODO: ADD submissions/<int:submission_id>/add_comment/ that points to views.add_comment
    # path(comment/create/', views.CommentCreate.as_view(), name='comments_create'),
    # path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    # path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),

    ## Login/Profile paths
    # path('profile/', views.view_profile, name='view_profile'),
    # path('profile/edit', views.edit_profile, name='edit_profile'),
    # path('login', views.login, name'login'),
    # path('accounts/signup', views.signup, name='signup'),

    # Submission

    # # Submissions/Community
    # TODO: ADD community/ URL that points to views.SubmissionList.as_view() named 'submission_index'


    # TODO: ADD SUBMISSIONS URLS:

    #   TODO: submissions/<int:submission_id>/ that points to views.submissions_detail named 'submission_detail"

    #   TODO: submissions/create/ that points to views.SubmissionCreate.as_view() named 'submission_create"

    #   TODO: submissions/<int:pk>/delete/ that points to views.SubmissionDelete.as_view() named 'submission_delete"


    # OTHER

    # TODO: add dsuccess/ URL that points to views.success_delete

]
