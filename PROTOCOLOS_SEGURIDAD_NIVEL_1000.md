# ARansys - Protocolos de Seguridad Estricta (Nivel 1000/10)

## 1. Segregación de Datos (Silos)
* **Independencia Total:** Ningún actor (Cliente, Técnico, Tienda) tiene permisos de lectura/escritura sobre tablas ajenas a su rol y propiedad.
* **Aislamiento por Token:** Cada petición al servidor debe ir acompañada de un token de seguridad que valida la identidad y los permisos del propietario de los datos.

## 2. Blindaje de Transacciones
* **Inmutabilidad del Chat:** Los registros de confirmación de pago y entrega son inalterables. Ni siquiera la tienda puede borrar un registro una vez validado.
* **Validación Cruzada de Pagos:** El sistema marcará como 'Sospechoso' cualquier número de referencia de pago móvil que se repita en el sistema en menos de 90 días.

## 3. Seguridad de Identidad (KYC Avanzado)
* **Verificación de Técnicos:** Carga obligatoria de Cédula de Identidad y Foto en tiempo real (Selfie) para comparar con el documento.
* **Reporte de Actividad:** Registro de IP y Geolocalización en cada inicio de sesión exitoso.

## 4. Cifrado y Respaldo
* **AES-256:** Cifrado de datos bancarios y personales sensibles.
* **Backup Desconectado:** Respaldo diario de la base de datos en un servidor espejo fuera de la red principal para prevenir ataques de Ransomware.
## 5. Persistencia de Sesión (Rol: Tienda)
* **Sesión Persistente:** Las cuentas de tipo 'Tienda' mantendrán la sesión activa de forma indefinida hasta que se ejecute un cierre manual por parte del usuario.
* **Capas de Re-autenticación:** Se implementará un PIN de seguridad de 4 dígitos (Quick-PIN) exclusivamente para acciones críticas:
  * Modificación de datos de cobro/bancarios.
  * Gestión de retiros de saldo.
  * Cambio de contraseña o correos de contacto.
* **Optimización de Notificaciones:** Uso de tecnología Push y WebSockets para garantizar que la tienda reciba alertas de chat y ventas sin necesidad de refrescar la sesión o re-ingresar credenciales.
# ARansys - Seguridad de Enlace e Información (Modelo Puente)

## 1. Misión de Seguridad
ARansys no es una pasarela de pago. Su función es garantizar que la información de contacto, cuentas bancarias y direcciones fluya de forma íntegra y privada entre las partes.

## 2. Inmutabilidad de Datos de Pago
* **Cero Edición:** Una vez que una tienda registra sus métodos de pago, cualquier modificación requiere el PIN del Propietario.
* **Blindaje en Chat:** Los datos de pago enviados al cliente dentro del chat son 'Solo Lectura'. El sistema garantiza que el cliente reciba exactamente lo que el dueño de la tienda configuró.

## 3. Privacidad y Acceso
* **Visualización Dinámica:** La información sensible (direcciones exactas, teléfonos) está oculta por defecto y solo se revela a la contraparte cuando existe una transacción activa y validada en el chat.
