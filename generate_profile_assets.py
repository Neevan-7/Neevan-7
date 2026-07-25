from pathlib import Path
import base64
p = Path('.')
avatar_data = base64.b64encode((p/'avatar.png').read_bytes()).decode('ascii')

banner = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740" role="img" aria-label="Naveen — Java Full Stack Developer banner">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#020816" />
      <stop offset="40%" stop-color="#061020" />
      <stop offset="100%" stop-color="#010409" />
    </linearGradient>
    <linearGradient id="neonBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00E5FF" />
      <stop offset="50%" stop-color="#0EA5E9" />
      <stop offset="100%" stop-color="#3B82F6" />
    </linearGradient>
    <linearGradient id="cyanGlow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0" />
      <stop offset="30%" stop-color="#00E5FF" stop-opacity="0.45" />
      <stop offset="70%" stop-color="#38BDF8" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="statGradient" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#22D3EE" />
    </linearGradient>
    <linearGradient id="pillGlow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0EA5E9" />
      <stop offset="100%" stop-color="#38BDF8" />
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="pulse" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" in="blur" result="glow" />
      <feMerge>
        <feMergeNode in="glow" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <clipPath id="avatarClip">
      <rect x="780" y="170" width="260" height="260" rx="28" ry="28" />
    </clipPath>
  </defs>
  <rect width="1280" height="740" fill="url(#bg)" />
  <g opacity="0.28">
    <path d="M0 720 H1280" stroke="#0a1831" stroke-width="2" />
    <path d="M160 0 L1280 720" stroke="#082034" stroke-width="1" />
    <path d="M0 180 L1080 740" stroke="#03121f" stroke-width="1" />
  </g>
  <g filter="url(#softGlow)">
    <rect x="48" y="50" width="520" height="260" rx="24" fill="#04111f" stroke="#0d4054" stroke-width="1.5" />
    <path d="M70 88 H512" stroke="#0a1835" stroke-width="3" />
    <circle cx="82" cy="82" r="7" fill="#ff5f57" />
    <circle cx="110" cy="82" r="7" fill="#ffbd2e" />
    <circle cx="138" cy="82" r="7" fill="#27c93f" />
    <text x="72" y="128" font-family="Inter, sans-serif" font-size="16" fill="#cbd5e1">user@dev:~$</text>
    <text x="160" y="128" font-family="Inter, sans-serif" font-size="16" fill="#cbd5e1">cat README.md</text>
    <rect x="340" y="118" width="10" height="24" rx="5" fill="#00e5ff">
      <animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite" />
    </rect>
    <text x="72" y="168" font-family="Inter, sans-serif" font-size="22" fill="#8ed1ff">Building scalable systems with Java and React.</text>
  </g>
  <g transform="translate(630 60)">
    <path d="M90 20 C60 80 28 90 12 90 C6 88 20 50 44 40 C80 25 150 42 146 88 C170 80 176 32 158 18 C145 8 128 28 108 58 C90 80 74 92 60 98" fill="none" stroke="url(#neonBlue)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.88" filter="url(#pulse)" />
    <text x="14" y="210" font-family="Inter, sans-serif" font-size="38" fill="#e2faff" letter-spacing="1.2">Naveen</text>
    <g transform="translate(10 250)" font-family="JetBrains Mono, monospace" font-size="24" fill="#cbd5e1">
      <text opacity="0">Java Full Stack Developer<animate attributeName="opacity" values="1;1;0" begin="0s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">Spring Boot Engineer<animate attributeName="opacity" values="0;1;1;0" begin="2s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">Backend Developer<animate attributeName="opacity" values="0;1;1;0" begin="4s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">REST API Architect<animate attributeName="opacity" values="0;1;1;0" begin="6s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">React Developer<animate attributeName="opacity" values="0;1;1;0" begin="8s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">Problem Solver<animate attributeName="opacity" values="0;1;1;0" begin="10s" dur="7s" repeatCount="indefinite" /></text>
    </g>
  </g>
  <g transform="translate(620 320)">
    <rect x="0" y="0" width="560" height="192" rx="20" fill="#061421" stroke="#0a3a61" stroke-width="1.5" />
    <text x="30" y="38" font-family="JetBrains Mono, monospace" font-size="18" fill="#7dd3fc">"</text>
    <text x="50" y="38" font-family="Inter, sans-serif" font-size="24" fill="#dbeafe">Turning precise Java systems into production-ready services."</text>
    <text x="50" y="72" font-family="Inter, sans-serif" font-size="16" fill="#94a3b8">A terminal-style quote for a dependable development flow.</text>
  </g>
  <g transform="translate(48 340)">
    <rect x="0" y="0" width="520" height="240" rx="24" fill="#031021" stroke="#0b2f50" stroke-width="1.4" />
    <text x="30" y="40" font-family="Inter, sans-serif" font-size="20" fill="#cbd5e1">About Me</text>
    <g font-family="JetBrains Mono, monospace" font-size="16" fill="#94a3b8">
      <text x="30" y="78" opacity="0"><tspan>• Java Full Stack Developer</tspan><animate attributeName="opacity" values="0;1" begin="0.6s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="108" opacity="0"><tspan>• Passionate about scalable backend systems</tspan><animate attributeName="opacity" values="0;1" begin="1.0s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="138" opacity="0"><tspan>• Love Spring Boot & Microservices</tspan><animate attributeName="opacity" values="0;1" begin="1.4s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="168" opacity="0"><tspan>• React enthusiast with clean UI intent</tspan><animate attributeName="opacity" values="0;1" begin="1.8s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="198" opacity="0"><tspan>• Always learning new technologies</tspan><animate attributeName="opacity" values="0;1" begin="2.2s" dur="0.4s" fill="freeze" /></text>
    </g>
  </g>
  <g transform="translate(48 600)">
    <rect x="0" y="0" width="1184" height="110" rx="22" fill="#041019" stroke="#07446f" stroke-width="1.6" />
    <text x="30" y="32" font-family="Inter, sans-serif" font-size="20" fill="#cbd5e1">Tech Stack</text>
    <g transform="translate(30 50)" font-family="JetBrains Mono, monospace" font-size="14" fill="#e2faff">
      <g transform="translate(0 0)"><rect x="0" y="0" width="140" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Core Java</text></g>
      <g transform="translate(160 0)"><rect x="0" y="0" width="180" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Spring Boot</text></g>
      <g transform="translate(360 0)"><rect x="0" y="0" width="178" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Hibernate / JPA</text></g>
      <g transform="translate(560 0)"><rect x="0" y="0" width="132" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">React</text></g>
      <g transform="translate(712 0)"><rect x="0" y="0" width="140" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Tailwind CSS</text></g>
      <g transform="translate(862 0)"><rect x="0" y="0" width="146" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">AWS / Docker</text></g>
    </g>
  </g>
  <g transform="translate(570 550)">
    <rect x="0" y="0" width="670" height="160" rx="20" fill="#081622" stroke="#0b4d7a" stroke-width="1.5" />
    <text x="30" y="32" font-family="Inter, sans-serif" font-size="20" fill="#cbd5e1">Skill Progress</text>
    <g font-family="JetBrains Mono, monospace" font-size="14" fill="#94a3b8">
      <text x="30" y="66">Backend</text>
      <text x="30" y="96">Frontend</text>
      <text x="30" y="126">Databases</text>
      <text x="30" y="156">DevOps</text>
      <text x="360" y="66">Cloud</text>
      <text x="360" y="96">Problem Solving</text>
    </g>
    <g>
      <rect x="140" y="50" width="460" height="18" rx="9" fill="#0f2a40" />
      <rect x="140" y="82" width="460" height="18" rx="9" fill="#0f2a40" />
      <rect x="140" y="114" width="460" height="18" rx="9" fill="#0f2a40" />
      <rect x="140" y="146" width="460" height="18" rx="9" fill="#0f2a40" />
      <rect x="430" y="50" width="260" height="18" rx="9" fill="#0f2a40" />
      <rect x="430" y="82" width="260" height="18" rx="9" fill="#0f2a40" />
      <rect x="140" y="50" width="420" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;420" dur="1.1s" begin="0.5s" fill="freeze" /></rect>
      <rect x="140" y="82" width="388" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;388" dur="1.1s" begin="0.7s" fill="freeze" /></rect>
      <rect x="140" y="114" width="364" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;364" dur="1.1s" begin="0.9s" fill="freeze" /></rect>
      <rect x="140" y="146" width="332" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;332" dur="1.1s" begin="1.1s" fill="freeze" /></rect>
      <rect x="430" y="50" width="208" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;208" dur="1.1s" begin="1.3s" fill="freeze" /></rect>
      <rect x="430" y="82" width="248" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;248" dur="1.1s" begin="1.5s" fill="freeze" /></rect>
    </g>
  </g>
  <g transform="translate(780 170)" clip-path="url(#avatarClip)">
    <image width="260" height="260" href="data:image/png;base64,{avatar_data}" preserveAspectRatio="xMidYMid slice" />
    <rect x="0" y="0" width="260" height="260" fill="url(#cyanGlow)" opacity="0.16" />
    <rect x="0" y="0" width="260" height="260" fill="none" stroke="#00e5ff" stroke-width="2" />
    <rect x="0" y="0" width="260" height="260" fill="url(#bg)" opacity="0.02" />
  </g>
  <g transform="translate(780 450)">
    <rect x="0" y="0" width="260" height="40" rx="16" fill="#02101d" stroke="#0b4b82" stroke-width="1.2" />
    <text x="18" y="26" font-family="Inter, sans-serif" font-size="14" fill="#cbd5e1">Hologram scan active</text>
    <rect x="0" y="0" width="260" height="6" fill="#0099ff" opacity="0.18"><animate attributeName="x" values="-260;260" dur="3.5s" repeatCount="indefinite" /></rect>
  </g>
