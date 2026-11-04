---
id: TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca
title: "Peringatan Kuota Tenant: Job Per Jam, Penilaian Pasca-commit, dan Pencatatan oleh System"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-429
  - TC-FA-LIC-430
  - TC-FA-LIC-491
  - TC-FA-LIC-492
  - TC-FA-LIC-546
  - TC-FA-LIC-547
coverage:
  web: automated
---

# Peringatan Kuota Tenant: Job Per Jam, Penilaian Pasca-commit, dan Pencatatan oleh System

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono), penerima dan aktor (daftar notifikasinya dibaca lewat Notification Center) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima peringatan kuota (daftar notifikasinya dibaca lewat kemampuan baca BE, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` dan `Spectra.env.FA_MGL_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): Total Asset License, Used, Reserved, penanda tingkat peringatan kuota, status aset, pembuatan event notifikasi, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1) dan #1 (jumlah entri System Log Rudi Hartono dicatat pada blok TC-FA-LIC-547). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-429, TC-FA-LIC-546, dan TC-FA-LIC-547 Total diturunkan di Admin Console sehingga Remaining 8 tanpa perubahan lokal (penanda Normal); blok TC-FA-LIC-491 penanda Low tercatat (Used 90, Remaining 10); blok TC-FA-LIC-430 pembuatan event notifikasi digagalkan, Used 85, Reserved 4 (Remaining 11), penanda Normal; blok TC-FA-LIC-492 Used 85, Reserved 4 (Remaining 11), penanda Normal, dan panggilan `assess_license_quota_alert` digagalkan.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant Pre-setup #16 bernama literal karena Total Asset License, Used, dan penanda tingkat tidak dapat dimiliki spec. Pemulihan ke Pre-setup #16 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, Used, Reserved, penanda tingkat, jam fixture, status aset, dan entri Changelog, Activity Log, dan notifikasi (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Sumber baca notifikasi (8b.10): baseline per penerima dicatat tepat sebelum pemicu dan pembacaan sesudah pemicu memakai sumber yang sama; akun UI Pre-setup #1 lewat Notification Center dengan scroll sampai seluruh item termuat, akun non-login Pre-setup #3 lewat kemampuan baca BE. Bell Notification (Dropdown Panel hanya memuat 5 item terbaru) tidak dipakai untuk menghitung.
- Jam server dan jam browser sinkron (S-12): asersi Date sesuai waktu job pada langkah 30 membandingkan Date entri dengan waktu job yang dicatat pada langkah 28 (jam fixture saat job berjalan, sebelum jam dipulihkan) dengan toleransi satu menit, karena kolom Date berketelitian menit.
- Asersi absence notifikasi in-app didahului anchor positif pada daftar yang sama (jumlah baseline yang tercatat termuat) dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 lewat fixture BE; kemampuan membaca penanda tingkat peringatan kuota tenant lewat fixture BE; fixture BE yang menggagalkan pembuatan event notifikasi dan panggilan `assess_license_quota_alert` (semuanya disediakan tim FE/BE; endpoint tidak dikarang); kemampuan membaca jumlah entri `Changelog: Allocation Quota`, Activity Log, dan System Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12). Jam fixture digeser maju sampai job per jam berjalan: sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`), entri dicari berdasarkan Field `Quota Alert Level`, Old Value, dan New Value (bukan posisi teratas), jam dipulihkan pada langkah yang sama dengan penggeseran sehingga akun aktor membuka Activity Log dan halaman lain setelah jam kembali (S-09), dan penantian job tidak memakai jeda nyata.

## Test Steps

### TC-FA-LIC-429: Job penilaian per jam menilai perubahan Total dari Admin Console, bukan saat halaman License dibuka

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Total diturunkan di Admin Console sehingga Remaining `8` tanpa perubahan lokal dan penanda Normal hingga tersimpan
2. Muat ulang halaman Fixed Asset > Dashboard
3. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE; catat jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level` lewat kemampuan baca
4. Buka halaman License tanpa menggeser jam fixture
5. Verifikasi `Remaining` kolom `Asset` `8`
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
8. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi `Asset license quota is running low` yang tercatat pada langkah 3
9. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru dibanding langkah 3 (membuka halaman License tidak memicu penilaian)
10. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
11. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 3 (sebelum job)
12. Tutup modal `Changelog: Allocation Quota`
13. Buka Fixed Asset > Reports & Logs > Activity Log
14. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 3 (sebelum job)
15. Geser jam fixture sampai job jam berikutnya berjalan, lalu pulihkan jam fixture
16. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
17. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 3 (job berjalan dengan interval 1 jam)
18. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
19. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding langkah 3: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
20. Tutup modal `Changelog: Allocation Quota`
21. Buka Fixed Asset > Reports & Logs > Activity Log
22. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 3: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`

### TC-FA-LIC-546: Changelog: Allocation Quota, perubahan penanda oleh job tercatat dengan Modified By System

23. Jalankan fixture BE pemulih Pre-setup #16 dengan Total diturunkan di Admin Console sehingga Remaining `8` dan penanda Normal hingga tersimpan
24. Catat jumlah entri `Changelog: Allocation Quota` dengan Field `Quota Alert Level`
25. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
26. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 24 (sebelum job)
27. Tutup modal `Changelog: Allocation Quota`
28. Geser jam fixture sampai job penilaian per jam berjalan dan catat waktu job (jam fixture saat job berjalan), lalu pulihkan jam fixture
29. Buka kembali modal `Changelog: Allocation Quota` dengan klik ikon Changelog pada toolbar Section 2
30. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding langkah 24 dengan Date sesuai waktu job yang dicatat pada langkah 28 (jam fixture, format General Settings `dd/MM/yy HH:mm`, toleransi satu menit)
31. Verifikasi entri baru itu: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
32. Verifikasi Action dan nilai entri baru itu ditulis plain text (bukan badge)
33. Tutup modal `Changelog: Allocation Quota`

### TC-FA-LIC-547: Activity Log dan System Log, perubahan penanda oleh job tercatat di Activity Log tanpa entri System Log

34. Jalankan fixture BE pemulih Pre-setup #16 dengan Total diturunkan di Admin Console sehingga Remaining `8` dan penanda Normal hingga tersimpan
35. Catat jumlah entri Activity Log dengan Field `Quota Alert Level` dan jumlah entri System Log Rudi Hartono (Pre-setup #1)
36. Geser jam fixture sampai job penilaian per jam berjalan, lalu pulihkan jam fixture
37. Buka Fixed Asset > Reports & Logs > Activity Log
38. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 35: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
39. Buka Global Settings > User > Detail Rudi Hartono > Tab System Log
40. Verifikasi Tab System Log Rudi Hartono memuat sedikitnya satu entri
41. Verifikasi jumlah entri System Log Rudi Hartono tidak bertambah dibanding langkah 35 (penilaian tidak punya user aktor)
42. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

### TC-FA-LIC-491: Delete aset memanggil penilaian pasca-commit, penanda turun ke Normal tanpa menunggu job per jam

43. Jalankan fixture BE pemulih Pre-setup #16 dengan penanda Low tercatat (Used 90, Remaining 10) dan approval OFF hingga tersimpan
44. Muat ulang halaman Fixed Asset > Dashboard
45. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
46. Delete satu aset Active hingga berhasil tersimpan
47. Verifikasi penanda tingkat Normal tanpa menunggu job per jam
48. Tunggu 5 detik tanpa memuat ulang halaman
49. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
50. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) termuat dan menampilkan jumlah notifikasi `Asset license quota is running low` yang tercatat pada langkah 45
51. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) tidak memuat notifikasi baru dibanding langkah 45
52. Registrasi satu aset tanpa approval hingga berhasil tersimpan
53. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
54. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 45

### TC-FA-LIC-430: Kegagalan membuat event tidak menaikkan penanda dan tidak memblokir transaksi pemicu

55. Jalankan fixture BE pemulih Pre-setup #16 dengan pembuatan event notifikasi digagalkan, Used `85`, Reserved `4` (Remaining 11), dan penanda Normal hingga tersimpan
56. Muat ulang halaman Fixed Asset > Dashboard
57. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE; catat jumlah entri `Changelog: Allocation Quota` dengan Field `Quota Alert Level` lewat kemampuan baca
58. Registrasi satu aset hingga berhasil tersimpan
59. Verifikasi registrasi berhasil walau event gagal
60. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
61. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 57 (penanda tidak naik)
62. Tutup modal `Changelog: Allocation Quota`
63. Pulihkan pembuatan event lewat fixture BE hingga tersimpan
64. Lakukan perubahan berikutnya yang menjaga Remaining 10 (Delete satu aset lalu registrasi satu aset) hingga berhasil tersimpan
65. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
66. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 57 (penanda belum naik)
67. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
68. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding langkah 57: Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
69. Tutup modal `Changelog: Allocation Quota`

### TC-FA-LIC-492: Kegagalan panggilan penilaian pasca-commit tidak memblokir registrasi dan dinilai ulang oleh job per jam

70. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4` (Remaining 11), penanda Normal, dan panggilan `assess_license_quota_alert` digagalkan hingga tersimpan
71. Registrasi satu aset tanpa approval hingga berhasil tersimpan
72. Buka License > All License
73. Verifikasi License Summary kolom Asset Used `86` (registrasi berhasil walau panggilan penilaian gagal)
74. Muat ulang halaman Fixed Asset > Dashboard
75. Buka Notification Center akun Pre-setup #1, scroll sampai seluruh item termuat, lalu catat jumlah notifikasi `Asset license quota is running low`; catat jumlah notifikasi `Asset license quota is running low` pada daftar notifikasi akun Pre-setup #3 lewat kemampuan baca BE
76. Pulihkan panggilan `assess_license_quota_alert` lewat fixture BE hingga tersimpan
77. Geser jam fixture sampai job per jam berjalan, lalu pulihkan jam fixture
78. Buka Notification Center akun Pre-setup #1 dan scroll sampai seluruh item termuat
79. Verifikasi Notification Center akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 (kemampuan baca BE) masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding jumlah pada langkah 75 (job sebagai jaring pengaman)
80. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (job penilaian per jam atas penanda tingkat peringatan kuota). `P-5` butir (b): TC-FA-LIC-430 (pembuatan event digagalkan) dan TC-FA-LIC-492 (panggilan penilaian digagalkan) adalah dua TC objek-uji ringan kelas b tanpa harness eksternal sendiri; keduanya berada di spec ini karena permukaan yang diasersi sama (notifikasi dan penanda tingkat) dengan job per jam, dan keduanya memakai fixture BE (bukan intercept) sebagai pemicu kegagalan.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 23, 34, 42, 43, 55, 70, dan 80 (fixture BE pemulih dan penyetel state), langkah 15, 28, 36, dan 77 (menggeser jam fixture lalu memulihkannya; langkah 28 juga mencatat waktu job sebagai acuan langkah 30, S-12), langkah 63 dan 76 (memulihkan pembuatan event dan panggilan penilaian), langkah 4 (membuka halaman License dari Dashboard tanpa menggeser jam fixture, sesuai TC-FA-LIC-429 langkah 1), menutup modal Changelog, `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi, membuka Notification Center dan scroll sampai seluruh item termuat, serta pencatatan baseline pada langkah 3, 24, 35, 45, 57, dan 75 (S-12). Nilai Remaining dan Used dalam kurung pada TC (mis. Remaining 10 sesudah registrasi atau Delete) tidak ditulis di langkah aksi (R-02): fixture mengatur state awal sesuai Precondition.
- Langkah penghubung muat ulang (S-03, aksi tanpa `Verifikasi`, 8b.10): `Muat ulang halaman Fixed Asset > Dashboard` pada langkah 2, 44, 56, dan 74, tepat sesudah fixture BE pemulih seed dan sebelum langkah yang mencatat baseline notifikasi atau mengasersi UI (juga menutup Dropdown Panel).
- Entri yang dibuat saat jam digeser bercap waktu di masa depan sehingga setelah jam dipulihkan entri baru bisa jatuh di bawahnya; entri pada langkah 19, 22, 31, 38, dan 68 dicari berdasarkan Field dan nilai serta selisih jumlah entri, bukan posisi teratas (S-12).
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` jumlah baseline termuat sebagai anchor absence notifikasi (8b.2), `Verifikasi` Remaining `8` setelah muat ulang halaman License pada TC-FA-LIC-429, dan `Verifikasi` tidak ada entri Activity Log `Quota Alert Level` baru sebelum job pada TC-FA-LIC-429 (Expected c: sebelum job tidak ada entri penanda).
- Alasan di atas sekitar 35 langkah (80 langkah): semua blok satu topik (penilaian peringatan kuota tenant oleh job per jam dan pasca-commit) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pembacaan baseline, penutupan modal, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-430 dan TC-FA-LIC-492 berlabel `Manual Only — (b)` (kegagalan sisi server tidak dapat dipicu dari klien); spec menuliskan pemicunya sebagai fixture BE yang disediakan tim FE/BE.
  - TC-FA-LIC-491 tidak menyebut cara membaca penanda tingkat; spec memakai kemampuan membaca penanda tingkat lewat fixture BE.
  - TC-FA-LIC-492 langkah 2 "Periksa daftar aset dan notifikasi ..." tidak punya Expected untuk notifikasi sebelum job; spec mencatat jumlah notifikasi itu sebagai baseline job, mengasersi Used bertambah (Used 86) dan notifikasi sesudah job.
  - TC-FA-LIC-429 dan TC-FA-LIC-546 tidak menyebut format Date persis; spec memakai format General Settings Pre-setup #1 (`dd/MM/yy`, `HH:mm`).
