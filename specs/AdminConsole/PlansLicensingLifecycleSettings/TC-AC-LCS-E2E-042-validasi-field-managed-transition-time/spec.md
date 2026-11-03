---
id: TC-AC-LCS-E2E-042-validasi-field-managed-transition-time
title: "Validasi Field Managed Transition Time"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-144
  - TC-AC-LCS-145
  - TC-AC-LCS-146
  - TC-AC-LCS-147
  - TC-AC-LCS-148
coverage:
  web: automated
---

# Validasi Field Managed Transition Time

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

### TC-AC-LCS-144: Field Managed Transition Time menolak karakter non-numerik

2. Klik di akhir nilai field Managed Transition Time
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Managed Transition Time
5. Verifikasi nilai Managed Transition Time tetap `24`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-145: Field Managed Transition Time dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Managed Transition Time (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter managed transition time" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-146: Field Managed Transition Time diisi 0 (di bawah minimum 1) menampilkan error rentang

14. Pilih seluruh isi field Managed Transition Time lalu ketik `0`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Managed Transition Time: "Value must be between 1 and 999"
17. Verifikasi `[Save]` disabled
18. Ubah Managed Transition Time kembali menjadi `24` lalu klik area kosong di luar field (blur)

### TC-AC-LCS-147: Field Managed Transition Time membatasi input hingga 3 karakter

19. Pilih seluruh isi field Managed Transition Time lalu ketik `1234`
20. Verifikasi field menampilkan `123`: karakter ke-4 tidak dapat diketik
21. Verifikasi tidak ada pesan error rentang nilai (nilai `123` berada dalam rentang)

### TC-AC-LCS-148: Save Managed Transition Time pada nilai maksimum 999

22. Ubah Managed Transition Time menjadi `999`
23. Verifikasi tidak ada pesan error rentang pada Managed Transition Time saat nilai `999` diisi
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, license timing settings have been saved."
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5 lalu klik tab License Timing
28. Verifikasi Managed Transition Time bernilai `999` (nilai tersimpan)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 18 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Validasi yang diblokir berada sebelum aksi sukses: urutan mengikuti nomor TC dan TC Save nilai maksimum berada di akhir spec (S-10).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-148 (nilai tersimpan) setara dengan `Verifikasi` nilai sesudah F5 pada langkah 28; tidak ada asersi tambahan.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
