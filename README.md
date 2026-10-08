# 🔐 Generador de Contraseñas Seguras y Portable

Aplicación ligera en Python con interfaz gráfica para generar contraseñas seguras personalizadas. Diseñada especialmente para superar restricciones estrictas de políticas de contraseñas (como *"Password cannot have consecutive repeating characters"* de gestores tipo NordPass o aplicaciones corporativas).

---

## ✨ Características Principales

* 🚫 **Sin caracteres consecutivos repetidos:** Garantiza que no existan dos caracteres iguales seguidos (evaluado de forma *case-insensitive*, evitando patrones como `aa`, `aA` o `11`).
* 🔤 **Palabra base personalizada:** Permite incluir una palabra inicial deseada manteniendo las reglas de seguridad.
* 🛡️ **Símbolos especiales seguros:** Utiliza únicamente símbolos compatibles con la mayoría de formularios web (`@#$%-+=!_?*`), evitando caracteres problemáticos como comillas, barras o espacios.
* 📐 **Longitud ajustable:** Define libremente el número de caracteres necesarios.
* 📋 **Copiado directo:** Botón para copiar la contraseña generada al portapapeles con un solo clic.
* 🚀 **100% Portable:** Disponible como ejecutable ejecutable (`.exe`) independiente sin necesidad de instalar Python.

---

## 🚀 Cómo usar la versión Portable (.exe)

1. Ve a la sección de **[Releases](../../releases)** en la barra lateral derecha de este repositorio.
2. Descarga el archivo **`generador.exe`** de la última versión.
3. Ejecútalo con doble clic en cualquier computadora con Windows (no requiere instalación ni permisos de administrador).

---

## 💻 Ejecución desde el Código Fuente

Si prefieres ejecutar el script en Python o modificar el código:

### Requisitos
* Python 3.x instalado.

### Pasos
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/christianjpp/generador-contrasenas.git](https://github.com/christianjpp/generador-contrasenas.git)
