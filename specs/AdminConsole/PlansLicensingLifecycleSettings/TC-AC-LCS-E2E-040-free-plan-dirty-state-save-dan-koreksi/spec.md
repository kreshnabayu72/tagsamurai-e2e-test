---
id: TC-AC-LCS-E2E-040-free-plan-dirty-state-save-dan-koreksi
title: "Tab Free Plan Settings: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-134
  - TC-AC-LCS-135
  - TC-AC-LCS-136
  - TC-AC-LCS-143
coverage:
  web: automated
---

# Tab Free Plan Settings: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Free Plan Settings (Free Plan Duration `365`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Free Plan Settings adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab Free Plan Settings

### TC-AC-LCS-134: Save mengikuti dirty state dan Reset to Default selalu enabled

2. Verifikasi `[Save]` disabled pada kondisi awal
3. Verifikasi `[Reset to Default]` enabled pada kondisi awal
4. Ubah Free Plan Duration dari `365` menjadi `366`
5. Verifikasi `[Save]` enabled
6. Verifikasi `[Reset to Default]` enabled
7. Kembalikan Free Plan Duration menjadi `365`
8. Verifikasi `[Save]` disabled kembali
9. Verifikasi `[Reset to Default]` tetap enabled

### TC-AC-LCS-143: memperbaiki nilai yang salah menghapus pesan error dan meng-enable Save

10. Isi Free Plan Duration dengan `0`
11. Klik area kosong di luar field (blur)
12. Verifikasi pesan error rentang tampil pada Free Plan Duration
13. Verifikasi `[Save]` disabled
14. Isi Free Plan Duration dengan `366`
15. Klik area kosong di luar field (blur)
16. Verifikasi pesan error hilang
17. Verifikasi `[Save]` enabled

### TC-AC-LCS-135: Save tab Free Plan Settings dengan seluruh field diubah ke nilai valid

18. Ubah Free Plan Duration menjadi `400`
19. Klik `[Save]`
20. Verifikasi toast sukses "Success, free plan settings have been saved."
21. Verifikasi tab refresh: field memuat nilai tersimpan Free Plan Duration `400`
22. Verifikasi `[Save]` disabled
23. Muat ulang halaman dengan F5 lalu klik tab Free Plan Settings
24. Verifikasi setelah F5: Free Plan Duration bernilai `400`

### TC-AC-LCS-136: Save tab Free Plan Settings dengan nilai minimum yang valid

25. Ubah Free Plan Duration menjadi `1`, lalu klik area kosong di luar field (blur)
26. Verifikasi tidak ada pesan error pada seluruh field yang diisi
27. Klik `[Save]`
28. Verifikasi toast sukses "Success, free plan settings have been saved."
29. Verifikasi tab refresh: field memuat Free Plan Duration `1`
30. Verifikasi `[Save]` disabled

## Notes

- Urutan TC: 134, 143, 135, 136 (validasi yang diblokir dan perbaikannya sebelum Save sukses, S-10).
- Langkah penghubung (S-03): langkah 1 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-135 (entri Changelog `Edit` per field) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-LCS-143 menyebut "pesan error rentang" tanpa teks pesan; spec mengasersi keberadaan pesan tanpa mengutip teksnya (S-02).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
- Langkah 25 menyertakan blur sesuai TC ("lalu blur") sebelum asersi absence pada langkah 26, karena validasi rentang muncul saat blur (bagian 8b butir 2).
