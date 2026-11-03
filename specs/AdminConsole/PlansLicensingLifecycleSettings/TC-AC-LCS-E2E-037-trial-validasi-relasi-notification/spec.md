---
id: TC-AC-LCS-E2E-037-trial-validasi-relasi-notification
title: "Tab Trial Settings: Validasi Relasi First Notification dan Second Notification"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-295
  - TC-AC-LCS-296
  - TC-AC-LCS-297
  - TC-AC-LCS-298
coverage:
  web: automated
---

# Tab Trial Settings: Validasi Relasi First Notification dan Second Notification

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

### TC-AC-LCS-295: First Notification lebih kecil dari Second Notification menampilkan error relasi

1. Ubah Second Notification dari `1` menjadi `10`
2. Klik area kosong di luar field (blur)
3. Verifikasi inline error (severity danger) pada field First Notification: "First notification must be greater than second notification"
4. Verifikasi `[Save]` disabled

### TC-AC-LCS-296: First Notification sama dengan Second Notification menampilkan error relasi

5. Ubah Second Notification kembali menjadi `1` lalu klik area kosong di luar field (blur)
6. Ubah Second Notification dari `1` menjadi `7`
7. Klik area kosong di luar field (blur)
8. Verifikasi inline error (severity danger) pada field First Notification: "First notification must be greater than second notification"
9. Verifikasi `[Save]` disabled

### TC-AC-LCS-297: Memperbaiki relasi First Notification dan Second Notification menghapus error dan meng-enable Save

10. Ubah Second Notification menjadi `10` lalu klik area kosong di luar field (blur)
11. Ubah First Notification menjadi `20`
12. Klik area kosong di luar field (blur)
13. Verifikasi pesan error relasi hilang
14. Verifikasi `[Save]` enabled

### TC-AC-LCS-298: First Notification satu lebih besar dari Second Notification diterima

15. Ubah First Notification menjadi `8`
16. Ubah Second Notification menjadi `7`
17. Klik area kosong di luar field (blur)
18. Verifikasi tidak ada pesan error relasi
19. Klik `[Save]`
20. Verifikasi toast sukses "Success, trial settings have been saved."
21. Verifikasi nilai tersimpan First Notification `8` dan Second Notification `7`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5, 10 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- TC-AC-LCS-295 dan TC-AC-LCS-296 menampilkan error identik pada field yang sama, sehingga langkah pembersih disisipkan di antaranya (R-12). Precondition TC-AC-LCS-297 (error relasi tampil karena Second Notification `10`) dibangun oleh langkah penghubung sebelum perbaikan.
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-298 (First Notification dan Second Notification tersimpan) setara dengan `Verifikasi` nilai tersimpan pada langkah terakhir; tidak ada asersi tambahan.
  - TC-AC-LCS-297 tidak menyebut cara memverifikasi bahwa error relasi tampil sebelum perbaikan (precondition d); spec tidak menambah asersi itu (S-03).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
