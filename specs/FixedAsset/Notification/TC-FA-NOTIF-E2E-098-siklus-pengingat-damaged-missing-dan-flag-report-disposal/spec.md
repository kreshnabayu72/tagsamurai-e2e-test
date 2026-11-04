---
id: TC-FA-NOTIF-E2E-098-siklus-pengingat-damaged-missing-dan-flag-report-disposal
title: "Siklus Pengingat Damaged dan Missing serta Flag Report Disposal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-343
  - TC-FA-NOTIF-344
  - TC-FA-NOTIF-345
  - TC-FA-NOTIF-346
coverage:
  web: automated
---

# Siklus Pengingat Damaged dan Missing serta Flag Report Disposal

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: siklus pengingat dan flag Report Disposal menjadi objek uji.
- Akun aktor pertama Group Manager (Gedung A): Pre-setup #3 (`groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`, `Fixture.fixedAssetNotification.groupManager`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Kemampuan menjalankan job latar (`F-FATX-11`), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta sebelum bagian spec yang tidak memerlukannya. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 dan Laptop - 1 AST-2024-0067 (Pre-setup #24). Tiket Damaged dan Missing, siklus pengingat yang sudah terkirim, flag Report Disposal, dan interval disiapkan fixture BE penyetel state sumber sebelum tiap TC. Cancel Disposal Report dikerjakan sesi API Asset Admin (Pre-setup #8; aktor pembatalan tidak disebut TC) hingga tersimpan.
- Waktu job "hari interval" ditentukan fixture BE penyetel state sumber (jam server dan jam browser diatur bersama ke tanggal itu, absolut).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan, sesudah aksi penyiapan (Cancel Disposal Report) karena aksi itu bisa menghasilkan notifikasi; jumlah awal item dengan Title dan Body yang sama juga dicatat sebelum job lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan), dan item baru dibuktikan lewat jumlah awal + 1 yang dibaca lewat kemampuan baca BE yang sama (bukan hitungan item Dropdown Panel dan bukan dua `Verifikasi` berlocator sama); asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di Dropdown Panel yang sama (bagian 8b butir 2 dan 11); status job selesai lewat kueri fixture BE hanya penanda pemicu selesai, bukan anchor; item pembanding adalah item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE, dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A, butir (i) dan (ii)): spec ini memicu job pengingat dan Cancel Disposal Report pada tiket Damaged AST-2024-0141 dan Missing AST-2024-0067 (Pre-setup #24) serta membaca notifikasi seed milik akun aktor; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar TC, dan suite berjalan serial.
- Tabel "Pembatalan Disposal Report TC-FA-NOTIF-345 dan 346" (urutan baris = urutan iterasi):

  | TC | Event | State | Aksi | Title | Body |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-345 | `damaged_reminder` | Tiket Damaged AST-2024-0141 flag Report Disposal aktif; pengingat siklus sebelumnya sudah terkirim; interval tercapai setelah flag dibatalkan | Cancel Disposal Report aset AST-2024-0141 | `Damaged asset is still unresolved` | `Kamera DSLR (AST-2024-0141) is still waiting to be repaired.` |
  | TC-FA-NOTIF-346 | `missing_reminder` | Tiket Missing AST-2024-0067 flag Report Disposal aktif; pengingat siklus sebelumnya sudah terkirim; interval tercapai setelah flag dibatalkan | Cancel Disposal Report aset AST-2024-0067 | `Missing asset is still under investigation` | `Laptop - 1 (AST-2024-0067) has not been found yet.` |


## Test Steps


### TC-FA-NOTIF-343: siklus pengingat kedua dikirim setelah interval berikutnya

1. Pulihkan seed lewat fixture BE pemulih, siapkan tiket Damaged AST-2024-0141 dengan pengingat siklus 1 sudah terkirim dan interval berikutnya tercapai, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline
3. Catat jumlah item ber-Title `Damaged asset is still unresolved` dan Body `Kamera DSLR (AST-2024-0141) is still waiting to be repaired.` milik akun aktor lewat fixture BE sebagai jumlah awal
4. Atur jam server dan jam browser ke hari interval berikutnya
5. Jalankan job `F-FATX-11` lewat kemampuan job latar hingga selesai
6. Klik Bell icon
7. Verifikasi badge Bell icon bertambah 1 terhadap baseline
8. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Damaged asset is still unresolved` dan Body `Kamera DSLR (AST-2024-0141) is still waiting to be repaired.` milik akun aktor sama dengan jumlah awal + 1 (item baru tampil dan item siklus 1 tetap tampil, tidak ditimpa)

### TC-FA-NOTIF-344: tiket Damaged dengan flag Report Disposal tidak menerima pengingat baru

9. Pulihkan seed lewat fixture BE pemulih, siapkan tiket Damaged AST-2024-0141 dengan flag Report Disposal aktif dan interval tercapai, lalu muat ulang halaman Fixed Asset > Dashboard
10. Catat jumlah badge Bell icon akun aktor sebagai baseline
11. Atur jam server dan jam browser ke hari interval
12. Jalankan job `F-FATX-11` lewat kemampuan job latar hingga selesai
13. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai)
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Klik Bell icon
16. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
17. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor sebagai pembanding
18. Verifikasi Dropdown Panel tidak memuat item `damaged_reminder` baru ber-Title `Damaged asset is still unresolved` untuk AST-2024-0141

### TC-FA-NOTIF-345 dan TC-FA-NOTIF-346: pengingat dilanjutkan setelah Cancel Disposal Report

19. Untuk setiap baris tabel "Pembatalan Disposal Report TC-FA-NOTIF-345 dan 346" (langkah 19 sampai 27): pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
20. Lakukan Aksi pada baris itu lewat sesi API Asset Admin hingga tersimpan
21. Catat jumlah badge Bell icon akun aktor sebagai baseline
22. Catat jumlah item ber-Title dan Body sesuai kolom Title dan Body baris itu milik akun aktor lewat fixture BE sebagai jumlah awal
23. Atur jam server dan jam browser ke hari interval yang tercapai setelah flag dibatalkan
24. Jalankan job `F-FATX-11` lewat kemampuan job latar hingga selesai
25. Klik Bell icon
26. Verifikasi badge Bell icon bertambah 1 terhadap baseline
27. Verifikasi (kemampuan baca BE) jumlah item ber-Title dan Body sesuai kolom Title dan Body baris itu milik akun aktor sama dengan jumlah awal + 1 (item baru tampil dan item siklus sebelumnya tetap tampil, tidak ditimpa)
28. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Pengulangan (bagian 8b butir 7): langkah 19 sampai 27 diulang untuk dua baris tabel "Pembatalan Disposal Report TC-FA-NOTIF-345 dan 346" (18 langkah setelah ekspansi; 37 langkah seluruh spec). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi): semua blok satu kelas (siklus pengingat job `F-FATX-11`, kelas d), nominalnya 28 langkah, dan tiap TC berdiri sendiri dengan seed dipulihkan.
- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state); "Catat jumlah badge Bell icon" (baseline S-12; pada baris 345 dan 346 sesudah Cancel Disposal Report) dan "Catat jumlah item ... sebagai jumlah awal" lewat kemampuan baca BE (langkah 3 dan 22); "Kueri status job" (langkah 13: menunggu job selesai sebagai penanda pemicu, tanpa `Verifikasi`; anchor absence adalah `Verifikasi` item pembanding langkah 17, bagian 8b butir 2); "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); Cancel Disposal Report lewat sesi API (R-20, "hingga tersimpan"); langkah 28 (pemulihan jam server dan jam browser sesudah blok terakhir yang menggeser jam, S-09).
- Asersi tambahan di luar Expected TC (S-03): item pembanding Dropdown Panel (langkah 17) adalah anchor positif absence (bagian 8b butir 2); jumlah item = jumlah awal + 1 (langkah 8 dan 27) menggantikan dua `Verifikasi` berlocator sama dan memuat Expected "item baru" serta "tanpa menimpa" sekaligus; baseline dan pembacaan sesudah pemicu sama-sama lewat kemampuan baca BE, bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru (bagian 8b butir 10); badge sama dengan baseline pada TC-FA-NOTIF-344 (langkah 16) dan badge bertambah 1 pada TC-FA-NOTIF-343, 345, dan 346 (langkah 7 dan 26) memakai baseline per penerima.
- Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-343, 345, dan 346 menulis "nomor siklus pengingat berikutnya"; nomor siklus tidak tampil di UI sehingga spec mengasersi item baru dan item siklus sebelumnya tetap ada.
  - TC-FA-NOTIF-345 dan 346 tidak menyebut Body dan tidak menyebut notifikasi siklus sebelumnya sebagai precondition; spec menyiapkannya lewat fixture BE dan menurunkan Body dari template TC-FA-NOTIF-343 dan 438. TC-FA-NOTIF-343, 344, 345, 346 juga tidak menyebut tanggal job ("hari interval").
  - TC-FA-NOTIF-345 dan 346 tidak menyebut aktor yang mengerjakan Cancel Disposal Report; spec memakai sesi API Asset Admin Pre-setup #8.
  - Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
