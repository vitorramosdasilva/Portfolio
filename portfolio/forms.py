from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        min_length=3,
        max_length=50,
        help_text="Nome Preenchimento Obrigatório",
        widget=forms.TextInput(attrs={'placeholder': 'Insira seu Nome'})
        # required=True
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=50,
        help_text="E-mail Preenchimento Obrigatório ",
        widget=forms.TextInput(attrs={'placeholder': 'exemplo@exemplo.com.br'})
        # required=True
    )
    subject = forms.CharField(
        label='Assunto',
        widget=forms.TextInput(attrs={'placeholder': 'Escreva o seu assunto'}),
        help_text="Assunto Preenchimento Obrigatório",
        min_length=5,
        max_length=100
    )
    message = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder': 'Escreva sua mensagem'}),
        help_text="Mensagem Preenchimento Obrigatório",
        min_length=10,
        max_length=400
    )
