# ARansys - Protocolo de Identidad y Persistencia de Datos

## 1. Métodos de Autenticación
* **SSO Integration:** Soporte nativo para Google (Gmail) y Microsoft (Outlook/Hotmail).
* **Vinculación Única:** Una cuenta de correo solo puede estar vinculada a un perfil (Tienda, Técnico, Delivery o Cliente). No se permiten duplicados.

## 2. Backup y Sincronización en la Nube
* **Persistencia Total:** Toda transacción, mensaje y calificación se almacena en el servidor central con respaldo en espejo (Mirroring) cada 60 minutos.
* **Recuperación Multi-dispositivo:** El usuario puede acceder desde cualquier dispositivo; la data se sincroniza automáticamente al iniciar sesión.

## 3. Seguridad de Recuperación
* **PIN Reset:** El cambio de PIN crítico requiere validación por correo electrónico Y código SMS (2FA).
* **Logs de Actividad:** Registro de los últimos 10 dispositivos que accedieron a la cuenta para detectar ingresos no autorizados.

## 4. Política de 'Cero Pérdida'
* ARansys mantiene copias de seguridad cifradas en tres ubicaciones geográficas distintas para garantizar que la data de los clientes en Maturín sea indestructible ante fallas de servidores.
