---
id: TC-AC-LCS-E2E-196-recycle-bin-countdown-reset-job-sweep-dan-item-terhapus
title: "Countdown Reset Job Recycle Bin: Job Per-Save Gagal dengan Daily Sweep dan Item Terhapus Permanen"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-577
  - TC-AC-LCS-578
coverage:
  web: automated
---

# Countdown Reset Job Recycle Bin: Job Per-Save Gagal dengan Daily Sweep dan Item Terhapus Permanen

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: Countdown Reset Job, daily sweep, dan jam server sebagai objek uji).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Pengamat: Default User Client PT Maju Jaya (TC 570 menyebut "Default User Client PT Maju Jaya"; TC 571 sampai 578 menyebut "User Client PT Maju Jaya"), `defaultUserClientMajuJaya_automated_{namaCompany}@qwertysystem.net` (Pre-setup 13, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), password dari `Spectra.env.AC_DUCLIENT_PASSWORD`; ganti akun ke pengamat dan kembali ke Total Control memakai langkah eksplisit.
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct) dengan file Recycle Bin `laporan-a.pdf` (dihapus 10 hari lalu) dan `laporan-b.pdf` (dihapus 25 hari lalu), dan `laporan-c.pdf` pada TC 578; diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite. Nilai awal Permanently Delete Recycle Bin `30` (default).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal hapus item Recycle Bin, menunda atau memaksa gagal Countdown Reset Job, memicu daily sweep, membaca status dan antrean job, serta memajukan jam server dan jam browser. Countdown dihitung dari tanggal hapus item; kolom Auto-Purge In dibaca pada Global Settings > File Manager > Recycle Bin.
- State global: konfigurasi tab Recycle Bin, item Recycle Bin PT Maju Jaya, antrean job, dan jam server dan jam browser diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-577: Job per-Save gagal, daily sweep memperbarui item dan tidak menerapkan floor 48 jam ulang

1. Atur lewat Fixture BE: Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu; Countdown Reset Job per-Save dipaksa gagal
2. Klik tab Recycle Bin
3. Ubah Permanently Delete Recycle Bin dari `30` menjadi `15` lalu klik `[Save]`
4. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
5. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
6. Verifikasi `laporan-b.pdf` masih menampilkan Auto-Purge In `5 days` (nilai sebelum recalculation)
7. Picu scheduled daily sweep lewat Fixture BE lalu muat ulang Recycle Bin
8. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `2 days` (floor 48 jam)
9. Atur jam server dan jam browser maju 1 hari, picu daily sweep lagi lewat Fixture BE, lalu muat ulang Recycle Bin
10. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `1 day` (floor tidak diterapkan ulang oleh sweep)
11. Pulihkan jam server dan jam browser lewat Fixture BE
12. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-578: Item yang sudah dihapus permanen tidak disentuh Countdown Reset Job

13. Atur lewat Fixture BE: Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu; `laporan-c.pdf` sudah dihapus permanen sebelum job berjalan
14. Klik tab Recycle Bin
15. Ubah Permanently Delete Recycle Bin dari `30` menjadi `15` lalu klik `[Save]`
16. Tunggu aksi `[Save]` dan Countdown Reset Job selesai (status job dibaca lewat Fixture BE)
17. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
18. Verifikasi hanya `laporan-a.pdf` dan `laporan-b.pdf` yang memiliki Auto-Purge In baru
19. Verifikasi `laporan-c.pdf` tidak muncul kembali pada Recycle Bin
20. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Tiap TC memulihkan item Recycle Bin lewat Fixture BE sebelum aksi (S-06, S-09).
- TC 578: `Verifikasi` Auto-Purge In baru pada `laporan-a.pdf` dan `laporan-b.pdf` (Expected b) ditulis sebelum `Verifikasi` `laporan-c.pdf` tidak muncul (Expected a) karena menjadi anchor positif asersi absence (bagian 8b butir 2).
- Pemajuan jam pada TC 577 dipulihkan pada langkah penghubung sebelum akun aktor membuka halaman lain (S-09).
- Temuan untuk QA:
  - Akun Default User Client PT Maju Jaya kini tertulis di Pre-setup 13 sebagai usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE; password dari `Spectra.env.AC_DUCLIENT_PASSWORD`.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
  - TC 578 Expected b tidak menyebut nilai Auto-Purge In baru; spec hanya mengasersi bahwa kedua item memiliki nilai baru.
  - TC 577 langkah 2 menyebut "amati laporan-b.pdf" tanpa menyebut akun pengamat selain User Client PT Maju Jaya pada precondition; spec memakai akun pengamat yang sama dengan TC lain.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 4-5, 7, 9, 11-14, 16-17, 20.
