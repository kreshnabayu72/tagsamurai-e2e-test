---
id: TC-AC-LCS-E2E-034-trial-dirty-state-save-seluruh-field
title: "Tab Trial Settings: Dirty State, Save Seluruh Field, dan Koreksi Nilai Salah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-119
  - TC-AC-LCS-120
  - TC-AC-LCS-128
coverage:
  web: automated
---

# Tab Trial Settings: Dirty State, Save Seluruh Field, dan Koreksi Nilai Salah

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

### TC-AC-LCS-119: Save mengikuti dirty state dan Reset to Default selalu enabled

1. Verifikasi `[Save]` disabled pada kondisi awal
2. Verifikasi `[Reset to Default]` enabled pada kondisi awal
3. Ubah Max Trial Duration dari `30` menjadi `31`
4. Verifikasi `[Save]` enabled
5. Verifikasi `[Reset to Default]` enabled
6. Kembalikan Max Trial Duration menjadi `30`
7. Verifikasi `[Save]` disabled kembali
8. Verifikasi `[Reset to Default]` tetap enabled

### TC-AC-LCS-128: memperbaiki nilai yang salah menghapus pesan error dan meng-enable Save

9. Isi Max Trial Duration dengan `0`
10. Klik area kosong di luar field (blur)
11. Verifikasi pesan error rentang tampil pada Max Trial Duration
12. Verifikasi `[Save]` disabled
13. Isi Max Trial Duration dengan `31`
14. Klik area kosong di luar field (blur)
15. Verifikasi pesan error hilang
16. Verifikasi `[Save]` enabled

### TC-AC-LCS-120: Save tab Trial Settings dengan seluruh field diubah ke nilai valid

17. Ubah Max Trial Duration menjadi `45`
18. Ubah Max Trial Asset Quota menjadi `100`
19. Ubah Max Trial Concurrent User Quota menjadi `20`
20. Aktifkan Switch Require Approval for Trial Activation (status `ON`)
21. Ubah First Notification menjadi `14`
22. Ubah Second Notification menjadi `3`
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, trial settings have been saved."
25. Verifikasi tab refresh: field memuat nilai tersimpan Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`
26. Verifikasi `[Save]` disabled
27. Muat ulang halaman dengan F5 lalu klik tab Trial Settings
28. Verifikasi setelah F5: Max Trial Duration bernilai `45`
29. Verifikasi setelah F5: Max Trial Asset Quota bernilai `100`
30. Verifikasi setelah F5: Max Trial Concurrent User Quota bernilai `20`
31. Verifikasi setelah F5: Require Approval for Trial Activation bernilai `ON`
32. Verifikasi setelah F5: First Notification bernilai `14`
33. Verifikasi setelah F5: Second Notification bernilai `3`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 119, 128, 120 (validasi yang diblokir dan perbaikannya sebelum Save sukses, S-10).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-120 (entri Changelog `Edit` per field) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-LCS-128 menyebut "pesan error rentang" tanpa teks pesan dan tanpa rentang nilai Max Trial Duration; spec mengasersi keberadaan pesan error tanpa mengutip teksnya (S-02).
  - TC-AC-LCS-128 berakhir dengan Max Trial Duration `31` belum disimpan; nilai itu diganti TC-AC-LCS-120 pada langkah berikutnya tanpa langkah pemulihan terpisah.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
