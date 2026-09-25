# Publicación y adopción

## Versión
Publicar `ai-ops-base` y cada perfil de forma independiente. Usar `0.x` durante pilotos y `1.0.0` tras revisión de propietarios y una implementación real por perfil. PATCH: redacción sin cambio conductual; MINOR: sección/comando compatible; MAJOR: cambio de entregables o gate. Fijar el core por tag y registrar matriz en `compatibilidad.md`.

## Etapa 1: pilotos locales
Instalar presets con `--dev` en proyectos temporales. Inspeccionar `specify preset list`, plantillas resueltas y comandos generados. Ejecutar los ejemplos y revisar los artefactos con el responsable de cada disciplina.

## Etapa 2: distribución
Crear un ZIP por preset con `preset.yml` en la raíz, subirlo a GitHub Releases o un registro privado accesible por HTTPS y publicar el catálogo de presets según el esquema del tag elegido. En el proyecto consumidor registrar `specify preset catalog add <URL> --name ai-ops --install-allowed`; instalar por ID y prioridad. Solo entonces validar y construir cada bundle con `specify bundle validate --path bundles/<perfil>` y `specify bundle build --path bundles/<perfil> --output dist`. Publicar ZIPs de bundles y un catálogo de bundles; registrar mediante `specify bundle catalog add <URL> --policy install-allowed --priority 5 --id ai-ops`. Probar desde un checkout vacío, con permisos equivalentes a los developers. Un repo privado requiere acceso autenticado al catálogo y a cada ZIP; comprobar ese acceso antes de recomendar comandos por ID.

## Actualización
Una actualización del preset por `specify preset update` remueve y vuelve a instalar; probarla en rama, pues puede perder modificaciones locales de archivos gestionados. Para bundles publicados usar `specify bundle update <id>`; para fuente local `specify bundle install <ruta> --refresh`. Fijar versiones exactas de los componentes en bundles y abrir PR por cada adopción. Verificar los componentes instalados tras actualizar: la instalación idempotente puede omitir una versión ya presente. Conservar rollback por release anterior y revisar cambios de constitución de cada proyecto.

## CI sugerida
Validar YAML, referencias, comandos y plantillas; ejecutar `checks/check_sdd.py`; probar cada preset con Spec Kit fijado y una integración activa; generar una spec de muestra por perfil; revisar manualmente seguridad, claridad y utilidad. Publicar releases solo después de ese smoke test. Nunca publicar secretos ni datos reales en las muestras.
