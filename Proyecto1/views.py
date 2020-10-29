from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        
def saludo(request): #Primera vista

    p1=Persona( "Liliana Brenda", "Gutierrez")

    #nombre="Brenda"
    #apellido="Gutierrez"

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/hugod/Desktop/practica-proyect/Proyecto1/Proyecto1/platillas/miplatilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request): #Segunda vista

    return HttpResponse("Ya me voy, tengo cosas que hacer")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Hola Soy Brenda %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    
    #edadActual=18
    periodo=agno-2020
    edadFutura=edad+periodo
    documento="<html><body><h2>En el agno %s tendras %s agnos" %(agno,edadFutura)

    return HttpResponse(documento)
