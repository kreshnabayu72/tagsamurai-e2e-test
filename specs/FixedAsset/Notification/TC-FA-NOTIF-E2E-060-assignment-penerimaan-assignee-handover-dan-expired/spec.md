---
id: TC-FA-NOTIF-E2E-060-assignment-penerimaan-assignee-handover-dan-expired
title: "Penerimaan Notifikasi Assignment oleh Assignee: Acceptance Required, Expired, dan Handover Selesai"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-241
  - TC-FA-NOTIF-244
  - TC-FA-NOTIF-246
coverage:
  web: automated
---
# Penerimaan Notifikasi Assignment oleh Assignee: Acceptance Required, Expired, dan Handover Selesai

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Assignee Siti Rahmawati | #12 | `assigneeSiti_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSIGNEE_PASSWORD` | `Fixture.fixedAssetNotification.assigneeSiti` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Menyelesaikan verifikasi scan dan handover fisik ASG-2026-0120.
- Login akun aktor pertama (Assignee Siti Rahmawati, Pre-setup #12) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): ASG-2026-0120 (Laptop - 1 AST-2024-0067, Assignee Siti Rahmawati; Pre-setup #19 dan #20). Job auto-cancel Waiting for Acceptance (F-ASSIGN-11 langkah 5) hanya pemicu.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu verifikasi scan, handover fisik, dan job auto-cancel pada ASG-2026-0120 (Pre-setup #19 dan #20) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSIGNEE_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-241: Notifikasi assignment_acceptance_required diterima: verifikasi scan selesai, status Waiting for Acceptance

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 aset Verified, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Assignee sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan ASG-2026-0120 hingga status Waiting for Acceptance tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Assignee bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Please accept your asset assignment"` dan Body `"Laptop - 1 (AST-2024-0067)"` (dari template `"[Asset Name] ([Asset ID])"`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/my-asset/task/assignment/ASG-2026-0120` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-244: Notifikasi assignment_acceptance_expired varian Assignee diterima: auto-cancel lewat 48 jam

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Acceptance lebih dari 48 jam, lalu muat ulang halaman Fixed Asset > Dashboard
16. Catat jumlah pada badge Bell icon Assignee sebagai baseline (0 bila badge tidak tampil)
17. Jalankan job terjadwal auto-cancel Waiting for Acceptance (F-ASSIGN-11 langkah 5) lewat fixture BE hingga ASG-2026-0120 dibatalkan otomatis dan notifikasi tersimpan
18. Klik Bell icon
19. Verifikasi badge Bell icon Assignee bertambah 1 dari baseline langkah 16
20. Verifikasi item baru berada di posisi teratas Dropdown Panel
21. Verifikasi Title item baru bold
22. Verifikasi dot Unread tampil pada item baru
23. Verifikasi item menampilkan Title `"Assignment acceptance expired"` dan Body `"Laptop - 1 (AST-2024-0067) was not accepted in time."` (dari template `"[Asset Name] ([Asset ID]) was not accepted in time."`)
24. Verifikasi icon `time-line` dengan severity `warning` pada item
25. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
26. Klik judul item tersebut (bukan tombol)
27. Verifikasi halaman tujuan `/fams/my-asset/task/assignment` terbuka
28. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 19

### TC-FA-NOTIF-246: Notifikasi assignment_handover_completed diterima: handover fisik selesai, status Assigned

29. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Handover, lalu muat ulang halaman Fixed Asset > Dashboard
30. Catat jumlah pada badge Bell icon Assignee sebagai baseline (0 bila badge tidak tampil)
31. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover fisik ASG-2026-0120 hingga status Assigned tersimpan
32. Klik Bell icon
33. Verifikasi badge Bell icon Assignee bertambah 1 dari baseline langkah 30
34. Verifikasi item baru berada di posisi teratas Dropdown Panel
35. Verifikasi Title item baru bold
36. Verifikasi dot Unread tampil pada item baru
37. Verifikasi item menampilkan Title `"Asset handover completed"` dan Body `"Laptop - 1 is now officially your responsibility."` (dari template `"[Asset Name] is now officially your responsibility."`)
38. Verifikasi icon `checkbox-circle-line` dengan severity `success` pada item
39. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
40. Klik judul item tersebut (bukan tombol)
41. Verifikasi halaman tujuan `/fams/my-asset/assigned/ASG-2026-0120` terbuka
42. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 33

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 29 (penyiapan kondisi data lewat fixture BE; pada langkah 1, 15, dan 29 diikuti muat ulang halaman Fixed Asset > Dashboard sebelum baseline); langkah 2, 16, 30 (pencatatan baseline badge Bell icon (S-12)).
- Job auto-cancel Waiting for Acceptance hanya pemicu, bukan objek uji.
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (42 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Spec 060 memuat penerimaan Assignee atas ASG-2026-0120; tahap persetujuan ada di spec 059 dan decline atau accepted di spec 061.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
