from datetime import date, timedelta

class Autor:
    def __init__(self, nombre: str, nacionalidad: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} - Nacionalidad: {self.nacionalidad}")

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} (Código: {self.codigo})")


class Libro:

    #COMPOSICIÓN
    class Pagina:
        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def mostrar(self):
            print(f"Página {self.numero}: {self.contenido}")

    def __init__(self, titulo, isbn, paginas_contenido):
        self.titulo = titulo
        self.isbn = isbn
        # COMPOSICIÓN:
        self.paginas = []
        for i, texto in enumerate(paginas_contenido, start=1):
            self.paginas.append(Libro.Pagina(i, texto))

    def leer(self):
        print(f"== Leyendo libro: {self.titulo} (ISBN: {self.isbn}) ==")
        for p in self.paginas:
            p.mostrar()
        print("==Fin del libro ==")

    def __str__(self):
        return f"{self.titulo} (ISBN:{self.isbn})"

class Prestamo:
    def __init__(self, estudiante, libro, dias_prestamo = 14):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_prestamo)
        # ASOCIACIÓN:
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print("--- Información del préstamo ---")
        print(f"Libro: {self.libro.titulo} (ISBN: {self.libro.isbn})")
        print(f"Estudiante: {self.estudiante.nombre} (Código: {self.estudiante.codigo})")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion}")
        print("------------------------------------")

class Biblioteca:
    #COMPOSICIÓN
    class Horario:
        def __init__(self, dias_apertura, hora_apertura, hora_cierre):
            self.dias_apertura = dias_apertura
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre

        def mostrarHorario(self):
            print(f"Horario: {self.dias_apertura} | {self.hora_apertura} - {self.hora_cierre}")

    def __init__(self, nombre):
        self.nombre = nombre
        # AGREGACIÓN:
        self.libros = []
        self.autores = []
        self.prestamos = []
        # COMPOSICIÓN:
        self.horario = None

    def setHorario(self, dias_apertura, hora_apertura, hora_cierre):
        self.horario = Biblioteca.Horario(dias_apertura, hora_apertura, hora_cierre)
        print(f"[Biblioteca] Horario establecido para '{self.nombre}'.")

    def agregarLibro(self, libro: Libro):
        # AGREGACIÓN
        self.libros.append(libro)
        print(f"[Biblioteca] Libro agregado: {libro.titulo}")

    def agregarAutor(self, autor: Autor):
        # AGREGACIÓN
        self.autores.append(autor)
        print(f"[Biblioteca] Autor registrado: {autor.nombre}")

    def prestarLibro(self, estudiante: Estudiante, libro: Libro):
        # ASOCIACIÓN
        if libro not in self.libros:
            print(f"[Error] El libro '{libro.titulo}' no está disponible en la biblioteca.")
            return None
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"[Biblioteca] Préstamo creado: {libro.titulo} -> {estudiante.nombre}")
        return prestamo

    def mostrarEstado(self):
        print(f"=== Estado de la Biblioteca: {self.nombre} ===")
        print("Libros disponibles:")
        for b in self.libros:
            print(f" - {b}")
        print("Autores registrados:")
        for a in self.autores:
            print(f" - {a.nombre} ({a.nacionalidad})")
        print("Préstamos activos:")
        if not self.prestamos:
            print(" - (ninguno)")
        else:
            for p in self.prestamos:
                print(f" - {p.libro.titulo} prestado a {p.estudiante.nombre} hasta {p.fecha_devolucion}")
        if self.horario:
            self.horario.mostrarHorario()
        else:
            print("Horario: NO establecido")
        print("============================")

    def cerrarBiblioteca(self):
        # COMPOSICIÓN
        print(f"[Biblioteca] Cerrando biblioteca '{self.nombre}'... Todos los préstamos se eliminan.")
        self.prestamos.clear()
        self.horario = None
        print("[Biblioteca] Biblioteca cerrada.")


# ejecucion hcc

autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("Isaac Asimov", "Estadounidense")

contenido1 = ["En un lugar de la Mancha...", "Segunda página del libro..."]
libro1 = Libro("Cien años de soledad (versión corta ejemplo)", "ISBN-1111", contenido1)

contenido2 = ["Página 1 de Fundamentos de IA", "Página 2: redes neuronales"]
libro2 = Libro("Fundamentos de IA", "ISBN-2222", contenido2)

est1 = Estudiante("2025001", "María Pérez")
est2 = Estudiante("2025002", "Juan Gómez")

bib = Biblioteca("Biblioteca Central UMSA")
bib.setHorario("Lunes-Viernes", "08:00", "18:00")

bib.agregarAutor(autor1)
bib.agregarAutor(autor2)
bib.agregarLibro(libro1)
bib.agregarLibro(libro2)

bib.mostrarEstado()

p1 = bib.prestarLibro(est1, libro1)
if p1:
    p1.mostrarInfo()

libro1.leer()

bib.mostrarEstado()

bib.cerrarBiblioteca()
bib.mostrarEstado()

if bib.horario is None:
    print("Confirmación: El horario ya no existe (composición):", bib.horario)
else:
    bib.horario.mostrarHorario()
