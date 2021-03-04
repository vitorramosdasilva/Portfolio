# coding=utf-8
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContatoForm
from django.shortcuts import render
from django.conf import settings


def IndexView(request):
    if request.method == 'GET':
        form = ContatoForm()
        return render(request, "index.html", {'form': form})
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Assunto: ' + subject + '\n' + 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'Messagem: ' + message
            messages.success(request, 'E-mail enviado com sucesso.\nRetornaremos em até 48 horas úteis.' )
            try:
                send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [settings.EMAIL_HOST_USER],
                          fail_silently=False
                          )
                form = ContatoForm
            except BadHeaderError:
                messages.error(request, 'Erro ao enviar e-mail.\nTente Novamente e revise o conteúdo.')
            return render(request, "index.html", {'form': form})
    return render(request, "index.html", {'form': form})


# Page Error ...
def error_400(request, exception):
    return render(request, '400.html', status=400)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_50x(request, exception):
    return render(request, '500.html', status=500)

