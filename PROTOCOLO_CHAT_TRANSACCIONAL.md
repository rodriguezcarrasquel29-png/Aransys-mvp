# ARansys - Protocolo de Chat Transaccional

## 1. El Chat como Entorno Seguro
* Todo acuerdo de venta debe ocurrir dentro del chat de la plataforma para ser reconocido por ARansys.
* Se prohíbe el envío de números telefónicos externos antes de la validación del cobro (opcional, para evitar fugas).

## 2. Flujo de Botones de Acción (WorkFlow)
1. **[Tienda] Botón 'Enviar Datos':** Muestra info de pago seleccionada por la tienda.
2. **[Cliente] Botón 'Reportar Pago':** Permite adjuntar captura y referencia. El estado cambia a 'Pendiente de Verificación'.
3. **[Tienda] Botón 'Validar Pago':** La tienda confirma ingreso de fondos. Dispara el cobro de comisión de ARansys.
4. **[Cliente] Botón 'Aceptar Mercancía':** El cliente confirma recepción. Finaliza la orden y habilita la calificación obligatoria.

## 3. Registro de Auditoría
* Cada acción de botón genera un 'Timestamp' (marca de tiempo) inalterable en la base de datos.
* Los chats están encriptados pero son accesibles para el Administrador en caso de disputa reportada.
