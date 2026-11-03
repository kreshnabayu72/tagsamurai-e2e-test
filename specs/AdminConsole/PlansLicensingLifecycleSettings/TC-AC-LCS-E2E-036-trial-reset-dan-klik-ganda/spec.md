---
id: TC-AC-LCS-E2E-036-trial-reset-dan-klik-ganda
title: "Tab Trial Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-123
  - TC-AC-LCS-124
  - TC-AC-LCS-126
  - TC-AC-LCS-127
coverage:
  web: automated
---

# Tab Trial Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Trial Settings (Max Trial Duration `30`, Max Trial Asset Quota `50`, Max Trial Concurrent User Quota `10`, Require Approval for Trial Activation `OFF`, First Notification `7`, Second Notification `1`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE); Fixture BE untuk menyimpan nilai non-default tab sebagai precondition TC (disediakan tim FE/BE); `Spectra.intercept` di atas backend nyata untuk menahan respons permintaan Save atau Reset, melepasnya, dan menghitung permintaan yang terkirim (menahan respons hanya untuk mengamati state loading, bukan kegagalan yang dipaksakan).
- Seeding precondition (dipakai sebagai precondition TC, tidak diasersi): tab Trial Settings tersimpan dengan nilai non-default Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`, disimpan sebelum TC-AC-LCS-123 dan sebelum TC-AC-LCS-127.
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Trial Settings adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

### TC-AC-LCS-124: Reset to Default tab Trial Settings saat nilai tersimpan sudah default tetap sukses

1. Klik `[Reset to Default]` tanpa mengubah field apa pun
2. Verifikasi tidak ada dialog konfirmasi
3. Verifikasi toast sukses "Success, trial settings have been reset to default."
4. Verifikasi nilai tab tetap default `30`, `50`, `10`, `OFF`, `7`, `1`
5. Verifikasi `[Save]` disabled

### TC-AC-LCS-123: Reset to Default tab Trial Settings dari nilai tersimpan non-default

6. Simpan tab Trial Settings dengan nilai non-default Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3` lewat Fixture BE
7. Muat ulang halaman dengan F5 lalu klik tab Trial Settings
8. Ubah Max Trial Duration menjadi `1` tanpa menyimpan
9. Klik `[Reset to Default]`
10. Verifikasi tidak ada dialog konfirmasi apa pun
11. Verifikasi toast sukses "Success, trial settings have been reset to default."
12. Verifikasi tab refresh dengan nilai default `30`, `50`, `10`, `OFF`, `7`, `1`
13. Verifikasi `[Save]` disabled
14. Muat ulang halaman dengan F5 lalu klik tab Trial Settings
15. Verifikasi nilai default `30`, `50`, `10`, `OFF`, `7`, `1` bertahan (tersimpan)

### TC-AC-LCS-126: Klik ganda cepat pada [Save] tab Trial Settings hanya memproses satu permintaan

16. Ubah Max Trial Duration dari `30` menjadi `31`
17. Tahan respons permintaan Save lewat `Spectra.intercept`
18. Klik dua kali cepat pada `[Save]`
19. Verifikasi `[Save]` menampilkan loading setelah klik pertama
20. Verifikasi `[Save]` disabled setelah klik pertama
21. Verifikasi tepat satu permintaan Save terkirim ke server
22. Lepas tahanan respons permintaan Save
23. Verifikasi satu toast sukses "Success, trial settings have been saved."
24. Verifikasi Max Trial Duration bernilai `31`

### TC-AC-LCS-127: Klik ganda cepat pada [Reset to Default] tab Trial Settings hanya memproses satu permintaan

25. Simpan tab Trial Settings dengan nilai non-default Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3` lewat Fixture BE
26. Muat ulang halaman dengan F5 lalu klik tab Trial Settings
27. Tahan respons permintaan Reset lewat `Spectra.intercept`
28. Klik dua kali cepat pada `[Reset to Default]`
29. Verifikasi `[Reset to Default]` menampilkan loading setelah klik pertama
30. Verifikasi `[Reset to Default]` disabled setelah klik pertama
31. Verifikasi tepat satu permintaan Reset terkirim ke server
32. Lepas tahanan respons permintaan Reset
33. Verifikasi satu toast sukses "Success, trial settings have been reset to default."

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 124, 123, 126, 127 (Reset sebelum klik ganda; TC-AC-LCS-124 dengan nilai default berjalan sebelum TC-AC-LCS-123 karena TC-AC-LCS-123 membutuhkan nilai non-default yang disimpan lewat Fixture BE dan TC-AC-LCS-127 menyimpannya ulang).
- Langkah penghubung (S-03): langkah 6, 7, 25, 26 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Intercept menahan respons hanya untuk mengamati state loading dan jumlah permintaan; bukan fault injection. Intercept dilepas segera setelah pengamatan selesai (S-09).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-123 dan TC-AC-LCS-126 (entri Changelog `Edit`) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-LCS-126 dan TC-AC-LCS-127 mengasersi state loading tombol dan "tepat satu permintaan"; TC tidak mendefinisikan cara mengamati permintaan jaringan, sehingga spec menulisnya sebagai kemampuan intercept yang disediakan tim FE (S-13) dan menahan respons agar state loading teramati.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
