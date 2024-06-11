from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse_lazy
from .models import Publicacion
from .forms import ResenaForm
from .models import Profesor, Materia
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PublicacionView(generic.ListView):
    template_name = 'publicacion/index.html'

    def get_queryset(self):
        #el signo de menos es para que retorne los mas recientes
        return Publicacion.objects.order_by('-fecha')[:5]

class ProfesorView(generic.DetailView):
    model = Profesor
    template_name = 'publicacion/profesor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesor = self.get_object()
        context['publicacion_list'] = Publicacion.objects.filter(profesor=profesor)
        context['general_rating'] = profesor.get_general_rating()
        context['rubric_averages'] = profesor.get_rubric_averages()
        return context
    
class MateriaView(generic.DetailView):
    model = Materia
    template_name = 'publicacion/materia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materia = self.get_object()
        context['publicacion_list'] = Publicacion.objects.filter(materia=materia)
        return context

class ResenaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Publicacion
    form_class = ResenaForm
    template_name = 'publicacion/crear_resena.html'
    success_url = reverse_lazy('publicacion:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual como autor de la reseña
        return super().form_valid(form)