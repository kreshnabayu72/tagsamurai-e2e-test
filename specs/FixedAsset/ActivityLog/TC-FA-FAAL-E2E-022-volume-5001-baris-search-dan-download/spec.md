---
id: TC-FA-FAAL-E2E-022-volume-5001-baris-search-dan-download
title: "Volume 5.000 dan 5.001 Baris: Download Ambang 5.000 serta Browsing dan Search Tanpa Loading Screen"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-69
  - TC-FA-FAAL-182
coverage:
  web: automated
---

# Volume 5.000 dan 5.001 Baris: Download Ambang 5.000 serta Browsing dan Search Tanpa Loading Screen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client volume (Pre-setup #14). Email dan nama env var password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data (kelas e, volume data): client dengan volume tepat 5.000 baris Tab Session dan 5.000 baris Tab User Action, lalu 5.001 baris Tab Session (Pre-setup #14). Seed volume dan penambahan satu baris Tab Session dari 5.000 ke 5.001 disediakan tim FE/BE (langkah 12).
- Kemampuan teknis: penangkap unduhan browser dan parser CSV (butir "Kemampuan teknis tambahan" di `suite.md`).
- Keyword Search `Chrome` (TC-FA-FAAL-69) dipakai pada volume 5.001 baris Tab Session; jumlah baris hasil tidak disebut TC.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-182: Download tepat 5.000 baris langsung terunduh (Tab Session)

1. Klik icon Download di Tab Session
2. Pilih `Download as CSV`
3. Verifikasi tidak ada loading screen pada Tab Session
4. Verifikasi berkas langsung terunduh pada Tab Session
5. Verifikasi berkas memuat 5.000 baris data pada Tab Session

### TC-FA-FAAL-182: Download tepat 5.000 baris langsung terunduh (Tab User Action)

6. Klik tab User Action
7. Klik icon Download di Tab User Action
8. Pilih `Download as CSV`
9. Verifikasi tidak ada loading screen pada Tab User Action
10. Verifikasi berkas langsung terunduh pada Tab User Action
11. Verifikasi berkas memuat 5.000 baris data pada Tab User Action

### Penghubung volume dari 5.000 ke 5.001 baris

12. Tambahkan satu baris log pada Tab Session dan satu baris log pada Tab User Action hingga volume masing-masing tepat 5.001 baris tersimpan

### TC-FA-FAAL-69: Browsing dan Search dengan volume besar tidak memunculkan loading screen

13. Muat ulang halaman Activity Log (F5), buka tab Session
14. Verifikasi tabel dimuat tanpa loading screen pemblokir
15. Verifikasi hanya Loading component biasa yang tampil saat tabel dimuat
16. Catat total Z0 dari teks pagination tab Session
17. Verifikasi teks pagination `Showing 1–10 of Z0 entries` pada tampilan awal
18. Verifikasi Z0 di atas ambang 5.000
19. Ketik Search `Chrome`, tekan Enter
20. Verifikasi tidak ada loading screen pemblokir saat Search
21. Verifikasi Search berjalan normal: hasil Search `Chrome` tampil (sedikitnya satu baris)
22. Klik `Next` untuk pindah ke halaman 2
23. Verifikasi paging berjalan normal: halaman 2 tampil
24. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 12, 13, 16, 24 (menambah volume ke 5.001 baris, memuat ulang halaman, mencatat baseline Z0 sesuai TC-FA-FAAL-69 langkah 1, menutup kotak Search). Langkah 12 memakai kemampuan seed yang disediakan tim FE/BE.
- Urutan menyimpang dari urutan nomor TC (S-10): TC-FA-FAAL-182 (5.000 baris) ditulis lebih dulu karena volume hanya bisa naik dari 5.000 ke 5.001; TC-FA-FAAL-69 berjalan pada 5.001 baris.
- Asersi absence state sementara (bagian 8b butir 11): `Verifikasi` tidak ada loading screen diletakkan segera setelah pemicu (pilih `Download as CSV`), sebelum `Verifikasi` berkas terunduh yang menjadi bukti respons sudah diproses.
- Langkah 13 memuat ulang halaman agar pemuatan tabel pada volume 5.001 baris dapat diamati (TC-FA-FAAL-69 langkah 1); hook `beforeEach` suite sudah membuka halaman sebelum spec berjalan.
- Temuan untuk QA:
  - Pre-setup #14 tidak menyebut client dan akun aktor untuk volume 5.000 dan 5.001 baris. Login aktor mencatat baris Session baru sehingga volume "tepat 5.000" dan "tepat 5.001" bergeser; TC tidak menyatakan apakah volume dihitung sebelum atau sesudah login. Spec mengikuti angka TC dan menyerahkan penyesuaian seed ke tim FE/BE.
  - TC-FA-FAAL-69 butir b ("Search dan paging berjalan normal") tidak terukur dan tidak menyebut jumlah hasil keyword `Chrome`; spec mengasersi bahwa hasil tampil dan halaman 2 tampil.
  - TC-FA-FAAL-182 hanya mengasersi jumlah baris berkas; isi berkas (nilai sel) bukan objek spec ini.
