---
id: TC-AC-LCS-E2E-035-trial-save-minimum-dan-switch-require-approval
title: "Tab Trial Settings: Save Nilai Minimum dan Switch Require Approval for Trial Activation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-121
  - TC-AC-LCS-292
  - TC-AC-LCS-293
  - TC-AC-LCS-294
coverage:
  web: automated
---

# Tab Trial Settings: Save Nilai Minimum dan Switch Require Approval for Trial Activation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Trial Settings (Max Trial Duration `30`, Max Trial Asset Quota `50`, Max Trial Concurrent User Quota `10`, Require Approval for Trial Activation `OFF`, First Notification `7`, Second Notification `1`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Trial Settings adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

### TC-AC-LCS-292: Switch Require Approval for Trial Activation: toggle ON memicu dirty state tanpa dialog konfirmasi

1. Klik Switch Require Approval for Trial Activation
2. Verifikasi Switch berstatus `ON`
3. Verifikasi tidak ada dialog konfirmasi
4. Verifikasi `[Save]` enabled
5. Klik Switch Require Approval for Trial Activation lagi
6. Verifikasi Switch kembali `OFF`
7. Verifikasi tidak ada dialog konfirmasi
8. Verifikasi `[Save]` disabled

### TC-AC-LCS-293: Save Switch Require Approval for Trial Activation menyimpan status ON dan menampilkannya setelah refresh

9. Aktifkan Switch Require Approval for Trial Activation (`ON`)
10. Klik `[Save]`
11. Verifikasi toast sukses "Success, trial settings have been saved."
12. Muat ulang halaman dengan F5 lalu klik tab Trial Settings
13. Verifikasi Switch Require Approval for Trial Activation berstatus `ON`
14. Verifikasi `[Save]` disabled

### TC-AC-LCS-294: Save Switch Require Approval for Trial Activation kembali ke OFF menyimpan status OFF

15. Nonaktifkan Switch Require Approval for Trial Activation (`OFF`)
16. Klik `[Save]`
17. Verifikasi toast sukses "Success, trial settings have been saved."
18. Muat ulang halaman dengan F5
19. Verifikasi Switch Require Approval for Trial Activation berstatus `OFF`

### TC-AC-LCS-121: Save tab Trial Settings dengan nilai minimum yang valid

20. Ubah Max Trial Duration menjadi `1`
21. Ubah Max Trial Asset Quota menjadi `1`
22. Ubah Max Trial Concurrent User Quota menjadi `1`
23. Ubah First Notification menjadi `2`
24. Ubah Second Notification menjadi `1`
25. Verifikasi tidak ada pesan error pada seluruh field yang diisi
26. Klik `[Save]`
27. Verifikasi toast sukses "Success, trial settings have been saved."
28. Verifikasi tab refresh: field memuat Max Trial Duration `1`, Max Trial Asset Quota `1`, Max Trial Concurrent User Quota `1`, First Notification `2`, Second Notification `1`
29. Verifikasi `[Save]` disabled

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 292, 293, 294, 121 (screening Switch tanpa Save di awal; Save ON lalu OFF berurutan; Save nilai minimum di akhir).
- Precondition TC-AC-LCS-294 (Require Approval for Trial Activation tersimpan `On`) dipenuhi oleh state yang disimpan TC-AC-LCS-293 di spec yang sama; TC-AC-LCS-121 berjalan sesudah Switch kembali `OFF` (nilai default), sehingga precondition defaultnya terpenuhi.
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-293 dan TC-AC-LCS-294 (Require Approval for Trial Activation tersimpan `On` atau `Off`) setara dengan `Verifikasi` Switch sesudah F5; tidak ada asersi tambahan.
  - TC-AC-LCS-294 menyebut "Muat ulang halaman dengan F5" tanpa langkah membuka kembali tab; spec mengikuti TC dan tidak menambah klik tab.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
