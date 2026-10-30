from abc import ABC, abstractmethod
import random

class Canal(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, texto: str) -> None:
        return True

class CanalEmail(Canal):
    def enviar(self, destinatario: str, texto: str) -> None:
        print(f"EMAIL a {destinatario}: {texto}")
        return True

class CanalSMS(Canal):
    def enviar(self, destinatario, texto):
        texto_corto = texto[:30]
        print(f"SMS a {destinatario}: {texto_corto}")
        return True

class CanalWhatsapp(Canal):
    def enviar(self, destinatario, texto):
        if random.choice([True, False]) == True:
            print(f"Whatsapp a {destinatario}: {texto_corto}")
            return True
        else:
            return False
        

class Notificacion:
    def __init__(self, canal):
        self.canal = canal


    def notificar(self, destinatario, mensaje) -> None:
        self.canal.enviar(destinatario)


# Prueba

aviso = Notificacion(CanalEmail())
aviso.notificar("ana@corro.com", "Entrega de un proyecto el viernes")
