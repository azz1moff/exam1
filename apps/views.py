from django.views.generic import ListView

from apps.models import Contact


class ContactListView(ListView):
    queryset = Contact.objects.order_by('-id')
    template_name = 'index.html'
    context_object_name = 'contacts'
