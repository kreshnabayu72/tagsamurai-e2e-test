---
id: TC-AC-LCS-E2E-078-validasi-field-hierarchy-depth-limit
title: "Validasi Field Hierarchy Depth Limit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-267
  - TC-AC-LCS-268
  - TC-AC-LCS-269
  - TC-AC-LCS-270
  - TC-AC-LCS-271
coverage:
  web: automated
---

# Validasi Field Hierarchy Depth Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: field Hierarchy Depth Limit (default `50`, rentang valid sesuai pesan error "Value must be between 5 and 100").
- State global yang diubah: nilai tersimpan Hierarchy Depth Limit menjadi `100` pada TC-AC-LCS-271; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab System Limits

### TC-AC-LCS-267: Field Hierarchy Depth Limit menolak karakter non-numerik

2. Klik di akhir nilai field Hierarchy Depth Limit
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Hierarchy Depth Limit
5. Verifikasi nilai Hierarchy Depth Limit tetap `50`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-268: Field Hierarchy Depth Limit dikosongkan, placeholder tampil, dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Hierarchy Depth Limit (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter hierarchy depth limit" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `5`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-269: Field Hierarchy Depth Limit diisi 4 (di bawah minimum) menampilkan error rentang

14. Pilih seluruh isi field Hierarchy Depth Limit lalu ketik `4`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Hierarchy Depth Limit: "Value must be between 5 and 100"
17. Verifikasi `[Save]` disabled

### TC-AC-LCS-270: Field Hierarchy Depth Limit diisi 101 (di atas maksimum) menampilkan error rentang

18. Pilih seluruh isi field Hierarchy Depth Limit lalu ketik `101`
19. Klik area kosong di luar field (blur)
20. Verifikasi inline error text (severity danger) di bawah field Hierarchy Depth Limit: "Value must be between 5 and 100"
21. Verifikasi `[Save]` disabled

### TC-AC-LCS-271: Save Hierarchy Depth Limit pada nilai maksimum

22. Ubah Hierarchy Depth Limit menjadi `100`
23. Verifikasi tidak ada pesan error rentang pada Hierarchy Depth Limit saat nilai `100` diisi
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, system limits settings have been saved."
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5, lalu buka kembali tab System Limits
28. Verifikasi Hierarchy Depth Limit bernilai `100` (nilai tersimpan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka tab; hook `beforeEach` suite membuka tab Trial Settings).
- Urutan mengikuti nomor TC; Save sukses pada nilai maksimum berada paling akhir sesudah semua validasi yang diblokir (S-10). Field dibersihkan oleh isi ulang pada TC berikutnya (tiap TC memilih seluruh isi field lebih dulu).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
