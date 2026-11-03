---
id: TC-AC-LCS-E2E-164-recycle-bin-countdown-reset-job-ketahanan
title: "Countdown Reset Job Recycle Bin: Reset pada Nilai 30, Respons Save Tanpa Menunggu Job, dan Schema Client Terhapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-574
  - TC-AC-LCS-575
  - TC-AC-LCS-576
coverage:
  web: automated
---

# Countdown Reset Job Recycle Bin: Reset pada Nilai 30, Respons Save Tanpa Menunggu Job, dan Schema Client Terhapus

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: Countdown Reset Job sebagai objek uji; penundaan job hanya untuk mengamati urutan respons).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Pengamat: Default User Client PT Maju Jaya (TC 570 menyebut "Default User Client PT Maju Jaya"; TC 571 sampai 578 menyebut "User Client PT Maju Jaya"), `defaultUserClientMajuJaya_automated_{namaCompany}@qwertysystem.net` (Pre-setup 13, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), password dari `Spectra.env.AC_DUCLIENT_PASSWORD`; ganti akun ke pengamat dan kembali ke Total Control memakai langkah eksplisit.
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct) dengan file Recycle Bin `laporan-a.pdf` (dihapus 10 hari lalu) dan `laporan-b.pdf` (dihapus 25 hari lalu), dan `laporan-c.pdf` pada TC 578; diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite. Nilai awal Permanently Delete Recycle Bin `30` (default).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal hapus item Recycle Bin, menunda atau memaksa gagal Countdown Reset Job, memicu daily sweep, membaca status dan antrean job, serta memajukan jam server dan jam browser. Countdown dihitung dari tanggal hapus item; kolom Auto-Purge In dibaca pada Global Settings > File Manager > Recycle Bin.
- State global: konfigurasi tab Recycle Bin, item Recycle Bin PT Maju Jaya, antrean job, dan jam server dan jam browser diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-574: Reset to Default saat nilai sudah 30 tidak mengantrekan job dan nilai countdown tidak berubah

1. Atur lewat Fixture BE: ketujuh tab pada nilai default dan Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu; catat baseline antrean Countdown Reset Job
2. Klik tab Recycle Bin
3. Klik `[Reset to Default]`
4. Verifikasi toast sukses "Success, recycle bin settings have been reset to default."
5. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
6. Verifikasi `laporan-a.pdf` menampilkan Auto-Purge In `20 days` (tidak berubah)
7. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `5 days` (tidak berubah)
8. Periksa antrean job lewat Fixture BE
9. Verifikasi tidak ada Countdown Reset Job yang diantrekan (selisih antrean terhadap baseline 0)
10. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-575: Respons Save tidak menunggu Countdown Reset Job selesai

11. Atur lewat Fixture BE: Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu; Countdown Reset Job ditunda
12. Klik tab Recycle Bin
13. Ubah Permanently Delete Recycle Bin dari `30` menjadi `15` lalu klik `[Save]`
14. Verifikasi toast sukses "Success, recycle bin settings have been saved." tampil tanpa menunggu job
15. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
16. Verifikasi `laporan-a.pdf` masih menampilkan Auto-Purge In `20 days` (job belum selesai)
17. Lepaskan penundaan Countdown Reset Job lewat Fixture BE, tunggu job selesai, lalu muat ulang Recycle Bin
18. Verifikasi `laporan-a.pdf` menampilkan Auto-Purge In `5 days`
19. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `2 days`
20. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-576: Schema client yang terhapus saat job berjalan dilewati dan client lain tetap diproses

21. Atur lewat Fixture BE: Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu; Client PT Lama Terhapus memiliki item Recycle Bin dan schema client dihapus saat job berjalan
22. Klik tab Recycle Bin
23. Ubah Permanently Delete Recycle Bin dari `30` menjadi `15` lalu klik `[Save]`
24. Tunggu aksi `[Save]` dan Countdown Reset Job selesai (status job dibaca lewat Fixture BE)
25. Verifikasi job selesai tanpa error fatal (status job dibaca lewat Fixture BE)
26. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
27. Verifikasi `laporan-a.pdf` menampilkan Auto-Purge In `5 days` (client lain tetap diproses)
28. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `2 days` (client lain tetap diproses)
29. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Tiap TC memulihkan item Recycle Bin lewat Fixture BE sebelum aksi (S-06, S-09).
- Langkah Reset to Default pada TC 574 tidak memuat dialog konfirmasi karena TC tidak menyebutnya.
- Temuan untuk QA:
  - Akun Default User Client PT Maju Jaya kini tertulis di Pre-setup 13 sebagai usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE; password dari `Spectra.env.AC_DUCLIENT_PASSWORD`.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
  - TC 574 Expected b menyebut `20 days` dan `5 days` "tidak berubah"; spec mengasersi kedua nilai per file sebagai dua `Verifikasi`.
  - TC 576 Expected a ("Job selesai tanpa error fatal") tidak menyebut cara pengamatan; spec membaca status job lewat Fixture BE.
  - TC 576 memuat Client PT Lama Terhapus yang tidak ada di Pre-setup 10; diatur lewat Fixture BE sebagai precondition TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 5, 8, 10-12, 15, 17, 20-22, 24, 26, 29.
