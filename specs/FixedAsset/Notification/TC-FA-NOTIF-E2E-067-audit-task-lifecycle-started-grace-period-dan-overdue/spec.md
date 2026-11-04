---
id: TC-FA-NOTIF-E2E-067-audit-task-lifecycle-started-grace-period-dan-overdue
title: "Penerimaan Notifikasi Audit Task: Started, Grace Period, dan Overdue"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-257
  - TC-FA-NOTIF-258
  - TC-FA-NOTIF-259
  - TC-FA-NOTIF-260
coverage:
  web: automated
---
# Penerimaan Notifikasi Audit Task: Started, Grace Period, dan Overdue

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Auditor Rina Wijaya | #13 | `auditorRina_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AUDITOR_PASSWORD` | `Fixture.fixedAssetNotification.auditorRina` |
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Login akun aktor pertama (Auditor Rina Wijaya, Pre-setup #13) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): Task Audit Q3-Gedung A (TASK-Q3-A; Pre-setup #23) dengan status diatur lewat fixture BE per blok; Auditor Rina Wijaya Pre-setup #13; Asset Admin Gedung A Pre-setup #8. Perpindahan status task dipicu scheduler harian audit lewat fixture BE (pemicu, bukan objek uji).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah scheduler harian audit pada Task Audit Q3-Gedung A (Pre-setup #23) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_AUDITOR_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-257: Notifikasi audit_task_started diterima: task memasuki In Audit

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Task Audit Q3-Gedung A On Schedule, tanggal audit tiba, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Auditor sebagai baseline (0 bila badge tidak tampil)
3. Jalankan scheduler harian audit lewat fixture BE hingga Task Audit Q3-Gedung A berstatus In Audit dan notifikasi tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Auditor bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"New audit task started"` dan Body `"Task Audit Q3-Gedung A is now active."` (dari template `"[Task Name] is now active."`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/audit/task/TASK-Q3-A` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-258: Notifikasi audit_task_grace_period diterima: task memasuki Grace Period

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Task Audit Q3-Gedung A In Audit, durasi berakhir
16. Muat ulang halaman Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Auditor sebagai baseline (0 bila badge tidak tampil)
18. Jalankan scheduler harian audit lewat fixture BE hingga Task Audit Q3-Gedung A berstatus Grace Period dan notifikasi tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Auditor bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Audit task entering grace period"` dan Body `"Task Audit Q3-Gedung A duration has expired."` (dari template `"[Task Name] duration has expired."`)
25. Verifikasi icon `time-line` dengan severity `warning` pada item
26. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
27. Klik `[Detail]` pada item tersebut
28. Verifikasi halaman tujuan `/fams/audit/task/TASK-Q3-A` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-259: Notifikasi audit_task_overdue varian Auditor diterima: task memasuki Overdue

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Task Audit Q3-Gedung A Grace Period habis
31. Muat ulang halaman Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Auditor sebagai baseline (0 bila badge tidak tampil)
33. Jalankan scheduler harian audit lewat fixture BE hingga Task Audit Q3-Gedung A berstatus Overdue dan notifikasi tersimpan
34. Klik Bell icon
35. Verifikasi badge Bell icon Auditor bertambah 1 dari baseline langkah 32
36. Verifikasi item baru berada di posisi teratas Dropdown Panel
37. Verifikasi Title item baru bold
38. Verifikasi dot Unread tampil pada item baru
39. Verifikasi item menampilkan Title `"Audit task is overdue"` dan Body `"Task Audit Q3-Gedung A requires immediate update."` (dari template `"[Task Name] requires immediate update."`)
40. Verifikasi icon `time-line` dengan severity `warning` pada item
41. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
42. Klik judul item tersebut (bukan tombol)
43. Verifikasi halaman tujuan `/fams/audit/task/TASK-Q3-A` terbuka
44. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 35

### TC-FA-NOTIF-260: Notifikasi audit_task_overdue varian Asset Admin atau Group Manager diterima: task memasuki Overdue

45. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Task Audit Q3-Gedung A Grace Period habis
46. Ganti akun: logout, lalu login sebagai Asset Admin (Gedung A) (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
47. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
48. Jalankan scheduler harian audit lewat fixture BE hingga Task Audit Q3-Gedung A berstatus Overdue dan notifikasi tersimpan
49. Klik Bell icon
50. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 47
51. Verifikasi item baru berada di posisi teratas Dropdown Panel
52. Verifikasi Title item baru bold
53. Verifikasi dot Unread tampil pada item baru
54. Verifikasi item menampilkan Title `"Audit task is overdue"` dan Body `"Task Audit Q3-Gedung A requires immediate update."` (dari template `"[Task Name] requires immediate update."`)
55. Verifikasi icon `time-line` dengan severity `warning` pada item
56. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
57. Klik `[Detail]` pada item tersebut
58. Verifikasi halaman tujuan `/fams/audit/task/TASK-Q3-A` terbuka
59. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 50

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30, 45 (penyiapan kondisi data lewat fixture BE); langkah 46 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17, 32, 47 (pencatatan baseline badge Bell icon (S-12)); langkah 16 dan 31 (muat ulang halaman Fixed Asset > Dashboard sesudah pemulihan seed dan sebelum pencatatan baseline; juga menutup Dropdown Panel blok sebelumnya (S-09, S-14)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (59 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Scheduler harian audit hanya pemicu perpindahan status; batas waktu perpindahan sebagai objek uji ada di spec job terjadwal.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-257 sampai 260 menulis "Picu: Task ..." tanpa menyebut job; spec memakai kemampuan scheduler harian audit yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-FA-NOTIF-260 menulis login "Asset Admin (Gedung A)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8.
