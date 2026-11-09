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
  T10 butir Notes «Klausa di luar E2E»: [FINDING] tanpa ID aturan, menyebut aturan yang tidak ada di sourceRules
      spec itu, atau tanpa satu pun dari tiga alasan sah bagian 2 (efek server murni, visual non-deterministik, lintas
      sistem; ditambah keadaan yang hilang sebelum teramati, 8b.8): hambatan data, akun, volume, modul lain, perilaku
      klien, atau delegasi PRD lain harus diuji; [REVIEW] bila alasannya memuat kata hambatan (data uji, akun kedua, celah
      PRD) di samping alasan sah (script hanya menilai kata, bukan kebenarannya)
  T11 [FINDING] baris «Tidak berlaku» di coverage: aturan itu aturan PRD (bukan kewajiban turunan `obligation`),
      alasannya tanpa rujukan baris `L<n>` atau § PRD, atau aturan itu sekaligus dikutip spec. T1 juga menerima
      kewajiban turunan yang tercantum di «Tidak berlaku»
Subjudul dan pembagian klausa (R-25, R-29; hanya di salinan Internal):
  T12 [FINDING] ID di sourceRules tanpa subjudul `### <ID>` di Test Steps
  T13 [FINDING] subjudul ganda untuk satu ID, atau subjudul yang menyebut aturan di luar sourceRules spec itu
  T14 [FINDING] butir Notes «Pembagian klausa lintas spec» melimpahkan klausa ke `spec NNN` yang tidak mengutip satu pun aturan yang
                disebut tepat sebelum rujukan itu (atau ke spec yang tidak ada di suite)
Bentuk klausa yang paling sering setengah diasersi (R-30..R-32; hanya di salinan Internal; semuanya [REVIEW], petunjuk untuk auditor):
  T15 [REVIEW] teks aturan menyebut beberapa permukaan («di X dan Y») tetapi subjudul aturan itu tidak memuat nama salah satunya
  T16 [REVIEW] angka bersatuan di teks aturan (24 jam, 7 hari, …) tidak muncul di subjudul aturan itu
  T17 [REVIEW] klausa «hanya/selain/kecuali» tetapi subjudul aturan itu tanpa asersi ketiadaan («tidak ada/tampil/…», «tanpa»)
  T18 [FINDING] aturan baris matriks kolom punya klausa `duties` (Sort, Search, Filter, Hover, Klik, Nilai kosong, Hidden default) yang tidak
      disebut satu langkah pun di subjudul aturan itu dan tidak dikesampingkan lewat butir Notes «Klausa di luar E2E» (T-4: klausa per kolom
      adalah klausa baris, bukan aturan sendiri; dulu tiap klausa adalah aturan leaf yang dijaga T1). Berlaku juga untuk klausa widget
      tabel pada kewajiban turunan (Search, Filter Panel, Sort, Setup Column, Pagination, Download, Kombinasi; testcase-conventions P5 5b..5r)
  C22 [REVIEW] langkah «Tab hingga/sampai/berulang …» tidak deterministik (R-33)
  T22 [FINDING] butir Notes spec atau butir `## Catatan` coverage mengakui klausa «belum diasersi/belum diuji» tanpa disposisi sah (Klausa di luar E2E,
      Temuan PRD, atau Ditahan): klausa yang tidak dites dan tidak punya tempat adalah celah diam, bukan catatan
  C29 [FINDING] langkah yang mengklik `[Delete]` langsung di Bulk Action Bar (pola usang); foundation memakai satu tombol `Bulk Action` + overlay (prd-conventions §8)
  C32 [REVIEW] «Klausa di luar E2E» beralasan lintas sistem / tidak teramati padahal permukaannya (Activity Log, System Log, token, counter, notifikasi, saldo) tercantum di suite.md sebagai kemampuan baca
  C33 [REVIEW] `Verifikasi` «sedikitnya/minimal/setidaknya satu baris» sebagai bukti pada audit trail permanen: kunci konstan lolos oleh baris sisa run atau spek lain; pakai baseline dan selisih
  T18 juga menegakkan duty yang membawa `match` (sel sync matrix dan action resilience: permukaan, state yang tetap, teks toast): satu string `match` harus muncul di subjudul aturannya
  T19 [FINDING] literal klausa `duties` (`Klausa fungsi:`, nilai berkutip) yang muncul di subjudul aturannya hanya di langkah aksi atau judul, tanpa satu `Verifikasi` yang memuatnya (disebut, belum diasersi)
  T20 [REVIEW] klausa yang butuh baris data khusus (markup, payload, karakter pola) tetapi file data uji tidak memuat nilai seperti itu
  C24 [REVIEW] langkah aksi bersyarat («bila/jika/kalau/apabila …»): langkah satu jalur, kondisinya disiapkan di Prerequisites atau hook
  T18 juga menegakkan `Batas: sisi lolos` (nilai tepat di batas diterima), `Status: pulihkan lalu ulangi` (status dipulihkan, aksi yang sama diulang dan diproses), `Mutasi: data backend dan efek samping` (aturan yang menyatakan perubahan state: satu `Verifikasi` membaca hasil tersimpan lewat jalur lain dan efek sampingnya, testcase-conventions §4) dan `Penolakan: state tidak berubah` (aturan yang menyatakan penolakan atau kegagalan sisi server: state yang diubah aksi itu tetap, dibaca lewat jalur yang tidak memakai request yang gagal) dan `Log: permukaan <X>` (tiap permukaan log yang disebut aturan, lewat `match`)
  T26 [REVIEW] klausa `Delegasi: <dokumen> §<n>` (baris PRD menyerahkan perilaku ke foundation) yang tidak disebut satu pun di subjudul aturan itu: sebut «<dokumen> §<n>» di Verifikasi yang menegaskan nilainya, atau butir «Klausa di luar E2E» / «dimiliki <modul pemilik>»
  C34 [REVIEW] `Verifikasi` yang membaca entri log permanen (Allocation/Activity/System/User Log, Changelog) sesudah aksi tulis spek itu (sepuluh langkah sebelumnya) tanpa tunggu atau polling dalam enam langkah: penulisan log best-effort, baca langsung bisa gagal atau lolos karena sebab lain
  C35 [REVIEW] `Verifikasi` dengan kutipan yang sama muncul lagi di blok berikutnya tanpa langkah pembersih (muat ulang, kosongkan, hilang) di antaranya: kutipan blok lama bisa meloloskan asersi blok baru
  C36 [REVIEW] `Verifikasi` jumlah email yang naik («tepat satu email baru», baseline+n) tanpa tunggu atau polling dalam tiga langkah sebelumnya: email dikirim best-effort sesudah commit, email kedua yang terlambat tidak terdeteksi (run 11: 16 kasus di 13 spek)
  C37 [REVIEW] spek yang memundurkan jam server tetapi membaca log lewat «baris teratas» / «entri teratas»: entri bercap masa lalu tidak ada di atas urutan Date terbaru; cari lewat Search nama unik (run 11: 039, 040, 041, 044)
  C38 [REVIEW] langkah Search pada log (Activity Log Session, System Log) dengan email: log itu mencocokkan nama tampil, bukan email; dua user bernama depan sama membuat hitungan «tepat satu» menghitung keduanya (run 11: 097, 099, 105)
  T27 [REVIEW] butir pembagian klausa yang menyebut label duty aturan yang dilimpahkan, padahal langkah spek tujuan tidak memuat kata-kata label itu (run 12: rate limit Submit ditunjuk ke 139, diuji di 144)
  C40 [REVIEW] `Verifikasi` yang membaca state backend (token, password, counter, lock, kotak email) selama intercept yang menjawab sendiri (5xx, timeout, respons ditahan) aktif: permintaan tidak sampai server, asersi tidak bisa gagal (run 12: 138, 142)
  C39 [REVIEW] dua `Verifikasi` toast Error / failed berturut-turut tanpa langkah «Tutup toast» di antaranya: toast Error bertahan sampai ditutup manual, toast blok lama meloloskan asersi blok baru (run 11: 129, 132)
  T24 [REVIEW] butir pembagian dengan «spec NNN» tetapi tanpa ID aturan sebelumnya: pelimpahan tidak bisa diperiksa
  T25 [REVIEW] butir pembagian yang menyebut id data (DU-nn) atau literal berkutip untuk spec NNN, padahal spec itu tidak memuatnya sama sekali: aturan penghubung ada di spec tujuan, klausanya belum tentu (RP F-1: DU-16 hanya di spek penunjuk)
  C30 [FINDING] langkah «Ketik/Isi/Masukkan `DU-nn`»: id baris data diketik sebagai teks (lima karakter «DU-20» bukan 120 karakter); tulis «Ketik nilai … (DU-nn)» tanpa backtick
  C31 [REVIEW] langkah menyebut verba HTTP dan «endpoint» (PATCH/POST/PUT/DELETE ke endpoint …) yang tidak dinyatakan PRD atau openapi: tulis «permintaan simpan …» kecuali sumbernya ada
  T23 [FINDING] butir Notes yang menyatakan sebuah klausa tidak berlaku/tanpa permukaan dengan prosa bebas, tanpa kalimat baku
      `Tidak berlaku: <aturan> klausa <label> (PRD L<n>)` (butir «Pembagian klausa lintas spec», Temuan PRD, IGAP, dan «Klausa di luar E2E» dikecualikan)
  C25 [FINDING] spek di atas 35 langkah yang alasannya di Notes mengaku sebuah blok memakai keadaan blok lain (ketergantungan antar-blok adalah alasan memecah, konvensi §3);
      [REVIEW] bila sebuah langkah merujuk nomor langkah lain pada spek sepanjang itu
  C26 [REVIEW] spek di atas 50 langkah: bukan batas; spek tetap dibuat, auditor memeriksa apakah blok-bloknya berdiri sendiri dan apakah alasan di Notes benar; C6 menerima butir Notes mana pun yang menyebut ukuran/langkah dan alasannya
  C26/C6 menghitung langkah «Untuk setiap role pada tabel Role yang diuji» sebanyak jumlah role di tabel itu (ekspansi perulangan role)
  C28 [REVIEW] «Tunggu toast … hilang otomatis» sesudah toast Error (toast Error bertahan sampai ditutup manual)
  C27 [REVIEW] asersi «tidak ada yang terhapus/tidak ada entri» sesudah kegagalan yang dipaksa intercept tanpa pass-through: request tidak pernah sampai ke backend, jadi tidak menguji apa pun
  T14 kini juga menangkap butir tanpa judul «Pembagian klausa lintas spec» yang berbunyi «ada di/dilimpahkan ke spec NNN»
  C23 [FINDING] `Verifikasi` «tidak ada toast …» ditulis di antara «Tahan respons» dan «Lepas tahanan»: toast belum mungkin muncul, jadi asersinya lulus tanpa
      menguji apa pun; tulis sesudah respons dilepas dan sesudah `Verifikasi` berkas atau hasilnya (8b.11)
Gaya spec (sama dengan check-suite.py, tidak bergantung TC):
  C4 id frontmatter != nama folder · C5 tanpa `- Mode:` · C6 > 35 langkah tanpa alasan · C9 [REVIEW] absence tanpa
  anchor · C11 butir pertama Prerequisites bukan `- Mode:` · C12 "→ … tampil" di langkah aksi · C13 "Kosongkan
  Search" tanpa aksi · C14 tunggu > 30 detik · C15 rujukan proses di Prerequisites/Notes · C16 "latar tabel"/"hook
  suite" · C17 Spectra.env tanpa Prerequisites · C18 rujukan langkah melewati jumlah langkah · C19 [REVIEW] hitungan
  toast tanpa tunggu toast lama · C20 placeholder generator · C21 [REVIEW] aksi tulis (`[Save]`, `[Submit]`,
  `[Continue]`, `[Delete]`, `[Confirm]`, «Pilih label», «konfirmasi aksi») langsung diikuti langkah yang pindah surface, sesi, atau konteks tanpa
  `Verifikasi` atau «Tunggu aksi selesai» di antaranya (bagian 8b butir 8)

