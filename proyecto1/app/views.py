from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
	
	doc_externo=open("/Users/jean/Documents/Python/Django/proyecto1/proyecto1/plantillas/misplantillas.html")

	plt=Template(doc_externo.read())

	doc_externo.close()

	ctx=Context()

	documento=plt.render(ctx)

	return HttpResponse(documento)


def despedida(request):
	
	return HttpResponse("esperemos que tenga un excelente dia")

def fecha(request):

	fecha_actual=datetime.datetime.now()

	documento="""<html>
	<body>
	<h1> Esta es la fecha Actual %s</h1>
	</body>
	</html>"""% fecha_actual

	return HttpResponse(documento)

def calcula_edad(request, edad, agno):	

	periodo=agno-2019
	edad_futura=edad+periodo

	documento="<html><body><h2> En el año %s tendras %s años" %(agno,edad_futura)

	return HttpResponse(documento)