
from django.db import models


class Persona(models.Model):
    num_documento = models.CharField(
        primary_key=True,
        max_length=20
    )
    tipo_documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    fech_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    rol = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(models.Model):
    # PK y FK hacia Persona
    per_num_documento = models.OneToOneField(
        Persona,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="Per_Num_Documento"
    )
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    grado_escolar = models.CharField(max_length=30)

    def __str__(self):
        return str(self.per_num_documento)


class Autor(models.Model):
    # PK y FK hacia Persona
    per_num_documento = models.OneToOneField(
        Persona,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="Per_Num_Documento"
    )
    nacionalidad = models.CharField(max_length=45)
    biografia = models.TextField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.per_num_documento)


class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=150)
    nombre_editorial = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_editorial


class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    nombre_tema = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_tema


class Libro(models.Model):
    codigo_barras = models.CharField(
        primary_key=True,
        max_length=30
    )
    estado = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.codigo_barras


class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    edicion = models.CharField(max_length=30)
    isbn = models.CharField(max_length=20)
    fecha_publicacion = models.DateTimeField()

    # FK hacia Libro
    codigo_barras = models.ForeignKey(
        Libro,
        on_delete=models.PROTECT,
        db_column="Codigo_Barras",
        related_name="publicaciones"
    )

    # FK hacia Editorial
    id_editorial = models.ForeignKey(
        Editorial,
        on_delete=models.PROTECT,
        db_column="Id_Editorial",
        related_name="publicaciones"
    )

    # FK hacia Tema
    id_tema = models.ForeignKey(
        Tema,
        on_delete=models.PROTECT,
        db_column="Id_Tema",
        related_name="publicaciones"
    )

    # FK hacia Autor
    aut_per_num_documento = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        db_column="Aut_Per_Num_Documento",
        related_name="publicaciones"
    )

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(
        null=True,
        blank=True
    )
    observacion = models.CharField(
        max_length=255,
        blank=True
    )

    # FK hacia Libro
    codigo_barras = models.ForeignKey(
        Libro,
        on_delete=models.PROTECT,
        db_column="Codigo_Barras",
        related_name="prestamos"
    )

    # FK hacia Estudiante
    est_per_num_documento = models.ForeignKey(
        Estudiante,
        on_delete=models.PROTECT,
        db_column="Est_Per_Num_Documento",
        related_name="prestamos"
    )

    def __str__(self):
        return f"Préstamo {self.id_prestamo}"
