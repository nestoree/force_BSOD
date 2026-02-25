# 🟦 force_BSOD

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%2011-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Este repositorio contiene un script sencillo en Python diseñado para forzar un **Pantallazo Azul (BSOD)** en Windows 11. El método utilizado es la finalización forzada de un proceso crítico del sistema (`wininit.exe`), lo que provoca un error inmediato de tipo `CRITICAL_PROCESS_DIED`.

> [!CAUTION]
> **ADVERTENCIA DE SEGURIDAD:** Este script cerrará tu sistema inmediatamente sin guardar cambios. Úsalo bajo tu propia responsabilidad. Asegúrate de haber guardado todo tu trabajo antes de ejecutarlo. El autor no se hace responsable de pérdidas de datos.

---

## 🛠️ ¿Cómo funciona?

El script utiliza la librería `os` de Python para enviar una señal de terminación forzada al proceso **Windows Initialization Process** (`wininit.exe`). Dado que este proceso es vital para el funcionamiento del sistema operativo, el Kernel de Windows entra en un estado de pánico defensivo y detiene toda actividad para proteger la integridad del sistema.



---

## 🚀 Uso Rápido

### Requisitos previos
1. **Sistema Operativo:** Windows 10 o Windows 11.
2. **Lenguaje:** [Python 3.x](https://www.python.org/) instalado y añadido al PATH.
3. **Privilegios:** Es obligatorio ejecutar la terminal como **Administrador**.

### Instrucciones
1. Descarga el archivo `force_bsod.py` de este repositorio.
2. Abre una **Terminal** o **PowerShell** con permisos de administrador.
3. Ejecuta el script con el siguiente comando:
   ```
   python force_bsod.py
   ```
## 📄 El Código
```
    import os
    import ctypes
    import sys

    def is_admin():
        """Verifica si el script se está ejecutando con privilegios de administrador."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def trigger_bsod():
        if not is_admin():
            print("[-] Error: Este script requiere privilegios de administrador.")
            print("[!] Por favor, abre la terminal como administrador y reintenta.")
            return

        print("[+] Invocando el pantallazo azul en 3, 2, 1...")
        
        # Comando para matar el proceso crítico wininit.exe
        # /F = Fuerza el cierre
        # /IM = Especifica el nombre de la imagen (proceso)
        os.system("taskkill /F /IM wininit.exe")

    if __name__ == "__main__":
        trigger_bsod()
```
## ❓ Preguntas Frecuentes

¿Esto romperá mi PC de forma permanente?

**No**. Al reiniciar el ordenador, Windows volverá a cargar todos los procesos correctamente desde el disco duro. Es un error provocado en la memoria RAM, no un daño físico o de archivos persistentes.

¿Qué riesgos existen?

- Pérdida de datos: Cualquier archivo abierto no guardado se perderá.
- Corrupción de caché: En casos muy raros, si el PC estaba escribiendo datos importantes en el momento del crash, un archivo podría quedar corrupto.

¿Por qué falla si no soy Administrador?

Windows protege sus procesos críticos contra usuarios estándar y malware común. Sin privilegios elevados, el sistema denegará el comando taskkill sobre procesos del sistema.

## ⚖️ Descargo de Responsabilidad
Este software se proporciona "tal cual", sin garantía de ningún tipo. El uso de este script es puramente educativo o para pruebas de diagnóstico. No se recomienda su uso en entornos de producción, servidores o equipos con datos críticos sin respaldo.
