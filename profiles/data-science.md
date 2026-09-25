# Data Science

## Ciclo
problema → datos → hipótesis → baseline → experimento → evaluación → decisión → transferencia.

## Artefactos sugeridos
`problem.md`, `data.md`, `experiment.md`, `evaluation.md`, `decision.md`; guardar por feature/experimento bajo `specs/<id>/`. El `spec.md` estándar de Spec Kit sigue siendo punto de entrada cuando aplica.

## Control mínimo
Definir población, ventana temporal, variable objetivo, cortes de entrenamiento/validación/test, leakage, baseline, métricas primarias y umbrales antes de entrenar. Registrar linaje, versiones, sesgo por segmentos, reproducibilidad y decisión de no desplegar.

## Gate previo a implementación
Responsable de negocio/producto revisa criterios de éxito; responsable técnico revisa contratos y riesgos; el equipo fija evidencia reproducible. Toda sección no aplicable se marca «N/A» con motivo.

## Gate de entrega
Demostrar resultado frente a baseline o aceptación, riesgos residuales, responsables, telemetría y cómo revertir o detener el cambio.
