# ARansys - Flujo de Interfaz de Usuario (UI/UX)

## PANTALLA 1: INICIO
* Buscador central (Keyword Search).
* Selector de categorías visuales.
* Display de saldo en Tasa ARansys.

## PANTALLA 2: RESULTADOS DE BÚSQUEDA
* Grid de productos con foto, precio y distancia.
* Sistema de ordenamiento por cercanía (Anillos GPS).

## PANTALLA 3: FICHA DE PRODUCTO
* Galería de imágenes.
* Botón de 'Asesoría Técnica' (Experimental).
* Botón de 'Comprar' con cálculo de delivery incluido.

## PANTALLA 4: TRACKING Y SEGURIDAD
* Mapa en tiempo real (Leaflet/OSM).
* Generador de Código de Validación (4 dígitos).
* Chat directo con el Delivery/Tienda.

## PANTALLA 5: POST-VENTA
* Formulario de calificación (Estrellas).
* Botón de 'Apelación' (Solo visible si hay calificación negativa).
* Botón 'Solicitar Instalación' (Vincula a un técnico).
## PANTALLA 4: TRANSACCIÓN Y SEGUIMIENTO
* **Pago Directo:** El sistema facilita la transferencia de saldo entre el Cliente y la Tienda. ARansys NO retiene ni congela fondos.
* **Confirmación de Disponibilidad:** Se recomienda el uso del chat interno antes de procesar el pago para validar stock físico.
* **Resolución de Conflictos de Stock:** En caso de error de inventario post-pago, la Tienda es responsable directa de la devolución del dinero al Cliente. ARansys actúa como testigo del registro de la transacción para posibles apelaciones.
## 6. PROTOCOLO DE VALIDACIÓN PRE-COMPRA
* **Interacción Obligatoria:** El flujo de UI debe incentivar al usuario a usar el chat de confirmación antes de procesar cualquier pago.
* **Estado de Inventario Dinámico:** Si la tienda confirma disponibilidad por chat, se genera un 'Token de Validación' temporal (ej. 15 min) que permite al cliente finalizar la compra.
* **Responsabilidad de Actualización:** Es deber de la Tienda marcar productos como 'Agotados' manualmente si la venta se realiza fuera de la plataforma (Venta de mostrador).
