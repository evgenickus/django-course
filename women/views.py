from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import slugify

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
  {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
  {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
  {'id': 2, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},

]

def index(request):
  data = {
    'title': 'Главная страница',
    'menu': menu,
    'posts': data_db,
    }
  return render(request, 'women/index.html', data)

def about(request):
  return render(request, 'women/about.html', {'title': "О сайте"})

def categories(requist, cat_id):
  return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
  return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
  if year > 2023:
    uri = reverse('cats', args=('sport', ))
    return HttpResponsePermanentRedirect(uri)
    # Http404()
  return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request, exception):
  return HttpResponseNotFound("<h1>Страница не найдена</h1>")