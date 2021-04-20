from django.db import models

"""
создание таблиц бд
"""
# Create your models here.
class Client(models.Model):
    SecondName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=70)
    IdCategory = models.ForeignKey('ClientCategory', on_delete=models.CASCADE)


class ClientCategory(models.Model):
    Name = models.CharField(max_length=50)


class Person(models.Model):
    SecondName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    IdClient = models.ForeignKey("Client", on_delete=models.CASCADE)
    IdPosition = models.ForeignKey('Position', on_delete=models.CASCADE)


class Position(models.Model):
    Name = models.CharField(max_length=50)
    Id_category = models.ForeignKey('PositionCategory', on_delete=models.CASCADE)


class PositionCategory(models.Model):
    Name = models.CharField(max_length=50)


class IndPers(models.Model):
    IdPerson = models.ForeignKey('Person', on_delete=models.CASCADE)
    IdIndPlan = models.ForeignKey('IndPlan', on_delete=models.CASCADE)


class Result(models.Model):
    IdIndPlan = models.ForeignKey('IndPlan', on_delete=models.CASCADE)
    IdIndPers = models.ForeignKey('IndPers', on_delete=models.CASCADE)


class IndPlan(models.Model):
    Name = models.CharField(max_length=50)


class Programm(models.Model):
    Lection = models.IntegerField
    Practice = models.IntegerField
    Test = models.BooleanField
    IdTopic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    IdIndPlan = models.ForeignKey('IndPlan', on_delete=models.CASCADE)


class ResTopic(models.Model):
    IdTopic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    IdResult = models.ForeignKey('Result', on_delete=models.CASCADE)


class Topic(models.Model):
    Name = models.CharField(max_length=50)
    IdCourse = models.ForeignKey('Course', on_delete=models.CASCADE)
    IdLevel = models.ForeignKey('Level', on_delete=models.CASCADE)


class Level(models.Model):
    Name = models.CharField(max_length=50)


class Course(models.Model):
    Name = models.CharField(max_length=50)
    Duration = models.CharField(max_length=10)
    Format = models.CharField(max_length=20)


class Test(models.Model):
    Date = models.DateField
    Number = models.IntegerField
    IdPerson = models.ForeignKey('Person', on_delete=models.CASCADE)


class AnswerTest(models.Model):
    IdTest = models.ForeignKey('Test', on_delete=models.CASCADE)
    IdVarAnswer = models.ForeignKey('VarAnsTest', on_delete=models.CASCADE)
    IdQuestion = models.ForeignKey('QuestionTest', on_delete=models.CASCADE)


class VarAnsTest(models.Model):
    Name = models.CharField(max_length=50)
    IdQuestion = models.ForeignKey('QuestionTest', on_delete=models.CASCADE)


class QuestionTest(models.Model):
    Question = models.CharField(max_length=50)
    IdTopic = models.ForeignKey('Topic', on_delete=models.CASCADE)


class Form(models.Model):
    Date = models.DateField
    Number = models.IntegerField
    IdPerson = models.ForeignKey('Person', on_delete=models.CASCADE)


class AnswerForm(models.Model):
    IdTopic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    IdVarAnswer = models.ForeignKey('VarAnsForm', on_delete=models.CASCADE)
    IdForm = models.ForeignKey('Form', on_delete=models.CASCADE)


class VarAnsForm(models.Model):
    Name = models.CharField(max_length=50)
