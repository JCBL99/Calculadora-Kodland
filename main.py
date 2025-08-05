import tkinter as tk
from tkinter import font

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora Kodland')
        self.root.configure(bg='#2E2E2E')
        self.root.resizable(False, False)

        # Configurar fuente personalizada
        self.fuente_botones = font.Font(family='Helvetica', size=12, weight='bold')
        self.fuente_pantalla = font.Font(family='Courier New', size=16, weight='bold')

        # Frame principal
        self.main_frame = tk.Frame(self.root, bg='#2E2E2E', padx=10, pady=10)
        self.main_frame.pack()

        # Pantalla de la calculadora
        self.pantalla = tk.Entry(
            self.main_frame, 
            width=20, 
            bg='#455A64', 
            fg='#FFFFFF', 
            borderwidth=0, 
            justify='right', 
            font=self.fuente_pantalla, 
            insertbackground='white')
        
        self.pantalla.grid(row=0,column=0, columnspan=4, pady=(0,15), ipady=10, sticky='ew')

        self.crear_botones()

        # Footer
        self.footer = tk.Label(
            self.main_frame,
            text='© 2023 Kodland Calculator',
            bg='#2E2E2E', 
            fg='#757575',
            font=('Arial', 8)
        )

    def crear_botones(self):
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in botones:

            if text.isdigit():
                bg_color = '#616161'  # Gris para números
            elif text == 'C':
                bg_color = '#D32F2F'  # Rojo para limpiar
            elif text == '=':
                bg_color = '#388E3C'  # Verde para igual
            else:
                bg_color = '#FF9800'  # Naranja para operadores

            
            button = tk.Button(
                self.main_frame, 
                text=text, 
                bg=bg_color,
                fg='#FFFFFF', 
                activebackground='#BDBDBD',
                activeforeground='#212121',
                relief='raised',
                borderwidth=0,
                padx=20, 
                pady=15,
                font=self.fuente_botones,
                command=lambda t=text: self.boton_click(t)
            )

            button.grid(row=row, column=col, padx=3, pady=3, sticky='nsew')

            # Efecto hover
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg=self.lighten_color(btn.cget('bg'))))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg=self.get_original_color(btn.cget('text'))))

            # Configurar tamaño de las columnas y filas
            self.main_frame.columnconfigure(col, weight=1)
            self.main_frame.rowconfigure(row, weight=1)

    def lighten_color(self, color):
        
        r, g, b = self.hex_to_rgb(color)
        
        r = min(255, int(r * 1.2))
        g = min(255, int(g * 1.2))
        b = min(255, int(b * 1.2))
        return self.rgb_to_hex(r, g, b)
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def rgb_to_hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def get_original_color(self, text):
        if text.isdigit():
            return '#616161'
        elif text == 'C':
            return '#D32F2F'
        elif text == '=':
            return '#388E3C'
        else:
            return '#FF9800'
            

    def boton_click(self, valor):
        if valor == "=":
            try:
                expression = self.pantalla.get()
                expression = expression.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, result)
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")

        elif valor == "C":
            self.pantalla.delete(0, tk.END)
        else:
            current = self.pantalla.get()
            self.pantalla.delete(0, tk.END)

            display_val = valor
            if valor == '*':
                display_val = '×'
            elif valor == '/':
                display_val = '÷'
            self.pantalla.insert(0, current + display_val)

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()