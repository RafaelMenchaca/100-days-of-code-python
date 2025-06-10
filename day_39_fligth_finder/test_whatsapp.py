from notification_manager import NotificationManager
from dotenv import load_dotenv

load_dotenv()

# Instancia del gestor de notificaciones
notifier = NotificationManager()

# Mensaje de prueba
mensaje = (
    "✅ Este es un mensaje de prueba desde tu proyecto de Flight Deal Finder.\n\n"
    "Si lo ves en WhatsApp, todo está funcionando correctamente. 🚀"
)

# Enviar mensaje
notifier.send_message(mensaje)