</svg>'''

banner_light = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740" role="img" aria-label="Naveen — Java Full Stack Developer light banner">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f8fbff" />
      <stop offset="45%" stop-color="#dfe7f3" />
      <stop offset="100%" stop-color="#eef4fb" />
    </linearGradient>
    <linearGradient id="neonBlue" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0099FF" />
      <stop offset="100%" stop-color="#60A5FA" />
    </linearGradient>
    <linearGradient id="cyanGlow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0" />
      <stop offset="30%" stop-color="#00E5FF" stop-opacity="0.45" />
      <stop offset="70%" stop-color="#38BDF8" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="statGradient" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0f4db8" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
    <linearGradient id="pillGlow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0099FF" />
      <stop offset="100%" stop-color="#60A5FA" />
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="pulse" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" in="blur" result="glow" />
      <feMerge>
        <feMergeNode in="glow" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <clipPath id="avatarClip">
      <rect x="780" y="170" width="260" height="260" rx="28" ry="28" />
    </clipPath>
  </defs>
  <rect width="1280" height="740" fill="url(#bg)" />
  <g opacity="0.18">
    <path d="M0 720 H1280" stroke="#b5c6d8" stroke-width="2" />
    <path d="M160 0 L1280 720" stroke="#dfe7f3" stroke-width="1" />
    <path d="M0 180 L1080 740" stroke="#d1dbe8" stroke-width="1" />
  </g>
  <g filter="url(#softGlow)">
    <rect x="48" y="50" width="520" height="260" rx="24" fill="#f4f8ff" stroke="#c7d8ef" stroke-width="1.5" />
    <path d="M70 88 H512" stroke="#cad8ee" stroke-width="3" />
    <circle cx="82" cy="82" r="7" fill="#ff5f57" />
    <circle cx="110" cy="82" r="7" fill="#ffbd2e" />
    <circle cx="138" cy="82" r="7" fill="#27c93f" />
    <text x="72" y="128" font-family="Inter, sans-serif" font-size="16" fill="#334155">user@dev:~$</text>
    <text x="160" y="128" font-family="Inter, sans-serif" font-size="16" fill="#334155">cat README.md</text>
    <rect x="340" y="118" width="10" height="24" rx="5" fill="#0099ff">
      <animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite" />
    </rect>
    <text x="72" y="168" font-family="Inter, sans-serif" font-size="22" fill="#0f172a">Building scalable systems with Java and React.</text>
  </g>
  <g transform="translate(630 60)">
    <path d="M90 20 C60 80 28 90 12 90 C6 88 20 50 44 40 C80 25 150 42 146 88 C170 80 176 32 158 18 C145 8 128 28 108 58 C90 80 74 92 60 98" fill="none" stroke="url(#neonBlue)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.88" filter="url(#pulse)" />
    <text x="14" y="210" font-family="Inter, sans-serif" font-size="38" fill="#0f172a" letter-spacing="1.2">Naveen</text>
    <g transform="translate(10 250)" font-family="JetBrains Mono, monospace" font-size="24" fill="#475569">
      <text opacity="0">Java Full Stack Developer<animate attributeName="opacity" values="1;1;0" begin="0s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">Spring Boot Engineer<animate attributeName="opacity" values="0;1;1;0" begin="2s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">Backend Developer<animate attributeName="opacity" values="0;1;1;0" begin="4s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">REST API Architect<animate attributeName="opacity" values="0;1;1;0" begin="6s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">React Developer<animate attributeName="opacity" values="0;1;1;0" begin="8s" dur="7s" repeatCount="indefinite" /></text>
      <text opacity="0">Problem Solver<animate attributeName="opacity" values="0;1;1;0" begin="10s" dur="7s" repeatCount="indefinite" /></text>
    </g>
  </g>
  <g transform="translate(620 320)">
    <rect x="0" y="0" width="560" height="192" rx="20" fill="#eef4fb" stroke="#c7d8ef" stroke-width="1.5" />
    <text x="30" y="38" font-family="JetBrains Mono, monospace" font-size="18" fill="#0369a1">"</text>
    <text x="50" y="38" font-family="Inter, sans-serif" font-size="24" fill="#1e293b">Turning precise Java systems into production-ready services."</text>
    <text x="50" y="72" font-family="Inter, sans-serif" font-size="16" fill="#475569">A terminal-style quote for a dependable development flow.</text>
  </g>
  <g transform="translate(48 340)">
    <rect x="0" y="0" width="520" height="240" rx="24" fill="#f8fbff" stroke="#c4d4e8" stroke-width="1.4" />
    <text x="30" y="40" font-family="Inter, sans-serif" font-size="20" fill="#0f172a">About Me</text>
    <g font-family="JetBrains Mono, monospace" font-size="16" fill="#475569">
      <text x="30" y="78" opacity="0"><tspan>• Java Full Stack Developer</tspan><animate attributeName="opacity" values="0;1" begin="0.6s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="108" opacity="0"><tspan>• Passionate about scalable backend systems</tspan><animate attributeName="opacity" values="0;1" begin="1.0s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="138" opacity="0"><tspan>• Love Spring Boot & Microservices</tspan><animate attributeName="opacity" values="0;1" begin="1.4s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="168" opacity="0"><tspan>• React enthusiast with clean UI intent</tspan><animate attributeName="opacity" values="0;1" begin="1.8s" dur="0.4s" fill="freeze" /></text>
      <text x="30" y="198" opacity="0"><tspan>• Always learning new technologies</tspan><animate attributeName="opacity" values="0;1" begin="2.2s" dur="0.4s" fill="freeze" /></text>
    </g>
  </g>
  <g transform="translate(48 600)">
    <rect x="0" y="0" width="1184" height="110" rx="22" fill="#eef4fb" stroke="#c7d8ef" stroke-width="1.6" />
    <text x="30" y="32" font-family="Inter, sans-serif" font-size="20" fill="#0f172a">Tech Stack</text>
    <g transform="translate(30 50)" font-family="JetBrains Mono, monospace" font-size="14" fill="#0f172a">
      <g transform="translate(0 0)"><rect x="0" y="0" width="140" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Core Java</text></g>
      <g transform="translate(160 0)"><rect x="0" y="0" width="180" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Spring Boot</text></g>
      <g transform="translate(360 0)"><rect x="0" y="0" width="178" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Hibernate / JPA</text></g>
      <g transform="translate(560 0)"><rect x="0" y="0" width="132" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">React</text></g>
      <g transform="translate(712 0)"><rect x="0" y="0" width="140" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">Tailwind CSS</text></g>
      <g transform="translate(862 0)"><rect x="0" y="0" width="146" height="32" rx="16" fill="url(#pillGlow)" /><text x="14" y="21">AWS / Docker</text></g>
    </g>
  </g>
  <g transform="translate(570 550)">
    <rect x="0" y="0" width="670" height="160" rx="20" fill="#f7fbff" stroke="#c7d8ef" stroke-width="1.5" />
    <text x="30" y="32" font-family="Inter, sans-serif" font-size="20" fill="#0f172a">Skill Progress</text>
    <g font-family="JetBrains Mono, monospace" font-size="14" fill="#475569">
      <text x="30" y="66">Backend</text>
      <text x="30" y="96">Frontend</text>
      <text x="30" y="126">Databases</text>
      <text x="30" y="156">DevOps</text>
      <text x="360" y="66">Cloud</text>
      <text x="360" y="96">Problem Solving</text>
    </g>
    <g>
      <rect x="140" y="50" width="460" height="18" rx="9" fill="#e2e8f0" />
      <rect x="140" y="82" width="460" height="18" rx="9" fill="#e2e8f0" />
      <rect x="140" y="114" width="460" height="18" rx="9" fill="#e2e8f0" />
      <rect x="140" y="146" width="460" height="18" rx="9" fill="#e2e8f0" />
      <rect x="430" y="50" width="260" height="18" rx="9" fill="#e2e8f0" />
      <rect x="430" y="82" width="260" height="18" rx="9" fill="#e2e8f0" />
      <rect x="140" y="50" width="420" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;420" dur="1.1s" begin="0.5s" fill="freeze" /></rect>
      <rect x="140" y="82" width="388" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;388" dur="1.1s" begin="0.7s" fill="freeze" /></rect>
      <rect x="140" y="114" width="364" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;364" dur="1.1s" begin="0.9s" fill="freeze" /></rect>
      <rect x="140" y="146" width="332" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;332" dur="1.1s" begin="1.1s" fill="freeze" /></rect>
      <rect x="430" y="50" width="208" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;208" dur="1.1s" begin="1.3s" fill="freeze" /></rect>
      <rect x="430" y="82" width="248" height="18" rx="9" fill="url(#statGradient)"><animate attributeName="width" values="0;248" dur="1.1s" begin="1.5s" fill="freeze" /></rect>
    </g>
  </g>
  <g transform="translate(780 170)" clip-path="url(#avatarClip)">
    <image width="260" height="260" href="data:image/png;base64,{avatar_data}" preserveAspectRatio="xMidYMid slice" />
    <rect x="0" y="0" width="260" height="260" fill="url(#cyanGlow)" opacity="0.16" />
    <rect x="0" y="0" width="260" height="260" fill="none" stroke="#0e7490" stroke-width="2" />
    <rect x="0" y="0" width="260" height="260" fill="url(#bg)" opacity="0.02" />
  </g>
  <g transform="translate(780 450)">
    <rect x="0" y="0" width="260" height="40" rx="16" fill="#e5effa" stroke="#94a3b8" stroke-width="1.2" />
    <text x="18" y="26" font-family="Inter, sans-serif" font-size="14" fill="#475569">Hologram scan active</text>
    <rect x="0" y="0" width="260" height="6" fill="#0099ff" opacity="0.18"><animate attributeName="x" values="-260;260" dur="3.5s" repeatCount="indefinite" /></rect>
  </g>
</svg>'''

