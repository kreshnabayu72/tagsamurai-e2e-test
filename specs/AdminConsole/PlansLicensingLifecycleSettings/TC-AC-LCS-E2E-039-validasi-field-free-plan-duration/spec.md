---
id: TC-AC-LCS-E2E-039-validasi-field-free-plan-duration
title: "Validasi Field Free Plan Duration"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-129
  - TC-AC-LCS-130
  - TC-AC-LCS-131
  - TC-AC-LCS-132
  - TC-AC-LCS-133
coverage:
  web: automated
---

# Validasi Field Free Plan Duration

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

### TC-AC-LCS-129: Field Free Plan Duration menolak karakter non-numerik

2. Klik di akhir nilai field Free Plan Duration
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Free Plan Duration
5. Verifikasi nilai Free Plan Duration tetap `365`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-130: Field Free Plan Duration dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Free Plan Duration (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter free plan duration" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-131: Field Free Plan Duration diisi 0 (di bawah minimum 1) menampilkan error rentang

14. Pilih seluruh isi field Free Plan Duration lalu ketik `0`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Free Plan Duration: "Value must be between 1 and 9,999"
17. Verifikasi `[Save]` disabled
18. Ubah Free Plan Duration kembali menjadi `365` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-132: Field Free Plan Duration diisi 10000 (di atas maksimum 9,999) menampilkan error rentang

19. Pilih seluruh isi field Free Plan Duration lalu ketik `10000`
20. Klik area kosong di luar field (blur)
21. Verifikasi inline error text (severity danger) di bawah field Free Plan Duration: "Value must be between 1 and 9,999"
22. Verifikasi `[Save]` disabled
23. Ubah Free Plan Duration kembali menjadi `365` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-133: Save Free Plan Duration pada nilai maksimum 9,999

24. Ubah Free Plan Duration menjadi `9999`
25. Verifikasi tidak ada pesan error rentang pada Free Plan Duration saat nilai `9999` diisi
26. Klik `[Save]`
27. Verifikasi toast sukses "Success, free plan settings have been saved."
28. Verifikasi `[Save]` disabled setelah tab refresh
29. Muat ulang halaman dengan F5 lalu klik tab Free Plan Settings
30. Verifikasi Free Plan Duration bernilai `9999` (nilai tersimpan)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 18, 23 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Validasi yang diblokir berada sebelum aksi sukses: urutan mengikuti nomor TC dan TC Save nilai maksimum berada di akhir spec (S-10).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-133 (nilai tersimpan) setara dengan `Verifikasi` nilai sesudah F5 pada langkah 30; tidak ada asersi tambahan.
  - TC-AC-LCS-132 mengetik `10000` (lima karakter) dan mengharapkan error rentang "Value must be between 1 and 9,999", sedangkan batas maksimum 9,999 berbentuk empat digit dan TC-AC-LCS-209 menunjukkan field memotong input pada jumlah karakter maksimum; bila field memiliki hard cap empat karakter, nilai menjadi `1000` dan error tidak tampil (kemungkinan kontradiktif). Spec mengikuti TC.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
