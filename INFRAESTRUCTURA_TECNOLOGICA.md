# ARansys - Manifiesto de Infraestructura de Costo Cero

## 1. Stack Tecnológico de Código Abierto
* **Motor de Mapas:** OpenStreetMap con librería Leaflet.js (Alternativa a Google Maps).
* **Gestor de Datos:** PostgreSQL (Alternativa a bases de datos comerciales).
* **Servidor Web:** Nginx con certificados SSL de Let's Encrypt.
* **Lenguaje:** Python (FastAPI) y React/Vue (Frontend), operando en contenedores Docker.

## 2. Estrategia de Mensajería
* **Notificaciones Operativas:** Integración con Telegram Bot API para alertas de pedidos, entregas y suspensiones.
* **Respaldo:** Uso de correos electrónicos vía servidores SMTP locales o gratuitos (Gmail/Outlook).

## 3. Optimización de Servidor
* **Alojamiento:** Servidor VPS básico.
* **Carga de Imágenes:** Procesamiento local para reducir el peso de las fotos de repuestos antes de ser almacenadas, optimizando el espacio en disco.
