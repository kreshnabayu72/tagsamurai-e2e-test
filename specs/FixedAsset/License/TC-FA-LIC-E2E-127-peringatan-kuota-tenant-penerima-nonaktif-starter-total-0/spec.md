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
| Pre-setup #1 | Total Control (Rudi Hartono), penerima dan aktor akun awal hook `before` | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #2 | Read Only, pembanding bukan penerima (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| Pre-setup #6 | Group Manager, pembanding bukan penerima (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| Pre-setup #9 | Total Control client Starter | `totalControlStarter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STARTER_TC_PASSWORD` |
| Pre-setup #21 | Total Control client Paid tanpa data dan tanpa ledger Asset License | `newClient_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_NEWCLIENT_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; ganti akun ke Pre-setup #9 (langkah 41) dan Pre-setup #21 (langkah 46) memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; setiap `Spectra.env.*` di atas didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): Total Asset License, cap plan Starter, Used, Reserved, penanda tingkat peringatan kuota, status akun penerima, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1, pembanding #6 dan #2), #9 (client Starter), #12 (Gudang A), dan #21 (client tanpa data). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-431 Gudang A Remaining 0 sedangkan tenant Remaining 60; blok TC-FA-LIC-432 dan TC-FA-LIC-533 Used 85, Reserved 4 (Remaining 11), penanda Normal; pada blok TC-FA-LIC-533 akun Pre-setup #3 berstatus nonaktif; blok TC-FA-LIC-487 client Paid tanpa baris Total Asset License (belum dialokasikan); blok TC-FA-LIC-548 ledger Asset License ada dengan Total 0 (semua alokasi term live Expired), Used 0, Reserved 0, penanda Normal; blok TC-FA-LIC-433 Starter dengan cap plan 100 (Pre-setup #9 diubah), Used 89, Reserved 0; blok TC-FA-LIC-434 client Paid tanpa ledger Asset License (belum dialokasikan).
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant, grup, dan akun Pre-setup #3, #9, #12, #16, dan #21 bernama literal karena Total Asset License, cap plan, Used, dan status akun tidak dapat dimiliki spec. Pemulihan ke Pre-setup dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, cap plan, Used, Reserved, penanda tingkat, status akun, status aset, dan entri Changelog, Activity Log, dan notifikasi (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima dan pembanding (Pre-setup #2, #3, dan #6) lewat fixture BE; kemampuan membaca log error server; kemampuan membaca jumlah entri `Changelog: Allocation Quota` dan Activity Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12), semuanya disediakan tim FE/BE (endpoint tidak dikarang). Jam fixture digeser maju sampai job penilaian per jam berjalan lalu dipulihkan pada langkah yang sama; sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`).
- Asersi absence notifikasi in-app didahului anchor positif dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-431: Peringatan kuota per grup tidak ada, hanya kuota tenant

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Gudang A Remaining `0` sedangkan tenant Remaining `60` hingga tersimpan
2. Catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
3. Registrasi aset hingga Remaining Gudang A 0
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 2
6. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi kuota baru dibanding langkah 2 (Remaining tenant masih di atas 10%)

### TC-FA-LIC-432: Peringatan kuota hanya diterima Manage global license (Update) dan Total Control

7. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, penanda Normal, serta akun Pre-setup #6 dan #2 aktif hingga tersimpan
8. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, #6, dan #2
9. Picu tingkat Low dengan registrasi satu aset sehingga Remaining 10
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low`
12. Verifikasi daftar notifikasi akun Pre-setup #6 dan #2 tidak memuat notifikasi baru dibanding langkah 8

### TC-FA-LIC-533: Peringatan kuota tidak diterima pemegang Manage global license yang nonaktif

13. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, penanda Normal, dan akun Pre-setup #3 berstatus nonaktif hingga tersimpan
14. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
15. Registrasi satu aset tanpa approval (Used 86, Remaining 10)
16. Tunggu 5 detik tanpa memuat ulang halaman
17. Verifikasi Bell Notification akun Pre-setup #1 (aktif) memuat tepat satu notifikasi baru `Asset license quota is running low`
18. Verifikasi daftar notifikasi akun Pre-setup #3 (nonaktif) tidak memuat notifikasi baru `license_quota_low` dibanding langkah 14

### TC-FA-LIC-487: Penilaian peringatan kuota dilewati untuk client yang belum memiliki Total Asset License

19. Jalankan fixture BE pemulih Pre-setup #16 dengan client Paid tanpa baris Total Asset License (belum dialokasikan) hingga tersimpan
20. Catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, serta jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level`
21. Registrasi satu aset tanpa approval
22. Verifikasi registrasi aset tidak terpengaruh (berhasil)
23. Geser jam fixture sampai job penilaian berjalan, lalu pulihkan jam fixture
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 20
26. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi baru `license_quota_low` maupun `license_quota_full` dibanding langkah 20
27. Verifikasi log error server tidak memuat error penilaian (penilaian dilewati tanpa error)
28. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
29. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 20
30. Tutup modal `Changelog: Allocation Quota`
31. Buka Fixed Asset > Reports & Logs > Activity Log
32. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 20

### TC-FA-LIC-548: Ledger Asset License ada dengan Total 0 dinilai Full

