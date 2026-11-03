---
id: TC-AC-LCS-E2E-038-input-angka-tempel-dan-normalisasi
title: "Input Angka: Tempel Teks Campuran, Normalisasi Awalan Nol, dan Batas Karakter Hard Cap"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-673
  - TC-AC-LCS-674
  - TC-AC-LCS-685
coverage:
  web: automated
---

# Input Angka: Tempel Teks Campuran, Normalisasi Awalan Nol, dan Batas Karakter Hard Cap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Trial Settings (Max Trial Duration `30`, Max Trial Asset Quota `50`, Max Trial Concurrent User Quota `10`, Require Approval for Trial Activation `OFF`, First Notification `7`, Second Notification `1`); License Timing (Managed Transition Time `24`, Managed Action Retry Delay `2`, Addon Reactivation Delay `2`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE); menempel teks dari clipboard ke field (disediakan tim FE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Trial Settings adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.

## Test Steps

### TC-AC-LCS-673: Tempel teks campuran ke field Max Trial Duration hanya memasukkan digitnya

1. Klik field Max Trial Duration lalu pilih seluruh isinya
2. Tempel teks `12abc` dari clipboard
3. Verifikasi field menampilkan `12` (karakter `a`, `b`, `c` tidak masuk)
4. Verifikasi tidak ada pesan error
5. Verifikasi `[Save]` enabled (nilai `12` berbeda dari nilai tersimpan `30`)
6. Ubah Max Trial Duration kembali menjadi `30`

### TC-AC-LCS-674: Angka berawalan nol pada field Max Trial Duration dinormalkan saat blur dan tidak membuat form dirty

7. Klik field Max Trial Duration, pilih seluruh isinya, ketik `030`
8. Klik area kosong di luar field (blur)
9. Verifikasi setelah blur field menampilkan `30`
10. Verifikasi `[Save]` disabled karena nilai ternormalisasi `30` sama dengan nilai tersimpan

### TC-AC-LCS-685: Tempel angka melebihi hard cap karakter pada field Managed Transition Time dipotong ke batas karakter

11. Klik tab License Timing
12. Klik field Managed Transition Time lalu pilih seluruh isinya
13. Tempel teks `12345` dari clipboard
14. Verifikasi field menampilkan `123` (hard cap 3 karakter)
15. Verifikasi tidak ada pesan error
16. Verifikasi `[Save]` enabled (nilai `123` berbeda dari nilai tersimpan `24`)
17. Ubah Managed Transition Time kembali menjadi `24`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6, 11, 17 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Pindah dari tab Trial Settings ke tab License Timing dilakukan sesudah Max Trial Duration dikembalikan ke nilai tersimpan, sehingga dialog `Unsaved Changes` tidak muncul; langkah terakhir mengembalikan Managed Transition Time ke nilai tersimpan agar form tidak berakhir dirty (S-09).
- Temuan untuk QA:
  - TC-AC-LCS-685 (field Managed Transition Time di tab License Timing) berada di section TC Trial Settings; spec menempatkannya bersama TC input angka sejenis.
  - Mekanisme menempel dari clipboard tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE (S-13).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
