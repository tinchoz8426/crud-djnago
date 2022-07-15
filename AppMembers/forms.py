from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Correo electronico")
    first_name = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pone el nombre'}))
    last_name = forms.CharField(max_length=50, label="Apellido")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2")

        
        #help_texts = {"username": None, "password1": "None", "password1": "None"} # No me funciona con los password

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    