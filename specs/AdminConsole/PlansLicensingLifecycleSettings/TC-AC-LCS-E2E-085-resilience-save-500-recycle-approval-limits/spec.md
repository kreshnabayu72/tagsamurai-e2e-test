---
id: TC-AC-LCS-E2E-085-resilience-save-500-recycle-approval-limits
title: "Resilience Save 500 pada Tab Recycle Bin, Approval Settings, dan System Limits"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-230
  - TC-AC-LCS-245
  - TC-AC-LCS-285
coverage:
  web: automated
---

# Resilience Save 500 pada Tab Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Save tab Recycle Bin, Approval Settings, System Limits gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Kemampuan teknis tambahan (disediakan tim FE): menangani dialog `beforeunload` bawaan browser (konfirmasi muat ulang) pada langkah F5 saat form dirty.
- Data uji: Recycle Bin: Permanently Delete Recycle Bin `30` lalu `31`; Approval Settings: Approval Timeout `3` lalu `4`; System Limits: Bulk Transaction Row Limit `1000` lalu `1001`; tidak ada nilai tersimpan yang berubah (Save selalu gagal).
- State global: tidak ada perubahan nilai tersimpan; intercept dipulihkan hook `beforeEach` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Pasang intercept: permintaan Save tab Recycle Bin dan Approval Settings dan System Limits dipaksa gagal HTTP 500

### TC-AC-LCS-230: Save tab Recycle Bin gagal 500: toast error, form tetap, data tidak berubah

2. Klik tab Recycle Bin
3. Ubah Permanently Delete Recycle Bin dari `30` menjadi `31`
4. Klik `[Save]`
5. Verifikasi toast error "Error, failed to save recycle bin settings."
6. Verifikasi Permanently Delete Recycle Bin tetap `31`
7. Verifikasi `[Save]` enabled
8. Verifikasi tab tidak refresh
9. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab Recycle Bin
10. Verifikasi Permanently Delete Recycle Bin bernilai `30` (data tidak berubah)

### TC-AC-LCS-245: Save tab Approval Settings gagal 500: toast error, form tetap, data tidak berubah

11. Klik tab Approval Settings
12. Ubah Approval Timeout dari `3` menjadi `4`
13. Klik `[Save]`
14. Verifikasi toast error "Error, failed to save approval settings."
15. Verifikasi Approval Timeout tetap `4`
16. Verifikasi `[Save]` enabled
17. Verifikasi tab tidak refresh
18. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab Approval Settings
19. Verifikasi Approval Timeout bernilai `3` (data tidak berubah)

### TC-AC-LCS-285: Save tab System Limits gagal 500: toast error, form tetap, data tidak berubah

20. Klik tab System Limits
21. Ubah Bulk Transaction Row Limit dari `1000` menjadi `1001`
22. Klik `[Save]`
23. Verifikasi toast error "Error, failed to save system limits settings."
24. Verifikasi Bulk Transaction Row Limit tetap `1001`
25. Verifikasi `[Save]` enabled
26. Verifikasi tab tidak refresh
27. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab System Limits
28. Verifikasi Bulk Transaction Row Limit bernilai `1000` (data tidak berubah)

## Notes

- Kelas harness b (fault injection): spec ini hanya memuat TC kegagalan yang dipaksa; kegagalan dipicu intercept di atas backend nyata (Mode FE+BE) karena Expected mengasersi state backend (nilai tersimpan setelah F5).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (memasang intercept), dan langkah 2, 11, 20, 9, 18, 27 (berpindah tab dan memuat ulang halaman; form dirty ditutup lewat konfirmasi `beforeunload` karena kemampuannya tertulis di Prerequisites, S-08).
- Sesudah muat ulang, form kembali ke nilai tersimpan sehingga spec tidak berakhir dirty.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
