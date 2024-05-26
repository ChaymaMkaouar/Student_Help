from django import forms
from .models import User
from .models import Recommandation 
from .models import Logement 
from .models import Stage
from .models import Transport
from .models import Evènement ,Poste
from .models import Enseignant,Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import Commentaire


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Adresse e-mail')
     # Champ pour l'image de profil

class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email','image')

        
class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = "__all__" 
class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = "__all__" 

class RecommandationForm(forms.ModelForm):
    class Meta:
        model = Recommandation
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LogementForm(forms.ModelForm):
    class Meta:
        model= Logement
        exclude = ['user']

class StageForm(forms.ModelForm):
    class Meta:
        model= Stage
        exclude = ['user']

class TransportForm(forms.ModelForm):
    class Meta:
        model= Transport
        exclude = ['user']

class EvènementForm(forms.ModelForm):
    class Meta:
        model= Evènement
        exclude = ['user']

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields ="__all__"


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

class LikeForm(forms.Form):
    # Vous pouvez ajouter d'autres champs au besoin
    class Meta:
        model= Contact
        fields ="__all__"

        

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields ="__all__"