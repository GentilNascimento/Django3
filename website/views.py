from django.shortcuts import render
 

def hello_blog(request):
    lista = [
        'Djando', 'Python', 'Git', 'Html', 'Banco de dados', 'Linux', 'Uwsgi', 'Systemctl'
    ]
    data = {'name':'Curso de Django 3', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)

