#!/usr/bin/env python3
"""
check-suite-prd.py — pemeriksa mekanis suite e2e yang digenerate langsung dari PRD (alur e2e-prd-generate-spec,
tanpa TC granular). Pasangan `docs/e2e-conventions-prd.md`. Alur lama berbasis TC tetap memakai `check-suite.py`.

Repo ini tidak mem-parse PRD: daftar aturan atomik datang dari harness (`python scripts/harness.py e2e-prd rules
--task <id>` menulis `work-items/<id>/rules-e2e-prd.json`: aturan leaf, induk, prioritas, dan aturan yang ditahan).

Keterlacakan PRD → spec:
  T1 [FINDING] aturan leaf tidak ada di sourceRules spec mana pun, tidak di "Di luar E2E", dan tidak di "Ditahan"
  T2 [FINDING] sourceRules (atau tabel coverage) menyebut ID yang tidak ada di PRD
  T3 [FINDING] sourceRules menyebut ID induk (punya sub-aturan); kutip sub-aturannya
  T4 [FINDING] entri "Di luar E2E" tidak sah: alasan kosong, rujukan tc-backend tidak ditemukan, atau aturan itu
               sekaligus dikutip spec ([REVIEW] bila ada rujukan tc-backend tetapi file tc-backend tidak diberikan)
  T5 [FINDING] aturan yang ditahan temuan PRD terbuka dikutip spec, atau tidak tercantum di "Ditahan"
  T6 [FINDING] priority spec != prioritas tertinggi aturan di sourceRules (P0 Critical, P1 High, P2 Medium, P3 Low)
  T7 [FINDING] header coverage (aturan leaf, spec) atau daftar spec di coverage tidak cocok dengan suite
  T8 [FINDING] PRD sha256 di header coverage != PRD sekarang (generate atau coverage basi)
  T9 [FINDING] DU-nn dipakai spec tetapi tidak ada di file data uji (atau file data uji tidak ada)
  T10 butir Notes «Klausa di luar E2E»: [FINDING] tanpa ID aturan, atau menyebut aturan yang tidak ada di sourceRules
      spec itu; [REVIEW] bila alasannya berupa hambatan data, akun, atau celah PRD (bagian 2 dan S-01 hanya mengizinkan
      klausa yang efeknya murni server; script tidak bisa menilai itu, hanya menampakkan alasan yang jelas bukan)
Gaya spec (sama dengan check-suite.py, tidak bergantung TC):
  C4 id frontmatter != nama folder · C5 tanpa `- Mode:` · C6 > 35 langkah tanpa alasan · C9 [REVIEW] absence tanpa
  anchor · C11 butir pertama Prerequisites bukan `- Mode:` · C12 "→ … tampil" di langkah aksi · C13 "Kosongkan
  Search" tanpa aksi · C14 tunggu > 30 detik · C15 rujukan proses di Prerequisites/Notes · C16 "latar tabel"/"hook
  suite" · C17 Spectra.env tanpa Prerequisites · C18 rujukan langkah melewati jumlah langkah · C19 [REVIEW] hitungan
  toast tanpa tunggu toast lama · C20 placeholder generator · C21 [REVIEW] aksi tulis (`[Save]`, `[Submit]`,
  `[Continue]`, `[Delete]`, `[Confirm]`, «Pilih label», «konfirmasi aksi») langsung diikuti langkah yang pindah surface, sesi, atau konteks tanpa
  `Verifikasi` atau «Tunggu aksi selesai» di antaranya (bagian 8b butir 8)

Pemakaian:
    python scripts/check-suite-prd.py specs/AdminConsole/SettingsDeviceSku --rules ../prd-harness/work-items/ac-device-sku/rules-e2e-prd.json \
        --coverage docs/coverage/AdminConsoleSettingsDeviceSku.md --data docs/data/AdminConsoleSettingsDeviceSku.md \
        --tc-backend ../admin-console/settings-device-sku/TestCases/tc-settings-device-sku-backend.md
Exit 1 bila ada [FINDING].
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

LIMIT = 35
SPECTRA_RANK = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
PRIORITY = {"P0": "Critical", "P1": "High", "P2": "Medium", "P3": "Low"}
DU_RE = re.compile(r"\bDU-\d{2,3}\b")
BE_CASE_RE = re.compile(r"\bTC-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*-BE-\d+\b")
SPEC_ROW_RE = re.compile(r"^\|\s*`?(TC-[A-Z0-9]+-[A-Z0-9]+-E2E-\d+[^\s|`]*)`?\s*\|", re.M)


def read(p):
    return Path(p).read_text(encoding="utf-8").replace("\r\n", "\n")


def frontmatter(text):
    parts = text.split("---", 2)
    return parts[1] if len(parts) > 2 else ""


def source_rules(fm):
    """IDs listed under `sourceRules:` (one `- <id>` per line, until the next top-level key)."""
    block = fm.split("sourceRules:", 1)
    if len(block) < 2:
        return []
    block = re.split(r"\n\w+:", block[1], maxsplit=1)[0]
    return [m.group(1).strip("`'\"") for m in re.finditer(r"^\s*-\s*(\S+)", block, re.M)]


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
PROCESS_WORDS = re.compile(r"(?i)dipecah dari|dipindah(?:kan)? dari|\borkestrator\b|\bbrief\b|\brencana\b|(?-i:\bQ-[0-9]+\b|\bD-[1-9]\b)")
PLACEHOLDER_GEN = re.compile(r"\(\[0-9\]\+\)")
PRE_WORDS = re.compile(r"(?i)latar tabel|dilakukan di hook suite")
STEP_REF = re.compile(r"(?i)\blangkah (\d+)(?:\s*(?:sampai|s\.d\.|hingga|-|–)\s*(\d+))?")
WRITE_ACTION = re.compile(r"^\d+\.\s+(?:Klik\s+`\[(?:Save|Submit|Continue|Delete|Confirm|Simpan)\]`|Pilih label\b|"
                          r".*\bkonfirmasi aksi\b)", re.I)
SURFACE_MOVE = re.compile(r"^\d+\.\s+(?:Buka|Navigasi|Pindah|Muat ulang|Refresh|Logout|Login|Ganti akun|Di konteks|"
                          r"Kirim request|Klik tab|Pilih tab)\b", re.I)
KLAUSA_BULLET = re.compile(r"(?i)klausa di luar e2e")
HINDRANCE = re.compile(r"(?i)data uji|\bakun (?:kedua|lain|tidak|tambahan)\b|(?:tidak|belum) (?:ada|tersedia|tercantum)"
                       r"(?: di| pada)? (?:data|akun|group|plan)|jalur navigasi|tidak memberi jalur|PRD (?:ini )?tidak|"
                       r"tidak (?:dinyatakan|ditulis) (?:di )?PRD")
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
    for cur, nxt in zip(lines, lines[1:]):
        if WRITE_ACTION.match(cur) and "setup column" not in cur.lower() and SURFACE_MOVE.match(nxt):
            out("REVIEW", "C21", f"{folder}: langkah {cur.split('.', 1)[0]} aksi tulis langsung diikuti langkah "
                                 f"{nxt.split('.', 1)[0]} yang pindah surface/sesi tanpa «Tunggu aksi selesai» (8b.8)")
    if PLACEHOLDER_GEN.search(text):
        out("FINDING", "C20", f"{folder}: memuat placeholder «([0-9]+)» yang belum diganti angka nyata")
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
    for blk in re.split(r"(?m)^(?=### )", steps):
        blines = [l for l in blk.split("\n") if re.match(r"^\d+\. ", l)]
        for i, l in enumerate(blines):
            if re.search(r"Verifikasi\s+Tidak ada (?:entri|pencatatan)", l, re.I):
                before = " ".join(blines[:i])
                if not re.search(r"Verifikasi[^\n]*(?:jangkar|anchor|memuat entri|Failed|tampil)", before, re.I) \
                        and "jangkar" not in l.lower():
                    out("REVIEW", "C9", f"{folder}: «{l[:90]}» tanpa anchor positif sebelumnya di blok yang sama")
                    break


def bullets(text):
    """Notes bullets as whole blocks: a bullet line plus its continuation lines."""
    out, current = [], None
    for line in text.split("\n"):
        if re.match(r"^\s*[-*]\s", line):
            current = [line]
            out.append(current)
        elif current is not None and line.strip() and re.match(r"^\s+\S", line):
            current.append(line)
        else:
            current = None
    return [" ".join(x.strip() for x in block) for block in out]


def klausa_checks(folder, notes, ids, rules, out):
    """T10: every «Klausa di luar E2E» bullet names a rule this spec cites; obvious non-server reasons are shown."""
    qids = sorted(rules, key=len, reverse=True)
    for bullet in bullets(notes):
        if not KLAUSA_BULLET.search(bullet):
            continue
        cited = [q for q in qids if re.search(rf"(?<![A-Za-z0-9]){re.escape(q)}(?![A-Za-z0-9])", bullet)]
        if not cited:
            out("FINDING", "T10", f"{folder}: butir «Klausa di luar E2E» tanpa ID aturan («{bullet[:70]}»)")
        elif not any(q in ids for q in cited):
            out("FINDING", "T10", f"{folder}: «Klausa di luar E2E» menyebut {cited[0]} yang tidak ada di sourceRules spec ini")
        hit = HINDRANCE.search(bullet)
        if hit:
            out("REVIEW", "T10", f"{folder}: «Klausa di luar E2E» beralasan «{hit.group(0)}», bukan efek server murni; "
                                 f"periksa bagian 2 dan S-01 («{bullet[:60]}»)")


def coverage_sections(text):
    """{heading: body} of the coverage page's `## ` sections."""
    out, current = {}, None
    for line in text.split("\n"):
        if line.startswith("## "):
            current = line[3:].strip()
            out[current] = []
        elif current is not None:
            out[current].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def table_rows(body):
    """[[cells]] of the data rows of the first markdown table in `body` (header and separator dropped)."""
    rows, seen_sep = [], False
    for line in body.split("\n"):
        if not line.strip().startswith("|"):
            if rows or seen_sep:
                break
            continue
        if re.match(r"^\s*\|[\s:|\-]+\|\s*$", line):
            seen_sep = True
            continue
        if seen_sep:
            body_cells = re.split(r"(?<!\\)\|", line.strip())
            rows.append([c.strip() for c in body_cells[1:-1]])
    return rows


