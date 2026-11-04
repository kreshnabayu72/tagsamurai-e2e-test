---
id: TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0
title: "Peringatan Kuota Tenant: Cakupan Penerima, Penerima Nonaktif, Plan Starter, dan Penilaian Dilewati"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-431
  - TC-FA-LIC-432
  - TC-FA-LIC-433
  - TC-FA-LIC-434
  - TC-FA-LIC-487
  - TC-FA-LIC-533
  - TC-FA-LIC-548
coverage:
  web: automated
---

# Peringatan Kuota Tenant: Cakupan Penerima, Penerima Nonaktif, Plan Starter, dan Penilaian Dilewati

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono), penerima dan aktor akun awal hook `before` (daftar notifikasinya dibaca lewat Notification Center) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #2 | Read Only, pembanding bukan penerima (daftar notifikasinya dibaca lewat kemampuan baca BE, tanpa login) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima (daftar notifikasinya dibaca lewat kemampuan baca BE, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| Pre-setup #6 | Group Manager, pembanding bukan penerima (daftar notifikasinya dibaca lewat kemampuan baca BE, tanpa login) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| Pre-setup #9 | Total Control client Starter (daftar notifikasinya dibaca lewat Notification Center) | `totalControlStarter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STARTER_TC_PASSWORD` |
| Pre-setup #21 | Total Control client Paid tanpa data dan tanpa ledger Asset License (tanpa seed notifikasi yang dijamin; daftar notifikasinya dibaca lewat kemampuan baca BE, Dropdown Panel Bell Notification hanya sebagai anchor termuat) | `newClient_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_NEWCLIENT_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; ganti akun ke Pre-setup #9 (langkah 53) dan Pre-setup #21 (langkah 60) memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; setiap `Spectra.env.*` di atas didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): Total Asset License, cap plan Starter, Used, Reserved, penanda tingkat peringatan kuota, status akun penerima, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1, pembanding #6 dan #2), #9 (client Starter), #12 (Gudang A), dan #21 (client tanpa data). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-431 Gudang A Remaining 0 sedangkan tenant Remaining 60; blok TC-FA-LIC-432 dan TC-FA-LIC-533 Used 85, Reserved 4 (Remaining 11), penanda Normal; pada blok TC-FA-LIC-533 akun Pre-setup #3 berstatus nonaktif; blok TC-FA-LIC-487 client Paid tanpa baris Total Asset License (belum dialokasikan); blok TC-FA-LIC-548 ledger Asset License ada dengan Total 0 (semua alokasi term live Expired), Used 0, Reserved 0, penanda Normal; blok TC-FA-LIC-433 Starter dengan cap plan 100 (Pre-setup #9 diubah), Used 89, Reserved 0; blok TC-FA-LIC-434 client Paid tanpa ledger Asset License (belum dialokasikan).
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant, grup, dan akun Pre-setup #3, #9, #12, #16, dan #21 bernama literal karena Total Asset License, cap plan, Used, dan status akun tidak dapat dimiliki spec. Pemulihan ke Pre-setup dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, cap plan, Used, Reserved, penanda tingkat, status akun, status aset, dan entri Changelog, Activity Log, dan notifikasi (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima dan pembanding (Pre-setup #2, #3, #6, dan #21) lewat fixture BE (kemampuan baca daftar notifikasi akun Pre-setup #21 disediakan tim FE/BE; akun #21 tanpa seed notifikasi yang dijamin); kemampuan membaca log error server; kemampuan membaca jumlah entri `Changelog: Allocation Quota` dan Activity Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12), semuanya disediakan tim FE/BE (endpoint tidak dikarang). Jam fixture digeser maju sampai job penilaian per jam berjalan lalu dipulihkan pada langkah yang sama; sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`).
- Sumber baca notifikasi (8b.10): baseline per penerima dicatat tepat sebelum pemicu dan pembacaan sesudah pemicu memakai sumber yang sama; akun UI (Pre-setup #1 dan #9) lewat Notification Center dengan scroll sampai seluruh item termuat, akun non-login (Pre-setup #2, #3, dan #6) dan akun Pre-setup #21 (tanpa seed notifikasi yang dijamin; baseline dicatat lewat BE tepat sebelum pemicu dan pembacaan sesudah pemicu dari BE yang sama, ditambah `Verifikasi` Dropdown Panel termuat) lewat kemampuan baca BE. Bell Notification (Dropdown Panel hanya memuat 5 item terbaru) tidak dipakai untuk menghitung.
- Asersi absence notifikasi in-app didahului anchor positif pada daftar yang sama (jumlah baseline yang tercatat termuat) dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-431: Peringatan kuota per grup tidak ada, hanya kuota tenant

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Gudang A Remaining `0` sedangkan tenant Remaining `60` hingga tersimpan
2. Muat ulang halaman Fixed Asset > Dashboard
3. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full`; catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
4. Registrasi aset hingga Remaining Gudang A 0 dan berhasil tersimpan
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
7. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 3
8. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi kuota baru dibanding langkah 3 (Remaining tenant masih di atas 10%)

### TC-FA-LIC-432: Peringatan kuota hanya diterima Manage global license (Update) dan Total Control

9. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, penanda Normal, serta akun Pre-setup #6 dan #2 aktif hingga tersimpan
10. Muat ulang halaman Fixed Asset > Dashboard
11. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3, #6, dan #2 lewat kemampuan baca BE
12. Picu tingkat Low dengan registrasi satu aset hingga berhasil tersimpan
13. Tunggu 5 detik tanpa memuat ulang halaman
14. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
15. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 11
16. Verifikasi daftar notifikasi akun Pre-setup #6 dan #2 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 11
17. Verifikasi daftar notifikasi akun Pre-setup #6 dan #2 (kemampuan baca BE) tidak memuat notifikasi baru dibanding langkah 11

### TC-FA-LIC-533: Peringatan kuota tidak diterima pemegang Manage global license yang nonaktif

18. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, penanda Normal, dan akun Pre-setup #3 berstatus nonaktif hingga tersimpan
19. Muat ulang halaman Fixed Asset > Dashboard
20. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
21. Registrasi satu aset tanpa approval hingga berhasil tersimpan
22. Tunggu 5 detik tanpa memuat ulang halaman
23. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
24. Verifikasi Notification Center akun Pre-setup #1 (aktif) memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 20
25. Verifikasi daftar notifikasi akun Pre-setup #3 (nonaktif, kemampuan baca BE) termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 20
26. Verifikasi daftar notifikasi akun Pre-setup #3 (nonaktif, kemampuan baca BE) tidak memuat notifikasi baru `license_quota_low` dibanding langkah 20

### TC-FA-LIC-487: Penilaian peringatan kuota dilewati untuk client yang belum memiliki Total Asset License

27. Jalankan fixture BE pemulih Pre-setup #16 dengan client Paid tanpa baris Total Asset License (belum dialokasikan) hingga tersimpan
28. Muat ulang halaman Fixed Asset > Dashboard
29. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full`; catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE; catat jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level` lewat kemampuan baca
30. Registrasi satu aset tanpa approval hingga berhasil tersimpan
31. Verifikasi registrasi aset tidak terpengaruh (berhasil)
32. Geser jam fixture sampai job penilaian berjalan, lalu pulihkan jam fixture
33. Tunggu 5 detik tanpa memuat ulang halaman
34. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
35. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 29
36. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru `license_quota_low` maupun `license_quota_full` dibanding langkah 29
37. Verifikasi log error server tidak memuat error penilaian (penilaian dilewati tanpa error)
38. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
39. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 29
40. Tutup modal `Changelog: Allocation Quota`
41. Buka Fixed Asset > Reports & Logs > Activity Log
42. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 29

### TC-FA-LIC-548: Ledger Asset License ada dengan Total 0 dinilai Full

43. Jalankan fixture BE pemulih Pre-setup #16 dengan ledger Asset License ada tetapi Total 0 (semua alokasi term live Expired), Used `0`, Reserved `0`, dan penanda Normal hingga tersimpan
44. Muat ulang halaman Fixed Asset > Dashboard
45. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full`; catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
46. Buka License > All License
47. Verifikasi baris `Total` dan `Remaining` kolom `Asset` bernilai `0`
48. Geser jam fixture sampai job penilaian berjalan, lalu pulihkan jam fixture
49. Tunggu 5 detik tanpa memuat ulang halaman
50. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
51. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is full` dengan Body `No asset license remains available. New asset registrations are blocked until more quota is added.` dibanding jumlah pada langkah 45
52. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru `license_quota_low` dibanding langkah 45

### Ganti akun ke Total Control client Starter

53. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client Starter (Pre-setup #9)

### TC-FA-LIC-433: Peringatan kuota berlaku pada tenant plan Starter dengan Total dari cap plan

54. Jalankan fixture BE pemulih Pre-setup #9 dengan cap plan 100, Used `89`, dan Reserved `0` hingga tersimpan
55. Muat ulang halaman Fixed Asset > Dashboard
56. Buka Notification Center akun Pre-setup #9, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`
57. Registrasi aset hingga berhasil tersimpan
58. Buka Notification Center akun Pre-setup #9 dan scroll sampai seluruh item termuat
59. Verifikasi Notification Center akun Pre-setup #9 memuat tepat satu notifikasi baru `license_quota_low` dengan Body `10 of 100 asset licenses remain available.` dibanding jumlah pada langkah 56

### Ganti akun ke Total Control client tanpa data

60. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client tanpa data dan tanpa ledger Asset License (Pre-setup #21)

### TC-FA-LIC-434: Penilaian dilewati untuk client tanpa Total (belum dialokasikan)

61. Jalankan fixture BE pemulih Pre-setup #21 dengan client Paid tanpa ledger Asset License (belum dialokasikan) hingga tersimpan
62. Muat ulang halaman Fixed Asset > Dashboard
63. Catat jumlah notifikasi kuota (`Asset license quota is running low` dan `Asset license quota is full`) pada daftar notifikasi akun Pre-setup #21 lewat kemampuan baca BE; catat jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level` lewat kemampuan baca
64. Lakukan perubahan Used atau Reserved lewat fixture BE hingga tersimpan
65. Tunggu 5 detik tanpa memuat ulang halaman
66. Buka Dropdown Panel Bell Notification akun Pre-setup #21
67. Verifikasi Dropdown Panel Bell Notification akun Pre-setup #21 termuat
68. Verifikasi daftar notifikasi akun Pre-setup #21 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 63
69. Verifikasi daftar notifikasi akun Pre-setup #21 (kemampuan baca BE) tidak memuat notifikasi kuota baru dibanding langkah 63
70. Verifikasi log error server tidak memuat error penilaian
71. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
72. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 63
73. Tutup modal `Changelog: Allocation Quota`
74. Buka Fixed Asset > Reports & Logs > Activity Log
75. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 63
76. Jalankan fixture BE pemulih Pre-setup #21, #9, dan #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (penilaian peringatan kuota tenant, termasuk job per jam pada TC-FA-LIC-487 dan TC-FA-LIC-548). Pembagian TC lintas spec: TC-FA-LIC-423 sampai TC-FA-LIC-427 ada di spec 125, TC-FA-LIC-428 dan TC-FA-LIC-532 di spec 145, dan TC-FA-LIC-429, TC-FA-LIC-430, TC-FA-LIC-491, TC-FA-LIC-492, TC-FA-LIC-546, dan TC-FA-LIC-547 di spec 126.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 9, 18, 27, 43, 54, 61, dan 76 (fixture BE pemulih dan penyetel state), langkah 32 dan 48 (menggeser jam fixture lalu memulihkannya), menutup modal Changelog, langkah 64 (mengubah Used atau Reserved lewat fixture), membuka Notification Center dan scroll sampai seluruh item termuat, serta pencatatan baseline pada langkah 3, 11, 20, 29, 45, 56, dan 63 (S-12). Ganti akun pada langkah 53 dan 60 mengikuti S-07. Nilai Remaining dari TC (mis. Remaining 10) tidak ditulis di langkah aksi (R-02): fixture mengatur state awal sesuai Precondition. Langkah `Tunggu 5 detik tanpa memuat ulang halaman` mendahului asersi absence notifikasi.
- Langkah penghubung muat ulang (S-03, aksi tanpa `Verifikasi`, 8b.10): `Muat ulang halaman Fixed Asset > Dashboard` pada langkah 2, 10, 19, 28, 44, 55, dan 62, tepat sesudah fixture BE pemulih seed dan sebelum langkah yang mencatat baseline notifikasi atau mengasersi UI (juga menutup Dropdown Panel).
- Urutan TC diubah dari urutan nomor: dikelompokkan per akun (Pre-setup #1, lalu #9, lalu #21) agar ganti akun hanya dua kali (S-10); pada akun Pre-setup #1 blok penerima (TC-FA-LIC-431, TC-FA-LIC-432, TC-FA-LIC-533) lebih dulu, lalu blok penilaian dilewati dan Total 0 (TC-FA-LIC-487, TC-FA-LIC-548). Asersi "tidak ada notifikasi atau entri baru" memakai selisih jumlah dengan baseline (asersi jumlah, bukan kelas g).
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` jumlah baseline termuat sebagai anchor absence notifikasi (8b.2), `Verifikasi` registrasi berhasil pada TC-FA-LIC-487 mengikuti Expected b, `Verifikasi` log error server pada TC-FA-LIC-434 mengikuti Expected a (tidak ada error), dan `Verifikasi` Dropdown Panel Bell Notification termuat sebagai anchor absence pada TC-FA-LIC-434 (8b.10: akun Pre-setup #21 tanpa seed notifikasi; baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE).
- Alasan di atas sekitar 35 langkah (76 langkah): semua blok satu topik (peringatan kuota tenant: cakupan penerima dan penilaian yang dilewati) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pembacaan baseline, ganti akun, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-434 memakai akun Pre-setup #21 sesuai Precondition TC; spec login sebagai Pre-setup #21 setelah ganti akun.
  - TC-FA-LIC-433 Precondition menulis `Login sbg Role: Total Control (Pre-setup #9)`; spec memakai Pre-setup #9 tanpa Pre-setup #1.
  - TC-FA-LIC-487 Precondition menulis akun Pre-setup #1 tetapi client "Paid tanpa baris Total Asset License (belum dialokasikan, fixture)", yang berbeda dari data client Pre-setup #1 (Total Asset License 5.000); spec mengikuti Precondition lewat fixture BE.
  - TC-FA-LIC-434 Expected a "tidak ada error" tidak menyebut permukaan error; spec memakai kemampuan membaca log error server seperti TC-FA-LIC-487.
  - TC-FA-LIC-487 dan TC-FA-LIC-433 tidak menyebut approval ON atau OFF pada Precondition; spec memakai approval OFF seperti blok lain.
  - TC-FA-LIC-487 berlabel `Manual Only — (b)`; spec menuliskan penilaian dilewati lewat jam fixture dan kemampuan baca log error server yang disediakan tim FE/BE.
