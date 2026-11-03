---
id: TC-AC-LCS-E2E-074-approval-settings-reset-dan-klik-ganda
title: "Tab Approval Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-246
  - TC-AC-LCS-247
  - TC-AC-LCS-249
  - TC-AC-LCS-250
coverage:
  web: automated
---

# Tab Approval Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Data Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE/BE): Fixture BE untuk mengatur nilai tersimpan non-default pada tab yang diuji sebagai precondition TC.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` untuk menahan respons Save dan Reset tab Approval Settings di atas backend nyata dan melepasnya, serta membaca daftar permintaan jaringan; intercept dipulihkan hook `beforeEach` suite.
- Data uji: nilai default tab Approval Settings `3`; nilai non-default tersimpan sebagai precondition: Approval Timeout `7`.
- State global yang diubah: nilai tersimpan tab Approval Settings (non-default, default, lalu perubahan Save pada TC klik ganda); pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Atur nilai tersimpan Approval Timeout menjadi `7` lewat Fixture BE
2. Muat ulang halaman dengan F5, lalu buka tab Approval Settings

### TC-AC-LCS-246: Reset to Default tab Approval Settings dari nilai tersimpan non-default

3. Ubah Approval Timeout menjadi `1` tanpa menyimpan
4. Klik `[Reset to Default]`
5. Verifikasi tidak ada dialog konfirmasi apa pun
6. Verifikasi toast sukses "Success, approval settings have been reset to default."
7. Verifikasi tab refresh dengan nilai default `3`
8. Verifikasi `[Save]` disabled
9. Muat ulang halaman dengan F5, lalu buka kembali tab Approval Settings
10. Verifikasi nilai default `3` bertahan (tersimpan)

### TC-AC-LCS-247: Reset to Default tab Approval Settings saat nilai tersimpan sudah default tetap sukses

11. Klik `[Reset to Default]` tanpa mengubah field apa pun
12. Verifikasi tidak ada dialog konfirmasi
13. Verifikasi toast sukses "Success, approval settings have been reset to default."
14. Verifikasi nilai tab tetap default `3`
15. Verifikasi `[Save]` disabled

### TC-AC-LCS-249: Klik ganda cepat pada [Save] tab Approval Settings hanya memproses satu permintaan

16. Tunggu toast sebelumnya hilang otomatis
17. Tahan respons Save tab Approval Settings (intercept)
18. Ubah Approval Timeout dari `3` menjadi `4`
19. Klik dua kali cepat pada `[Save]`
20. Verifikasi `[Save]` menampilkan loading
21. Verifikasi `[Save]` disabled setelah klik pertama
22. Verifikasi tepat satu permintaan Save terkirim ke server
23. Lepas tahanan respons Save
24. Verifikasi satu toast sukses "Success, approval settings have been saved."
25. Verifikasi Approval Timeout bernilai `4`

### TC-AC-LCS-250: Klik ganda cepat pada [Reset to Default] tab Approval Settings hanya memproses satu permintaan

26. Atur nilai tersimpan Approval Timeout menjadi `7` lewat Fixture BE
27. Muat ulang halaman dengan F5, lalu buka tab Approval Settings
28. Tahan respons Reset tab Approval Settings (intercept)
29. Klik dua kali cepat pada `[Reset to Default]`
30. Verifikasi `[Reset to Default]` menampilkan loading
31. Verifikasi `[Reset to Default]` disabled setelah klik pertama
32. Verifikasi tepat satu permintaan Reset terkirim ke server
33. Lepas tahanan respons Reset
34. Verifikasi satu toast sukses "Success, approval settings have been reset to default."

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 26 (mengatur nilai tersimpan non-default sebagai precondition TC), langkah 2, 9, 27 (memuat ulang halaman agar tab membaca nilai dari server), langkah 16 (menunggu toast sebelumnya hilang otomatis supaya asersi satu toast sukses tidak terpenuhi toast lama), langkah 17, 28 (menahan respons), dan langkah 23, 33 (melepas tahanan respons).
- Urutan di spec: TC-AC-LCS-246, TC-AC-LCS-247, lalu klik ganda (Reset sebelum klik ganda mengikuti bagian 3); urutan sama dengan nomor TC kecuali TC klik ganda ditempatkan sesudah kedua TC Reset.
- Asersi toast sukses sesudah klik ganda ditulis setelah respons dilepas karena toast hasil belum dapat muncul selama respons ditahan (bagian 8b butir 11).
- Asersi absence dialog konfirmasi ditulis segera setelah klik `[Reset to Default]`; toast sukses sesudahnya menjadi anchor positif (bagian 8b butir 11).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - Post Condition "Entri Changelog" (satu baris per field berubah) pada TC yang menyimpan atau mereset tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini; spec ini tidak mengamati Changelog.
  - Expected TC-AC-LCS-249 dan TC-AC-LCS-250 menuntut state loading dan disabled teramati sesudah klik pertama, tetapi precondition TC tidak menyebut penahan respons; spec menahan respons lewat intercept (kemampuan tercantum di Prerequisites).
  - Expected "tepat satu permintaan terkirim" membutuhkan kemampuan membaca daftar permintaan jaringan yang tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE.