lanyard = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 520" width="320" height="520" role="img" aria-label="Naveen GitHub lanyard badge">
  <defs>
    <linearGradient id="strap" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b3b66" />
      <stop offset="100%" stop-color="#08263f" />
    </linearGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#d8e3eb" />
      <stop offset="100%" stop-color="#9aa8b6" />
    </linearGradient>
    <linearGradient id="badgeGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.05" />
    </linearGradient>
    <filter id="sling" x="-30%" y="-40%" width="160%" height="180%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feOffset dx="0" dy="2" result="offset" />
      <feMerge><feMergeNode in="offset" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
    <clipPath id="avatarCut"><circle cx="160" cy="190" r="42" /></clipPath>
  </defs>
  <rect width="320" height="520" rx="34" ry="34" fill="#020814" />
  <g transform="translate(158 45)">
    <g id="sway" transform="rotate(0 0 0)">
      <rect x="-31" y="-2" width="62" height="220" rx="15" fill="url(#strap)" />
      <path d="M-31 -2 C-30 -10 30 -10 31 -2" fill="#0a2e4c" />
      <rect x="-31" y="-2" width="62" height="38" rx="14" fill="#102140" />
      <rect x="-19" y="-0.5" width="38" height="20" rx="10" fill="url(#metal)" />
      <ellipse cx="0" cy="28" rx="18" ry="6" fill="#f8fafc" opacity="0.35" />
    </g>
    <animateTransform xlink:href="#sway" attributeName="transform" type="rotate" values="-6 0 0; 4 0 0; -3 0 0; 2 0 0; 0 0 0" keyTimes="0;0.25;0.55;0.8;1" dur="4.2s" repeatCount="indefinite" />
  </g>
  <g transform="translate(30 120)">
    <rect x="0" y="0" width="260" height="340" rx="28" ry="28" fill="#061427" stroke="#0b537d" stroke-width="2" filter="url(#sling)" />
    <rect x="0" y="0" width="260" height="100" rx="28" ry="28" fill="#0c3860" />
    <circle cx="160" cy="190" r="44" fill="#08243b" />
    <circle cx="160" cy="190" r="42" fill="#0f3f6b" />
    <image x="118" y="148" width="84" height="84" href="data:image/png;base64,{avatar_data}" clip-path="url(#avatarCut)" preserveAspectRatio="xMidYMid slice" />
    <circle cx="160" cy="190" r="44" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0.8" />
    <circle cx="160" cy="190" r="58" fill="none" stroke="#0ea5e9" stroke-width="1.4" opacity="0.35" />
    <text x="18" y="246" font-family="Inter, sans-serif" font-size="18" fill="#e2faff">Naveen</text>
    <text x="18" y="270" font-family="Inter, sans-serif" font-size="13" fill="#94a3b8">Java Full Stack Developer</text>
    <text x="18" y="294" font-family="JetBrains Mono, monospace" font-size="12" fill="#94a3b8">@Neevan-7</text>
    <rect x="18" y="308" width="224" height="40" rx="10" fill="#071d30" />
    <g fill="#94a3b8">
      <rect x="30" y="318" width="6" height="22" />
      <rect x="40" y="318" width="4" height="22" />
      <rect x="48" y="318" width="2" height="22" />
      <rect x="54" y="318" width="3" height="22" />
      <rect x="62" y="318" width="5" height="22" />
      <rect x="72" y="318" width="3" height="22" />
      <rect x="80" y="318" width="2" height="22" />
      <rect x="88" y="318" width="5" height="22" />
      <rect x="98" y="318" width="3" height="22" />
      <rect x="106" y="318" width="4" height="22" />
      <rect x="116" y="318" width="2" height="22" />
      <rect x="124" y="318" width="7" height="22" />
    </g>
    <rect x="18" y="358" width="224" height="18" rx="8" fill="#00e5ff" opacity="0.12" />
    <rect x="18" y="384" width="224" height="14" rx="7" fill="#c6f5ff" opacity="0.14" />
    <rect x="18" y="356" width="224" height="2" fill="#38bdf8" />
    <rect x="18" y="382" width="224" height="2" fill="#60a5fa" />
    <rect x="18" y="418" width="224" height="2" fill="#0ea5e9" />
  </g>
  <text x="20" y="500" font-family="Inter, sans-serif" font-size="12" fill="#94a3b8">Holographic ID / GitHub connection token</text>
