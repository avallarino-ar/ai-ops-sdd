#!/usr/bin/env python3
"""Validación estructural sin dependencias externas."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
for slug, short in (("data-science", "ds"), ("ai-engineering", "ai"), ("frontend", "front")):
    paths = [f"presets/ai-ops-{slug}/preset.yml", f"presets/ai-ops-{slug}/commands/ai-ops.{short}.specify.md", f"presets/ai-ops-{slug}/commands/ai-ops.{short}.review.md", f"presets/ai-ops-{slug}/templates/ai-ops-{short}-spec-template.md", f"bundles/ai-ops-{slug}/bundle.yml", f"profiles/{slug}.md"]
    for path in paths:
        assert (ROOT/path).is_file(), f"Falta {path}"
    m = (ROOT/paths[0]).read_text()
    for ref in re.findall(r'^\s+file: "([^"]+)"', m, re.M):
        assert (ROOT/f"presets/ai-ops-{slug}"/ref).is_file(), f"Referencia rota: {ref}"
    bundle = (ROOT/paths[4]).read_text()
    assert f'id: "ai-ops-{slug}"' in bundle and 'id: "ai-ops-base"' in bundle
assert (ROOT/'policy/constitution.md').is_file()
print('Estructura y referencias locales: OK (3 perfiles, base, 3 bundles)')
