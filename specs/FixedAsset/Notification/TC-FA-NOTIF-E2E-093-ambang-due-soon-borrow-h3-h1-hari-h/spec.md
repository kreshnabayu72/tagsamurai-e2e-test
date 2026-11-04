---
id: TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h
title: "Ambang Due Soon Borrow: H-3, H-1, Hari-H, Date Format, dan Di Luar Ambang"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-324
  - TC-FA-NOTIF-325
  - TC-FA-NOTIF-326
  - TC-FA-NOTIF-350
  - TC-FA-NOTIF-376
coverage:
  web: automated
---

# Ambang Due Soon Borrow: H-3, H-1, Hari-H, Date Format, dan Di Luar Ambang

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: ambang tanggal job menjadi objek uji.
- Akun aktor pertama Borrower (Budi Santoso): Pre-setup #11 (`borrowerBudi_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_BORROWER_PASSWORD`, `Fixture.fixedAssetNotification.borrowerBudi`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (job due soon harian, job overdue harian), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di akhir blok terakhir yang menggeser jam. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 Borrowed pada BRW-2026-0342 (Pre-setup #19 dan #24) dengan Due Date 25/06/26. Status Borrowed dan Due Date disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- State global yang diubah: Date Format General Settings menjadi `M/d/yy` pada TC-FA-NOTIF-350 (nilai awal `dd/MM/yy`, Pre-setup #1); dipulihkan oleh langkah eksplisit di spec ini dan oleh hook `after` sebagai cadangan.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di surface yang sama (item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE; kueri status job selesai lewat fixture BE hanya menandai pemicu selesai, bukan bukti panel memuat item) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job pada transaksi dan aset Pre-setup bersama (BRW-2026-0342, AST-2024-0141) yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_BORROWER_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.
- Tabel "Ambang TC-FA-NOTIF-324, 325, dan 326" (urutan baris = urutan iterasi; Waktu job diatur ke jam server dan jam browser secara absolut):

  | TC | State | Waktu job |
  |---|---|---|
  | TC-FA-NOTIF-324 | AST-2024-0141 Borrowed dengan Due Date 25/06/26 | 22/06/26 (H-3) |
  | TC-FA-NOTIF-325 | AST-2024-0141 Borrowed dengan Due Date 25/06/26 | 24/06/26 (H-1) |
  | TC-FA-NOTIF-326 | AST-2024-0141 Borrowed dengan Due Date 25/06/26 | 25/06/26 (hari-H) |


## Test Steps


### TC-FA-NOTIF-324, 325, dan 326: borrow_due_soon pada ambang H-3, H-1, dan hari-H

1. Untuk setiap baris tabel "Ambang TC-FA-NOTIF-324, 325, dan 326" (langkah 1 sampai 5): pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
2. Atur jam server dan jam browser ke waktu job pada baris itu
3. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
4. Klik Bell icon
5. Verifikasi item ber-Title `Your borrowed asset is due soon` dan Body `Kamera DSLR is due on 25/06/26.` diterima

### TC-FA-NOTIF-350: Body tanggal mengikuti Date Format General Settings

6. Pulihkan seed lewat fixture BE pemulih, atur Date Format General Settings menjadi `M/d/yy` lewat fixture BE penyetel state, siapkan AST-2024-0141 Borrowed dengan Due Date 25/06/26 yang sudah terlewati, lalu muat ulang halaman Fixed Asset > Dashboard
7. Atur jam server dan jam browser ke 26/06/26
8. Jalankan job overdue harian lewat kemampuan job latar hingga selesai
9. Klik Bell icon
10. Verifikasi item notifikasi overdue AST-2024-0141 ber-Body `Kamera DSLR was due on 6/25/26.`
11. Pulihkan Date Format General Settings menjadi `dd/MM/yy` lewat fixture BE penyetel state

### TC-FA-NOTIF-376: borrow_due_soon tidak dikirim di luar ambang