def first_id(cell):
    return cell.strip().strip("`*").split("`")[0].strip()


def section(sections, *names):
    for name in names:
        for key, body in sections.items():
            if key.lower().startswith(name.lower()):
                return body
    return ""


def main(argv=None):
    ap = argparse.ArgumentParser(description="pemeriksa mekanis suite e2e berbasis PRD")
    ap.add_argument("suite")
    ap.add_argument("--rules", required=True, help="rules-e2e-prd.json dari harness (e2e-prd rules)")
    ap.add_argument("--coverage", help="docs/coverage/<Group><SubModul>.md")
    ap.add_argument("--data", help="docs/data/<Group><SubModul>.md")
    ap.add_argument("--tc-backend", help="tc-<modul>-backend.md (rujukan tabel Di luar E2E)")
    a = ap.parse_args(argv)
    suite = Path(a.suite)
    inventory = json.loads(read(a.rules))
    prefix = inventory.get("prefix") or "PRD"
    rules = {r["qid"]: r for r in inventory.get("rules", [])}
    parents = {p if ("-LOGIC-" in p or p.startswith("F-")) else f"{prefix}:{p}" for p in inventory.get("parents", [])}
    held = inventory.get("held", {}) or {}
    findings = 0
    per_code = {}

    def out(level, code, msg):
        nonlocal findings
        if level == "FINDING":
            findings += 1
        per_code[code] = per_code.get(code, 0) + 1
        print(f"[{level}] {code} {msg}")

    specs = sorted(suite.glob("TC-*/spec.md"))
    cited = {}
    data_ids = set()
    if a.data and Path(a.data).is_file():
        data_ids = set(re.findall(r"^\|\s*`?(DU-\d{2,3})`?\s*\|", read(a.data), re.M))
    for sp in specs:
        text = read(sp)
        fm = frontmatter(text)
        folder = sp.parent.name
        mid = re.search(r"^id:\s*(\S+)", fm, re.M)
        if not mid or mid.group(1) != folder:
            out("FINDING", "C4", f"{folder}: id frontmatter «{mid.group(1) if mid else '-'}» != nama folder")
        ids = source_rules(fm)
        if not ids:
            out("FINDING", "T2", f"{folder}: frontmatter tanpa sourceRules")
        for rid in ids:
            if rid in parents:
                out("FINDING", "T3", f"{folder}: sourceRules {rid} adalah aturan induk; kutip sub-aturannya")
            elif rid not in rules:
                out("FINDING", "T2", f"{folder}: sourceRules {rid} tidak ada di PRD")
            else:
                cited.setdefault(rid, []).append(folder)
                if rid in held:
                    out("FINDING", "T5", f"{folder}: sourceRules {rid} ditahan temuan {', '.join(held[rid])}")
        mp = re.search(r"^priority:\s*(\w+)", fm, re.M)
        ranks = [rules[r].get("spectra_priority") or PRIORITY.get(rules[r].get("priority"), "Medium")
                 for r in ids if r in rules]
        if mp and ranks:
            expected = min(ranks, key=lambda p: SPECTRA_RANK.get(p, 9))
            if mp.group(1) != expected:
                out("FINDING", "T6", f"{folder}: priority {mp.group(1)} != {expected} (tertinggi aturan sumber)")
        steps, notes = steps_and_notes(text)
        n = len(re.findall(r"^\d+\. ", steps, re.M))
        if not re.search(r"^- Mode:", text, re.M):
            out("FINDING", "C5", f"{folder}: tidak ada baris «- Mode:» di Prerequisites")
        if n > LIMIT and not re.search(r"di atas smell|(?<!\d)35 langkah", notes):
            out("FINDING", "C6", f"{folder}: {n} langkah (> {LIMIT}) tanpa alasan di Notes")
        style_checks(folder, text, out)
        klausa_checks(folder, notes, ids, rules, out)
        used_du = sorted(set(DU_RE.findall(text)))
        if used_du and not (a.data and Path(a.data).is_file()):
            out("FINDING", "T9", f"{folder}: memakai {', '.join(used_du[:5])} tetapi file data uji tidak diberikan/tidak ada")
        else:
            for du in used_du:
                if du not in data_ids:
                    out("FINDING", "T9", f"{folder}: {du} tidak ada di {Path(a.data).name}")

    outside, ditahan = {}, {}
    cov_text = read(a.coverage) if a.coverage and Path(a.coverage).is_file() else ""
    backend_text = read(a.tc_backend) if a.tc_backend and Path(a.tc_backend).is_file() else None
    if cov_text:
        sections = coverage_sections(cov_text)
        for cells in table_rows(section(sections, "Di luar E2E")):
            rid = first_id(cells[0]) if cells else ""
            if not rid:
                continue
            outside[rid] = cells
            reason = cells[1].strip() if len(cells) > 1 else ""
            ref = cells[2].strip() if len(cells) > 2 else ""
            if rid not in rules:
                out("FINDING", "T2", f"Di luar E2E: {rid} tidak ada di PRD")
            if not reason or reason in ("-", "—"):
                out("FINDING", "T4", f"Di luar E2E: {rid} tanpa alasan")
            if rid in cited:
                out("FINDING", "T4", f"Di luar E2E: {rid} sekaligus dikutip {', '.join(cited[rid])}")
            refs = BE_CASE_RE.findall(ref)
            if refs and backend_text is None:
                out("REVIEW", "T4", f"Di luar E2E: {rid} merujuk {', '.join(refs)} tetapi --tc-backend tidak diberikan")
            for case in refs if backend_text is not None else []:
                if case not in backend_text:
                    out("FINDING", "T4", f"Di luar E2E: {rid} merujuk {case} yang tidak ada di file tc-backend")
        for cells in table_rows(section(sections, "Ditahan")):
            rid = first_id(cells[0]) if cells else ""
            if rid:
                ditahan[rid] = cells
                if rid not in rules:
                    out("FINDING", "T2", f"Ditahan: {rid} tidak ada di PRD")
        header = cov_text.split("\n## ", 1)[0]
        m = re.search(r"(\d+)\s+aturan leaf", header)
        if m and int(m.group(1)) != len(rules):
            out("FINDING", "T7", f"coverage menyebut {m.group(1)} aturan leaf, PRD berisi {len(rules)}")
        m = re.search(r"(\d+)\s+spec\b", header)
        if m and int(m.group(1)) != len(specs):
            out("FINDING", "T7", f"coverage menyebut {m.group(1)} spec, suite berisi {len(specs)}")
        if not re.search(r"aturan leaf", header):
            out("FINDING", "T7", "header coverage tanpa jumlah «<N> aturan leaf»")
        cov_specs = set(SPEC_ROW_RE.findall(section(sections, "Spec")))
        folders = {sp.parent.name for sp in specs}
        for f in sorted(folders - cov_specs):
            out("FINDING", "T7", f"spec {f} tidak ada di tabel Spec coverage")
        for f in sorted(cov_specs - folders):
            out("FINDING", "T7", f"coverage menyebut {f} yang tidak ada sebagai folder")
        sha = re.search(r"PRD sha256 `([0-9a-f]{8,64})`", header)
        current = str(inventory.get("sha256") or "")
        if not sha:
            out("FINDING", "T8", "header coverage tanpa «PRD sha256 `…`»")
        elif current and not current.startswith(sha.group(1)):
            out("FINDING", "T8", f"PRD sha256 coverage {sha.group(1)} != PRD sekarang {current[:16]}")
    elif specs:
        out("FINDING", "T7", "halaman coverage tidak diberikan atau tidak ada")

    for rid in sorted(held):
        if rid in rules and cov_text and rid not in ditahan:
            out("FINDING", "T5", f"{rid} ditahan temuan {', '.join(held[rid])} tetapi tidak tercantum di Ditahan")
    for rid in rules:
        if rid not in cited and rid not in outside and rid not in ditahan:
            out("FINDING", "T1", f"{rid} tidak tercakup spec mana pun, tidak di Di luar E2E, tidak di Ditahan")

    print(f"\n{len(specs)} spec, {len(rules)} aturan leaf, {len(cited)} tercakup spec, {len(outside)} di luar E2E, "
          f"{len(ditahan)} ditahan, {findings} temuan")
    if per_code:
        order = lambda item: (item[0][0], int(item[0][1:]))
        print("per kode: " + ", ".join(f"{c} {n}" for c, n in sorted(per_code.items(), key=order)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
