<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!--<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">-->
    <title>S.AI</title>
</head>
    <div class="s1">
        <a class="s2" href="{% url 'base_login' %}" >S.AI</a>
    </div>
 <style>
        .s1{
            margin: 20px;
            padding: 10px;
            font-family: Circe;
            font-size: 18px;

    }
        .s2{
            font-weight: bold;
            font-family: Circe;
            font-size: 24px;
            text-decoration: none;
            color: #333333;

        }
        .s2:hover{
            color: black;
        }
        .r1{

            font-family: Circe;
            font-size: 18px;
            height: 60px;
            width: 200px;
            border-radius: 100px;
            background: #2f6abf;
            color: #f6f6f6;
            border: none;
            position: absolute;
            left: 670px;
            margin-top: 30px;

        }
         .r2{

            font-family: Circe;
            font-size: 18px;
            height: 60px;
            width: 200px;
            border-radius: 100px;
            background: #2f6abf;
            color: #f6f6f6;
            border: none;
            position: absolute;
            left: 670px;
            margin-top: 150px;

        }
        button:hover{
           background: #0e2c96;
        }
</style>
<h1 align="center" style="font-family: Circe; margin-top: 100px">Кто вы?</h1>
<p align="center" style="font-family: Circe;color: dimgray">Выберите подходящую Вам должность</p>
    <form name="b1" action="{% url 'shef' %}">
        <button type="submit" class="r1" >Работодатель</button>
    </form>
    <form name="b2" action="{% url 'empl' %}">
        <button type="submit" class="r2">Сотрудник</button>
    </form>

