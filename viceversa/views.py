from django.shortcuts import render

def home(requests):
    return render(requests, 'home.html')

def reverse(requests):
    user_text = requests.GET['usertext'] # Сохраняем в переменную запрос пользователя
    words = len(user_text.split()) # Считаем кол-во слов в тексте
    reversed_text = user_text[::-1]
    # Возвращаем страницу, и 2 переменных исходный текст и перевернутый
    return render(requests, 'reverse.html',{'usertext': user_text, 'reversedtext':reversed_text, 'count_text':words})
