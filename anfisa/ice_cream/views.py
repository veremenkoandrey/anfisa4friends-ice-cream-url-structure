# from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     template = 'ice_cream/index.html'
#     return render(request, template)


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = "ice_cream/index.html"
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = "Анфиса для друзей"
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        "title": title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        "text": "Главная страница",
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def ice_cream_list(request):
    template = "ice_cream/ice_cream_list.html"
    title = "Список мороженого"
    text = "Вложенная страница"
    context = {
        "title": title,
        "text": text,
    }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    template = "ice_cream/ice_cream_detail.html"
    return render(request, template)
