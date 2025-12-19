from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Passport

class PassportCreateView(CreateView):
    model = Passport
    fields = ['series', 'number']
    template_name = 'passport/form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

