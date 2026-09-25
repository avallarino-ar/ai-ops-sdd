# /ai-ops.ds.specify

Recibe la descripción de la iniciativa. Lee `.specify/memory/constitution.md` y la documentación del repositorio. Conserva datos confirmados y marca lo desconocido como decisión pendiente. Nunca inventes umbrales aprobados, rutas de acceso ni cumplimiento legal.

Crea `specs/<id>/spec.md` usando la plantilla `ai-ops-ds-spec-template.md` del preset (si no la encuentras, usa su contenido en este repositorio). Resume antes el alcance y los riesgos. Incluye identificadores de requisitos y criterios de aceptación observables. Para el trabajo de Data Science, considera: Definir población, ventana temporal, variable objetivo, cortes de entrenamiento/validación/test, leakage, baseline, métricas primarias y umbrales antes de entrenar. Registrar linaje, versiones, sesgo por segmentos, reproducibilidad y decisión de no desplegar.

Pregunta solo por vacíos que bloqueen decisiones; documenta supuestos menores. Presenta al final riesgos, pendientes, siguiente comando `/speckit.plan` y evidencia necesaria para cerrar la spec. No implementes código en este paso.
