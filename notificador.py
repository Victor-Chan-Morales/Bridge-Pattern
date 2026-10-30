from abc import ABC, abstractmethod

class Canal(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, texto: str) -> None:

class CanalEmail(Canal):
    def enviar(self, destinatario: str, texto: str) -> None:
        print(f"EMAIL a {destinatario}: {texto}")

class CanalSMS(Canal):
    def enviar(self, destinatario, texto):
        texto_corto = texto[:30]
        print(f"SMS a {destinatario}: {texto_corto}")

class Notificacion:
    def __init__(self, canal):
        self.canal = canal


    def notificar(self, destinatario, mensaje) -> None:
        self.canal.enviar(destinatario)


# Prueba

aviso = Notificacion(CanalEmail())
aviso.notificar("ana@corro.com", "Entrega de un proyecto el viernes")