# ARansys - Estructura de Datos (Tienda de Maturín)

## 1. Módulo de Usuarios (Autenticación)
* **Campos Obligatorios:** ID_Usuario, Correo, Contraseña (Encriptada), Teléfono, Rol (Cliente/Técnico/Tienda).
* **Perfiles:**
    * **Clientes:** Nombre, Puntos de Fidelidad (1-15 para delivery gratis).
    * **Técnicos:** Nombre, Especialidad (Multicategoría), Años de Experiencia, Foto de Cédula (Validación).
    * **Tiendas:** Nombre Empresa, RIF (Validación), Teléfono WhatsApp, Dirección GPS (Lat/Long).

## 2. Módulo de Inventario (Tiendas)
Cada producto registrado tendrá los siguientes atributos:
* **ID_Producto / ID_Tienda:** Para vincular el producto a su dueño.
* **Fotos:** Array de hasta 3 URLs de imágenes.
* **Detalles:** Nombre, Descripción, Precio ($), Stock disponible, Estado (Nuevo/Usado).
* **Garantía:** Definida por la tienda (Ej: "7 días", "Sin garantía").
* **Horario de Atención:** Rango de horas y días activos para la venta.

## 3. Módulo de Interacción (Q&A)
Sistema de preguntas públicas sobre artículos:
* **ID_Pregunta:** Vinculada al Producto y al Usuario que pregunta.
* **Texto_Pregunta / Texto_Respuesta:** Comunicación pública para otros compradores.
* **Estatus:** (Pendiente por responder / Respondida).

## 4. Módulo de Monedero y Comisiones
* **Saldo_Real:** Dinero recargado por el aliado (Tasa ARansys: Promedio BCV/Binance).
* **Saldo_Bono:** $5.00 de cortesía (No retirables).
* **Transacciones:** Registro de descuentos (3% - 5% ventas / $3.00 contacto técnico / $0.50 mínimo).

## 5. Módulo de Reputación
* **Calificaciones:** Tabla vinculada a la venta final.
* **Criterio:** Estrellas (1-5) y comentario obligatorio para cerrar el ciclo de compra.
* **Monitor de Reembolsos:** Registro de incidencias para técnicos por falta de contacto.
