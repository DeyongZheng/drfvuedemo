from rest_framework import serializers
from backend.models import Student, LearningHistory

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'lastname', 'firstname')

class LearningHistorySerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False, read_only=True)
    class Meta:
        model = LearningHistory
        fields = ('id', 'student', 'learningdate', 'questions', 'correct', 'elapsedtime')



