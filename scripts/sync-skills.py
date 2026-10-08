#!/usr/bin/env python3
"""
sync-skills.py — menjaga salinan skill `.claude/skills` dan `.agents/skills` tetap sama.

Hanya skill berawalan `tagsamurai-e2e-`. Perbedaan akhir baris (CRLF/LF) diabaikan.

Pemakaian:
    python scripts/sync-skills.py --check                 # exit 1 bila ada drift
    python scripts/sync-skills.py --from agents           # salin .agents -> .claude (default)
    python scripts/sync-skills.py --from claude           # salin .claude -> .agents
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = {"claude": ROOT / ".claude" / "skills", "agents": ROOT / ".agents" / "skills"}


def norm(b):
    return b.replace(b"\r\n", b"\n")


def files(base):
    return {p.relative_to(base): p for p in base.glob("tagsamurai-e2e-*/**/*") if p.is_file()}


def main():
    args = sys.argv[1:]
    check = "--check" in args
    src_name = "agents"
    if "--from" in args:
        src_name = args[args.index("--from") + 1]
    dst_name = "claude" if src_name == "agents" else "agents"
    src, dst = DIRS[src_name], DIRS[dst_name]
    sf, df = files(src), files(dst)
    drift = 0
    for rel, sp in sorted(sf.items()):
        dp = df.get(rel)
        if dp is None or norm(sp.read_bytes()) != norm(dp.read_bytes()):
            drift += 1
            print(("beda   " if dp else "hilang ") + str(rel))
            if not check:
                target = dst / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                data = norm(sp.read_bytes())
                if dp is not None and b"\r\n" in dp.read_bytes():
                    data = data.replace(b"\n", b"\r\n")
                target.write_bytes(data)
    for rel in sorted(set(df) - set(sf)):
        drift += 1
        print(f"lebih  {rel} (hanya ada di {dst_name})")
    print(f"{drift} perbedaan" + (" (belum disalin, mode --check)" if check else ""))
    return 1 if (check and drift) else 0


if __name__ == "__main__":
    sys.exit(main())
