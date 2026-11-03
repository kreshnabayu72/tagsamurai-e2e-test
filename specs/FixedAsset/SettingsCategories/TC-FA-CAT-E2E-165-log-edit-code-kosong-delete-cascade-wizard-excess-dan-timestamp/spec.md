---
id: TC-FA-CAT-E2E-165-log-edit-code-kosong-delete-cascade-wizard-excess-dan-timestamp
title: "Log pada Tiga Surface: Edit Kosongkan Code, Delete, Delete Cascade Descendant Excess, Marked as Excess dari Wizard, Timestamp Sama, dan Kolom Action Teks Biasa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-463
  - TC-FA-CAT-465
  - TC-FA-CAT-479
  - TC-FA-CAT-480
  - TC-FA-CAT-466
  - TC-FA-CAT-468
coverage:
  web: automated
---

# Log pada Tiga Surface: Edit Kosongkan Code, Delete, Delete Cascade Descendant Excess, Marked as Excess dari Wizard, Timestamp Sama, dan Kolom Action Teks Biasa

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua: Total Control (Pre-setup #1) pada client CatExcess (Pre-setup #31) untuk TC-FA-CAT-466; akun aktor ketiga: Total Control (Pre-setup #1) pada client CatPostT0 (Pre-setup #33) untuk TC-FA-CAT-468; password keduanya dari `Spectra.env.FA_TC_PASSWORD`. Login lewat langkah Ganti akun eksplisit (langkah 33 dan 42). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data milik spec pada CatMain (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`):
  - `Furn Edit {runId}-165` (Code `FE165`, leaf, Total Asset 0): target Edit kosongkan Code (langkah 1). Nama baru `Gen Code Log` literal tanpa suffix karena Code hasil generate diturunkan dari nama (`GCL`); hook `before` menghapus sisa kategori `Gen Code Log` dan hook `after` menghapusnya.
  - `Del Log {runId}-165` (Code `DL165`, leaf, Total Asset 0): target Delete (langkah 10).
  - `Desc Time {runId}-165` (Description kosong, leaf, Total Asset 0): target Edit Description (langkah 18).
- Data Pre-setup #31 (CatExcess, Starter setelah downgrade, 9 kategori): `Spare Parts` (internal) berisi `Old Parts` (Excess) dihapus pada langkah 34 sampai 35. Pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` (S-06, pengecualian 2026-10-30). Efek: Last Updated dan entri Changelog bertambah; suite berjalan serial.
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection; 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy` dengan waktu pembuatan terlama ke terbaru dalam urutan itu): spec menyimpan seleksi Wizard pada langkah 45, sehingga tiga kategori menjadi Excess. Pemulihan lewat fixture backend yang sama, di hook `before` dan `after`.
- Kemampuan teknis: membuka Modal Changelog (filter Category Name atau Action), Detail User aktor > Tab System Log, dan Activity Log serta mencari baris berdasarkan nama kategori; mekanisme pencarian tidak diuraikan TC dan disediakan tim FE/BE tanpa endpoint karangan. Kolom Modified By diasersi berformat `[First Name] [Last Initial]` aktor. Jam server dan jam browser sinkron untuk perbandingan Date (kolom Date berketelitian menit).
- Nama kategori milik spec bersuffix unik sehingga baseline baris log per nama adalah nol (S-12); pengecualian `Gen Code Log` dan kategori Pre-setup memakai baseline yang dicatat (langkah 44).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-463: Log Edit mengosongkan Code mencatat Code lama ke Code hasil generate

1. Klik elipsis (⋯) pada baris `Furn Edit {runId}-165` > `Edit`
2. Kosongkan Code dan ubah Category Name menjadi `Gen Code Log`, lalu klik `[Save]`
3. Buka Modal Changelog dan filter Category Name `Gen Code Log`
4. Verifikasi Changelog memuat baris Edit Field `Category Name` Old Value `Furn Edit {runId}-165` New Value `Gen Code Log`
5. Verifikasi Changelog memuat baris Edit Field `Code` Old Value `FE165` New Value `GCL`
6. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Gen Code Log`
7. Verifikasi System Log aktor memuat kedua baris Edit (Field `Category Name` dan Field `Code`)
8. Buka Activity Log dan cari baris `Gen Code Log`
9. Verifikasi Activity Log memuat kedua baris Edit (Field `Category Name` dan Field `Code`)

### TC-FA-CAT-465: Log Delete pada tiga surface memuat path sebelum dihapus

10. Klik elipsis (⋯) pada baris `Del Log {runId}-165` > `Delete`
11. Klik `[Delete]` pada dialog D-09
12. Buka Modal Changelog dan filter Category Name `Del Log {runId}-165`
13. Verifikasi Changelog menulis tepat satu baris: Action `Delete`, Field `Category Name`, Old Value `Del Log {runId}-165`, New Value `—`, Category Name `Del Log {runId}-165`, Modified By aktor
14. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Del Log {runId}-165`
15. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Del Log {runId}-165`
16. Buka Activity Log dan cari baris `Del Log {runId}-165`
17. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor

### TC-FA-CAT-479: Tiga surface menampilkan baris dengan timestamp transaksi yang sama

18. Klik elipsis (⋯) pada baris `Desc Time {runId}-165` > `Edit`
19. Ubah Description menjadi `Waktu sama {runId}-165`, lalu klik `[Save]`
20. Buka Modal Changelog dan filter Category Name `Desc Time {runId}-165`
21. Catat Date baris Edit Field `Description` pada Changelog
22. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Desc Time {runId}-165`
23. Catat Date baris pada System Log aktor
24. Buka Activity Log dan cari baris `Desc Time {runId}-165`
25. Catat Date baris pada Activity Log
26. Verifikasi ketiga baris memiliki Date yang sama sesuai satu transaksi

### TC-FA-CAT-480: Kolom Action pada tabel log berupa teks biasa, bukan badge

27. Buka Modal Changelog
28. Verifikasi kolom Action di Changelog tampil teks biasa tanpa badge berwarna
29. Tutup Modal Changelog dan buka Detail User aktor > Tab System Log
30. Verifikasi kolom Action di System Log tampil teks biasa tanpa badge berwarna
31. Buka Activity Log
32. Verifikasi kolom Action di Activity Log tampil teks biasa tanpa badge berwarna

### TC-FA-CAT-466: Log Delete cascade, satu baris per node termasuk descendant Excess

33. Ganti akun: logout, login sebagai Total Control pada client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Settings > Categories
34. Klik elipsis (⋯) pada baris `Spare Parts` > `Delete`
35. Klik `[Delete]` pada dialog D-08
36. Buka Modal Changelog dan filter Category Name `Spare Parts`
37. Verifikasi Changelog memuat dua baris Delete: `Spare Parts` dan `Spare Parts › Old Parts` (descendant Excess ikut tercatat)
38. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Spare Parts`
39. Verifikasi System Log aktor memuat kedua baris Delete
40. Buka Activity Log dan cari baris `Spare Parts`
41. Verifikasi Activity Log memuat kedua baris Delete

### TC-FA-CAT-468: Log Marked as Excess dari Wizard, aktor Total Control pada tiga surface

42. Ganti akun: logout, login sebagai Total Control pada client CatPostT0 (Pre-setup #33) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Settings > Categories
43. Klik `[Choose Categories]` pada Alert Category Consolidation
44. Catat baseline jumlah baris Changelog Action `Marked as Excess (Category Consolidation)` untuk `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy`
45. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`, lalu klik `[Save Selection]`
46. Buka Modal Changelog dan filter Action `Marked as Excess (Category Consolidation)`
47. Verifikasi Changelog menulis tepat satu baris baru: Action `Marked as Excess (Category Consolidation)`, Field `Excess`, Old Value `Usable`, New Value `Excess`, Category Name `Zeta Vehicle`, Modified By aktor
48. Verifikasi Changelog menulis satu baris baru serupa untuk `Eta Furniture` dan satu untuk `Theta Heavy` (satu baris per node berubah)
49. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Zeta Vehicle`
50. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Zeta Vehicle`
51. Buka Activity Log dan cari baris `Zeta Vehicle`
52. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor

## Notes

- Spec melewati sekitar 35 langkah (52). Alasan: enam blok TC satu kelas (pencatatan log tiga surface) yang berdiri sendiri; 33 langkah di antaranya adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung terhadap ambang (prinsip 13 bagian 3), sehingga langkah di luar blok itu sekitar 19.
- Langkah penghubung (S-03, S-09, R-16): membuka surface dan mencari entri berdasarkan nama kategori (langkah 3, 6, 8, 12, 14, 16, 20, 22, 24, 27, 29, 31, 36, 38, 40, 46, 49, 51), langkah 21, 23, 25 (mencatat Date), langkah 44 (baseline), langkah 43 (membuka wizard).
- Urutan: blok CatMain (TC-FA-CAT-463, 465, 479, 480) mendahului ganti akun ke CatExcess (TC-FA-CAT-466) lalu CatPostT0 (TC-FA-CAT-468) karena client berbeda (S-10).
- Data milik spec menggantikan `Furniture` dan `Vehicle` Pre-setup #20 yang disebut TC-FA-CAT-463, 465, dan 479 (S-06).
- Langkah 48 memeriksa baris serupa pada Changelog; TC-FA-CAT-468 Expected d tidak menyebut surface dan spec memilih Changelog.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan, termasuk untuk client CatExcess dan CatPostT0.
  - TC-FA-CAT-463 mengosongkan Code sambil mengganti nama menjadi `Office Furniture` (Code `OF`); aturan generate Code dengan nama bersuffix tidak diuraikan TC, sehingga spec memakai nama literal `Gen Code Log` dengan Code `GCL` mengikuti pola inisial pada TC-FA-CAT-169.
  - TC-FA-CAT-480 judulnya menyebut kolom Action dan Status, sedangkan Expected hanya menyebut kolom Action; spec hanya memverifikasi kolom Action.
  - TC-FA-CAT-479 tidak menyebut nilai Description baru; spec memakai `Waktu sama {runId}-165` dan tidak mengasersi nilainya.
  - TC-FA-CAT-468 langkah 1 ("Simpan seleksi Wizard dengan 5 centang") tidak menyebut lima kategori; spec memilih `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear` sehingga `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy` menjadi Excess sesuai Expected.
  - TC-FA-CAT-466 dan TC-FA-CAT-468 memakai Pre-setup #31 dan #33 pada client berbeda dari #20 yang menjadi konteks spec lain; client mengikuti Precondition TC.
