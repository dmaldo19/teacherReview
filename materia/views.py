from django.views import generic
from .models import Materia

# Create your views here.
class MateriaView(generic.ListView):
    template_name = 'materia/mostrar_materia.html'

    def get_queryset(self):
        queryset = Materia.objects.order_by('-nombre')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset