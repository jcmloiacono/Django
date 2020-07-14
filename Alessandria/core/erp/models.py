from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class employee(models.Model):
    #ManyToMany (hace relacion entre dos categorias)
    categ= models.ManyToManyField(Category)
    #ForeingKey Para relacionar la tabla, on-delete(que pasa en caso que se elimine la tabla relacionada)
    #CASCADE(si elimino un registro de Type elimina tambien employee por que esta relacionado)
    #SET_NULL(acepta eliminar el valor de type y lo coloca nulo, se debe agregar null=True)
    #PROTECT(no se puede eliminar un registro si otro depende el el)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    #Max_length (Es el maximo de caracteres) verbose_name(Asigna el nombre que se va a mostrar)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    #unique (asigna clave unica)
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    #datetime.now (es de la libreria datetime y pone fecha actual)
    date_joined = models.DateField(default=datetime.now(), verbose_name='Fecha de Registro')
    #auto.now (asigna hora y fecha actual la primera vez que se crea)
    date_created = models.DateTimeField(auto_now=True)
    #auto.now (asigna hora y fecha actual y siempre al actualiza para cualquier modifificacion)
    date_upgrade = models.DateTimeField(auto_now_add=True)
    #PositiveIntegerField (acepta valores positivos en el valor) IntegerField(Acepta numeros positivos y negativos)
    age = models.PositiveIntegerField(default=0)
    #DecimalField (acepta valores decimales) max_digits(Maximo de digitos), decimal_places(cantidad de decimales)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    #BooleanField (acepta valores booleanos)
    state = models.BooleanField(default=True)
    # ImageField (acepta imagenes) upload_to(guarda en la carpeta seleccionada, Opcional /%Y/%m/%d)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    # null y blank (Acepta valores nulos y vacios
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        self.names

    class Meta:
        # Para darle propiedades adiconales a la entidad
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        # Darle el nombre a la tabla
        db_table = 'empleado'
        #Tipo Ordenamiento (si quiere que sea desendente -id
        ordering = ['id']