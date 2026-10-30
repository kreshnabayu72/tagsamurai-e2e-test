---
id: TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql
title: "Defense-in-Depth: Emoji Lolos Validasi FE, Delete In-Use Langsung, Markup HTML, dan Payload SQL"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-238
  - TC-GS-UOM-242
  - TC-GS-UOM-243
  - TC-GS-UOM-244
  - TC-GS-UOM-272
coverage:
  web: automated
---

# Defense-in-Depth: Emoji Lolos Validasi FE, Delete In-Use Langsung, Markup HTML, dan Payload SQL

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Pelaku pemicu seeding (hanya lewat sesi API, tanpa login UI): Admin FAMS Client A, `famsAdmin_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.FA_ADMIN_PASSWORD`, untuk membuat Asset Name FAMS yang membuat unit in-use. Email akun ini tidak tertulis di Pre-setup TC Measurement (lihat Temuan untuk QA); fixture disediakan tim FE.
- Environment variable: `GS_TC_PASSWORD`, `FA_ADMIN_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Kemampuan teknis: (a) klien HTTP yang mengirim request Measurement langsung ke server memakai token sesi Total Control yang sedang login, untuk TC-GS-UOM-238, 242, dan 272; (b) membaca state data Measurement lewat fixture BE dengan sesi API aktor Total Control (lihat `suite.md`, bagian Hook suite; disediakan tim FE; endpoint tidak disebut TC) untuk asersi "tetap ada", "tidak dibuat", dan "tidak berubah". Asersi pada langkah request langsung hanya respons server dan state data (bagian 8b butir 1).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - `Terpakai {runId}-070` / `tp`: unit in-use milik spec, di-seed lewat API di hook `before` dan dipakai Asset Name FAMS `Terpakai Item {runId}-070` (pengganti `Box` Pre-setup untuk request Delete yang ditolak; S-06). Nilai field wajib lain Asset Name FAMS (Category, TAG Type) disediakan tim FE lewat fixture `fixtures/measurement.json` (belum ada): kunci `assetName.category` dan `assetName.tagType`.
  - `Gram {runId}-070` / `g`: unit bebas relasi milik spec, di-seed lewat API; target request Edit yang ditolak pada TC-GS-UOM-272 (pengganti Gram Pre-setup; S-06).
  - `Box 📦 {runId}-070` dan `Emoji Test {runId}-070`: nama pada request Create yang ditolak sehingga tidak membuat data.
  - `<b>Bold</b> {runId}-070` / `bd`: dibuat spec lewat UI pada TC-GS-UOM-243 (tag HTML literal).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Terpakai Item {runId}-070`, lalu unit `Terpakai`, `Gram`, `Box 📦`, `Emoji Test`, dan `<b>Bold</b>` bersuffix `{runId}-070` bila ada.
- Tidak ada state global yang diubah.
- TC-GS-UOM-238, 242, 243, 244, 272: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-238: Request Delete unit in-use langsung ke server tetap ditolak guard

1. Kirim request Delete Measurement langsung ke server untuk `Terpakai {runId}-070` memakai sesi aktor
2. Verifikasi server menolak request (respons bukan sukses)
3. Verifikasi `Terpakai {runId}-070` tetap ada pada data Measurement

### TC-GS-UOM-242: Unit Name berisi emoji yang lolos validasi klien tetap ditolak server

4. Kirim request Create Measurement langsung ke server dengan Unit Name `Box 📦 {runId}-070` dan Symbol `bx` memakai sesi aktor
5. Verifikasi server menolak request
6. Verifikasi `Terpakai {runId}-070` ada pada data Measurement (anchor) dan `Box 📦 {runId}-070` tidak dibuat

### TC-GS-UOM-272: Symbol berisi emoji yang lolos validasi klien tetap ditolak server saat Create dan Edit

7. Kirim request Create Measurement langsung ke server dengan Unit Name `Emoji Test {runId}-070` dan Symbol `kg😀` memakai sesi aktor
8. Verifikasi server menolak request Create dengan pesan `Symbol contains invalid characters`
9. Verifikasi `Emoji Test {runId}-070` tidak dibuat
10. Kirim request Edit Measurement langsung ke server untuk `Gram {runId}-070` dengan Symbol `g😀` memakai sesi aktor
11. Verifikasi server menolak request Edit
12. Verifikasi Symbol `Gram {runId}-070` tetap `g`

### TC-GS-UOM-244: Search berisi payload SQL tidak memengaruhi hasil

