empleadosDiccionario={}
class Empleado:
    def __init__(self, nombre, departamento, antiguedad):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Antiguedad: {self.antiguedad}")

class Desempeño:
    def __init__(self, puntualidad, trabajoEquipo, productividad, observaciones, promedio, estado):
        self.puntualidad = puntualidad
        self.trabajoEquipo = trabajoEquipo
        self.productividad = productividad
        self.observaciones = observaciones

    def mostrar(self):
        print(f"Puntualidad: {self.puntualidad}")
        print(f"Trabajo Equipo: {self.trabajoEquipo}")
        print(f"Productividad: {self.productividad}")
        print(f"Observaciones: {self.observaciones}")
        print(f"Promedio: {self.promedio}")
        print(f"Estado: {self.estado}")
class Contacto:
    def __init__(self, telefono,correo):
        self.telefono = telefono
        self.correo = correo
    def mostrar(self):
        print(f"Telefono: {self.telefono}")
        print(f"Correo: {self.correo}")

def Ingresar():
    try:
        idAux=input("Ingrese ID del empleado: ")
        if not idAux in empleadosDiccionario:
            nombreAux=input("Ingrese nombre del empleado: ")
            departamentoAux=input("Ingrese el  departamento en el que esta el empleado: ")
            antiguedadAux=input("Ingrese la antiguedad del empleado en la empresa: ")
            empleadoAux= Empleado(nombreAux, departamentoAux, antiguedadAux)
            #
            telefonoAux = input("Ingrese el telefono del empleado: ")
            correoAux = input("Ingrese el correo del empleado: ")
            contatoAux = Contacto(telefonoAux, correoAux)
            #
            observacionesAux = input("Ingrese la observaciones del empleado: ")
            puntualidadAux=int(input("Califique la puntualidad del empleado (1 a 10): "))
            if puntualidadAux>=1 and puntualidadAux<=10:
                trabajoEquipoAux=int(input("Ingrese la capacidad del empleado de trabajo en equipo (1 a 10): "))
                if trabajoEquipoAux>=1 and trabajoEquipoAux<=10:
                    productividadAux=int(input("Ingrese la productividad del empleado en la escala de (1 a 10)"))
                    if productividadAux>=1 and productividadAux<=10:
                        promedioAux=(puntualidadAux+trabajoEquipoAux+productividadAux)//3
                        if promedioAux>=7:
                            estadoAux="Safisfactorio"
                        else:
                            estadoAux="Mojorar"
                        desempeñoAux=Desempeño(puntualidadAux,trabajoEquipoAux,productividadAux,observacionesAux,promedioAux,estadoAux)
                else:
                    print("ERROR: Debe ser un numero entero en el rango indicado")
            else:
                print("ERROR: Debe ser un numero entero en el rango indicado")
        else:
            print("ERROR: El Id ya existe en el sistema por favor cambielo")
    except ValueError:
        print("ERROR: PARAMETROS INCORRECTOS")