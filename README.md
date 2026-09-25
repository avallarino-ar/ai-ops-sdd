# AI Ops SDD · starter corporativo

Distribución de prácticas de desarrollo guiado por especificaciones para Data Science, AI Engineering y Frontend. Versión inicial `0.3.0` para pilotos; sustituye `ai-ops` por el nombre de tu organización y valida las reglas con Seguridad, Datos y Plataforma antes de convertirlas en controles obligatorios.

## Prueba local (sin catálogo)

1. Instala `uv` y Spec Kit desde una versión oficial fijada y compatible con presets: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@<TAG_VERIFICADO>`; comprueba `specify --version` y `specify preset --help`. Anota el tag elegido en `docs/compatibilidad.md`.
2. Crea o entra en un repositorio de prueba: `specify init --here --ai codex` (usa `claude` u otra integración si corresponde; consulta `specify init --help`).
3. Desde el proyecto de prueba, instala ambos presets (ajusta la ruta a este checkout):

```bash
specify preset add --dev /ruta/ai-ops-sdd/presets/ai-ops-base --priority 20
specify preset add --dev /ruta/ai-ops-sdd/presets/ai-ops-ai-engineering --priority 10
specify preset list
```

Reemplaza `ai-ops-ai-engineering` por `ai-ops-data-science` o `ai-ops-frontend`. El número menor tiene mayor prioridad. Para probar otra disciplina en el mismo proyecto, quita primero el preset especializado. Los comandos se registran en la integración activa; reinicia tu agente si aún no aparecen.

4. Dentro de Codex/Claude ejecuta `/ai-ops.ai.specify` (o `/ai-ops.ds.specify`, `/ai-ops.front.specify`), luego los comandos estándar `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`. Los comandos del perfil piden los artefactos complementarios y enlazan con los comandos estándar. Los nombres visibles pueden depender de la integración; inspecciona el directorio de comandos generado.
5. Copia `policy/constitution.md` a `.specify/memory/constitution.md` en el proyecto piloto, revísala y reemplaza sus campos organizacionales. Mantén esa constitución versionada dentro del proyecto.

## Contenido

- `policy/`: principios comunes, seguridad y decisiones de gobierno.
- `presets/`: manifiestos reales Spec Kit con comandos y plantillas de cada disciplina.
- `profiles/`: ciclos, artefactos y criterios de aceptación de cada equipo.
- `examples/`: casos de prueba concretos aplicados a activación, asistente de inversión e interfaz.
- `checks/check_sdd.py`: validación local de estructura, referencias y contenido mínimo.
- `bundles/`: manifiestos de composición para publicar tras registrar los componentes en catálogos.
- `docs/publicacion.md`: versionado, distribución, instalación y actualización.

## Alcance de este starter

La primera prueba es local y reproducible sin catálogo. Los bundles se validan y consumen una vez que sus presets estén publicados. No presupone que rutas de GitHub, modelos, umbrales de calidad o controles internos estén aprobados; los valores relevantes quedan marcados como decisiones del equipo. Los comandos de agente son instrucciones y requieren revisión humana de los artefactos resultantes.

## Validación

```bash
python3 checks/check_sdd.py
```

Para probar con el CLI instalado: `specify preset add --dev ./presets/ai-ops-base` desde un proyecto piloto inicializado y `specify bundle validate --path ./bundles/ai-ops-ai-engineering --offline` (este último puede advertir referencias no instaladas). Referencias oficiales en `docs/referencias.md`.