33. Jalankan fixture BE pemulih Pre-setup #16 dengan ledger Asset License ada tetapi Total 0 (semua alokasi term live Expired), Used `0`, Reserved `0`, dan penanda Normal hingga tersimpan
34. Catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
35. Buka License > All License
36. Verifikasi baris `Total` dan `Remaining` kolom `Asset` bernilai `0`
37. Geser jam fixture sampai job penilaian berjalan, lalu pulihkan jam fixture
38. Tunggu 5 detik tanpa memuat ulang halaman
39. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is full` dengan Body `No asset license remains available. New asset registrations are blocked until more quota is added.`
40. Verifikasi tidak ada notifikasi baru `license_quota_low` dibanding langkah 34

### Ganti akun ke Total Control client Starter

41. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client Starter (Pre-setup #9)

### TC-FA-LIC-433: Peringatan kuota berlaku pada tenant plan Starter dengan Total dari cap plan

42. Jalankan fixture BE pemulih Pre-setup #9 dengan cap plan 100, Used `89`, dan Reserved `0` hingga tersimpan
43. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #9
44. Registrasi aset sehingga Remaining 10
45. Verifikasi Bell Notification akun Pre-setup #9 memuat tepat satu notifikasi baru `license_quota_low` dengan Body `10 of 100 asset licenses remain available.`

### Ganti akun ke Total Control client tanpa data

46. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client tanpa data dan tanpa ledger Asset License (Pre-setup #21)

### TC-FA-LIC-434: Penilaian dilewati untuk client tanpa Total (belum dialokasikan)

47. Jalankan fixture BE pemulih Pre-setup #21 dengan client Paid tanpa ledger Asset License (belum dialokasikan) hingga tersimpan
48. Catat jumlah notifikasi kuota pada Bell Notification akun Pre-setup #21, serta jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level`
49. Lakukan perubahan Used atau Reserved lewat fixture BE
50. Tunggu 5 detik tanpa memuat ulang halaman
51. Verifikasi Bell Notification akun Pre-setup #21 termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 48
52. Verifikasi Bell Notification akun Pre-setup #21 tidak memuat notifikasi kuota baru dibanding langkah 48
53. Verifikasi log error server tidak memuat error penilaian
54. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
55. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 48
56. Tutup modal `Changelog: Allocation Quota`
57. Buka Fixed Asset > Reports & Logs > Activity Log
58. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 48
59. Jalankan fixture BE pemulih Pre-setup #21, #9, dan #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (penilaian peringatan kuota tenant, termasuk job per jam pada TC-FA-LIC-487 dan TC-FA-LIC-548). Pembagian TC lintas spec: TC-FA-LIC-423 sampai TC-FA-LIC-427 ada di spec 125, TC-FA-LIC-428 dan TC-FA-LIC-532 di spec 145, dan TC-FA-LIC-429, TC-FA-LIC-430, TC-FA-LIC-491, TC-FA-LIC-492, TC-FA-LIC-546, dan TC-FA-LIC-547 di spec 126.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 7, 13, 19, 33, 42, 47, dan 59 (fixture BE pemulih dan penyetel state), langkah 23 dan 37 (menggeser jam fixture lalu memulihkannya), langkah 30 dan 56 (menutup modal Changelog), langkah 49 (mengubah Used atau Reserved lewat fixture), serta pencatatan baseline pada langkah 2, 8, 14, 20, 34, 43, dan 48 (S-12). Ganti akun pada langkah 41 dan 46 mengikuti S-07. Langkah `Tunggu 5 detik tanpa memuat ulang halaman` mendahului asersi absence notifikasi.
- Urutan TC diubah dari urutan nomor: dikelompokkan per akun (Pre-setup #1, lalu #9, lalu #21) agar ganti akun hanya dua kali (S-10); pada akun Pre-setup #1 blok penerima (TC-FA-LIC-431, TC-FA-LIC-432, TC-FA-LIC-533) lebih dulu, lalu blok penilaian dilewati dan Total 0 (TC-FA-LIC-487, TC-FA-LIC-548). Asersi "tidak ada notifikasi atau entri baru" memakai selisih jumlah dengan baseline (asersi jumlah, bukan kelas g).
- Alasan di atas sekitar 35 langkah (59 langkah): semua blok satu topik (peringatan kuota tenant: cakupan penerima dan penilaian yang dilewati) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pembacaan baseline, ganti akun, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-434 memakai akun Pre-setup #21 sesuai Precondition TC; spec login sebagai Pre-setup #21 setelah ganti akun.
  - TC-FA-LIC-433 Precondition menulis `Login sbg Role: Total Control (Pre-setup #9)`; spec memakai Pre-setup #9 tanpa Pre-setup #1.
  - TC-FA-LIC-487 Precondition menulis akun Pre-setup #1 tetapi client "Paid tanpa baris Total Asset License (belum dialokasikan, fixture)", yang berbeda dari data client Pre-setup #1 (Total Asset License 5.000); spec mengikuti Precondition lewat fixture BE.
  - TC-FA-LIC-434 Expected a "tidak ada error" tidak menyebut permukaan error; spec memakai kemampuan membaca log error server seperti TC-FA-LIC-487.
  - TC-FA-LIC-487 dan TC-FA-LIC-433 tidak menyebut approval ON atau OFF pada Precondition; spec memakai approval OFF seperti blok lain.
  - TC-FA-LIC-487 berlabel `Manual Only — (b)`; spec menuliskan penilaian dilewati lewat jam fixture dan kemampuan baca log error server yang disediakan tim FE/BE.
