""""
регистрация моделей в админке
"""
from django.contrib import admin
from .models import Client
from .models import Person
from .models import ClientCategory
from .models import IndPers
from .models import Result
from .models import IndPlan
from .models import Programm
from .models import ResTopic
from .models import Topic
from .models import Level
from .models import Course
from .models import Test
from .models import AnswerTest
from .models import VarAnsTest
from .models import QuestionTest
from .models import Form
from .models import VarAnsForm
from .models import AnswerForm
from .models import Position
from .models import PositionCategory

# Register your models here.

admin.site.register(Client)
admin.site.register(Person)
admin.site.register(ClientCategory)
admin.site.register(IndPers)
admin.site.register(Result)
admin.site.register(IndPlan)
admin.site.register(Programm)
admin.site.register(ResTopic)
admin.site.register(Topic)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(AnswerTest)
admin.site.register(VarAnsTest)
admin.site.register(QuestionTest)
admin.site.register(Form)
admin.site.register(VarAnsForm)
admin.site.register(AnswerForm)
admin.site.register(Position)
admin.site.register(PositionCategory)
