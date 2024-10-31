from django.shortcuts import render, redirect

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("users:login")
    context = {}
    return render(request, "MyChat/chatPage.html", context)