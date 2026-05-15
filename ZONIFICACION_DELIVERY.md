# ARansys - Zonificación y Logística de Delivery (Maturín)

## 1. Centro de Operaciones (Punto Cero)
* **Referencia:** Cruce de la Av. Rómulo Gallegos (Casco Central).
* **Metodología:** Cálculo por **Diámetros de Cobertura** (Circunferencias Concéntricas) para garantizar precisión geográfica en 360°.

## 2. Tabla de Tarifas por Diámetro
| Zona | Diámetro Total | Costo USD | Cobertura de Sectores (Ejemplos) |
| :--- | :--- | :--- | :--- |
| **D1: Núcleo** | 4 km | $2.00 | Centro, Catedral, Las Avenidas, Fundemos. |
| **D2: Urbano** | 10 km | $3.00 | Los Guaritos, La Floresta, Juanico, Palma Real. |
| **D3: Gran Maturín**| 16 km | $4.50 | Tipuro, Entrada a La Pica, San Jaime, Boquerón. |
| **D4: Límite** | 24 km | $6.00 | Zona Industrial (Final), San Miguel, La Pica. |

## 3. Protocolo Extra-Diámetro (Tarifas Especiales)
Cualquier coordenada GPS detectada fuera del **D4 (24 km)** activa el protocolo de contingencia:
* **Zonas Fuera de Rango:** Alcabala 58, Vía al Sur (después de San Miguel), El Furrial.
* **Mecánica de Cobro:** El sistema inhabilita el cobro automático y abre una negociación en el chat.
* **Cálculo Sugerido:** $0.80 por km adicional o mutuo acuerdo basado en el riesgo/retorno.
* **Evidencia:** El monto final debe ser escrito por el motorizado y aceptado por el cliente en el chat oficial.

## 4. Reglas de Control Quirúrgico
* **Validación Geográfica:** El sistema comparará el punto de recogida (Tienda) y entrega (Cliente) para asignar el diámetro correspondiente.
* **Seguridad GPS:** Activación de rastreo en tiempo real cada 5 segundos para entregas en el Diámetro 4 y Zonas Especiales.
* **Compromiso de Retorno:** Las tarifas D3 y D4 ya incluyen el factor de retorno para proteger la ganancia del repartidor.
