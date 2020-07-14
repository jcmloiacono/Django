from django.db import models

# Create your models here.

class Alumno(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    dni = models.CharField(max_length=8)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXOS,default='M')

    def NombreCompleto(self):
        cadena ='{0} {1} , {2}'
        return cadena.format(self.ApellidoPaterno,self.ApellidoMaterno,self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Cursos(models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return '{0} ({1})'.format(self.Nombre, self.Creditos)

class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Cursos = models.ForeignKey(Cursos, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateField(auto_now=True)

    def __str__(self):
        cadena = "{0} ==> {1}"
        return cadena.format(self.Alumno, self.Cursos.Nombre)