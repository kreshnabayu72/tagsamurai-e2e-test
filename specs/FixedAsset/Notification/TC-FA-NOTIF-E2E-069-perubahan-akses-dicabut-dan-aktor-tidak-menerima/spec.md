---
id: TC-FA-NOTIF-E2E-069-perubahan-akses-dicabut-dan-aktor-tidak-menerima
title: "Penerimaan Notifikasi Perubahan Akses Dicabut: Total Control, Read Only, Group Manager, dan Kejadian Berulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-264
  - TC-FA-NOTIF-265
  - TC-FA-NOTIF-266
  - TC-FA-NOTIF-378
coverage:
  web: automated
---
# Penerimaan Notifikasi Perubahan Akses Dicabut: Total Control, Read Only, Group Manager, dan Kejadian Berulang

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Citra Lestari (target perubahan akses) | #14 | `targetCitra_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TARGETCITRA_PASSWORD` | `Fixture.fixedAssetNotification.targetCitra` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Total Control (Admin Alpha) (Pre-setup #1, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Remove akses Citra Lestari di Settings > Role & Permission.
- Login akun aktor pertama (Citra Lestari (target perubahan akses), Pre-setup #14) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): Citra Lestari (Pre-setup #14, target perubahan akses; pemegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A); Admin Alpha Pre-setup #1 (aktor, nama tampil pada Body). Peran Citra (Total Control, Read Only, Group Manager) diatur lewat fixture BE pada langkah penyiapan tiap blok; pemulihan di hook `before` dan `after`.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu Remove akses Citra Lestari (Pre-setup #14) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10); format tanggal item mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TARGETCITRA_PASSWORD`, `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-264: access_total_control_removed diterima: Remove Total Control

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari memegang Total Control, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Remove Total Control Citra Lestari di Tab Total Control hingga perubahan tersimpan
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

### TC-FA-NOTIF-265: access_read_only_removed diterima: Remove Read Only

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari memegang Read Only
16. Muat ulang halaman Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Remove Read Only Citra Lestari di Tab Read Only hingga perubahan tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Your Read Only access was removed"` dan Body `"Admin Alpha removed your Read Only access on 18/06/26."` (dari template `"[Admin Name] removed your Read Only access on [Date]."`)
25. Verifikasi icon `information-line` dengan severity `warning` pada item
26. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
27. Klik judul item tersebut (bukan tombol)
28. Verifikasi halaman tujuan `/fams/profile` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-266: access_group_manager_removed diterima: Remove Group Manager manual

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari Group Manager Gedung A
31. Muat ulang halaman Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
33. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Remove Group Manager manual Citra Lestari (Gedung A) di Tab Group Manager hingga perubahan tersimpan
34. Klik Bell icon
35. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 32
36. Verifikasi item baru berada di posisi teratas Dropdown Panel
37. Verifikasi Title item baru bold
38. Verifikasi dot Unread tampil pada item baru
39. Verifikasi item menampilkan Title `"You are no longer Group Manager for Gedung A"` (dari template `"You are no longer Group Manager for [Group Name]"`) dan Body `"Admin Alpha removed your Group Manager status for Gedung A on 18/06/26."` (dari template `"[Admin Name] removed your Group Manager status for [Group Name] on [Date]."`)
40. Verifikasi icon `information-line` dengan severity `warning` pada item
41. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
42. Klik judul item tersebut (bukan tombol)
43. Verifikasi halaman tujuan `/fams/profile` terbuka
44. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 35

### TC-FA-NOTIF-378: access_total_control_removed kejadian kedua pada user yang sama menghasilkan notifikasi baru

45. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari pernah di-Remove Total Control dan notifikasi pertamanya Read
46. Muat ulang halaman Fixed Asset > Dashboard
47. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
48. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), beri Total Control kepada Citra Lestari lalu Remove Total Control untuk kedua kalinya hingga perubahan tersimpan
49. Klik Bell icon
50. Verifikasi badge Bell icon Citra Lestari bertambah 1 dari baseline langkah 47
51. Verifikasi item baru `"Your Total Control access was removed"` tampil di posisi teratas Dropdown Panel
52. Verifikasi item baru tersebut Unread dengan dot Unread
53. Verifikasi notifikasi pertama `"Your Total Control access was removed"` tetap Read (tanpa dot Unread)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30, 45 (penyiapan kondisi data lewat fixture BE); langkah 2, 17, 32, 47 (pencatatan baseline badge Bell icon (S-12)); langkah 16, 31 dan 46 (muat ulang halaman Fixed Asset > Dashboard sesudah pemulihan seed dan sebelum pencatatan baseline; juga menutup Dropdown Panel blok sebelumnya (S-09, S-14)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (53 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Blok TC-FA-NOTIF-378: Expected (a) "notifikasi baru Unread muncul" diasersi lewat selisih badge 1 dan item teratas Unread (S-03); notifikasi pertama dibedakan sebagai item kedua berjudul sama tanpa dot Unread.
- Blok TC-FA-NOTIF-266: TC menulis "satu notifikasi per group yang dilepas" pada pemicu; yang dilepas hanya Gedung A, sehingga selisih badge 1 dan satu item (S-03).
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-264 sampai 266 menyebut aktor Admin Alpha hanya lewat Body; spec memakai Total Control Pre-setup #1 lewat sesi API.
  - TC-FA-NOTIF-378 menyebut notifikasi pertama Read tanpa langkah yang membuatnya Read; spec membentuknya lewat fixture BE pada langkah penyiapan.
