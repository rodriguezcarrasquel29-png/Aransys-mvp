# ARansys - Lógica de Negocio: Proyecto Tienda de Maturín

## 1. Visión General
Tienda de Maturín es una plataforma de integración comercial y técnica diseñada para conectar proveedores de repuestos, servicios técnicos y logística (delivery) en el estado Monagas. El modelo se basa en la democratización del acceso digital para comercios locales bajo una estructura de costos variables.

## 2. Modelo de Ingresos: Comisiones y Tarifas
El sistema de monetización se rige por el éxito en las ventas de los aliados:

* **Comisión Estándar:** 3% sobre el valor de cada venta concretada a través de la plataforma.
* **Comisión Premium:** 5% para comercios que opten por posicionamiento destacado y mayor visibilidad en el feed principal.
* **Tarifa de Protección (Micro-transacciones):** Se aplicará un cobro mínimo de **$0.50** por transacción en ventas cuyo 3% sea inferior a dicha cifra. Esto garantiza la sostenibilidad operativa del servidor y la plataforma.

## 3. Sistema de Gestión: El Monedero Virtual (Escrow/Wallet)
Para eliminar la fricción en la cobranza y asegurar el flujo de caja, ARansys implementa un sistema de **Prepago mediante Monedero Virtual**:

* **Recarga Obligatoria:** Tanto tiendas como técnicos deben mantener un saldo positivo en su monedero dentro de la App para permanecer visibles.
* **Descuento Automatizado:** El sistema descontará en tiempo real la comisión correspondiente (3%, 5% o tarifa mínima) al confirmarse cada transacción.
* **Suspensión Automática:** Si el saldo del monedero llega a $0, el perfil del aliado se ocultará automáticamente de las búsquedas hasta que se realice una nueva recarga.

## 4. Roles de Usuario y Operatividad
* **Comercios:** Encargados de la actualización de inventarios y confirmación de ventas.
* **Técnicos:** Prestadores de servicio especializado bajo modalidad de monedero por contacto efectivo.
* **Riders (Delivery):** Gestión logística con comisiones por zona (Anillo 1: $2, Anillo 2: $3.5, Anillo 3: $5).
* **ARansys (Admin):** Supervisión de transacciones, mediación de garantías y liquidación de pagos a los delivery.
## 5. Sistema de Reputación y Confianza
Para garantizar la calidad del servicio, ARansys implementa un sistema de validación social:

### A. Perfil del Aliado (Tiendas y Técnicos)
* **Barra de Calificación:** Un indicador visual basado en estrellas (1-5) que resume el promedio de satisfacción de los clientes.
* **Trayectoria:** Mención explícita de los "Años en el Mercado". Este dato es vital para generar autoridad y confianza en negocios establecidos de Maturín.
* **Multicategoría (Técnicos):** Los técnicos pueden registrar múltiples especialidades (ej. Refrigeración + Electrónica), aumentando su visibilidad.

### B. Sistema de Calificación Triple
Al finalizar cada transacción, el cliente tendrá la obligación/derecho de calificar:
1. **Tienda:** Calidad del producto y veracidad de lo publicado (Positivo / Regular / Negativo).
2. **Técnico:** Puntualidad, conocimiento y trato al cliente.
3. **Delivery:** Rapidez y estado del paquete al llegar.

### C. Dinámica para Técnicos (Pago por Selección)
* **Costo por Contacto:** Se descontarán **$3.00** del monedero del técnico únicamente cuando el cliente presione el botón "Elegir este Técnico".
* **Transparencia:** Tras el cobro, el sistema libera los datos de contacto (WhatsApp/Teléfono) para la coordinación del servicio.
## 6. Política de Reembolso Protegido para Técnicos
Para garantizar la equidad en el sistema de "Pago por Selección", se establece el siguiente protocolo de protección al técnico:

* **Derecho a Reclamo:** Si tras el descuento de los $3.00 el técnico no logra establecer contacto con el cliente (número errado, el cliente no responde tras 24h, o el servicio fue cancelado por el cliente antes de la visita), el técnico podrá presionar el botón "Reportar Incidencia".
* **Validación:** ARansys verificará la situación (mediante un mensaje rápido al cliente o revisión de tiempos).
* **Reembolso:** De comprobarse la falla en el contacto, los $3.00 serán devueltos íntegramente al "Saldo Real" del monedero del técnico en un plazo máximo de 12 horas.
