---
id: TC-FA-NOTIF-E2E-066-damaged-repaired-missing-found-dan-satu-notifikasi-per-aset
title: "Penerimaan Notifikasi Damaged Repaired dan Missing Found serta Satu Notifikasi per Aset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-255
  - TC-FA-NOTIF-256
  - TC-FA-NOTIF-311
  - TC-FA-NOTIF-312
coverage:
  web: automated
---
# Penerimaan Notifikasi Damaged Repaired dan Missing Found serta Satu Notifikasi per Aset

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Mark as Repaired dan Mark as Found.
- Login akun aktor pertama (Asset Admin (Gedung A), Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141, Laptop - 1 AST-2024-0067, Laptop - 2 AST-2024-0068, Proyektor AST-2024-0150 (Pre-setup #24). Asset Admin Pre-setup #8 adalah PIC aset. Status Damaged dan Missing diatur lewat fixture BE pada langkah penyiapan. Asersi TC-FA-NOTIF-311 dan 312 bersyarat Open Item #6 PRD (menunggu keputusan produk).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Mark as Repaired dan Mark as Found pada aset AST-2024-0141, AST-2024-0067, AST-2024-0068, dan AST-2024-0150 (Pre-setup #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-255: Notifikasi damaged_repaired diterima: Mark as Repaired

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): AST-2024-0141 Damaged dengan PIC aset, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), klik Mark as Repaired pada AST-2024-0141 hingga status tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Asset has been repaired"` dan Body `"Kamera DSLR (AST-2024-0141) has been repaired and is ready for use."` (dari template `"[Asset Name] ([Asset ID]) has been repaired and is ready for use."`)
10. Verifikasi icon `checkbox-circle-line` dengan severity `success` pada item
11. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
12. Klik judul item tersebut (bukan tombol)
13. Verifikasi halaman tujuan `/fams/asset/detail/AST-2024-0141` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-256: Notifikasi missing_found diterima: Mark as Found

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): AST-2024-0067 Missing dengan PIC aset
16. Muat ulang halaman Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Asset Admin (Pre-setup #8, sesi API), klik Mark as Found pada AST-2024-0067 hingga status tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Asset has been found"` dan Body `"Laptop - 1 (AST-2024-0067)"` (dari template `"[Asset Name] ([Asset ID])"`)
25. Verifikasi icon `checkbox-circle-line` dengan severity `success` pada item
26. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
27. Klik judul item tersebut (bukan tombol)
28. Verifikasi halaman tujuan `/fams/asset/detail/AST-2024-0067` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-311: damaged_repaired untuk dua aset mengirim satu notifikasi per aset

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Dua aset Damaged dengan PIC aset sama: Kamera DSLR (AST-2024-0141) dan Proyektor (AST-2024-0150)
31. Muat ulang halaman Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
33. Dari akun Asset Admin (Pre-setup #8, sesi API), Mark as Repaired kedua aset sekaligus hingga status tersimpan
34. Klik Bell icon
35. Verifikasi badge Bell icon Asset Admin bertambah 2 dari baseline langkah 32 (satu notifikasi per aset)
36. Verifikasi item `"Asset has been repaired"` dengan Body `"Kamera DSLR (AST-2024-0141) has been repaired and is ready for use."` tampil sebagai notifikasi terpisah
37. Verifikasi item `"Asset has been repaired"` dengan Body `"Proyektor (AST-2024-0150) has been repaired and is ready for use."` tampil sebagai notifikasi terpisah

### TC-FA-NOTIF-312: missing_found untuk dua aset mengirim satu notifikasi per aset

38. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Dua aset Missing dengan PIC aset sama: Laptop - 1 (AST-2024-0067) dan Laptop - 2 (AST-2024-0068)
39. Muat ulang halaman Fixed Asset > Dashboard
40. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
41. Dari akun Asset Admin (Pre-setup #8, sesi API), Mark as Found kedua aset sekaligus hingga status tersimpan
42. Muat ulang halaman Fixed Asset > Dashboard
43. Klik Bell icon
44. Verifikasi badge Bell icon Asset Admin bertambah 2 dari baseline langkah 40 (satu notifikasi per aset)
45. Verifikasi item `"Asset has been found"` dengan Body `"Laptop - 1 (AST-2024-0067)"` tampil sebagai notifikasi terpisah
46. Verifikasi item `"Asset has been found"` dengan Body `"Laptop - 2 (AST-2024-0068)"` tampil sebagai notifikasi terpisah

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30, 38 (penyiapan kondisi data lewat fixture BE); langkah 2, 17, 32, 40 (pencatatan baseline badge Bell icon (S-12)); langkah 16, 31 dan 39 (muat ulang halaman Fixed Asset > Dashboard sesudah pemulihan seed dan sebelum pencatatan baseline; juga menutup Dropdown Panel blok sebelumnya (S-09, S-14)).
- Bell icon adalah toggle: langkah 16, 31, dan 39 (muat ulang halaman sebelum baseline) serta langkah 42 (muat ulang halaman sesudah pemicu) menutup Dropdown Panel yang masih terbuka dari blok sebelumnya sebelum Bell icon diklik lagi; langkah penghubung tanpa Verifikasi (S-03, S-14).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (46 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Blok TC-FA-NOTIF-311 dan 312: "Hitung item" pada Langkah TC dijadikan Verifikasi selisih badge 2 dari baseline dan dua item terpisah (S-03); TC menulis Expected tanpa angka badge.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-311 dan 312 bersyarat Open Item #6 PRD; asersi ditulis persis TC dan dapat direvisi bila produk memutuskan lain.
  - TC-FA-NOTIF-255 dan 256 menulis login "Asset Admin (PIC aset ...)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8.
