from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.mail import send_mail


from apps.contact.models import Contact
from apps.contact.forms import ContactForm

from apps.gallery.models import Gallery


print("inside views")
# class ContactCreateView(CreateView):
#     print("inside contact create view")
#     model =  Contact
#     template_name = "base.html"
#     form_class = ContactForm
    
    
    
#     def form_valid(self, form):
#         print('valid')
#         contact = form.save(commit=False)
#         contact.save()
#         return super(ContactCreateView, self).form_valid(form)

#     def form_invalid(self, form):
#         print('Invalid form datas', form.errors)
#         return super(ContactCreateView, self).form_invalid(form)

def form_and_galleryimages(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            print(contact)
            contact.save()
    else:
        form = ContactForm()
    galleries = Gallery.objects.all()
    context = {'form': form, 'galleries': galleries}
    return render(request, 'base.html', context)


# ContactCreateView()

# if __name__ == "__main__":
#     print("contact create view")