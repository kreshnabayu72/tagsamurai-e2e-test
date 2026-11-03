---
id: TC-AC-LCS-E2E-067-validasi-field-permanently-delete-recycle-bin
title: "Validasi Field Permanently Delete Recycle Bin"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-222
  - TC-AC-LCS-223
  - TC-AC-LCS-224
  - TC-AC-LCS-225
  - TC-AC-LCS-226
coverage:
  web: automated
---

# Validasi Field Permanently Delete Recycle Bin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: field Permanently Delete Recycle Bin (default `30`, rentang valid sesuai pesan error "Value must be between 1 and 999").
- State global yang diubah: nilai tersimpan Permanently Delete Recycle Bin menjadi `999` pada TC-AC-LCS-226; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab Recycle Bin

### TC-AC-LCS-222: Field Permanently Delete Recycle Bin menolak karakter non-numerik

2. Klik di akhir nilai field Permanently Delete Recycle Bin
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Permanently Delete Recycle Bin
5. Verifikasi nilai Permanently Delete Recycle Bin tetap `30`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-223: Field Permanently Delete Recycle Bin dikosongkan, placeholder tampil, dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Permanently Delete Recycle Bin (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter permanently delete recycle bin" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-224: Field Permanently Delete Recycle Bin diisi 0 (di bawah minimum) menampilkan error rentang

14. Pilih seluruh isi field Permanently Delete Recycle Bin lalu ketik `0`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Permanently Delete Recycle Bin: "Value must be between 1 and 999"
17. Verifikasi `[Save]` disabled

### TC-AC-LCS-225: Field Permanently Delete Recycle Bin membatasi input hingga 3 karakter

18. Pilih seluruh isi field Permanently Delete Recycle Bin lalu ketik `1234`
19. Verifikasi field menampilkan `123`: karakter ke-4 tidak dapat diketik
20. Verifikasi tidak ada pesan error rentang nilai (nilai `123` berada dalam rentang)

### TC-AC-LCS-226: Save Permanently Delete Recycle Bin pada nilai maksimum

21. Ubah Permanently Delete Recycle Bin menjadi `999`
22. Verifikasi tidak ada pesan error rentang pada Permanently Delete Recycle Bin saat nilai `999` diisi
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, recycle bin settings have been saved."
25. Verifikasi `[Save]` disabled setelah tab refresh
26. Muat ulang halaman dengan F5, lalu buka kembali tab Recycle Bin
27. Verifikasi Permanently Delete Recycle Bin bernilai `999` (nilai tersimpan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka tab; hook `beforeEach` suite membuka tab Trial Settings).
- Urutan mengikuti nomor TC; Save sukses pada nilai maksimum berada paling akhir sesudah semua validasi yang diblokir (S-10). Field dibersihkan oleh isi ulang pada TC berikutnya (tiap TC memilih seluruh isi field lebih dulu).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
