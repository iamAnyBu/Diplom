from django.db import models


# Create your models here.
class Client(models.Model):
    SecondName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=70)

    def __str__(self):
        return self.SecondName


class Department(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Position(models.Model):
    Name = models.CharField(max_length=50)
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Person(models.Model):
    SecondName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Client = models.ForeignKey("Client", on_delete=models.CASCADE)
    Position = models.ForeignKey('Position', on_delete=models.CASCADE)

    def __str__(self):
        return self.SecondName


class Test(models.Model):
    Data = models.DateTimeField()
    Number = models.IntegerField()
    Person = models.ForeignKey('Person', on_delete=models.CASCADE)


class TestAnswer(models.Model):
    Test = models.ForeignKey('Test', on_delete=models.CASCADE)
    VarAnswer = models.ForeignKey('VarAnswer', on_delete=models.CASCADE)
    Question = models.ForeignKey('Question', on_delete=models.CASCADE)
    Level = models.ForeignKey('Level', on_delete=models.CASCADE)

    def __str__(self):
        return self.Test


class VarAnswer(models.Model):
    Name = models.CharField(max_length=80)
    Question = models.ForeignKey('Question', on_delete=models.CASCADE)
    Point = models.IntegerField()

    def __str__(self):
        return self.Name


class Question(models.Model):
    Wording = models.TextField()
    Topic = models.ForeignKey('Topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.Wording


class Form(models.Model):
    Data = models.DateTimeField()
    Number = models.IntegerField()
    Person = models.ForeignKey('Person', on_delete=models.CASCADE)


class Topic(models.Model):
    Name = models.CharField(max_length=80)
    Description = models.TextField()
    Level = models.ForeignKey('Level', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class FormAnswer(models.Model):
    Form = models.ForeignKey('Form', on_delete=models.CASCADE)
    VarAnswer = models.ForeignKey('FormVarAnswer', on_delete=models.CASCADE)
    Topic = models.ForeignKey('Topic', on_delete=models.CASCADE)




class FormVarAnswer(models.Model):
    Name = models.CharField(max_length=80)

    def __str__(self):
        return self.Name

class FinishTest(models.Model):
    Data = models.DateTimeField()
    Number = models.IntegerField()



class Level(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class Program(models.Model):
    Name = models.CharField(max_length=80)
    Level = models.ForeignKey('Level', on_delete=models.CASCADE)
    Topic = models.ManyToManyField(Topic)
    Person = models.ManyToManyField(Person)
    FinishTest = models.OneToOneField(FinishTest, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.Name

class FQuestion(models.Model):
    Wording = models.TextField()


class FVarAnswer(models.Model):
    Name = models.CharField(max_length=80)
    FQuestion = models.ForeignKey('FQuestion', on_delete=models.CASCADE)
    Point = models.IntegerField()


class FResult(models.Model):
    Finished = models.BooleanField()


class FTestAnswer(models.Model):
    FinishTest = models.ForeignKey('FinishTest', on_delete=models.CASCADE)
    FVarAnswer = models.ForeignKey('FVarAnswer', on_delete=models.CASCADE)
    FQuestion = models.ForeignKey('FQuestion', on_delete=models.CASCADE)
    FResult = models.ForeignKey('FResult', on_delete=models.CASCADE)