Pemakaian:
    python scripts/check-suite-prd.py specs/HrApp/UserManagement --rules ../prd-harness/work-items/hr-user-management/rules-e2e-prd.json \
        --coverage docs/coverage/HrAppUserManagement.md --data docs/data/HrAppUserManagement.md \
        --tc-backend ../hr-app/user-management/TestCases/tc-user-management-backend.md
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
HARD_LIMIT = 50   # above this a spec is only flagged for the auditor (a lead, not a limit; decision 2026-11-06: specs are still written)
LONG_REASON_RE = re.compile(r"(?i)\b(?:langkah|ukuran|panjang)\b.{0,160}\b(?:klausa|blok|aturan|kelas|alasan|karena|state)\b|\b(?:klausa|blok|aturan|kelas)\b.{0,160}\b(?:langkah|ukuran|panjang)\b|di atas smell")
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
# The three legitimate reasons of conventions §2 (pure server effect, non-deterministic visual, cross-system) plus a state that is gone before it can be
# observed (8b.8). A «Klausa di luar E2E» bullet that names none of them is a data hurdle, a cross-module delegation or a client behaviour: it must be tested.
VALID_REASON = re.compile(
    r"(?i)\b(?:server|backend|back-end|basis data|database|atomik|atomic|idempoten\w*|retry|rollback|cron|scheduler|queue|antrean)\b|\bBE\b|\bTC-[A-Z0-9-]*BE-\d+"
    r"|visual|warna|bayangan|opasitas|animasi|transisi|piksel|non-?deterministik|tidak deterministik"
    r"|lintas sistem|cross-system|sistem eksternal|sistem lain|\bemail masuk\b"
    r"|8b\.8|keadaan sementara|tidak teramati sesudah|hilang sebelum")
HOLD_START = re.compile(r"(?i)\btahan(?:\s+(?:respons|response|request|permintaan))\b")
HOLD_END = re.compile(r"(?i)\blepas(?:kan)?\s+(?:tahanan|respons|response)\b|\blepas\s+(?:yang\s+)?ditahan\b")
ABSENT_TOAST = re.compile(r"(?i)(?:tidak\s+ada|tanpa|belum\s+ada)\s+toast|toast\b[^.\n]{0,50}\btidak\s+(?:tampil|muncul|ada)")
TAB_WALK = re.compile(r"(?i)\bTab\b[^\n.]{0,25}\b(?:hingga|sampai|berulang)\b")
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
        if TAB_WALK.search(l):
            out("REVIEW", "C22", f"{folder}: langkah {num} «{TAB_WALK.search(l).group(0)}» tidak deterministik; tulis jumlah Tab "
                                 "atau langkah atomik «Fokuskan … lewat keyboard»")
    held = None
    for l in lines:  # C23 (8b.11): an absence asserted while the response is still held passes without testing anything
        num = l.split(".", 1)[0]
        if HOLD_START.search(l) and not re.match(r"^\d+\.\s+Verifikasi", l):
            held = num
        elif HOLD_END.search(l) and not re.match(r"^\d+\.\s+Verifikasi", l):
            held = None
        elif held and re.match(r"^\d+\.\s+Verifikasi", l) and ABSENT_TOAST.search(l):
            out("FINDING", "C23", f"{folder}: langkah {num} «tidak ada toast» saat respons masih ditahan (ditahan di langkah {held}); "
                                  "tulis sesudah «Lepas tahanan» dan sesudah Verifikasi berkas atau hasilnya (8b.11)")
    for index, (cur, nxt) in enumerate(zip(lines, lines[1:])):
        in_setup_column = any("setup column" in x.lower() for x in lines[max(0, index - 4):index + 1])   # its [Save] is client-side only (8b.8): the step may not name the modal
        if WRITE_ACTION.match(cur) and not in_setup_column and SURFACE_MOVE.match(nxt):
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
        if re.match(r"^\s*(?:[-*]|\d+\.)\s", line):
            current = [line]
            out.append(current)
        elif current is not None and line.strip() and re.match(r"^\s+\S", line):
            current.append(line)
        else:
            current = None
    return [" ".join(x.strip() for x in block) for block in out]


NOT_OBSERVABLE_RE = re.compile(r"(?i)lintas sistem|sistem lain|milik modul|modul lain|tidak teramati|tidak dapat diamati|tidak bisa dibaca|tidak (?:ada )?kemampuan baca")
READABLE_SURFACES = (("Activity Log", r"activity log"), ("System Log", r"system log"), ("token", r"\btoken\b"), ("counter", r"\bcounter\b"),
                     ("notifikasi", r"notifikasi|notification"), ("saldo atau Reserved", r"saldo|reserved|wallet"))
SUITE_TEXT = ""   # suite.md of the suite under check, set in main()
DATA_TEXT = ""    # the test-data file, set in main()
VERIF_LINE_RE = re.compile(r"(?im)^\d+\.\s*Verifikasi\b.*$")
SPECIAL_DATA_DUTIES = {"Search: karakter khusus", "Input: markup dan payload", "Sel: teks literal"}
SPECIAL_DATA_RE = re.compile(r"(?i)<script|<b>|<img|\.\*|' ?OR ?'|&lt;|onerror")
LITERAL_RE = re.compile(r"`([^`\n]{4,60})`|\"([^\"\n]{4,60})\"|«([^»\n]{4,60})»")
CONDITIONAL_STEP_RE = re.compile(r"(?im)^(\d+)\.\s+(?!Verifikasi)[^\n]*\b(?:bila|jika|kalau|apabila)\b(?![^\n]*\b(?:Verifikasi|tampil)\b)[^\n]*$")


STOP_WORDS = {"yang", "dan", "atau", "pada", "dari", "untuk", "dengan", "the", "and", "for", "tab", "tidak", "baru", "lama"}


class WordSets:
    """A `match` list of a cell duty, matched loosely: one entry is met when every significant word of it occurs in the text (any order);
    «Active/History» is either word. The PRD names a surface «Wallet Balance», the spec «Wallet ... Balance Card»: both are the same assertion."""

    def __init__(self, entries):
        self.sets = []
        for entry in entries:
            words = []
            for token in re.findall(r"[\w/.-]+", entry.lower()):
                alts = [a.strip(".") for a in token.split("/") if len(a.strip(".")) >= 3 and a.strip(".") not in STOP_WORDS]
                if alts:
                    words.append(alts)
            if words:
                self.sets.append(words)

    def search(self, text):
        low = text.lower()
        return any(all(any(a in low for a in alts) for alts in words) for words in self.sets)


def dynamic_key(duty):
    """A key for duties whose label is built from the PRD (`Klausa fungsi: …`): the quoted literals of the duty text, any of which must be asserted.
    None when the text carries no literal (nothing exact to look for; the auditor judges)."""
    label = str(duty.get("duty") or "")
    if not label.startswith("Klausa fungsi:"):
        return None
    lits = [next(g for g in m.groups() if g) for m in LITERAL_RE.finditer(str(duty.get("text") or ""))]
    lits = [x for x in lits if re.search(r"[A-Za-z]", x) and not re.match(r"^[A-Z][A-Z0-9]*[-:]", x)]
    return re.compile("(?i)" + "|".join(re.escape(x) for x in dict.fromkeys(lits))) if lits else None


def conditional_step_check(folder, steps, out):
    """C24 [REVIEW]: an action step that branches on a condition (the run takes one path; the other is never asserted)."""
    hits = [m.group(1) for m in CONDITIONAL_STEP_RE.finditer(steps)]
    if hits:
        out("REVIEW", "C24", f"{folder}: langkah {', '.join(hits[:5])} bersyarat («bila/jika/kalau»); siapkan kondisinya di Prerequisites atau hook dan tulis satu jalur")
ONE_ROW_RE = re.compile(r"(?im)^\d+\.\s*Verifikasi[^\n]*\b(?:sedikitnya|minimal|setidaknya|paling sedikit)\s+(?:satu|1)\s+baris")


def readable_in_suite(pattern):
    """suite.md names a capability to READ this surface (baca / membaca / dibaca / read within 160 characters)."""
    return bool(re.search(r"(?is)(?:baca|membaca|dibaca|read)[^.\n]{0,160}(?:" + pattern + r")|(?:" + pattern + r")[^.\n]{0,160}(?:baca|membaca|dibaca|read)", SUITE_TEXT))


def one_row_check(folder, steps, out):
    """C33 [REVIEW]: «at least one row» with constant values on a permanent audit trail (Transactions, Activity Log, Changelog) is satisfied by a leftover row of an earlier run or spec."""
    hits = [m.group(0) for m in ONE_ROW_RE.finditer(steps) if re.search(r"(?i)log|transaction|transaksi|wallet|changelog|audit", m.group(0))]
    if hits:
        out("REVIEW", "C33", f"{folder}: «{hits[0][:80]}»: pada audit trail permanen baris sisa dari run atau spek lain meloloskan asersi; catat baseline dan asersi selisih atau kunci unik")


LOG_SURFACE_RE = re.compile(r"(?i)\b(?:allocation log|activity log|system log|user log|changelog)\b")
WAIT_RE = re.compile(r"(?i)tunggu|polling|tiap \d+ detik|setiap \d+ detik|sampai\b[^.\n]{0,80}(?:tampil|muncul|ada|bertambah|sama|terbaca|terbit)|hingga\b|ulangi|buka ulang|tutup dan buka|maks(?:imal)?\s+\d+\s+(?:menit|detik)")
STEP_RE = re.compile(r"(?m)^(\d+)\.\s+(.*)$")
RESET_RE = re.compile(r"(?i)hilang|tidak (?:lagi )?tampil|belum tampil|muat ulang|buka (?:halaman|tautan|ulang|kembali)|kosongkan|reload|\bF5\b|navigasi|kembali ke")
WRITE_RE = re.compile(r"(?i)klik\s+`?\[(?:save|submit|simpan|delete|hapus|approve|reject|cancel allocation|confirm|yes|resubmit|reset password|kirim|send)|tunggu aksi selesai|kirim (?:permintaan|request)|permintaan (?:simpan|hapus|langsung)|lewat klien http")
MESSAGE_RE = re.compile(r"(?i)caption|pesan|error|alert|toast|helper text|peringatan")
QUOTE_RE = re.compile(r"`([^`\n]{12,100})`|\"([^\"\n]{12,100})\"|«([^»\n]{12,100})»")


def log_read_checks(folder, steps, out):
    """C34 [REVIEW]: the first Verifikasi of a run on a permanent log needs a wait or polling (log writes are best-effort, PRD L443 pattern)."""
    rows = [(int(m.group(1)), m.group(2)) for m in STEP_RE.finditer(steps)]
    flagged, last_log = [], -99
    for i, (num, text) in enumerate(rows):
        if not re.match(r"(?i)verifikasi", text) or not LOG_SURFACE_RE.search(text) or not re.search(r"(?i)entri|entry|description|baris", text):
            continue   # «menu aksi menampilkan `Allocation Log`» names the menu item, it does not read the log
        near = " ".join(t for _, t in rows[max(0, i - 6): i + 1])
        first_of_run = num - last_log > 3
        last_log = num
        wrote = any(WRITE_RE.search(t) for _, t in rows[max(0, i - 10): i])
        if first_of_run and wrote and not WAIT_RE.search(near):
            flagged.append(num)
    if flagged:
        shown = ", ".join(str(n) for n in flagged[:6]) + (" …" if len(flagged) > 6 else "")
        out("REVIEW", "C34", f"{folder}: langkah {shown} membaca log permanen tanpa tunggu atau polling; tutup dan buka lagi tiap 5 detik sampai entri tampil, baru Verifikasi")


