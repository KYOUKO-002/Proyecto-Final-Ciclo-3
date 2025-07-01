class Estudiante:
    def __init__(self, id=None, identificacion=None, nombres=None):
        self.id = id
        self.identificacion = identificacion
        self.nombres = nombres

class Carrera:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

class Docente:
    def __init__(self, id=None,cedula=None, nombre=None):
        self.id = id
        self.cedula = cedula
        self.nombre = nombre

class Asignatura:
    def __init__(self, id=None, nombre=None, nivel=None, id_carrera=None ):
        self.id = id
        self.nombre = nombre
        self.nivel = nivel
        self.id_carrera = id_carrera

class Periodo:
    def __init__(self, id=None, nombre=None, paralelo=None):
        self.id = id
        self.nombre = nombre
        self.paralelo = paralelo

class Matricula:
    def __init__(self, id=None, id_estudiante=None, id_periodo=None, estado=None, ingreso=None):
        self.id = id
        self.id_estudiante = id_estudiante
        self.id_periodo = id_periodo
        self.estado = estado
        self.ingreso = ingreso

class Detalle_matricula:
    def __init__(self, id=None, id_matricula=None, id_asignatura=None, id_docente=None, asistencia=None, nota_final=None):
        self.id = id
        self.id_matricula = id_matricula
        self.id_asignatura = id_asignatura
        self.id_docente = id_docente
        self.asistencia = asistencia
        self.nota_final = nota_final

class Notas:
    def __init__(self, id=None, asistencia=None, nota_final=None, id_estudiante=None, id_asignatura= None, id_periodo=None):
        self.id = id
        self.asistencia = asistencia
        self.nota_final = nota_final
        self.id_estudiante = id_estudiante
        self.id_asignatura = id_asignatura
        self.id_periodo = id_periodo

