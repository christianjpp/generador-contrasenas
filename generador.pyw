import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

SIMBOLOS_SEGUROS = "@#$%-+=!_?*"

def generar_password(longitud, palabra_base, usar_numeros, usar_simbolos):
    # Validar que la palabra base no tenga letras repetidas consecutivas (case-insensitive)
    for i in range(len(palabra_base) - 1):
        if palabra_base[i].lower() == palabra_base[i+1].lower():
            raise ValueError(f"La palabra base contiene caracteres repetidos consecutivos ('{palabra_base[i]}').")

    if len(palabra_base) >= longitud:
        return palabra_base[:longitud]

    # Conjuntos de caracteres según la selección del usuario
    conjunto_mayusculas = string.ascii_uppercase
    conjunto_minusculas = string.ascii_lowercase
    conjunto_numeros = string.digits if usar_numeros else ""
    conjunto_simbolos = SIMBOLOS_SEGUROS if usar_simbolos else ""

    pool_general = conjunto_mayusculas + conjunto_minusculas + conjunto_numeros + conjunto_simbolos

    # Intentos para garantizar que la contraseña contenga todos los tipos requeridos
    for _ in range(100):
        password = list(palabra_base)
        
        while len(password) < longitud:
            caracter = secrets.choice(pool_general)
            # Evitar caracteres consecutivos iguales (case-insensitive)
            if password and caracter.lower() == password[-1].lower():
                continue
            password.append(caracter)

        pwd_str = "".join(password)

        # Confirmar que cumple con todas las reglas seleccionadas
        tiene_mayus = any(c in conjunto_mayusculas for c in pwd_str)
        tiene_minus = any(c in conjunto_minusculas for c in pwd_str)
        tiene_num = any(c in conjunto_numeros for c in pwd_str) if usar_numeros else True
        tiene_simb = any(c in conjunto_simbolos for c in pwd_str) if usar_simbolos else True

        if tiene_mayus and tiene_minus and tiene_num and tiene_simb:
            return pwd_str

    return pwd_str

def accion_generar():
    try:
        longitud = int(entry_longitud.get())
        palabra = entry_palabra.get().strip()
        numeros = var_numeros.get()
        simbolos = var_simbolos.get()
        
        if longitud < 4:
            messagebox.showwarning("Atención", "La longitud mínima recomendada es 4.")
            return

        if not numeros and not simbolos and not palabra:
            messagebox.showwarning("Atención", "Debes seleccionar al menos una opción o ingresar una palabra base.")
            return

        pwd = generar_password(longitud, palabra, numeros, simbolos)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, pwd)
    except ValueError as e:
        msg = str(e) if "repetidos" in str(e) else "Ingresa un número entero válido para la longitud."
        messagebox.showerror("Error", msg)

def copiar_portapapeles():
    pwd = entry_resultado.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Éxito", "¡Contraseña copiada al portapapeles!")

# Configuración de la Ventana Principal
root = tk.Tk()
root.title("Generador Portable de Contraseñas")
root.geometry("420x370")
root.resizable(False, False)

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Campo: Palabra Base
ttk.Label(frame, text="Palabra base (opcional):").pack(anchor=tk.W, pady=(0, 2))
entry_palabra = ttk.Entry(frame)
entry_palabra.pack(fill=tk.X, pady=(0, 10))

# Campo: Longitud
ttk.Label(frame, text="Longitud total de caracteres:").pack(anchor=tk.W, pady=(0, 2))
entry_longitud = ttk.Entry(frame)
entry_longitud.insert(0, "16")
entry_longitud.pack(fill=tk.X, pady=(0, 10))

# Selector: Números
var_numeros = tk.BooleanVar(value=True)
chk_numeros = ttk.Checkbutton(frame, text="Incluir números (0-9)", variable=var_numeros)
chk_numeros.pack(anchor=tk.W, pady=(0, 5))

# Selector: Símbolos seguros
var_simbolos = tk.BooleanVar(value=True)
chk_simbolos = ttk.Checkbutton(frame, text="Incluir símbolos seguros (@#$%-+=!_?*)", variable=var_simbolos)
chk_simbolos.pack(anchor=tk.W, pady=(0, 15))

# Botón Generar
btn_generar = ttk.Button(frame, text="⚡ Generar Contraseña", command=accion_generar)
btn_generar.pack(fill=tk.X, pady=(0, 10))

# Resultado
entry_resultado = ttk.Entry(frame, font=("Consolas", 12), justify="center")
entry_resultado.pack(fill=tk.X, pady=(0, 10))

# Botón Copiar
btn_copiar = ttk.Button(frame, text="📋 Copiar al Portapapeles", command=copiar_portapapeles)
btn_copiar.pack(fill=tk.X)

root.mainloop()