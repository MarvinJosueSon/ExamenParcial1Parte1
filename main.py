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
        self.promedio = promedio
        self.estado = estado

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
                    productividadAux=int(input("Ingrese la productividad del empleado en la escala de (1 a 10): "))
                    if productividadAux>=1 and productividadAux<=10:
                        promedioAux=(puntualidadAux+trabajoEquipoAux+productividadAux)//3
                        if promedioAux>=7:
                            estadoAux="Safisfactorio"
                        else:
                            estadoAux="Mejorar"
                        desempeñoAux=Desempeño(puntualidadAux,trabajoEquipoAux,productividadAux,observacionesAux,promedioAux,estadoAux)
                        empleadosDiccionario[idAux]={
                            "informacion": empleadoAux,
                            "contacto": contatoAux,
                            "desempeño": desempeñoAux
                        }
                        print("INGRESADO CON EXITO")
                else:
                    print("ERROR: Debe ser un numero entero en el rango indicado")
            else:
                print("ERROR: Debe ser un numero entero en el rango indicado")
        else:
            print("ERROR: El Id ya existe en el sistema por favor cambielo")
    except ValueError:
        print("ERROR: PARAMETROS INCORRECTOS")
def verEmpleados():
    for clave, valor in empleadosDiccionario.items():
        print(f"Codigo: {clave}")
        valor["informacion"].mostrar()
        valor["contacto"].mostrar()
        valor["desempeño"].mostrar()
        print("---------------------------"*10)
def buscar():
    if len(empleadosDiccionario)>0:
        buscarIdAux=input("Ingrese el ID del empleado a buscar: ")
        if buscarIdAux in empleadosDiccionario:
            print("Empleado encontrado")
            print(f"Codigo: {buscarIdAux}")
            empleadosDiccionario[buscarIdAux]["informacion"].mostrar()
            empleadosDiccionario[buscarIdAux]["contacto"].mostrar()
            empleadosDiccionario[buscarIdAux]["desempeño"].mostrar()
        else:
            print("Empleado no encontrado")

    else:
        print("ERROR: Aun no hay empleados disponibles")
def empleadosSatisfactorios():
    if len(empleadosDiccionario)>0:
        print("Empleados satisfactorios")
        for clave, valor in empleadosDiccionario.items():
            if valor["desempeño"].estado=="Safisfactorio":
                print(f"Nombre: {valor["informacion"].nombre}; ID:{clave}")
while True:
    print("==MENU==")
    print("1. Ingresar empleado")
    print("2. Ver empleados ingresados")
    print("3. Buscar empleado por codigo")
    print("4. Mostrar solo empleados satisfactorios")
    print("5. Mejor promedio")
    print("6. Eliminar empleado")
    opcion=input("Ingrese el numero de opcion: ")
    match opcion:
        case "1":
            Ingresar()
        case "2":
            verEmpleados()
        case "3":
            buscar()
        case "4":
            empleadosSatisfactorios()