#!/usr/bin/env python3
"""
check-suite.py — pemeriksa mekanis hasil generate spec e2e (pelengkap `spectra lint` dan skill tagsamurai-e2e-audit).

Memeriksa satu suite terhadap TC granular sumbernya:
  C1 [FINDING] TC di tc-[modul].md yang tidak ada di sourceTc spec mana pun dan tidak tercatat hanya-BE di coverage
  C2 [FINDING] id TC muncul di sourceTc lebih dari satu spec
  C3 [FINDING] sourceTc menunjuk id yang tidak ada di tc-[modul].md
  C4 [FINDING] nama folder spec != field id di frontmatter
  C5 [FINDING] spec tanpa baris `Mode:` di Prerequisites
  C6 [FINDING] spec di atas 35 langkah tanpa alasan di Notes (kata kunci: "di atas smell" atau "35 langkah")
  C7 [FINDING] jumlah TC di header docs/coverage != jumlah TC di tc-[modul].md; spec di coverage != folder spec
  C8 [REVIEW]  tc-[modul].md lebih baru dari spec terbaru (generate mungkin basi)
  C9 [REVIEW]  asersi absence ("tidak ada entri/pencatatan") tanpa langkah anchor positif dalam blok yang sama
  C10 [FINDING] priority spec != prioritas tertinggi TC sumber (mapping konvensi bagian 8: P0 Critical, P1 High, P2 Medium, P3 Low)

Pemakaian:
    python scripts/check-suite.py specs/Auth/AccountActivation ../auth/account-activation/TestCases/tc-account-activation.md docs/coverage/AuthAccountActivation.md
Exit 1 bila ada [FINDING].
"""
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

LIMIT = 35
PRIORITY = {"P0": ("Critical", 0), "P1": ("High", 1), "P2": ("Medium", 2), "P3": ("Low", 3)}


def read(p):
    return Path(p).read_text(encoding="utf-8").replace("\r\n", "\n")


def frontmatter(text):
    parts = text.split("---", 2)
    return parts[1] if len(parts) > 2 else ""


def source_tc(fm):
    block = fm.split("sourceTc:", 1)
    if len(block) < 2:
        return []
    block = re.split(r"\n\w+:", block[1], 1)[0]
    return re.findall(r"TC-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*-\d+", block)


def tc_priorities(tc_text):
    result = {}
    col = None
    for line in tc_text.split("\n"):
        if not line.startswith("|"):
            col = None if not line.strip() else col
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if cells and cells[0] == "TC ID":
            col = cells.index("Priority") if "Priority" in cells else None
            continue
        if col is not None and len(cells) > col and re.fullmatch(r"TC-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*-\d+", cells[0]):
            if cells[col] in PRIORITY:
                result.setdefault(cells[0], cells[col])
    return result


