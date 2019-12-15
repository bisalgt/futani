from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


from apps.home.models import Gallery, Feedback
from apps.home.forms import ContactForm, GalleryForm, FeedbackForm


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
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

@login_required
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

@login_required
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


class GalleryListView(ListView):
    model = Gallery
    template_name = "gallery/gallery_list.html"
    context_object_name = "galleries"
    ordering = ['-upload_date']
    paginate_by = 6

@login_required
def gallery_delete(request, id):
    gallery_object = Gallery.objects.get(id=id).delete()
    return redirect("gallery_list")


@login_required
def feedback_delete(request, id):
    feedback_object_delete = Feedback.objects.get(id=id).delete()
    return redirect("home")


@login_required
def gallery_update(request, id):
    object = Gallery.objects.get(id=id)
    form = GalleryForm(request.POST or None,request.FILES or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect("gallery_list")
    return render(request, 'gallery/gallery_form.html', {'form':form})



@login_required
def feedback_update(request, id):
    object = get_object_or_404(Feedback, id=id)
    form = FeedbackForm(request.POST or None,request.FILES or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'feedback/feedback_form.html', {'form':form})