</svg>'''

stats = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" aria-label="Naveen local stats card">
  <defs>
    <linearGradient id="ringGradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00e5ff" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
    <linearGradient id="row" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#60a5fa" />
    </linearGradient>
  </defs>
  <rect width="640" height="360" rx="24" fill="#041224" />
  <text x="40" y="46" font-family="Inter, sans-serif" font-size="26" fill="#dbeafe">Local Stats</text>
  <g transform="translate(40 40)">
    <circle cx="160" cy="140" r="100" fill="none" stroke="#0f2b45" stroke-width="24" />
    <circle cx="160" cy="140" r="100" fill="none" stroke="url(#ringGradient)" stroke-width="24" stroke-dasharray="628" stroke-dashoffset="628">
      <animate attributeName="stroke-dashoffset" values="628;251.2" dur="1.5s" fill="freeze" />
    </circle>
    <text x="110" y="150" font-family="Inter, sans-serif" font-size="40" fill="#ffffff">92%</text>
    <text x="100" y="176" font-family="Inter, sans-serif" font-size="16" fill="#94a3b8">Backend</text>
  </g>
  <g transform="translate(320 46)" font-family="JetBrains Mono, monospace" font-size="14" fill="#cbd5e1">
    <text x="0" y="0">Cloud</text>
    <rect x="0" y="12" width="260" height="14" rx="7" fill="#0d324a" />
    <rect x="0" y="12" width="176" height="14" rx="7" fill="url(#row)"><animate attributeName="width" values="0;176" dur="1.2s" begin="0.3s" fill="freeze" /></rect>
    <text x="232" y="11" font-family="Inter, sans-serif" font-size="12" fill="#dbeafe">70%</text>
    <text x="0" y="42">Frontend</text>
    <rect x="0" y="54" width="260" height="14" rx="7" fill="#0d324a" />
    <rect x="0" y="54" width="210" height="14" rx="7" fill="url(#row)"><animate attributeName="width" values="0;210" dur="1.2s" begin="0.5s" fill="freeze" /></rect>
    <text x="232" y="53" font-family="Inter, sans-serif" font-size="12" fill="#dbeafe">81%</text>
    <text x="0" y="84">Databases</text>
    <rect x="0" y="96" width="260" height="14" rx="7" fill="#0d324a" />
    <rect x="0" y="96" width="196" height="14" rx="7" fill="url(#row)"><animate attributeName="width" values="0;196" dur="1.2s" begin="0.7s" fill="freeze" /></rect>
    <text x="232" y="95" font-family="Inter, sans-serif" font-size="12" fill="#dbeafe">75%</text>
    <text x="0" y="126">Problem Solving</text>
    <rect x="0" y="138" width="260" height="14" rx="7" fill="#0d324a" />
    <rect x="0" y="138" width="232" height="14" rx="7" fill="url(#row)"><animate attributeName="width" values="0;232" dur="1.2s" begin="0.9s" fill="freeze" /></rect>
    <text x="232" y="137" font-family="Inter, sans-serif" font-size="12" fill="#dbeafe">89%</text>
  </g>
</svg>'''

