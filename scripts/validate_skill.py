#!/usr/bin/env python3
"""Offline structure checks only; does not evaluate model behavior or scientific claims."""
from __future__ import annotations
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts: dict[str, int] = {}
    def check(ok: bool, message: str) -> None:
        if not ok:
            errors.append(message)
    def read(name: str) -> str:
        try:
            return (root / name).read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'{name}: {exc}')
            return ''
    required = ['SKILL.md', 'README.md', 'CHANGELOG.md', 'agents/openai.yaml',
                'assets/icon.svg', 'assets/chinese-revision-worksheet.md',
                'references/revision-rubric.md', 'references/engineering-robotics.md',
                'references/chinese-algorithm-writing.md', 'references/algorithm-evidence-audit.md',
                'references/chinese-rewrite-examples.md', 'references/corpus-source-notes.md',
                'evals/chinese-algorithm-cases.json', 'scripts/validate_skill.py']
    for name in required:
        check((root / name).is_file(), f'Missing: {name}')
    skill = read('SKILL.md')
    front = skill.split('---', 2)
    check(skill.startswith('---\n') and len(front) == 3, 'Invalid frontmatter boundaries')
    header = front[1] if len(front) == 3 else ''
    check(bool(re.search(r'^name: revise-paper-draft$', header, re.M)), 'Skill name missing/changed')
    check(bool(re.search(r'^description: .+', header, re.M)), 'Description missing')
    interface = read('agents/openai.yaml')
    for field in ['interface:', '$revise-paper-draft', 'allow_implicit_invocation: true']:
        check(field in interface, f'Missing interface value: {field}')
    # Required fields only, not general YAML grammar or client compatibility.
    links = 0
    for path in sorted(root.rglob('*.md')):
        body = read(path.relative_to(root).as_posix())
        check(not re.search(r'turn\d+file\d+|sandbox:/|/mnt/data/', body), f'Runtime reference: {path.name}')
        check(len(re.findall(r'^\s*```', body, re.M)) % 2 == 0, f'Unbalanced fences: {path.name}')
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', body):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            check(dest.is_relative_to(root) and dest.exists(), f'Broken/escaping link: {target}')
            links += 1
    counts['relative_links'] = links
    ids: set[str] = set()
    for name, prefix, number in [
        ('chinese-algorithm-writing.md', 'L', 12), ('chinese-algorithm-writing.md', 'S', 8),
        ('algorithm-evidence-audit.md', 'A', 14), ('chinese-rewrite-examples.md', 'E', 16),
        ('corpus-source-notes.md', 'P', 17)]:
        found = re.findall(r'^#{2,3} (' + prefix + r'\d{2})\b', read('references/' + name), re.M)
        expected = {f'{prefix}{n:02d}' for n in range(1, number + 1)}
        check(set(found) == expected and len(found) == number, f'Invalid/duplicate {prefix} IDs')
        ids.update(found)
        counts[prefix] = len(found)
    try:
        data = json.loads(read('evals/chinese-algorithm-cases.json'))
        cases = data['cases']
        check(data['evaluation_status'] == 'not_run', 'Fixtures must not imply executed evaluation')
        check(len(cases) == 20 and len({c['id'] for c in cases}) == 20, 'Expected 20 unique cases')
        for case in cases:
            check(set(case['rules']).issubset(ids) and bool(case['rules']), f'Unknown rule: {case["id"]}')
            for key in ['id', 'request', 'evidence', 'must', 'must_not']:
                check(isinstance(case.get(key), str) and bool(case[key].strip()), f'Invalid {key}')
        counts['behavior_fixtures'] = len(cases)
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid fixtures: {exc}')
    try:
        ET.parse(root / 'assets/icon.svg')
    except (OSError, ET.ParseError) as exc:
        errors.append(f'Invalid icon: {exc}')
    prohibited = {'.pdf', '.docx', '.pptx', '.ttf', '.otf'}
    check(not any(p.suffix.lower() in prohibited for p in root.rglob('*') if p.is_file()),
          'Unexpected source documents or fonts')
    return errors, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    errors, counts = validate(parser.parse_args().root.resolve())
    if errors:
        print('\n'.join('ERROR: ' + e for e in errors), file=sys.stderr)
        return 1
    print(json.dumps({'status': 'passed', 'scope': 'static_structure_only', 'counts': counts,
                      'model_behavior_evaluation': 'not_run'}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
