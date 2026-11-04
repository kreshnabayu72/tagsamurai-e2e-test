---
id: TC-FA-NOTIF-E2E-070-perubahan-akses-auto-reverted-edit-crud-dan-remove-peran
title: "Penerimaan Notifikasi Perubahan Akses Auto-Reverted: Edit CRUD dan Remove Peran pada Total Control dan Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-267
  - TC-FA-NOTIF-268
  - TC-FA-NOTIF-269
  - TC-FA-NOTIF-270
coverage:
  web: automated
---
# Penerimaan Notifikasi Perubahan Akses Auto-Reverted: Edit CRUD dan Remove Peran pada Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Citra Lestari (target perubahan akses) | #14 | `targetCitra_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TARGETCITRA_PASSWORD` | `Fixture.fixedAssetNotification.targetCitra` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Total Control (Admin Alpha) (Pre-setup #1, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Edit CRUD peran individual dan Remove baris peran Citra Lestari.
- Login akun aktor pertama (Citra Lestari (target perubahan akses), Pre-setup #14) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): Citra Lestari (Pre-setup #14, target perubahan akses; pemegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A); Admin Alpha Pre-setup #1 (aktor, nama tampil pada Body). Peran Citra (Total Control, Read Only, Group Manager) diatur lewat fixture BE pada langkah penyiapan tiap blok; pemulihan di hook `before` dan `after`.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu Edit CRUD dan Remove baris peran pada Citra Lestari (Pre-setup #14) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10); format tanggal item mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TARGETCITRA_PASSWORD`, `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-267: access_total_control_auto_reverted varian Edit CRUD diterima

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari memegang Total Control, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Edit CRUD peran individual Citra Lestari yang menyimpangkan pola Total Control hingga perubahan tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Your Total Control access was removed"` dan Body `"Admin Alpha removed your Total Control access on 18/06/26."` (dari template `"[Admin Name] removed your Total Control access on [Date]."`)
10. Verifikasi icon `information-line` dengan severity `warning` pada item
11. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
12. Klik judul item tersebut (bukan tombol)
13. Verifikasi halaman tujuan `/fams/profile` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-268: access_total_control_auto_reverted varian Remove peran diterima

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari memegang Total Control dengan baris peran
16. Muat ulang halaman Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Remove baris peran milik target Total Control hingga perubahan tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Your Total Control access was removed"` dan Body `"Admin Alpha removed your Total Control access on 18/06/26."` (dari template `"[Admin Name] removed your Total Control access on [Date]."`)
25. Verifikasi icon `information-line` dengan severity `warning` pada item
26. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
27. Klik judul item tersebut (bukan tombol)
28. Verifikasi halaman tujuan `/fams/profile` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-269: access_read_only_auto_reverted varian Edit CRUD diterima

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari memegang Read Only
31. Muat ulang halaman Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
33. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Edit CRUD peran individual Citra Lestari yang menyimpangkan pola Read Only hingga perubahan tersimpan
34. Klik Bell icon
35. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 32
36. Verifikasi item baru berada di posisi teratas Dropdown Panel
37. Verifikasi Title item baru bold
38. Verifikasi dot Unread tampil pada item baru
39. Verifikasi item menampilkan Title `"Your Read Only access was removed"` dan Body `"Admin Alpha removed your Read Only access on 18/06/26."` (dari template `"[Admin Name] removed your Read Only access on [Date]."`)
40. Verifikasi icon `information-line` dengan severity `warning` pada item
41. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
42. Klik judul item tersebut (bukan tombol)
43. Verifikasi halaman tujuan `/fams/profile` terbuka
44. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 35

### TC-FA-NOTIF-270: access_read_only_auto_reverted varian Remove peran diterima

45. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari memegang Read Only dengan baris peran
46. Muat ulang halaman Fixed Asset > Dashboard
47. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
48. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Remove baris peran milik target Read Only hingga perubahan tersimpan
49. Klik Bell icon
50. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 47
51. Verifikasi item baru berada di posisi teratas Dropdown Panel
52. Verifikasi Title item baru bold
53. Verifikasi dot Unread tampil pada item baru
54. Verifikasi item menampilkan Title `"Your Read Only access was removed"` dan Body `"Admin Alpha removed your Read Only access on 18/06/26."` (dari template `"[Admin Name] removed your Read Only access on [Date]."`)
55. Verifikasi icon `information-line` dengan severity `warning` pada item
56. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
57. Klik judul item tersebut (bukan tombol)
58. Verifikasi halaman tujuan `/fams/profile` terbuka
59. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 50

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30, 45 (penyiapan kondisi data lewat fixture BE); langkah 2, 17, 32, 47 (pencatatan baseline badge Bell icon (S-12)); langkah 16, 31 dan 46 (muat ulang halaman Fixed Asset > Dashboard sesudah pemulihan seed dan sebelum pencatatan baseline; juga menutup Dropdown Panel blok sebelumnya (S-09, S-14)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (59 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
