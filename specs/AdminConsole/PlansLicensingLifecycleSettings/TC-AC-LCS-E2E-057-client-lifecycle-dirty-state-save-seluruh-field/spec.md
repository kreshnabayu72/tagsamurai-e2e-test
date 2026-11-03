---
id: TC-AC-LCS-E2E-057-client-lifecycle-dirty-state-save-seluruh-field
title: "Tab Client Lifecycle: Dirty State dan Save Seluruh Sembilan Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-212
  - TC-AC-LCS-213
coverage:
  web: automated
---

# Tab Client Lifecycle: Dirty State dan Save Seluruh Sembilan Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Client Lifecycle (Notify Plan Owner Before Event `45`, First Reminder Before Event `30`, Second Reminder Before Event `7`, Final Reminder Before Event `1`, Grace Period Duration `30`, Archive Period Duration `30`, Purge Warning Email `10`, Purge Urgent Warning Email `2`, Post-Purge Retention `730`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Client Lifecycle adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab Client Lifecycle

### TC-AC-LCS-212: Save mengikuti dirty state dan Reset to Default selalu enabled

2. Verifikasi `[Save]` disabled pada kondisi awal
3. Verifikasi `[Reset to Default]` enabled pada kondisi awal
4. Ubah Notify Plan Owner Before Event dari `45` menjadi `46`
5. Verifikasi `[Save]` enabled
6. Verifikasi `[Reset to Default]` enabled
7. Kembalikan Notify Plan Owner Before Event menjadi `45`
8. Verifikasi `[Save]` disabled kembali
9. Verifikasi `[Reset to Default]` tetap enabled

### TC-AC-LCS-213: Save tab Client Lifecycle dengan seluruh field diubah ke nilai valid

10. Ubah Notify Plan Owner Before Event menjadi `60`
11. Ubah First Reminder Before Event menjadi `45`
12. Ubah Second Reminder Before Event menjadi `14`
13. Ubah Final Reminder Before Event menjadi `3`
14. Ubah Grace Period Duration menjadi `20`
15. Ubah Archive Period Duration menjadi `25`
16. Ubah Purge Warning Email menjadi `12`
17. Ubah Purge Urgent Warning Email menjadi `4`
18. Ubah Post-Purge Retention menjadi `1000`
19. Klik `[Save]`
20. Verifikasi toast sukses "Success, client lifecycle settings have been saved."
21. Verifikasi tab refresh: field memuat nilai tersimpan Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000`
22. Verifikasi `[Save]` disabled
23. Muat ulang halaman dengan F5 lalu klik tab Client Lifecycle
24. Verifikasi setelah F5: Notify Plan Owner Before Event bernilai `60`
25. Verifikasi setelah F5: First Reminder Before Event bernilai `45`
26. Verifikasi setelah F5: Second Reminder Before Event bernilai `14`
27. Verifikasi setelah F5: Final Reminder Before Event bernilai `3`
28. Verifikasi setelah F5: Grace Period Duration bernilai `20`
29. Verifikasi setelah F5: Archive Period Duration bernilai `25`
30. Verifikasi setelah F5: Purge Warning Email bernilai `12`
31. Verifikasi setelah F5: Purge Urgent Warning Email bernilai `4`
32. Verifikasi setelah F5: Post-Purge Retention bernilai `1000`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-213 (entri Changelog `Edit` per field) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
