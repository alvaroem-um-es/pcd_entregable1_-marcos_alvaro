import pytest
from ejercicio_entregable_1 import ProfesorTitular, ProfesorAsociado, Estudiante, Asignatura, Departamento, Sexo, Profesor, Persona

# Crear instancias de Departamento
departamento_DIIC = Departamento.DIIC
departamento_DITEC = Departamento.DITEC

# Crear instancias de Profesores
profe1 = ProfesorTitular("Paco", "09224070", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
profe2 = ProfesorAsociado("Ana", "12345679", "Calle Principal", Sexo.V, "ID002", departamento_DITEC)

def test_profesor_añadir_asignatura():
    #profe1.añadir_asignatura("mlml")
    profe1.añadir_asignatura(Asignatura("Física", "FIS101", 4, departamento_DIIC))
    profe1.añadir_asignatura(Asignatura("Mates", "M1T3s", 5, departamento_DIIC))
    profe2.añadir_asignatura(Asignatura("Lengua", "LenG", 12, departamento_DITEC))
    profe2.añadir_asignatura(Asignatura("Historia", "HisT", 1, departamento_DITEC))
    #profe2.añadir_asignatura({"nombre": "lolo", "codigo": "INF101", "creditos": 3, "departamento": departamento_DITEC})

def test_profesor_asignatura_impartida():
    # Mostrar las asignaturas impartidas por cada profesor
    print("Asignaturas impartidas por", profe1.nombre + ":")
    print(profe1.get_asignaturas_impartidas())

    print("\nAsignaturas impartidas por", profe2.nombre + ":")
    print(profe2.get_asignaturas_impartidas())

def test_cambio_departamento():
    profe1.cambio_departamento(departamento_DITEC)
    print("\nNuevo departamento de", profe1.nombre + ":", profe1.devolver_departamento())

def test_mostrar_info_estudiante():
    estudiante1 = Estudiante("Maria", "98765432", "Calle Secundaria", Sexo.V)
    estudiante1.matricular(Asignatura("Historia", "HIS101", 5, departamento_DITEC))
    #estudiante1.matricular('Lengua')
    print("\nInformación de", estudiante1.nombre + ":")
    print(estudiante1.get_estudiante())