def repeated_assertion_checks(folder, steps, out):
    """C35 [REVIEW]: the same quoted literal asserted in several Verifikasi with no reset step between the occurrences."""
    rows = [(int(m.group(1)), m.group(2)) for m in STEP_RE.finditer(steps)]
    seen = {}
    for i, (num, text) in enumerate(rows):
        if not re.match(r"(?i)verifikasi", text) or not MESSAGE_RE.search(text) or re.search(r"(?i)tidak\s+(?:lagi\s+)?(?:tampil|muncul|ada)|hilang|belum tampil", text):
            continue
        for groups in set(QUOTE_RE.findall(text)):
            lit = next((g for g in groups if g), "")
            if lit and not re.search(r"\{runId\}|DU-\d|[>()]", lit):
                seen.setdefault(lit, []).append(i)
    hits = []
    for lit, idx in seen.items():
        if len(lit.split()) < 3 or lit.startswith("["):
            continue   # buttons and short labels repeat legitimately; a caption or message of a rejected submit does not
        bare = [b for a, b in zip(idx, idx[1:]) if b - a > 1 and not any(RESET_RE.search(t) for _, t in rows[a + 1:b])]
        if len(bare) >= 2:
            hits.append((lit, rows[bare[1]][0]))
    if hits:
        lit, num = hits[0]
        out("REVIEW", "C35", f"{folder}: «{lit[:50]}» diasersi lagi di langkah {num} tanpa langkah pembersih sejak asersi sebelumnya ({len(hits)} kutipan); caption atau nilai blok lama bisa meloloskan asersi ini")


EMAIL_COUNT_RE = re.compile(r"(?i)(?:jumlah|hitung)\s+email|email\s+(?:baru|bertambah|naik)|(?:tepat\s+)?(?:satu|1|dua|2|tiga|3)\s+email\s+(?:baru|masuk|diterima|terkirim|lagi)\b|email[^.\n]{0,60}baseline|kotak[^.\n]{0,60}menerima")
EMAIL_LITERAL_RE = re.compile(r"`[^`]*`|«[^»]*»|\"[^\"]*\"|(?i:email sent!?|resend email)")
NO_EMAIL_RE = re.compile(r"(?i)tidak\s+(?:ada|bertambah|menerima)|tanpa\s+email|tetap")
TOP_ROW_RE = re.compile(r"(?i)(?:baris|entri)\s+(?:\w+\s+)?teratas|baris pertama|paling atas|urutan teratas")
BACKWARD_RE = re.compile(r"(?i)\bmundur|dikurangi|dikurangkan|\bminus\b|geser(?:kan)?\s+(?:jam|waktu)[^.\n]{0,40}(?:lalu|silam)")
LOG_SEARCH_RE = re.compile(r"(?i)\bsearch\b|\bcari\b|\bketik\b")
EMAIL_TOKEN_RE = re.compile(r"[\w.+-]+@[\w.-]+|\bemail\b")
ERROR_TOAST_VERIF_RE = re.compile(r"(?i)^verifikasi[^\n]*\btoast\b[^\n]*(?:error|failed|gagal)")


INTERCEPT_MOCK_RE = re.compile(r"(?i)intercept[^\n]*(?:\b5\d\d\b|5xx|timeout|balas|kembalikan|respons|tahan|menahan|ditahan)")   # «menahan»: t assimilates to n
MOCK_PASS_RE = re.compile(r"(?i)pass-?through|diteruskan|teruskan ke server|hitung-?saja")
INTERCEPT_END_RE = re.compile(r"(?i)(?:lepas|hapus|matikan|reset|akhiri)\s+intercept")
BACKEND_READ_RE = re.compile(r"(?i)fixture|status token|token[^\n]{0,30}(?:active|consumed|invalidated|tetap)|password lama|login dengan|counter|lock|mail-?catcher|kotak (?:email|DU)")


def intercept_state_check(folder, steps, out):
    """C40 [REVIEW] (run 12 audit F-3): a `Verifikasi` that reads backend state (token, password, counter, lock, mailbox) while an intercept that answers by
    itself (5xx, timeout, held response) is active: the request never reached the server, so «state unchanged» cannot fail. Use a real failure (a BE
    fixture, a down provider) or write the clause as server-pure."""
    rows = [(int(m.group(1)), m.group(2)) for m in STEP_RE.finditer(steps)]
    # `pending`: the last request of the flow was answered by a mock; it stays so after «lepas intercept» until a real action reaches the server
    active, pending, hits = False, False, []
    for num, t in rows:
        if INTERCEPT_MOCK_RE.search(t) and not MOCK_PASS_RE.search(t):
            active = pending = True
        elif INTERCEPT_END_RE.search(t):
            active = False
        elif re.match(r"(?i)verifikasi", t):
            if pending and BACKEND_READ_RE.search(t):
                hits.append(num)
        elif not active and re.match(r"(?i)(?:klik|kirim|submit|picu|buka|ketik[^\n]*lalu klik)", t):
            pending = False
    if hits:
        out("REVIEW", "C40", f"{folder}: langkah {', '.join(str(n) for n in hits[:5])} membaca state backend sesudah intercept yang menjawab sendiri (permintaan tidak sampai server): "
                             "«state tidak berubah» tidak bisa gagal; pakai kegagalan nyata (fixture BE, penyedia mati) atau tulis klausanya sebagai efek server murni")


def leads_from_audit_run11(folder, steps, text, out):
    """C36-C39 [REVIEW]: four shapes the run 11 audit found in 61 of 122 reset-password specs; none can be told apart from a correct step by the script alone."""
    rows = [(int(m.group(1)), m.group(2)) for m in STEP_RE.finditer(steps)]
    bad36 = []
    for i, (num, t) in enumerate(rows):
        if re.match(r"(?i)verifikasi", t) and EMAIL_COUNT_RE.search(EMAIL_LITERAL_RE.sub(" ", t)) and not NO_EMAIL_RE.search(t) \
                and not WAIT_RE.search(" ".join(x for _, x in rows[max(0, i - 3): i + 1])):
            bad36.append(num)
    if bad36:
        out("REVIEW", "C36", f"{folder}: langkah {', '.join(str(n) for n in bad36[:6])}{' …' if len(bad36) > 6 else ''} menegaskan jumlah email naik tanpa tunggu atau polling; "
                             "email dikirim best-effort: «Tunggu hingga kotak menerima email baru terhadap baseline (polling 5 detik, batas 2 menit)»")
    if BACKWARD_RE.search(text):
        top = [n for n, t in rows if re.match(r"(?i)verifikasi", t) and TOP_ROW_RE.search(t)]
        if top:
            out("REVIEW", "C37", f"{folder}: jam dimundurkan tetapi langkah {', '.join(str(n) for n in top[:5])} membaca log lewat baris teratas; "
                                 "entri bercap masa lalu tidak di atas, cari lewat Search nama unik")
    bad38 = []
    for i, (num, t) in enumerate(rows):
        near = " ".join(x for _, x in rows[max(0, i - 2): i + 1])
        if re.search(r"(?i)activity log|system log", near) and LOG_SEARCH_RE.search(t) and re.search(r"[\w.+-]+@[\w.-]+", t):
            bad38.append(num)
    if bad38:
        out("REVIEW", "C38", f"{folder}: langkah {', '.join(str(n) for n in bad38[:5])} mencari baris log dengan email; Activity Log Session tidak punya kolom email dan Search mencocokkan nama tampil")
    stacked, last = [], None
    for i, (num, t) in enumerate(rows):
        if ERROR_TOAST_VERIF_RE.match(t) and not re.search(r"(?i)\btidak\b", t):
            between = [x for _, x in rows[last + 1:i]] if last is not None else []
            persistence = re.search(r"(?i)masih tampil|bertahan|tetap tampil", t) or (between and all(re.match(r"(?i)tunggu|verifikasi", x) for x in between))
            if last is not None and not persistence and not any(re.search(r"(?i)tutup|close|dismiss", x) for x in between):
                stacked.append(num)
            last = i
    if stacked:
        out("REVIEW", "C39", f"{folder}: langkah {', '.join(str(n) for n in stacked[:5])} menegaskan toast Error lagi tanpa «Tutup toast» sejak toast sebelumnya; toast Error bertahan, toast lama bisa meloloskan asersi ini")


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
        if cited and not VALID_REASON.search(bullet):
            out("FINDING", "T10", f"{folder}: «Klausa di luar E2E» tanpa salah satu dari tiga alasan sah (efek server murni, visual non-deterministik, "
                                  f"lintas sistem; atau keadaan yang hilang sebelum teramati, 8b.8): hambatan data, akun, volume, modul lain, perilaku klien, "
                                  f"atau delegasi PRD lain harus diuji, bukan dikecualikan («{bullet[:70]}»)")
        hit = HINDRANCE.search(bullet)
        if hit:
            out("REVIEW", "T10", f"{folder}: «Klausa di luar E2E» beralasan «{hit.group(0)}», bukan efek server murni; "
                                 f"periksa bagian 2 dan S-01 («{bullet[:60]}»)")
        if cited and NOT_OBSERVABLE_RE.search(bullet) and SUITE_TEXT:
            for name, pattern in READABLE_SURFACES:
                if re.search(pattern, bullet, re.I) and readable_in_suite(pattern):
                    out("REVIEW", "C32", f"{folder}: «Klausa di luar E2E» beralasan lintas sistem atau tidak teramati untuk {name}, tetapi suite.md mencantumkan kemampuan membacanya; "
                                         f"alasan ini bisa dibantah fixture suite sendiri: uji atau ganti alasan («{bullet[:60]}»)")
                    break


UNASSERTED_RE = re.compile(r"(?i)\bbelum\s+(?:di)?(?:asersi(?:kan)?|uji|ditest|dites|diverifikasi|tercakup|ditulis|dicakup|ada\s+(?:asersi|spe[ck]|verifikasi)|punya\s+(?:asersi|spe[ck]|verifikasi))"
                           r"|\b(?:tidak|tanpa)\s+(?:di)?asersi|\bkebutuhan terbuka|\btidak (?:diuji|dites|diverifikasi)\b|\btidak ada (?:asersi|spec)\b")
DELEGATED_RE = re.compile(r"(?i)pembagian klausa lintas spec|\bspe[ck]\s+\d{3}\b|ada di spe[ck]")
IGAP_RE = re.compile(r"(?i)\bIGAP-\d+")


def disposition_ok(bullet, rules, held):
    """A legitimate home for a clause that no step asserts: a valid «Klausa di luar E2E», a rule that is held (or an IGAP id), or a «Temuan PRD» naming the rule
    (the PRD is silent or ambiguous: S-15), or a delegation to another spec; «Tidak berlaku» naming a rule and a PRD reference."""
    if KLAUSA_BULLET.search(bullet) and VALID_REASON.search(bullet):
        return True
    cited = [q for q in rules if re.search(rf"(?<![A-Za-z0-9]){re.escape(q)}(?![A-Za-z0-9])", bullet)]
    if IGAP_RE.search(bullet) or any(q in held for q in cited):
        return True
    if re.search(r"(?i)temuan prd", bullet) and cited:
        return True
    if re.search(r"(?i)tidak berlaku", bullet) and cited and re.search(r"\bL\d+\b|§\s?\d", bullet):
        return True
    if re.search(r"\bS-14\b", bullet) or re.search(r"(?i)\byang diasersi\b", bullet):
        return True
    return bool(DELEGATED_RE.search(bullet))


def unasserted_checks(folder, notes, out, rules=None, held=None):
    """T22: a bullet admitting an unasserted clause must carry a legitimate disposition (a silent gap is a finding, not a note)."""
    for bullet in bullets(notes):
        if UNASSERTED_RE.search(bullet) and not disposition_ok(bullet, rules or {}, held or {}):
            out("FINDING", "T22", f"{folder}: butir mengakui klausa yang tidak diasersi tanpa disposisi sah (Klausa di luar E2E dengan alasan sah, aturan yang Ditahan atau "
                                  f"IGAP, Temuan PRD yang menyebut aturannya, atau tulis Verifikasi-nya): «{bullet[:80]}»")


