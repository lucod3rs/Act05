# ==========================================
# main.py
# archivo principal del proyecto
#======================================

# Importar las librerías necesarias
import tkinter as tk
from tkinter import messagebox

# Conectamos los módulos cofre y contrasena
from contrasena import Contrasena, LongitudInvalidaError
from cofre import Cofre


# Clase principal del juego
class JuegoCazador:
    #Inicialización de la clase
    def __init__(self):
        self.puntaje = 0
        self.nombre_jugador = ""

       # Variables para la interfaz gráfica 
        self.ventana = None
        self.entrada_nombre = None
        self.entrada_longitud = None
        self.etiqueta_marcador = None

    # Método para iniciar el juego
    def mostrar_recompensa(self, cofre, clave=""):
        #Crea una ventana emergente para mostrar la recompensa al jugador
        top = tk.Toplevel(self.ventana)
        top.title("¡RECOMPENSA!")
        top.geometry("320x280")
        top.resizable(False, False)
        
        top.transient(self.ventana) 
        top.grab_set()


        # Mostrar el nombre del cofre y los puntos obtenidos
        tk.Label(top, text=f"COFRE {cofre.nombre.upper()}", font=("Arial", 16)).pack(pady=15)
        tk.Label(top, text="").pack() 

        # Mostrar la clave correcta si el jugador no adivinó correctamente
        puntos_txt = f"{cofre.puntos} puntos" if cofre.puntos < 0 else f"+{cofre.puntos} puntos"
        tk.Label(top, text=puntos_txt, font=("Arial", 14)).pack(pady=5)

        # Si se proporcionó una clave, mostrarla en la ventana
        if clave: 
            tk.Label(top, text="Contraseña Cazada:", font=("Arial", 10, "italic")).pack(pady=(10,0))
            tk.Label(top, text=clave, font=("Courier", 12, "bold"), relief="ridge", padx=10, pady=5).pack(pady=5)
        
        # Botón Aceptar para cerrar la ventana de recompensa
        tk.Button(top, text="ACEPTAR", command=top.destroy, width=20, font=("Arial", 9)).pack(pady=15)

   
    # Método para iniciar la partida del juego, solicitando el nombre del jugador y mostrando el marcador inicial
    def iniciar_partida(self):
        nombre = self.entrada_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Atención", "Cazador, ingresa tu nombre.")
            return
        
        # Guardar el nombre del jugador y actualizar el marcador en la interfaz
        self.nombre_jugador = nombre
        self.etiqueta_marcador.config(text=f"CAZADOR: {self.nombre_jugador.upper()}  |  PUNTAJE: {self.puntaje}")
        messagebox.showinfo("Caza Iniciada", f"¡Bienvenido, {self.nombre_jugador}!")


# Método para ejecutar la acción de cazar, validando la longitud ingresada y mostrando la recompensa obtenida
    def ejecutar_caza(self):
        if not self.nombre_jugador: # Validación para asegurarse de que el jugador haya ingresado su nombre
            messagebox.showwarning("Atención", "Regístrate antes de cazar.")
            return
            
        txt_lon = self.entrada_longitud.get().strip() #obtiene el texto ingresado en la entrada de longitud
        
        try: # Validación de la longitud ingresada,validacion entero positivo
            if not txt_lon.isdigit():
                raise ValueError("Ingresa un número entero.")
            
            longitud = int(txt_lon)
            
            # Usamos la clase Contrasena importada de contrasena.py 
            password_obj = Contrasena(longitud)
            clave = password_obj.generar_contrasena()
            
            # Usamos la clase Cofre importada de cofre.py 
            cofre = Cofre.generar_cofre_aleatorio()
            self.puntaje += cofre.puntos
            self.mostrar_recompensa(cofre, clave)
            

        # Manejo de excepciones para casos de longitud inválida o errores en los datos ingresados por el jugador    
        except (LongitudInvalidaError, ValueError) as e:
            # Caso de cofre maldito por error en los datos
            cofre_maldito = Cofre.generar_cofre_maldito()
            self.puntaje += cofre_maldito.puntos
            self.mostrar_recompensa(cofre_maldito, f"Error: {e}")
            
            # Actualizar el marcador después de la caza, incluso en caso de error
        self.etiqueta_marcador.config(text=f"CAZADOR: {self.nombre_jugador.upper()}  |  PUNTAJE: {self.puntaje}")


#   Método para iniciar la interfaz gráfica del juego, creando la ventana principal 
#   y los elementos necesarios para la interacción del jugador
    def iniciar_juego(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cazador de Contraseñas")
        self.ventana.geometry("400x320")
        self.ventana.config(padx=20, pady=20)
        
        # Etiqueta para mostrar el nombre del jugador y el puntaje actual, se actualizará después de cada acción
        self.etiqueta_marcador = tk.Label(self.ventana, text="ESPERANDO CAZADOR...", 
                                          font=("Arial", 12, "bold"), fg="#2C3E50")
        self.etiqueta_marcador.pack(pady=(0, 20))

        # Frame para el registro del jugador, donde se solicita el nombre y se inicia la partida
        frame_reg = tk.LabelFrame(self.ventana, text=" Registro ", padx=10, pady=10)
        frame_reg.pack(fill="x", pady=5)
        
        # Elementos para el registro del jugador: etiqueta, entrada de texto y botón para iniciar la partida
        tk.Label(frame_reg, text="Nombre:").pack(side="left")
        self.entrada_nombre = tk.Entry(frame_reg, width=15)
        self.entrada_nombre.pack(side="left", padx=5)
        tk.Button(frame_reg, text="Registrar", command=self.iniciar_partida).pack(side="left", padx=5)

        # Frame para el panel de acción, donde se ingresa la longitud y se ejecuta la caza
        frame_caza = tk.LabelFrame(self.ventana, text=" Panel de Acción ", padx=10, pady=10)
        frame_caza.pack(fill="x", pady=15)
        
        # Elementos para el panel de acción: etiqueta, entrada de texto para la longitud y botón para ejecutar la caza
        tk.Label(frame_caza, text="Longitud (8-50):").pack(side="left")
        self.entrada_longitud = tk.Entry(frame_caza, width=8)
        self.entrada_longitud.pack(side="left", padx=5)
        
        # Botón para ejecutar la caza, que llama al método ejecutar_caza al ser presionado
        btn_cazar = tk.Button(frame_caza, text="¡ABRIR COFRE!", font=("Arial", 10, "bold"),
                              bg="#27AE60", fg="white", command=self.ejecutar_caza)
        btn_cazar.pack(side="left", padx=10)

        self.ventana.mainloop()

if __name__ == "__main__":
    JuegoCazador().iniciar_juego()