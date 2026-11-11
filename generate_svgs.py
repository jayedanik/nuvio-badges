import os
import json

BASE_DIR = r"C:\Users\yourt\.gemini\antigravity\scratch\nuvio-badges-original"
BADGES_DIR = os.path.join(BASE_DIR, "badges")
os.makedirs(BADGES_DIR, exist_ok=True)

# Define SVG Badge Templates (Height 32px standard)
BADGES = {
    "4k": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 104 32" height="32">
  <rect width="104" height="32" rx="6" fill="#121008" stroke="#EAB308" stroke-width="1.5"/>
  <text x="14" y="22" fill="#EAB308" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="18">4K</text>
  <text x="48" y="14" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="8.5" letter-spacing="0.5">ULTRA HD</text>
  <line x1="48" y1="18" x2="94" y2="18" stroke="#EAB308" stroke-width="1"/>
  <text x="48" y="26" fill="#9CA3AF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="600" font-size="7" letter-spacing="1">BLU-RAY</text>
</svg>''',

    "1080p": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#0B132B" stroke="#3B82F6" stroke-width="1.5"/>
  <text x="10" y="22" fill="#60A5FA" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="16">1080p</text>
  <text x="64" y="15" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="7.5">FULL</text>
  <text x="64" y="24" fill="#93C5FD" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="7.5">HD</text>
</svg>''',

    "720p": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 32" height="32">
  <rect width="76" height="32" rx="6" fill="#0F172A" stroke="#64748B" stroke-width="1.5"/>
  <text x="10" y="22" fill="#94A3B8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="16">720p</text>
  <text x="54" y="20" fill="#CBD5E1" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="9">HD</text>
</svg>''',

    "dolby-vision": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 114 32" height="32">
  <rect width="114" height="32" rx="6" fill="#0A0A0A" stroke="#52525B" stroke-width="1.5"/>
  <path d="M12 9h4a7 7 0 0 1 0 14h-4V9zm18 0h-4a7 7 0 0 0 0 14h4V9z" fill="#FFFFFF"/>
  <text x="36" y="15" fill="#A1A1AA" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="8" letter-spacing="1.2">DOLBY</text>
  <text x="36" y="25" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="10.5" letter-spacing="1.5">VISION</text>
</svg>''',

    "dolby-atmos": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 114 32" height="32">
  <rect width="114" height="32" rx="6" fill="#0A0A0A" stroke="#38BDF8" stroke-width="1.5"/>
  <path d="M12 9h4a7 7 0 0 1 0 14h-4V9zm18 0h-4a7 7 0 0 0 0 14h4V9z" fill="#FFFFFF"/>
  <text x="36" y="15" fill="#A1A1AA" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="8" letter-spacing="1.2">DOLBY</text>
  <text x="36" y="25" fill="#38BDF8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="10.5" letter-spacing="1.5">ATMOS</text>
</svg>''',

    "dolby-audio": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 32" height="32">
  <rect width="110" height="32" rx="6" fill="#0A0A0A" stroke="#52525B" stroke-width="1.5"/>
  <path d="M12 9h4a7 7 0 0 1 0 14h-4V9zm18 0h-4a7 7 0 0 0 0 14h4V9z" fill="#FFFFFF"/>
  <text x="36" y="15" fill="#A1A1AA" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="8" letter-spacing="1.2">DOLBY</text>
  <text x="36" y="25" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="10" letter-spacing="1">AUDIO</text>
</svg>''',

    "hdr10plus": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 32" height="32">
  <rect width="96" height="32" rx="6" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="10" y="22" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="15">HDR10</text>
  <text x="74" y="23" fill="#38BDF8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="19">+</text>
</svg>''',

    "hdr": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 68 32" height="32">
  <rect width="68" height="32" rx="6" fill="#1C1917" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="14" y="22" fill="#F59E0B" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="16" letter-spacing="1">HDR</text>
</svg>''',

    "imax": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 32" height="32">
  <rect width="108" height="32" rx="6" fill="#031633" stroke="#2563EB" stroke-width="1.5"/>
  <text x="10" y="22" fill="#60A5FA" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="15" letter-spacing="1.5">IMAX</text>
  <text x="60" y="16" fill="#93C5FD" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="6.5" letter-spacing="0.5">ENHANCED</text>
</svg>''',

    "dts-hd": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#1A0D00" stroke="#F97316" stroke-width="1.5"/>
  <text x="10" y="22" fill="#F97316" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="15">dts</text>
  <text x="38" y="15" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="8">HD</text>
  <text x="38" y="24" fill="#FDBA74" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="6.5">MASTER AUDIO</text>
</svg>''',

    "dts-x": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 82 32" height="32">
  <rect width="82" height="32" rx="6" fill="#1A0D00" stroke="#EA580C" stroke-width="1.5"/>
  <text x="10" y="22" fill="#F97316" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="15">dts</text>
  <text x="46" y="24" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="20">X</text>
</svg>''',

    "netflix": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#140203" stroke="#E50914" stroke-width="1.5"/>
  <text x="10" y="22" fill="#E50914" font-family="Impact,-apple-system,sans-serif" font-weight="900" font-size="17" letter-spacing="1.2">NETFLIX</text>
</svg>''',

    "appletv": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#121214" stroke="#71717A" stroke-width="1.5"/>
  <g transform="translate(10, 6) scale(0.65)" fill="#FFFFFF">
    <path d="M15.2 12.9c-.1-2.4 2-3.6 2.1-3.7-1.1-1.6-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.2 1-4 2.5-1.8 3.1-.5 7.7 1.2 10.2.9 1.2 1.9 2.6 3.2 2.5 1.3-.1 1.8-.8 3.3-.8 1.6 0 2 .8 3.4.8 1.4 0 2.3-1.2 3.1-2.5 1-1.5 1.4-2.9 1.4-3-.1 0-2.8-1.1-2.9-4.2zm-2.4-7c.7-.8 1.1-2 1-3.1-1 .1-2.2.7-2.9 1.5-.6.7-1.2 1.9-1 3 1.1.1 2.2-.6 2.9-1.4z"/>
  </g>
  <text x="34" y="22" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="14">tv+</text>
</svg>''',

    "disney": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#030C1C" stroke="#0063E5" stroke-width="1.5"/>
  <text x="12" y="22" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="14" letter-spacing="0.5">DISNEY<tspan fill="#38BDF8">+</tspan></text>
</svg>''',

    "prime": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#001221" stroke="#00A8E1" stroke-width="1.5"/>
  <text x="10" y="17" fill="#00A8E1" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="12">prime</text>
  <text x="48" y="17" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="600" font-size="9">video</text>
  <path d="M12 23 Q 32 28 50 22" stroke="#FF9900" stroke-width="2" fill="none" stroke-linecap="round"/>
</svg>''',

    "max": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 32" height="32">
  <rect width="76" height="32" rx="6" fill="#100319" stroke="#9333EA" stroke-width="1.5"/>
  <text x="16" y="23" fill="#FFFFFF" font-family="Impact,-apple-system,sans-serif" font-weight="900" font-size="18" letter-spacing="1">max</text>
</svg>''',

    "paramount": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 32" height="32">
  <rect width="102" height="32" rx="6" fill="#001833" stroke="#0064FF" stroke-width="1.5"/>
  <text x="10" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="11">Paramount<tspan fill="#60A5FA" font-size="14" font-weight="900">+</tspan></text>
</svg>''',

    "hulu": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 32" height="32">
  <rect width="76" height="32" rx="6" fill="#001A0E" stroke="#1CE783" stroke-width="1.5"/>
  <text x="15" y="22" fill="#1CE783" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="17" letter-spacing="0.5">hulu</text>
</svg>''',

    "peacock": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#0A0A0A" stroke="#EAB308" stroke-width="1.5"/>
  <circle cx="16" cy="16" r="3" fill="#EAB308"/>
  <circle cx="23" cy="12" r="3" fill="#3B82F6"/>
  <circle cx="23" cy="20" r="3" fill="#10B981"/>
  <text x="32" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="11">peacock</text>
</svg>''',

    "crunchyroll": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 32" height="32">
  <rect width="108" height="32" rx="6" fill="#1A0D00" stroke="#F47521" stroke-width="1.5"/>
  <circle cx="18" cy="16" r="6" fill="#F47521"/>
  <circle cx="20" cy="15" r="3" fill="#1A0D00"/>
  <text x="30" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="10.5">crunchyroll</text>
</svg>''',

    "hoichoi": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 88 32" height="32">
  <rect width="88" height="32" rx="6" fill="#200000" stroke="#EF4444" stroke-width="1.5"/>
  <text x="10" y="22" fill="#EF4444" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="14" letter-spacing="0.5">hoichoi</text>
</svg>''',

    "zee5": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 32" height="32">
  <rect width="76" height="32" rx="6" fill="#1A0022" stroke="#A855F7" stroke-width="1.5"/>
  <text x="12" y="22" fill="#C084FC" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="14">ZEE<tspan fill="#FFFFFF">5</tspan></text>
</svg>''',

    "sonyliv": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 88 32" height="32">
  <rect width="88" height="32" rx="6" fill="#0A0A0A" stroke="#3B82F6" stroke-width="1.5"/>
  <text x="10" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="12">SONY <tspan fill="#38BDF8">LIV</tspan></text>
</svg>''',

    "realdebrid": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 32" height="32">
  <rect width="102" height="32" rx="6" fill="#021C11" stroke="#10B981" stroke-width="1.5"/>
  <path d="M16 6 L8 18 L15 18 L13 26 L23 14 L16 14 Z" fill="#10B981"/>
  <text x="28" y="21" fill="#34D399" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="13">[RD+]</text>
  <text x="68" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="9">FAST</text>
</svg>''',

    "torbox": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 32" height="32">
  <rect width="96" height="32" rx="6" fill="#001B2E" stroke="#0284C7" stroke-width="1.5"/>
  <text x="12" y="21" fill="#38BDF8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="13">[TB+]</text>
  <text x="50" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="10">TorBox</text>
</svg>''',

    "alldebrid": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 32" height="32">
  <rect width="96" height="32" rx="6" fill="#1A1300" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="12" y="21" fill="#FBBF24" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="13">[AD+]</text>
  <text x="50" y="21" fill="#FFFFFF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="9.5">AllDebrid</text>
</svg>''',

    "remux": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 86 32" height="32">
  <rect width="86" height="32" rx="6" fill="#EAB308"/>
  <text x="10" y="22" fill="#000000" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="15" letter-spacing="1">REMUX</text>
</svg>''',

    "bluray": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 92 32" height="32">
  <rect width="92" height="32" rx="6" fill="#021329" stroke="#1D4ED8" stroke-width="1.5"/>
  <text x="10" y="21" fill="#60A5FA" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="13">Blu-ray</text>
  <text x="64" y="21" fill="#93C5FD" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="10">DISC</text>
</svg>''',

    "webdl": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 86 32" height="32">
  <rect width="86" height="32" rx="6" fill="#0B132B" stroke="#3B82F6" stroke-width="1.5"/>
  <text x="11" y="21" fill="#93C5FD" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="14">WEB-DL</text>
</svg>''',

    "webrip": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 86 32" height="32">
  <rect width="86" height="32" rx="6" fill="#1E1E24" stroke="#64748B" stroke-width="1.5"/>
  <text x="12" y="21" fill="#CBD5E1" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="13">WEBRip</text>
</svg>''',

    "hevc": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 32" height="32">
  <rect width="76" height="32" rx="6" fill="#111827" stroke="#4B5563" stroke-width="1.5"/>
  <text x="10" y="21" fill="#E5E7EB" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="800" font-size="13">HEVC</text>
  <text x="49" y="16" fill="#9CA3AF" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="700" font-size="7">x265</text>
</svg>''',

    "av1": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 66 32" height="32">
  <rect width="66" height="32" rx="6" fill="#1C1917" stroke="#78716C" stroke-width="1.5"/>
  <text x="16" y="22" fill="#F5F5F4" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-weight="900" font-size="16">AV1</text>
</svg>'''
}

# Write all SVG files
for name, svg_content in BADGES.items():
    svg_path = os.path.join(BADGES_DIR, f"{name}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(BADGES)} badges in {BADGES_DIR}")
