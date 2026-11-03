---
id: TC-AC-LCS-E2E-072-validasi-field-approval-timeout
title: "Validasi Field Approval Timeout"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-237
  - TC-AC-LCS-238
  - TC-AC-LCS-239
  - TC-AC-LCS-240
  - TC-AC-LCS-241
coverage:
  web: automated
---

# Validasi Field Approval Timeout

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: field Approval Timeout (default `3`, rentang valid sesuai pesan error "Value must be between 1 and 30").
- State global yang diubah: nilai tersimpan Approval Timeout menjadi `30` pada TC-AC-LCS-241; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab Approval Settings

### TC-AC-LCS-237: Field Approval Timeout menolak karakter non-numerik

2. Klik di akhir nilai field Approval Timeout
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Approval Timeout
5. Verifikasi nilai Approval Timeout tetap `3`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-238: Field Approval Timeout dikosongkan, placeholder tampil, dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Approval Timeout (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter approval timeout" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-239: Field Approval Timeout diisi 0 (di bawah minimum) menampilkan error rentang

14. Pilih seluruh isi field Approval Timeout lalu ketik `0`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Approval Timeout: "Value must be between 1 and 30"
17. Verifikasi `[Save]` disabled

### TC-AC-LCS-240: Field Approval Timeout diisi 31 (di atas maksimum) menampilkan error rentang

18. Pilih seluruh isi field Approval Timeout lalu ketik `31`
19. Klik area kosong di luar field (blur)
20. Verifikasi inline error text (severity danger) di bawah field Approval Timeout: "Value must be between 1 and 30"
21. Verifikasi `[Save]` disabled

### TC-AC-LCS-241: Save Approval Timeout pada nilai maksimum

22. Ubah Approval Timeout menjadi `30`
23. Verifikasi tidak ada pesan error rentang pada Approval Timeout saat nilai `30` diisi
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, approval settings have been saved."
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5, lalu buka kembali tab Approval Settings
28. Verifikasi Approval Timeout bernilai `30` (nilai tersimpan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka tab; hook `beforeEach` suite membuka tab Trial Settings).
- Urutan mengikuti nomor TC; Save sukses pada nilai maksimum berada paling akhir sesudah semua validasi yang diblokir (S-10). Field dibersihkan oleh isi ulang pada TC berikutnya (tiap TC memilih seluruh isi field lebih dulu).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
