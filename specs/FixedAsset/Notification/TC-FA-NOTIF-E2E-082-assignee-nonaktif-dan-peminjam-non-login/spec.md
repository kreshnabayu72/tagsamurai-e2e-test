---
id: TC-FA-NOTIF-E2E-082-assignee-nonaktif-dan-peminjam-non-login
title: "Assignee Nonaktif dan Peminjam Non-login: Penerima Pengganti Atasan Assignee dan Pengguna Perwakilan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-387
  - TC-FA-NOTIF-388
  - TC-FA-NOTIF-389
  - TC-FA-NOTIF-398
coverage:
  web: automated
---

# Assignee Nonaktif dan Peminjam Non-login: Penerima Pengganti Atasan Assignee dan Pengguna Perwakilan

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena penerima berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-387, 388, 389 | Atasan assignee Siti Rahmawati | #28 | `atasanSiti_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ATASANSITI_PASSWORD` | `Fixture.fixedAssetNotification.atasanSiti` |
  | TC-FA-NOTIF-398 | Pengguna perwakilan peminjam non-login Joko Prasetyo | #30 | `perwakilanJoko_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_PERWAKILANJOKO_PASSWORD` | `Fixture.fixedAssetNotification.perwakilanJoko` |

- Login akun aktor pertama (atasan assignee, Pre-setup #28) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Asset Admin (Pre-setup #8, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- State yang diubah dan dipulihkan: Assignee Siti Rahmawati (Pre-setup #12) dinonaktifkan lewat fixture BE di hook `before` dan diaktifkan kembali di hook `after`; fixture BE pemulih seed dan transaksi (Pre-setup #17 sampai #24) juga memulihkan status akun #11/#12 (`suite.md`), sehingga tiap blok TC-FA-NOTIF-387, 388, dan 389 menonaktifkan Siti Rahmawati lagi sesudah pemulihan di langkah awal blok. Tiap blok memakai langkah awal "Pulihkan seed lalu atur <precondition TC> lewat fixture BE penyetel state sumber" (ASG-2026-0120: Verified menuju Waiting for Acceptance untuk TC-FA-NOTIF-387, Waiting for Acceptance lebih dari 48 jam untuk TC-FA-NOTIF-388, Waiting for Handover untuk TC-FA-NOTIF-389).
- Data Pre-setup (tetap di environment): ASG-2026-0120 (Laptop - 1 AST-2024-0067; Pre-setup #20 dan #24) untuk TC-FA-NOTIF-387, 388, 389; transaksi Borrow milik peminjam non-login Joko Prasetyo berstatus Ready for Verification dengan 1 aset Printer Lantai 1 (AST-2024-0160) di Gedung A > Lantai 1 > Ruang 101 (Pre-setup #30), dan akun #30 belum punya notifikasi. Keadaan awal per blok disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu verifikasi scan, bypass konfirmasi peminjam non-login, dan handover; menjalankan job auto-cancel Waiting for Acceptance (`F-ASSIGN-11` langkah 5); membaca daftar dan jumlah notifikasi per penerima, termasuk akun nonaktif Siti Rahmawati, per Title, nilai badge Bell icon, dan status transaksi (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Jendela amat notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6); dijalankan juga sebelum tiap pembacaan BE absence penerima nonaktif (langkah 8, 17, dan 26).
- Asersi handover ke pengguna perwakilan pada TC-FA-NOTIF-398 bersyarat pada Open Item #6 PRD (menunggu keputusan produk) dan dapat direvisi.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu verifikasi scan, job auto-cancel, handover, dan bypass konfirmasi pada ASG-2026-0120 (Pre-setup #20 dan #24) serta transaksi Borrow Joko Prasetyo (Pre-setup #30) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ATASANSITI_PASSWORD`, `FA_PERWAKILANJOKO_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-387: assignment_acceptance_required, Assignee nonaktif

1. Pulihkan seed lalu atur ASG-2026-0120 Verified menuju Waiting for Acceptance lewat fixture BE penyetel state sumber, lalu nonaktifkan kembali Siti Rahmawati (Pre-setup #12) lewat fixture BE (pemulih seed juga memulihkan status #11/#12, `suite.md`), lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah item `"Please accept your asset assignment"` milik akun Pre-setup #28 dan milik Siti Rahmawati (nonaktif) (baseline) lewat fixture BE
3. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan ASG-2026-0120 hingga status Waiting for Acceptance tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai akun Pre-setup #28
6. Verifikasi item `"Please accept your asset assignment"` tampil pada Dropdown Panel akun Pre-setup #28
7. Verifikasi (kemampuan baca BE) jumlah item `"Please accept your asset assignment"` milik akun Pre-setup #28 bertambah tepat 1 dari baseline
8. Tunggu 5 detik tanpa memuat ulang halaman
9. Verifikasi jumlah item `"Please accept your asset assignment"` milik Siti Rahmawati (nonaktif) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-388: assignment_acceptance_expired varian Assignee, Assignee nonaktif

10. Pulihkan seed lalu atur ASG-2026-0120 Waiting for Acceptance lebih dari 48 jam lewat fixture BE penyetel state sumber, lalu nonaktifkan kembali Siti Rahmawati (Pre-setup #12) lewat fixture BE (pemulih seed juga memulihkan status #11/#12, `suite.md`)
11. Catat jumlah item `"Assignment acceptance expired"` milik akun Pre-setup #28 dan milik Siti Rahmawati (nonaktif) (baseline) lewat fixture BE
12. Jalankan job terjadwal auto-cancel ASG-2026-0120 yang Waiting for Acceptance melewati batas 48 jam (`F-ASSIGN-11` langkah 5) hingga notifikasi tersimpan
13. Muat ulang halaman Fixed Asset > Dashboard
14. Klik Bell icon sebagai akun Pre-setup #28
15. Verifikasi item `"Assignment acceptance expired"` tampil pada Dropdown Panel akun Pre-setup #28
16. Verifikasi (kemampuan baca BE) jumlah item `"Assignment acceptance expired"` milik akun Pre-setup #28 bertambah tepat 1 dari baseline
17. Tunggu 5 detik tanpa memuat ulang halaman
18. Verifikasi jumlah item `"Assignment acceptance expired"` milik Siti Rahmawati (nonaktif) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-389: assignment_handover_completed, Assignee nonaktif

19. Pulihkan seed lalu atur ASG-2026-0120 Waiting for Handover lewat fixture BE penyetel state sumber, lalu nonaktifkan kembali Siti Rahmawati (Pre-setup #12) lewat fixture BE (pemulih seed juga memulihkan status #11/#12, `suite.md`)
20. Catat jumlah item `"Asset handover completed"` milik akun Pre-setup #28 dan milik Siti Rahmawati (nonaktif) (baseline) lewat fixture BE
21. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover fisik ASG-2026-0120 hingga status Assigned tersimpan
22. Muat ulang halaman Fixed Asset > Dashboard
23. Klik Bell icon sebagai akun Pre-setup #28
24. Verifikasi item `"Asset handover completed"` tampil pada Dropdown Panel akun Pre-setup #28
25. Verifikasi (kemampuan baca BE) jumlah item `"Asset handover completed"` milik akun Pre-setup #28 bertambah tepat 1 dari baseline
26. Tunggu 5 detik tanpa memuat ulang halaman
27. Verifikasi jumlah item `"Asset handover completed"` milik Siti Rahmawati (nonaktif) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-398: peminjam non-login, konfirmasi di-bypass dan handover ke pengguna perwakilan

28. Pulihkan seed lalu atur transaksi Borrow Joko Prasetyo Ready for Verification dengan 1 aset Printer Lantai 1 (AST-2024-0160) dan akun Pre-setup #30 tanpa notifikasi lewat fixture BE penyetel state sumber
29. Catat jumlah item `"Please confirm your borrowed asset"` dan `"Asset handover completed"` serta nilai badge Bell icon milik akun Pre-setup #30 (baseline) lewat fixture BE
30. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan transaksi Borrow Joko Prasetyo dan bypass konfirmasi untuk peminjam non-login hingga tersimpan
31. Logout, lalu login sebagai pengguna perwakilan (Pre-setup #30), lalu buka Fixed Asset > Dashboard
32. Verifikasi transaksi Borrow Joko Prasetyo tidak lagi berstatus Ready for Verification lewat fixture BE
33. Tunggu 5 detik tanpa memuat ulang halaman
34. Klik Bell icon sebagai pengguna perwakilan
35. Verifikasi Dropdown Panel akun Pre-setup #30 termuat (anchor permukaan; akun belum punya notifikasi)
36. Verifikasi (kemampuan baca BE) jumlah item `"Please confirm your borrowed asset"` milik akun Pre-setup #30 sama dengan baseline langkah 29 (tidak bertambah)
37. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik akun Pre-setup #30 sama dengan baseline langkah 29 (tidak bertambah)
38. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover transaksi Borrow Joko Prasetyo hingga status handover tersimpan
39. Muat ulang halaman Fixed Asset > Dashboard
40. Klik Bell icon sebagai pengguna perwakilan
41. Verifikasi (kemampuan baca BE) jumlah item `"Asset handover completed"` milik akun Pre-setup #30 bertambah tepat 1 dari baseline
42. Verifikasi item `"Asset handover completed"` berstatus Unread pada Dropdown Panel pengguna perwakilan
43. Verifikasi Body item `"Printer Lantai 1 is now officially your responsibility."`
44. Verifikasi tombol `[Mark as Read]` tampil pada item `"Asset handover completed"`
45. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik akun Pre-setup #30 menjadi `1`
46. Verifikasi badge Bell icon pengguna perwakilan menampilkan `1` pada UI sesudah muat ulang langkah 39

## Notes

- Langkah penghubung (S-03): langkah 4, 13, 22, dan 39 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1 (pulihkan seed, penyiapan state, dan muat ulang blok pertama); langkah 10, 19, dan 28 (pulihkan seed antar blok); langkah 2, 11, 20, dan 29 (baseline per TC); langkah 31 (ganti akun dan buka Fixed Asset > Dashboard); langkah 33 (jendela 5 detik untuk absence in-app, bagian 6).
- Langkah 8, 17, dan 26 (jendela 5 detik tanpa memuat ulang halaman sebelum pembacaan BE absence penerima nonaktif, bagian 6) adalah langkah penghubung tanpa Verifikasi (S-03). Pada blok TC-FA-NOTIF-398 baseline badge (langkah 29) dan pembacaan sesudah pemicu (langkah 37 dan 45) sama-sama lewat kemampuan baca BE (bagian 8b butir 10).
- Asersi tambahan di langkah 32 (S-03): status transaksi Joko Prasetyo tidak lagi Ready for Verification dibaca lewat fixture BE sebagai anchor positif bahwa pemicu bypass terproses sebelum asersi absence langkah 36 dan 37 (bagian 8b butir 2 dan 11). TC tidak menyebut status transaksi sesudah bypass.
- Anchor absence TC-FA-NOTIF-398 (langkah 35 dan 36): akun Pre-setup #30 belum punya seed notifikasi sehingga item pembanding di Dropdown Panel mustahil; anchor memakai Verifikasi Dropdown Panel akun #30 termuat (anchor permukaan, langkah 35) dan jumlah item agregat awal akun #30 (baseline langkah 29) dibandingkan lewat kemampuan baca BE (bagian 8b butir 2 dan 10), sesuai Expected butir a TC-FA-NOTIF-398 (jumlah item tetap sama dengan sebelum langkah pemicu dan badge tidak bertambah).
- Asersi tambahan (S-03): Verifikasi jumlah item akun Pre-setup #28 bertambah tepat 1 dari baseline (langkah 7, 16, dan 25) menurunkan selisih dari baseline BE dan menjadi anchor positif sebelum asersi absence penerima nonaktif (bagian 8b butir 2 dan 10); TC hanya menyebut item tampil.
- Asersi "Siti Rahmawati (nonaktif) tidak menerima" dibaca lewat fixture BE (TC langkah 3 menyebut "lewat fixture BE"), didahului penerimaan item oleh akun Pre-setup #28 pada blok yang sama sebagai anchor positif.
- Job auto-cancel (langkah 12) hanya pemicu keadaan; batas waktunya diuji di spec 121.
- Spec ini melewati sekitar 35 langkah (46); blok TC-FA-NOTIF-398 memuat dua tahap yang saling bergantung (bypass lalu handover pada transaksi yang sama), sehingga tidak dapat dipisah tanpa membangun ulang state yang sama.
- Langkah 46 (badge UI `1` sesudah muat ulang) melengkapi pembacaan BE langkah 45 (S-03; Expected butir b TC-FA-NOTIF-398).
- Pembagian per TC: TC-FA-NOTIF-387 (langkah 1 sampai 9), TC-FA-NOTIF-388 (langkah 10 sampai 18), TC-FA-NOTIF-389 (langkah 19 sampai 27), TC-FA-NOTIF-398 (langkah 28 sampai 45).
- Temuan untuk QA:
  - TC-FA-NOTIF-387, 388, 389 menulis precondition ASG-2026-0120 tanpa menyebut akun pelaku; spec memakai sesi API Asset Admin (Pre-setup #8).
  - TC-FA-NOTIF-398 tidak menyebut status transaksi sesudah bypass konfirmasi dan tidak menyebut Title notifikasi handover untuk peminjam non-login selain `"Asset handover completed"`.
  - TC-FA-NOTIF-398 mengasumsikan akun #30 belum punya notifikasi; baseline badge dicatat sebelum pemicu.
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
