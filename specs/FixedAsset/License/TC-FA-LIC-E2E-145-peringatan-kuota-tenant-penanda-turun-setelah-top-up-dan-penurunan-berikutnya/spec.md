---
id: TC-FA-LIC-E2E-145-peringatan-kuota-tenant-penanda-turun-setelah-top-up-dan-penurunan-berikutnya
title: "Peringatan Kuota Tenant: Penanda Turun Setelah Top-up dan Penurunan Berikutnya Mengirim Low"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-428
  - TC-FA-LIC-532
coverage:
  web: automated
---

# Peringatan Kuota Tenant: Penanda Turun Setelah Top-up dan Penurunan Berikutnya Mengirim Low

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
- Suite berjalan serial (`parallel: false`): Total Asset License, Used, Reserved, penanda tingkat peringatan kuota, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-428 penanda Low tercatat dengan Remaining 10; blok TC-FA-LIC-532 penanda Full tercatat dengan Used 96, Reserved 4, dan Remaining 0. Top-up +50 pada Total Asset License di Admin Console (Total 150) dilakukan lewat fixture BE yang disediakan tim FE/BE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant Pre-setup #16 bernama literal karena Total Asset License, Used, dan penanda tingkat tidak dapat dimiliki spec. Pemulihan ke Pre-setup #16 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, Used, Reserved, penanda tingkat, jam fixture, status aset, dan entri Changelog dan Activity Log (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 lewat fixture BE (disediakan tim FE/BE; endpoint tidak dikarang); kemampuan membaca jumlah entri `Changelog: Allocation Quota` dan Activity Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12). Jam fixture digeser maju sampai job penilaian per jam berjalan: sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`), entri dicari berdasarkan Field `Quota Alert Level`, Old Value, dan New Value (bukan posisi teratas), dan jam dipulihkan pada langkah yang sama dengan penggeseran sehingga akun aktor membuka Activity Log setelah jam kembali (S-09), serta di hook `after`.
- Asersi absence notifikasi in-app didahului anchor positif dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-428: Penanda turun saat Remaining naik, top-up lalu penurunan berikutnya mengirim Low lagi

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Total `100`, penanda Low tercatat (Remaining 10), dan approval OFF hingga tersimpan
2. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, serta jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level`
3. Top-up +50 pada Total Asset License di Admin Console lewat fixture BE (Total 150, Remaining 60)
4. Geser jam fixture sampai job penilaian berikutnya berjalan, lalu pulihkan jam fixture
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 2
7. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi baru dibanding langkah 2 (penanda turun ke Normal tanpa notifikasi)
8. Tambah Used lewat fixture BE sampai Remaining 16
9. Registrasi satu aset tanpa approval (Remaining 15)
10. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` (penurunan ke ≤ 10% dari Total 150)
11. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
12. Verifikasi `Changelog: Allocation Quota` bertambah tepat dua entri dibanding langkah 2
13. Verifikasi entri baru pertama: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Low`, New Value `Normal`, Modified By `System` (setelah job)
14. Verifikasi entri baru kedua: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System` (setelah penurunan ke ≤ 10%)
15. Tutup modal `Changelog: Allocation Quota`
16. Buka Fixed Asset > Reports & Logs > Activity Log
17. Verifikasi Activity Log bertambah tepat dua entri dengan Field `Quota Alert Level` dibanding langkah 2
18. Verifikasi dua entri itu: Action `Edit`, Object `License`, Name `—`, Modified By `System`, dengan nilai `Low` → `Normal` (setelah job) lalu `Normal` → `Low` (setelah penurunan ke ≤ 10%)
19. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

### TC-FA-LIC-532: Penanda turun dari Full, setelah top-up penurunan berikutnya ke batas Low mengirim license_quota_low

20. Jalankan fixture BE pemulih Pre-setup #16 dengan Total `100`, penanda Full tercatat (Used 96, Reserved 4, Remaining 0), dan approval OFF hingga tersimpan
21. Catat jumlah notifikasi `Asset license quota is running low` dan `Asset license quota is full` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, serta jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level`
22. Top-up +50 pada Total Asset License di Admin Console lewat fixture BE (Total 150, Remaining 50)
23. Geser jam fixture sampai job penilaian berikutnya berjalan, lalu pulihkan jam fixture
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 termuat dan menampilkan jumlah notifikasi yang tercatat pada langkah 21
26. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi baru dibanding langkah 21 (penanda turun ke Normal tanpa notifikasi baru)
27. Tambah Used lewat fixture BE sampai Remaining 16
28. Registrasi satu aset tanpa approval (Remaining 15)
29. Tunggu 5 detik tanpa memuat ulang halaman
30. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low`
31. Verifikasi tidak ada notifikasi baru `Asset license quota is full` dibanding langkah 21 (Remaining masih di atas 0)
32. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
33. Verifikasi `Changelog: Allocation Quota` bertambah tepat dua entri dibanding langkah 21
34. Verifikasi entri baru pertama: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Full`, New Value `Normal`, Modified By `System` (setelah job)
35. Verifikasi entri baru kedua: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System` (setelah registrasi)
36. Tutup modal `Changelog: Allocation Quota`
37. Buka Fixed Asset > Reports & Logs > Activity Log
38. Verifikasi Activity Log bertambah tepat dua entri dengan Field `Quota Alert Level` dibanding langkah 21
39. Verifikasi dua entri itu: Action `Edit`, Object `License`, Name `—`, Modified By `System`, dengan nilai `Full` → `Normal` (setelah job) lalu `Normal` → `Low` (setelah registrasi)
40. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (job penilaian per jam atas penanda tingkat peringatan kuota setelah top-up Total). Pembagian TC lintas spec: TC-FA-LIC-423 sampai TC-FA-LIC-427 ada di spec 125.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 19, 20, dan 40 (fixture BE pemulih dan penyetel state), langkah 3 dan 22 (top-up Total lewat fixture BE), langkah 4 dan 23 (menggeser jam fixture lalu memulihkannya), langkah 8 dan 27 (menambah Used lewat fixture BE), langkah 15 dan 36 (menutup modal Changelog), serta pencatatan baseline pada langkah 2 dan 21 (S-12). Langkah `Tunggu 5 detik tanpa memuat ulang halaman` mendahului asersi absence notifikasi.
- Entri yang dibuat saat jam digeser bercap waktu di masa depan sehingga setelah jam dipulihkan entri baru bisa jatuh di bawahnya; entri Changelog dan Activity Log dicari berdasarkan Field dan nilai serta selisih jumlah entri (S-12).
- Temuan untuk QA:
  - TC-FA-LIC-428 dan TC-FA-LIC-532 tidak menyebut aktor Top-up di Admin Console; disediakan tim FE/BE lewat fixture BE.
  - TC-FA-LIC-428 langkah 1 dan TC-FA-LIC-532 langkah 2 tidak menyebut akun mana yang periksa Bell kecuali "akun Pre-setup #3 dan Pre-setup #1"; spec mengasersi kedua akun.
  - TC-FA-LIC-428 dan TC-FA-LIC-532 tidak mengasersi kolom Date entri; spec tidak mengasersinya karena entri dibuat saat jam digeser.
- Alasan di atas 35 langkah (40 langkah): semua blok satu topik (penanda turun setelah top-up) dan berdiri sendiri; langkah di atas 35 berasal dari anchor positif dan jeda 5 detik sebelum asersi absence; kegagalan satu blok tidak membuat blok lain kehilangan makna.
