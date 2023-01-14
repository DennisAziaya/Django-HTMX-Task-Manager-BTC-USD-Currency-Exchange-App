import json

import requests
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from frontend.models import BTCUSExchange, Task


def index(request):
    rates = BTCUSExchange.objects.all()
    tasks_list = Task.objects.all()

    # url = settings.API_ENDPOINT
    # api_key = settings.API_KEY
    # headers = {'X-CoinAPI-Key': api_key}
    # response = requests.get(url, headers=headers)
    # resps = response.json()
    # print(resps)
    # for resp in resps:
    #     BTCUSExchange.objects.create(
    #         time_period_start=resp['time_period_start'],
    #         time_period_end=resp['time_period_end'],
    #         time_open=resp['time_open'],
    #         time_close=resp['time_close'],
    #         rate_open=resp['rate_open'],
    #         rate_high=resp['rate_high'],
    #         rate_low=resp['rate_low'],
    #         rate_close=resp['rate_close'],
    #     )

    # tasks_lists = json.dumps(Task.objects.all, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    all_rates = json.dumps(list(BTCUSExchange.objects.values()), default=str)

    # print(all_rates)

    page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 5)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        "response": rates,
        "tasks": tasks,
        "rates": rates,
        "all_rates": all_rates,
    }
    return render(request, 'index.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    tasks_list = Task.objects.all()
    tasks_lists = json.dumps(list(Task.objects.values()), default=str)

    page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 5)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        "tasks": tasks,
        "tasks_lists": tasks_lists,
    }
    return render(request, 'index.html', context)


def search_task(request):
    search_term = request.POST['search']
    tasks_list = Task.objects.filter(title__icontains=search_term)

    page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 5)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        "tasks": tasks
    }
    return render(request, 'index.html', context)


def get_edit_task(request, pk):
    title = request.POST.get('title')
    task = get_object_or_404(Task, id=pk)
    task.title = title
    new_task = task.save()
    context = {
        "new_task": new_task
    }
    return render(request, 'index.html', context)


@require_http_methods(['GET', 'POST'])
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    tasks_list = Task.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 5)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
        context = {'task': task,
                   'tasks': tasks
                   }
        return render(request, 'index.html', context)
    context = {'task': task,
               'tasks': tasks
               }
    return render(request, 'edit.html', context)
