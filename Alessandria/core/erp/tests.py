from app.wsgi import *
from core.erp.models import Type

# Listar

query = Type.objects.all()
print(query)

# Insercion
text = Type()
text.name = 'Asistente'
text.save()

# Editar
text = Type.objects.get(id=1)
text.name = "Secretaria"
text.save()

# Eliminacion
text = Type.objects.get(pk=1)
text.delete()

