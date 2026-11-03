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
  C11 [FINDING] butir pertama Prerequisites bukan baris `- Mode:` (R-01)
  C12 [FINDING] langkah aksi (bukan Verifikasi) memuat tanda "→ … tampil" (R-02)
  C13 [FINDING] "Kosongkan Search" tanpa aksi (Enter, lewat, ←, ✕) pada Search tabel (R-16, bagian 8b butir 9)
  C14 [FINDING] langkah "Tunggu N menit/jam/hari" atau "Tunggu" di atas 30 detik, di luar idiom "batas tunggu" (R-10)
  C15 [FINDING] Prerequisites/Notes memuat rujukan proses atau narasi pemecahan (rencana, brief, orkestrator, dipecah/dipindah dari) (R-17)
  C16 [FINDING] Prerequisites memuat "latar tabel" atau "dilakukan di hook suite" (R-09)
  C17 [FINDING] Spectra.env.<NAMA> dipakai di Test Steps tetapi nama itu tidak ada di Prerequisites (R-07)
  C18 [FINDING] rujukan "langkah N" melewati jumlah langkah spec (R-04)
  C19 [REVIEW]  "Verifikasi hanya N toast" tanpa "Tunggu toast lama hilang" sebelumnya di blok yang sama (R-12)

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
    block = re.split(r"\n\w+:", block[1], maxsplit=1)[0]
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


def heading_split(text, title):
    return re.split(rf"(?m)^## {title}[ \t]*$", text, maxsplit=1)


def steps_and_notes(text):
    body = text.split("---", 2)[-1]
    steps = heading_split(body, "Test Steps")[-1]
    notes = ""
    parts = heading_split(steps, "Notes")
    if len(parts) > 1:
        steps, notes = parts
    return steps, notes


def prerequisites(text):
    body = text.split("---", 2)[-1]
    parts = heading_split(body, "Prerequisites")
    if len(parts) < 2:
        return ""
    return heading_split(parts[1], "Test Steps")[0]


ARROW = re.compile(r"→[^\n]*\btampil")
CLEAR_SEARCH = re.compile(r"(?i)\bkosongkan search\b")
CLEAR_ACTION = re.compile(r"(?i)enter|lewat|\(←\)|←|✕|dropdown")
LONG_WAIT = re.compile(r"(?i)(?<!batas )\btunggu (?:\d+ (?:menit|jam|hari)\b|(?:3[1-9]|[4-9]\d|\d{3,}) detik)")
PROCESS_WORDS = re.compile(r"(?i)dipecah dari|dipindah(?:kan)? dari|\borkestrator\b|\bbrief\b|\brencana\b")
PRE_WORDS = re.compile(r"(?i)latar tabel|dilakukan di hook suite")
STEP_REF = re.compile(r"(?i)\blangkah (\d+)(?:\s*(?:sampai|s\.d\.|hingga|-|–)\s*(\d+))?")
ONLY_TOAST = re.compile(r"(?i)Verifikasi hanya (?:satu|\d+) toast")
OLD_TOAST_GONE = re.compile(r"(?i)toast (?:lama|sebelumnya) hilang")


def style_checks(folder, text, out):
    pre = prerequisites(text)
    steps, notes = steps_and_notes(text)
    lines = [l for l in steps.split("\n") if re.match(r"^\d+\. ", l)]
    items = [l for l in pre.split("\n") if l.startswith("- ")]
    if items and not items[0].startswith("- Mode:"):
        out("FINDING", "C11", f"{folder}: butir pertama Prerequisites bukan «- Mode:» («{items[0][:60]}»)")
    for l in lines:
        num = l.split(".", 1)[0]
        is_assert = re.match(r"^\d+\.\s+Verifikasi", l)
        if not is_assert and ARROW.search(l):
            out("FINDING", "C12", f"{folder}: langkah {num} memuat «→ … tampil» di langkah aksi")
        if CLEAR_SEARCH.search(l) and not CLEAR_ACTION.search(l):
            out("FINDING", "C13", f"{folder}: langkah {num} «Kosongkan Search» tanpa aksi")
        if LONG_WAIT.search(l):
            out("FINDING", "C14", f"{folder}: langkah {num} «{LONG_WAIT.search(l).group(0)}»; atur jam, bukan menunggu")
    for name, part in (("Prerequisites", pre), ("Notes", notes)):
        for m in PROCESS_WORDS.finditer(part):
            out("FINDING", "C15", f"{folder}: {name} memuat «{m.group(0)}»")
    for m in PRE_WORDS.finditer(pre):
        out("FINDING", "C16", f"{folder}: Prerequisites memuat «{m.group(0)}»")
    used = set(re.findall(r"Spectra\.env\.(\w+)", steps))
    listed = set(re.findall(r"\b([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)\b", pre))
    for name in sorted(used - listed):
        out("FINDING", "C17", f"{folder}: Spectra.env.{name} dipakai di Test Steps tetapi tidak ada di Prerequisites")
    n = len(lines)
    for m in STEP_REF.finditer(pre + "\n" + steps + "\n" + notes):
        hi = int(m.group(2) or m.group(1))
        if hi > n:
            out("FINDING", "C18", f"{folder}: rujukan «{m.group(0)}» melewati {n} langkah")
    for blk in re.split(r"(?m)^(?=### )", steps):
        blines = [l for l in blk.split("\n") if re.match(r"^\d+\. ", l)]
        for i, l in enumerate(blines):
            if ONLY_TOAST.search(l) and not any(OLD_TOAST_GONE.search(x) for x in blines[:i]):
                out("REVIEW", "C19", f"{folder}: langkah {l.split('.', 1)[0]} hitungan toast tanpa «Tunggu toast lama hilang» sebelumnya")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    suite = Path(sys.argv[1])
    tc_path = Path(sys.argv[2])
    cov_path = Path(sys.argv[3]) if len(sys.argv) > 3 else None
    findings = 0
    per_code = {}

    def out(level, code, msg):
        nonlocal findings
        if level == "FINDING":
            findings += 1
        per_code[code] = per_code.get(code, 0) + 1
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
        style_checks(folder, text, out)
        for blk in re.split(r"(?m)^(?=### )", steps):
            lines = [l for l in blk.split("\n") if re.match(r"^\d+\. ", l)]
            for i, l in enumerate(lines):
                if re.search(r"Verifikasi\s+Tidak ada (?:entri|pencatatan)", l, re.I):
                    before = " ".join(lines[:i])
                    if not re.search(r"Verifikasi[^\n]*(?:jangkar|anchor|memuat entri|Failed|tampil|bertambah tepat satu|entri baru itu adalah)", before, re.I) and "jangkar" not in l.lower():
                        out("REVIEW", "C9", f"{folder}: «{l[:90]}» tanpa anchor positif sebelumnya di blok yang sama")
                        break

    for tid, folders in owner.items():
        if len(folders) > 1:
            if all(re.search(r"^- Mode:\s*mock", read(suite / f / "spec.md"), re.M)
                   and "Pembagian TC lintas spec" in read(suite / f / "spec.md") for f in folders):
                continue
            # TC terbelah presence/absence (S-05 [2026-10-13]): sah bila tiap spec mencatat pembagiannya di Notes
            if all(re.search(r"Pembagian TC lintas spec|\bS-05\b", read(suite / f / "spec.md")) for f in folders):
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
    if per_code:
        print("per kode: " + ", ".join(f"{c} {n}" for c, n in sorted(per_code.items(), key=lambda x: int(x[0][1:]))))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
