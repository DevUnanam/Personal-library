from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/face-login/', views.face_login_view, name='face_login'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Diary
    path('diary/new/', views.diary_entry_view, name='diary_new'),
    path('diary/<int:entry_id>/', views.diary_entry_view, name='diary_entry'),
    path('api/diary/list/', views.diary_list_api, name='diary_list_api'),
    path('api/diary/save/', views.diary_save_api, name='diary_save_api'),
    path('api/diary/delete/<int:entry_id>/', views.diary_delete_api, name='diary_delete_api'),
    path('api/diary/by-date/', views.diary_by_date_api, name='diary_by_date_api'),

    # Library
    path('api/library/upload/', views.library_upload_api, name='library_upload_api'),
    path('api/library/list/', views.library_list_api, name='library_list_api'),
    path('api/library/delete/<int:item_id>/', views.library_delete_api, name='library_delete_api'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('api/profile/delete-face/', views.delete_face_data_api, name='delete_face_data_api'),

    # Search
    path('search/', views.search_view, name='search'),
]
