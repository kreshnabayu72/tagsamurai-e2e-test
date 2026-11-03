---
id: TC-AC-LCS-E2E-073-approval-settings-dirty-state-save-dan-koreksi
title: "Tab Approval Settings: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-242
  - TC-AC-LCS-243
  - TC-AC-LCS-244
  - TC-AC-LCS-251
coverage:
  web: automated
---

# Tab Approval Settings: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Data Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: Approval Timeout default `3`, nilai uji `4`, `0`, `1`, dan `7`.
- State global yang diubah: nilai tersimpan Approval Timeout menjadi `1` lalu `7`; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab Approval Settings

### TC-AC-LCS-242: Tab Approval Settings: Save mengikuti dirty state dan Reset to Default selalu enabled

2. Verifikasi `[Save]` disabled
3. Verifikasi `[Reset to Default]` enabled
4. Ubah Approval Timeout dari `3` menjadi `4`
5. Verifikasi `[Save]` enabled
6. Verifikasi `[Reset to Default]` enabled
7. Kembalikan Approval Timeout menjadi `3`
8. Verifikasi `[Save]` disabled kembali
9. Verifikasi `[Reset to Default]` tetap enabled

### TC-AC-LCS-251: Tab Approval Settings: memperbaiki nilai yang salah menghapus pesan error dan meng-enable Save

10. Isi Approval Timeout dengan `0`, lalu klik area kosong di luar field (blur)
11. Verifikasi pesan error rentang "Value must be between 1 and 30" tampil
12. Verifikasi `[Save]` disabled
13. Isi Approval Timeout dengan `4`, lalu klik area kosong di luar field (blur)
14. Verifikasi pesan error hilang
15. Verifikasi `[Save]` enabled

### TC-AC-LCS-244: Save tab Approval Settings dengan nilai minimum yang valid

16. Ubah Approval Timeout menjadi `1`, lalu klik area kosong di luar field (blur)
17. Verifikasi tidak ada pesan error pada seluruh field yang diisi
18. Klik `[Save]`
19. Verifikasi toast sukses "Success, approval settings have been saved."
20. Verifikasi tab refresh: field memuat Approval Timeout `1`
21. Verifikasi `[Save]` disabled setelah tab refresh

### TC-AC-LCS-243: Save tab Approval Settings dengan seluruh field diubah ke nilai valid

22. Ubah Approval Timeout menjadi `7`
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, approval settings have been saved."
25. Verifikasi tab refresh: field memuat nilai tersimpan
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5, lalu buka kembali tab Approval Settings
28. Verifikasi Approval Timeout bernilai `7`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (berpindah ke tab) dan langkah 27 (membuka tab dalam keadaan termuat baru).
- Urutan di spec: TC-AC-LCS-242, TC-AC-LCS-251, TC-AC-LCS-244, TC-AC-LCS-243 (validasi yang diblokir dan koreksi nilai sebelum Save sukses, S-10); urutan nomor TC berbeda.
- Teks pesan error rentang pada TC-AC-LCS-251 diambil dari TC validasi field yang sama (Value must be between 1 and 30); Expected TC-AC-LCS-251 hanya menyebut "pesan error rentang".
- Asersi "tidak ada pesan error" ditulis sesudah blur karena validasi field muncul saat blur.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - Post Condition "Entri Changelog" (satu baris per field berubah) pada TC yang menyimpan atau mereset tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini; spec ini tidak mengamati Changelog.
  - Expected TC-AC-LCS-251 menyebut "pesan error rentang" tanpa teks; spec memakai teks dari TC validasi field yang sama.
