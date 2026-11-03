---
id: TC-AC-LCS-E2E-049-validasi-field-second-reminder-before-event
title: "Validasi Field Second Reminder Before Event"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-179
  - TC-AC-LCS-180
  - TC-AC-LCS-181
  - TC-AC-LCS-182
coverage:
  web: automated
---

# Validasi Field Second Reminder Before Event

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

### TC-AC-LCS-179: Field Second Reminder Before Event menolak karakter non-numerik

2. Klik di akhir nilai field Second Reminder Before Event
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Second Reminder Before Event
5. Verifikasi nilai Second Reminder Before Event tetap `7`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-180: Field Second Reminder Before Event dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Second Reminder Before Event (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter second reminder before event" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error rentang nilai
13. Verifikasi inline error (severity danger) pada field Second Reminder Before Event: "Second reminder must be greater than final reminder" (nilai `1` tidak lebih besar dari Final Reminder `1`)
14. Verifikasi `[Save]` disabled
15. Ubah Second Reminder Before Event kembali menjadi `7` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-181: Field Second Reminder Before Event diisi 0 (di bawah minimum 1) menampilkan error rentang

16. Pilih seluruh isi field Second Reminder Before Event lalu ketik `0`
17. Klik area kosong di luar field (blur)
18. Verifikasi inline error text (severity danger) di bawah field Second Reminder Before Event: "Value must be between 1 and 999" (pesan rentang ditampilkan lebih dulu daripada pesan relasi)
19. Verifikasi `[Save]` disabled
20. Ubah Second Reminder Before Event kembali menjadi `7` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-182: Field Second Reminder Before Event membatasi input hingga 3 karakter

21. Pilih seluruh isi field Second Reminder Before Event lalu ketik `1234`
22. Verifikasi field menampilkan `123`: karakter ke-4 tidak dapat diketik
23. Verifikasi tidak ada pesan error rentang nilai (nilai `123` berada dalam rentang)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 15, 20 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Temuan untuk QA:
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
