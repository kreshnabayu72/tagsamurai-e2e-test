---
id: TC-AC-LCS-E2E-055-validasi-field-post-purge-retention
title: "Validasi Field Post-Purge Retention: Non-numerik, Kosong, Di Bawah Minimum, dan Batas Karakter"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-206
  - TC-AC-LCS-207
  - TC-AC-LCS-208
  - TC-AC-LCS-209
coverage:
  web: automated
---

# Validasi Field Post-Purge Retention: Non-numerik, Kosong, Di Bawah Minimum, dan Batas Karakter

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

### TC-AC-LCS-206: Field Post-Purge Retention menolak karakter non-numerik

2. Klik di akhir nilai field Post-Purge Retention
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Post-Purge Retention
5. Verifikasi nilai Post-Purge Retention tetap `730`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-207: Field Post-Purge Retention dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Post-Purge Retention (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter post-purge retention" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-208: Field Post-Purge Retention diisi 0 (di bawah minimum 1) menampilkan error rentang

14. Pilih seluruh isi field Post-Purge Retention lalu ketik `0`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Post-Purge Retention: "Value must be between 1 and 3,650"
17. Verifikasi `[Save]` disabled
18. Ubah Post-Purge Retention kembali menjadi `730` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-209: Field Post-Purge Retention membatasi input hingga 4 karakter

19. Pilih seluruh isi field Post-Purge Retention lalu ketik `99999`
20. Verifikasi field menampilkan `9999`: karakter ke-5 tidak dapat diketik
21. Klik area kosong di luar field (blur)
22. Verifikasi inline error text (severity danger): "Value must be between 1 and 3,650" karena `9999` melebihi 3,650
23. Ubah Post-Purge Retention kembali menjadi `730` lalu klik area kosong di luar field (blur)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 18, 21, 23 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Langkah blur pada TC-AC-LCS-209 ditambahkan sebagai langkah penghubung karena pesan error rentang pada Expected b muncul setelah blur; langkah terakhir mengembalikan field ke nilai tersimpan agar form tidak berakhir dirty (S-09).
- Temuan untuk QA:
  - TC-AC-LCS-209 tidak menyebut langkah blur pada kolom Langkah, padahal Expected b menyebut "Setelah blur"; spec menambahkan blur sebagai langkah penghubung (S-15).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
