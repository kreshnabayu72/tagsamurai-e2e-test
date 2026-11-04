---
id: TC-FA-NOTIF-E2E-121-batas-acceptance-expired-assignment-48-jam-dan-idempotensi-job
title: "Batas Acceptance Expired Assignment 48 Jam dan Idempotensi Job"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-340
  - TC-FA-NOTIF-341
  - TC-FA-NOTIF-416
coverage:
  web: automated
---

# Batas Acceptance Expired Assignment 48 Jam dan Idempotensi Job

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: batas 48 jam job acceptance expired menjadi objek uji.
- Akun aktor pertama Assignee (Siti Rahmawati): Pre-setup #12 (`assigneeSiti_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSIGNEE_PASSWORD`, `Fixture.fixedAssetNotification.assigneeSiti`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (job auto-cancel Waiting for Acceptance (`F-ASSIGN-11` langkah 5)), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta sebelum bagian spec yang tidak memerlukannya. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta. Waktu job dihitung dari `verified_at` transaksi yang dibaca fixture BE penyetel state sumber saat seed dibuat (bukan diperkirakan dari waktu hook); jam server diset absolut ke `verified_at` + durasi. Margin terhadap batas hanya satu menit (kurang dari 5 menit) dan dihitung sebagai selisih menit terhadap `verified_at` + 48 jam (bagian 8b butir 3).
- Data Pre-setup (tetap di environment): transaksi Assignment ASG-2026-0120 (Pre-setup #20). Status Waiting for Acceptance dan `verified_at` disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job pada transaksi Pre-setup bersama (ASG-2026-0120) yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar TC; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di surface yang sama (item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE; kueri status job selesai lewat fixture BE hanya menandai pemicu selesai, bukan bukti panel memuat item) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSIGNEE_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.

## Test Steps


### TC-FA-NOTIF-340: acceptance expired pada verified_at + tepat 48 jam

1. Pulihkan seed lewat fixture BE pemulih, siapkan ASG-2026-0120 Waiting for Acceptance dengan `verified_at` + tepat 48 jam, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline
3. Atur jam server dan jam browser ke `verified_at` + tepat 48 jam
4. Jalankan job expiry (`F-ASSIGN-11` langkah 5) lewat kemampuan job latar hingga selesai
5. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Klik Bell icon
8. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
9. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
10. Verifikasi Dropdown Panel tidak memuat item ber-Title `Assignment acceptance expired` untuk ASG-2026-0120

### TC-FA-NOTIF-341: acceptance expired pada verified_at + 48 jam 1 menit

11. Pulihkan seed lewat fixture BE pemulih, siapkan ASG-2026-0120 Waiting for Acceptance dengan `verified_at` + 48 jam 1 menit, lalu muat ulang halaman Fixed Asset > Dashboard
12. Catat jumlah badge Bell icon akun aktor sebagai baseline
13. Atur jam server dan jam browser ke `verified_at` + 48 jam 1 menit
14. Jalankan job expiry (`F-ASSIGN-11` langkah 5) lewat kemampuan job latar hingga selesai
15. Klik Bell icon sebagai Assignee
16. Verifikasi badge Bell icon bertambah 1 terhadap baseline
17. Verifikasi item ber-Title `Assignment acceptance expired` untuk ASG-2026-0120 diterima

### TC-FA-NOTIF-416: re-eksekusi job tidak menggandakan notifikasi

18. Pulihkan jam server dan jam browser ke jam fixture acuan (18/06/26) lewat kemampuan menggeser jam
19. Pulihkan seed lewat fixture BE pemulih, siapkan ASG-2026-0120 Waiting for Acceptance lebih dari 48 jam, lalu muat ulang halaman Fixed Asset > Dashboard
20. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `Assignment acceptance expired` untuk ASG-2026-0120 milik akun aktor sebagai jumlah awal
21. Jalankan job terjadwal auto-cancel Waiting for Acceptance (`F-ASSIGN-11` langkah 5) lewat kemampuan job latar hingga selesai
22. Jalankan job terjadwal auto-cancel Waiting for Acceptance sekali lagi hingga selesai
23. Klik Bell icon sebagai Assignee
24. Verifikasi badge Bell icon bertambah 1 terhadap baseline
25. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Assignment acceptance expired` untuk ASG-2026-0120 milik akun aktor sama dengan jumlah awal langkah 20 + 1

## Notes

- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state); "Catat jumlah badge Bell icon" (baseline S-12); "Kueri status job" (penanda pemicu selesai; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); "Pulihkan jam server dan jam browser" di awal TC-FA-NOTIF-416 (jam dari TC-FA-NOTIF-341 tidak terbawa, S-09 dan R-08).
- Pembagian TC lintas spec: TC-FA-NOTIF-338, 339, dan 342 (akun Asset Admin) ada di spec 097.
- Asersi tambahan di luar Expected TC (S-03): badge sama dengan baseline pada TC-FA-NOTIF-340 dan badge bertambah 1 pada TC-FA-NOTIF-341 dan 416, karena Dropdown Panel hanya memuat lima item terbaru dan jumlah notifikasi harus memakai baseline per penerima (bagian 8b butir 10); jumlah item per Title pada TC-FA-NOTIF-416 (langkah 25) dibaca lewat kemampuan baca BE terhadap jumlah awal langkah 20, bukan hitungan item Dropdown Panel.
- Tidak ada butir `P-n`.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (item seed pembanding `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 untuk akun aktor dan sudah ada pada surface yang sama) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-FA-NOTIF-340 sampai 341 menyebut "job expiry" tanpa ID job; spec memakai `F-ASSIGN-11` langkah 5 menurut TC-FA-NOTIF-416.
  - TC-FA-NOTIF-341 tidak menyebut Body notifikasi `assignment_acceptance_expired`; spec hanya mengasersi Title.
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
