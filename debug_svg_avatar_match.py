from pathlib import Path
import re

for fname in ['banner.svg', 'banner-light.svg', 'lanyard.svg']:
    text = Path(fname).read_text(encoding='utf-8')
    print('FILE:', fname)
    pos = text.find('<image')
    print('image pos:', pos)
    if pos >= 0:
        start = max(0, pos - 120)
        end = min(len(text), pos + 120)
        snippet = text[start:end]
        print(snippet)
    else:
        print('no <image> found')
    print('\n---\n')
    if fname != 'lanyard.svg':
        m = re.search(r'(<g transform="translate\(780 170\)" clip-path="url\(#avatarClip\)">.*?</g>)', text, re.S)
        print('group match:', bool(m))
        if m:
            print(m.group(1)[:500])
    else:
        m = re.search(r'(<circle cx="160" cy="190" r="42" fill="#0f3f6b" />.*?<circle cx="160" cy="190" r="44" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0\.8" />)', text, re.S)
        print('lanyard match:', bool(m))
        if m:
            print(m.group(1)[:500])
    print('========================\n')
