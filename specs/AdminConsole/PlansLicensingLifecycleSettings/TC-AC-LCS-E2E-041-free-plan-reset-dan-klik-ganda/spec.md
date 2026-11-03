---
id: TC-AC-LCS-E2E-041-free-plan-reset-dan-klik-ganda
title: "Tab Free Plan Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-138
  - TC-AC-LCS-139
  - TC-AC-LCS-141
  - TC-AC-LCS-142
coverage:
  web: automated
---

# Tab Free Plan Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Free Plan Settings (Free Plan Duration `365`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE); Fixture BE untuk menyimpan nilai non-default tab sebagai precondition TC (disediakan tim FE/BE); `Spectra.intercept` di atas backend nyata untuk menahan respons permintaan Save atau Reset, melepasnya, dan menghitung permintaan yang terkirim (menahan respons hanya untuk mengamati state loading, bukan kegagalan yang dipaksakan).
- Seeding precondition (dipakai sebagai precondition TC, tidak diasersi): tab Free Plan Settings tersimpan dengan nilai non-default Free Plan Duration `400`, disimpan sebelum TC-AC-LCS-138 dan sebelum TC-AC-LCS-142.
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Free Plan Settings adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab Free Plan Settings

### TC-AC-LCS-139: Reset to Default tab Free Plan Settings saat nilai tersimpan sudah default tetap sukses

2. Klik `[Reset to Default]` tanpa mengubah field apa pun
3. Verifikasi tidak ada dialog konfirmasi
4. Verifikasi toast sukses "Success, free plan settings have been reset to default."
5. Verifikasi nilai tab tetap default `365`
6. Verifikasi `[Save]` disabled

### TC-AC-LCS-138: Reset to Default tab Free Plan Settings dari nilai tersimpan non-default

7. Simpan tab Free Plan Settings dengan nilai non-default Free Plan Duration `400` lewat Fixture BE
8. Muat ulang halaman dengan F5 lalu klik tab Free Plan Settings
9. Ubah Free Plan Duration menjadi `1` tanpa menyimpan
10. Klik `[Reset to Default]`
11. Verifikasi tidak ada dialog konfirmasi apa pun
12. Verifikasi toast sukses "Success, free plan settings have been reset to default."
13. Verifikasi tab refresh dengan nilai default `365`
14. Verifikasi `[Save]` disabled
15. Muat ulang halaman dengan F5 lalu klik tab Free Plan Settings
16. Verifikasi nilai default `365` bertahan (tersimpan)

### TC-AC-LCS-141: Klik ganda cepat pada [Save] tab Free Plan Settings hanya memproses satu permintaan

17. Ubah Free Plan Duration dari `365` menjadi `366`
18. Tahan respons permintaan Save lewat `Spectra.intercept`
19. Klik dua kali cepat pada `[Save]`
20. Verifikasi `[Save]` menampilkan loading setelah klik pertama
21. Verifikasi `[Save]` disabled setelah klik pertama
22. Verifikasi tepat satu permintaan Save terkirim ke server
23. Lepas tahanan respons permintaan Save
24. Verifikasi satu toast sukses "Success, free plan settings have been saved."
25. Verifikasi Free Plan Duration bernilai `366`

### TC-AC-LCS-142: Klik ganda cepat pada [Reset to Default] tab Free Plan Settings hanya memproses satu permintaan

26. Simpan tab Free Plan Settings dengan nilai non-default Free Plan Duration `400` lewat Fixture BE
27. Muat ulang halaman dengan F5 lalu klik tab Free Plan Settings
28. Tahan respons permintaan Reset lewat `Spectra.intercept`
29. Klik dua kali cepat pada `[Reset to Default]`
30. Verifikasi `[Reset to Default]` menampilkan loading setelah klik pertama
31. Verifikasi `[Reset to Default]` disabled setelah klik pertama
32. Verifikasi tepat satu permintaan Reset terkirim ke server
33. Lepas tahanan respons permintaan Reset
34. Verifikasi satu toast sukses "Success, free plan settings have been reset to default."

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 139, 138, 141, 142 (Reset sebelum klik ganda; TC-AC-LCS-139 dengan nilai default berjalan sebelum TC-AC-LCS-138 karena TC-AC-LCS-138 membutuhkan nilai non-default yang disimpan lewat Fixture BE dan TC-AC-LCS-142 menyimpannya ulang).
- Langkah penghubung (S-03): langkah 1, 7, 8, 26, 27 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Intercept menahan respons hanya untuk mengamati state loading dan jumlah permintaan; bukan fault injection. Intercept dilepas segera setelah pengamatan selesai (S-09).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-138 dan TC-AC-LCS-141 (entri Changelog `Edit`) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-LCS-141 dan TC-AC-LCS-142 mengasersi state loading tombol dan "tepat satu permintaan"; TC tidak mendefinisikan cara mengamati permintaan jaringan, sehingga spec menulisnya sebagai kemampuan intercept yang disediakan tim FE (S-13) dan menahan respons agar state loading teramati.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
