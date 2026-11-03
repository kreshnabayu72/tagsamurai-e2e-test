---
id: TC-AC-LCS-E2E-054-validasi-field-purge-urgent-warning-email
title: "Validasi Field Purge Urgent Warning Email"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-202
  - TC-AC-LCS-203
  - TC-AC-LCS-204
  - TC-AC-LCS-205
coverage:
  web: automated
---

# Validasi Field Purge Urgent Warning Email

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Client Lifecycle (Notify Plan Owner Before Event `45`, First Reminder Before Event `30`, Second Reminder Before Event `7`, Final Reminder Before Event `1`, Grace Period Duration `30`, Archive Period Duration `30`, Purge Warning Email `10`, Purge Urgent Warning Email `2`, Post-Purge Retention `730`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Client Lifecycle adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.

## Test Steps

1. Klik tab Client Lifecycle

### TC-AC-LCS-202: Field Purge Urgent Warning Email menolak karakter non-numerik

2. Klik di akhir nilai field Purge Urgent Warning Email
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Purge Urgent Warning Email
5. Verifikasi nilai Purge Urgent Warning Email tetap `2`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-203: Field Purge Urgent Warning Email dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Purge Urgent Warning Email (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter purge urgent warning email" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-204: Field Purge Urgent Warning Email diisi 0 (di bawah minimum 1) menampilkan error rentang

14. Pilih seluruh isi field Purge Urgent Warning Email lalu ketik `0`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Purge Urgent Warning Email: "Value must be between 1 and 999"
17. Verifikasi `[Save]` disabled
18. Ubah Purge Urgent Warning Email kembali menjadi `2` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-205: Field Purge Urgent Warning Email membatasi input hingga 3 karakter

19. Pilih seluruh isi field Purge Urgent Warning Email lalu ketik `1234`
20. Verifikasi field menampilkan `123`: karakter ke-4 tidak dapat diketik
21. Verifikasi tidak ada pesan error rentang nilai (nilai `123` berada dalam rentang)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 18 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Temuan untuk QA:
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
