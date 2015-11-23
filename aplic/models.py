from django.db import models
from django.core.validators import MaxLengthValidator
from test.test_imageop import MAX_LEN

class Usuario(models.Model):
	Nombres            = models.CharField(max_length=80, blank=True)
	Apellidos          = models.CharField(max_length=80, blank=True)
	UserLogon          = models.CharField(max_length=20, blank=True)
	TipoUser           = models.IntegerField()
	CodUser            = models.CharField(max_length=15, unique=True)
	UserPassword       = models.CharField(max_length=20, blank=True)
	EstadoUser         = models.IntegerField()
	Eliminado          = models.BooleanField(default=False)

class Tercero(models.Model):
	CodTercero         = models.CharField(max_length=15, unique=True)
	IdTipoTercero      = models.BooleanField(default=False)
	RazonSocial        = models.CharField(max_length=200, blank=True)
	Email              = models.EmailField(max_length=100, blank=True)
	Direccion          = models.CharField(max_length=100, blank=True)
	IdEstadoTercero    = models.IntegerField()
	Telefono           = models.CharField(max_length=100, blank=True)
	Eliminado          = models.BooleanField(default=False)		

class Kardex(models.Model):
	CodKardex          = models.CharField(max_length=15, unique=True)
	TipoMovimiento     = models.IntegerField()
	Fecha              = models.DateField()
	CodTercero         = models.ForeignKey('Tercero')
	CodProduc          = models.ForeignKey('Producto')
	CantProduc         = models.IntegerField()
	ValorUnitario      = models.DecimalField(max_digits=10, decimal_places=2)
	EstadoKardex       = models.IntegerField()
	ValorPublico       = models.DecimalField(max_digits=10, decimal_places=2)
	Eliminado          = models.BooleanField(default=False)

class Producto(models.Model):
	CodProduc          = models.CharField(max_length=15, unique=True)
	NomProduc          = models.CharField(max_length=80, blank=True)
	CantProduc         = models.DecimalField(max_digits=10, decimal_places=2)
	ValorProduc        = models.DecimalField(max_digits=10, decimal_places=2)
	EstadoProduc       = models.IntegerField()
	Eliminado          = models.BooleanField(default=False)

class Parametro(models.Model):
	IdParametro        = models.IntegerField()
	Atributo           = models.CharField(max_length=50)
	Descripcion        = models.CharField(max_length=200)
	EstadoParametro    = models.CharField(max_length=1)

	def __str__(self):
		return self.Atributo

class ValorParametro(models.Model):
	Valor              = models.CharField(max_length=30)
	IdParametro        = models.ForeignKey('Parametro')
	Orden              = models.CharField(max_length=3)
	EstadoValParametro = models.CharField(max_length=1)

	def __str__(self):
		return self.Valor