from django import forms
from .models import *
from processAuth.models import userModel

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'responsable', 'description', 'expire_at',)
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'expire_at': forms.DateTimeInput(),
        }

class flujoForm(forms.ModelForm):
    class Meta:
        model = FlujoTareas
        fields = ('nombre', 'responsables', 'tareas', 'descripcion', 'plazo_maximo',)
        responsables: forms.ModelMultipleChoiceField(queryset=userModel.objects.all())
        tareas: forms.ModelMultipleChoiceField(queryset=Task.objects.all())
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),       
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'plazo_maximo': forms.DateTimeInput(),
        }


class subordinadaForm(forms.ModelForm):
    class Meta:
        model = TareaSubordinada
        fields = ('name', 'responsable', 'description', 'expire_at',)
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'expire_at': forms.DateTimeInput(),
        }

class processForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class unidadForm(forms.ModelForm):
    class Meta:
        model = UnidadInterna
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class commentForm(forms.ModelForm):
    class Meta:
        model = Rejectcomment
        fields = ('reason',)
        widgets = {
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }

class problemaForm(forms.ModelForm):
    class Meta:
        model = ProblemaTarea
        fields = ('titulo', 'responsable', 'descripcion')
        widgets = {

            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),            
        }