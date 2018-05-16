# -*- coding: utf-8 -*-
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from backend.models import Student, LearningHistory
from backend.serializers import StudentSerializer, LearningHistorySerializer

class LearningHistoryFilter(django_filters.FilterSet):
    learningdate = django_filters.DateFilter(name='learningdate', lookup_expr='exact')

    class Meta:
       model = LearningHistory
       fields = ('learningdate',)

class StudentListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LearningHistoryListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = LearningHistory.objects.all()
    serializer_class = LearningHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = LearningHistoryFilter
    filter_fields = ('learningdate')

