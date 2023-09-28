from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import UserForm
import logging

from magazin.models import Order
from unicodedata import decimal
from .models import User, Order, Product

logger = logging.getLogger(__name__)


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def my_view(request):
    context = {"name": "John"}
    return render(request, "magazin/index.html", context)


class TemplIf(TemplateView):
    template_name = "magazin/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['id_user'])
        orders = Order.objects.filter(user=user).all()
        context['order'] = orders
        return context

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            logger.info(f'Получили {name=}, {email=}, {phone=}, {address=}.')
    else:
        form = UserForm()
        return render(request, 'myapp4/user_form.html', {'form': form})