def steps_and_notes(text):
    body = text.split("---", 2)[-1]
    steps = body.split("## Test Steps", 1)[-1]
    notes = ""
    if "## Notes" in steps:
        steps, notes = steps.split("## Notes", 1)
    return steps, notes


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    suite = Path(sys.argv[1])
    tc_path = Path(sys.argv[2])
    cov_path = Path(sys.argv[3]) if len(sys.argv) > 3 else None
    findings = 0

    def out(level, code, msg):
        nonlocal findings
        if level == "FINDING":
            findings += 1
        print(f"[{level}] {code} {msg}")

    tc_text = read(tc_path)
    tc_ids = []
    for m in re.finditer(r"^\|\s*(TC-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*-\d+)\s*\|", tc_text, re.M):
        if m.group(1) not in tc_ids:
            tc_ids.append(m.group(1))

    tc_prio = tc_priorities(tc_text)
    specs = sorted(suite.glob("TC-*/spec.md"))
    owner = {}
    newest = 0
    for sp in specs:
        text = read(sp)
        newest = max(newest, sp.stat().st_mtime)
        fm = frontmatter(text)
        folder = sp.parent.name
        mid = re.search(r"^id:\s*(\S+)", fm, re.M)
        if not mid or mid.group(1) != folder:
            out("FINDING", "C4", f"{folder}: id frontmatter «{mid.group(1) if mid else '-'}» != nama folder")
        for tid in source_tc(fm):
            owner.setdefault(tid, []).append(folder)
            if tid not in tc_ids:
                out("FINDING", "C3", f"{folder}: sourceTc {tid} tidak ada di {tc_path.name}")
        mp = re.search(r"^priority:\s*(\w+)", fm, re.M)
        ranks = [PRIORITY[tc_prio[t]] for t in source_tc(fm) if t in tc_prio]
        if mp and ranks:
            expected = min(ranks, key=lambda r: r[1])[0]
            if mp.group(1) != expected:
                out("FINDING", "C10", f"{folder}: priority {mp.group(1)} != {expected} (tertinggi TC sumber)")
        steps, notes = steps_and_notes(text)
        n = len(re.findall(r"^\d+\. ", steps, re.M))
        if not re.search(r"^- Mode:", text, re.M):
            out("FINDING", "C5", f"{folder}: tidak ada baris «- Mode:» di Prerequisites")
        if n > LIMIT and not re.search(r"di atas smell|35 langkah", notes):
            out("FINDING", "C6", f"{folder}: {n} langkah (> {LIMIT}) tanpa alasan di Notes")
        for blk in re.split(r"(?m)^(?=### )", steps):
            lines = [l for l in blk.split("\n") if re.match(r"^\d+\. ", l)]
            for i, l in enumerate(lines):
                if re.search(r"Verifikasi\s+Tidak ada (?:entri|pencatatan)", l, re.I):
                    before = " ".join(lines[:i])
                    if not re.search(r"Verifikasi[^\n]*(?:jangkar|anchor|memuat entri|Failed|tampil)", before, re.I) and "jangkar" not in l.lower():
                        out("REVIEW", "C9", f"{folder}: «{l[:90]}» tanpa anchor positif sebelumnya di blok yang sama")
                        break

    for tid, folders in owner.items():
        if len(folders) > 1:
            if all(re.search(r"^- Mode:\s*mock", read(suite / f / "spec.md"), re.M)
                   and "Pembagian TC lintas spec" in read(suite / f / "spec.md") for f in folders):
                continue
            out("FINDING", "C2", f"{tid} ada di sourceTc {len(folders)} spec: {', '.join(folders)}")

    be_only = set()
    cov_text = ""
    if cov_path and cov_path.exists():
        cov_text = read(cov_path)
        tail = cov_text.split("TC hanya-BE", 1)
        if len(tail) > 1:
            be_only = set(re.findall(r"^\|\s*(TC-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*-\d+)\s*\|", tail[1], re.M))
    for tid in tc_ids:
        if tid not in owner and tid not in be_only:
            out("FINDING", "C1", f"{tid} tidak tercakup spec mana pun dan tidak tercatat hanya-BE")

    if cov_text:
        m = re.search(r"\((\d+)\s*TC", cov_text)
        if m and int(m.group(1)) != len(tc_ids):
            out("FINDING", "C7", f"coverage menyebut {m.group(1)} TC, {tc_path.name} berisi {len(tc_ids)} TC")
        cov_specs = set(re.findall(r"^\|\s*(TC-[A-Z0-9]+-[A-Z0-9]+-E2E-\d+[^\s|]*)\s*\|", cov_text, re.M))
        folders = {sp.parent.name for sp in specs}
        for f in sorted(folders - cov_specs):
            out("FINDING", "C7", f"spec {f} tidak ada di coverage")
        for f in sorted(cov_specs - folders):
            out("FINDING", "C7", f"coverage menyebut {f} yang tidak ada sebagai folder")

    if specs and tc_path.stat().st_mtime > newest:
        out("REVIEW", "C8", f"{tc_path.name} lebih baru dari spec terbaru; periksa apakah ada TC/baris yang berubah setelah generate")

    print(f"\n{len(specs)} spec, {len(tc_ids)} TC, {len(owner)} TC tercakup, {findings} temuan")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
