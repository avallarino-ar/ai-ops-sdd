# Constitución de ingeniería · borrador 0.1.0

> Sustituir «AI Ops» y aprobar propietarios/umbrales antes de exigir esta política en CI.

## 1. Trazabilidad
Cada cambio significativo DEBE tener objetivo, alcance, requisitos verificables, propietario y vínculo entre especificación, tareas y PR. Las decisiones de arquitectura con impacto transversal DEBEN quedar documentadas.

## 2. Seguridad y privacidad
Los secretos DEBEN gestionarse fuera del código; el acceso a datos y servicios DEBE concederse por mínimo privilegio. Los datos personales y financieros DEBEN minimizarse; quedan prohibidos en logs y datasets de prueba no autorizados. Todo flujo sensible DEBE incluir revisión de amenazas, autorización y retención. Cualquier excepción requiere responsable y caducidad registrada.

## 3. Datos y contratos
Cada fuente DEBE tener propietario, definición, clasificación, vigencia y controles de calidad. Las interfaces de datos/API DEBEN incluir esquema, compatibilidad y manejo de errores. El acceso entre dominios DEBE usar contratos aprobados.

## 4. Calidad reproducible
Toda propuesta DEBE declarar un resultado observable y criterios de aceptación antes de implementar. Los cambios DEBEN incluir pruebas útiles para sus riesgos, instrucciones de despliegue/reversión y evidencia de verificación. En experimentos se DEBEN fijar cortes temporales, linaje, baseline y semillas cuando aplique.

## 5. Operación
Los servicios DEBEN definir métricas, alertas, responsables, límites de costo y respuesta ante fallos. El despliegue de capacidades de IA DEBE definir evaluación, revisión de seguridad, control de acceso a herramientas y estrategia de fallback proporcional al riesgo.

## Gobierno## Stack y excepciones
El perfil de AI Engineering adopta Vercel AI SDK cuando el servicio TypeScript lo permite; Frontend utiliza Node.js LTS y Next.js para aplicaciones nuevas cuando resulten adecuados. Cada repositorio DEBE fijar versiones de runtime y dependencias. Una alternativa requiere decisión documentada; ninguna regla de stack sustituye pruebas de compatibilidad, seguridad ni evaluación.


Propietarios: Engineering Platform + representantes de DS, AI Engineering y Frontend (confirmar). Cambios por PR con revisión de responsables. Versionado SemVer: PATCH aclara; MINOR añade reglas compatibles; MAJOR cambia obligaciones. Las excepciones se registran en cada spec con justificación, responsable y fecha de revisión.
