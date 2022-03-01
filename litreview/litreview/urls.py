"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import flux.views
import follow.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket/upload/', flux.views.ticket_upload, name='ticket_upload'),
    path('review/upload/', flux.views.review_upload, name='review_upload'),
    path('review/<int:ticket_id>/answer/', flux.views.review_answer, name='review_answer'),
    path('', flux.views.home, name='home'),
    path('posts/', flux.views.own_posts, name='own_posts'),
    path('ticket/<int:ticket_id>/delete', flux.views.ticket_delete, name='ticket_delete'),
    path('review/<int:review_id>/delete', flux.views.review_delete, name='review_delete'),
    path('ticket/<int:ticket_id>/update', flux.views.ticket_update, name='ticket_update'),
    path('review/<int:review_id>/update', flux.views.review_update, name='review_update'),
    path('follow/', follow.views.follow_user, name='follow_manager'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
