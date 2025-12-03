import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import json
import os

from biblioteca import Biblioteca, Libro, Autor, Estudiante

ARCHIVO_JSON = "bibliotecas.json"

COLOR_FONDO = "#d0e7ff"
COLOR_TITULO = "#0a4d8c"
COLOR_BOTON = "#70b8ff"
COLOR_BOTON_TEXTO = "white"
COLOR_BOTON_ELIMINAR = "#ff7070"

class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.bibliotecas = []
        self.biblioteca_actual = None
        self.estudiantes_dict = {}

        root.title("Biblioteca - Interfaz Gráfica")
        root.geometry("800x600")
        root.configure(bg=COLOR_FONDO)

        # ----- CARGAR DATOS AL INICIAR -----
        self.cargar_datos()

        # ------------------ SELECCIÓN DE BIBLIOTECA ------------------
        frame_bib = tk.Frame(root, bg=COLOR_FONDO)
        frame_bib.pack(pady=10)

        tk.Label(frame_bib, text="Seleccionar Biblioteca:", bg=COLOR_FONDO).grid(row=0, column=0, padx=5)
        self.combo_bibliotecas = ttk.Combobox(frame_bib, width=40)
        self.combo_bibliotecas.grid(row=0, column=1, padx=5)
        self.combo_bibliotecas.bind("<<ComboboxSelected>>", self.cambiar_biblioteca)

        self.nueva_bib_entry = tk.Entry(frame_bib)
        self.nueva_bib_entry.grid(row=1, column=0, padx=5)
        tk.Button(frame_bib, text="Agregar Biblioteca", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.agregar_biblioteca).grid(row=1, column=1, padx=5)

        # ------------------ NOTEBOOK ------------------
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=COLOR_FONDO)
        style.configure("TNotebook", background=COLOR_FONDO)
        style.configure("TNotebook.Tab", background="#b9dcff", padding=10)
        style.map("TNotebook.Tab", background=[("selected", "#79c3ff")])

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_libros = ttk.Frame(self.tabs)
        self.tab_autores = ttk.Frame(self.tabs)
        self.tab_estudiantes = ttk.Frame(self.tabs)
        self.tab_prestamos = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_libros, text="Libros")
        self.tabs.add(self.tab_autores, text="Autores")
        self.tabs.add(self.tab_estudiantes, text="Estudiantes")
        self.tabs.add(self.tab_prestamos, text="Préstamos")

        # Crear pestañas
        self.crear_tab_libros()
        self.crear_tab_autores()
        self.crear_tab_estudiantes()
        self.crear_tab_prestamos()

        self.actualizar_listas()

        # Guardar datos al cerrar la ventana
        root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    # ------------------ AGREGAR Y CAMBIAR BIBLIOTECA ------------------
    def agregar_biblioteca(self):
        nombre = self.nueva_bib_entry.get()
        if not nombre:
            messagebox.showerror("Error", "Ingresa un nombre para la biblioteca.")
            return
        nueva = Biblioteca(nombre)
        self.bibliotecas.append(nueva)
        self.estudiantes_dict[nombre] = []

        self.combo_bibliotecas["values"] = [b.nombre for b in self.bibliotecas]
        self.combo_bibliotecas.set(nombre)
        self.biblioteca_actual = nueva
        self.actualizar_listas()
        self.nueva_bib_entry.delete(0, tk.END)
        self.guardar_datos()

    def cambiar_biblioteca(self, event):
        nombre = self.combo_bibliotecas.get()
        self.biblioteca_actual = next((b for b in self.bibliotecas if b.nombre == nombre), None)
        if nombre not in self.estudiantes_dict:
            self.estudiantes_dict[nombre] = []
        self.actualizar_listas()

    # ------------------ TAB LIBROS ------------------
    def crear_tab_libros(self):
        tk.Label(self.tab_libros, text="Libros", font=("Arial", 14, "bold"), bg=COLOR_FONDO, fg=COLOR_TITULO).pack()

        self.lista_libros = tk.Listbox(self.tab_libros, width=70, height=10)
        self.lista_libros.pack(pady=5)
        self.lista_libros.bind("<<ListboxSelect>>", self.cargar_paginas_libro)

        frame = tk.Frame(self.tab_libros, bg=COLOR_FONDO)
        frame.pack(pady=5)

        tk.Label(frame, text="Título:", bg=COLOR_FONDO).grid(row=0, column=0)
        tk.Label(frame, text="ISBN:", bg=COLOR_FONDO).grid(row=1, column=0)

        self.titulo_libro = tk.Entry(frame)
        self.isbn_libro = tk.Entry(frame)
        self.titulo_libro.grid(row=0, column=1)
        self.isbn_libro.grid(row=1, column=1)

        btn_frame = tk.Frame(frame, bg=COLOR_FONDO)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btn_frame, text="Agregar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.agregar_libro).grid(row=0, column=0, padx=2)
        tk.Button(btn_frame, text="Eliminar", bg=COLOR_BOTON_ELIMINAR, fg="white",
                  command=self.eliminar_libro).grid(row=0, column=1, padx=2)

        # Páginas del libro
        tk.Label(self.tab_libros, text="Páginas", font=("Arial", 12, "bold"), bg=COLOR_FONDO).pack()
        self.lista_paginas = tk.Listbox(self.tab_libros, width=70, height=5)
        self.lista_paginas.pack(pady=5)

        pagina_frame = tk.Frame(self.tab_libros, bg=COLOR_FONDO)
        pagina_frame.pack(pady=5)
        self.pagina_entry = tk.Entry(pagina_frame, width=50)
        self.pagina_entry.grid(row=0, column=0, padx=5)
        tk.Button(pagina_frame, text="Agregar Página", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.agregar_pagina).grid(row=0, column=1, padx=2)

    def agregar_libro(self):
        if not self.biblioteca_actual:
            messagebox.showerror("Error", "Selecciona una biblioteca primero.")
            return
        titulo = self.titulo_libro.get()
        isbn = self.isbn_libro.get()
        if not titulo or not isbn:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        nuevo = Libro(titulo, isbn, [])
        self.biblioteca_actual.agregarLibro(nuevo)
        self.actualizar_listas()
        self.guardar_datos()

    def eliminar_libro(self):
        index = self.lista_libros.curselection()
        if not index:
            messagebox.showerror("Error", "Selecciona un libro primero.")
            return
        self.biblioteca_actual.libros.pop(index[0])
        self.actualizar_listas()
        self.guardar_datos()

    # ------------------ Páginas ------------------
    def cargar_paginas_libro(self, event=None):
        self.lista_paginas.delete(0, tk.END)
        index = self.lista_libros.curselection()
        if not index:
            return
        libro = self.biblioteca_actual.libros[index[0]]
        for p in libro.paginas:
            self.lista_paginas.insert(tk.END, p)

    def agregar_pagina(self):
        index = self.lista_libros.curselection()
        if not index:
            messagebox.showerror("Error", "Selecciona un libro primero.")
            return
        libro = self.biblioteca_actual.libros[index[0]]
        contenido = self.pagina_entry.get()
        if contenido:
            libro.paginas.append(contenido)
            self.actualizar_listas()
            self.guardar_datos()

    # ------------------ TAB AUTORES ------------------
    def crear_tab_autores(self):
        tk.Label(self.tab_autores, text="Autores", font=("Arial", 14, "bold"), bg=COLOR_FONDO, fg=COLOR_TITULO).pack()
        self.lista_autores = tk.Listbox(self.tab_autores, width=70, height=15)
        self.lista_autores.pack(pady=5)

        frame = tk.Frame(self.tab_autores, bg=COLOR_FONDO)
        frame.pack(pady=5)

        tk.Label(frame, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0)
        tk.Label(frame, text="Nacionalidad:", bg=COLOR_FONDO).grid(row=1, column=0)
        self.nombre_autor = tk.Entry(frame)
        self.nac_autor = tk.Entry(frame)
        self.nombre_autor.grid(row=0, column=1)
        self.nac_autor.grid(row=1, column=1)

        btn_frame = tk.Frame(frame, bg=COLOR_FONDO)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btn_frame, text="Agregar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.agregar_autor).grid(row=0, column=0, padx=2)
        tk.Button(btn_frame, text="Eliminar", bg=COLOR_BOTON_ELIMINAR, fg="white",
                  command=self.eliminar_autor).grid(row=0, column=1, padx=2)

    def agregar_autor(self):
        if not self.biblioteca_actual:
            messagebox.showerror("Error", "Selecciona una biblioteca primero.")
            return
        nombre = self.nombre_autor.get()
        nac = self.nac_autor.get()
        if not nombre or not nac:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        nuevo = Autor(nombre, nac)
        self.biblioteca_actual.agregarAutor(nuevo)
        self.actualizar_listas()
        self.guardar_datos()

    def eliminar_autor(self):
        index = self.lista_autores.curselection()
        if not index:
            messagebox.showerror("Error", "Selecciona un autor primero.")
            return
        self.biblioteca_actual.autores.pop(index[0])
        self.actualizar_listas()
        self.guardar_datos()

    # ------------------ TAB ESTUDIANTES ------------------
    def crear_tab_estudiantes(self):
        tk.Label(self.tab_estudiantes, text="Estudiantes", font=("Arial", 14, "bold"), bg=COLOR_FONDO, fg=COLOR_TITULO).pack()
        self.lista_estudiantes = tk.Listbox(self.tab_estudiantes, width=70, height=15)
        self.lista_estudiantes.pack(pady=5)

        frame = tk.Frame(self.tab_estudiantes, bg=COLOR_FONDO)
        frame.pack(pady=5)

        tk.Label(frame, text="Código:", bg=COLOR_FONDO).grid(row=0, column=0)
        tk.Label(frame, text="Nombre:", bg=COLOR_FONDO).grid(row=1, column=0)
        self.codigo_est = tk.Entry(frame)
        self.nombre_est = tk.Entry(frame)
        self.codigo_est.grid(row=0, column=1)
        self.nombre_est.grid(row=1, column=1)

        btn_frame = tk.Frame(frame, bg=COLOR_FONDO)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btn_frame, text="Agregar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.agregar_estudiante).grid(row=0, column=0, padx=2)
        tk.Button(btn_frame, text="Eliminar", bg=COLOR_BOTON_ELIMINAR, fg="white",
                  command=self.eliminar_estudiante).grid(row=0, column=1, padx=2)

    def agregar_estudiante(self):
        if not self.biblioteca_actual:
            messagebox.showerror("Error", "Selecciona una biblioteca primero.")
            return
        codigo = self.codigo_est.get()
        nombre = self.nombre_est.get()
        if not codigo or not nombre:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        nuevo = Estudiante(codigo, nombre)
        self.estudiantes_dict[self.biblioteca_actual.nombre].append(nuevo)
        self.actualizar_listas()
        self.guardar_datos()

    def eliminar_estudiante(self):
        index = self.lista_estudiantes.curselection()
        if not index:
            messagebox.showerror("Error", "Selecciona un estudiante primero.")
            return
        self.estudiantes_dict[self.biblioteca_actual.nombre].pop(index[0])
        self.actualizar_listas()
        self.guardar_datos()

    # ------------------ TAB PRÉSTAMOS ------------------
    def crear_tab_prestamos(self):
        tk.Label(self.tab_prestamos, text="Registrar Préstamo", font=("Arial", 14, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_TITULO).pack()
        frame = tk.Frame(self.tab_prestamos, bg=COLOR_FONDO)
        frame.pack(pady=10)

        tk.Label(frame, text="Estudiante:", bg=COLOR_FONDO).grid(row=0, column=0)
        tk.Label(frame, text="Libro:", bg=COLOR_FONDO).grid(row=1, column=0)

        self.combo_est_prestamo = ttk.Combobox(frame, width=40)
        self.combo_libro_prestamo = ttk.Combobox(frame, width=40)
        self.combo_est_prestamo.grid(row=0, column=1)
        self.combo_libro_prestamo.grid(row=1, column=1)

        tk.Button(frame, text="Prestar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.prestar_libro).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(self.tab_prestamos, text="Préstamos Activos", font=("Arial", 12, "bold"),
                 bg=COLOR_FONDO).pack()
        self.lista_prestamos = tk.Listbox(self.tab_prestamos, width=70, height=10)
        self.lista_prestamos.pack(pady=10)

    def prestar_libro(self):
        if not self.biblioteca_actual:
            messagebox.showerror("Error", "Selecciona una biblioteca primero.")
            return
        est = self.combo_est_prestamo.get()
        libro = self.combo_libro_prestamo.get()
        if est and libro:
            self.lista_prestamos.insert(tk.END, f"{est} -> {libro} ({date.today()})")
        else:
            messagebox.showerror("Error", "Selecciona estudiante y libro.")

    # ------------------ ACTUALIZAR LISTAS ------------------
    def actualizar_listas(self):
        # Libros
        self.lista_libros.delete(0, tk.END)
        if self.biblioteca_actual:
            for l in self.biblioteca_actual.libros:
                self.lista_libros.insert(tk.END, f"{l.titulo} - {l.isbn}")
        # Páginas
        self.lista_paginas.delete(0, tk.END)
        # Autores
        self.lista_autores.delete(0, tk.END)
        if self.biblioteca_actual:
            for a in self.biblioteca_actual.autores:
                self.lista_autores.insert(tk.END, f"{a.nombre} ({a.nacionalidad})")
        # Estudiantes
        self.lista_estudiantes.delete(0, tk.END)
        if self.biblioteca_actual:
            for e in self.estudiantes_dict[self.biblioteca_actual.nombre]:
                self.lista_estudiantes.insert(tk.END, f"{e.codigo} - {e.nombre}")
        # Combos
        if self.biblioteca_actual:
            self.combo_est_prestamo["values"] = [f"{e.codigo} - {e.nombre}" for e in self.estudiantes_dict[self.biblioteca_actual.nombre]]
            self.combo_libro_prestamo["values"] = [f"{l.titulo} - {l.isbn}" for l in self.biblioteca_actual.libros]

        # Bibliotecas
        self.combo_bibliotecas["values"] = [b.nombre for b in self.bibliotecas]

    # ------------------ GUARDAR Y CARGAR JSON ------------------
    def guardar_datos(self):
        datos = []
        for b in self.bibliotecas:
            datos.append({
                "nombre": b.nombre,
                "libros": [{"titulo": l.titulo, "isbn": l.isbn, "paginas": [{"numero": i+1, "contenido": p} for i, p in enumerate(l.paginas)]} for l in b.libros],
                "autores": [{"nombre": a.nombre, "nacionalidad": a.nacionalidad} for a in b.autores],
                "estudiantes": [{"codigo": e.codigo, "nombre": e.nombre} for e in self.estudiantes_dict.get(b.nombre, [])]
            })
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        if os.path.exists(ARCHIVO_JSON):
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                try:
                    datos = json.load(f)
                    for d in datos:
                        b = Biblioteca(d["nombre"])
                        for l in d.get("libros", []):
                            libro = Libro(l["titulo"], l["isbn"], l.get("paginas", []))
                            b.agregarLibro(libro)
                        for a in d.get("autores", []):
                            autor = Autor(a["nombre"], a["nacionalidad"])
                            b.agregarAutor(autor)
                        self.bibliotecas.append(b)
                        self.estudiantes_dict[b.nombre] = [Estudiante(e["codigo"], e["nombre"]) for e in d.get("estudiantes", [])]
                    if self.bibliotecas:
                        self.biblioteca_actual = self.bibliotecas[0]
                except json.JSONDecodeError:
                    self.bibliotecas = []
                    self.estudiantes_dict = {}

    # ------------------ CERRAR APLICACIÓN ------------------
    def cerrar_aplicacion(self):
        self.guardar_datos()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()
