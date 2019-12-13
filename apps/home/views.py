from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

from apps.home.models import Gallery, Feedback
from apps.home.forms import ContactForm, GalleryForm, FeedbackForm


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            print(contact.message)
            subject = f'{contact.name} is trying to reach to you.'
            message = f'The messages sent by {contact.name} is \n {contact.message}. The  mail id is {contact.email}'
            send_from = settings.EMAIL_HOST_USER
            recipient = ['bisalgt@gmail.com',]
            send_mail(subject, message, send_from, recipient)
            contact.save()
            form = ContactForm()
    else:
        form = ContactForm()
    galleries = Gallery.objects.all()
    feedbacks = Feedback.objects.all()
    context = {'form': form, 'galleries': galleries, 'feedbacks': feedbacks}
    return render(request, 'home/home.html', context)


def gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = GalleryForm()
            return redirect("home")
    else:
        form = GalleryForm()
    galleries = Gallery.objects.all()
    context = {'form':form, 'galleries':galleries}
    return render(request, 'gallery/gallery_form.html', context)


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            return redirect("home")
    else:
        form = FeedbackForm()
    context = {"form":form, "message":"this is message"}
    return render(request, 'feedback/feedback_form.html', context)

# def gallery_list(request):
#     galleries = Gallery.objects.all()
#     paginator = Paginator(galleries, 6)
#     page = request.GET.get('page', 1)
#     try:
#         galleries = paginator.page(page)
#     except PageNotAnInteger:
#         galleries = paginator.page(1)
#     except EmptyPage:
#         galleries = paginator.page(paginator.num_pages)

#     context={'galleries':galleries}
#     return render(request, 'gallery/gallery_list.html', context)


class GalleryListView(ListView):
    model = Gallery
    template_name = "gallery/gallery_list.html"
    context_object_name = "galleries"
    ordering = ['-upload_date']
    paginate_by = 6