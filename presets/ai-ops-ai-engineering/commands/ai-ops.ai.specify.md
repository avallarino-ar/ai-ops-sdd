# /ai-ops.ai.specify

Recibe la descripción de la iniciativa. Lee `.specify/memory/constitution.md` y la documentación del repositorio. Conserva datos confirmados y marca lo desconocido como decisión pendiente. Nunca inventes umbrales aprobados, rutas de acceso ni cumplimiento legal.

Crea `specs/<id>/spec.md` usando la plantilla `ai-ops-ai-spec-template.md` del preset (si no la encuentras, usa su contenido en este repositorio). Resume antes el alcance y los riesgos. Incluye identificadores de requisitos y criterios de aceptación observables. Para el trabajo de AI Engineering, considera: Definir límites del agente, fuentes y herramientas, permisos, AI Gateway, versiones de prompts, conjunto de evaluación, fallas esperadas, coste/latencia, privacidad, inyección de prompts, fallback y criterios de rollback.

Pregunta solo por vacíos que bloqueen decisiones; documenta supuestos menores. Presenta al final riesgos, pendientes, siguiente comando `/speckit.plan` y evidencia necesaria para cerrar la spec. No implementes código en este paso. Revisa si aplica Vercel AI SDK y registra la compatibilidad comprobada con AI Gateway, especialmente streaming y llamadas a herramientas.
