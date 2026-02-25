# 🟦 force_BSOD

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%2011-lightgrey.svg)
![Method](https://img.shields.io/badge/method-ntdll.dll-red.svg)

Este repositorio contiene un script avanzado en Python para forzar un **Pantallazo Azul (BSOD)** en Windows 11. A diferencia de otros métodos que intentan cerrar procesos, este utiliza llamadas directas a la API nativa de Windows (`ntdll.dll`) para invocar un error crítico del sistema.

> [!CAUTION]
> **ADVERTENCIA:** Este script detendrá el sistema de forma inmediata. No habrá advertencias de guardado. Úsalo exclusivamente en entornos de prueba o máquinas virtuales.

---

## 🛠️ ¿Cómo funciona?

El script evita las restricciones de acceso denegado de `taskkill` mediante dos pasos técnicos:
1. **RtlAdjustPrivilege**: Eleva los privilegios del script para obtener permisos de apagado/error a nivel de Kernel (Privilegio 19).
2. **NtRaiseHardError**: Envía una señal de error fatal al sistema con el parámetro de respuesta `6`, lo que obliga al Kernel a ejecutar un *Bug Check* (BSOD).

Este método es mucho más eficaz en versiones modernas de Windows 11 donde los procesos críticos están protegidos contra administradores estándar.

---

## 🚀 Uso

### Requisitos
* **Windows 10/11.**
* **Python 3.x**.
* **Permisos de Administrador** (necesarios para interactuar con `ntdll.dll`).

### Ejecución
1. Abre la **Terminal** o **PowerShell** como **Administrador**.
2. Lanza el script:
   ```
   python advanced_bsod.py
   ```

---

## 📄 Código Fuente

```
import ctypes
import os

def trigger_win11_bsod():
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))

    response = ctypes.c_uint()
    
    print("Ejecutando llamada directa al Kernel... Adiós Windows.")
    
    ctypes.windll.ntdll.NtRaiseHardError(
        0xC0000022, 
        0,          
        0,          
        0,          
        6,          
        ctypes.byref(response)
    )

if __name__ == "__main__":
    trigger_win11_bsod()
```

---

## ❓ FAQ

¿Por qué este método y no taskkill?
Windows 11 ha reforzado la seguridad de procesos como wininit.exe. Incluso como administrador, el sistema suele devolver "Acceso denegado". Usar la API nativa se salta esa capa de protección de la interfaz de usuario.

¿Es reversible?
Sí. Al reiniciar el ordenador, el sistema cargará normalmente. No modifica archivos en el disco, solo detiene la ejecución actual en la memoria RAM.

---

## ⚖️ Descargo de Responsabilidad

Este proyecto tiene fines estrictamente educativos y de diagnóstico. El autor no se hace responsable por el mal uso de esta herramienta o la pérdida de datos que pueda ocasionar.
