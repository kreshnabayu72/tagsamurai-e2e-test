---
id: TC-FA-NOTIF-E2E-094-due-soon-mundur-extend-dan-re-eksekusi-job
title: "Due Soon: Ambang Terlewati saat Handover, Extend Due Date, dan Re-Eksekusi Job"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-327
  - TC-FA-NOTIF-328
  - TC-FA-NOTIF-415
coverage:
  web: automated
---

# Due Soon: Ambang Terlewati saat Handover, Extend Due Date, dan Re-Eksekusi Job

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: ambang tanggal job menjadi objek uji.
- Akun aktor pertama Borrower (Budi Santoso): Pre-setup #11 (`borrowerBudi_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_BORROWER_PASSWORD`, `Fixture.fixedAssetNotification.borrowerBudi`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Kemampuan menjalankan job latar (job due soon harian), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di akhir blok terakhir yang menggeser jam. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 Borrowed pada BRW-2026-0342 (Pre-setup #19 dan #24). Handover, Due Date 25/06/26, dan notifikasi due soon yang sudah terkirim disiapkan fixture BE penyetel state sumber sebelum tiap TC. Extend Due Date dikerjakan sesi API Asset Admin (Pre-setup #8; aktor Extend tidak disebut TC).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job pada transaksi dan aset Pre-setup bersama (BRW-2026-0342, AST-2024-0141) yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar TC; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Format tanggal pada Body notifikasi mengikuti Date Format General Settings `dd/MM/yy` (nilai awal, Pre-setup #1); jam fixture acuan "hari ini" 18/06/26.
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di surface yang sama (item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE; kueri status job selesai lewat fixture BE hanya menandai pemicu selesai, bukan bukti panel memuat item) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_BORROWER_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.

## Test Steps


### TC-FA-NOTIF-327: tidak ada notifikasi mundur untuk ambang yang terlewati saat Handover

1. Pulihkan seed lewat fixture BE pemulih, siapkan Handover AST-2024-0141 pada 23/06/26 dengan Due Date 25/06/26 (ambang H-3 = 22/06/26 sudah terlewati), lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `Your borrowed asset is due soon` untuk AST-2024-0141 milik akun aktor sebagai jumlah awal
3. Atur jam server dan jam browser ke 23/06/26
4. Jalankan job due soon lewat kemampuan job latar hingga selesai
5. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Klik Bell icon
8. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
9. Verifikasi badge Bell icon sama dengan baseline (tidak ada notifikasi ambang H-3)
10. Klik Bell icon untuk menutup Dropdown Panel
11. Atur jam server dan jam browser ke 24/06/26
12. Jalankan job due soon lewat kemampuan job latar hingga selesai
13. Verifikasi badge Bell icon bertambah 1 terhadap baseline (ambang H-1 dikirim pada tanggalnya)
14. Atur jam server dan jam browser ke 25/06/26
15. Jalankan job due soon lewat kemampuan job latar hingga selesai
16. Verifikasi badge Bell icon bertambah 2 terhadap baseline (ambang hari-H dikirim pada tanggalnya)
17. Klik Bell icon
18. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Your borrowed asset is due soon` untuk AST-2024-0141 milik akun aktor sama dengan jumlah awal langkah 2 + 2 (ambang H-1 dan hari-H masing-masing satu item)

### TC-FA-NOTIF-328: ambang dihitung ulang terhadap Due Date baru setelah Extend

19. Pulihkan seed lewat fixture BE pemulih, siapkan AST-2024-0141 Borrowed dengan Due Date 25/06/26 yang notifikasi due soon ambang H-3 (job 22/06/26) sudah terkirim dan masih Unread, lalu muat ulang halaman Fixed Asset > Dashboard
20. Extend Due Date AST-2024-0141 menjadi 30/06/26 lewat sesi API Asset Admin hingga tersimpan
21. Atur jam server dan jam browser ke 27/06/26 (H-3 Due Date baru)
22. Catat jumlah badge Bell icon akun aktor sebagai baseline
23. Jalankan job due soon lewat kemampuan job latar hingga selesai
24. Klik Bell icon
25. Verifikasi badge Bell icon bertambah 1 terhadap baseline (notifikasi Due Date baru tidak dianggap duplikat)
26. Verifikasi item baru ber-Title `Your borrowed asset is due soon` dan Body `Kamera DSLR is due on 30/06/26.` tampil
27. Verifikasi notifikasi due soon lama untuk Due Date 25/06/26 tetap Unread

### TC-FA-NOTIF-415: re-eksekusi job pada ambang yang sama tidak menggandakan notifikasi

28. Pulihkan seed lewat fixture BE pemulih, siapkan AST-2024-0141 Borrowed pada BRW-2026-0342 dengan Due Date 25/06/26, lalu muat ulang halaman Fixed Asset > Dashboard
29. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `Your borrowed asset is due soon` untuk AST-2024-0141 milik akun aktor sebagai jumlah awal
30. Atur jam server dan jam browser ke 22/06/26 (H-3)
31. Jalankan job harian due soon lewat kemampuan job latar hingga selesai
32. Jalankan job harian due soon sekali lagi pada tanggal yang sama hingga selesai
33. Klik Bell icon
34. Verifikasi badge Bell icon bertambah 1 terhadap baseline
35. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Your borrowed asset is due soon` untuk AST-2024-0141 milik akun aktor sama dengan jumlah awal langkah 29 + 1 (ambang H-3; identitas event yang sama diabaikan)
36. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state); "Catat jumlah badge Bell icon" (baseline S-12); "Kueri status job" (penanda pemicu selesai; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); Extend Due Date lewat sesi API (R-20, "hingga tersimpan"); langkah 36 (pemulihan jam server dan jam browser ke waktu nyata, S-09 dan R-08).
- Alasan melewati ambang sekitar 35 langkah (36 langkah): semua blok satu kelas (ambang tanggal job due soon, kelas d) pada dataset AST-2024-0141 yang sama, tiap TC berdiri sendiri dengan seed dipulihkan, dan langkah ke-36 hanya pemulihan jam.
- Pengamatan TC-FA-NOTIF-327 dilakukan setelah tiap job (badge terhadap baseline) agar "dikirim pada tanggalnya" teramati; Expected TC mengamati lewat Klik Bell icon sekali sesudah tiga job. Asersi tambahan ini dicatat sesuai S-03 karena notifikasi H-1 dan hari-H memakai Title dan Body yang sama sehingga tidak dapat dibedakan di Dropdown Panel; jumlah item per Title (langkah 18 dan 35) dibaca lewat kemampuan baca BE terhadap jumlah awal (langkah 2 dan 29), bukan hitungan item Dropdown Panel (bagian 8b butir 10).
- Tidak ada butir `P-n`.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (item seed pembanding `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 untuk akun aktor dan sudah ada pada surface yang sama) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-FA-NOTIF-328 tidak menyebut aktor yang mengerjakan Extend; spec memakai sesi API Asset Admin Pre-setup #8 (disediakan tim FE/BE).
  - TC-FA-NOTIF-327 menulis "dikirim pada tanggalnya" tetapi item H-1 dan hari-H tidak dapat dibedakan di UI (Title dan Body sama); spec mengasersi jumlah badge per titik job dan jumlah item akhir.
  - TC-FA-NOTIF-328 tidak menyebut Body notifikasi Due Date baru; spec menurunkannya dari template TC-FA-NOTIF-324 (`Kamera DSLR is due on 30/06/26.`).
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
