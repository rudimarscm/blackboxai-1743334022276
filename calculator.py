import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Custom font
        self.custom_font = font.Font(size=20)
        
        # Variables
        self.current_input = ""
        self.total = 0
        self.operation = None
        self.reset_screen = False
        
        # Create display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=self.custom_font, 
            bd=0, 
            insertwidth=0,
            justify="right",
            bg="#ffffff",
            fg="#333333",
            readonlybackground="#ffffff",
            state="readonly"
        )
        self.display.pack(fill=tk.X, ipady=20, padx=20, pady=20)
        
        # Create buttons frame
        buttons_frame = tk.Frame(root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
        
        # Button layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]
        
        # Create buttons
        for row in buttons:
            row_frame = tk.Frame(buttons_frame, bg="#f0f0f0")
            row_frame.pack(expand=True, fill=tk.BOTH)
            
            for btn_text in row:
                btn = tk.Button(
                    row_frame,
                    text=btn_text,
                    font=self.custom_font,
                    bd=0,
                    command=lambda t=btn_text: self.on_button_click(t),
                    bg="#e0e0e0" if btn_text not in ['/', '*', '-', '+', '='] else "#f8a145",
                    fg="#333333",
                    activebackground="#d0d0d0",
                    activeforeground="#333333",
                    relief=tk.RAISED
                )
                if btn_text == '=':
                    btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, ipady=10)
                else:
                    btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, ipady=10, padx=2, pady=2)
    
    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            if self.reset_screen:
                self.current_input = ""
                self.reset_screen = False
            self.current_input += button_text
            self.display_var.set(self.current_input)
        elif button_text == 'C':
            self.current_input = ""
            self.total = 0
            self.operation = None
            self.display_var.set("0")
        elif button_text in ['+', '-', '*', '/']:
            if self.current_input:
                self.calculate()
                self.operation = button_text
                self.total = float(self.current_input)
                self.current_input = ""
                self.display_var.set(str(self.total))
        elif button_text == '=':
            if self.current_input and self.operation:
                self.calculate()
                self.operation = None
                self.reset_screen = True
    
    def calculate(self):
        try:
            if self.operation == '+':
                self.total += float(self.current_input)
            elif self.operation == '-':
                self.total -= float(self.current_input)
            elif self.operation == '*':
                self.total *= float(self.current_input)
            elif self.operation == '/':
                self.total /= float(self.current_input)
            else:
                self.total = float(self.current_input)
            
            self.current_input = str(self.total)
            self.display_var.set(self.current_input)
        except ZeroDivisionError:
            self.display_var.set("Error")
            self.current_input = ""
            self.total = 0
            self.operation = None

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()