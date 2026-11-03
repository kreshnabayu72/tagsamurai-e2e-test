---
id: TC-AC-LCS-E2E-053-validasi-field-purge-warning-email
title: "Validasi Field Purge Warning Email"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-197
  - TC-AC-LCS-198
  - TC-AC-LCS-199
  - TC-AC-LCS-200
  - TC-AC-LCS-201
coverage:
  web: automated
---

# Validasi Field Purge Warning Email

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

### TC-AC-LCS-197: Field Purge Warning Email menolak karakter non-numerik

2. Klik di akhir nilai field Purge Warning Email
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Purge Warning Email
5. Verifikasi nilai Purge Warning Email tetap `10`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-198: Field Purge Warning Email dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Purge Warning Email (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter purge warning email" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error rentang nilai
13. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning must be greater than urgent warning" (nilai `1` tidak lebih besar dari Purge Urgent Warning Email `2`)
14. Verifikasi `[Save]` disabled
15. Ubah Purge Warning Email kembali menjadi `10` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-199: Field Purge Warning Email diisi 0 (di bawah minimum 1) menampilkan error rentang

16. Pilih seluruh isi field Purge Warning Email lalu ketik `0`
17. Klik area kosong di luar field (blur)
18. Verifikasi inline error text (severity danger) di bawah field Purge Warning Email: "Value must be between 1 and 999" (pesan rentang ditampilkan lebih dulu daripada pesan relasi)
19. Verifikasi `[Save]` disabled
20. Ubah Purge Warning Email kembali menjadi `10` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-200: Field Purge Warning Email membatasi input hingga 3 karakter

21. Pilih seluruh isi field Purge Warning Email lalu ketik `1234`
22. Verifikasi field menampilkan `123`: karakter ke-4 tidak dapat diketik
23. Verifikasi tidak ada pesan error rentang nilai (nilai `123` berada dalam rentang)

### TC-AC-LCS-201: Save Purge Warning Email pada nilai maksimum 999

24. Ubah Archive Period Duration menjadi `999`
25. Ubah Purge Warning Email menjadi `999`
26. Verifikasi tidak ada pesan error rentang pada Purge Warning Email saat nilai `999` diisi
27. Klik `[Save]`
28. Verifikasi toast sukses "Success, client lifecycle settings have been saved."
29. Verifikasi `[Save]` disabled setelah tab refresh
30. Muat ulang halaman dengan F5 lalu klik tab Client Lifecycle
31. Verifikasi Purge Warning Email bernilai `999` (nilai tersimpan)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 15, 20 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Validasi yang diblokir berada sebelum aksi sukses: urutan mengikuti nomor TC dan TC Save nilai maksimum berada di akhir spec (S-10).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-201 (nilai tersimpan) setara dengan `Verifikasi` nilai sesudah F5 pada langkah 31; tidak ada asersi tambahan.
  - TC-AC-LCS-201 mengubah Archive Period Duration menjadi `999` sebagai langkah pertama, tetapi Data Uji dan Expected hanya menyebut Purge Warning Email `999`; spec mengikuti langkah TC tanpa asersi atas Archive Period Duration.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
