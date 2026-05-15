# ARansys - Sistema de Búsqueda e Inteligencia de Mercado

## 1. Algoritmo de Búsqueda Rápida
* **Indexación en Tiempo Real:** Los productos subidos por las tiendas deben ser rastreables en menos de 1 segundo.
* **Jerarquía de Resultados:** 1. Coincidencia exacta del nombre.
    2. Menor distancia al usuario (Geolocalización).
    3. Mejor reputación de la tienda.
* **Visualización:** Foto miniatura, precio en $, distancia y botón directo al chat.

## 2. Gestión de "Cero Resultados" (Radar de Demanda)
* **Captura de Intención:** Si una búsqueda no arroja resultados, el sistema registra el término exacto de búsqueda.
* **Archivo de Inteligencia:** Generación de un reporte dinámico para los socios (Tiendas) sobre la demanda insatisfecha.
* **Notificación de 'Repuesto en Camino':** Si una tienda carga un producto que estaba en el radar de faltantes, el sistema puede notificar a los usuarios que lo buscaron recientemente.

## 3. Filtros Avanzados
* Por marca (Samsung, LG, Whirlpool, etc.).
* Por estado (Nuevo, Original, Genérico).
* Por disponibilidad de delivery inmediato.
