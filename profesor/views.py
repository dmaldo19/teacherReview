from django.views import generic
from .models import Profesor

# Create your views here.
class ProfesorView(generic.ListView):
    template_name = 'profesor/mostrar_profesores.html'

    def get_queryset(self):
        queryset = Profesor.objects.order_by('-nombre')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset
    
