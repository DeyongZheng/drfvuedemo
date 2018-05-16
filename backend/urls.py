from django.conf.urls import url
from backend import views
from backend.views import StudentListViewset, LearningHistoryListViewset
from rest_framework import renderers

student_list = StudentListViewset.as_view({
    'get': 'list'
})

student_detail = StudentListViewset.as_view({
    'get': 'retrieve'
})

history_list = LearningHistoryListViewset.as_view({
    'get': 'list'
})

history_detail = LearningHistoryListViewset.as_view({
    'get': 'retrieve'
})



urlpatterns = [
    url(r'^students/$', student_list, name="student_list"),
    url(r'^students/(?P<pk>[0-9]+)/$', student_detail, name="student_detail"),
    url(r'^history/$', history_list, name="history_list"),
    url(r'^history/(?P<pk>[0-9]+)/$', history_detail, name="history_detail"),
]