ROLE_LOOP_RE = re.compile(r"(?i)\bUntuk\s+(?:setiap|tiap|masing-masing)\s+role\b|\bper\s+role\b")


def role_table_rows(text):
    """Number of roles in the «Role yang diuji» table of Prerequisites (0 when the spec has none)."""
    i = text.find("Role yang diuji")
    if i < 0:
        return 0
    rows = 0
    for line in text[i:].split(chr(10))[1:]:
        if line.startswith("|"):
            rows += 1
        elif rows and not line.strip().startswith("|"):
            break
    return max(rows - 2, 0)   # minus header and separator


def expanded_steps(n, steps, text):
    """A step «Untuk setiap role pada tabel …» runs once per role: it counts R times toward the length limits (run 7: Position 007, 008 and 009 were 32-34 nominal
    steps and about 50-65 when run, and the nominal count let them pass C6/C26)."""
    roles = role_table_rows(text)
    loops = sum(1 for m in re.finditer(r"^\d+\. .*$", steps, re.M) if ROLE_LOOP_RE.search(m.group(0)))
    return n + (roles - 1) * loops if roles > 1 and loops else n


ERROR_TOAST_RE = re.compile(r"(?i)toast.{0,30}(?:error|gagal|failed|connection problem)|(?:error|failed|connection problem).{0,60}toast|`Error,")
WAIT_TOAST_GONE_RE = re.compile(r"(?i)tunggu.{0,40}toast.{0,60}(?:hilang|menghilang|tertutup)\s*(?:otomatis)?|toast.{0,60}hilang otomatis")


def error_toast_wait_check(folder, steps, out):
    """C28 [REVIEW]: a Toast Error stays until it is closed by hand (toast-copy, locked rule 12), so «Tunggu toast … hilang otomatis» right after one never finishes
    (run 7: Division 084 and 091). Close it with a step or wait for a success toast instead."""
    lines = [m.group(0) for m in re.finditer(r"^\d+\. .*$", steps, re.M)]
    for i, line in enumerate(lines):
        if re.search(r"(?i)\bbertahan\b|\b(?:tidak|belum)\s+(?:ikut\s+)?(?:hilang|menghilang)", line):
            continue   # the step asserts that the toast STAYS
        if WAIT_TOAST_GONE_RE.search(line) and any(ERROR_TOAST_RE.search(x) for x in lines[max(0, i - 4):i + 1]):
            out("REVIEW", "C28", f"{folder}: «{line[:80]}» sesudah toast Error: toast Error bertahan sampai ditutup manual; tulis «Tutup toast»")


FORCED_FAIL_RE = re.compile(r"(?i)intercept.{0,160}(?:\b5\d\d\b|5xx|timeout|abort|putus)|(?:\b5\d\d\b|5xx|timeout|abort|putus).{0,160}intercept")
NOTHING_DONE_RE = re.compile(r"(?i)tidak ada (?:item|entri|baris|record|perubahan)[^.\n]{0,40}(?:terhapus|bertambah|tercatat|baru|log)|tidak (?:ada yang )?terhapus|selisih nol|jumlah entri (?:tetap|sama)|tidak bertambah")
PASS_THROUGH_RE = re.compile(r"(?i)teruskan|pass-?through|callCount|lepas(?:kan)? (?:tahanan|respons)|tanpa intercept|backend nyata")


def vacuous_absence_check(folder, steps, out):
    """C27 [REVIEW]: after a failure forced by an intercept the request never reached the backend, so «nothing was deleted / no new log entry» passes whatever the
    backend does (run 6: Division 046 and 049). It tests something only when the same block lets the request through (pass-through, call count, release)."""
    lines = [m.group(0) for m in re.finditer(r"^\d+\. .*$", steps, re.M)]
    for i, line in enumerate(lines):
        if not FORCED_FAIL_RE.search(line):
            continue
        window = lines[i + 1:i + 9]
        for j, later in enumerate(window):
            if NOTHING_DONE_RE.search(later) and not any(PASS_THROUGH_RE.search(x) for x in [line] + window[:j + 1]):
                out("REVIEW", "C27", f"{folder}: «{later[:70]}» sesudah kegagalan yang dipaksa intercept ({line[:50]}…): request tidak pernah sampai ke backend, jadi asersi ini lulus apa pun yang dilakukan backend; "
                                      "teruskan request (pass-through) atau tulis klausanya sebagai efek server murni")
                break


STD_NA_RE = re.compile(r"(?i)Tidak berlaku:\s*\S+.{0,200}?klausa\s+\S")
PRD_REF_RE = re.compile(r"\bL\d+\b|§\s?\d")
NA_PROSE_RE = re.compile(r"(?i)tidak berlaku|tidak (?:ada|punya|memiliki) (?:permukaan|objek)|tanpa permukaan|tidak teramati di (?:tabel|form|modal)")


def clause_na_checks(folder, notes, out):
    """T23: a clause with no object on this surface is written as the fixed sentence `Tidak berlaku: <aturan> klausa <label> (PRD L<n>)`; free prose («tidak ada permukaan»,
    «tidak berlaku karena ...») is what T18/T22 cannot validate, so a bullet that says a clause does not apply and omits the sentence is a finding. A rule-level «Tidak berlaku»
    of the coverage page (T11) is a different thing and is not checked here."""
    for bullet in bullets(notes):
        if re.match(r"(?i)\s*(?:[-*]|\d+\.)?\s*Pembagian klausa", bullet):
            continue   # a delegation list names where each clause lives; a clause it calls not applicable is checked at its own spec
        if NA_PROSE_RE.search(bullet) and re.search(r"(?i)klausa", bullet) and not (STD_NA_RE.search(bullet) and PRD_REF_RE.search(bullet)) \
                and not KLAUSA_BULLET.search(bullet) and not re.search(r"(?i)temuan prd|\bIGAP-\d+", bullet):
            out("FINDING", "T23", f"{folder}: klausa yang tidak berlaku ditulis sebagai prosa; pakai kalimat baku «Tidak berlaku: <aturan> klausa <label> (PRD L<n>)»: «{bullet[:80]}»")


DEPENDENT_REASON_RE = re.compile(r"(?i)bergantung|saling (?:memakai|mengandalkan|menggunakan)|memakai (?:ulang|hasil|keadaan|seleksi|user|record|data)\b|dibangun (?:oleh )?(?:langkah|blok)|masih terbuka dari|mengandalkan (?:flag|hasil|state|keadaan)|melanjutkan (?:dari )?blok|hasil blok (?:sebelum|awal)")
INDEPENDENT_RE = re.compile(r"(?i)tidak (?:saling )?(?:bergantung|memakai|mengandalkan|menggunakan)|tidak ada (?:blok |langkah )?(?:yang )?(?:bergantung|memakai|mengandalkan|menggunakan)|tanpa (?:saling )?ketergantungan|berdiri sendiri")
STEP_BACKREF_RE = re.compile(r"(?im)^\d+\..*\blangkah\s+\d+\b")


def long_spec_checks(folder, n, steps, notes, out):
    """C25: a spec above the step limit must be long for a reason that is not block dependency (a dependency between blocks is the reason to split, not to extend; measured on run 5:
    nine of the long specs on two modules claimed independence or admitted dependence). [FINDING] when the Notes reason for the length admits that a block uses the state of an earlier
    block; [REVIEW] when a step of a long spec points back to an earlier step number."""
    if n <= LIMIT:
        return
    for bullet in bullets(notes):
        if re.search(r"(?i)35|langkah|blok", bullet) and DEPENDENT_REASON_RE.search(bullet) and not INDEPENDENT_RE.search(bullet):
            out("FINDING", "C25", f"{folder}: {n} langkah dan alasannya mengaku blok bergantung pada blok lain; pecah di batas ketergantungan (tiap blok menyiapkan state-nya sendiri): «{bullet[:90]}»")
            break
    back = STEP_BACKREF_RE.findall(steps)
    if back:
        out("REVIEW", "C25", f"{folder}: {n} langkah dan {len(back)} langkah merujuk nomor langkah lain (mis. «{back[0][:70]}»); pastikan blok tidak memakai state blok sebelumnya")


BAR_DIRECT_RE = re.compile(r"(?im)^\d+\.\s*(?:Klik|Tekan|Pilih)\s+(?:tombol\s+)?[`\[]*(?:Delete|Hapus)[`\]]*\s+(?:pada|di|dari)\s+(?:Bulk Action Bar|bar aksi massal|bar bulk|bar)\b")
BAR_OVERLAY_RE = re.compile(r"(?im)^\d+\.\s*(?:Klik|Buka)\s+(?:tombol\s+)?[`\[]*Bulk Action[`\]]*")


def bulk_pattern_check(specs_text, out):
    """C29: the Bulk Action Bar is ONE `Bulk Action` button whose overlay lists the actions (prd-conventions §8); a step that clicks `[Delete]` straight on the bar follows the
    obsolete pattern, whether or not another spec uses the overlay. A PRD that still says `[Delete]` on the bar is a «Temuan PRD», not the pattern to test."""
    direct = sorted(f for f, t in specs_text.items() if BAR_DIRECT_RE.search(t))
    overlay = sorted(f for f, t in specs_text.items() if BAR_OVERLAY_RE.search(t))
    if direct:
        out("FINDING", "C29", f"{len(direct)} spec mengklik `[Delete]` langsung di Bulk Action Bar (mis. {direct[0].split('-E2E-')[-1][:3]})"
                              + (f" sementara {len(overlay)} spec memakai tombol `Bulk Action` + overlay" if overlay else "")
                              + "; foundation (prd-conventions §8) memakai satu tombol `Bulk Action`, pakai pola itu di semua spec dan catat teks PRD yang usang sebagai Temuan PRD")


DU_TYPED_RE = re.compile(r"(?im)^\d+\.\s*(?:Ketik|Isi(?:kan)?|Masukkan|Tulis|Type|Input)\b[^\n]{0,60}?`DU-\d+[a-z]?`")
HTTP_VERB_RE = re.compile(r"(?im)^\d+\.[^\n]{0,80}\b(?:PATCH|PUT|POST|DELETE)\b\s+(?:ke|to)\s+(?:the\s+)?(?:endpoint|API|server)\b")


def writer_guard_checks(specs_text, out):
    """C30/C31 (Brand audit 2026-11-07, F-13/F-14): a data-row id typed as text would never trigger the rule under test; an HTTP verb and endpoint that no PRD or openapi states is invented."""
    typed = sorted((f, DU_TYPED_RE.search(t).group(0)) for f, t in specs_text.items() if DU_TYPED_RE.search(t))
    if typed:
        out("FINDING", "C30", f"{len(typed)} spec mengetik id data sebagai teks (mis. {typed[0][0].split('-E2E-')[-1][:3]}: «{typed[0][1][:80]}»); tulis «Ketik nilai … (DU-nn)» tanpa backtick atau rujuk nilai di file data")
    verbs = sorted((f, HTTP_VERB_RE.search(t).group(0)) for f, t in specs_text.items() if HTTP_VERB_RE.search(t))
    if verbs:
        out("REVIEW", "C31", f"{len(verbs)} spec menyebut verba HTTP dan endpoint (mis. {verbs[0][0].split('-E2E-')[-1][:3]}: «{verbs[0][1][-70:]}»); pastikan PRD atau openapi menyatakannya, bila tidak tulis «permintaan simpan …»")


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


