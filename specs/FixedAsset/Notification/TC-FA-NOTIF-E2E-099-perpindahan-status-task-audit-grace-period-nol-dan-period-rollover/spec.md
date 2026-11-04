---
id: TC-FA-NOTIF-E2E-099-perpindahan-status-task-audit-grace-period-nol-dan-period-rollover
title: "Perpindahan Status Task Audit: Sekali per Perpindahan, Grace Period Nol, dan Period Rollover"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-347
  - TC-FA-NOTIF-348
  - TC-FA-NOTIF-349
coverage:
  web: automated
---

# Perpindahan Status Task Audit: Sekali per Perpindahan, Grace Period Nol, dan Period Rollover

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: perpindahan status task audit oleh scheduler harian menjadi objek uji.
- Akun aktor pertama Auditor (Rina Wijaya): Pre-setup #13 (`auditorRina_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_AUDITOR_PASSWORD`, `Fixture.fixedAssetNotification.auditorRina`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (scheduler harian audit (termasuk Period Rollover)) dan menggeser jam server dan jam fixture (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di akhir blok terakhir yang menggeser jam. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): task audit `Task Audit Q3-Gedung A` (Pre-setup #23; status On Schedule, In Audit, Grace Period, Overdue per TC). Status task, durasi, grace period, dan jadwal periode berikutnya disiapkan fixture BE penyetel state sumber sebelum tiap TC; tanggal tiap perpindahan dibaca dari state task itu.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah scheduler harian pada Task Audit Q3-Gedung A (Pre-setup #23) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului anchor positif (`Verifikasi` item yang diterima pada surface yang sama, bagian 8b butir 2) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_AUDITOR_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.

## Test Steps


### TC-FA-NOTIF-347: satu notifikasi per perpindahan status dan eksekusi ulang tidak menggandakan

1. Pulihkan seed lewat fixture BE pemulih, siapkan Task Audit Q3-Gedung A sebelum dimulai dengan penerima Auditor Rina Wijaya, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title `New audit task started`, `Audit task entering grace period`, dan `Audit task is overdue` milik akun aktor sebagai jumlah awal masing-masing
3. Atur jam server dan jam browser ke tanggal task memasuki In Audit, lalu jalankan scheduler harian hingga selesai
4. Atur jam server dan jam browser ke tanggal task memasuki Grace Period, lalu jalankan scheduler harian hingga selesai
5. Atur jam server dan jam browser ke tanggal task memasuki Overdue, lalu jalankan scheduler harian hingga selesai
6. Jalankan scheduler harian sekali lagi pada hari yang sama hingga selesai
7. Klik Bell icon
8. Verifikasi (kemampuan baca BE) jumlah item ber-Title `New audit task started` milik akun aktor sama dengan jumlah awal langkah 2 + 1
9. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task entering grace period` milik akun aktor sama dengan jumlah awal langkah 2 + 1
10. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task is overdue` milik akun aktor sama dengan jumlah awal langkah 2 + 1
11. Verifikasi badge Bell icon bertambah 3 terhadap baseline (eksekusi ulang tidak menggandakan)

### TC-FA-NOTIF-348: grace period 0 hari, hanya audit_task_overdue dikirim

12. Pulihkan seed lewat fixture BE pemulih, siapkan Task Audit Q3-Gedung A dengan grace period 0 hari dan durasi berakhir, lalu muat ulang halaman Fixed Asset > Dashboard
13. Catat jumlah badge Bell icon akun aktor sebagai baseline
14. Atur jam server dan jam browser ke tanggal durasi task berakhir
15. Jalankan scheduler harian hingga selesai
16. Tunggu 5 detik tanpa memuat ulang halaman
17. Klik Bell icon
18. Verifikasi item ber-Title `Audit task is overdue` diterima
19. Verifikasi Dropdown Panel tidak memuat item ber-Title `Audit task entering grace period`
20. Verifikasi badge Bell icon bertambah 1 terhadap baseline

### TC-FA-NOTIF-349: Period Rollover membentuk task baru yang memicu audit_task_started

21. Pulihkan seed lewat fixture BE pemulih, siapkan task lama Overdue dengan notifikasi `New audit task started`, `Audit task entering grace period`, dan `Audit task is overdue` task lama sudah diterima Auditor Rina Wijaya, lalu muat ulang halaman Fixed Asset > Dashboard
22. Catat lewat kemampuan baca BE jumlah item ber-Title `New audit task started` milik akun aktor sebagai jumlah awal
23. Atur jam server dan jam browser ke tanggal jadwal periode berikutnya
24. Jalankan scheduler harian yang menjalankan Period Rollover hingga selesai
25. Klik Bell icon
26. Verifikasi (kemampuan baca BE) jumlah item ber-Title `New audit task started` milik akun aktor sama dengan jumlah awal langkah 22 + 1 (item baru untuk task baru diterima)
27. Verifikasi notifikasi task lama ber-Title `New audit task started` berstatus Read
28. Verifikasi notifikasi task lama ber-Title `Audit task entering grace period` berstatus Read
29. Verifikasi notifikasi task lama ber-Title `New audit task started` tanpa tombol `[Detail]`
30. Verifikasi notifikasi task lama ber-Title `Audit task entering grace period` tanpa tombol `[Detail]`
31. Verifikasi notifikasi task lama ber-Title `Audit task is overdue` (varian Auditor, view-only) tetap Unread
32. Verifikasi notifikasi task lama ber-Title `Audit task is overdue` (varian Auditor, view-only) memuat tombol `[Mark as Read]`
33. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state); "Catat jumlah badge Bell icon" (baseline S-12); pengaturan jam ke tanggal tiap perpindahan (dibaca dari state task); "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 16, bagian 6) sebelum absence notifikasi grace period; langkah 33 (pemulihan jam server dan jam browser ke waktu nyata, S-09 dan R-08).
- Pembagian TC lintas spec: TC-FA-NOTIF-395 dan 420 (siklus berikutnya setelah Extend dan Reject) ada di spec 120.
- Asersi tambahan di luar Expected TC (S-03): TC-FA-NOTIF-347 dan 348 memakai badge terhadap baseline selain item, karena jumlah notifikasi harus memakai baseline per penerima (bagian 8b butir 10); jumlah item per Title (langkah 8 sampai 10 dan 26) dibaca lewat kemampuan baca BE terhadap jumlah awal (langkah 2 dan 22), bukan hitungan item Dropdown Panel; pada TC-FA-NOTIF-348 absence item grace period memakai item overdue yang diterima sebagai anchor positif (bagian 8b butir 2).
- Tidak ada butir `P-n`.
- Spec 099 dan 120 memakai Task Audit Q3-Gedung A yang sama (juga spec 067 dan 068) dan dibedakan karena spec 099 menguji satu siklus perpindahan status, sedangkan spec 120 menguji siklus berikutnya setelah Extend dan Reject; state task disiapkan ulang fixture BE sebelum tiap TC.
- Temuan untuk QA:
  - TC-FA-NOTIF-347, 348, dan 349 tidak menyebut tanggal tiap perpindahan task maupun nama task baru hasil Period Rollover; spec membaca tanggal dari state task fixture dan mengidentifikasi item lewat Title.
  - TC-FA-NOTIF-349 tidak menyebut Body notifikasi sehingga item task lama dan task baru dengan Title sama dibedakan hanya lewat urutan dan status; mohon Body (nama task) dilengkapi.
  - TC-FA-NOTIF-347 menyebut `audit_task_started` tanpa Title; spec memakai Title dari TC-FA-NOTIF-349 (`New audit task started`).
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
