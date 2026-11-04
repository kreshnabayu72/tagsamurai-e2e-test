---
id: TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian
title: "Overdue Borrow: Job Harian, Pengulangan Harian, Berhenti saat Return, dan Tidak Dikirim"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-329
  - TC-FA-NOTIF-330
  - TC-FA-NOTIF-331
  - TC-FA-NOTIF-332
  - TC-FA-NOTIF-375
coverage:
  web: automated
---

# Overdue Borrow: Job Harian, Pengulangan Harian, Berhenti saat Return, dan Tidak Dikirim

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: batas hari job overdue menjadi objek uji.
- Akun aktor pertama Borrower (Budi Santoso): Pre-setup #11 (`borrowerBudi_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_BORROWER_PASSWORD`, `Fixture.fixedAssetNotification.borrowerBudi`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Kemampuan menjalankan job latar (job overdue harian), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta sebelum bagian spec yang tidak memerlukannya. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 Borrowed pada BRW-2026-0342 (Pre-setup #19 dan #24) dengan Due Date 25/06/26. Pengaturan pengingat overdue, Return aset, dan notifikasi overdue yang sudah terkirim disiapkan fixture BE penyetel state sumber sebelum tiap TC; pengaturan yang di-OFF dipulihkan fixture BE pemulih. Return aset dikerjakan sesi API Asset Admin (Pre-setup #8; aktor Return tidak disebut TC).
- Waktu job "pukul 00:00" memakai zona waktu tenant Asia/Jakarta.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) untuk baseline dan pembacaan sesudah pemicu (sumber baca yang sama); badge Bell icon dibandingkan terhadap badge baseline.
- Format tanggal pada Body notifikasi mengikuti Date Format General Settings `dd/MM/yy` (nilai awal, Pre-setup #1).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A, butir (i) dan (ii)): spec ini memicu job overdue dan Return aset pada AST-2024-0141 di BRW-2026-0342 (Pre-setup #19 dan #24) serta membaca notifikasi seed Pre-setup #17 milik akun aktor; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar TC, dan suite berjalan serial.
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di surface yang sama (item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE; kueri status job selesai lewat fixture BE hanya menandai pemicu selesai, bukan bukti panel memuat item) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_BORROWER_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.
- Tabel "Kasus tidak dikirim TC-FA-NOTIF-332 dan 375" (urutan baris = urutan iterasi; Waktu job diatur ke jam server dan jam browser secara absolut):

  | TC | State | Waktu job |
  |---|---|---|
  | TC-FA-NOTIF-332 | Pengaturan pengingat overdue OFF (`enable_overdue_reminder`); AST-2024-0141 melewati Due Date 25/06/26 | 26/06/26 pukul 00:00 |
  | TC-FA-NOTIF-375 | AST-2024-0141 Borrowed dengan Due Date 25/06/26; pengingat overdue aktif | 25/06/26 pukul 00:00 |


## Test Steps


### TC-FA-NOTIF-329: borrow_overdue dikirim hari pertama setelah Due Date

1. Pulihkan seed lewat fixture BE pemulih, siapkan AST-2024-0141 Borrowed dengan Due Date 25/06/26 dan pengingat overdue aktif, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline
3. Atur jam server dan jam browser ke 26/06/26 pukul 00:00
4. Jalankan job overdue lewat kemampuan job latar hingga selesai
5. Klik Bell icon
6. Verifikasi badge Bell icon bertambah 1 terhadap baseline
7. Verifikasi item ber-Title `Your borrowed asset is overdue` dan Body `Kamera DSLR was due on 25/06/26.` tampil

### TC-FA-NOTIF-330: borrow_overdue berulang tiap hari dan paling banyak satu per aset per hari

8. Pulihkan seed lewat fixture BE pemulih, siapkan AST-2024-0141 Borrowed dengan Due Date 25/06/26, pengingat overdue aktif, dan belum ada notifikasi overdue untuk aset itu, lalu muat ulang halaman Fixed Asset > Dashboard
9. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `Your borrowed asset is overdue` untuk AST-2024-0141 milik akun aktor sebagai jumlah awal
10. Atur jam server dan jam browser ke 26/06/26
11. Jalankan job overdue lewat kemampuan job latar hingga selesai
12. Jalankan job overdue sekali lagi pada tanggal yang sama hingga selesai
13. Atur jam server dan jam browser ke 27/06/26
14. Jalankan job overdue lewat kemampuan job latar hingga selesai
15. Klik Bell icon
16. Verifikasi badge Bell icon bertambah 2 terhadap baseline
17. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Your borrowed asset is overdue` untuk AST-2024-0141 milik akun aktor sama dengan jumlah awal langkah 9 + 2 (satu untuk 26/06/26 dan satu untuk 27/06/26)

### TC-FA-NOTIF-331: borrow_overdue berhenti saat aset dikembalikan

18. Pulihkan seed lewat fixture BE pemulih, siapkan AST-2024-0141 Borrowed dengan Due Date 25/06/26 yang sudah menerima notifikasi overdue 26/06/26, lalu muat ulang halaman Fixed Asset > Dashboard
19. Atur jam server dan jam browser ke 27/06/26
20. Return aset AST-2024-0141 lewat sesi API Asset Admin hingga tersimpan
21. Catat nilai badge Bell icon akun aktor dan, lewat fixture BE, jumlah item ber-Title `Your borrowed asset is overdue` untuk AST-2024-0141 milik akun aktor sebagai baseline
22. Atur jam server dan jam browser ke 28/06/26
23. Jalankan job overdue lewat kemampuan job latar hingga selesai
24. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai)
25. Tunggu 5 detik tanpa memuat ulang halaman
26. Klik Bell icon
27. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
28. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
29. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Your borrowed asset is overdue` untuk AST-2024-0141 milik akun aktor sama dengan baseline langkah 21 (tidak ada notifikasi overdue baru)

### TC-FA-NOTIF-332 dan TC-FA-NOTIF-375: borrow_overdue tidak dikirim

30. Untuk setiap baris tabel "Kasus tidak dikirim TC-FA-NOTIF-332 dan 375" (langkah 30 sampai 39): pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
31. Atur jam server dan jam browser ke waktu job pada baris itu
32. Catat jumlah badge Bell icon akun aktor sebagai baseline
33. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
34. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai)
35. Tunggu 5 detik tanpa memuat ulang halaman
36. Klik Bell icon
37. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
38. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
39. Verifikasi Dropdown Panel tidak memuat item ber-Title `Your borrowed asset is overdue` untuk AST-2024-0141 yang baru
40. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Pengulangan (bagian 8b butir 7): langkah 30 sampai 39 diulang untuk dua baris tabel "Kasus tidak dikirim TC-FA-NOTIF-332 dan 375" (50 langkah setelah ekspansi). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi): semua blok satu kelas (job overdue harian dan batas harinya, kelas d), nominalnya 40 langkah, dan tiap TC berdiri sendiri dengan seed dipulihkan.
- Urutan: tiga TC dengan notifikasi diterima atau dihitung (329, 330, 331) lebih dulu, lalu dua TC tanpa notifikasi (332, 375) dalam tabel; urutan nomor TC diubah agar kasus berpola sama berurutan (S-10).
- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state); "Catat" nilai badge dan jumlah item (baseline S-12); "Kueri status job" (langkah 24 dan 34: menunggu job selesai sebagai penanda pemicu, tanpa `Verifikasi`; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); Return aset lewat sesi API (R-20, "hingga tersimpan"); langkah 40 (pemulihan jam server dan jam browser sesudah blok terakhir yang menggeser jam, S-09).
- Asersi tambahan di luar Expected TC (S-03): TC-FA-NOTIF-332 dan 375 mengasersi badge sama dengan baseline selain item tidak ada, karena Dropdown Panel hanya memuat lima item terbaru; jumlah item per Title pada TC-FA-NOTIF-330 (langkah 17) dibaca lewat kemampuan baca BE terhadap jumlah awal (langkah 9), bukan hitungan item Dropdown Panel (bagian 8b butir 10).
- Tidak ada butir `P-n`.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (item seed pembanding `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 untuk akun aktor dan sudah ada pada surface yang sama) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-FA-NOTIF-330 dan 331 berprecondition "sudah menerima overdue 26/06/26" tetapi langkah 1 TC-FA-NOTIF-330 menjalankan job overdue pada 26/06/26; spec menyiapkan aset tanpa notifikasi overdue sebelumnya pada TC-FA-NOTIF-330 supaya total 2 teramati, dan memakai notifikasi 26/06/26 yang sudah terkirim sebagai precondition TC-FA-NOTIF-331.
  - TC-FA-NOTIF-331 tidak menyebut aktor yang mengerjakan Return; spec memakai sesi API Asset Admin Pre-setup #8. TC-FA-NOTIF-332 tidak menyebut tanggal job; spec memakai 26/06/26 pukul 00:00.
  - TC-FA-NOTIF-329 dan 330 menulis "waktu penyewa" (tampaknya waktu tenant); spec memakai zona Asia/Jakarta.
  - Post Condition kelima TC kosong (`-`); tidak ada yang diasersi.
