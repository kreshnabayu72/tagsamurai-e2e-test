---
id: TC-AC-LCS-E2E-088-resilience-save-gagal-dan-timeout
title: "Resilience Save: Respons Gagal Mengembalikan Field Enabled, dan Timeout pada Save serta Reset Trial Settings"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-349
  - TC-AC-LCS-353
  - TC-AC-LCS-354
coverage:
  web: automated
---

# Resilience Save: Respons Gagal Mengembalikan Field Enabled, dan Timeout pada Save serta Reset Trial Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Save tab Trial Settings, serta memaksa timeout tanpa respons pada Save dan Reset tab Trial Settings gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Kemampuan teknis tambahan (disediakan tim FE/BE): Fixture BE untuk mengatur nilai tersimpan non-default pada tab yang diuji sebagai precondition TC.
- Data uji: Max Trial Duration `45`, First Notification `14` (TC-AC-LCS-349); Max Trial Duration `30` lalu `45` (TC-AC-LCS-353); nilai non-default tersimpan Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3` (TC-AC-LCS-354).
- State global yang diubah: Max Trial Duration tersimpan `45` pada TC-AC-LCS-353, lalu nilai non-default tab Trial Settings diatur ulang untuk TC-AC-LCS-354 (Reset gagal, nilai tidak berubah, lalu Reset sukses mengembalikan default); pemulihan cadangan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE); intercept dipulihkan hook `beforeEach` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-349: Respons Save gagal mengembalikan field ke Enabled dengan nilai yang sudah diisi tetap utuh

1. Pasang intercept: permintaan Save tab Trial Settings dipaksa gagal HTTP 500
2. Ubah Max Trial Duration menjadi `45`
3. Ubah First Notification menjadi `14`
4. Klik `[Save]`
5. Verifikasi toast error "Error, failed to save trial settings."
6. Verifikasi seluruh field kembali enabled
7. Verifikasi Max Trial Duration `45` tetap terisi
8. Verifikasi First Notification `14` tetap terisi
9. Verifikasi `[Save]` enabled
10. Kembalikan Max Trial Duration menjadi `30` dan First Notification menjadi `7`

### TC-AC-LCS-353: Save tab Trial Settings tanpa respons (timeout): toast koneksi tanpa tombol aksi dan retry manual lewat Save

11. Ganti intercept: permintaan Save tab Trial Settings dipaksa timeout tanpa respons (menggantikan intercept HTTP 500 sebelumnya)
12. Ubah Max Trial Duration dari `30` menjadi `45`
13. Klik `[Save]`
14. Verifikasi toast error "Connection problem. Please try again." tanpa tombol aksi
15. Verifikasi `[Save]` kembali enabled untuk retry manual
16. Verifikasi tidak ada toast sukses dan tidak ada toast "Error, failed to save trial settings." (hasil tidak diasumsikan)
17. Pulihkan jaringan (lepas intercept timeout)
18. Klik `[Save]` lagi
19. Verifikasi toast sukses "Success, trial settings have been saved."

### TC-AC-LCS-354: Reset to Default tab Trial Settings tanpa respons (timeout): toast koneksi tanpa tombol aksi dan retry manual lewat Reset to Default

20. Atur nilai tersimpan tab Trial Settings ke nilai non-default lewat Fixture BE: Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`
21. Muat ulang halaman dengan F5, lalu buka tab Trial Settings
22. Pasang intercept: permintaan Reset tab Trial Settings dipaksa timeout tanpa respons
23. Klik `[Reset to Default]`
24. Verifikasi toast error "Connection problem. Please try again." tanpa tombol aksi
25. Verifikasi `[Reset to Default]` kembali enabled untuk retry manual
26. Verifikasi tidak ada toast sukses dan tidak ada toast "Error, failed to reset trial settings." (hasil tidak diasumsikan)
27. Pulihkan jaringan (lepas intercept timeout)
28. Klik `[Reset to Default]` lagi
29. Verifikasi toast sukses "Success, trial settings have been reset to default."

## Notes

- Kelas harness b (fault injection): spec ini hanya memuat TC kegagalan yang dipaksa; kegagalan dipicu intercept di atas backend nyata (Mode FE+BE) karena Expected mengasersi state backend (nilai tersimpan setelah F5).
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 11, 22 (memasang intercept), langkah 10 (mengembalikan field ke nilai tersimpan agar TC berikutnya mulai dari form bersih, S-09), langkah 17, 27 (memulihkan jaringan), serta langkah 20 dan 21 (mengatur nilai tersimpan non-default sebagai precondition TC-AC-LCS-354 dan memuat ulang halaman).
- Asersi absence toast sukses ditulis sesudah toast error "Connection problem. Please try again." tampil, yang menjadi anchor positif pada surface yang sama (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - TC-AC-LCS-349 (respons Save gagal 500 pada tab Trial Settings) tumpang tindih dengan TC-AC-LCS-122 (Save tab Trial Settings gagal 500); keduanya tetap ditulis sesuai sumber masing-masing.
  - TC-AC-LCS-353 dan TC-AC-LCS-354 menyebut "pulihkan jaringan" tanpa mekanisme; spec menulisnya sebagai melepas intercept timeout (kemampuan disediakan tim FE).