langs = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" aria-label="Naveen language chart">
  <defs>
    <linearGradient id="langBar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#60a5fa" />
    </linearGradient>
  </defs>
  <rect width="640" height="360" rx="24" fill="#061124" />
  <text x="40" y="46" font-family="Inter, sans-serif" font-size="26" fill="#dbeafe">Languages & Tools</text>
  <g font-family="JetBrains Mono, monospace" font-size="16" fill="#cbd5e1">
    <text x="40" y="96">Java</text>
    <text x="40" y="146">Spring Boot</text>
    <text x="40" y="196">React</text>
    <text x="40" y="246">JavaScript</text>
    <text x="340" y="96">SQL</text>
    <text x="340" y="146">AWS</text>
  </g>
  <rect x="38" y="106" width="250" height="18" rx="9" fill="#0b3250" />
  <rect x="38" y="106" width="238" height="18" rx="9" fill="url(#langBar)"><animate attributeName="width" values="0;238" dur="1.1s" fill="freeze" /></rect>
  <text x="296" y="120" font-family="Inter, sans-serif" font-size="13" fill="#dbeafe">95%</text>
  <rect x="38" y="156" width="250" height="18" rx="9" fill="#0b3250" />
  <rect x="38" y="156" width="230" height="18" rx="9" fill="url(#langBar)"><animate attributeName="width" values="0;230" dur="1.1s" begin="0.2s" fill="freeze" /></rect>
  <text x="296" y="170" font-family="Inter, sans-serif" font-size="13" fill="#dbeafe">92%</text>
  <rect x="38" y="206" width="250" height="18" rx="9" fill="#0b3250" />
  <rect x="38" y="206" width="222" height="18" rx="9" fill="url(#langBar)"><animate attributeName="width" values="0;222" dur="1.1s" begin="0.4s" fill="freeze" /></rect>
  <text x="296" y="220" font-family="Inter, sans-serif" font-size="13" fill="#dbeafe">88%</text>
  <rect x="38" y="256" width="250" height="18" rx="9" fill="#0b3250" />
  <rect x="38" y="256" width="216" height="18" rx="9" fill="url(#langBar)"><animate attributeName="width" values="0;216" dur="1.1s" begin="0.6s" fill="freeze" /></rect>
  <text x="296" y="270" font-family="Inter, sans-serif" font-size="13" fill="#dbeafe">86%</text>
  <rect x="338" y="106" width="250" height="18" rx="9" fill="#0b3250" />
  <rect x="338" y="106" width="208" height="18" rx="9" fill="url(#langBar)"><animate attributeName="width" values="0;208" dur="1.1s" begin="0.3s" fill="freeze" /></rect>
  <text x="596" y="120" font-family="Inter, sans-serif" font-size="13" fill="#dbeafe">80%</text>
  <rect x="338" y="156" width="250" height="18" rx="9" fill="#0b3250" />
  <rect x="338" y="156" width="168" height="18" rx="9" fill="url(#langBar)"><animate attributeName="width" values="0;168" dur="1.1s" begin="0.5s" fill="freeze" /></rect>
  <text x="596" y="170" font-family="Inter, sans-serif" font-size="13" fill="#dbeafe">72%</text>
