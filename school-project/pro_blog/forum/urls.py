from . import views
from . import views_second
from django.conf.urls import include, url

app_name = 'forum'

urlpatterns = [
	url(r'^posts/$', views.las_posts, name='las-posts'), # the post's user and date
	url(r'^posts/subject/(?P<slug>[\w-]+)/$', views.subject, name='subject'), #done
	url(r'^posts/grade/(?P<slug>[\w-]+)/$', views.grade, name='grade'), #done
	url(r'^posts/hottest-posts/$', views.hot_posts, name='hot-posts'), # the proper logic
	url(r'^posts/unanswered-posts/$', views.unanswered, name='answered'),#done
	url(r'^posts/most-liked/$', views.most_liked, name='most-liked'), #done
	
	url(r'^post/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.detail2, name='detail'), # comment section, ajax 

	url(r'^edit/(?P<pk>\d+)/post/$', views.post_update, name='post-edit'),#done
	url(r'^flag/(?P<pk>[0-9]+)/post/$', views_second.post_flag, name='flag-post'),#done

	url(r'^post/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/like/(?P<user_pk>[0-9]+)/$', views_second.like_post_redirect, name='like_post_redirect'), #done
	url(r'^post-id/(?P<pk>[0-9]+)/comment-id/(?P<pk_comment>[0-9]+)/right/$', views_second.make_right, name='make_right'), #done
	url(r'^post-pk/(?P<pk>[0-9]+)/delete/$', views_second.delete_post, name='delete-post'), # done
	url(r'^my-comment-pk/(?P<pk>[0-9]+)/delete/$', views_second.delete_comment, name='delete-comment'), # done
	url(r'^comment/(?P<pk>[0-9]+)/like/$', views_second.like_comment, name='comment-like'), #done
	url(r'^comment/(?P<pk>[0-9]+)/right/$', views_second.mark_comment, name='mark-comment'), # done
	url(r'^comment/flag/(?P<pk>[0-9]+)/$', views_second.comment_flag, name='comment-flag'), # done
	url(r'^comment/(?P<pk>[0-9]+)/edit$', views.comment_edit, name='comment-edit'),
	url(r'^post/flag/(?P<pk>\d+)/$', views_second.post_flag, name='post-flag'),

	url(r'^create/$', views.create_post, name='create_post'), #done
]