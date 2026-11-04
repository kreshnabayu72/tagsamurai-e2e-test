---
id: TC-AC-LCS-E2E-187-license-timing-save-nilai-minimum
title: "Tab License Timing: Save Nilai Minimum"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-161
coverage:
  web: automated
---

# Tab License Timing: Save Nilai Minimum

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: License Timing (Managed Transition Time `24`, Managed Action Retry Delay `2`, Addon Reactivation Delay `2`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab License Timing adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab License Timing

### TC-AC-LCS-161: Save tab License Timing dengan nilai minimum yang valid

2. Ubah Managed Transition Time menjadi `1`, lalu klik area kosong di luar field (blur)
3. Ubah Managed Action Retry Delay menjadi `1`, lalu klik area kosong di luar field (blur)
4. Ubah Addon Reactivation Delay menjadi `1`, lalu klik area kosong di luar field (blur)
5. Verifikasi tidak ada pesan error pada seluruh field yang diisi
6. Klik `[Save]`
7. Verifikasi toast sukses "Success, license timing settings have been saved."
8. Verifikasi tab refresh: field memuat Managed Transition Time `1`, Managed Action Retry Delay `1`, Addon Reactivation Delay `1`
9. Verifikasi `[Save]` disabled

## Notes

- Langkah penghubung (S-03): langkah 1 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- TC-AC-LCS-161 berada di spec terpisah dari TC dirty state dan Save License Timing lainnya (spec 045) sebagai fakta pembagian TC lintas spec.
- Langkah 2 sampai 4 menyertakan blur sesuai TC-AC-LCS-161 langkah 1 sampai 3 ("lalu blur") sebelum asersi absence pada langkah 5, karena validasi rentang muncul saat blur (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-161 (nilai License Timing tersimpan sesuai Data Uji) setara dengan `Verifikasi` nilai tersimpan; tidak ada asersi tambahan.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
