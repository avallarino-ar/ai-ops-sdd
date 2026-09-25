# /ai-ops.ai.review

Lee la spec, plan, tasks, artefactos complementarios y cambios de código del feature actual. Contrasta cada criterio de aceptación con evidencia observable y registra resultado en `specs/<id>/review.md` con columnas requisito, evidencia, estado, responsable y acción. Verifica los gates del perfil AI Engineering: Definir límites del agente, fuentes y herramientas, permisos, AI Gateway, versiones de prompts, conjunto de evaluación, fallas esperadas, coste/latencia, privacidad, inyección de prompts, fallback y criterios de rollback.

Señala errores, riesgos y faltantes con rutas y líneas cuando existan. No declares aprobado lo que no se haya medido. No despliegues, publiques ni alteres datos reales.

Verifica la decisión de stack, versiones fijadas y evidencia de integración exigida por el perfil.
