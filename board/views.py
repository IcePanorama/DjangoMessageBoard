from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Thread


def index(request):
    latest_thread_list = Thread.objects.order_by("-date_posted")
    context = {"latest_thread_list": latest_thread_list}
    return render(request, "board/index.html", context)


def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    return render(request, "board/thread.html", {"thread": thread})


def archive(request):
    return HttpResponse("You're looking at the archive.")
