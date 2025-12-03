import json
import os
from datetime import date, timedelta

class Autor:
    def __init__(self, nombre: str, nacionalidad: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} - Nacionalidad: {self.nacionalidad}")

    def to_dict(self):
        return {"nombre": self.nombre, "nacionalidad": self.nacionalidad}


class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} (Código: {self.codigo})")

    def to_dict(self):
        return {"codigo": self.codigo, "nombre": self.nombre}


class Libro:

    class Pagina:
        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def mostrar(self):
            print(f"Página {self.numero}: {self.contenido}")

        def to_dict(self):
            return {
                "numero": self.numero,
                "contenido": self.contenido
            }

    def __init__(self, titulo, isbn, paginas=None):
        self.titulo = titulo
        self.isbn = isbn
        # Si pasan páginas como strings, convertirlas a objetos Pagina
        self.paginas = []
        if paginas:
            for i, contenido in enumerate(paginas, start=1):
                if isinstance(contenido, str):
                    self.paginas.append(self.Pagina(i, contenido))
                elif isinstance(contenido, self.Pagina):
                    self.paginas.append(contenido)

    def leer(self):
        print(f"== Leyendo libro: {self.titulo} (ISBN: {self.isbn}) ==")
        for p in self.paginas:
            p.mostrar()
        print("== Fin del libro ==")

    def __str__(self):
        return f"{self.titulo} (ISBN:{self.isbn})"

    # ----------------- Páginas -----------------
    def agregar_pagina(self, contenido):
        numero = len(self.paginas) + 1
        self.paginas.append(self.Pagina(numero, contenido))

    def editar_pagina(self, indice, nuevo_contenido):
        if 0 <= indice < len(self.paginas):
            self.paginas[indice].contenido = nuevo_contenido

    def borrar_pagina(self, indice):
        if 0 <= indice < len(self.paginas):
            del self.paginas[indice]
            # Re-numerar las páginas después de borrar
            for i, p in enumerate(self.paginas, start=1):
                p.numero = i

    # ----------------- JSON -----------------
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "isbn": self.isbn,
            "paginas": [p.to_dict() for p in self.paginas]
        }



class Prestamo:
    def __init__(self, estudiante, libro, dias_prestamo=14):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_prestamo)
        self.estudiante = estudiante
        self.libro = libro

    def to_dict(self):
        return {
            "estudiante": self.estudiante.to_dict(),
            "libro": self.libro.to_dict(),
            "fecha_prestamo": str(self.fecha_prestamo),
            "fecha_devolucion": str(self.fecha_devolucion)
        }

    def mostrarInfo(self):
        print("--- Información del préstamo ---")
        print(f"Libro: {self.libro.titulo} (ISBN: {self.libro.isbn})")
        print(f"Estudiante: {self.estudiante.nombre} (Código: {self.estudiante.codigo})")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion}")
        print("------------------------------------")


class Biblioteca:

    class Horario:
        def __init__(self, dias_apertura, hora_apertura, hora_cierre):
            self.dias_apertura = dias_apertura
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre

        def mostrarHorario(self):
            print(f"Horario: {self.dias_apertura} | {self.hora_apertura} - {self.hora_cierre}")

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = None

    def setHorario(self, dias_apertura, hora_apertura, hora_cierre):
        self.horario = Biblioteca.Horario(dias_apertura, hora_apertura, hora_cierre)
        print(f"[Biblioteca] Horario establecido para '{self.nombre}'.")

    def agregarLibro(self, libro: Libro):
        self.libros.append(libro)
        print(f"[Biblioteca] Libro agregado: {libro.titulo}")

    def agregarAutor(self, autor: Autor):
        self.autores.append(autor)
        print(f"[Biblioteca] Autor registrado: {autor.nombre}")

    def prestarLibro(self, estudiante: Estudiante, libro: Libro):
        if libro not in self.libros:
            print(f"[Error] El libro '{libro.titulo}' no está disponible.")
            return None
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"[Biblioteca] Préstamo creado: {libro.titulo} -> {estudiante.nombre}")
        return prestamo

    def mostrarEstado(self):
        print(f"=== Estado de la Biblioteca: {self.nombre} ===")
        print("Libros disponibles:")
        for l in self.libros:
            print(f" - {l.titulo}")
