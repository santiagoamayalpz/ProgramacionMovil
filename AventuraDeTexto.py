import tkinter as tk
from tkinter import messagebox

class SimuladorEstudiante:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Simulador: Programación Móvil")
        self.ventana.geometry("700x500")

        self.pantalla = tk.Label(ventana, text="", wraplength=600, font=("Segoe UI", 12), justify="left")
        self.pantalla.pack(pady=40, padx=30)

        self.marco_opciones = tk.Frame(ventana)
        self.marco_opciones.pack(pady=20)

        self.ir_a("inicio")

    def limpiar(self):
        for b in self.marco_opciones.winfo_children():
            b.destroy()

    def ir_a(self, escena):
        self.limpiar()

        if escena == "inicio":
            self.pantalla.config(text="Primer día de clase con el profesor Ivan Isay Guerra. El salón está lleno y escuchas que la materia de Programación Móvil es pesada por los proyectos. El profesor empieza a explicar el plan de la asignatura y el reglamento. ¿Qué decides hacer?")
            tk.Button(self.marco_opciones, text="Poner atención a los detalles", command=lambda: self.ir_a("detalles")).pack(side="left", padx=10)
            tk.Button(self.marco_opciones, text="Revisar qué tan difícil está el temario", command=lambda: self.ir_a("temario")).pack(side="left", padx=10)

        elif escena == "detalles":
            self.pantalla.config(text="Te enteras de cosas importantes: necesitas el 80% de asistencia para no perder el derecho a examen y solo hay 10 minutos de tolerancia. Además, queda prohibido el uso de audífonos y comida en el salón. ¿Crees que puedas cumplir con todo?")
            tk.Button(self.marco_opciones, text="Sí, parece razonable", command=lambda: self.ir_a("unidad1")).pack()

        elif escena == "temario":
            self.pantalla.config(text="Ves que son 4 unidades: desde lo básico hasta publicar la app. Lo que más resalta es que el Proyecto Integrador del tercer parcial vale el 50% de la nota. Es mucho peso para un solo trabajo.")
            tk.Button(self.marco_opciones, text="Anotarlo y seguir con la clase", command=lambda: self.ir_a("unidad1")).pack()

        elif escena == "unidad1":
            self.pantalla.config(text="Unidad 1: Introducción. El profesor pide un resumen de exposición y unos ejercicios en Classroom sobre la estructura de las apps. Estás cansado y la tarea es para hoy mismo. ¿Cómo la vas a entregar?")
            tk.Button(self.marco_opciones, text="Hacerla por mi cuenta", command=lambda: self.ir_a("unidad2")).pack(side="left", padx=10)
            tk.Button(self.marco_opciones, text="Pedirle el archivo a alguien más", command=lambda: self.ir_a("duda_plagio")).pack(side="left", padx=10)

        elif escena == "duda_plagio":
            self.pantalla.config(text="Un compañero te pasa su archivo. Recuerdas que el reglamento es muy claro: si detectan plagio o copia, repruebas la materia de inmediato. ¿Vale la pena el riesgo?")
            tk.Button(self.marco_opciones, text="Mejor no, la hago yo solo", command=lambda: self.ir_a("unidad2")).pack(side="left", padx=10)
            tk.Button(self.marco_opciones, text="Entregar el archivo ajeno", command=lambda: self.ir_a("muerte_plagio")).pack(side="left", padx=10)

        elif escena == "muerte_plagio":
            messagebox.showerror("Resultado", "El profesor revisó los archivos y se dio cuenta. Te aplicaron el reglamento y perdiste la materia.")
            self.ir_a("inicio")

        elif escena == "unidad2":
            self.pantalla.config(text="Unidad 2: Diseño de interfaces. Estamos en pleno julio y tienes problemas para que las notificaciones de la app funcionen. No logras avanzar. ¿Qué intentas ahora?")
            tk.Button(self.marco_opciones, text="Pedir una asesoría con el profesor", command=lambda: self.ir_a("asesoria")).pack(side="left", padx=10)
            tk.Button(self.marco_opciones, text="Intentar resolverlo buscando en internet", command=lambda: self.ir_a("unidad3")).pack(side="left", padx=10)

        elif escena == "asesoria":
            self.pantalla.config(text="Fuiste a asesoría y el profesor te explicó cómo funcionan los servicios en segundo plano. Te ahorraste horas de frustración y ya tienes lista la práctica para el segundo parcial.")
            tk.Button(self.marco_opciones, text="Continuar a la Unidad 3", command=lambda: self.ir_a("unidad3")).pack()

        elif escena == "unidad3":
            self.pantalla.config(text="Unidad 3: Programación y sensores. Es la parte más larga del curso. El profesor te recuerda que ya debes tener un avance real del Proyecto Integrador porque vale el 50%. ¿En qué te vas a enfocar?")
            tk.Button(self.marco_opciones, text="Priorizar el Proyecto Integrador", command=lambda: self.ir_a("unidad4")).pack(side="left", padx=10)
            tk.Button(self.marco_opciones, text="Estudiar solo para el examen", command=lambda: self.ir_a("fallo_puntos")).pack(side="left", padx=10)

        elif escena == "fallo_puntos":
            self.pantalla.config(text="Sacaste buena nota en el examen, pero como no entregaste el proyecto, no te dio el promedio para pasar. Los porcentajes de la evaluación no perdonan.")
            tk.Button(self.marco_opciones, text="Volver a intentar", command=lambda: self.ir_a("inicio")).pack()

        elif escena == "unidad4":
            self.pantalla.config(text="Llegaste a la Unidad 4: Publicación. Solo falta empaquetar y desplegar la app. Sin embargo, te das cuenta de que has faltado un par de veces y estás en el límite del 80%. ¿Qué haces?")
            tk.Button(self.marco_opciones, text="No faltar a ninguna clase más", command=lambda: self.ir_a("victoria")).pack(side="left", padx=10)
            tk.Button(self.marco_opciones, text="Arriesgarte y faltar para avanzar el código", command=lambda: self.ir_a("fallo_asistencia")).pack(side="left", padx=10)

        elif escena == "fallo_asistencia":
            self.pantalla.config(text="Faltaste una vez más y bajaste del 80% de asistencia. El profesor revisó la lista final y perdiste el derecho a la evaluación final.")
            tk.Button(self.marco_opciones, text="Reiniciar", command=lambda: self.ir_a("inicio")).pack()

        elif escena == "victoria":
            self.pantalla.config(text="¡Felicidades! Lograste cumplir con las asistencias, entregaste el proyecto a tiempo y publicaste tu aplicación. Ya terminaste Programación Móvil con éxito.")
            tk.Button(self.marco_opciones, text="Cerrar programa", command=self.ventana.quit).pack()

if __name__ == "__main__":
    root = tk.Tk()
    juego = SimuladorEstudiante(root)
    root.mainloop()