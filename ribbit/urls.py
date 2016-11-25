from django.conf.urls import url
from django.contrib import admin
from ribbit_app.views import index, login_view, logout_view, signup, submit, public, users, follow

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index), # root
    url(r'^login$', login_view), # login
    url(r'^logout/$', logout_view), # logout
    url(r'^signup$', signup), # signup
    url(r'^ribbits$', public),
    url(r'^submit$', submit),
    url(r'^users/$', users),
    url(r'^users/(?P<username>\w{0,30})/$', users),
    url(r'^follow$', follow),

]
