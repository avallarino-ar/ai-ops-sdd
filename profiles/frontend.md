# Frontend

## Ciclo
problema de usuario → UX → contrato API → estados → implementación → accesibilidad → verificación.

## Artefactos sugeridos
`spec.md`, `ux.md`, `api-contract.md`, `verification.md`; guardar por feature/experimento bajo `specs/<id>/`. El `spec.md` estándar de Spec Kit sigue siendo punto de entrada cuando aplica.

## Control mínimo
Definir flujos, diseño responsive, estados loading/empty/error/success, manejo de sesión y permisos, teclado y lector de pantalla, instrumentación, performance, pruebas visuales y criterios de aceptación.

## Gate previo a implementación## Stack corporativo preferido
- **Node.js LTS** como entorno de desarrollo y ejecución cuando corresponda; fijar versión en el repositorio (`.nvmrc`, `.node-version` o `engines`) y usar el gestor de paquetes aprobado con lockfile.
- **Next.js** para nuevas aplicaciones web, con TypeScript. Documentar la versión fijada, router elegido, límites entre código de servidor y cliente, estrategia de renderizado, manejo de caché y autenticación.
- Las aplicaciones existentes o casos que exijan otro framework registran la justificación en `ux.md` o ADR. Node.js es el runtime y Next.js es el framework; la especificación describe requisitos sin imponer una solución cuando aún se evalúan alternativas.


Responsable de negocio/producto revisa criterios de éxito; responsable técnico revisa contratos y riesgos; el equipo fija evidencia reproducible. Toda sección no aplicable se marca «N/A» con motivo.

## Gate de entrega
Demostrar resultado frente a baseline o aceptación, riesgos residuales, responsables, telemetría y cómo revertir o detener el cambio.
