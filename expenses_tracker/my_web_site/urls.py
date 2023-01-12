from django.urls import path

from expenses_tracker.my_web_site.views import show_index, create_expense, edit_expense, delete_expense, show_profile, \
    edit_profile, delete_profile

urlpatterns = (
    path('', show_index, name='show index'),

    path('create/', create_expense, name='create expense'),
    path('edit/<id>/', edit_expense, name='edit expense'),
    path('delete/<id>/', delete_expense, name='delete expense'),

    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
