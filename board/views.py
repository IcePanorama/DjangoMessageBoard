from django.shortcuts import render
from django.http import HttpResponse

from .models import Thread


def index(request):
    latest_thread_list = Thread.objects.order_by("-date_posted")
    context = {"latest_thread_list": latest_thread_list}
    return render(request, "board/index.html", context)


def thread(request, thread_id):
    return HttpResponse("You're looking at thread %s." % thread_id)


def archive(request):
    return HttpResponse("You're looking at the archive.")