</svg>'''

 trophies = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" aria-label="Naveen trophy showcase">
  <defs>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f8e469" />
      <stop offset="100%" stop-color="#d6b53c" />
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
  </defs>
  <rect width="640" height="360" rx="24" fill="#03111f" />
  <text x="40" y="46" font-family="Inter, sans-serif" font-size="26" fill="#dbeafe">Trophy Room</text>
  <g font-family="JetBrains Mono, monospace" font-size="14" fill="#cbd5e1">
    <g transform="translate(40 90)">
      <rect x="0" y="0" width="166" height="192" rx="20" fill="#071a2c" />
      <path d="M83 44 L72 60 H94 L83 44" fill="#ffd966" />
      <path d="M60 68 C58 94 60 132 60 132 H106 C106 132 108 94 106 68 Z" fill="#f8e469" />
      <rect x="66" y="132" width="34" height="36" rx="14" fill="#d6b53c" />
      <text x="20" y="170" font-family="Inter, sans-serif" font-size="16" fill="#e2faff">Project Builder</text>
      <text x="20" y="190" font-family="Inter, sans-serif" font-size="12" fill="#94a3b8">Ecommerce, portfolio, landing pages.</text>
    </g>
    <g transform="translate(242 90)">
      <rect x="0" y="0" width="166" height="192" rx="20" fill="#071a2c" />
      <path d="M44 78 H122 V108 H44 Z" fill="#0f172a" />
      <rect x="48" y="108" width="68" height="20" fill="#ffd966" />
      <rect x="76" y="128" width="12" height="26" fill="#d6b53c" />
      <path d="M60 64 C74 42 116 42 130 64 L130 84 H60 Z" fill="#f8e469" />
      <text x="20" y="170" font-family="Inter, sans-serif" font-size="16" fill="#e2faff">Code Refinement</text>
      <text x="20" y="190" font-family="Inter, sans-serif" font-size="12" fill="#94a3b8">Clean architecture and maintainability.</text>
    </g>
    <g transform="translate(444 90)">
      <rect x="0" y="0" width="166" height="192" rx="20" fill="#071a2c" />
      <path d="M40 56 L126 56 L110 92 H56 Z" fill="#f8e469" />
      <rect x="68" y="92" width="28" height="24" fill="#d6b53c" />
      <circle cx="82" cy="136" r="18" fill="#ffd966" />
      <text x="20" y="170" font-family="Inter, sans-serif" font-size="16" fill="#e2faff">Growth Mindset</text>
      <text x="20" y="190" font-family="Inter, sans-serif" font-size="12" fill="#94a3b8">Learning, feedback, and improvement.</text>
    </g>
  </g>
  <rect x="40" y="90" width="166" height="192" rx="20" fill="url(#shine)" opacity="0.15"><animate attributeName="opacity" values="0.15;0.05;0.15" dur="3.2s" repeatCount="indefinite" /></rect>
  <rect x="242" y="90" width="166" height="192" rx="20" fill="url(#shine)" opacity="0.15"><animate attributeName="opacity" values="0.05;0.18;0.05" dur="3.6s" repeatCount="indefinite" /></rect>
  <rect x="444" y="90" width="166" height="192" rx="20" fill="url(#shine)" opacity="0.15"><animate attributeName="opacity" values="0.1;0.22;0.1" dur="4s" repeatCount="indefinite" /></rect>
</svg>'''

