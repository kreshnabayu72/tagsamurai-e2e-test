---
id: TC-FA-NOTIF-E2E-085-tag-report-declined-dan-canceled
title: "Notifikasi TAG Report Declined dan TAG Report Canceled: Decline Report, Cancel Report, dan Pembatal Tidak Menerima"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-476
  - TC-FA-NOTIF-479
  - TC-FA-NOTIF-477
coverage:
  web: automated
---

# Notifikasi TAG Report Declined dan TAG Report Canceled: Decline Report, Cancel Report, dan Pembatal Tidak Menerima

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena penerima berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-476, 479 | Manage asset & TAG Update Gedung A (Dewi Anggraini, pelapor) | #35 | `manageAssetTagGedungA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MATAGA_PASSWORD` | `Fixture.fixedAssetNotification.manageAssetTagGedungA` |
  | TC-FA-NOTIF-477 | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |

- Login akun aktor pertama (Dewi Anggraini, Pre-setup #35) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Total Control (Pre-setup #1, `Spectra.env.FA_TC_PASSWORD`) untuk Decline Report dan Cancel Report pada TC-FA-NOTIF-476 dan 479, serta Dewi Anggraini (Pre-setup #35) untuk Cancel Report pada TC-FA-NOTIF-477.
- Data Pre-setup (tetap di environment): Proyektor AST-2024-0150 dengan Tag `RF-00150` (Pre-setup #24 dan #38). Laporan terbuka pada `RF-00150` (dibuat Dewi Anggraini untuk blok TC-FA-NOTIF-476 dan 479; laporan terbuka untuk blok TC-FA-NOTIF-477) diberikan fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); seed dipulihkan fixture BE pemulih (butir "Fixture BE pemulih seed notifikasi dan transaksi") di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu Decline Report dan Cancel Report dengan alasan terisi lewat sesi API aktor; membaca jumlah notifikasi per penerima dan per Title serta nilai badge (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Asersi absence atas notifikasi in-app memakai baseline per penerima (kemampuan baca BE) yang dicatat sebelum pemicu, anchor positif (pelapor Dewi Anggraini menerima item hasil pemicu yang sama), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" sebelum tiap pembacaan BE absence; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu Decline Report dan Cancel Report pada `RF-00150` (AST-2024-0150) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_MATAGA_PASSWORD` dan `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-476: tag_report_declined diterima pelapor

1. Muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah item `"TAG report declined"` dan nilai badge Bell icon milik Dewi Anggraini (baseline) lewat fixture BE
3. Atur `RF-00150` memiliki laporan terbuka yang dibuat Dewi Anggraini lewat fixture BE
4. Dari akun Total Control (Pre-setup #1, sesi API), Decline Report pada `RF-00150` dengan alasan terisi hingga laporan tertutup tersimpan
5. Muat ulang halaman Fixed Asset > Dashboard
6. Klik Bell icon sebagai pelapor
7. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Dewi Anggraini bertambah 1 dari baseline
8. Verifikasi item baru berada di posisi teratas Dropdown Panel
9. Verifikasi Title item teratas bold
10. Verifikasi dot Unread tampil pada item teratas
11. Verifikasi item teratas dengan Title `"TAG report declined"`
12. Verifikasi Body item teratas `"Your report on RF-00150 (AST-2024-0150) was declined."`
13. Verifikasi item teratas memakai icon `close-circle-line` dengan severity `danger`
14. Verifikasi tombol `[Mark as Read]` tampil pada item teratas
15. Verifikasi tombol `[Detail]` tidak tampil pada item teratas
16. Klik judul item notifikasi teratas (bukan tombol)
17. Verifikasi halaman berpindah ke `/fams/asset/detail/AST-2024-0150`

### TC-FA-NOTIF-479: tag_report_canceled diterima pelapor, pembatal admin lain

18. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24 dan #38) lewat fixture BE
19. Atur `RF-00150` memiliki laporan terbuka yang dibuat Dewi Anggraini lewat fixture BE
20. Catat jumlah item `"TAG report canceled"` milik Dewi Anggraini dan milik Total Control Pre-setup #1 (baseline) lewat fixture BE
21. Dari akun Total Control (Pre-setup #1, sesi API), Cancel Report pada `RF-00150` dengan alasan terisi hingga laporan tertutup tersimpan
22. Muat ulang halaman Fixed Asset > Dashboard
23. Klik Bell icon sebagai pelapor
24. Verifikasi item baru berada di posisi teratas Dropdown Panel
25. Verifikasi (kemampuan baca BE) jumlah item `"TAG report canceled"` milik Dewi Anggraini bertambah tepat 1 dari baseline
26. Verifikasi item teratas berstatus Unread
27. Verifikasi item teratas dengan Title `"TAG report canceled"`
28. Verifikasi Body item teratas `"The report on RF-00150 (AST-2024-0150) was canceled by Admin Alpha."` memuat nama lengkap pembatal
29. Tunggu 5 detik tanpa memuat ulang halaman
30. Verifikasi (kemampuan baca BE) akun Total Control Pre-setup #1 (pembatal) memuat item seed Pre-setup #17 (jumlah item agregat awal akun sama dengan baseline langkah 20; anchor absence akun sendiri)
31. Verifikasi jumlah item `"TAG report canceled"` milik Total Control Pre-setup #1 (pembatal) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-477: tag_report_canceled diterima Total Control

32. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24 dan #38) lewat fixture BE
33. Atur `RF-00150` memiliki laporan terbuka lewat fixture BE
34. Catat jumlah item `"TAG report canceled"` dan nilai badge Bell icon milik Total Control Pre-setup #1 (baseline) lewat fixture BE
35. Dari akun Dewi Anggraini (Pre-setup #35, sesi API), Cancel Report pada `RF-00150` dengan alasan terisi hingga laporan tertutup tersimpan
36. Logout, lalu login sebagai Total Control (Pre-setup #1), lalu buka Fixed Asset > Dashboard
37. Klik Bell icon sebagai penerima
38. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Total Control Pre-setup #1 bertambah 1 dari baseline
39. Verifikasi item baru berada di posisi teratas Dropdown Panel
40. Verifikasi Title item teratas bold
41. Verifikasi dot Unread tampil pada item teratas
42. Verifikasi item teratas dengan Title `"TAG report canceled"`
43. Verifikasi Body item teratas `"The report on RF-00150 (AST-2024-0150) was canceled by Dewi Anggraini."`
44. Verifikasi item teratas memakai icon `information-line` dengan severity `warning`
45. Verifikasi tombol `[Mark as Read]` tampil pada item teratas
46. Verifikasi tombol `[Detail]` tidak tampil pada item teratas
47. Klik judul item notifikasi teratas (bukan tombol)
48. Verifikasi halaman berpindah ke `/fams/tag?tab=paired`

## Notes

- Langkah penghubung (S-03): langkah 5, 22 (muat ulang agar notifikasi hasil pemicu termuat); langkah 18 dan 32 (pulihkan seed antar blok); langkah 2, 20, dan 34 (baseline per TC); langkah 3, 19, dan 33 (precondition TC lewat fixture BE); langkah 36 (ganti akun dan buka Fixed Asset > Dashboard).
- Langkah 29 (jendela 5 detik tanpa memuat ulang halaman sebelum pembacaan BE absence pembatal, bagian 6) adalah langkah penghubung tanpa Verifikasi (S-03). Baseline badge (langkah 2 dan 34) dan pembacaan sesudah pemicu (langkah 7 dan 38) sama-sama lewat kemampuan baca BE (bagian 8b butir 10).
- Langkah 1 (muat ulang halaman sebelum baseline blok pertama, bagian 8b butir 10) adalah langkah penghubung (S-03). Langkah 30 (Verifikasi item seed Pre-setup #17 akun #1 dan jumlah agregat sama dengan baseline) adalah asersi tambahan (S-03; bagian 8b butir 2): anchor absence akun pembatal memakai seed milik akun itu sendiri, bukan item hasil pemicu. Expected 'badge bertambah 1' pada TC-FA-NOTIF-476 dan 477 diasersi lewat kemampuan baca BE (langkah 7 dan 38); nilai badge pada UI tidak diasersi terpisah karena baseline dan pembacaan memakai sumber baca yang sama (bagian 8b butir 10).
- Urutan blok: TC-FA-NOTIF-476, 479, lalu 477, supaya dua blok pelapor berurutan dan ganti akun hanya satu kali.
- Asersi absence langkah 31 memakai anchor positif: pelapor menerima item hasil pemicu yang sama (langkah 24 sampai 28), dan jumlah dibandingkan dengan baseline pembatal (bagian 8b butir 2 dan 10).
- Nama lengkap pembatal pada langkah 28 (`Admin Alpha`) diambil dari keterangan akun Pre-setup #1 pada Tabel Data Uji Pre-setup TC.
- Pembagian per TC: TC-FA-NOTIF-476 (langkah 1 sampai 17), TC-FA-NOTIF-479 (langkah 18 sampai 31), TC-FA-NOTIF-477 (langkah 32 sampai 48).
- Alasan melewati ambang sekitar 35 langkah (48 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan seed dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari pemecahan satu klausa per Verifikasi (S-01).
- Temuan untuk QA:
  - TC-FA-NOTIF-479 menulis Body dengan placeholder `[User Name]` tanpa nilai; spec memakai nama lengkap akun Pre-setup #1 dari Tabel Data Uji Pre-setup (`Admin Alpha`).
  - TC-FA-NOTIF-479 Expected butir c ("pembatal tidak menerima notifikasi ini") tidak menyebut cara mengamatinya; spec membaca lewat fixture BE.
  - TC-FA-NOTIF-476 Expected butir e tidak menyebut status baca setelah klik; tidak diasersi.
  - Kolom Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