13. Verifikasi tabel Measurement memuat sedikitnya satu baris
14. Catat jumlah unit Measurement Client A pada data (baseline, lewat fixture BE)
15. Ketik Search `' OR 1=1 --`, tekan Enter
16. Verifikasi empty state `No results found`
17. Verifikasi jumlah unit Measurement Client A pada data sama dengan langkah 14
18. Klik `(←)` pada kotak Search

### TC-GS-UOM-243: Unit Name berisi markup HTML ditampilkan sebagai teks biasa

19. Klik [+ Unit], isi Unit Name `<b>Bold</b> {runId}-070` dan Symbol `bd`, klik [Submit]
20. Tunggu aksi selesai (form tertutup)
21. Ketik Search `{runId}-070`, tekan Enter
22. Verifikasi nama tampil literal `<b>Bold</b> {runId}-070` di tabel
23. Verifikasi tidak ada HTML yang dirender (tidak ada teks tebal dari tag `<b>`) di tabel
24. Klik teks `<b>Bold</b> {runId}-070` untuk membuka Unit Detail
25. Verifikasi nama tampil literal `<b>Bold</b> {runId}-070` di Unit Detail
26. Verifikasi tidak ada HTML yang dirender (tidak ada teks tebal dari tag `<b>`) di Unit Detail
27. Tutup Unit Detail, buka Changelog, ketik Search `{runId}-070`, tekan Enter
28. Verifikasi nama tampil literal `<b>Bold</b> {runId}-070` di Changelog
29. Verifikasi tidak ada HTML yang dirender (tidak ada teks tebal dari tag `<b>`) di Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas defense-in-depth (prinsip 13a) tanpa harness eksternal; TC-GS-UOM-238, 242, dan 272 bertanda server langsung (FE Test `-`, PIC FE `-`) dan tetap berada di spec dengan asersi hanya respons server dan state data (bagian 8b butir 1), sesuai konvensi 3 prinsip 13 kelas a dan preseden `TC-GS-BRAND-E2E-068`. Perilaku FE untuk validasi emoji dan Delete in-use yang sama diasersi di spec jalur form (020, 021, 026) dan spec 029.
- Urutan TC di spec berbeda dari urutan sumber: request langsung (238, 242, 272), lalu Search SQL (244, tanpa membuat data), dan terakhir TC-GS-UOM-243 yang membuat data lewat UI (prinsip 3.3).
- Langkah penghubung: langkah 14 dan 17 (membaca jumlah unit dari data sebagai baseline "data tidak berubah", S-12), langkah 18 (mengosongkan kotak Search sebelum TC berikutnya), langkah 20 (menunggu aksi selesai), langkah 21 dan 27 (Search baris atau entri log milik unit), langkah 24 (membuka Unit Detail) dan langkah 27 (menutup Unit Detail, membuka Changelog).
- Langkah 13 adalah `Verifikasi` pembanding (bagian 8b butir 2): tabel Measurement memuat sedikitnya satu baris sebelum baseline jumlah unit dicatat pada langkah 14; bukan dari Expected TC-GS-UOM-244.
- Langkah 3, 6, dan 12 memakai unit milik spec sebagai pengganti `Box` dan `Gram` Pre-setup yang disebut sumber (S-06). Langkah 6 memuat `Terpakai` sebagai anchor positif bagi absence `Box 📦` (bagian 8b butir 2).
- Langkah 21 dan 27 memakai kata kunci `{runId}-070` (sufiks unik milik spec) karena nama target `<b>Bold</b> {runId}-070` tidak memuat substring `Bold {runId}-070` (ada `</b>` di antaranya); hasil Search memuat juga unit milik spec lain, sehingga langkah 24 menyebut nama unit yang diklik.
- Temuan untuk QA:
  - TC-GS-UOM-238 dan 242 mengharapkan "Ditolak" dan "Server menolak" tanpa kode status atau pesan; spec hanya mengasersi bahwa respons bukan sukses dan state data tidak berubah. TC-GS-UOM-272 menyebut pesan `Symbol contains invalid characters` dan diasersi sesuai TC; pesan untuk request Edit tidak disebut.
  - Mekanisme membaca state data pada TC server langsung tidak disebut TC; disediakan tim FE (S-11, S-13). Akun Admin FAMS untuk seeding unit in-use tidak ada di Pre-setup TC.
  - TC-GS-UOM-244 Expected "data tidak berubah" tidak menyebut cara mengamati; spec membandingkan jumlah unit dari data sebelum dan sesudah Search.
  - TC-GS-UOM-243 memakai nama `<b>Bold</b>` dan Symbol `bd`; tidak ada Post Condition di luar Expected.
