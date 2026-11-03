---
id: TC-AC-LCS-E2E-089-unsaved-changes-dialog-sidebar-dan-state-bersih
title: "Dialog Unsaved Changes: Menu Sidebar, Tab Lain Dirty, Tanpa Perubahan, Nilai Dikembalikan, dan Setelah Save"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-336
  - TC-AC-LCS-337
  - TC-AC-LCS-338
  - TC-AC-LCS-339
  - TC-AC-LCS-340
coverage:
  web: automated
---

# Dialog Unsaved Changes: Menu Sidebar, Tab Lain Dirty, Tanpa Perubahan, Nilai Dikembalikan, dan Setelah Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: Max Trial Duration `30` lalu `45`; menu sidebar Plans & Features sebagai tujuan keluar.
- State global yang diubah: Max Trial Duration tersimpan `45` pada TC-AC-LCS-340; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-336: Dialog Unsaved Changes saat klik menu sidebar lain dengan tab dirty: Cancel mempertahankan, Leave meninggalkan tanpa simpan

1. Ubah Max Trial Duration dari `30` menjadi `45` (belum disimpan)
2. Klik menu Plans & Features di sidebar
3. Verifikasi dialog "Unsaved Changes" (severity warning) tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` serta `[Leave]` (severity warning)
4. Klik `[Cancel]`
5. Verifikasi dialog tertutup
6. Verifikasi halaman Lifecycle Settings tetap terbuka
7. Verifikasi Max Trial Duration tetap `45`
8. Klik menu Plans & Features di sidebar
9. Klik `[Leave]`
10. Verifikasi navigasi dilanjutkan ke Plans & Features tanpa menyimpan
11. Klik menu Plans & Licensing > Lifecycle Settings di sidebar, lalu buka tab Trial Settings
12. Verifikasi Max Trial Duration bernilai `30` (perubahan tidak tersimpan)

### TC-AC-LCS-337: Dialog Unsaved Changes muncul saat tab lain (bukan tab aktif) masih dirty

13. Ubah Max Trial Duration dari `30` menjadi `45` (belum disimpan)
14. Klik tab Free Plan Settings (Trial Settings dirty, Free Plan Settings clean)
15. Klik menu Plans & Features di sidebar
16. Verifikasi dialog "Unsaved Changes" dengan body "You have unsaved changes. Are you sure you want to leave?" tampil karena Trial Settings masih dirty
17. Klik `[Leave]`
18. Klik menu Plans & Licensing > Lifecycle Settings di sidebar, lalu buka tab Trial Settings

### TC-AC-LCS-338: Tanpa perubahan: keluar dari Lifecycle Settings tidak memunculkan dialog Unsaved Changes

19. Klik menu Plans & Features di sidebar
20. Verifikasi halaman Plans & Features tampil
21. Verifikasi tidak ada dialog Unsaved Changes
22. Klik menu Plans & Licensing > Lifecycle Settings di sidebar, lalu buka tab Trial Settings

### TC-AC-LCS-339: Perubahan yang dikembalikan ke nilai tersimpan dianggap clean dan tidak memunculkan dialog

23. Ubah Max Trial Duration dari `30` menjadi `45`
24. Kembalikan Max Trial Duration menjadi `30`
25. Klik menu Plans & Features di sidebar
26. Verifikasi halaman Plans & Features tampil
27. Verifikasi tidak ada dialog Unsaved Changes
28. Klik menu Plans & Licensing > Lifecycle Settings di sidebar, lalu buka tab Trial Settings

### TC-AC-LCS-340: Setelah Save berhasil guard dilepas dan keluar halaman tidak memunculkan dialog

29. Ubah Max Trial Duration dari `30` menjadi `45`
30. Klik `[Save]`
31. Tunggu aksi Save selesai (toast sukses tampil dan `[Save]` kembali disabled)
32. Klik menu Plans & Features di sidebar
33. Verifikasi halaman Plans & Features tampil
34. Verifikasi tidak ada dialog Unsaved Changes

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 11, 18, 22, 28 (membuka kembali halaman Lifecycle Settings dalam keadaan termuat baru), langkah 14 (memindahkan tab aktif agar tab yang dirty bukan tab aktif), langkah 17 (meninggalkan halaman dengan `[Leave]` agar spec tidak berakhir dirty, S-08 dan S-09), dan langkah 31 (menunggu Save selesai).
- Asersi tidak ada dialog Unsaved Changes memakai halaman Plans & Features yang tampil sebagai anchor positif (bagian 8b butir 2); TC hanya menulis "navigasi langsung ke Plans & Features tanpa dialog".
- Verifikasi dialog Unsaved Changes pada TC-AC-LCS-336 dan TC-AC-LCS-337 ditulis sebagai satu elemen dialog konfirmasi (judul, isi, dan tombol disebut utuh).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - TC-AC-LCS-340 menyebut "tunggu toast sukses" tanpa teks toast; spec tidak mengasersi toast dan hanya menunggu Save selesai.
