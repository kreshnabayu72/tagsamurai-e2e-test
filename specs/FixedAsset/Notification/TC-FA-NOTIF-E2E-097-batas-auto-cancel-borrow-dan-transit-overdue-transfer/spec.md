---
id: TC-FA-NOTIF-E2E-097-batas-auto-cancel-borrow-dan-transit-overdue-transfer
title: "Batas Auto Cancel Borrow dan Transit Overdue Transfer"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-338
  - TC-FA-NOTIF-339
  - TC-FA-NOTIF-342
coverage:
  web: automated
---

# Batas Auto Cancel Borrow dan Transit Overdue Transfer

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: batas menit job auto-cancel dan transit overdue menjadi objek uji.
- Akun aktor pertama Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (`F-FATX-07`, job transit overdue), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di awal TC yang tidak memerlukannya. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta. Waktu job dihitung dari `cancel_deadline_at` transaksi yang dibaca fixture BE penyetel state sumber saat seed dibuat (bukan diperkirakan dari waktu hook), jam server diset absolut. Margin terhadap batas hanya satu menit (kurang dari 5 menit) dan dihitung sebagai selisih menit terhadap `cancel_deadline_at` (bagian 8b butir 3).
- Kemampuan teknis tambahan: fixture BE pembaca status transaksi (dipakai langkah 2 untuk baseline status BRW-2026-0342), disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (Pre-setup #19) dan Transfer TRF-2026-0055 (Pre-setup #21). Status transaksi, `cancel_deadline_at`, dan batas transit disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job pada transaksi Pre-setup bersama (BRW-2026-0342, TRF-2026-0055) yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar TC; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di Dropdown Panel yang sama (status job selesai lewat kueri fixture BE hanya penanda pemicu selesai, bukan anchor absence; bagian 8b butir 2 dan 11; item pembanding adalah item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.

## Test Steps


### TC-FA-NOTIF-338: auto_cancel satu menit sebelum cancel_deadline_at

1. Pulihkan seed lewat fixture BE pemulih, siapkan BRW-2026-0342 pra-komitmen, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline, dan catat status transaksi BRW-2026-0342 lewat fixture BE pembaca status transaksi sebagai baseline status
3. Atur jam server dan jam browser ke `cancel_deadline_at` − 1 menit
4. Jalankan job `F-FATX-07` langkah 3 lewat kemampuan job latar hingga selesai
5. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Buka detail transaksi BRW-2026-0342 di `/fams/borrow/BRW-2026-0342`
8. Verifikasi status transaksi sama dengan baseline status dan bukan Canceled (belum dibatalkan)
9. Buka halaman Fixed Asset > Dashboard
10. Klik Bell icon
11. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
12. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor sebagai pembanding
13. Verifikasi Dropdown Panel tidak memuat item ber-Title `Your request was canceled automatically` untuk BRW-2026-0342

### TC-FA-NOTIF-339: auto_cancel tepat di cancel_deadline_at

14. Pulihkan jam server dan jam browser ke waktu nyata
15. Pulihkan seed lewat fixture BE pemulih, siapkan BRW-2026-0342 pra-komitmen, lalu muat ulang halaman Fixed Asset > Dashboard
16. Catat jumlah badge Bell icon akun aktor sebagai baseline
17. Atur jam server dan jam browser ke `cancel_deadline_at` + 0 menit
18. Jalankan job `F-FATX-07` langkah 3 lewat kemampuan job latar hingga selesai
19. Buka detail transaksi BRW-2026-0342 di `/fams/borrow/BRW-2026-0342`
20. Verifikasi status transaksi Canceled
21. Buka halaman Fixed Asset > Dashboard
22. Klik Bell icon
23. Verifikasi badge Bell icon bertambah 1 terhadap baseline
24. Verifikasi item ber-Title `Your request was canceled automatically` untuk BRW-2026-0342 diterima

### TC-FA-NOTIF-342: transfer_transit_overdue satu kali per transaksi

25. Pulihkan jam server dan jam browser ke waktu nyata
26. Pulihkan seed lewat fixture BE pemulih, siapkan TRF-2026-0055 In Transfer Process dengan batas transit terlampaui, lalu muat ulang halaman Fixed Asset > Dashboard
27. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `Your transfer is overdue` untuk TRF-2026-0055 milik akun aktor sebagai jumlah awal
28. Jalankan job overdue transit lewat kemampuan job latar hingga selesai
29. Jalankan job overdue transit sekali lagi lewat kemampuan job latar hingga selesai
30. Klik Bell icon
31. Verifikasi badge Bell icon bertambah 1 terhadap baseline
32. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Your transfer is overdue` untuk TRF-2026-0055 milik akun aktor sama dengan jumlah awal langkah 27 + 1
33. Buka detail transaksi TRF-2026-0055 di `/fams/transactions-transfer/TRF-2026-0055`
34. Verifikasi status transaksi tetap In Transfer Process (tidak auto-cancel)

## Notes

- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state) dan langkah 14 serta 25 (pemulihan jam server dan jam browser yang digeser TC sebelumnya, S-09 dan R-08); status transaksi baseline dibaca lewat fixture BE pembaca status (langkah 2) lalu dibandingkan dengan status di halaman detail (langkah 8); "Catat jumlah badge Bell icon" (baseline S-12); "Kueri status job" (penanda pemicu selesai, bukan anchor absence; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); membuka detail transaksi dan kembali ke Dashboard (mengamati status transaksi yang disebut Expected).
- Urutan: TC-FA-NOTIF-338, 339, 342 berurutan menurut nomor TC; TC-FA-NOTIF-340, 341, dan 416 (akun Assignee) ada di spec 121.
- Asersi tambahan di luar Expected TC (S-03): item pembanding Dropdown Panel (langkah 12) adalah anchor positif absence (bagian 8b butir 2); badge sama dengan baseline pada TC-FA-NOTIF-338 dan badge bertambah 1 pada TC-FA-NOTIF-339 dan 342, karena Dropdown Panel hanya memuat lima item terbaru dan jumlah notifikasi harus memakai baseline per penerima (bagian 8b butir 10); jumlah item per Title pada TC-FA-NOTIF-342 (langkah 32) dibaca lewat kemampuan baca BE terhadap jumlah awal langkah 27, bukan hitungan item Dropdown Panel.
- Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-338 sampai 342 menyebut Role Asset Admin tanpa nomor Pre-setup (PIC pembuat dan pemohon); spec memakai Pre-setup #8.
  - TC-FA-NOTIF-342 tidak menyebut Body notifikasi `transfer_transit_overdue`; spec hanya mengasersi Title dan jumlah item.
  - TC-FA-NOTIF-338 tidak menyebut status transaksi pra-komitmen yang spesifik; spec mencatat status sebelum job dan membandingkannya.
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
