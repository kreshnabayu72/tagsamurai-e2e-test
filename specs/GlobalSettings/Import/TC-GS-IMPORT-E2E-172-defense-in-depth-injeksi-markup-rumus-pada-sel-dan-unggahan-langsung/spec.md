---
id: TC-GS-IMPORT-E2E-172-defense-in-depth-injeksi-markup-rumus-pada-sel-dan-unggahan-langsung
title: "Defense-in-depth: injeksi markup/rumus pada sel dan unggahan langsung yang melanggar penyaringan berkas (422, tanpa berkas sementara, tanpa draft)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-536
  - TC-GS-IMPORT-537
  - TC-GS-IMPORT-547
  - TC-GS-IMPORT-577
  - TC-GS-IMPORT-814
coverage:
  web: automated
---

# Defense-in-depth: injeksi markup/rumus pada sel dan unggahan langsung yang melanggar penyaringan berkas (422, tanpa berkas sementara, tanpa draft)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Import dibagikan ke seluruh admin satu client dan suite mengubah state global; lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama:
  - Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTB_TC_PASSWORD`: aktor pertama (TC-547, 536, 537).
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_TC_PASSWORD`: ganti akun eksplisit (TC-577, 814).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Klien HTTP yang mengirim request unggah langsung ke server (Upload File) dengan token sesi akun aktor pada Import Type tertentu; asersi hanya respons server dan state data (butir 1 bagian 8b).
  - Pendeteksi dialog alert JavaScript pada halaman (TC-536) dan pembaca gaya/DOM sel (teks literal, elemen gambar, ketebalan huruf).
  - Generator berkas besar: `brand-1mb-plus1-direct.csv` (header `Brand Name`, 87380 baris `Brand 00001` sampai `Brand 87380`, dan satu baris terakhir `XXXXX`, tepat 1.048.577 byte, setiap baris diakhiri LF termasuk baris terakhir, tanpa BOM).
  - Skrip fixture reset Client B dan Client C ke tanpa draft pada Sub-Tab Brand dan Measurement (Kontrak Fixture R1).
- Data Dinamis (berkas fixture uji, D-07; milik spec ini; draft dibuang oleh reset sehingga isi berkas literal sesuai Data Uji TC):
  - `brand-markup.csv`: header `Brand Name`; 2 baris `<img src=x onerror=alert(1)>` dan `<b>x</b>` (TC-536).
  - `brand-formula.csv`: header `Brand Name`; 4 baris `=SUM(A1)`, `+1`, `-1`, `@SUM(A1)` (TC-537).
  - `brand-12.csv`: 12 baris Brand (TC-547; upload langsung dua kali).
  - `notes.txt` (format tidak didukung) dan `brand-1mb-plus1-direct.csv` (TC-577).
  - `brand-header-only-direct.csv` (hanya header `Brand Name`), `measurement-semicolon-direct.csv` (header `Unit Name;Symbol`; `Meter;m`, `Liter;L`, `Gram;g`), `brand-bad-encoding-direct.csv` (Windows-1252; `Café Brand` dengan byte `0xE9`, `Nikon`, `Ricoh`), `brand-empty-sheet-direct.xlsx` (sheet pertama kosong; sheet kedua header `Brand Name` dan `Nikon`) (TC-814).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus draft Client B dan Client C, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-547: Upload File langsung dua kali menghasilkan dua pengenal berkas sementara berbeda tanpa draft

1. Reset Client B ke tanpa draft Tab Brand (aksi fixture)
2. Muat ulang halaman Import > Brand
3. Kirim permintaan Upload File langsung ke server dengan token akun Total Control Client B dan berkas `brand-12.csv`
4. Verifikasi permintaan Upload File pertama sukses
5. Kirim permintaan Upload File yang sama sekali lagi
6. Verifikasi permintaan Upload File kedua sukses
7. Verifikasi respons kedua permintaan memuat pengenal berkas sementara yang berbeda
8. Muat ulang halaman Import > Brand
9. Verifikasi Dropzone tampil
10. Verifikasi Unsaved Banner tidak tampil

### TC-GS-IMPORT-536: Isi sel berisi markup tidak dieksekusi saat dirender di Staging Table

11. Reset Client B ke tanpa draft Tab Brand (aksi fixture)
12. Muat ulang halaman Import > Brand
13. Klik `[Upload File]` di Dropzone dan pilih berkas `brand-markup.csv`
14. Klik `[Confirm Mapping]`
15. Verifikasi Staging Table menampilkan 2 baris
16. Verifikasi tidak ada dialog alert JavaScript yang muncul
17. Verifikasi sel Brand Name Row # 1 menampilkan teks persis `<img src=x onerror=alert(1)>`
18. Verifikasi sel Brand Name Row # 2 menampilkan teks persis `<b>x</b>`
19. Verifikasi tidak ada gambar yang dirender pada sel Row # 1
20. Verifikasi teks `x` pada sel Row # 2 tidak tampil tebal

### TC-GS-IMPORT-537: Nilai sel berawalan = + - @ diperlakukan sebagai teks

