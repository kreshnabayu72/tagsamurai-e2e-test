---
id: TC-AC-LCS-E2E-076-validasi-field-selection-limit
title: "Validasi Field Selection Limit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-257
  - TC-AC-LCS-258
  - TC-AC-LCS-259
  - TC-AC-LCS-260
  - TC-AC-LCS-261
coverage:
  web: automated
---

# Validasi Field Selection Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Data Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: field Selection Limit (default `1000`, rentang valid sesuai pesan error "Value must be between 100 and 5,000").
- State global yang diubah: nilai tersimpan Selection Limit menjadi `5000` pada TC-AC-LCS-261; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab System Limits

### TC-AC-LCS-257: Field Selection Limit menolak karakter non-numerik

2. Klik di akhir nilai field Selection Limit
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Selection Limit
5. Verifikasi nilai Selection Limit tetap `1000`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-258: Field Selection Limit dikosongkan, placeholder tampil, dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Selection Limit (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter selection limit" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `100`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-259: Field Selection Limit diisi 99 (di bawah minimum) menampilkan error rentang

14. Pilih seluruh isi field Selection Limit lalu ketik `99`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Selection Limit: "Value must be between 100 and 5,000"
17. Verifikasi `[Save]` disabled

### TC-AC-LCS-260: Field Selection Limit diisi 5001 (di atas maksimum) menampilkan error rentang

18. Pilih seluruh isi field Selection Limit lalu ketik `5001`
19. Klik area kosong di luar field (blur)
20. Verifikasi inline error text (severity danger) di bawah field Selection Limit: "Value must be between 100 and 5,000"
21. Verifikasi `[Save]` disabled

### TC-AC-LCS-261: Save Selection Limit pada nilai maksimum

22. Ubah Selection Limit menjadi `5000`, lalu klik area kosong di luar field (blur)
23. Verifikasi tidak ada pesan error rentang pada Selection Limit saat nilai `5000` diisi
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, system limits settings have been saved."
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5, lalu buka kembali tab System Limits
28. Verifikasi Selection Limit bernilai `5000` (nilai tersimpan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka tab; hook `beforeEach` suite membuka tab Trial Settings).
- Urutan mengikuti nomor TC; Save sukses pada nilai maksimum berada paling akhir sesudah semua validasi yang diblokir (S-10). Field dibersihkan oleh isi ulang pada TC berikutnya (tiap TC memilih seluruh isi field lebih dulu).
- Asersi "tidak ada pesan error" ditulis sesudah blur karena validasi field muncul saat blur.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
