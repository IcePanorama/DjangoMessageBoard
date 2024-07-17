from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

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


def submit(request):
    # Should handle cases where users simply navigate to the /submit/ url
    if request.method != "POST":
        return redirect("board:index")

    # TODO: Handle blank posts
    # should probably be done when the user tries to click the submit button
    # rather than in here
    if request.POST.get("post_text", "").strip() == "":
        return redirect("board:index")

    new_thread = Thread.objects.create(
        date_posted=timezone.now(), post_text=request.POST.get("post_text"),
    )

    if request.POST.get("title", None):
        new_thread.title = request.POST["title"]

    if request.POST.get("name", None):
        new_thread.name = request.POST["name"]

    new_thread.save()
    return redirect("board:thread", thread_id=new_thread.id)
