# /ai-ops.ds.review

Lee la spec, plan, tasks, artefactos complementarios y cambios de código del feature actual. Contrasta cada criterio de aceptación con evidencia observable y registra resultado en `specs/<id>/review.md` con columnas requisito, evidencia, estado, responsable y acción. Verifica los gates del perfil Data Science: Definir población, ventana temporal, variable objetivo, cortes de entrenamiento/validación/test, leakage, baseline, métricas primarias y umbrales antes de entrenar. Registrar linaje, versiones, sesgo por segmentos, reproducibilidad y decisión de no desplegar.

Señala errores, riesgos y faltantes con rutas y líneas cuando existan. No declares aprobado lo que no se haya medido. No despliegues, publiques ni alteres datos reales.
