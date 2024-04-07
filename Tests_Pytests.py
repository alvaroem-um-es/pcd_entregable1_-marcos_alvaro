import pytest
from Prueba_mejorada import *

#Prueba de creación de instancias de clases
def test_creacion_instancias():
    departamento_DIIC = Departamento.DIIC
    departamento_DITEC = Departamento.DITEC
    asignatura = Asignatura("Matemáticas", "MAT101", 5, departamento_DIIC)
    profesor = ProfesorTitular("Paco", "09224070", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
    profesor2 = ProfesorAsociado("Ana", "12345679", "Calle Principal", Sexo.V, "ID002", departamento_DITEC)
    estudiante = Estudiante("Maria", "98765432", "Calle Secundaria", Sexo.V)
    
    assert isinstance(departamento_DIIC, Departamento)
    assert isinstance(departamento_DITEC, Departamento)
    assert isinstance(asignatura, Asignatura)
    assert isinstance(profesor, ProfesorTitular)
    assert isinstance(profesor2, ProfesorAsociado)
    assert isinstance(estudiante, Estudiante)

#Pruebas para la clase Asignatura
def test_creacion_asignatura():
    departamento_DIIC = Departamento.DIIC
    asignatura = Asignatura("Matemáticas", "MAT101", 5, departamento_DIIC)
    assert asignatura.nombre == "Matemáticas"
    assert asignatura.codigo == "MAT101"
    assert asignatura.creditos == 5
    assert asignatura.departamento == departamento_DIIC

def test_creditos_excesivos():
    departamento_DIIC = Departamento.DIIC
    with pytest.raises(AsignaturaCreditosError):
        Asignatura("Física", "FIS101", 8, departamento_DIIC)

#Pruebas para la clase Profesor
def test_profesor_añadir_asignatura():
    departamento_DIIC = Departamento.DIIC
    profesor = ProfesorTitular("Paco", "09224070", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
    profesor.añadir_asignatura(Asignatura("Física", "FIS101", 4, departamento_DIIC))
    profesor.añadir_asignatura("Historia")
    profesor.añadir_asignatura({"nombre": "Lengua", "codigo": "INF101", "creditos": 3, "departamento": departamento_DIIC})
    assert len(profesor.asignaturas_impartidas) == 3
    assert profesor.asignaturas_impartidas[1].nombre == "Historia"
    assert profesor.get_asignaturas_impartidas() == ['Física', 'Historia', 'Lengua']

def test_cambio_departamento():
    departamento_DIIC = Departamento.DIIC
    departamento_DITEC = Departamento.DITEC
    profesor = ProfesorTitular("Paco", "09224070", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
    profesor.cambio_departamento(departamento_DITEC)
    assert profesor.departamento == departamento_DITEC

#Pruebas para la clase Estudiante
def test_matricular_asignatura_estudiante():
    estudiante = Estudiante("Maria", "98765432", "Calle Secundaria", Sexo.V)
    estudiante.matricular("Matemáticas")
    assert len(estudiante.asignaturas) == 1
    assert estudiante.asignaturas[0].nombre == "Matemáticas"

def test_matricular_asignatura_creditos_excesivos():
    departamento_DIIC = Departamento.DIIC
    estudiante = Estudiante("Maria", "98765432", "Calle Secundaria", Sexo.V)
    with pytest.raises(AsignaturaCreditosError):
        estudiante.matricular(Asignatura("Física", "FIS101", 8, departamento_DIIC))

#Prueba de relación entre clases
def test_relaciones_entre_clases():
    departamento_DIIC = Departamento.DIIC
    profesor = ProfesorTitular("Paco", "09224070", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
    assert isinstance(profesor, Investigador)
    assert isinstance(profesor, Profesor)
    assert hasattr(profesor, "asignaturas_impartidas")
