---
id: TC-AC-LCS-E2E-163-recycle-bin-countdown-reset-job-durasi
title: "Countdown Reset Job Recycle Bin: Durasi Diperpendek, Diperpanjang, dan Reset to Default dari Nilai 60"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-571
  - TC-AC-LCS-572
  - TC-AC-LCS-573
coverage:
  web: automated
---

# Countdown Reset Job Recycle Bin: Durasi Diperpendek, Diperpanjang, dan Reset to Default dari Nilai 60

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: Countdown Reset Job dan jam server sebagai objek uji).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Pengamat: Default User Client PT Maju Jaya (TC 570 menyebut "Default User Client PT Maju Jaya"; TC 571 sampai 578 menyebut "User Client PT Maju Jaya"), `defaultUserClientMajuJaya_automated_{namaCompany}@qwertysystem.net` (Pre-setup 13, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), password dari `Spectra.env.AC_DUCLIENT_PASSWORD`; ganti akun ke pengamat dan kembali ke Total Control memakai langkah eksplisit.
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct) dengan file Recycle Bin `laporan-a.pdf` (dihapus 10 hari lalu) dan `laporan-b.pdf` (dihapus 25 hari lalu), dan `laporan-c.pdf` pada TC 578; diatur per TC lewat Fixture BE dan dipulihkan di hook `after` suite. Nilai awal Permanently Delete Recycle Bin `30` (default).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal hapus item Recycle Bin, menunda atau memaksa gagal Countdown Reset Job, memicu daily sweep, membaca status dan antrean job, serta memajukan jam server dan jam browser. Countdown dihitung dari tanggal hapus item; kolom Auto-Purge In dibaca pada Global Settings > File Manager > Recycle Bin.
- State global: konfigurasi tab Recycle Bin, item Recycle Bin PT Maju Jaya, antrean job, dan jam server dan jam browser diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-571: Durasi diperpendek, item dihitung dari tanggal hapus dan item yang terlewat mendapat minimal 48 jam

1. Atur lewat Fixture BE: Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu
2. Klik tab Recycle Bin
3. Ubah Permanently Delete Recycle Bin dari `30` menjadi `15` lalu klik `[Save]`
4. Tunggu aksi `[Save]` dan Countdown Reset Job selesai (status job dibaca lewat Fixture BE)
5. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
6. Verifikasi `laporan-a.pdf` menampilkan Auto-Purge In `5 days` (15 hari dikurangi 10 hari)
7. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `2 days` (batas minimal 48 jam dari saat job berjalan, bukan batas yang sudah terlewat)
8. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-572: Durasi diperpanjang, batas purge dihitung ulang dari tanggal hapus

9. Atur lewat Fixture BE: Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu
10. Klik tab Recycle Bin
11. Ubah Permanently Delete Recycle Bin dari `30` menjadi `60` lalu klik `[Save]`
12. Tunggu aksi `[Save]` dan Countdown Reset Job selesai (status job dibaca lewat Fixture BE)
13. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
14. Verifikasi `laporan-a.pdf` menampilkan Auto-Purge In `50 days`
15. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `35 days`
16. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-573: Reset to Default dari nilai 60 menghitung ulang batas purge ke 30

17. Atur lewat Fixture BE: Permanently Delete Recycle Bin tersimpan `60` dan batas purge item sudah dihitung dengan nilai tersebut; Client PT Maju Jaya memiliki dua file di Recycle Bin: `laporan-a.pdf` dihapus 10 hari lalu dan `laporan-b.pdf` dihapus 25 hari lalu
18. Klik tab Recycle Bin
19. Klik `[Reset to Default]` sehingga Permanently Delete Recycle Bin menjadi `30`
20. Tunggu aksi `[Reset to Default]` dan Countdown Reset Job selesai (status job dibaca lewat Fixture BE)
21. Ganti akun ke Default User Client PT Maju Jaya lalu buka Global Settings > File Manager > Recycle Bin
22. Verifikasi `laporan-a.pdf` menampilkan Auto-Purge In `20 days`
23. Verifikasi `laporan-b.pdf` menampilkan Auto-Purge In `5 days`
24. Ganti akun ke Total Control lalu buka Plans & Licensing > Lifecycle Settings

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Tiap TC memulihkan item Recycle Bin lewat Fixture BE sebelum aksi sehingga hasil TC sebelumnya tidak dipakai (S-06, S-09).
- Temuan untuk QA:
  - Akun Default User Client PT Maju Jaya kini tertulis di Pre-setup 13 sebagai usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE; password dari `Spectra.env.AC_DUCLIENT_PASSWORD`.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
  - TC 573 precondition menyebut batas purge sudah dihitung dengan nilai `60`; spec mengaturnya lewat Fixture BE sebagai precondition TC tanpa diasersi.
  - TC 571 sampai 573 tidak menyebut toast hasil Save atau Reset; spec tidak mengasersinya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 4-5, 8-10, 12-13, 16-18, 20-21, 24.
