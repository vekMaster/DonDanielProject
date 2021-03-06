from apps.perro.forms import FormularioPerro, FormularioVeterinario, FormularioMadre, FormularioPadre, FormularioSuplemento, FormularioNivelPersonalizado, FormularioDieta, FormularioAlimentacion
from apps.perro.models import Perro, Veterinario, Madre, Padre, Suplemento, NivelEntrenamiento, HorarioDieta, Alimentacion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
# Create your views here.

class RegistrarPerro(CreateView):
    """
    Clase encargada de registrar el perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Perro
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioPerro
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroPerro.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:listar_perro')

class RegistrarVeterinario(CreateView):
    """
    Clase encargada de registrar el veterinario en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Veterinario
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioVeterinario
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroVeterinario.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_perro')

class RegistrarMadre(CreateView):
    """
    Clase encargada de registrar la madre de un perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Madre
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioMadre
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroMadre.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_perro')

class RegistrarPadre(CreateView):
    """
    Clase encargada de registrar el padre de un perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Padre
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioPadre
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroPadre.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_perro')

class RegistrarSuplemento(CreateView):
    """
    Clase encargada de registrar suplementos de un perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Suplemento
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioSuplemento
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroSuplemento.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_perro')

class RegistrarNivelPersonalizado(CreateView):
    """
    Clase encargada de registrar niveles personalizados de adiestramiento de un perro
    """
    #se ingresa qué modelo se utilizará para el registro
    model = NivelEntrenamiento
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioNivelPersonalizado
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroNivelPersonalizado.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_perro')

class RegistrarDieta(CreateView):
    """
    Clase encargada de registrar niveles personalizados de adiestramiento de un perro
    """
    #se ingresa qué modelo se utilizará para el registro
    model = HorarioDieta
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioDieta
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroDieta.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_perro')


class RegistrarAlimentacion(CreateView):
    """
    Clase encargada de registrar niveles personalizados de adiestramiento de un perro
    """
    #se ingresa qué modelo se utilizará para el registro
    model = Alimentacion
    #se indica que formulario va a dar soporte a la acción de registro
    form_class = FormularioAlimentacion
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagRegistroAlimentacion.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:registrar_dieta')

class ActualizarInformacionPerro(UpdateView):
    """
    Clase encargada de actualizar la información del Perro en la base de datos
    """
    #se ingresa qué modelo se utilizará para la actualización de la información
    model = Perro
    #se indica que formulario va a dar soporte a la acción de actualización de la información
    form_class = FormularioPerro
    #se indica que template va a gestionar el registro
    template_name = 'perro/pagActualizarPerro.html'
    #se indica cual será la url de finalización
    success_url= reverse_lazy('perro:listar_perro')

class EliminarPerro(DeleteView):
    """
    Clase encargada de eliminar el Perro de la base de datos
    """
    #se ingresa qué modelo se utilizará para el borrado de Perro
    model = Perro
    #se indica que template va a gestionar el borrado
    template_name = 'Perro/pagEliminarPerro.html'
    #se indica cual será la url de finalización
    success_url=reverse_lazy('perro:listar_perro')

class ListarPerro(ListView):
    """
    Clase encargada de listar los perros de la base de datos
    """
    #se ingresa qué modelo se utilizará para listar los perros
    model = Perro
    #se indica que template va a gestionar el listador de los perros
    template_name = 'perro/pagListarPerro.html'
    def get_queryset(self):
        #pylint:disable=E1101
        return self.model.objects.all().order_by('id')