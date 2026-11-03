---
id: TC-AC-LCS-E2E-084-resilience-save-500-trial-dan-free-plan
title: "Resilience Save 500: Toast Error, Form Tetap, dan Data Tidak Berubah pada Tab Trial Settings dan Free Plan Settings"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-122
  - TC-AC-LCS-137
coverage:
  web: automated
---

# Resilience Save 500: Toast Error, Form Tetap, dan Data Tidak Berubah pada Tab Trial Settings dan Free Plan Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Save tab Trial Settings, Free Plan Settings gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Kemampuan teknis tambahan (disediakan tim FE): menangani dialog `beforeunload` bawaan browser (konfirmasi muat ulang) pada langkah F5 saat form dirty.
- Data uji: Trial Settings: Max Trial Duration `30` lalu `31`; Free Plan Settings: Free Plan Duration `365` lalu `366`; tidak ada nilai tersimpan yang berubah (Save selalu gagal).
- State global: tidak ada perubahan nilai tersimpan; intercept dipulihkan hook `beforeEach` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Pasang intercept: permintaan Save tab Trial Settings dan Free Plan Settings dipaksa gagal HTTP 500

### TC-AC-LCS-122: Save tab Trial Settings gagal 500: toast error, form tetap, data tidak berubah

2. Ubah Max Trial Duration dari `30` menjadi `31`
3. Klik `[Save]`
4. Verifikasi toast error "Error, failed to save trial settings."
5. Verifikasi Max Trial Duration tetap `31`
6. Verifikasi `[Save]` enabled
7. Verifikasi tab tidak refresh
8. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab Trial Settings
9. Verifikasi Max Trial Duration bernilai `30` (data tidak berubah)

### TC-AC-LCS-137: Save tab Free Plan Settings gagal 500: toast error, form tetap, data tidak berubah

10. Klik tab Free Plan Settings
11. Ubah Free Plan Duration dari `365` menjadi `366`
12. Klik `[Save]`
13. Verifikasi toast error "Error, failed to save free plan settings."
14. Verifikasi Free Plan Duration tetap `366`
15. Verifikasi `[Save]` enabled
16. Verifikasi tab tidak refresh
17. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab Free Plan Settings
18. Verifikasi Free Plan Duration bernilai `365` (data tidak berubah)

## Notes

- Kelas harness b (fault injection): spec ini hanya memuat TC kegagalan yang dipaksa; kegagalan dipicu intercept di atas backend nyata (Mode FE+BE) karena Expected mengasersi state backend (nilai tersimpan setelah F5).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (memasang intercept), dan langkah 10, 8, 17 (berpindah tab dan memuat ulang halaman; form dirty ditutup lewat konfirmasi `beforeunload` karena kemampuannya tertulis di Prerequisites, S-08).
- Sesudah muat ulang, form kembali ke nilai tersimpan sehingga spec tidak berakhir dirty.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