workflow = '''name: GitHub Snake

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch: {}

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Generate GitHub Snake animation
        uses: Platane/snk@v1
        with:
          branch: output
          filename: snake.svg
          theme: |
            background: '#020712'
            border: '#0ea5e9'
            border2: '#00e5ff'
            snake: '#38bdf8'
            apple: '#0ea5e9'
            text: '#cbd5e1'
            wall: '#0f172a'
            viewport: '#0f172a'
            score: '#60a5fa'
'''

contrib_blocks = ''.join(f'<rect x="{(i*18)}" y="{(j*18)}" width="14" height="14" rx="3" fill="#0d2745" />\n' for j in range(5) for i in range(24))
contrib = f'''<svg width="100%" height="90" viewBox="0 0 520 90" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Contribution graph">
  <defs>
    <linearGradient id="contrib" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>
  </defs>
  <rect width="520" height="90" rx="14" fill="#061124" />
  <g transform="translate(18 18)">
    {contrib_blocks}
    <g fill="url(#contrib)">
      <rect x="0" y="0" width="14" height="14" rx="3" />
      <rect x="36" y="0" width="14" height="14" rx="3" />
      <rect x="72" y="18" width="14" height="14" rx="3" />
      <rect x="108" y="0" width="14" height="14" rx="3" />
      <rect x="180" y="18" width="14" height="14" rx="3" />
      <rect x="234" y="36" width="14" height="14" rx="3" />
      <rect x="294" y="18" width="14" height="14" rx="3" />
      <rect x="330" y="36" width="14" height="14" rx="3" />
      <rect x="396" y="0" width="14" height="14" rx="3" />
      <rect x="432" y="18" width="14" height="14" rx="3" />
      <rect x="468" y="36" width="14" height="14" rx="3" />
    </g>
  </g>
</svg>'''

