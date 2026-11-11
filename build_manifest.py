import json
import os

BASE_DIR = r"C:\Users\yourt\.gemini\antigravity\scratch\nuvio-badges-original"

GROUPS = [
    { "id": "resolution", "name": "Resolution", "color": "#00000000", "borderColor": "#00000000", "isExpanded": True },
    { "id": "hdr", "name": "HDR & Video", "color": "#00000000", "borderColor": "#00000000", "isExpanded": True },
    { "id": "audio", "name": "Audio Format", "color": "#00000000", "borderColor": "#00000000", "isExpanded": True },
    { "id": "service", "name": "Streaming Service", "color": "#00000000", "borderColor": "#00000000", "isExpanded": True },
    { "id": "source", "name": "Source & Codec", "color": "#00000000", "borderColor": "#00000000", "isExpanded": True },
    { "id": "delivery", "name": "Debrid & Delivery", "color": "#00000000", "borderColor": "#00000000", "isExpanded": True }
]

FILTERS = [
    # --- Debrid & Delivery ---
    {
        "id": "realdebrid",
        "groupId": "delivery",
        "name": "Real-Debrid [RD+]",
        "pattern": r"(?i)\[(?:rd|ad|pm|tb|dl|ed|oc|pk)\+\]|\b(?:cached|instant)\b|\[rd\+?\]|\breal[\s._-]?debrid\b",
        "badge": "realdebrid.svg"
    },
    {
        "id": "torbox",
        "groupId": "delivery",
        "name": "TorBox [TB+]",
        "pattern": r"(?i)\[tb\+?\]|\btorbox\b",
        "badge": "torbox.svg"
    },
    {
        "id": "alldebrid",
        "groupId": "delivery",
        "name": "AllDebrid [AD+]",
        "pattern": r"(?i)\[ad\+?\]|\balldebrid\b",
        "badge": "alldebrid.svg"
    },

    # --- Resolution ---
    {
        "id": "res-4k",
        "groupId": "resolution",
        "name": "4K Ultra HD",
        "pattern": r"(?i)^(?=.*(?:2160[pi]?|4k|uhd))(?!.*(?:1080|720|480)[pi])",
        "badge": "4k.svg"
    },
    {
        "id": "res-1080p",
        "groupId": "resolution",
        "name": "1080p Full HD",
        "pattern": r"(?i)\b(?:1080[pi]|fhd|full[\s._-]?hd)\b",
        "badge": "1080p.svg"
    },
    {
        "id": "res-720p",
        "groupId": "resolution",
        "name": "720p HD",
        "pattern": r"(?i)\b720[pi]\b",
        "badge": "720p.svg"
    },

    # --- HDR & Visual ---
    {
        "id": "hdr-dolby-vision",
        "groupId": "hdr",
        "name": "Dolby Vision",
        "pattern": r"(?i)\b(?:dv|dovi|dolby[\s._-]?vision)\b",
        "badge": "dolby-vision.svg"
    },
    {
        "id": "hdr-hdr10plus",
        "groupId": "hdr",
        "name": "HDR10+",
        "pattern": r"(?i)\b(?:hdr10\+|hdr10plus|hdr[\s._-]?10\+)\b",
        "badge": "hdr10plus.svg"
    },
    {
        "id": "hdr-standard",
        "groupId": "hdr",
        "name": "HDR",
        "pattern": r"(?i)\bhdr(?:10)?\b(?![\s._-]?\+)",
        "badge": "hdr.svg"
    },
    {
        "id": "hdr-imax",
        "groupId": "hdr",
        "name": "IMAX Enhanced",
        "pattern": r"(?i)\b(?:imax|imax[\s._-]?enhanced)\b",
        "badge": "imax.svg"
    },

    # --- Audio Format ---
    {
        "id": "audio-dolby-atmos",
        "groupId": "audio",
        "name": "Dolby Atmos",
        "pattern": r"(?i)\b(?:atmos|dolby[\s._-]?atmos)\b",
        "badge": "dolby-atmos.svg"
    },
    {
        "id": "audio-dts-x",
        "groupId": "audio",
        "name": "DTS:X",
        "pattern": r"(?i)\b(?:dts[\s._-]?x|dtsx)\b",
        "badge": "dts-x.svg"
    },
    {
        "id": "audio-dts-hd",
        "groupId": "audio",
        "name": "DTS-HD Master Audio",
        "pattern": r"(?i)\b(?:dts[\s._-]?hd(?:[\s._-]?(?:ma|master[\s._-]?audio))?|dtshd)\b",
        "badge": "dts-hd.svg"
    },
    {
        "id": "audio-dolby-audio",
        "groupId": "audio",
        "name": "Dolby Audio / DD+ 5.1",
        "pattern": r"(?i)\b(?:ddp|dd\+|eac3|truehd|dolby[\s._-]?(?:digital|audio)|ac3)\b",
        "badge": "dolby-audio.svg"
    },

    # --- Streaming Services ---
    {
        "id": "service-netflix",
        "groupId": "service",
        "name": "Netflix",
        "pattern": r"(?i)\b(?:nf|netflix)\b",
        "badge": "netflix.svg"
    },
    {
        "id": "service-appletv",
        "groupId": "service",
        "name": "Apple TV+",
        "pattern": r"(?i)\b(?:atvp|apple[\s._-]?tv(?:\+|plus)?)\b",
        "badge": "appletv.svg"
    },
    {
        "id": "service-disney",
        "groupId": "service",
        "name": "Disney+",
        "pattern": r"(?i)\b(?:dsnp|disney(?:\+|plus)?)\b",
        "badge": "disney.svg"
    },
    {
        "id": "service-prime",
        "groupId": "service",
        "name": "Prime Video",
        "pattern": r"(?i)\b(?:amzn|prime[\s._-]?video|amazon)\b",
        "badge": "prime.svg"
    },
    {
        "id": "service-max",
        "groupId": "service",
        "name": "Max / HBO Max",
        "pattern": r"(?i)\b(?:hmax|max|hbo[\s._-]?max)\b",
        "badge": "max.svg"
    },
    {
        "id": "service-paramount",
        "groupId": "service",
        "name": "Paramount+",
        "pattern": r"(?i)\b(?:pmtp|paramount(?:\+|plus)?)\b",
        "badge": "paramount.svg"
    },
    {
        "id": "service-hulu",
        "groupId": "service",
        "name": "Hulu",
        "pattern": r"(?i)\bhulu\b",
        "badge": "hulu.svg"
    },
    {
        "id": "service-peacock",
        "groupId": "service",
        "name": "Peacock",
        "pattern": r"(?i)\b(?:peac|peacock)\b",
        "badge": "peacock.svg"
    },
    {
        "id": "service-crunchyroll",
        "groupId": "service",
        "name": "Crunchyroll",
        "pattern": r"(?i)\b(?:cr|crunchyroll)\b",
        "badge": "crunchyroll.svg"
    },
    {
        "id": "service-hoichoi",
        "groupId": "service",
        "name": "Hoichoi",
        "pattern": r"(?i)\bhoichoi\b",
        "badge": "hoichoi.svg"
    },
    {
        "id": "service-zee5",
        "groupId": "service",
        "name": "ZEE5",
        "pattern": r"(?i)\bzee5\b",
        "badge": "zee5.svg"
    },
    {
        "id": "service-sonyliv",
        "groupId": "service",
        "name": "Sony LIV",
        "pattern": r"(?i)\b(?:sonyliv|sony[\s._-]?liv)\b",
        "badge": "sonyliv.svg"
    },

    # --- Sources & Codecs ---
    {
        "id": "source-remux",
        "groupId": "source",
        "name": "REMUX",
        "pattern": r"(?i)^(?!.*\bdvd[\s._-]?remux\b).*\bremux\b",
        "badge": "remux.svg"
    },
    {
        "id": "source-bluray",
        "groupId": "source",
        "name": "Blu-ray Disc",
        "pattern": r"(?i)\b(?:blu[\s._-]?ray|bdrip|brrip)\b",
        "badge": "bluray.svg"
    },
    {
        "id": "source-webdl",
        "groupId": "source",
        "name": "WEB-DL",
        "pattern": r"(?i)\bweb[\s._-]?dl\b",
        "badge": "webdl.svg"
    },
    {
        "id": "source-webrip",
        "groupId": "source",
        "name": "WEBRip",
        "pattern": r"(?i)\bweb[\s._-]?rip\b",
        "badge": "webrip.svg"
    },
    {
        "id": "codec-hevc",
        "groupId": "source",
        "name": "HEVC / x265",
        "pattern": r"(?i)\b(?:hevc|x265|h[\s._-]?265)\b",
        "badge": "hevc.svg"
    },
    {
        "id": "codec-av1",
        "groupId": "source",
        "name": "AV1",
        "pattern": r"(?i)\bav1\b",
        "badge": "av1.svg"
    }
]

def build_manifest(username="YOUR_USERNAME", repo="nuvio-badges-original", branch="main"):
    filters_output = []
    base_url = f"https://cdn.jsdelivr.net/gh/{username}/{repo}@{branch}/badges"

    for f in FILTERS:
        filters_output.append({
            "id": f["id"],
            "groupId": f["groupId"],
            "name": f["name"],
            "pattern": f["pattern"],
            "imageURL": f"{base_url}/{f['badge']}",
            "tagColor": "#00000000",
            "borderColor": "#00000000",
            "textColor": "#00000000",
            "tagStyle": "filled and bordered",
            "isEnabled": True,
            "type": "filter"
        })

    manifest = {
        "groups": GROUPS,
        "filters": filters_output
    }

    out_file = os.path.join(BASE_DIR, "badges.json")
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(manifest, fp, indent=2, ensure_ascii=False)

    print(f"Generated badges.json with {len(filters_output)} filters at {out_file}")

if __name__ == "__main__":
    build_manifest()
