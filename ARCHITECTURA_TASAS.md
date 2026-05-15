# ARansys - Arquitectura de Tasas de Cambio

## 1. Definición de la Tasa ARansys
Para garantizar un equilibrio económico entre el costo operativo y la accesibilidad para el cliente, se establece la **Tasa ARansys** como el promedio aritmético entre la tasa oficial del Banco Central de Venezuela (BCV) y la tasa de referencia del mercado (Binance P2P).

### Fórmula:
Tasa_ARansys = (Tasa_BCV + Tasa_Binance) / 2

## 2. Automatización del Cálculo
El sistema contará con un módulo de sincronización automática:
* **Frecuencia:** Actualización diaria (sugerido 9:00 AM y 1:00 PM).
* **Fuentes:** Conexión vía API/WebScraping a portales oficiales y Binance P2P.
* **Respaldo:** En caso de falla de conexión, se activará un "Modo Manual" para que el administrador asigne la tasa.

## 3. Transparencia y Auditoría
Cada vez que el sistema actualice la tasa, se generará un registro con:
* Fecha y hora exacta.
* Valor capturado de las fuentes.
* Tasa resultante aplicada al monedero.

## 4. Aplicación en Recargas
El monedero interno se maneja en **Dólares ($)**. Al momento de una recarga, el sistema calculará los Bolívares necesarios multiplicando el monto en dólares solicitado por la **Tasa ARansys** vigente.
