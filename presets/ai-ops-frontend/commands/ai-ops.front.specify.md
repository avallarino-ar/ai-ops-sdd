# /ai-ops.front.specify

Recibe la descripción de la iniciativa. Lee `.specify/memory/constitution.md` y la documentación del repositorio. Conserva datos confirmados y marca lo desconocido como decisión pendiente. Nunca inventes umbrales aprobados, rutas de acceso ni cumplimiento legal.

Crea `specs/<id>/spec.md` usando la plantilla `ai-ops-front-spec-template.md` del preset (si no la encuentras, usa su contenido en este repositorio). Resume antes el alcance y los riesgos. Incluye identificadores de requisitos y criterios de aceptación observables. Para el trabajo de Frontend, considera: Definir flujos, diseño responsive, estados loading/empty/error/success, manejo de sesión y permisos, teclado y lector de pantalla, instrumentación, performance, pruebas visuales y criterios de aceptación.

Pregunta solo por vacíos que bloqueen decisiones; documenta supuestos menores. Presenta al final riesgos, pendientes, siguiente comando `/speckit.plan` y evidencia necesaria para cerrar la spec. No implementes código en este paso. Registra Node.js LTS y Next.js como stack preferido cuando corresponda, con versiones fijadas y decisiones sobre renderizado y caché.
