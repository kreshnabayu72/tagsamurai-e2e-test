---
id: TC-FA-LIC-E2E-128-peringatan-kuota-tenant-starter-tanpa-ledger-perubahan
title: "Peringatan Kuota Tenant: Aksi Manage, Starter Tanpa Ledger, Perubahan Cap Plan, dan Term Trial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-509
  - TC-FA-LIC-603
  - TC-FA-LIC-604
  - TC-FA-LIC-605
coverage:
  web: automated
---

# Peringatan Kuota Tenant: Aksi Manage, Starter Tanpa Ledger, Perubahan Cap Plan, dan Term Trial

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono), akun awal hook `before` | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| Pre-setup #9 | Total Control client Starter | `totalControlStarter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STARTER_TC_PASSWORD` |
| Pre-setup #32 | Total Control client term Trial Free | `totalControlTrialFree_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TRIALFREE_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; ganti akun ke Pre-setup #9 (langkah 6) dan Pre-setup #32 (langkah 28) memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; setiap `Spectra.env.*` di atas didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): Total Asset License, cap plan Starter, Trial Asset Quota, Used, Reserved, penanda tingkat peringatan kuota, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, penanda tingkat Normal; penerima #3 dan #1), #28 (satu aset Unmanaged di grup level 1 tanpa alokasi pada tenant Pre-setup #16 dengan sisa pool organisasi cukup; pemicu aksi Manage sesuai PRD `asset/`), #9 (client Starter, term non-Trial), dan #32 (client dengan hanya term Trial Active, plan term Free; approval OFF; Trial Asset Quota, Used, Reserved, dan penanda tingkat dapat diatur lewat fixture BE). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-509 Total 100, penanda Normal, Used 85, Reserved 4 (Remaining 11); blok TC-FA-LIC-603 Starter dengan cap plan 100 (Pre-setup #9 diubah), Used 99, Reserved 0, penanda Normal, tanpa ledger Asset License (Total dari cap plan); blok TC-FA-LIC-604 Starter dengan cap plan 100 (Pre-setup #9 diubah), Used 85, Reserved 0, penanda Normal, lalu cap plan diturunkan menjadi 90 (Remaining 5, ambang Low 9) tanpa perubahan Used atau Reserved; blok TC-FA-LIC-605 Trial Asset Quota 100 (Pre-setup #32 diubah), Used 89, Reserved 0, penanda Normal.
- Blok TC-FA-LIC-509 berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1; Reserved dari Manage); pemicu aksi Manage disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant dan aset Pre-setup #9, #16, #28, dan #32 bernama literal karena Total Asset License, cap plan, Trial Asset Quota, Used, dan penanda tingkat tidak dapat dimiliki spec. Pemulihan ke Pre-setup dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, cap plan, Trial Asset Quota, Used, Reserved, penanda tingkat, status aset, dan entri Activity Log dan notifikasi (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 dan kemampuan membaca penanda tingkat peringatan kuota lewat fixture BE; kemampuan membaca jumlah entri Activity Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12), semuanya disediakan tim FE/BE (endpoint tidak dikarang). Jam fixture digeser maju sampai job per jam berjalan lalu dipulihkan pada langkah yang sama; sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`), dan entri dicari berdasarkan Field `Quota Alert Level`, Old Value, dan New Value (bukan posisi teratas).
- Asersi absence notifikasi in-app didahului anchor positif dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-509: Aksi Manage yang menurunkan Remaining tenant ke ambang Low memicu penilaian pasca-commit

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Total `100`, penanda Normal, Used `85`, Reserved `4`, dan 1 aset Unmanaged di grup level 1 tanpa alokasi (Pre-setup #28) hingga tersimpan
2. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
3. Jalankan aksi Manage atas 1 aset Unmanaged sesuai PRD `asset/` (Reserved 5, Remaining 10)
4. Verifikasi penilaian peringatan kuota dipanggil pasca-commit setelah aksi Manage dan menilai tingkat `Low` (Remaining 10 ≤ 10% dari Total 100) tanpa menunggu job per jam
5. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `license_quota_low` (`Asset license quota is running low`)

### Ganti akun ke Total Control client Starter

6. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client Starter (Pre-setup #9)

### TC-FA-LIC-603: Peringatan kuota Full berlaku pada tenant Starter tanpa ledger Asset License

7. Jalankan fixture BE pemulih Pre-setup #9 dengan cap plan 100, Used `99`, Reserved `0`, penanda Normal, tanpa ledger Asset License, dan approval OFF hingga tersimpan
8. Catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada Bell Notification akun Pre-setup #9, serta jumlah entri Activity Log dengan Field `Quota Alert Level`
9. Registrasi satu aset tanpa approval sehingga Remaining 0
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi Bell Notification akun Pre-setup #9 memuat tepat satu notifikasi baru `Asset license quota is full` dengan Body `No asset license remains available. New asset registrations are blocked until more quota is added.`
12. Verifikasi tidak ada notifikasi baru `license_quota_low` dibanding langkah 8
13. Buka Fixed Asset > Reports & Logs > Activity Log
14. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 8: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Full`, Modified By `System`

### TC-FA-LIC-604: Perubahan cap konfigurasi plan Starter dinilai oleh job per jam, bukan saat halaman License dibuka

15. Jalankan fixture BE pemulih Pre-setup #9 dengan cap plan 100, Used `85`, Reserved `0`, dan penanda Normal, lalu turunkan cap plan menjadi `90` (Remaining 5, ambang Low 9) tanpa perubahan Used atau Reserved hingga tersimpan
16. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #9, serta jumlah entri Activity Log dengan Field `Quota Alert Level`
17. Buka License > All License (job belum berjalan)
18. Verifikasi kolom `Asset`: `Total` `90` dan `Remaining` `5`
19. Tunggu 5 detik tanpa memuat ulang halaman
20. Verifikasi Bell Notification akun Pre-setup #9 termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 16
21. Verifikasi Bell Notification akun Pre-setup #9 tidak memuat notifikasi kuota baru dibanding langkah 16 (membuka halaman License tidak memicu penilaian)
22. Buka Fixed Asset > Reports & Logs > Activity Log
23. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 16
24. Geser jam fixture sampai job per jam berjalan, lalu pulihkan jam fixture
25. Verifikasi Bell Notification akun Pre-setup #9 memuat tepat satu notifikasi baru `Asset license quota is running low` dengan Body `5 of 90 asset licenses remain available.`
26. Muat ulang halaman Activity Log
27. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 16: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`

### Ganti akun ke Total Control client term Trial

28. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client dengan hanya term Trial Active (Pre-setup #32)

### TC-FA-LIC-605: Peringatan kuota Low berlaku pada term Trial dengan Total dari Trial Asset Quota

29. Jalankan fixture BE pemulih Pre-setup #32 dengan Trial Asset Quota `100`, Used `89`, Reserved `0`, penanda Normal, dan approval OFF hingga tersimpan
30. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #32, serta jumlah entri Activity Log dengan Field `Quota Alert Level`
31. Registrasi satu aset tanpa approval (Used 90, Remaining 10)
32. Verifikasi Bell Notification akun Pre-setup #32 memuat tepat satu notifikasi baru `Asset license quota is running low` dengan Body `10 of 100 asset licenses remain available.`
33. Buka License > All License
34. Verifikasi kolom `Asset`: `Total` sama dengan Trial Asset Quota `100`
35. Buka Fixed Asset > Reports & Logs > Activity Log
36. Verifikasi Activity Log bertambah tepat satu entri dibanding langkah 30: Action `Edit`, Object `License`, Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
37. Jalankan fixture BE pemulih Pre-setup #32, #9, dan #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (penilaian peringatan kuota tenant, termasuk job per jam pada TC-FA-LIC-604). Banner pada spec lain memakai fixture tanggal, bukan time-travel; spec ini hanya menggeser jam untuk job per jam.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 7, 15, 29, dan 37 (fixture BE pemulih dan penyetel state), langkah 24 (menggeser jam fixture lalu memulihkannya), langkah 26 (muat ulang Activity Log), navigasi License dan Activity Log, serta pencatatan baseline pada langkah 2, 8, 16, dan 30 (S-12). Ganti akun pada langkah 6 dan 28 mengikuti S-07. Langkah `Tunggu 5 detik tanpa memuat ulang halaman` mendahului asersi absence notifikasi.
- Urutan TC diubah dari urutan nomor: dikelompokkan per akun (Pre-setup #1, #9, lalu #32) agar ganti akun hanya dua kali (S-10).
- TC-FA-LIC-603 Expected c ("penilaian tidak dilewati walau tidak ada ledger Asset License") adalah kesimpulan dari notifikasi dan entri penanda pada langkah 11 dan 14 yang tidak teramati terpisah; tidak ada `Verifikasi` tersendiri (S-03).
- Temuan untuk QA:
  - TC-FA-LIC-509 Expected a tidak menyebut cara mengamati penilaian Low selain notifikasi; spec memakai kemampuan membaca penanda tingkat.
  - TC-FA-LIC-603, TC-FA-LIC-604, dan TC-FA-LIC-605 tidak menyebut approval ON atau OFF untuk Starter; spec memakai approval OFF seperti pada Precondition TC-FA-LIC-605.
  - TC-FA-LIC-603 Expected b tidak mengasersi kolom Date entri Activity Log; spec tidak mengasersinya.
- Alasan di atas 35 langkah (37 langkah): semua blok satu topik (Starter tanpa ledger perubahan) dan berdiri sendiri; langkah di atas 35 berasal dari anchor positif dan jeda 5 detik sebelum asersi absence; kegagalan satu blok tidak membuat blok lain kehilangan makna.
