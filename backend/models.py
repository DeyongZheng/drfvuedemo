# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.lastname, self.firstname)

    class Meta:
        db_table = 'students'
        managed = False

class LearningHistory(models.Model):
    id = models.AutoField(primary_key=True)
    #student = models.OneToOneField(Student, on_delete=models.DO_NOTHING, primary_key=False)
    #student = models.ForeignKey(Student, models.DO_NOTHING, db_column='student', blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, primary_key=False)
    learningdate = models.DateField(verbose_name="学習日")
    questions = models.IntegerField(blank=True, null=True, verbose_name="解いた問題数")
    correct = models.IntegerField(blank=True, null=True, verbose_name="正解数")
    elapsedtime = models.IntegerField(default=0, verbose_name="学習時間")

    def __unicode__(self):
        return u'学習日:%s 名前:%s 解いた問題数:%d 正解数:%d 学習時間:%d' % (
            self.learningdate, self.student, self.questions, self.correct, self.elapsedtime
        )

    class Meta:
        db_table = 'history'
        managed = False
        unique_together = (('student', 'learningdate'),)

