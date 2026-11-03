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
| Pre-setup #1 | Total Control (Rudi Hartono), penerima dan aktor | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima peringatan kuota (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` dan `Spectra.env.FA_MGL_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): Total Asset License, Used, Reserved, penanda tingkat peringatan kuota, status aset, pembuatan event notifikasi, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1) dan #1 (jumlah entri System Log Rudi Hartono dicatat pada blok TC-FA-LIC-547). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-429, TC-FA-LIC-546, dan TC-FA-LIC-547 Total diturunkan di Admin Console sehingga Remaining 8 tanpa perubahan lokal (penanda Normal); blok TC-FA-LIC-491 penanda Low tercatat (Used 90, Remaining 10); blok TC-FA-LIC-430 pembuatan event notifikasi digagalkan, Used 85, Reserved 4 (Remaining 11), penanda Normal; blok TC-FA-LIC-492 Used 85, Reserved 4 (Remaining 11), penanda Normal, dan panggilan `assess_license_quota_alert` digagalkan.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant Pre-setup #16 bernama literal karena Total Asset License, Used, dan penanda tingkat tidak dapat dimiliki spec. Pemulihan ke Pre-setup #16 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, Used, Reserved, penanda tingkat, jam fixture, status aset, dan entri Changelog, Activity Log, dan notifikasi (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 lewat fixture BE; kemampuan membaca penanda tingkat peringatan kuota tenant lewat fixture BE; fixture BE yang menggagalkan pembuatan event notifikasi dan panggilan `assess_license_quota_alert` (semuanya disediakan tim FE/BE; endpoint tidak dikarang); kemampuan membaca jumlah entri `Changelog: Allocation Quota`, Activity Log, dan System Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12). Jam fixture digeser maju sampai job per jam berjalan: sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`), entri dicari berdasarkan Field `Quota Alert Level`, Old Value, dan New Value (bukan posisi teratas), jam dipulihkan pada langkah yang sama dengan penggeseran sehingga akun aktor membuka Activity Log dan halaman lain setelah jam kembali (S-09), dan penantian job tidak memakai jeda nyata.

## Test Steps

### TC-FA-LIC-429: Job penilaian per jam menilai perubahan Total dari Admin Console, bukan saat halaman License dibuka

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Total diturunkan di Admin Console sehingga Remaining `8` tanpa perubahan lokal dan penanda Normal hingga tersimpan
2. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, serta jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level`
3. Muat ulang halaman License (tanpa job)
4. Verifikasi `Remaining` kolom `Asset` `8`
5. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi baru dibanding langkah 2 (membuka halaman License tidak memicu penilaian)
6. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
7. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 2 (sebelum job)
8. Tutup modal `Changelog: Allocation Quota`
9. Geser jam fixture sampai job jam berikutnya berjalan, lalu pulihkan jam fixture
10. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` (job berjalan dengan interval 1 jam)
11. Klik ikon Changelog pada toolbar Section 2
12. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding langkah 2: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
13. Tutup modal `Changelog: Allocation Quota`
14. Buka Fixed Asset > Reports & Logs > Activity Log
15. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 2: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`

### TC-FA-LIC-546: Changelog: Allocation Quota, perubahan penanda oleh job tercatat dengan Modified By System

16. Jalankan fixture BE pemulih Pre-setup #16 dengan Total diturunkan di Admin Console sehingga Remaining `8` dan penanda Normal hingga tersimpan
17. Catat jumlah entri `Changelog: Allocation Quota` dengan Field `Quota Alert Level`
18. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
19. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 17 (sebelum job)
20. Tutup modal `Changelog: Allocation Quota`
21. Geser jam fixture sampai job penilaian per jam berjalan, lalu pulihkan jam fixture
22. Buka kembali modal `Changelog: Allocation Quota` dengan klik ikon Changelog pada toolbar Section 2
23. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding langkah 17 dengan Date sesuai waktu job (jam fixture, format General Settings `dd/MM/yy HH:mm`, toleransi satu menit)
24. Verifikasi entri baru itu: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
25. Verifikasi Action dan nilai entri baru itu ditulis plain text (bukan badge)
26. Tutup modal `Changelog: Allocation Quota`

### TC-FA-LIC-547: Activity Log dan System Log, perubahan penanda oleh job tercatat di Activity Log tanpa entri System Log

27. Jalankan fixture BE pemulih Pre-setup #16 dengan Total diturunkan di Admin Console sehingga Remaining `8` dan penanda Normal hingga tersimpan
28. Catat jumlah entri Activity Log dengan Field `Quota Alert Level` dan jumlah entri System Log Rudi Hartono (Pre-setup #1)
29. Geser jam fixture sampai job penilaian per jam berjalan, lalu pulihkan jam fixture
30. Buka Fixed Asset > Reports & Logs > Activity Log
31. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 28: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
32. Buka Global Settings > User > Detail Rudi Hartono > Tab System Log
33. Verifikasi Tab System Log Rudi Hartono memuat sedikitnya satu entri
34. Verifikasi jumlah entri System Log Rudi Hartono tidak bertambah dibanding langkah 28 (penilaian tidak punya user aktor)
35. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

### TC-FA-LIC-491: Delete aset memanggil penilaian pasca-commit, penanda turun ke Normal tanpa menunggu job per jam

36. Jalankan fixture BE pemulih Pre-setup #16 dengan penanda Low tercatat (Used 90, Remaining 10) dan approval OFF hingga tersimpan
37. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
38. Delete satu aset Active (Used 89, Remaining 11)
39. Verifikasi penanda tingkat Normal tanpa menunggu job per jam
40. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi baru dibanding langkah 37
41. Registrasi satu aset tanpa approval (Remaining 10)
42. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low`

### TC-FA-LIC-430: Kegagalan membuat event tidak menaikkan penanda dan tidak memblokir transaksi pemicu

43. Jalankan fixture BE pemulih Pre-setup #16 dengan pembuatan event notifikasi digagalkan, Used `85`, Reserved `4` (Remaining 11), dan penanda Normal hingga tersimpan
44. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, serta jumlah entri `Changelog: Allocation Quota` dengan Field `Quota Alert Level`
45. Registrasi satu aset sehingga Remaining 10 (event gagal)
46. Verifikasi registrasi berhasil walau event gagal
47. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
48. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 44 (penanda tidak naik)
49. Tutup modal `Changelog: Allocation Quota`
50. Pulihkan pembuatan event lewat fixture BE hingga tersimpan
51. Lakukan perubahan berikutnya yang menjaga Remaining 10 (Delete satu aset lalu registrasi satu aset)
52. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` (penanda belum naik)
53. Klik ikon Changelog pada toolbar Section 2
54. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding langkah 44: Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
55. Tutup modal `Changelog: Allocation Quota`

### TC-FA-LIC-492: Kegagalan panggilan penilaian pasca-commit tidak memblokir registrasi dan dinilai ulang oleh job per jam

56. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4` (Remaining 11), penanda Normal, dan panggilan `assess_license_quota_alert` digagalkan hingga tersimpan
57. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
58. Registrasi satu aset tanpa approval sehingga Remaining 10
59. Buka License > All License
60. Verifikasi License Summary kolom Asset Used `86` (registrasi berhasil walau panggilan penilaian gagal)
61. Pulihkan panggilan `assess_license_quota_alert` lewat fixture BE hingga tersimpan
62. Geser jam fixture sampai job per jam berjalan, lalu pulihkan jam fixture
63. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dibanding langkah 57 (job sebagai jaring pengaman)
64. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (job penilaian per jam atas penanda tingkat peringatan kuota). `P-5` butir (b): TC-FA-LIC-430 (pembuatan event digagalkan) dan TC-FA-LIC-492 (panggilan penilaian digagalkan) adalah dua TC objek-uji ringan kelas b tanpa harness eksternal sendiri; keduanya berada di spec ini karena permukaan yang diasersi sama (notifikasi dan penanda tingkat) dengan job per jam, dan keduanya memakai fixture BE (bukan intercept) sebagai pemicu kegagalan.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 16, 27, 35, 36, 43, 56, dan 64 (fixture BE pemulih dan penyetel state), langkah 9, 21, 29, dan 62 (menggeser jam fixture lalu memulihkannya), langkah 50 dan 61 (memulihkan pembuatan event dan panggilan penilaian), langkah 8, 13, 20, 26, 49, dan 55 (menutup modal Changelog), serta pencatatan baseline pada langkah 2, 17, 28, 37, 44, dan 57 (S-12).
- Entri yang dibuat saat jam digeser bercap waktu di masa depan sehingga setelah jam dipulihkan entri baru bisa jatuh di bawahnya; entri pada langkah 12, 15, 24, dan 31 dicari berdasarkan Field dan nilai serta selisih jumlah entri, bukan posisi teratas (S-12).
- Alasan di atas sekitar 35 langkah (64 langkah): semua blok satu topik (penilaian peringatan kuota tenant oleh job per jam dan pasca-commit) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pembacaan baseline, penutupan modal, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-430 dan TC-FA-LIC-492 berlabel `Manual Only — (b)` (kegagalan sisi server tidak dapat dipicu dari klien); spec menuliskan pemicunya sebagai fixture BE yang disediakan tim FE/BE.
  - TC-FA-LIC-491 tidak menyebut cara membaca penanda tingkat; spec memakai kemampuan membaca penanda tingkat lewat fixture BE.
  - TC-FA-LIC-492 langkah 2 "Periksa daftar aset dan Bell" tidak punya Expected untuk Bell sebelum job; spec hanya mengasersi Used bertambah (Used 86) dan notifikasi sesudah job.
  - TC-FA-LIC-429 dan TC-FA-LIC-546 tidak menyebut format Date persis; spec memakai format General Settings Pre-setup #1 (`dd/MM/yy`, `HH:mm`).
