from csv import field_size_limit
from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from tempfile import template
from turtle import mode
from django.shortcuts import render
from .models import Usuario
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy


# Create your views here.
class CreateUser(CreateView):
    model = Usuario
    fields = ['id_usuario', 'password','nombre', 'email', 'tel', 'balance']
    success_url = reverse_lazy('user')

    def form_valid(self,form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()
        return super().form_valid(form)

class UpdateUser(UpdateView):
    model = Usuario
    fields = ['id_usuario', 'nombre', 'email', 'tel', 'balance']
    success_url = reverse_lazy('user')

class DeleteUser(DeleteView):
    model = Usuario
    success_url = reverse_lazy('user')

class VistaUsers(TemplateView):
    template_name = 'portfolio/users.html'

    def get_context_data(self, **kwargs):
        context = super(VistaUsers, self).get_context_data(**kwargs)
        filtrado = self.request.GET.get('filtrado','')
        if filtrado:
            users = Usuario.objects.filter(nombre__icontains=filtrado)
        else:
            users = Usuario.objects.all()
        
        paginador = Paginator(users,20)
        pagina = self.request.GET.get('page',1)
        context['users'] = paginador.get_page(pagina)

        return context

    