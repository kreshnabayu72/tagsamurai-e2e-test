---
id: TC-FA-NOTIF-E2E-061-assignment-decline-accepted-dan-penerima-negatif
title: "Penerimaan Notifikasi Assignment Declined dan Accepted serta Penerima yang Tidak Berhak"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-242
  - TC-FA-NOTIF-243
  - TC-FA-NOTIF-406
  - TC-FA-NOTIF-407
coverage:
  web: automated
---
# Penerimaan Notifikasi Assignment Declined dan Accepted serta Penerima yang Tidak Berhak

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | Approver (Borrowing & Assignment, Gedung A) | #4 | `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Assignee Siti Rahmawati (Pre-setup #12, `assigneeSiti_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSIGNEE_PASSWORD`). Klik Accept atau Decline pada halaman acceptance ASG-2026-0120.
- Login akun aktor pertama (Asset Admin (Gedung A), Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): ASG-2026-0120 (Laptop - 1 AST-2024-0067, Assignee Siti Rahmawati; Pre-setup #19 dan #20); Asset Admin Pre-setup #8 adalah PIC admin; Group Manager Gedung A (Pre-setup #3) dan Approver Borrowing & Assignment (Pre-setup #4, tanpa kapabilitas Handover) sebagai pembanding penerima.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu Accept dan Decline pada ASG-2026-0120 (Pre-setup #19 dan #20) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi absence atas notifikasi in-app memakai baseline badge Bell icon per penerima yang dicatat sebelum pemicu, anchor positif (penerima sah menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_GM_PASSWORD`, `FA_APPROVERBA_PASSWORD`, `FA_ASSIGNEE_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-242: Notifikasi assignment_declined diterima: Assignee klik Decline

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Acceptance
2. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Assignee Siti Rahmawati (Pre-setup #12, sesi API), klik Decline pada halaman acceptance ASG-2026-0120 hingga penolakan tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Assignment was declined"` dan Body `"Siti Rahmawati declined Laptop - 1 (AST-2024-0067)."` (dari template `"[Assignee Name] declined [Asset Name] ([Asset ID])."`)
10. Verifikasi icon `close-circle-line` dengan severity `danger` pada item
11. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
12. Klik judul item tersebut (bukan tombol)
13. Verifikasi halaman tujuan `/fams/transactions-assignment/ASG-2026-0120` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-243: Notifikasi assignment_accepted diterima: Assignee klik Accept, status Waiting for Handover

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Acceptance
16. Ganti akun: logout, lalu login sebagai Group Manager (Gedung A) (Pre-setup #3) dengan `Spectra.env.FA_GM_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Group Manager sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Assignee Siti Rahmawati (Pre-setup #12, sesi API), klik Accept pada halaman acceptance ASG-2026-0120 (F-ASSIGN-11 langkah 3; F-ASSIGN-15) hingga status Waiting for Handover tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Group Manager bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Assignment was accepted"` dan Body `"Siti Rahmawati accepted Laptop - 1 (AST-2024-0067)."` (dari template `"[Assignee Name] accepted [Asset Name] ([Asset ID])."`)
25. Verifikasi icon `time-line` dengan severity `primary` pada item
26. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
27. Klik `[Detail]` pada item tersebut
28. Verifikasi halaman tujuan `/fams/transactions-assignment/ASG-2026-0120` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-406: assignment_accepted tidak diterima pemegang Approver tanpa kapabilitas Handover

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Acceptance
31. Ganti akun: logout, lalu login sebagai Approver (Borrowing & Assignment, Gedung A) (Pre-setup #4) dengan `Spectra.env.FA_APPROVERBA_PASSWORD`, lalu buka Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Approver (Borrowing & Assignment) sebagai baseline (0 bila badge tidak tampil)
33. Dari akun Assignee Siti Rahmawati (Pre-setup #12, sesi API), klik Accept pada halaman acceptance ASG-2026-0120 hingga status Waiting for Handover tersimpan
34. Ganti akun: logout, lalu login sebagai Group Manager (Gedung A) (Pre-setup #3) dengan `Spectra.env.FA_GM_PASSWORD`, lalu buka Fixed Asset > Dashboard
35. Klik Bell icon
36. Verifikasi item `"Assignment was accepted"` tampil pada Dropdown Panel Group Manager (anchor positif)
37. Ganti akun: logout, lalu login sebagai Approver (Borrowing & Assignment, Gedung A) (Pre-setup #4) dengan `Spectra.env.FA_APPROVERBA_PASSWORD`, lalu buka Fixed Asset > Dashboard
38. Tunggu 5 detik tanpa memuat ulang halaman
39. Klik Bell icon
40. Verifikasi Dropdown Panel Approver (Borrowing & Assignment) tampil
41. Verifikasi item `"Assignment was accepted"` tidak tampil pada Dropdown Panel Approver (Borrowing & Assignment)
42. Verifikasi badge Bell icon Approver (Borrowing & Assignment) sama dengan baseline langkah 32 (tidak bertambah)

### TC-FA-NOTIF-407: assignment_declined hanya diterima PIC admin dan tidak dikirim ke penerima lain

43. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Acceptance
44. Ganti akun: logout, lalu login sebagai Group Manager (Gedung A) (Pre-setup #3) dengan `Spectra.env.FA_GM_PASSWORD`, lalu buka Fixed Asset > Dashboard
45. Catat jumlah pada badge Bell icon Group Manager sebagai baseline (0 bila badge tidak tampil)
46. Dari akun Assignee Siti Rahmawati (Pre-setup #12, sesi API), klik Decline pada halaman acceptance ASG-2026-0120 hingga penolakan tersimpan
47. Ganti akun: logout, lalu login sebagai Asset Admin (Gedung A) (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
48. Klik Bell icon
49. Verifikasi item `"Assignment was declined"` dengan Body `"Siti Rahmawati declined Laptop - 1 (AST-2024-0067)."` tampil pada Dropdown Panel PIC admin (anchor positif)
50. Ganti akun: logout, lalu login sebagai Group Manager (Gedung A) (Pre-setup #3) dengan `Spectra.env.FA_GM_PASSWORD`, lalu buka Fixed Asset > Dashboard
51. Tunggu 5 detik tanpa memuat ulang halaman
52. Klik Bell icon
53. Verifikasi Dropdown Panel Group Manager tampil
54. Verifikasi item `"Assignment was declined"` tidak tampil pada Dropdown Panel Group Manager
55. Verifikasi badge Bell icon Group Manager sama dengan baseline langkah 45 (tidak bertambah)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30, 43 (penyiapan kondisi data lewat fixture BE); langkah 16, 31, 34, 37, 44, 47, 50 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17, 32, 45 (pencatatan baseline badge Bell icon (S-12)); langkah 38, 51 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (55 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Blok TC-FA-NOTIF-406 dan 407 mengubah akun dengan langkah eksplisit; anchor positif (penerima sah menerima item) mendahului asersi absence. Asersi absence dibaca setelah login ulang akun negatif sesudah pemicu, sehingga daftar notifikasi dimuat dari server.
- Langkah 40 dan 53 (Dropdown Panel tampil) adalah asersi tambahan di luar Expected TC sebagai anchor permukaan sebelum asersi absence (S-03; bagian 8b butir 2).
- Spec 061 memuat tahap decline dan accepted atas ASG-2026-0120 beserta penerima yang tidak berhak; tahap persetujuan ada di spec 059 dan penerimaan Assignee di spec 060, dibedakan karena status awal transaksi dan akun penerima berbeda.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-406 dan 407 menulis "Klik Bell icon sebagai ..." berurutan tanpa menyebut pencatatan badge awal; spec mencatat baseline akun negatif sebelum pemicu untuk klausa "badge tidak bertambah".