HEAD_RE = re.compile(r"(?m)^### (.+?)\s*$")
DELEG = re.compile(r"(?i)pembagian klausa lintas spec")
# a Notes bullet that moves a clause to another spec without the heading words is the same delegation (run 6: Position 076 said «ada di spec 064 yang mengutip …» and 064 did not)
# run 8 Position: «diasersi oleh aturan FI masing-masing ... di spec 033 dan 043» was a delegation the destination did not honour and the narrow form above did not match it
DELEG_ALT = re.compile(r"(?i)\b(?:ada|dilimpahkan|dibagi|dipindah\w*|ditempatkan|diasersi|dicakup|diuji|dites|ditegaskan|diverifikasi)\s+(?:di|ke|oleh)\s+(?:[^.;\n]{0,90}?\s)?(?:di\s+)?spe[ck]\s+\d{3}")
DELEG_TOKEN = re.compile(r"`([^`]+)`|\bspec\s+(\d{3}(?:\s*(?:,|dan|serta|atau)\s*\d{3})*)", re.I)


def heading_rule(heading, known):
    """The rule id a `### <ID>: <title>` heading starts with (the longest known id), or None."""
    best = None
    for rid in known:
        if heading == rid or heading[len(rid):len(rid) + 1] in (":", " ") and heading.startswith(rid):
            if best is None or len(rid) > len(best):
                best = rid
    return best


def heading_checks(folder, steps, ids, rules, out):
    """T12/T13 (R-25): one `### <rule>` subheading per sourceRules id, none naming a rule outside sourceRules."""
    known = set(rules) | set(ids)
    count = {}
    for m in HEAD_RE.finditer(steps):
        rid = heading_rule(m.group(1), known)
        if rid is None:
            continue
        count[rid] = count.get(rid, 0) + 1
        if rid not in ids:
            out("FINDING", "T13", f"{folder}: subjudul «### {rid}» menyebut aturan yang tidak ada di sourceRules spec ini")
    for rid in dict.fromkeys(ids):
        if count.get(rid, 0) == 0:
            out("FINDING", "T12", f"{folder}: sourceRules {rid} tanpa subjudul «### {rid}: …» di Test Steps")
        elif count[rid] > 1:
            out("FINDING", "T13", f"{folder}: subjudul «### {rid}» muncul {count[rid]} kali; satu aturan satu subjudul")


T25_DU = re.compile(r"\bDU-\d{2,3}\b")
T25_LIT = re.compile(r"`([^`\n]{4,80})`")


def carried_tokens(segment, rules):
    """The data ids and quoted literals a delegation bullet names for one target: what the target must show for the clause to be there at all."""
    tokens = list(dict.fromkeys(T25_DU.findall(segment)))
    for m in T25_LIT.finditer(segment):
        tok = m.group(1).strip()
        if (len(tok) > 40 or len(tok.split()) > 3 or (len(tok.split()) < 2 and not T25_DU.fullmatch(tok)) or tok.endswith(".md") or re.search(r"[,;()→]", tok) or not (tok[0].isalnum() or tok[0] == "[")
                or tok in rules or tok.endswith("/*") or "{" in tok or tok.startswith(("/", "spec ", "PRD", "DU-")) or not re.search(r"[A-Za-z]", tok)
                or re.match(r"^[A-Z][A-Z0-9]+[:/-]", tok) or re.match(r"^[A-Z]{1,6}-\d+[a-z]?$", tok) or any(r.startswith(tok) for r in rules)):
            continue
        tokens.append(tok)
    return tokens


