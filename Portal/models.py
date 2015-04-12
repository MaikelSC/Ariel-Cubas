from django.db import models

class Categoria(models.Model):
		valor = models.CharField(max_length=40)
		posicion = models.PositiveIntegerField(max_length = 1)
		
		def __str__(self):
			return self.valor


class Noticia(models.Model):		
		categoria = models.ForeignKey(Categoria)	
		titulo = models.CharField(max_length=30)
		fecha_publicacion = models.DateTimeField()		
		imagen = models.ImageField(upload_to='Portal/static/images/news')
		pie_foto = models.CharField(max_length=200, blank=True)
		comentarios = models.BooleanField(default= 1)
		publicado = models.BooleanField(default= 1)
		codigo = models.TextField()

		
		def __str__(self):
			return self.titulo
		

class Comentario(models.Model):		
		noticia = models.ForeignKey(Noticia)
		fecha_publicacion = models.DateTimeField()		
		email = models.CharField(max_length=50)
		nombre_usuario = models.CharField(max_length=200)
		comentario = models.TextField()
		publicado = models.BooleanField(default= 1)
		
		def __str__(self):
			return self.nombre_usuario


class ArticulosFijos(models.Model):		
		titulo = models.CharField(max_length=100)
		fecha_publicacion = models.DateTimeField()		
		imagen = models.ImageField(upload_to='Portal/static/images/articulosFijos')
		pie_foto = models.CharField(max_length=200, blank = True)
		nombre = models.CharField(max_length=30, unique= True)
		comentarios = models.BooleanField(default= 1)
		codigo = models.TextField()		
		
		def __str__(self):
			return self.titulo

class Comentario_articulosFijos(models.Model):		
		articuloFijo = models.ForeignKey(ArticulosFijos)
		fecha_publicacion = models.DateTimeField()		
		email = models.CharField(max_length=30)
		nombre_usuario = models.CharField(max_length=200)
		comentario = models.TextField()
		publicado = models.BooleanField(default= 1)
		
		def __str__(self):
			return self.nombre_usuario
			
			
class ArticuloBlog(models.Model):
	
		titulo = models.CharField(max_length=100)
		fecha_publicacion = models.DateTimeField()		
		imagen = models.ImageField(upload_to='Portal/static/images/articulosBlog')
		pie_foto = models.CharField(max_length=200, blank=True)
		comentarios = models.BooleanField(default= 1)
		codigo = models.TextField()
		publicado = models.BooleanField(default= 1)
		
		def __str__(self):
			return self.titulo	
			
class Comentario_articuloBlog(models.Model):		
		articuloBlog = models.ForeignKey(ArticuloBlog)
		fecha_publicacion = models.DateTimeField()		
		email = models.CharField(max_length=30)
		nombre_usuario = models.CharField(max_length=200)
		comentario = models.TextField()
		publicado = models.BooleanField(default= 1)
		
		def __str__(self):
			return self.nombre_usuario						


class Galeria(models.Model):
	nombre = models.CharField(max_length=150) 
	
	def __str__(self):
			return self.nombre

from django.utils.html import format_html
	
class Imagen_galeria(models.Model):
	galeria = models.ForeignKey(Galeria)
	imagen = models.ImageField(upload_to='Portal/static/images/galerias')
	pie_foto = models.CharField(max_length=150, blank = True)
	fecha = models.DateField(blank = True)
	fotografo = models.CharField(max_length=100, blank = True)	
	portada = models.BooleanField(default= 0)
	
	def __str__(self):
			return self.galeria.nombre

class Videos(models.Model):
	video = models.FileField(upload_to='Portal/static/videos/')
	pie_video = models.CharField(max_length=150, blank = True)
	fecha = models.DateField(blank = True)
	autor = models.CharField(max_length=100, blank = True)

	# def __str__(self):
			# return self.video
			
class Informacion_contacto(models.Model):
	codigo = models.TextField()
	telefono = models.CharField(max_length=14, blank = True)
	fax = models.CharField(max_length=14, blank = True)
	email = models.CharField(max_length=60, blank = True)
	imagen = models.ImageField(upload_to='Portal/static/images/contacto')
	


class Trabajo(models.Model):
	galeria = models.ForeignKey(Galeria)	
	nombre = models.CharField(max_length=40)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	codigo = codigo = models.TextField()
	publicado = models.BooleanField(default= 1)	
	
	def __str__(self):
			return self.nombre


class Ejemplos_trabajos(models.Model):
		trabajo = models.ForeignKey(Trabajo)
		galeria = models.ForeignKey(Galeria)
		modelo = models.CharField(max_length=40)
		sitio_modelo = models.URLField(max_length=200, blank= True)
		evento = models.CharField(max_length=150, blank= True)
		opinion = models.TextField(blank= True)
		codigo = models.TextField()
		comentarios = models.BooleanField(default= 1)
		publicado = models.BooleanField(default= 1)


class Comentario_ejemplosTrabajos(models.Model):		
		ejemplosTrabajos = models.ForeignKey(Ejemplos_trabajos)
		fecha_publicacion = models.DateTimeField()		
		email = models.CharField(max_length=30)
		nombre_usuario = models.CharField(max_length=200)
		comentario = models.TextField()
		publicado = models.BooleanField(default= 1)
		
		def __str__(self):
			return self.nombre_usuario			


class Sitios(models.Model):
		nombre = models.CharField(max_length=70)
		url = models.CharField(max_length= 100)
		publicado = models.BooleanField(default= 1)
		
		def __str__(self):
			return self.nombre
	
