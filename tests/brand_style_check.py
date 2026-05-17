from pathlib import Path

html = Path('index.html').read_text()

assert '<title>My Digital Flo' in html, 'title should use My Digital Flo brand, not License & Scale'
assert '<strong>My Digital Flo</strong>' in html, 'header wordmark should say My Digital Flo'
assert 'src="logo.webp"' in html, 'header should use the official logo.webp asset'

for token in ['#050509', '#0a0a12', '#00a0ff', '#00c8ff']:
    assert token in html.lower(), f'missing brand token {token}'

for leakage in [
    'License & Scale',
    '#ff4fd8',
    '#a855f7',
    '#7c3aed',
    '#d9b4ff',
    'Instrument Serif',
]:
    assert leakage not in html, f'found off-brand reference: {leakage}'

print('Brand style checks passed')
