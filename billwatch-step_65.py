# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: BillWatch
def merge_imports(source_lines):
    existing = {}
    for line in source_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('"') or stripped.startswith("'") or stripped.startswith('import') or stripped.startswith('from') or stripped.startswith('import ') or stripped.startswith('from '):
            continue
        if stripped.startswith('import '):
            names = [n.strip() for n in stripped[len('import '):].split(',')]
            for name in names:
                name = name.strip()
                if ' as ' in name:
                    alias, real = name.split(' as ')
                    existing[real.strip()] = alias.strip()
                else:
                    existing[name] = name
        elif stripped.startswith('from '):
            parts = stripped[len('from '):].split(' import ')
            module = parts[0].strip()
            names = [n.strip() for n in parts[1].split(',')]
            for name in names:
                name = name.strip()
                if ' as ' in name:
                    alias, real = name.split(' as ')
                    existing[real.strip()] = alias.strip()
                else:
                    existing[name] = name
    return existing
