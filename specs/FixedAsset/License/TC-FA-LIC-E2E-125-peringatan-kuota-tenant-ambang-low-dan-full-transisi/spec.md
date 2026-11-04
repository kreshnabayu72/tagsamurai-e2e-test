---
id: TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi
title: "Peringatan Kuota Tenant: Ambang Low dan Full serta Transisi Penanda Tingkat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-423
  - TC-FA-LIC-424
  - TC-FA-LIC-425
  - TC-FA-LIC-426
  - TC-FA-LIC-427
  - TC-FA-LIC-495
coverage:
  web: automated
---

# Peringatan Kuota Tenant: Ambang Low dan Full serta Transisi Penanda Tingkat

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono), penerima dan aktor (daftar notifikasinya dibaca lewat Notification Center) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima peringatan kuota (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` dan `Spectra.env.FA_MGL_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): Total Asset License, Used, Reserved, penanda tingkat peringatan kuota, dan status aset dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, variasi 105; penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-423 dan TC-FA-LIC-424 Used 85 dan Reserved 4 (Remaining 11); blok TC-FA-LIC-425 Total 105, Used 94, Reserved 0 (Remaining 11); blok TC-FA-LIC-426 penanda Low sudah tercatat dan Remaining 1; blok TC-FA-LIC-427 Used 85, Reserved 4 (Remaining 11), dan 11 draf aset; blok TC-FA-LIC-495 Used 95 dan Reserved 10 (Remaining rumus −5), penanda Normal.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant Pre-setup #16 bernama literal karena Total Asset License, Used, dan penanda tingkat tidak dapat dimiliki spec. Pemulihan ke Pre-setup #16 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Remaining, penanda tingkat, status aset, dan entri Changelog dan Activity Log (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 lewat fixture BE (disediakan tim FE/BE; endpoint tidak dikarang); kemampuan membaca jumlah entri Changelog: Allocation Quota dan Activity Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12). Kemampuan menggeser jam fixture sampai job penilaian per jam berjalan (langkah 32 dan 57; jam dipulihkan pada langkah yang sama dengan penggeseran, sehingga blok sesudahnya berjalan dengan jam semula; sesi UI dan sesi API aktor tetap valid selama jam digeser, dinyatakan di `suite.md`); penilaian lainnya dipicu pasca-commit oleh registrasi dan Delete aset.
  - Sumber baca notifikasi (8b.10; baseline dan pembacaan sesudah pemicu memakai sumber yang sama): akun UI Pre-setup #1 lewat Notification Center dengan scroll sampai seluruh item termuat, akun non-login Pre-setup #3 lewat kemampuan baca BE; Bell Notification (Dropdown Panel hanya memuat 5 item terbaru) tidak dipakai untuk menghitung. Baseline per penerima dicatat tepat sebelum pemicu.
  - Asersi absence notifikasi in-app didahului anchor positif dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-423: Peringatan Low, Remaining turun ke 10 dari 100 mengirim satu license_quota_low

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, penanda Normal, approval OFF, dan draf aset hingga tersimpan
2. Muat ulang halaman Fixed Asset > Dashboard
3. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
4. Registrasi satu aset tanpa approval hingga berhasil tersimpan
5. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
6. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dengan Body `10 of 100 asset licenses remain available.` dibanding jumlah pada langkah 3
7. Registrasi satu aset lagi hingga berhasil tersimpan
8. Tunggu 5 detik tanpa memuat ulang halaman
9. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
10. Verifikasi notifikasi `Asset license quota is running low` dari langkah 6 tetap tampil pada Notification Center akun Pre-setup #1
11. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru dibanding hasil pembacaan pada langkah 6 (Remaining 9 masih Low)

### TC-FA-LIC-424: Batas Low, Remaining 11 dari 100 tidak mengirim peringatan

12. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, dan penanda Normal hingga tersimpan
13. Muat ulang halaman Fixed Asset > Dashboard
14. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi kuota (`Asset license quota is running low` dan `Asset license quota is full`); catat jumlah notifikasi kuota (`Asset license quota is running low` dan `Asset license quota is full`) pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE; catat jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level` lewat kemampuan baca
15. Lakukan perubahan yang membuat Remaining tetap 11 (Delete satu aset lalu registrasi satu aset) hingga berhasil tersimpan
16. Tunggu 5 detik tanpa memuat ulang halaman
17. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
18. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi kuota yang tercatat pada langkah 14
19. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi kuota baru dibanding langkah 14
20. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
21. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 14
22. Tutup modal `Changelog: Allocation Quota`
23. Buka Fixed Asset > Reports & Logs > Activity Log
24. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 14

### TC-FA-LIC-425: Ambang 10% pada Total tidak kelipatan 10 (Total 105)

25. Jalankan fixture BE pemulih Pre-setup #16 dengan Total `105`, penanda Normal, Used `94`, dan Reserved `0` (Remaining 11) hingga tersimpan
26. Muat ulang halaman Fixed Asset > Dashboard
27. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
28. Registrasi satu aset hingga berhasil tersimpan
29. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
30. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `license_quota_low` dengan Body `10 of 105 asset licenses remain available.` dibanding jumlah pada langkah 27 (Remaining 10 ≤ 10,5)
31. Pulihkan Remaining ke 11 lewat fixture BE hingga tersimpan
32. Geser jam fixture sampai job penilaian per jam berjalan, lalu pulihkan jam fixture
33. Tunggu 5 detik tanpa memuat ulang halaman
34. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
35. Verifikasi notifikasi `license_quota_low` dari langkah 30 tetap tampil pada Notification Center akun Pre-setup #1
36. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru dibanding hasil pembacaan pada langkah 30 (Remaining 11 > 10,5)

### TC-FA-LIC-426: Peringatan Full, Remaining 0 mengirim license_quota_full termasuk setelah Low terkirim

37. Jalankan fixture BE pemulih Pre-setup #16 dengan penanda Low tercatat dan Remaining `1` hingga tersimpan
38. Muat ulang halaman Fixed Asset > Dashboard
39. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is full`; catat jumlah notifikasi `Asset license quota is full` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
40. Registrasi satu aset hingga berhasil tersimpan
41. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
42. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is full` dengan Body `No asset license remains available. New asset registrations are blocked until more quota is added.` dibanding jumlah pada langkah 39

### TC-FA-LIC-427: Normal langsung ke Full hanya mengirim license_quota_full

43. Jalankan fixture BE pemulih Pre-setup #16 dengan penanda Normal, Used `85`, Reserved `4` (Remaining 11), approval OFF, dan 11 draf aset hingga tersimpan
44. Muat ulang halaman Fixed Asset > Dashboard
45. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is full` dan `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is full` dan `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
46. Registrasi massal 11 aset pada penanda Normal hingga berhasil tersimpan
47. Tunggu 5 detik tanpa memuat ulang halaman
48. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
49. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `license_quota_full` (`Asset license quota is full`) dibanding jumlah pada langkah 45
50. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru `license_quota_low` (`Asset license quota is running low`) dibanding jumlah pada langkah 45
51. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

### TC-FA-LIC-495: Used + Reserved tenant melampaui Total, Remaining ditampilkan 0 dan tingkat Full

52. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `95`, Reserved `10`, dan penanda tingkat Normal hingga tersimpan
53. Buka License > All License
54. Verifikasi Remaining tenant ditampilkan `0`, bukan `-5`
55. Muat ulang halaman Fixed Asset > Dashboard
56. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is full` dan `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is full` dan `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
57. Geser jam fixture sampai penilaian berjalan, lalu pulihkan jam fixture
58. Tunggu 5 detik tanpa memuat ulang halaman
59. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
60. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is full` dibanding jumlah pada langkah 56
61. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 56
62. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (peringatan kuota tenant dan penanda tingkat oleh `assess_license_quota_alert()`); blok di spec ini dipicu pasca-commit oleh registrasi dan Delete aset, kecuali TC-FA-LIC-425 dan TC-FA-LIC-495 yang menggeser jam fixture sampai job penilaian per jam berjalan; blok yang memerlukan job per jam dan top-up Total lainnya ada di spec 126, 127, 128, dan 145.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): fixture BE pemulih dan penyetel state, memulihkan Remaining, penggeseran jam fixture yang dipulihkan pada langkah yang sama (langkah 32 dan 57; blok sesudahnya tidak membutuhkan jam bergeser karena yang diasersi adalah notifikasi yang sudah tercatat), menutup modal Changelog, `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi, membuka Notification Center dan scroll sampai seluruh item termuat, serta pencatatan baseline pada langkah 3, 14, 27, 39, 45, dan 56 (S-12). Pada TC-FA-LIC-424 asersi "tidak ada entri baru" berupa asersi jumlah dengan baseline langkah 14, bukan asersi absence kelas g (bagian 3 prinsip 13). Nilai Remaining dari TC (mis. Remaining 10 sesudah registrasi pertama TC-FA-LIC-423) tidak ditulis di langkah aksi (R-02): fixture mengatur state awal dan registrasi menurunkan Remaining sesuai Precondition.
- Langkah penghubung muat ulang (S-03, aksi tanpa `Verifikasi`, 8b.10): `Muat ulang halaman Fixed Asset > Dashboard` pada langkah 2, 13, 26, 38, 44, dan 55, tepat sesudah fixture BE pemulih seed dan sebelum langkah yang mencatat baseline notifikasi atau mengasersi UI (juga menutup Dropdown Panel).
- Urutan TC mengikuti urutan nomor (TC-FA-LIC-495 di akhir); pembagian TC lintas spec: TC-FA-LIC-428 dan TC-FA-LIC-532 (penanda turun setelah top-up) ada di spec 145.
- Temuan untuk QA:
  - TC-FA-LIC-424 mengasersi tidak ada entri baru pada Changelog dan Activity Log; spec membandingkan jumlah entri dengan baseline.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` bahwa notifikasi sebelumnya tetap tampil pada daftar yang sama sebelum asersi absence notifikasi (8b.2), dan `Verifikasi` Remaining `0` pada TC-FA-LIC-495 mengikuti Expected a.
- Alasan di atas 35 langkah (62 langkah): semua blok satu topik (ambang peringatan kuota Low dan Full) dan berdiri sendiri; langkah di atas 35 berasal dari pemicu job penilaian, anchor positif, dan jeda 5 detik; kegagalan satu blok tidak membuat blok lain kehilangan makna.
