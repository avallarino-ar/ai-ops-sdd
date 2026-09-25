# AI Engineering

## Ciclo
caso de uso → responsabilidad IA → arquitectura → diseño de evaluación → implementación → seguridad → despliegue → monitoreo.

## Artefactos sugeridos
`spec.md`, `architecture.md`, `evaluation.md`, `operations.md`; guardar por feature/experimento bajo `specs/<id>/`. El `spec.md` estándar de Spec Kit sigue siendo punto de entrada cuando aplica.

## Control mínimo
Definir límites del agente, fuentes y herramientas, permisos, AI Gateway, versiones de prompts, conjunto de evaluación, fallas esperadas, coste/latencia, privacidad, inyección de prompts, fallback y criterios de rollback.

## Gate previo a implementación## Stack corporativo preferido
- Para servicios TypeScript que integran modelos, streaming, generación de objetos o herramientas, usar **Vercel AI SDK** como biblioteca de aplicación. Documentar la versión y las API concretas de la versión fijada en el proyecto.
- Acceder a modelos mediante **AI Gateway corporativo** y su endpoint compatible cuando exista. Verificar en un spike la compatibilidad real entre proveedor/adaptador del AI SDK, autenticación, streaming, tool calling y telemetría antes de escoger la integración. No asumir que cualquier gateway es compatible de forma automática.
- Separar reglas de negocio, prompts versionados, definición de herramientas y acceso a modelos; mantener pruebas y evaluaciones independientes del proveedor.
- Si el servicio usa otro lenguaje o una capacidad no soportada, registrar alternativa, motivo, impacto y responsable en `architecture.md`. La elección de AI SDK no obliga a adoptar Next.js.


Responsable de negocio/producto revisa criterios de éxito; responsable técnico revisa contratos y riesgos; el equipo fija evidencia reproducible. Toda sección no aplicable se marca «N/A» con motivo.

## Gate de entrega
Demostrar resultado frente a baseline o aceptación, riesgos residuales, responsables, telemetría y cómo revertir o detener el cambio.
