---
id: TC-FA-NOTIF-E2E-083-tag-replacement-needed-satu-notifikasi-per-asset-name
title: "Notifikasi TAG Replacement Needed: Satu Notifikasi per Asset Name per Penerima dan Scope Pemegang Update"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-449
  - TC-FA-NOTIF-450
  - TC-FA-NOTIF-451
  - TC-FA-NOTIF-452
coverage:
  web: automated
---

# Notifikasi TAG Replacement Needed: Satu Notifikasi per Asset Name per Penerima dan Scope Pemegang Update

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role pada TC-FA-NOTIF-452 karena ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-449, 450, 451, 452 (blok pertama) | Manage asset & TAG Update Gedung A (Dewi Anggraini) | #35 | `manageAssetTagGedungA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MATAGA_PASSWORD` | `Fixture.fixedAssetNotification.manageAssetTagGedungA` |
  | TC-FA-NOTIF-452 | Manage asset & TAG Update Gedung B saja | #36 | `manageAssetTagGedungB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MATAGB_PASSWORD` | `Fixture.fixedAssetNotification.manageAssetTagGedungB` |
  | TC-FA-NOTIF-452 | Read Only | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | `Fixture.fixedAssetNotification.readOnly` |
  | TC-FA-NOTIF-452 | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |

- Login akun aktor pertama (Dewi Anggraini, Pre-setup #35) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Total Control tanpa Transaction Role (Pre-setup #26, `totalControlNoRole_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TCNOROLE_PASSWORD`, `Fixture.fixedAssetNotification.totalControlNoRole`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Data Pre-setup (tetap di environment): Asset Name `Forklift 5 Ton` (1 aset, AST-2024-0204) dan `Excavator 20 Ton` (3 aset, AST-2024-0201 sampai AST-2024-0203), semua ber-Tag RFID Paired di Gedung A (Pre-setup #37). TAG Type diubah dari RFID ke NFC lewat Settings > Asset Name oleh pemicu; fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) mengembalikan TAG Type ke RFID dan menghapus notifikasi Tag di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah mengubah TAG Type Asset Name `Forklift 5 Ton` dan `Excavator 20 Ton` (Pre-setup #37) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu perubahan TAG Type lewat sesi API aktor; membaca jumlah notifikasi per penerima dan per Title serta nilai badge (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Asersi absence atas notifikasi in-app memakai baseline per penerima (kemampuan baca BE) yang dicatat sebelum pemicu, anchor positif (akun Pre-setup #35 menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" sebelum tiap pembacaan BE absence; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_MATAGA_PASSWORD`, `FA_MATAGB_PASSWORD`, `FA_RO_PASSWORD`, `FA_TC_PASSWORD`, dan `FA_TCNOROLE_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-449: tag_replacement_needed untuk 1 aset

1. Muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah item `"TAG replacement needed"` dan nilai badge Bell icon milik Dewi Anggraini (baseline) lewat fixture BE
3. Dari akun Total Control (Pre-setup #26, sesi API), simpan perubahan TAG Type Forklift 5 Ton dari RFID ke NFC di Settings > Asset Name hingga tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai penerima
6. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Dewi Anggraini bertambah 1 dari baseline
7. Verifikasi item baru berada di posisi teratas Dropdown Panel
8. Verifikasi Title item baru bold
9. Verifikasi item baru memiliki dot Unread
10. Verifikasi item teratas dengan Title `"TAG replacement needed"` dan Body `"1 Forklift 5 Ton asset needs TAG replacement."`
11. Verifikasi item teratas memakai icon `time-line` dengan severity `warning`
12. Verifikasi tombol `[Mark as Read]` tampil dan `[Detail]` tidak tampil pada item teratas
13. Klik judul item notifikasi teratas (bukan tombol)
14. Verifikasi halaman berpindah ke `/fams/tag?tab=paired`
15. Klik Bell icon
16. Verifikasi item `"TAG replacement needed"` tetap berstatus Unread (status baca tidak berubah)

### TC-FA-NOTIF-450: tag_replacement_needed bentuk jamak untuk 3 aset

17. Pulihkan seed, TAG Type, dan transaksi (Pre-setup #17 sampai #24 dan #37) lewat fixture BE
18. Catat jumlah item `"TAG replacement needed"` dan nilai badge Bell icon milik Dewi Anggraini (baseline) lewat fixture BE
19. Dari akun Total Control (Pre-setup #26, sesi API), simpan perubahan TAG Type Excavator 20 Ton dari RFID ke NFC di Settings > Asset Name hingga tersimpan
20. Muat ulang halaman Fixed Asset > Dashboard
21. Klik Bell icon sebagai penerima
22. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Dewi Anggraini bertambah 1 dari baseline
23. Verifikasi item baru berada di posisi teratas Dropdown Panel
24. Verifikasi Title item baru bold
25. Verifikasi item baru memiliki dot Unread
26. Verifikasi item teratas dengan Title `"TAG replacement needed"` dan Body `"3 Excavator 20 Ton assets need TAG replacement."`
27. Verifikasi item teratas memakai icon `time-line` dengan severity `warning`
28. Verifikasi tombol `[Mark as Read]` tampil dan `[Detail]` tidak tampil pada item teratas
29. Klik judul item notifikasi teratas (bukan tombol)
30. Verifikasi halaman berpindah ke `/fams/tag?tab=paired`
31. Klik Bell icon
32. Verifikasi item `"TAG replacement needed"` tetap berstatus Unread (status baca tidak berubah)

### TC-FA-NOTIF-451: satu notifikasi per Asset Name per penerima

33. Pulihkan seed, TAG Type, dan transaksi (Pre-setup #17 sampai #24 dan #37) lewat fixture BE
34. Catat jumlah item `"TAG replacement needed"` milik Dewi Anggraini (baseline) lewat fixture BE
35. Dari akun Total Control (Pre-setup #26, sesi API), simpan perubahan TAG Type Forklift 5 Ton dari RFID ke NFC hingga tersimpan
36. Dari akun Total Control (Pre-setup #26, sesi API), simpan perubahan TAG Type Excavator 20 Ton dari RFID ke NFC hingga tersimpan
37. Muat ulang halaman Fixed Asset > Dashboard
38. Klik Bell icon sebagai penerima
39. Verifikasi (kemampuan baca BE) jumlah item `"TAG replacement needed"` Unread bertambah tepat 2 dari baseline (bukan 4)
40. Verifikasi satu notifikasi dengan Body `"1 Forklift 5 Ton asset needs TAG replacement."`
41. Verifikasi satu notifikasi dengan Body `"3 Excavator 20 Ton assets need TAG replacement."`

### TC-FA-NOTIF-452: hanya pemegang Update dalam scope group aset yang menerima

42. Pulihkan seed, TAG Type, dan transaksi (Pre-setup #17 sampai #24 dan #37) lewat fixture BE
43. Catat jumlah item `"TAG replacement needed"` milik akun Pre-setup #35, #36, #2, dan #1 (baseline) lewat fixture BE
44. Dari akun Total Control (Pre-setup #26, sesi API), simpan perubahan TAG Type Excavator 20 Ton dari RFID ke NFC hingga tersimpan
45. Muat ulang halaman Fixed Asset > Dashboard
46. Klik Bell icon sebagai akun Pre-setup #35
47. Verifikasi (kemampuan baca BE) jumlah item `"TAG replacement needed"` milik akun Pre-setup #35 bertambah tepat 1 dari baseline
48. Verifikasi item `"TAG replacement needed"` berstatus Unread pada Dropdown Panel akun Pre-setup #35
49. Logout, lalu login sebagai Manage asset & TAG Update Gedung B (Pre-setup #36), lalu buka Fixed Asset > Dashboard
50. Klik Bell icon sebagai akun Pre-setup #36
51. Verifikasi Dropdown Panel akun Pre-setup #36 termuat (anchor permukaan untuk pembacaan BE absence)
52. Tunggu 5 detik tanpa memuat ulang halaman
53. Verifikasi (kemampuan baca BE) jumlah item `"TAG replacement needed"` milik akun Pre-setup #36 sama dengan baseline (tidak menerima)
54. Logout, lalu login sebagai Read Only (Pre-setup #2), lalu buka Fixed Asset > Dashboard
55. Klik Bell icon sebagai akun Pre-setup #2
56. Verifikasi Dropdown Panel akun Pre-setup #2 termuat (anchor permukaan untuk pembacaan BE absence)
57. Tunggu 5 detik tanpa memuat ulang halaman
58. Verifikasi (kemampuan baca BE) jumlah item `"TAG replacement needed"` milik akun Pre-setup #2 sama dengan baseline (tidak menerima)
59. Logout, lalu login sebagai Total Control (Pre-setup #1), lalu buka Fixed Asset > Dashboard
60. Klik Bell icon sebagai akun Pre-setup #1
61. Verifikasi (kemampuan baca BE) jumlah item `"TAG replacement needed"` milik akun Pre-setup #1 bertambah tepat 1 dari baseline
62. Verifikasi item `"TAG replacement needed"` berstatus Unread pada Dropdown Panel akun Pre-setup #1

## Notes

- Langkah penghubung (S-03): langkah 4, 20, 37, dan 45 (muat ulang agar notifikasi hasil pemicu termuat); langkah 17, 33, dan 42 (pulihkan seed antar blok); langkah 2, 18, 34, dan 43 (baseline per TC); langkah 15 dan 31 (buka ulang Bell icon sesudah navigasi untuk mengamati status baca); langkah 49, 54, dan 59 (ganti akun dan buka Fixed Asset > Dashboard).
- Langkah 52 dan 57 (jendela 5 detik tanpa memuat ulang halaman sebelum pembacaan BE absence, bagian 6) adalah langkah penghubung tanpa Verifikasi (S-03).
- Asersi absence langkah 53 dan 58 memakai anchor positif: akun Pre-setup #35 menerima notifikasi hasil pemicu yang sama (langkah 47), dan jumlah dibandingkan dengan baseline per penerima (bagian 8b butir 2 dan 10).
- Baseline dan pembacaan badge sesudah pemicu pada TC-FA-NOTIF-449 dan 450 sama-sama lewat kemampuan baca BE (langkah 2 dan 6; langkah 18 dan 22), supaya sumber baca seragam (bagian 8b butir 10); item dibaca pada Dropdown Panel.
- Langkah 1 (muat ulang halaman sebelum baseline blok pertama, bagian 8b butir 10), langkah 51 dan 56 (Verifikasi Dropdown Panel termuat sesudah klik Bell icon akun #36 dan #2) adalah langkah penghubung/anchor permukaan (S-03). Badge Bell icon pada UI untuk Expected 'badge bertambah 1' di TC-FA-NOTIF-449 dan 450 diasersi lewat kemampuan baca BE (langkah 6 dan 22); nilai badge pada UI tidak diasersi terpisah karena baseline dan pembacaan memakai sumber baca yang sama (bagian 8b butir 10).
- Urutan ganti akun pada TC-FA-NOTIF-452 mengikuti urutan TC (#35, #36, #2, #1).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruh blok satu topik (event `tag_replacement_needed`), tiap blok berdiri sendiri karena diawali pemulihan seed dan TAG Type, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected TC-FA-NOTIF-449 dan 450 masing-masing memuat lima butir asersi tampilan, dan TC-FA-NOTIF-452 memuat empat akun.
- Pembagian per TC: TC-FA-NOTIF-449 (langkah 1 sampai 16), TC-FA-NOTIF-450 (langkah 17 sampai 32), TC-FA-NOTIF-451 (langkah 33 sampai 41), TC-FA-NOTIF-452 (langkah 42 sampai 62).
- Temuan untuk QA:
  - TC-FA-NOTIF-449, 450, dan 451 menulis pemicu "Save perubahan TAG Type" tanpa menyebut akun pelaku; spec memakai sesi API Total Control Pre-setup #26 seperti TC-FA-NOTIF-452.
  - Expected TC-FA-NOTIF-449 dan 450 butir e ("tanpa mengubah status baca") tidak menyebut langkah observasi status baca; spec membuka ulang Bell icon sesudah navigasi (langkah 15 dan 31).
  - Template Body pada Expected TC-FA-NOTIF-449 dan 450 memuat template dengan tanda kutip bertingkat; spec hanya menyalin teks Body hasil render.
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
