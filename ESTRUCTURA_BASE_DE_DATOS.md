# ARansys - Esquema de Base de Datos (Relacional)

## 1. Entidades Principales
* **Usuarios:** Gestión de perfiles, autenticación (SSO) y roles.
* **Tiendas:** Registro legal, geolocalización y catálogo de repuestos.
* **Técnicos/Delivery:** Registro de disponibilidad, vehículos y especialidades.
* **Transacciones:** Registro de pedidos, estados de entrega y códigos de validación.

## 2. Relaciones Críticas
* Una **Tienda** tiene muchos **Productos**.
* Una **Orden** vincula a un **Cliente**, una **Tienda**, un **Delivery** y opcionalmente un **Técnico**.
* Las **Calificaciones** se vinculan directamente al ID de la Orden para evitar fraudes.

## 3. Seguridad de Datos
* Las contraseñas y PINs nunca se guardan en texto plano (Uso de Hashing).
* Copias de seguridad automáticas cada 24 horas en un volumen separado.
## 4. Definición de Integridad Rígida (SQL Strict Mode)
* **Tipos de Datos Estrictos:** Uso de DECIMAL para finanzas y UUID para identificadores.
* **Foreign Keys (FK):** Ningún registro puede existir huérfano; todo pedido debe estar amarrado a un usuario y una tienda existente.
* **Constraints (Restricciones):**
    - El stock nunca puede ser negativo.
    - El precio debe ser mayor a 0.
    - Los correos electrónicos deben seguir el formato estándar.
* **Triggers de Auditoría:** Registro automático de quién modificó un precio y a qué hora.
