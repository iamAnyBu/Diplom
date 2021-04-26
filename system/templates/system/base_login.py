<!DOCTYPE html>
<body lang="en">
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
        <a class="s7" href="{% url 'logout' %}">Выход</a>
        <a class="s3" href="#">Личный кабинет</a>

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
         .s7{
            margin: 10px;
            text-decoration: none;
            color: #333333;
            float: right;

        }
        .s3{
            margin: 10px;
            text-decoration: none;
            color: #333333;
            float: right;
        }
        .s3:hover{
            color: #2f6abf;
        }
        .s4{
            font-family: Circe;
            font-size: 50px;
            font-weight: bolder;
            margin-top: 200px;
            margin-left: 150px;

        }
        .s5{
            font-family: Circe;
            font-size: 18px;
            height: 60px;
            width: 200px;
            border-radius: 100px;
            background: #2f6abf;
            color: #f6f6f6;
            border: none;
            position: absolute;
            left: 150px;
        }
        .s5:hover{
            background: #0e2c96;
        }
        .s6{
            margin-right: 100px;
            float: right;
            width: 600px;
        }

    </style>
    <div class="s6" align="right">
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://assets6.lottiefiles.com/packages/lf20_0T1oLM.json"  background="transparent"  speed="1"    loop  autoplay></lottie-player>
    </div>
    <p class="s4" align="left" >Давайте развиваться вместе!</p>

    <form action="#">
        <p><button class="s5">Личный кабинет</button></p>
    </form>
</body>
</html>
