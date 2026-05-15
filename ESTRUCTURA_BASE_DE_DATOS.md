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
