from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^loginpage$', views.loginpage),
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^users/new$', views.admin_new), #admin only new
    url(r'^dashboard/admin$', views.dash_admin),
    url(r'^users/show/(?P<id>\d+)$', views.users_show),
    # url(r'^users/show/fake$', views.users_show),
    url(r'^logout$', views.logout),
    # url(r'^users/edit/fake$', views.admin_edit), #fake admin edit page
    url(r'^users/edit/(?P<id>\d+)$', views.admin_edit), #admin only edit
    url(r'^update/(?P<id>\d+)$', views.update_user), #admin only edit







    url(r'^users/edit$', views.users_edit), #users edit page
    url(r'^dashboard$', views.dashboard),





    url(r'^users/create_comment$', views.create_comment),
    url(r'^users/create_message$', views.create_message),
    # url(r'^admin/remove$', views.admin_remove),
    # url(r'^admin/create$', views.admin_create),
  ]