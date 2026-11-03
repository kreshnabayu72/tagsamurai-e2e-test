---
id: TC-AC-LCS-E2E-189-resilience-save-500-license-timing-dan-client-lifecycle
title: "Resilience Save 500: Toast Error, Form Tetap, dan Data Tidak Berubah pada Tab License Timing dan Client Lifecycle"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-162
  - TC-AC-LCS-215
coverage:
  web: automated
---

# Resilience Save 500: Toast Error, Form Tetap, dan Data Tidak Berubah pada Tab License Timing dan Client Lifecycle

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Save tab License Timing, Client Lifecycle gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Kemampuan teknis tambahan (disediakan tim FE): menangani dialog `beforeunload` bawaan browser (konfirmasi muat ulang) pada langkah F5 saat form dirty.
- Data uji: License Timing: Managed Transition Time `24` lalu `25`; Client Lifecycle: Notify Plan Owner Before Event `45` lalu `46`; tidak ada nilai tersimpan yang berubah (Save selalu gagal).
- State global: tidak ada perubahan nilai tersimpan; intercept dipulihkan hook `beforeEach` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Pasang intercept: permintaan Save tab License Timing dan Client Lifecycle dipaksa gagal HTTP 500

### TC-AC-LCS-162: Save tab License Timing gagal 500: toast error, form tetap, data tidak berubah

2. Klik tab License Timing
3. Ubah Managed Transition Time dari `24` menjadi `25`
4. Klik `[Save]`
5. Verifikasi toast error "Error, failed to save license timing settings."
6. Verifikasi Managed Transition Time tetap `25`
7. Verifikasi `[Save]` enabled
8. Verifikasi tab tidak refresh
9. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab License Timing
10. Verifikasi Managed Transition Time bernilai `24` (data tidak berubah)

### TC-AC-LCS-215: Save tab Client Lifecycle gagal 500: toast error, form tetap, data tidak berubah

11. Klik tab Client Lifecycle
12. Ubah Notify Plan Owner Before Event dari `45` menjadi `46`
13. Klik `[Save]`
14. Verifikasi toast error "Error, failed to save client lifecycle settings."
15. Verifikasi Notify Plan Owner Before Event tetap `46`
16. Verifikasi `[Save]` enabled
17. Verifikasi tab tidak refresh
18. Muat ulang halaman dengan F5 (konfirmasi dialog `beforeunload` bawaan browser), lalu buka kembali tab Client Lifecycle
19. Verifikasi Notify Plan Owner Before Event bernilai `45` (data tidak berubah)

## Notes

- Kelas harness b (fault injection): spec ini hanya memuat TC kegagalan yang dipaksa; kegagalan dipicu intercept di atas backend nyata (Mode FE+BE) karena Expected mengasersi state backend (nilai tersimpan setelah F5).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (memasang intercept), dan langkah 2, 11, 9, 18 (berpindah tab dan memuat ulang halaman; form dirty ditutup lewat konfirmasi `beforeunload` karena kemampuannya tertulis di Prerequisites, S-08).
- Sesudah muat ulang, form kembali ke nilai tersimpan sehingga spec tidak berakhir dirty.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
