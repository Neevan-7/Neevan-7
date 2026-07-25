from pathlib import Path
import re

replacements = {
    "banner.svg": (
        re.compile(r'(?s)<g transform="translate\(780 170\)" clip-path="url\(#avatarClip\)">.*?</g>'),
        "  <g transform=\"translate(780 170)\" clip-path=\"url(#avatarClip)\">\n"
        "    <rect x=\"0\" y=\"0\" width=\"260\" height=\"260\" rx=\"28\" ry=\"28\" fill=\"#081322\" />\n"
        "    <circle cx=\"130\" cy=\"130\" r=\"70\" fill=\"#0f3b5f\" />\n"
        "    <circle cx=\"130\" cy=\"130\" r=\"64\" fill=\"#0a2f4a\" />\n"
        "    <circle cx=\"130\" cy=\"94\" r=\"28\" fill=\"#1c4963\" />\n"
        "    <circle cx=\"110\" cy=\"90\" r=\"8\" fill=\"#cde8ff\" />\n"
        "    <circle cx=\"150\" cy=\"90\" r=\"8\" fill=\"#cde8ff\" />\n"
        "    <path d=\"M104 150 C115 166 145 166 156 150\" stroke=\"#81d4ff\" stroke-width=\"5\" fill=\"none\" stroke-linecap=\"round\" />\n"
        "    <path d=\"M90 60 C100 34 120 22 130 22 C140 22 160 34 170 60\" fill=\"none\" stroke=\"#0ea5e9\" stroke-width=\"4\" opacity=\"0.8\" />\n"
        "    <rect x=\"16\" y=\"210\" width=\"228\" height=\"28\" rx=\"14\" fill=\"#0c3660\" />\n"
        "    <rect x=\"16\" y=\"210\" width=\"228\" height=\"28\" rx=\"14\" fill=\"none\" stroke=\"#00e5ff\" stroke-width=\"1.5\" />\n"
        "    <text x=\"30\" y=\"230\" font-family=\"Inter, sans-serif\" font-size=\"14\" fill=\"#dbeafe\">Developer</text>\n"
        "  </g>"
    ),
    "banner-light.svg": (
        re.compile(r'(?s)<g transform="translate\(780 170\)" clip-path="url\(#avatarClip\)">.*?</g>'),
        "  <g transform=\"translate(780 170)\" clip-path=\"url(#avatarClip)\">\n"
        "    <rect x=\"0\" y=\"0\" width=\"260\" height=\"260\" rx=\"28\" ry=\"28\" fill=\"#eef4fb\" />\n"
        "    <circle cx=\"130\" cy=\"130\" r=\"70\" fill=\"#9bb8d7\" />\n"
        "    <circle cx=\"130\" cy=\"130\" r=\"64\" fill=\"#dbe7f5\" />\n"
        "    <circle cx=\"130\" cy=\"94\" r=\"28\" fill=\"#b4c9e0\" />\n"
        "    <circle cx=\"110\" cy=\"90\" r=\"8\" fill=\"#ffffff\" />\n"
        "    <circle cx=\"150\" cy=\"90\" r=\"8\" fill=\"#ffffff\" />\n"
        "    <path d=\"M104 150 C115 166 145 166 156 150\" stroke=\"#60a5fa\" stroke-width=\"5\" fill=\"none\" stroke-linecap=\"round\" />\n"
        "    <path d=\"M90 60 C100 34 120 22 130 22 C140 22 160 34 170 60\" fill=\"none\" stroke=\"#3b82f6\" stroke-width=\"4\" opacity=\"0.8\" />\n"
        "    <rect x=\"16\" y=\"210\" width=\"228\" height=\"28\" rx=\"14\" fill=\"#dbe7f5\" />\n"
        "    <rect x=\"16\" y=\"210\" width=\"228\" height=\"28\" rx=\"14\" fill=\"none\" stroke=\"#60a5fa\" stroke-width=\"1.5\" />\n"
        "    <text x=\"30\" y=\"230\" font-family=\"Inter, sans-serif\" font-size=\"14\" fill=\"#1e293b\">Developer</text>\n"
        "  </g>"
    ),
    "lanyard.svg": (
        re.compile(
            r'(?s)    <circle cx="160" cy="190" r="42" fill="#0f3f6b" />.*?'
            r'    <circle cx="160" cy="190" r="44" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0\.8" />'
        ),
        "    <circle cx=\"160\" cy=\"190\" r=\"42\" fill=\"#0f3f6b\" />\n"
        "    <g clip-path=\"url(#avatarCut)\">\n"
        "      <circle cx=\"160\" cy=\"190\" r=\"42\" fill=\"#17547a\" />\n"
        "      <circle cx=\"160\" cy=\"170\" r=\"24\" fill=\"#1f5f87\" />\n"
        "      <circle cx=\"150\" cy=\"168\" r=\"6\" fill=\"#dbeafe\" />\n"
        "      <circle cx=\"170\" cy=\"168\" r=\"6\" fill=\"#dbeafe\" />\n"
        "      <path d=\"M145 206 C153 218 167 218 175 206\" stroke=\"#82cfff\" stroke-width=\"4\" fill=\"none\" stroke-linecap=\"round\" />\n"
        "    </g>\n"
        "    <circle cx=\"160\" cy=\"190\" r=\"44\" fill=\"none\" stroke=\"#00e5ff\" stroke-width=\"2\" opacity=\"0.8\" />"
    ),
}

for fname, (pattern, replacement) in replacements.items():
    path = Path(fname)
    text = path.read_text(encoding='utf-8')
    new_text, count = pattern.subn(replacement, text)
    if count:
        path.write_text(new_text, encoding='utf-8')
        print(f'{fname}: replaced {count}')
    else:
        print(f'{fname}: no matches found')