12. Pulihkan seed lewat fixture BE pemulih, siapkan AST-2024-0141 Borrowed dengan Due Date 25/06/26, lalu muat ulang halaman Fixed Asset > Dashboard
13. Catat jumlah badge Bell icon akun aktor sebagai baseline
14. Atur jam server dan jam browser ke 21/06/26 (H-4)
15. Jalankan job due soon harian lewat kemampuan job latar hingga selesai
16. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
17. Tunggu 5 detik tanpa memuat ulang halaman
18. Klik Bell icon
19. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
20. Verifikasi badge Bell icon sama dengan baseline
21. Verifikasi Dropdown Panel tidak memuat item `Your borrowed asset is due soon`
22. Tutup Dropdown Panel
23. Atur jam server dan jam browser ke 23/06/26 (H-2)
24. Jalankan job due soon harian lewat kemampuan job latar hingga selesai
25. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
26. Tunggu 5 detik tanpa memuat ulang halaman
27. Klik Bell icon
28. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
29. Verifikasi badge Bell icon sama dengan baseline
30. Verifikasi Dropdown Panel tidak memuat item `Your borrowed asset is due soon`
31. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- AST-2024-0141 juga dipakai spec lain (Overdue dan lainnya) dengan job, tanggal ambang, dan Title notifikasi berbeda; tiap TC memulihkan seed lewat fixture BE sehingga tidak ada keadaan yang dibawa antar spec.
- Pengulangan (bagian 8b butir 7): langkah 1 sampai 5 diulang untuk tiga baris tabel "Ambang TC-FA-NOTIF-324, 325, dan 326" (41 langkah setelah ekspansi: 31 langkah nominal ditambah 2 x 5 langkah pengulangan). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi, 41 langkah): semua blok satu kelas (ambang tanggal job due soon, kelas d) pada dataset AST-2024-0141 yang sama, tiap TC berdiri sendiri dengan seed dipulihkan, dan 10 dari 41 langkah berasal dari pengulangan tiga baris tabel ambang.
- Langkah penghubung (S-03): langkah 1 (pemulihan seed dan penyiapan state) dan langkah pembuka TC-FA-NOTIF-350 dan 376; langkah pemulihan Date Format setelah asersi TC-FA-NOTIF-350; "Catat jumlah badge Bell icon" (baseline S-12); "Kueri status job" (penanda pemicu selesai; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); langkah 31 (pemulihan jam server dan jam browser ke waktu nyata, S-09 dan R-08).
- Asersi tambahan di luar Expected TC (S-03): pada TC-FA-NOTIF-376 badge sama dengan baseline dilengkapi `Verifikasi` Dropdown Panel tidak memuat item karena Dropdown Panel hanya memuat lima item terbaru; keduanya satu `Verifikasi` per titik amat.
- Pengamatan TC-FA-NOTIF-376 dilakukan setelah tiap job (Expected TC a setelah langkah 2 TC, b setelah langkah 5 TC; langkah 3 TC "Tutup Dropdown Panel" menjadi langkah 22 spec). Klik Bell icon bersifat toggle, sehingga Dropdown Panel ditutup pada langkah 22 sebelum dibuka lagi pada langkah 27; tanpa langkah penutup, klik kedua menutup panel dan asersi absence lulus hampa.
- P-5 butir b: TC-FA-NOTIF-350 (format tanggal General Settings) adalah objek-uji ringan tanpa harness eksternal sendiri di spec harness job; satu-satunya objek-uji ringan di spec ini (batas dua) dan memakai kemampuan job overdue yang sama dengan TC lain di spec.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (item seed pembanding `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 untuk akun aktor dan sudah ada pada surface yang sama) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-FA-NOTIF-324, 325, dan 326 menulis "tanggal penyewa" di precondition dan langkah (tampaknya "tanggal tenant"); spec mengartikannya sebagai tanggal jam server dan jam fixture tenant.
  - TC-FA-NOTIF-350 tidak menyebut tanggal job overdue; spec memakai 26/06/26 (hari pertama setelah Due Date 25/06/26, sesuai TC-FA-NOTIF-329). TC juga tidak menyebut Title item; spec mengidentifikasi item lewat Body.
  - TC-FA-NOTIF-324, 325, dan 326 tidak menyebut langkah memuat ulang atau menunggu; asersi "diterima" mengandalkan badge dan Dropdown Panel setelah job selesai.
  - Post Condition kelima TC kosong (`-`); tidak ada yang diasersi.