21. Reset Client B ke tanpa draft Tab Brand (aksi fixture)
22. Muat ulang halaman Import > Brand
23. Klik `[Upload File]` di Dropzone dan pilih berkas `brand-formula.csv`
24. Klik `[Confirm Mapping]`
25. Verifikasi keempat baris berstatus `pending`
26. Verifikasi tidak ada Error Banner
27. Verifikasi sel Brand Name menampilkan teks literal `=SUM(A1)`, `+1`, `-1`, dan `@SUM(A1)` (tidak dihitung sebagai rumus)

### TC-GS-IMPORT-577: Unggahan langsung yang melanggar penyaringan berkas ditolak 422

28. Ganti akun: logout, lalu login sebagai Total Control Client C (Rudi Hartanto)
29. Reset Client C ke tanpa draft Tab Brand (aksi fixture)
30. Buka Global Settings > Import, pilih Sub-Tab Brand
31. Kirim permintaan unggah langsung ke server dengan token akun Total Control Client C dan berkas `notes.txt` (format tidak didukung)
32. Verifikasi server menolak permintaan dengan 422
33. Kirim permintaan unggah langsung ke server dengan token akun Total Control Client C dan berkas CSV `brand-1mb-plus1-direct.csv` berukuran 1.048.577 byte
34. Verifikasi server menolak permintaan dengan 422
35. Muat ulang halaman Import > Brand
36. Verifikasi Dropzone tampil
37. Verifikasi Unsaved Banner tidak tampil

### TC-GS-IMPORT-814: Unggahan langsung berkas yang melanggar penyaringan ditolak 422 tanpa draft

38. Reset Client C ke tanpa draft Tab Brand dan Tab Measurement (aksi fixture)
39. Kirim permintaan unggah langsung ke server dengan token akun Total Control Client C pada Import Type Brand dan berkas `brand-header-only-direct.csv`
40. Verifikasi server menolak permintaan dengan 422
41. Kirim permintaan unggah langsung ke server dengan token akun Total Control Client C pada Import Type Measurement dan berkas `measurement-semicolon-direct.csv`
42. Verifikasi server menolak permintaan dengan 422
43. Kirim permintaan unggah langsung ke server dengan token akun Total Control Client C pada Import Type Brand dan berkas `brand-bad-encoding-direct.csv`
44. Verifikasi server menolak permintaan dengan 422
45. Kirim permintaan unggah langsung ke server dengan token akun Total Control Client C pada Import Type Brand dan berkas `brand-empty-sheet-direct.xlsx`
46. Verifikasi server menolak permintaan dengan 422
47. Muat ulang halaman Import > Brand
48. Verifikasi Dropzone tampil
49. Verifikasi Unsaved Banner tidak tampil (tidak ada draft Brand)
50. Buka Global Settings > Import, pilih Sub-Tab Measurement
51. Verifikasi Dropzone tampil
52. Verifikasi Unsaved Banner tidak tampil (tidak ada draft Measurement)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (a); objek uji adalah penolakan server atas unggahan langsung dan perenderan aman isi sel. Tanpa harness eksternal.
- Alasan melewati sekitar 35 langkah (52 langkah nominal): lima blok homogen satu kelas dan berdiri sendiri dengan reset Client B atau Client C di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Bagian sesudah ganti akun (langkah 28, Client C) tetap bermakna walau bagian sebelumnya gagal. Blok TC-547 diletakkan lebih dulu karena tidak menciptakan draft; blok TC-536 dan TC-537 menciptakan draft sehingga masing-masing mereset Client B.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan akun, bukan nomor TC.
- Langkah penghubung (tanpa `Verifikasi`): reset (langkah 1, 11, 21, 29, 38), pembukaan halaman dan Sub-Tab, muat ulang halaman (langkah 2, 12, 22), dan ganti akun (langkah 28). Asersi absence Unsaved Banner dan draft (langkah 10, 37, 49, 52) didahului Verifikasi Dropzone tampil sebagai anchor positif pada halaman yang sama; langkah 16 (tidak ada alert) didahului langkah 15 (Staging Table tampil) dan diasersi segera setelah perenderan (butir 5 bagian 8b).
- Pembagian TC lintas spec: penyaringan berkas lewat UI ada di spec 021 (kelas fungsional); spec ini memuat penolakan lewat unggahan langsung ke server.
- Temuan untuk QA:
  - TC-GS-IMPORT-577 menyebut berkas `brand-1mb-plus1-direct.csv` 87380 baris dengan baris terakhir `XXXXX` agar tepat 1.048.577 byte; spec mengandalkan generator berkas besar tim FE. Nama TC menyebut "melanggar penyaringan berkas" tanpa membedakan batas ukuran dan format; spec mengasersi 422 tiap permintaan tanpa copy UI.
  - TC-GS-IMPORT-536 dan TC-GS-IMPORT-537 mengunggah lewat UI (bukan request langsung) walau berada di section defense-in-depth; spec mengikuti Langkah TC.
  - TC-GS-IMPORT-547 mengasersi dua pengenal berkas sementara berbeda dari respons; nama field respons tidak disebut dan dibaca oleh klien HTTP tim FE.
  - Post Condition TC-GS-IMPORT-536, 537, 547, 577 "-" dan TC-GS-IMPORT-814 ("tidak ada draft Brand dan Measurement pada Client C") dikonfirmasi oleh Expected e dan f; tidak diasersi tambahan.
