import customtkinter

customtkinter.set_appearance_mode("dasrk")  
customtkinter.set_default_color_theme("blue")  


class PreguntaFrame(customtkinter.CTkFrame):
    def __init__(self, master, pregunta):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, text=pregunta)

        self.slider = customtkinter.CTkSlider(self, from_=1, to=5, number_of_steps=5)
        self.slider.grid(row=1, column=0, padx=10, pady=(10,0), sticky="w")

class App(customtkinter.CTk):
    ANCHO = 1000
    ALTO = 800
    RUTA_PREGUNTAS = "preguntas.txt"

    def __init__(self):
        super().__init__()
        self.preguntas = self.set_preguntas()
        self.construir_ui()
        
        self.sliders = []

    def construir_ui(self):
        self.title("Evaluador SUS")
        self.geometry(f"{App.ANCHO}x{App.ALTO}")
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

        self.slider_frame = PreguntaFrame(self, self.preguntas[0])
        self.slider_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")
    
    def set_preguntas(self):
        archi = open(self.RUTA_PREGUNTAS, "r")
        preguntas = archi.readlines()
        archi.close()
        return preguntas
    
    

    def lanzar(self):
        self.mainloop()

    
        
if __name__ == "__main__":
    app = App()
    app.lanzar()
# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("1000x800")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# app.mainloop()

