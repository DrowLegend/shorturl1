from django.shortcuts import render, redirect
from shortrurlapp.forms import UrlForm
from shortrurlapp.models import ShortUrls
from .shortner import Shortner

# Create your views here.


def base(request):
    return redirect(home)


def home(request):
    form = UrlForm(request.POST)
    a = ''
    all_url = ShortUrls.objects.all()

    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = Shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'shorturlapp/home.html', {
        'form': form,
        'a': a,
        'all_url': all_url,
    })


def make(request, token):
    long_url = ShortUrls.objects.filter(short_url=token)[0]
    return redirect(long_url.url)




# def home(request):
#     form = UrlForm()
#
#     if request.method == "POST":
#         form = UrlForm(request.POST, request.FILES)
#         if form.is_valid():
#             url = form.save(commit=False)
#             url.save()
#             return redirect(home)
#     return render(request, 'shorturlapp/home.html', {
#         'form': form,
#     })