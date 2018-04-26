from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^loginpage$', views.loginpage),
    url(r'^registration$', views.registration),
    url(r'^users/show/(?P<id>\d+)$', views.users_show),
    url(r'^users/show/message/(?P<receiver_id>\d+)$', views.users_show_message),
    url(r'^dashboard/admin$', views.dash_admin),
    url(r'^admin/add/user$', views.admin_newuser), #admin only add new user
    url(r'^users/new$', views.admin_new), #admin only add new user
    url(r'^users/edit/(?P<id>\d+)$', views.admin_edit), #admin only edit user
    url(r'^logout$', views.logout),
    url(r'^update/(?P<id>\d+)$', views.update_user), #admin only edit
    url(r'^update/self/(?P<id>\d+)$', views.update_user_self), #user only edit
    url(r'^updatepw/(?P<id>\d+)$', views.update_user_pw), #admin only edit
    url(r'^updatepw/self$', views.update_user_pw_self), #user only edit
    url(r'^remove/(?P<id>\d+)$', views.remove), #admin only edit
    url(r'^users/edit/$', views.users_edit), #users edit page
    url(r'^dashboard$', views.dashboard),
    url(r'^message/save/(?P<receiver_id>\d+)$', views.message_save),
    url(r'^users/comment_save/(?P<message_id>\d+)$', views.comment_save),






    url(r'^users/create_comment$', views.create_comment),
    # url(r'^admin/remove$', views.admin_remove),
    # url(r'^admin/create$', views.admin_create),
  ]