readme = f'''<picture>
  <source srcset="banner-light.svg?v=1" media="(prefers-color-scheme: light)">
  <img src="banner.svg?v=1" alt="Naveen — Java Full Stack Developer" width="100%" />
</picture>

# Naveen — Java Full Stack Developer

> Building modern Java systems with backend strength and frontend polish.

## About Me

I am a Java Full Stack Developer from Chennai with an EEE background, focused on building clean, scalable applications using Spring Boot, React, and microservices. My GitHub profile highlights web projects, portfolio work, and experience in Java, cloud tooling, and CI/CD.

- Java, Spring Boot, Hibernate, REST APIs, JWT authentication
- React.js, Tailwind CSS, responsive UI design
- MySQL, PostgreSQL, MongoDB
- Git, GitHub, Maven, Jenkins, Docker, AWS, Postman
- Agile collaboration, code reviews, and practical software delivery

## Featured Projects

| Project | Description | Primary Tech |
|---|---|---|
| [Marvel-Seating](https://github.com/Neevan-7/Marvel-Seating) | Ecommerce website for a furniture brand with modern UI and client interaction. | JavaScript |
| [RoadCraft](https://github.com/Neevan-7/RoadCraft) | Landing page with polished layout and responsive design for RoadCrafting company. | CSS |
| [Smart-electricity-system](https://github.com/Neevan-7/Smart-electricity-system) | Java full-stack monitoring app for electrical parameters and fault prediction. | Java |
| [Myportfolio](https://github.com/Neevan-7/Myportfolio) | Developer portfolio site showcasing skills and contact details. | HTML |
| [Portfolio1](https://github.com/Neevan-7/Portfolio1) | Personal portfolio with professional styling and navigation. | TypeScript |
| [Fitness--Studio-02-](https://github.com/Neevan-7/Fitness--Studio-02-) | Responsive fitness studio website showcasing classes and workouts. | HTML/CSS |

## Dashboard

![Stats](stats.svg?v=1)

![Languages](langs.svg?v=1)

![Trophies](trophies.svg?v=1)

## Contribution Graph

{contrib}

## Connect

- [GitHub](https://github.com/Neevan-7)
- [LinkedIn](https://www.linkedin.com/in/naveen798/)
- [Portfolio](https://neevan-7.github.io/Myportfolio/)
- [Live Demo](https://naveenatfly.github.io/Portfolio1/)
- Email: [naveen.electricalstuff@gmail.com](mailto:naveen.electricalstuff@gmail.com)

## Stats & Workflows

- **Followers:** 3
- **Following:** 13
- **Contributions (last year):** 86
- **Pinned repositories:** 6

### GitHub Workflows

This repository includes a custom local snake generation workflow:

- `.github/workflows/github-snake.yml`

### Local badges

- Stats, language summaries, and trophies are rendered with local SVG assets.
'''

(p/'.github/workflows').mkdir(parents=True, exist_ok=True)
(p/'banner.svg').write_text(banner, encoding='utf-8')
(p/'banner-light.svg').write_text(banner_light, encoding='utf-8')
(p/'lanyard.svg').write_text(lanyard, encoding='utf-8')
(p/'stats.svg').write_text(stats, encoding='utf-8')
(p/'langs.svg').write_text(langs, encoding='utf-8')
(p/'trophies.svg').write_text(trophies, encoding='utf-8')
(p/'.github/workflows/github-snake.yml').write_text(workflow, encoding='utf-8')
(p/'README.md').write_text(readme, encoding='utf-8')
print('CREATED')
'''  }  }  )  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }