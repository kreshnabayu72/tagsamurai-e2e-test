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
coverage:
  web: automated
---

# Peringatan Kuota Tenant: Ambang Low dan Full serta Transisi Penanda Tingkat

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
- Suite berjalan serial (`parallel: false`): Total Asset License, Used, Reserved, penanda tingkat peringatan kuota, dan status aset dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #16 (tenant peringatan kuota Total Asset License 100, variasi 105; penanda tingkat Normal; Used dan Reserved diatur fixture BE; approval OFF dengan sekurangnya 60 draf aset siap Submit; penerima #3 dan #1). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-423 dan TC-FA-LIC-424 Used 85 dan Reserved 4 (Remaining 11); blok TC-FA-LIC-425 Total 105, Used 94, Reserved 0 (Remaining 11); blok TC-FA-LIC-426 penanda Low sudah tercatat dan Remaining 1; blok TC-FA-LIC-427 Used 85, Reserved 4 (Remaining 11), dan 11 draf aset.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah tenant Pre-setup #16 bernama literal karena Total Asset License, Used, dan penanda tingkat tidak dapat dimiliki spec. Pemulihan ke Pre-setup #16 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Remaining, penanda tingkat, status aset, dan entri Changelog dan Activity Log (audit trail permanen) bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 lewat fixture BE (disediakan tim FE/BE; endpoint tidak dikarang); kemampuan membaca jumlah entri Changelog: Allocation Quota dan Activity Log sebagai baseline (audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12). Kemampuan menggeser jam fixture sampai job penilaian per jam berjalan (TC-FA-LIC-425 langkah 2); penilaian lainnya dipicu pasca-commit oleh registrasi dan Delete aset.
  - Asersi absence notifikasi in-app didahului anchor positif dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-423: Peringatan Low, Remaining turun ke 10 dari 100 mengirim satu license_quota_low

1. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, penanda Normal, approval OFF, dan draf aset hingga tersimpan
2. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
3. Registrasi satu aset tanpa approval (Used 86, Remaining 10)
4. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is running low` dengan Body `10 of 100 asset licenses remain available.`
5. Registrasi satu aset lagi (Remaining 9)
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Verifikasi notifikasi `Asset license quota is running low` dari langkah 4 tetap tampil pada Bell Notification akun Pre-setup #1
8. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi baru dibanding setelah langkah 3 (Remaining 9 masih Low)

### TC-FA-LIC-424: Batas Low, Remaining 11 dari 100 tidak mengirim peringatan

9. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `85`, Reserved `4`, dan penanda Normal hingga tersimpan
10. Catat jumlah notifikasi kuota pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3, serta jumlah entri `Changelog: Allocation Quota` dan Activity Log dengan Field `Quota Alert Level`
11. Lakukan perubahan yang membuat Remaining tetap 11 (Delete satu aset lalu registrasi satu aset)
12. Tunggu 5 detik tanpa memuat ulang halaman
13. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 termuat dan menampilkan jumlah notifikasi kuota yang tercatat pada langkah 10
14. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 tidak memuat notifikasi kuota baru dibanding langkah 10
15. Buka License > Allocation Quota; klik ikon Changelog pada toolbar Section 2
16. Verifikasi `Changelog: Allocation Quota` tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 10
17. Tutup modal `Changelog: Allocation Quota`
18. Buka Fixed Asset > Reports & Logs > Activity Log
19. Verifikasi Activity Log tidak memuat entri baru dengan Field `Quota Alert Level` dibanding langkah 10

### TC-FA-LIC-425: Ambang 10% pada Total tidak kelipatan 10 (Total 105)

20. Jalankan fixture BE pemulih Pre-setup #16 dengan Total `105`, penanda Normal, Used `94`, dan Reserved `0` (Remaining 11) hingga tersimpan
21. Catat jumlah notifikasi `Asset license quota is running low` pada Bell Notification akun Pre-setup #1
22. Registrasi satu aset (Remaining 10)
23. Verifikasi Bell Notification akun Pre-setup #1 memuat tepat satu notifikasi baru `license_quota_low` dengan Body `10 of 105 asset licenses remain available.` (Remaining 10 ≤ 10,5)
24. Pulihkan Remaining ke 11 lewat fixture BE hingga tersimpan
25. Geser jam fixture sampai job penilaian per jam berjalan
26. Tunggu 5 detik tanpa memuat ulang halaman
27. Verifikasi notifikasi `license_quota_low` dari langkah 23 tetap tampil pada Bell Notification akun Pre-setup #1
28. Verifikasi Bell Notification akun Pre-setup #1 tidak memuat notifikasi baru dibanding setelah langkah 22 (Remaining 11 > 10,5)

### TC-FA-LIC-426: Peringatan Full, Remaining 0 mengirim license_quota_full termasuk setelah Low terkirim

29. Jalankan fixture BE pemulih Pre-setup #16 dengan penanda Low tercatat dan Remaining `1` hingga tersimpan
30. Catat jumlah notifikasi `Asset license quota is full` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
31. Registrasi satu aset sehingga Remaining 0
32. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is full` dengan Body `No asset license remains available. New asset registrations are blocked until more quota is added.`

### TC-FA-LIC-427: Normal langsung ke Full hanya mengirim license_quota_full

33. Jalankan fixture BE pemulih Pre-setup #16 dengan penanda Normal, Used `85`, Reserved `4` (Remaining 11), approval OFF, dan 11 draf aset hingga tersimpan
34. Catat jumlah notifikasi `Asset license quota is full` dan `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
35. Registrasi massal 11 aset (Remaining 11 → 0) pada penanda Normal
36. Tunggu 5 detik tanpa memuat ulang halaman
37. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `license_quota_full` (`Asset license quota is full`)
38. Verifikasi tidak ada notifikasi baru `license_quota_low` (`Asset license quota is running low`) dibanding langkah 34
39. Jalankan fixture BE pemulih Pre-setup #16 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini berkelas d (peringatan kuota tenant dan penanda tingkat oleh `assess_license_quota_alert()`); blok di spec ini dipicu pasca-commit oleh registrasi dan Delete aset, kecuali TC-FA-LIC-425 yang menggeser jam fixture sampai job penilaian per jam berjalan; blok yang memerlukan job per jam dan top-up Total lainnya ada di spec 126, 127, 128, dan 145.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 9, 20, 29, 33, dan 39 (fixture BE pemulih dan penyetel state), langkah 17 (menutup modal Changelog), langkah 24 (memulihkan Remaining) dan 25 (menggeser jam fixture), langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi, serta pencatatan baseline pada langkah 2, 10, 21, 30, dan 34 (S-12). Pada TC-FA-LIC-424 asersi "tidak ada entri baru" berupa asersi jumlah dengan baseline langkah 10, bukan asersi absence kelas g (bagian 3 prinsip 13).
- Urutan TC mengikuti urutan nomor; pembagian TC lintas spec: TC-FA-LIC-428 dan TC-FA-LIC-532 (penanda turun setelah top-up) ada di spec 145.
- Temuan untuk QA:
  - TC-FA-LIC-424 dan TC-FA-LIC-426 sampai TC-FA-LIC-427 tidak menyebut akun yang periksa Bell pada beberapa langkah; spec mengasersi akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 sesuai Precondition Pre-setup #16.
  - TC-FA-LIC-424 mengasersi tidak ada entri baru pada Changelog dan Activity Log; spec membandingkan jumlah entri dengan baseline.
- Alasan di atas 35 langkah (39 langkah): semua blok satu topik (ambang peringatan kuota Low dan Full) dan berdiri sendiri; langkah di atas 35 berasal dari pemicu job penilaian, anchor positif, dan jeda 5 detik; kegagalan satu blok tidak membuat blok lain kehilangan makna.
