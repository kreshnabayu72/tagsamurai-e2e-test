---
id: TC-AC-LCS-E2E-046-license-timing-reset-dan-klik-ganda
title: "Tab License Timing: Reset to Default dan Klik Ganda Cepat pada Save serta Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-163
  - TC-AC-LCS-164
  - TC-AC-LCS-166
  - TC-AC-LCS-167
coverage:
  web: automated
---

# Tab License Timing: Reset to Default dan Klik Ganda Cepat pada Save serta Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: License Timing (Managed Transition Time `24`, Managed Action Retry Delay `2`, Addon Reactivation Delay `2`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE); Fixture BE untuk menyimpan nilai non-default tab sebagai precondition TC (disediakan tim FE/BE); `Spectra.intercept` di atas backend nyata untuk menahan respons permintaan Save atau Reset, melepasnya, dan menghitung permintaan yang terkirim (menahan respons hanya untuk mengamati state loading, bukan kegagalan yang dipaksakan).
- Seeding precondition (dipakai sebagai precondition TC, tidak diasersi): tab License Timing tersimpan dengan nilai non-default Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7`, disimpan sebelum TC-AC-LCS-163 dan sebelum TC-AC-LCS-167.
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab License Timing adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab License Timing

### TC-AC-LCS-164: Reset to Default tab License Timing saat nilai tersimpan sudah default tetap sukses

2. Klik `[Reset to Default]` tanpa mengubah field apa pun
3. Verifikasi tidak ada dialog konfirmasi
4. Verifikasi toast sukses "Success, license timing settings have been reset to default."
5. Verifikasi nilai tab tetap default `24`, `2`, `2`
6. Verifikasi `[Save]` disabled

### TC-AC-LCS-163: Reset to Default tab License Timing dari nilai tersimpan non-default

7. Simpan tab License Timing dengan nilai non-default Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7` lewat Fixture BE
8. Muat ulang halaman dengan F5 lalu klik tab License Timing
9. Ubah Managed Transition Time menjadi `1` tanpa menyimpan
10. Klik `[Reset to Default]`
11. Verifikasi tidak ada dialog konfirmasi apa pun
12. Verifikasi toast sukses "Success, license timing settings have been reset to default."
13. Verifikasi tab refresh dengan nilai default `24`, `2`, `2`
14. Verifikasi `[Save]` disabled
15. Muat ulang halaman dengan F5 lalu klik tab License Timing
16. Verifikasi nilai default `24`, `2`, `2` bertahan (tersimpan)

### TC-AC-LCS-166: Klik ganda cepat pada [Save] tab License Timing hanya memproses satu permintaan

17. Ubah Managed Transition Time dari `24` menjadi `25`
18. Tahan respons permintaan Save lewat `Spectra.intercept`
19. Klik dua kali cepat pada `[Save]`
20. Verifikasi `[Save]` menampilkan loading setelah klik pertama
21. Verifikasi `[Save]` disabled setelah klik pertama
22. Verifikasi tepat satu permintaan Save terkirim ke server
23. Lepas tahanan respons permintaan Save
24. Verifikasi satu toast sukses "Success, license timing settings have been saved."
25. Verifikasi Managed Transition Time bernilai `25`

### TC-AC-LCS-167: Klik ganda cepat pada [Reset to Default] tab License Timing hanya memproses satu permintaan

26. Simpan tab License Timing dengan nilai non-default Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7` lewat Fixture BE
27. Muat ulang halaman dengan F5 lalu klik tab License Timing
28. Tahan respons permintaan Reset lewat `Spectra.intercept`
29. Klik dua kali cepat pada `[Reset to Default]`
30. Verifikasi `[Reset to Default]` menampilkan loading setelah klik pertama
31. Verifikasi `[Reset to Default]` disabled setelah klik pertama
32. Verifikasi tepat satu permintaan Reset terkirim ke server
33. Lepas tahanan respons permintaan Reset
34. Verifikasi satu toast sukses "Success, license timing settings have been reset to default."

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 164, 163, 166, 167 (Reset sebelum klik ganda; TC-AC-LCS-164 dengan nilai default berjalan sebelum TC-AC-LCS-163 karena TC-AC-LCS-163 membutuhkan nilai non-default yang disimpan lewat Fixture BE dan TC-AC-LCS-167 menyimpannya ulang).
- Langkah penghubung (S-03): langkah 1, 7, 8, 26, 27 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Intercept menahan respons hanya untuk mengamati state loading dan jumlah permintaan; bukan fault injection. Intercept dilepas segera setelah pengamatan selesai (S-09).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-163 dan TC-AC-LCS-166 (entri Changelog `Edit`) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-LCS-166 dan TC-AC-LCS-167 mengasersi state loading tombol dan "tepat satu permintaan"; TC tidak mendefinisikan cara mengamati permintaan jaringan, sehingga spec menulisnya sebagai kemampuan intercept yang disediakan tim FE (S-13) dan menahan respons agar state loading teramati.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
