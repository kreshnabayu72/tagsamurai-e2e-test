---
id: TC-AC-LCS-E2E-091-state-in-flight-save-dan-reset
title: "State In-Flight Save dan Reset: Field, Switch, Save, dan Reset Disabled Selama Permintaan Berjalan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-347
  - TC-AC-LCS-348
coverage:
  web: automated
---

# State In-Flight Save dan Reset: Field, Switch, Save, dan Reset Disabled Selama Permintaan Berjalan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE/BE): Fixture BE untuk mengatur nilai tersimpan non-default pada tab yang diuji sebagai precondition TC.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` untuk menahan respons Save tab Trial Settings dan Reset tab Client Lifecycle di atas backend nyata dan melepasnya, serta membaca daftar permintaan jaringan; intercept dipulihkan hook `beforeEach` suite.
- Data uji: Max Trial Duration `30` lalu `45`; nilai non-default tersimpan Client Lifecycle: Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000` (TC-AC-LCS-348 hanya menulis "nilai non-default").
- State global yang diubah: Max Trial Duration tersimpan `45` pada TC-AC-LCS-347, lalu nilai non-default Client Lifecycle diatur untuk TC-AC-LCS-348 dan dikembalikan ke default oleh Reset; pemulihan cadangan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-347: Selama Save tab Trial Settings in-flight, field, Switch, Save, dan Reset to Default Disabled

1. Tahan respons Save tab Trial Settings (intercept)
2. Ubah Max Trial Duration dari `30` menjadi `45`
3. Klik `[Save]`
4. Verifikasi `[Save]` menampilkan loading (spinner)
5. Verifikasi `[Save]` disabled
6. Verifikasi `[Reset to Default]` disabled
7. Verifikasi seluruh Number Input dan Switch Require Approval for Trial Activation berstatus Disabled
8. Lepas tahanan respons Save dan tunggu respons diterima
9. Verifikasi toast sukses "Success, trial settings have been saved."
10. Verifikasi field kembali enabled
11. Verifikasi Max Trial Duration bernilai `45` (nilai tersimpan)

### TC-AC-LCS-348: Selama Reset to Default tab Client Lifecycle in-flight, field, Save, dan Reset Disabled

12. Atur nilai tersimpan tab Client Lifecycle ke nilai non-default lewat Fixture BE: Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000`
13. Muat ulang halaman dengan F5, lalu buka tab Client Lifecycle
14. Tahan respons Reset tab Client Lifecycle (intercept)
15. Klik `[Reset to Default]`
16. Verifikasi `[Reset to Default]` menampilkan loading
17. Verifikasi `[Reset to Default]` disabled
18. Verifikasi `[Save]` disabled
19. Verifikasi seluruh Number Input berstatus Disabled
20. Lepas tahanan respons Reset dan tunggu respons diterima
21. Verifikasi toast sukses "Success, client lifecycle settings have been reset to default."
22. Verifikasi field kembali enabled
23. Verifikasi seluruh field Client Lifecycle bernilai default (`45`, `30`, `7`, `1`, `30`, `30`, `10`, `2`, `730`)

## Notes

- Penahan respons (langkah 1 dan 14) hanya untuk mengamati state in-flight (loading dan Disabled), bukan fault injection (bagian 3 prinsip 13 butir b); karena itu spec ini fungsional.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 14 (menahan respons), langkah 8, 20 (melepas tahanan respons), serta langkah 12 dan 13 (mengatur nilai non-default sebagai precondition TC-AC-LCS-348 dan memuat ulang halaman).
- Asersi state sementara (loading dan Disabled) ditulis sebelum respons dilepas; asersi toast dan field enabled sesudahnya (bagian 8b butir 5 dan 11).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - TC-AC-LCS-348 menulis "nilai non-default" tanpa nilai; spec memilih nilai non-default yang sama dengan precondition TC-AC-LCS-218.
  - Expected TC-AC-LCS-348 butir d menyebut "nilai default" tanpa daftar; spec mengasersi kesembilan nilai default Client Lifecycle dari Pre-setup 7.