def label_check(folder, num, segment, current, rules, target_text, seen, out):
    """T27 [REVIEW] (run 12 audit F-2): a delegation bullet that names a duty label of the delegated rule («Rate limit per IP ([F-AUTHRST-06]): Submit»)
    needs that clause in the TARGET's steps; T14 only checks that the target cites the rule, and a target that merely points on again (139 → 144) passed."""
    steps = re.split(r"(?m)^## Notes", target_text)[0].lower()
    low = re.sub(r"\s+", " ", segment).lower()
    for rid in sorted(current):
        for duty in (rules.get(rid) or {}).get("duties") or []:
            label = str(duty.get("duty") or "")
            if not label.startswith("Klausa fungsi:"):        # generic family labels (Mutasi:, Penolakan:, …) are never quoted word by word in steps
                continue
            core = label[len("Klausa fungsi:"):].strip()
            if len(core) < 10 or re.sub(r"\s+", " ", core).lower() not in low or (num, core) in seen:
                continue
            seen.add((num, core))
            words = [w for w in re.findall(r"[a-z]{4,}", re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", core).lower()) if w not in STOP_WORDS]
            if words and sum(1 for w in words if w in steps) < 0.6 * len(words):
                out("REVIEW", "T27", f"{folder}: klausa «{core[:70]}» dilimpahkan ke spec {num}, tetapi langkah spec {num} tidak memuatnya "
                                     "(hanya aturannya yang dikutip, atau klausanya dilimpahkan lagi); tunjuk spek yang benar-benar mengasersinya")


def delegation_checks(delegations, spec_rules, rules, out, spec_full=None):
    """T14 (R-29): a delegated clause must land in a spec that cites one of the rules named right before the `spec NNN` reference.
    T25 (REVIEW): the data ids and quoted literals named in that segment must occur in the destination spec, else only the vehicle rule is there."""
    spec_full = spec_full or {}
    for folder, notes in delegations:
        seen = set()
        for bullet in bullets(notes):
            if not (DELEG.search(bullet) or DELEG_ALT.search(bullet)):
                continue
            if not DELEG.search(bullet) and re.search(r"(?i)dikutip hanya di spe[ck] ini", bullet):
                continue   # the heading-less form says the rule is cited ONLY here: the other spec holds a different rule
            current, after_spec, last_full, seg_start = set(), False, None, 0
            for m in DELEG_TOKEN.finditer(bullet):
                if m.group(1) is not None:
                    tok = m.group(1)
                    if tok in rules:
                        named, last_full = {tok}, tok
                    elif tok.endswith("/*"):
                        named = {r for r in rules if r.startswith(tok[:-1])}
                    elif tok.startswith("/") and last_full and (last_full.rsplit("/", 1)[0] + tok) in rules:
                        named = {last_full.rsplit("/", 1)[0] + tok}      # shorthand `/role` after `…/name`
                    else:
                        continue
                    if after_spec:
                        current, after_spec = set(), False
                    current |= named
                    continue
                after_spec = True
                segment, seg_start = bullet[seg_start:m.start()], m.end()
                for num in re.findall(r"\d{3}", m.group(2)):
                    if num in spec_full and (num, "T25") not in seen:
                        seen.add((num, "T25"))
                        target = re.sub(r"\s+", " ", spec_full[num]).lower()
                        missing = [t for t in carried_tokens(segment, rules) if re.sub(r"\s+", " ", t).lower() not in target]
                        if missing:
                            out("REVIEW", "T25", f"{folder}: pelimpahan ke spec {num} menyebut {', '.join(missing[:3])}, tetapi spec {num} tidak memuatnya; aturan penghubung ada di sana, klausanya mungkin belum")
                    if num in spec_full and current:
                        label_check(folder, num, segment, current, rules, spec_full[num], seen, out)
                    if not current and (num, None) not in seen:
                        seen.add((num, None))
                        out("REVIEW", "T24", f"{folder}: pelimpahan ke spec {num} tanpa ID aturan sebelum rujukan; tidak bisa diperiksa, tulis ID aturan dalam backtick sebelum «spec {num}»")
                    if not current or (num, frozenset(current)) in seen:
                        continue
                    seen.add((num, frozenset(current)))
                    if num not in spec_rules:
                        out("FINDING", "T14", f"{folder}: «Pembagian klausa lintas spec» menyebut spec {num} yang tidak ada di suite")
                    elif not (current & spec_rules[num]):
                        names = ", ".join(sorted(current)[:3]) + (" …" if len(current) > 3 else "")
                        out("FINDING", "T14", f"{folder}: klausa {names} dilimpahkan ke spec {num}, tetapi spec itu tidak mengutip aturan itu")


SURFACE_PAIR = re.compile(r"\b(?:di|pada)\s+((?:[A-Z][\w-]*)(?:\s[A-Z][\w-]*)*)\s+(?:dan|serta)\s+((?:[A-Z][\w-]*)(?:\s[A-Z][\w-]*)*)")
VALUE_RE = re.compile(r"\b(\d+)\s*(jam|hari|menit|detik|karakter|baris|kali|px|MB|KB)\b")
EXCLUSIVE_RE = re.compile(r"(?i)(?<!tidak )\b(?:hanya|selain|kecuali)\b")
DUTY_KEYS = {"Sort": re.compile(r"(?i)sort|urut|naik|turun(?!an)|ascending|descending|terbaru|terlama|newest|oldest|a-z|z-a"),
             "Search": re.compile(r"(?i)search|cari|ketik"),
             "Filter": re.compile(r"(?i)filter"), "Hover": re.compile(r"(?i)hover|tooltip|arahkan"),
             "Klik": re.compile(r"(?i)klik|tautan|\blink\b"), "Nilai kosong": re.compile(r"(?i)kosong|tidak pernah"),
             "Hidden default": re.compile(r"(?i)hidden|tersembunyi|disembunyikan|tidak (?:tampil|terlihat)|tidak muncul (?:sebagai|di) (?:kolom|tabel|header)|belum dicentang|tidak dicentang|dicentang"),
             # Klausa widget tabel (testcase-conventions P5 5b..5r), turunan `table_clauses` pada kewajiban tabel. Satu pola per label.
             "Search: reveal": re.compile(r"(?i)fokus|melebar|reveal|auto-?focus"),
             "Search: ✕ dan Enter kosong": re.compile(r"(?i)✕|\(x\)|hapus teks|clear text|enter.{0,40}kosong|kosong.{0,40}enter"),
             "Search: ←": re.compile(r"(?i)←|panah kembali|collapse|menutup kotak|kotak.{0,30}menutup"),
             "Search: trim spasi": re.compile(r"(?i)spasi|trim"),
             "Search: karakter khusus": re.compile(r"(?i)script|markup|\.\*|karakter (?:khusus|pola)|tanda kutip|injeksi|wildcard"),
             "Search: kata kunci multi-kolom": re.compile(r"(?i)beberapa kolom|multi-?kolom|dua kolom|kolom berbeda|kolom lain"),
             "Search: kolom disembunyikan": re.compile(r"(?i)disembunyikan|di-?hide|tersembunyi"),
             "Search: kolom non-searchable": re.compile(r"(?i)non-?searchable|tidak (?:dapat|bisa|ikut) dicari|tidak searchable|tidak ditemukan"),
             "Filter: opsi dari data tabel": re.compile(r"(?i)distinct|opsi.{0,80}(?:data|isi|baris|riwayat)|tanpa (?:muat ulang|reload)"),
             "Filter: OR dalam field": re.compile(r"(?i)\bOR\b|salah satu|dua opsi|gabungan"),
             "Filter: search dalam dropdown": re.compile(r"(?i)(?:dalam|di dalam) dropdown|kotak search|mempersempit opsi"),
             "Filter: chip": re.compile(r"(?i)chip"),
             "Filter: hapus chip": re.compile(r"(?i)chip.{0,80}(?:✕|\(x\)|hapus|menghapus|hilang)|(?:✕|\(x\)).{0,40}chip"),
             "Filter: uncheck opsi": re.compile(r"(?i)uncheck|hapus centang|menghapus centang|menghilangkan centang|tidak dicentang"),
             "Filter: overflow chip": re.compile(r"(?i)\+\s?\d*\s?more|\+N|overflow|ringkasan|gulir|scroll"),
             "Filter: tutup tanpa Apply": re.compile(r"(?i)tanpa apply|draft|dibuang|membuang"),
             "Filter: indikator aktif": re.compile(r"(?i)indikator|badge titik|titik"),
             "Filter: nilai kosong": re.compile(r"(?i)nilai kosong|baris kosong|sel kosong|tanpa nilai"),
             "Filter: format tanggal": re.compile(r"(?i)format tanggal|date format|dd/mm|dd mmm|yyyy|zona waktu|timezone"),
             "Filter: loading dan sumber kosong": re.compile(r"(?i)no options available|skeleton|spinner|loading|sumber kosong|tanpa data"),
             "Filter: kolom disembunyikan": re.compile(r"(?i)disembunyikan|di-?hide|tersembunyi"),
             "Sort: kosong dan tie-break": re.compile(r"(?i)tie-?break|nilai sama|bernilai sama|kosong|—.{0,30}(?:akhir|awal|bawah|atas)"),
             "Sort: huruf besar kecil": re.compile(r"(?i)huruf besar|kapital|case-?insensitive|tidak membedakan|natural|urut(?:an)? angka|collation"),
             "Sort: kolom non-sortable": re.compile(r"(?i)non-?sortable|tanpa ikon (?:sort|urut)|tidak (?:punya|ada|memiliki) ikon (?:sort|urut)|tidak sortable"),
             "Setup Column: screening popup": re.compile(r"(?i)drag handle|ikon pin|reset to default|subtitle|pratinjau|preview"),
             "Setup Column: screening overlay": re.compile(r"(?i)setup column\.\.\.|daftar kolom|drag handle|tanpa ikon (?:sort|urut)"),
             "Setup Column: simpan dan F5": re.compile(r"(?i)F5|refresh|muat ulang|reload|memuat ulang"),
             "Setup Column: kolom terakhir": re.compile(r"(?i)at least one|setidaknya satu|kolom terakhir|satu kolom"),
             "Setup Column: batal": re.compile(r"(?i)esc|✕|\(x\)|dibuang|membuang|batal"),
             "Setup Column: Column Visibility": re.compile(r"(?i)column visibility|panel cepat|overlay|tanpa save"),
             "Setup Column: batas pin": re.compile(r"(?i)pin ke-?4|ke-?empat|keempat|empat kolom|4 kolom|batas (?:tiga|3) kolom|maksimal (?:tiga|3)"),
             "Pagination: halaman tidak valid": re.compile(r"(?i)tidak valid|melebihi|diabaikan"),
             "Pagination: navigasi dan ukuran halaman": re.compile(r"(?i)\bnext\b|\bprev\b|halaman (?:berikut|sebelum)|tombol (?:berikut|sebelum)|(?:me)?lompat|loncat|ukuran 50|ukuran 100|page size 50|page size 100|(?:pilih|ubah) 50|(?:pilih|ubah) 100"),
             "Pagination: page size dan sort": re.compile(r"(?i)page size|ukuran halaman|halaman 1"),
             "Pagination: hapus baris terakhir": re.compile(r"(?i)(?:hapus|delete|menghapus).{0,80}(?:baris|halaman) terakhir|(?:baris|halaman) terakhir.{0,80}(?:hapus|delete)|(?:hapus|delete).{0,60}satu-satunya baris"),
             "Download: cakupan baris": re.compile(r"(?i)seluruh (?:data|baris)|semua baris|hanya baris|bukan hanya halaman|jumlah baris"),
             "Download: urutan dan isolasi": re.compile(r"(?i)urutan (?:baris|kolom)|mengikuti sort|format tanggal|entitas lain|client lain|isolasi"),
             # Round 4 (convention-only themes from the cross-module TC survey)
             "Halaman: breadcrumb dan route": re.compile(r"(?i)breadcrumb|route|url|segmen"),
             "State: kosong": re.compile(r"(?i)ilustrasi|belum ada|empty state|state kosong|tanpa cta"),
             "State: kosong tersaring": re.compile(r"(?i)no results found|tidak cocok|tersaring|tanpa hasil"),
             "State: error muat": re.compile(r"(?i)unable to load|try again|gagal memuat|error muat"),
             "Tampilan: format General Settings dan bahasa": re.compile(r"(?i)general settings|format tanggal|date format|time format|zona waktu|bahasa|timezone"),
             "Filter: referensi basi": re.compile(r"(?i)basi|stale|sudah dihapus|dihapus.{0,100}(?:opsi|filter|kriteria)|(?:opsi|filter|kriteria).{0,100}dihapus"),
             "Bulk: Selection Limit": re.compile(r"(?i)selection limit|maximum selection|only the first|batas seleksi|limit baris"),
             "Form: reload dan pindah menu": re.compile(r"(?i)reload|\bf5\b|pindah menu|beforeunload|konfirmasi (?:bawaan )?browser|tutup tab|leave site"),
             "Log: snapshot dan tidak nyasar": re.compile(r"(?i)snapshot|nilai (?:lama|saat itu)|record lain|tidak nyasar|entri ganda|tidak ganda"),
             "Input: injeksi DOM": re.compile(r"(?i)injeksi|\bdom\b|bypass|fallback|ditolak (?:oleh )?server|diblok (?:oleh )?server"),
             "Input: markup dan payload": re.compile(r"(?i)<script|<b>|markup|payload|\bsql\b|' or |tampil sebagai teks|teks literal"),
             "Form: aksesibilitas field": re.compile(r"(?i)aria|focus trap|nama aksesibel|urutan tab|fokus keyboard"),
             "Akses langsung: capability dicabut": re.compile(r"(?i)dicabut|revoke|di tengah sesi|akses dihapus"),
             "Akses langsung: capability tunggal": re.compile(r"(?i)hanya (?:punya )?(?:create|update|delete)|capability tunggal|(?:create|update|delete)[- ](?:saja|only)|satu capability"),
             "Plan: identik lintas tier": re.compile(r"(?i)starter|growth|professional|enterprise|lintas tier|semua tier|tier plan"),
             "Edge: sudah selesai (D7)": re.compile(r"(?i)sudah (?:dihapus|selesai|terhapus)|idempoten|idempotent|diulang|dua kali|state final"),
             "Edge: kuantitas (D9)": re.compile(r"(?i)terakhir|satu-satunya|nol baris|0 baris|banyak baris|sebagian|di-skip|tidak eligible"),
             "Edge: nasib dependen (D14)": re.compile(r"(?i)dependen|turunan|child|pending|in-flight|parent|induk|yatim|snapshot"),
             # Round 5 (audit of run 5: double-click and Edit/Delete side effects, third sort click)
             "Sort: tiga klik": re.compile(r"(?i)klik ke-?3|ketiga|tiga klik|kembali ke (?:urutan )?default|indikator.{0,40}hilang"),
             "Form: klik ganda": re.compile(r"(?i)klik ganda|double.?click|dua kali (?:klik|cepat)|\bdblclick\b|klik dua kali"),
             "Edit: efek simpan": re.compile(r"(?i)tetap terbuka|tidak berubah|bertahan|setelah f5|tanpa toast|field lain"),
             "Bulk: klik ganda Confirm": re.compile(r"(?i)klik ganda|double.?click|dua kali (?:klik|cepat)|\bdblclick\b|klik dua kali"),
             "Delete: klik ganda": re.compile(r"(?i)klik ganda|double.?click|dua kali (?:klik|cepat)|\bdblclick\b|klik dua kali"),
             "Delete: gagal 5xx dan timeout": re.compile(r"(?i)5xx|timeout|500|gagal|connection problem|failed to delete"),
             "Delete: cek ulang saat konfirmasi": re.compile(r"(?i)cek ulang|in-use|sudah dihapus|no longer available|berubah menjadi|antara dialog"),
             "Delete: dialog aksesibel": re.compile(r"(?i)esc|focus trap|fokus (?:terjebak|kembali)|nama aksesibel|aria"),
             # Duties added by the 2026-11-06 per-table and parity commit (17ff961): every label needs a pattern, or T18 skips it silently
             "Akses: URL langsung": re.compile(r"(?i)\burl\b|alamat langsung|tautan langsung|ditolak|redirect|403"),
             "Akses: endpoint langsung": re.compile(r"(?i)endpoint|request langsung|api langsung|\b403\b"),
             "Bahasa: Verbatim dan Translatable": re.compile(r"(?i)verbatim|translatable|terjemah|bahasa|language"),
             "Download: filter dan sort pada berkas": re.compile(r"(?i)(?:filter|saring).{0,120}(?:berkas|csv|xlsx|file)|(?:berkas|csv|xlsx|file).{0,120}(?:filter|sort|urut)"),
             "Download: format dan zona": re.compile(r"(?i)format|zona|time ?zone|\butc\b|tengah malam"),
             "Download: isolasi dan peran": re.compile(r"(?i)isolasi|entitas lain|client b|entitas b|read only|peran"),
             "Download: urutan dan format isi": re.compile(r"(?i)urutan|header|nol baris|0 baris|tanpa toast|nama lengkap"),
             "Download: urutan kolom pada berkas": re.compile(r"(?i)urutan kolom|digeser|geser|header.{0,60}urutan"),
             "Filter: anatomi panel": re.compile(r"(?i)placeholder|\[clear field\]|\[apply\]|ikon filter|urutan field|field filter"),
             "Filter: keyboard": re.compile(r"(?i)keyboard|\btab\b|\benter\b|spasi|panah|\besc\b"),
             "Filter: loading, sumber kosong, tanpa kecocokan": re.compile(r"(?i)skeleton|spinner|no options available|no results found|sumber kosong|loading"),
             "Filter: teks field tanggal": re.compile(r"(?i)format tanggal|date format|teks tanggal|tanggal terpilih"),
             "Guided: anatomi": re.compile(r"(?i)tooltip|judul|deskripsi|step \d|langkah \d|indikator|\bof \d"),
             "Guided: navigasi dan tutup": re.compile(r"(?i)\bnext\b|\bback\b|\bskip\b|\bdone\b|\besc\b|panah|tutup|selesai"),
             "Guided: pemicu": re.compile(r"(?i)\[\?\]|tombol bantuan|pemicu|ikon bantuan|\bhelp\b|pertama kali|flag"),
             "Guided: satu halaman": re.compile(r"(?i)satu halaman|halaman lain|pindah halaman|hanya di halaman"),
             "Search: cakupan kolom": re.compile(r"(?i)cakupan|semua kolom|union|digabung|kolom (?:ikon|badge|enum|status)|accessibility label"),
             "Search: hanya spasi": re.compile(r"(?i)hanya spasi|spasi saja|spasi"),
             "Sel: teks literal": re.compile(r"(?i)literal|<script|<b>|markup|payload|bukan html|tidak dieksekusi"),
             "Setup Column: Reset melepas pin": re.compile(r"(?i)reset.{0,80}(?:pin|beku)|(?:pin|beku).{0,80}reset|melepas pin"),
             "Setup Column: anatomi modal": re.compile(r"(?i)judul|deskripsi|subtitle|✕|drag handle|checkbox|\[cancel\]|tanpa cancel|footer"),
             "Setup Column: ikon Pin disabled": re.compile(r"(?i)disabled|pin.{0,60}(?:aktif lagi|unpin)|ikon pin"),
             "Setup Column: kolom bertipe khusus": re.compile(r"(?i)tipe|tanggal|enum|badge|kolom (?:pertama|terakhir)|bernilai kosong|sembunyi"),
             "Setup Column: panel Column Visibility": re.compile(r"(?i)column visibility|panel|setup column\.\.\.|overlay"),
             "Setup Column: preview dan Reset": re.compile(r"(?i)preview|pratinjau|reset to default|belum tersimpan|\breset\b"),
             "Setup Column: preview reorder": re.compile(r"(?i)preview|pratinjau|reorder|geser|seret|urutan"),
             "Setup Column: urutan kolom beku": re.compile(r"(?i)urutan.{0,60}(?:beku|pin)|(?:beku|pin).{0,60}urutan|kolom beku"),
             "Sort: alfabetis": re.compile(r"(?i)huruf besar|kecil|\bcase\b|\bicu\b|collation|alfabetis|a-z"),
             "Sort: kolom bertipe khusus": re.compile(r"(?i)tanggal|angka|enum|badge|kosong|\bsort\b|urut"),
             "State list: Back dan F5": re.compile(r"(?i)\bback\b|\bf5\b|refresh|muat ulang|breadcrumb|bertahan"),
             "State list: reset": re.compile(r"(?i)klik ulang|\bmenu\b|default|tab baru|\breset\b"),
             "State list: sub-tab": re.compile(r"(?i)sub-?tab|\btab\b"),
             "Toolbar: ikon Download": re.compile(r"(?i)tooltip|download|hover"),
             "Toolbar: ikon Filter": re.compile(r"(?i)tooltip|filter|hover"),
             "Tampilan: markup literal": re.compile(r"(?i)<script|<b>|markup|literal|tidak dirender|tampil sebagai teks"),
             "Tooltip: Skip dan overlay": re.compile(r"(?i)skip|overlay"),
             "Tooltip: Back dan Next": re.compile(r"(?i)back|next|done"),
             "Tooltip: replay": re.compile(r"(?i)replay|ulang|\[\?\]|tombol \?"),
             "Tooltip: keluar tanpa selesai": re.compile(r"(?i)resize|ukuran viewport|pindah halaman|tanpa selesai|tidak menyimpan"),
             "Tooltip: keyboard": re.compile(r"(?i)enter|panah|esc|keyboard"),
             "Akses langsung: URL": re.compile(r"(?i)you don't have permission|tidak punya izin|url|tempel|alamat langsung|tanpa redirect"),
             "Akses langsung: endpoint": re.compile(r"(?i)403|endpoint|request langsung|ditolak server"),
             "Download: kolom tersembunyi": re.compile(r"(?i)disembunyikan|di-?hide|tersembunyi|tidak ikut"),
             "Download: umpan balik": re.compile(r"(?i)toast|failed to download|gagal"),
             "Download: nama dan isi berkas": re.compile(r"(?i)\.csv|\.xlsx|nama berkas|ekstensi|header"),
             "Kombinasi: empat kontrol": re.compile(r"(?i)bersamaan|sekaligus|irisan"),
             "Kombinasi: alur Search dan Filter": re.compile(r"(?i)irisan|search lalu filter|filter lalu search"),
             "Kombinasi: lepas satu kontrol": re.compile(r"(?i)clear filter|kosongkan search|mengosongkan|ganti kolom sort|tetap aktif|tetap (?:berlaku|menyaring)"),
             "Kombinasi: pulih dari kosong": re.compile(r"(?i)pulih|memulihkan|no results found"),
             # Klausa aksi bulk (prd-conventions §8)
             "Bulk: checkbox header": re.compile(r"(?i)checkbox header|indeterminate|header.{0,40}checkbox|centang semua baris halaman"),
             "Bulk: bar dan counter": re.compile(r"(?i)\d+ \w+ selected|selected|counter|bulk action"),
             "Bulk: Select All lintas halaman": re.compile(r"(?i)select all|unselect all|lintas halaman"),
             "Bulk: seleksi bertahan": re.compile(r"(?i)bertahan|tetap (?:tercentang|terpilih|dicentang)|tidak (?:ter-?reset|direset|hilang)"),
             "Bulk: bentuk tunggal dan jamak": re.compile(r"(?i)tunggal|jamak|single|satu baris|1 baris|\bin-?use\b|dipakai"),
             "Bulk: sebagian atau semua tidak bisa diproses": re.compile(r"(?i)di-?skip|dilewati|some items|sebagian|diblokir|blokir|semua tidak"),
             "Bulk: setelah aksi selesai": re.compile(r"(?i)bar (?:hilang|tertutup|tidak tampil)|seleksi (?:menjadi|jadi|kembali) 0|seleksi (?:ter-?reset|dikosongkan|bersih)|tidak ada (?:bar|seleksi)"),
             "Bulk: Cancel dialog": re.compile(r"(?i)cancel|batal|ditutup tanpa"),
             "Bulk: gagal 5xx dan timeout": re.compile(r"(?i)5xx|timeout|500|gagal|connection problem"),
             "Bulk: aksi dua arah": re.compile(r"(?i)activate|deactivate|dua arah|disembunyikan|tidak tampil"),
             "Kombinasi: mutasi saat terfilter": re.compile(r"(?i)(?:create|edit|ubah|tambah|buat).{0,140}(?:tidak muncul|menghilang|hilang|tidak tampil)|(?:tidak muncul|menghilang|hilang|tidak tampil).{0,140}(?:create|edit|ubah|tambah|buat)"),
             # Klausa form Create/Edit (P2 2a..2h, P3 3b-3, P8 8a..8c, P9 9a), turunan `form_clauses`
             "Form: kondisi bersih": re.compile(r"(?i)kosong|tanpa perubahan|bersih|tidak muncul|langsung tertutup"),
             "Form: klik backdrop": re.compile(r"(?i)backdrop|di luar modal|area luar|klik luar"),
             "Form: Clear Field": re.compile(r"(?i)clear field"),
             "Form: status Saving": re.compile(r"(?i)saving|loading|disabled|dinonaktifkan|tombol.{0,30}(?:nonaktif|dikunci)"),
             "Form: gagal 5xx dan timeout": re.compile(r"(?i)5xx|timeout|500|gagal|try again"),
             "Search: fokus setelah ✕": re.compile(r"(?is)(?=.*✕)(?=.*(?:fokus|focus))"),
             "Setup Column: seret lalu batal": re.compile(r"(?is)(?=.*(?:seret|drag))(?=.*(?:esc\b|✕|batal|tutup))(?=.*(?:urutan|buang|tetap))"),
             "Bulk: uncheck header": re.compile(r"(?is)(?=.*header)(?=.*(?:uncheck|hapus centang|batalkan centang|tercentang lagi|dikosongkan|bar hilang|kembali nol))"),
             "Form: Esc pada dialog Unsaved Changes": re.compile(r"(?i)\besc\b[^\n]{0,120}unsaved|unsaved[^\n]{0,120}\besc\b"),   # one step: Esc ON the dialog, not Esc on the form plus a dialog somewhere
             "Setup Column: bertahan lintas logout": re.compile(r"(?i)logout|keluar akun|login (?:lagi|kembali)|masuk (?:lagi|kembali)|cache browser|localstorage"),
             "Download: di atas 5.000 baris": re.compile(r"(?i)5\.?000|loading screen|lebih dari 5"),
             "Form: Leave lewat menu": re.compile(r"(?is)(?=.*leave)(?=.*(?:menu|sidebar|halaman tujuan|berpindah|pindah))"),
             "Form: fokus setelah Clear Field": re.compile(r"(?is)(?=.*clear field)(?=.*(?:fokus|focus))"),
             "Setup Column: independen antar tabel": re.compile(r"(?is)(?=.*(?:tabel lain|tabel yang lain|antar-?tabel|tidak memengaruhi|tidak ikut berubah))(?=.*(?:setup column|kolom))"),
             # both state duties need a `Verifikasi` LINE that reads the state; a word anywhere in the block (an action step, a heading) does not count
             "Penolakan: state tidak berubah": re.compile(r"(?im)^\d+\.\s*Verifikasi\b(?=[^\n]*(?:tidak berubah|tetap|utuh|masih berlaku|sama seperti|baseline|sama dengan|tidak ada (?:email|token|entri|baris)|tidak bertambah))(?=[^\n]*(?:login|saldo|reserved|baris|nilai|token|counter|jumlah|email|log|password|lock|record|entri|status))"),
             "Batas: sisi lolos": re.compile(r"(?im)^\d+\.\s*Verifikasi\b(?=[^\n]*(?:diterima|lolos|berhasil|tersimpan|tanpa caption|tidak (?:ada|tampil|muncul)[^\n]{0,30}caption|caption[^\n]{0,30}(?:hilang|tidak tampil)|diproses|sukses|email sent))"),
             "Status: pulihkan lalu ulangi": re.compile(r"(?ims)(?=.*(?:aktifkan kembali|diaktifkan kembali|reaktivasi|buka kunci|unlock|pulihkan|kembalikan status|selesaikan aktivasi|ubah status[^\n]{0,40}active|restore))(?=.*^\d+\.\s*Verifikasi\b[^\n]*(?:berhasil|diproses|diterima|sukses|tampil|email sent|tersimpan))"),
             "Mutasi: data backend dan efek samping": re.compile(r"(?im)^\d+\.\s*Verifikasi\b(?=[^\n]*(?:tersimpan|buka ulang|muat ulang|refresh|fixture|login dengan|entri|\blog\b|email|notifikasi|token|counter|saldo|reserved|consumed|invalidated|sesi|session|field|nilai baru|menjadi|bertambah|berkurang|terhapus|dihapus))"),
             "Edge: state tidak berubah sesudah penolakan": re.compile(r"(?is)(?=.*(?:tidak berubah|tetap|utuh|sama seperti|sama dengan baseline|baseline))(?=.*(?:login|saldo|reserved|baris|nilai|token|counter|jumlah))"),
             "Edge: entitas Suspended atau Expired (D1)": re.compile(r"(?is)(?=.*(?:suspended|expired))(?=.*(?:ditolak|toast|tidak dapat|berjalan))"),
             "Delete: batal tanpa efek": re.compile(r"(?is)(?=.*(?:cancel|batal|✕))(?=.*(?:tanpa toast|tidak ada toast|tidak ada entri|tanpa entri|tidak ada log|tidak terhapus|tetap ada))"),
             "Bulk: capability dicabut": re.compile(r"(?is)(?=.*bulk)(?=.*(?:dicabut|permission|izin))"),
             "Bulk: cek referensi gagal": re.compile(r"(?is)(?=.*bulk)(?=.*(?:5xx|timeout|500))(?=.*(?:referensi|in-?use|check references))"),
             "Bulk: entitas Suspended": re.compile(r"(?is)(?=.*bulk)(?=.*(?:suspended|expired))"),
             "Toolbar: tooltip ikon": re.compile(r"(?is)(?=.*tooltip)(?=.*(?:changelog|column visibility|search|filter|download))"),
             "Visibilitas: kontrol header tabel": re.compile(r"(?is)(?=.*(?:column visibility|sort header|header sort|header kolom))(?=.*(?:pagination|paginasi))"),
             "Create: validasi simetris Edit": re.compile(r"(?is)(?=.*create)(?=.*(?:hanya spasi|spasi saja|ter-?trim|dipangkas|beraksen))"),
             "Form: prioritas pesan": re.compile(r"(?is)(?=.*(?:prioritas|pesan pertama|hanya satu pesan|satu pesan))"),
             "Log: tiga permukaan": re.compile(r"(?is)(?=.*system log)(?=.*activity log)"),
             "Toast: sukses hilang sendiri": re.compile(r"(?is)(?=.*(?:sukses|success))(?=.*(?:hilang sendiri|menghilang|hilang otomatis))(?=.*(?:4 detik|empat detik|±4))"),
             "Toast: error bertahan": re.compile(r"(?i)bertahan|masih tampil|tidak hilang|lebih dari 4|setelah 6 detik|tunggu 6 detik"),
             "Input: jalur paste": re.compile(r"(?i)paste|tempel|clipboard"),
             "Edit: validasi simetris Create": re.compile(r"(?i)spasi|trim|tepat di batas|batas karakter|already exists|terlarang|emoji"),
             "Edit: tanpa perubahan": re.compile(r"(?i)no changes|tanpa (?:perubahan|mengubah)|tidak (?:ada )?berubah|netral"),
             "Edit: satu entri log per field": re.compile(r"(?i)per field|tepat satu entri|dua entri|2 entri|tanpa entri|tidak ada entri|tidak ganda"),
             "Konkurensi: edit atau hapus oleh pihak lain": re.compile(r"(?i)no longer|sudah dihapus|dihapus (?:oleh )?(?:admin|pihak)|admin lain|sesi lain"),
             "Konkurensi: dua admin mengedit": re.compile(r"(?i)last-?write|menimpa|dua admin|nilai akhir"),
             "Konkurensi: Create duplikat bersamaan": re.compile(r"(?i)already exists|duplikat")}
NEGATION_RE = re.compile(r"(?i)\b(?:tidak (?:ada|tampil|muncul|menampilkan|terlihat|memuat|memiliki|berubah|dapat)|tanpa|hilang|tersembunyi|tertutup)\b")


def rule_blocks(steps, folder, ids, rules, blocks):
    """Collect, per rule id, the text under its `### <ID>` subheading (all specs that cite it)."""
    known = set(rules) | set(ids)
    parts = re.split(r"(?m)^(?=### )", steps)
    for part in parts:
        m = HEAD_RE.match(part)
        rid = heading_rule(m.group(1), known) if m else None
        if rid:
            blocks.setdefault(rid, []).append((folder, part))


def clause_review_checks(blocks, rules, held, out, notes_all=()):
    """T15/T16/T17 [REVIEW] (R-30, R-31, R-32): clause shapes the spec writers most often leave half asserted.
    Judged on the text under the rule's own `### <ID>` subheadings across every spec that cites it.
    Leads for the auditor, never findings: the script cannot tell a surface or value that is only named from one that is asserted."""
    for rid in sorted(blocks):
        rule = rules.get(rid) or {}
        text = rule.get("text") or ""
        if not text or rid in held:
            continue
        body = "\n".join(b for _, b in blocks[rid])
        specs = ", ".join(sorted({f.split("-E2E-")[-1][:3] for f, _ in blocks[rid]}))
        for m in SURFACE_PAIR.finditer(text):
            for name in m.groups():
                if name not in body:
                    out("REVIEW", "T15", f"{rid}: klausa menyebut permukaan «{name}» tetapi subjudul aturan itu (spec {specs}) tidak memuat «{name}»; "
                                         "satu Verifikasi per permukaan yang disebut")
        for num, unit in dict.fromkeys(VALUE_RE.findall(text)):
            if not re.search(rf"(?<![\d:]){num}(?![\d])", body):
                out("REVIEW", "T16", f"{rid}: nilai «{num} {unit}» di teks aturan tidak muncul di subjudul aturan itu (spec {specs}); "
                                     "nilai dan batas dari contoh aturan diasersi satu per satu")
        if EXCLUSIVE_RE.search(text) and not NEGATION_RE.search(body):
            out("REVIEW", "T17", f"{rid}: klausa «hanya/selain/kecuali» tetapi subjudul aturan itu (spec {specs}) tidak memuat asersi ketiadaan; "
                                 "uji juga sisi pembanding (8b.2)")
        for duty in rule.get("duties") or []:
            label = str(duty.get("duty") or "")
            if label.startswith("Delegasi:"):
                doc, _, section = label[len("Delegasi:"):].strip().partition(" §")
                if doc and not re.search(rf"(?i){re.escape(doc)}|§\s?{re.escape(section)}(?![\d.])", body) and not duty_waived(rid, duty, notes_all):
                    out("REVIEW", "T26", f"{rid}: baris PRD menyerahkan perilaku ke {doc} §{section} tetapi subjudul aturan itu (spec {specs}) tidak menyebutnya; "
                                         f"baca bagian itu dan tegaskan nilainya (sebut «{doc} §{section}»), atau tulis siapa pemiliknya di «Klausa di luar E2E»")
                continue
            literal = dynamic_key(duty)
            given = [m for m in duty.get("match") or [] if isinstance(m, str) and m.strip()]
            key = DUTY_KEYS.get(duty.get("duty")) or literal or (WordSets(given) if given else None)
            if label in SPECIAL_DATA_DUTIES and DATA_TEXT and not SPECIAL_DATA_RE.search(DATA_TEXT):
                out("REVIEW", "T20", f"{rid}: klausa «{label}» butuh nilai markup, payload, atau karakter pola, tetapi file data uji tidak memuat satu pun; tambah baris DU-nya")
            # T19 only for exact literals: a static key mixes action and topic words («Hapus centang …» then «Verifikasi chip … hilang» is a real assertion)
            if literal and literal.search(body) and not any(literal.search(line) for line in VERIF_LINE_RE.findall(body)) and not duty_waived(rid, duty, notes_all):
                out("FINDING", "T19", f"{rid}: klausa «{label}» disebut di subjudul aturan itu (spec {specs}) hanya di langkah aksi atau judul, tanpa `Verifikasi` yang memuatnya; "
                                      "satu Verifikasi per klausa")
                continue
            seen_in = body + "\n" + "\n".join(b for o in duty.get("owners") or [] for _, b in blocks.get(o, []))   # a clause owned by a rule the cell names
            if key and not key.search(seen_in) and not duty_waived(rid, duty, notes_all):
                origin = f"dulu {duty['was']}" if duty.get("was") else f"{duty.get('ref', 'konvensi platform')}: {str(duty.get('text', ''))[:90]}"
                out("FINDING", "T18", f"{rid}: klausa {'baris ' if duty.get('was') else ''}«{duty['duty']}» ({origin}) tidak disebut satu langkah pun di subjudul "
                                      f"aturan itu (spec {specs}); satu Verifikasi per klausa dengan nilai dari sel PRD, atau butir «Klausa di luar E2E» "
                                      "yang menyebut aturan dan klausanya")


def duty_waived(rid, duty, notes_all):
    """A row clause left out on purpose: a Notes bullet «Klausa di luar E2E» that names the row rule and the clause (or its old qid)."""
    label, was = str(duty.get("duty", "")).casefold(), str(duty.get("was") or "")
    for _, notes in notes_all:
        for bullet in bullets(notes):
            if rid in bullet and (label in bullet.casefold() or (was and was in bullet)):
                if KLAUSA_BULLET.search(bullet):
                    return True
                # a clause with no object on this surface: «Tidak berlaku: <rule> klausa <label>» with the PRD line or § that shows it (the clause analogue of T11)
                if re.search(r"(?i)tidak berlaku", bullet) and re.search(r"\bL\d+\b|§\s?\d", bullet):
                    return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description="pemeriksa mekanis suite e2e berbasis PRD")
    ap.add_argument("suite")
    ap.add_argument("--rules", required=True, help="rules-e2e-prd.json dari harness (e2e-prd rules)")
    ap.add_argument("--coverage", help="docs/coverage/<Group><SubModul>.md")
    ap.add_argument("--data", help="docs/data/<Group><SubModul>.md")
    ap.add_argument("--tc-backend", help="tc-<modul>-backend.md (rujukan tabel Di luar E2E)")
    a = ap.parse_args(argv)
    suite = Path(a.suite)
    globals()["SUITE_TEXT"] = read(suite / "suite.md") if (suite / "suite.md").is_file() else ""
    globals()["DATA_TEXT"] = read(a.data) if a.data and Path(a.data).is_file() else ""
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
    spec_rules, delegations, blocks = {}, [], {}
    specs_text, spec_full = {}, {}
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
        num = re.search(r"-E2E-(\d{3})", folder)
        if num:
            spec_rules[num.group(1)] = set(ids)
            spec_full[num.group(1)] = text
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
        n_nominal, n = n, expanded_steps(n, steps, text)
        shown = f"{n_nominal} langkah, {n} setelah ekspansi perulangan role" if n != n_nominal else f"{n} langkah"
        if n > LIMIT and not any(LONG_REASON_RE.search(b) for b in bullets(notes)):
            out("FINDING", "C6", f"{folder}: {shown} (> {LIMIT}) tanpa alasan di Notes (butir yang menyebut langkah/ukuran dan alasannya: jumlah klausa, satu kelas harness, blok menyiapkan state sendiri)")
        if n > HARD_LIMIT:
            out("REVIEW", "C26", f"{folder}: {shown} (> {HARD_LIMIT}): tinjau apakah blok-bloknya berdiri sendiri dan alasan di Notes benar; spek tetap dibuat")
        style_checks(folder, text, out)
        klausa_checks(folder, notes, ids, rules, out)
        unasserted_checks(folder, notes, out, rules, held)
        clause_na_checks(folder, notes, out)
        long_spec_checks(folder, n, steps, notes, out)
        vacuous_absence_check(folder, steps, out)
        error_toast_wait_check(folder, steps, out)
        specs_text[folder] = steps
        one_row_check(folder, steps, out)
        conditional_step_check(folder, steps, out)
        leads_from_audit_run11(folder, steps, text, out)
        intercept_state_check(folder, steps, out)
        log_read_checks(folder, steps, out)
        repeated_assertion_checks(folder, steps, out)
        heading_checks(folder, steps, ids, rules, out)
        rule_blocks(steps, folder, ids, rules, blocks)
        delegations.append((folder, notes))
        used_du = sorted(set(DU_RE.findall(text)))
        if used_du and not (a.data and Path(a.data).is_file()):
            out("FINDING", "T9", f"{folder}: memakai {', '.join(used_du[:5])} tetapi file data uji tidak diberikan/tidak ada")
        else:
            for du in used_du:
                if du not in data_ids:
                    out("FINDING", "T9", f"{folder}: {du} tidak ada di {Path(a.data).name}")

    delegation_checks(delegations, spec_rules, rules, out, spec_full)
    bulk_pattern_check(specs_text, out)
    writer_guard_checks(specs_text, out)
    clause_review_checks(blocks, rules, held, out, delegations)

    outside, ditahan, not_applicable = {}, {}, {}
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
        unasserted_checks("coverage `## Catatan`", section(sections, "Catatan"), out, rules, held)
        for cells in table_rows(section(sections, "Ditahan")):
            rid = first_id(cells[0]) if cells else ""
            if rid:
                ditahan[rid] = cells
                if rid not in rules:
                    out("FINDING", "T2", f"Ditahan: {rid} tidak ada di PRD")
        # T11: an obligation derived from the PRD structure (`obligation: true`) that the PRD itself rules out
        for cells in table_rows(section(sections, "Tidak berlaku")):
            rid = first_id(cells[0]) if cells else ""
            if not rid:
                continue
            not_applicable[rid] = cells
            reason = cells[1].strip() if len(cells) > 1 else ""
            if rid not in rules:
                out("FINDING", "T2", f"Tidak berlaku: {rid} tidak ada di PRD")
            elif not rules[rid].get("obligation"):
                out("FINDING", "T11", f"Tidak berlaku: {rid} aturan PRD, bukan kewajiban turunan; kutip di spec, "
                                      "Di luar E2E, atau Ditahan")
            if not re.search(r"\bL\d+\b|§\s?\d", reason):
                out("FINDING", "T11", f"Tidak berlaku: {rid} tanpa rujukan baris atau § PRD pada alasan")
            if rid in cited:
                out("FINDING", "T11", f"Tidak berlaku: {rid} sekaligus dikutip {', '.join(cited[rid])}")
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
        if rid not in cited and rid not in outside and rid not in ditahan and rid not in not_applicable:
            out("FINDING", "T1", f"{rid} tidak tercakup spec mana pun, tidak di Di luar E2E, tidak di Ditahan"
                                 + (", tidak di Tidak berlaku" if rules[rid].get("obligation") else ""))

    obligations = sum(1 for r in rules.values() if r.get("obligation"))
    print(f"\n{len(specs)} spec, {len(rules)} aturan leaf ({obligations} kewajiban turunan), {len(cited)} tercakup spec, "
          f"{len(outside)} di luar E2E, {len(ditahan)} ditahan, {len(not_applicable)} tidak berlaku, {findings} temuan")
    if per_code:
        order = lambda item: (item[0][0], int(item[0][1:]))
        print("per kode: " + ", ".join(f"{c} {n}" for c, n in sorted(per_code.items(), key=order)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
