---
id: TC-AC-LCS-E2E-083-system-limits-reset-dan-klik-ganda
title: "Tab System Limits: Reset to Default dan Klik Ganda Cepat pada Save serta Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-286
  - TC-AC-LCS-287
  - TC-AC-LCS-289
  - TC-AC-LCS-290
coverage:
  web: automated
---

# Tab System Limits: Reset to Default dan Klik Ganda Cepat pada Save serta Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE/BE): Fixture BE untuk mengatur nilai tersimpan non-default pada tab yang diuji sebagai precondition TC.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` untuk menahan respons Save dan Reset tab System Limits di atas backend nyata dan melepasnya, serta membaca daftar permintaan jaringan; intercept dipulihkan hook `beforeEach` suite.
- Data uji: nilai default tab System Limits `1000, 1000, 1000, 50, 10000, 20` (urutan Bulk Transaction Row Limit, Selection Limit, Register Asset Bulk Limit, Hierarchy Depth Limit, Master Data Count Limit, Max Visible Columns); nilai non-default tersimpan sebagai precondition: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`.
- State global yang diubah: nilai tersimpan tab System Limits (non-default, default, lalu perubahan Save pada TC klik ganda); pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Atur nilai tersimpan tab System Limits ke nilai non-default lewat Fixture BE: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`
2. Muat ulang halaman dengan F5, lalu buka tab System Limits

### TC-AC-LCS-286: Reset to Default tab System Limits dari nilai tersimpan non-default

3. Ubah Bulk Transaction Row Limit menjadi `100` tanpa menyimpan
4. Klik `[Reset to Default]`
5. Verifikasi tidak ada dialog konfirmasi apa pun
6. Verifikasi toast sukses "Success, system limits settings have been reset to default."
7. Verifikasi tab refresh dengan nilai default `1000, 1000, 1000, 50, 10000, 20`
8. Verifikasi `[Save]` disabled
9. Muat ulang halaman dengan F5, lalu buka kembali tab System Limits
10. Verifikasi nilai default `1000, 1000, 1000, 50, 10000, 20` bertahan (tersimpan)

### TC-AC-LCS-287: Reset to Default tab System Limits saat nilai tersimpan sudah default tetap sukses

11. Klik `[Reset to Default]` tanpa mengubah field apa pun
12. Verifikasi tidak ada dialog konfirmasi
13. Verifikasi toast sukses "Success, system limits settings have been reset to default."
14. Verifikasi nilai tab tetap default `1000, 1000, 1000, 50, 10000, 20` (urutan Bulk Transaction Row Limit, Selection Limit, Register Asset Bulk Limit, Hierarchy Depth Limit, Master Data Count Limit, Max Visible Columns)
15. Verifikasi `[Save]` disabled

### TC-AC-LCS-289: Klik ganda cepat pada [Save] tab System Limits hanya memproses satu permintaan

16. Tahan respons Save tab System Limits (intercept)
17. Ubah Bulk Transaction Row Limit dari `1000` menjadi `1001`
18. Klik dua kali cepat pada `[Save]`
19. Verifikasi `[Save]` menampilkan loading
20. Verifikasi `[Save]` disabled setelah klik pertama
21. Verifikasi tepat satu permintaan Save terkirim ke server
22. Lepas tahanan respons Save
23. Verifikasi satu toast sukses "Success, system limits settings have been saved."
24. Verifikasi Bulk Transaction Row Limit bernilai `1001`

### TC-AC-LCS-290: Klik ganda cepat pada [Reset to Default] tab System Limits hanya memproses satu permintaan

25. Atur nilai tersimpan tab System Limits ke nilai non-default lewat Fixture BE: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`
26. Muat ulang halaman dengan F5, lalu buka tab System Limits
27. Tahan respons Reset tab System Limits (intercept)
28. Klik dua kali cepat pada `[Reset to Default]`
29. Verifikasi `[Reset to Default]` menampilkan loading
30. Verifikasi `[Reset to Default]` disabled setelah klik pertama
31. Verifikasi tepat satu permintaan Reset terkirim ke server
32. Lepas tahanan respons Reset
33. Verifikasi satu toast sukses "Success, system limits settings have been reset to default."

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 25 (mengatur nilai tersimpan non-default sebagai precondition TC), langkah 2, 9, 26 (memuat ulang halaman agar tab membaca nilai dari server), langkah 16, 27 (menahan respons), dan langkah 22, 32 (melepas tahanan respons).
- Urutan di spec: TC-AC-LCS-286, TC-AC-LCS-287, lalu klik ganda (Reset sebelum klik ganda mengikuti bagian 3); urutan sama dengan nomor TC kecuali TC klik ganda ditempatkan sesudah kedua TC Reset.
- Asersi toast sukses sesudah klik ganda ditulis setelah respons dilepas karena toast hasil belum dapat muncul selama respons ditahan (bagian 8b butir 11).
- Asersi absence dialog konfirmasi ditulis segera setelah klik `[Reset to Default]`; toast sukses sesudahnya menjadi anchor positif (bagian 8b butir 11).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - Post Condition "Entri Changelog" (satu baris per field berubah) pada TC yang menyimpan atau mereset tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini; spec ini tidak mengamati Changelog.
  - Expected TC-AC-LCS-289 dan TC-AC-LCS-290 menuntut state loading dan disabled teramati sesudah klik pertama, tetapi precondition TC tidak menyebut penahan respons; spec menahan respons lewat intercept (kemampuan tercantum di Prerequisites).
  - Expected "tepat satu permintaan terkirim" membutuhkan kemampuan membaca daftar permintaan jaringan yang tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE.
