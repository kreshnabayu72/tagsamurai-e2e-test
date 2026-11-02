---
id: TC-AC-CS-E2E-045-aksesibilitas-form-add-activate-trial-dan-edit
title: "Aksesibilitas Form Add, Activate Trial, dan Edit"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-568
  - TC-AC-CS-622
  - TC-AC-CS-623
coverage:
  web: automated
---

# Aksesibilitas Form Add, Activate Trial, dan Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit, TC-AC-CS-623): Create-Only Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Apotek Sehat Sentosa+{runId}-045` dengan term FAMS plan Growth berstatus Waiting for Approval, tanggal "—", Plan Owner PT Maju Bersama (Distributor), milik `Fajar Nugroho` (padanan Pre-setup #49); toggle `Require Approval for Allocation` PT Maju Bersama (Pre-setup #23) tidak diubah. Tidak ada Submit sukses pada spec ini.
- Kemampuan teknis (disediakan tim FE/BE): membaca atribut ARIA (`aria-required`, `aria-describedby`) dan urutan fokus elemen pada modal.

## Test Steps

### TC-AC-CS-568: Aksesibilitas form Add

1. Klik `[+ Subscription]`
2. Tekan `Tab` berulang dari field pertama melewati semua kontrol hingga tombol `[Submit]`, lalu tekan `Tab` sekali lagi
3. Verifikasi fokus berpindah melingkar di dalam modal dan tidak keluar ke halaman di belakangnya
4. Klik `[Submit]` tanpa mengisi apa pun
5. Verifikasi field wajib Client, Product, Plan, Duration, dan Start Date memiliki `aria-required="true"`
6. Verifikasi field yang error memiliki `aria-describedby` ke pesan error inline
7. Buka dropdown Client, lalu tekan `Esc`
8. Verifikasi `Esc` pertama hanya menutup dropdown Client dan modal tetap terbuka
9. Klik `[Clear Field]`, lalu tekan `Esc` pada form bersih
10. Verifikasi `Esc` kedua menutup modal tanpa dialog Unsaved Changes karena form bersih

### TC-AC-CS-622: Aksesibilitas form Activate Trial

11. Klik `[+ Activate Trial]`
12. Tekan `Tab` berulang dari field pertama melewati semua kontrol hingga tombol `[Submit]`, lalu tekan `Tab` sekali lagi
13. Verifikasi fokus berpindah melingkar di dalam modal dan tidak keluar ke halaman di belakangnya
14. Pilih Product `FAMS`, lalu klik `[Submit]` tanpa mengisi field lain
15. Verifikasi field wajib Client, Product, Plan, Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota memiliki `aria-required="true"`
16. Verifikasi field yang error memiliki `aria-describedby` ke pesan error inline
17. Buka dropdown Client, lalu tekan `Esc`
18. Verifikasi `Esc` pertama hanya menutup dropdown Client dan modal tetap terbuka
19. Tekan `Esc` pada form yang sudah berisi pilihan Product
20. Verifikasi `Esc` kedua memunculkan dialog Unsaved Changes karena form sudah berisi pilihan
21. Klik `[Leave]`

### TC-AC-CS-623: Aksesibilitas form Edit

22. Logout, lalu login sebagai Create-Only Distributor `Fajar Nugroho` (Pre-setup #6)
23. Buka menu Allocation > Client Subscription
24. Ketik Search `Apotek Sehat Sentosa+{runId}-045`, tekan Enter
25. Klik ikon `⋯` pada baris term Waiting for Approval, lalu pilih `Edit`
26. Tekan `Tab` berulang dari field pertama melewati semua kontrol hingga tombol `[Save]`, lalu tekan `Tab` sekali lagi
27. Verifikasi fokus berpindah melingkar di dalam modal dan tidak keluar ke halaman di belakangnya
28. Kosongkan Duration, lalu klik `[Save]`
29. Verifikasi field wajib Duration dan Start Date memiliki `aria-required="true"`
30. Verifikasi Duration yang error memiliki `aria-describedby` ke pesan error inline
31. Tekan `Esc` pada form yang sudah diubah
32. Verifikasi dialog Unsaved Changes muncul dan modal tetap terbuka sampai pilihan diambil
33. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): `[Clear Field]` agar form bersih sebelum `Esc` kedua (langkah 9; TC-AC-CS-568 Langkah 5 menyebut "form bersih"), `[Leave]` menutup form dirty (langkah 21, 33; S-08), dan Search untuk menemukan baris target (R-16; langkah 24).
- Ganti akun eksplisit di langkah 22 (S-07), diikuti `Buka menu Allocation > Client Subscription` (langkah 23).
- Temuan untuk QA:
  - TC-AC-CS-568 Langkah 3 mengklik `[Submit]` pada form kosong lalu mengecek atribut; urutan pengecekan atribut `aria-required` sebelum atau sesudah Submit tidak dinyatakan, spec memeriksanya setelah Submit.
  - TC-AC-CS-622 Langkah 5 menyebut "form yang sudah berisi pilihan Product"; spec mempertahankan pilihan Product dari langkah 14.
  - TC-AC-CS-623 Expected c tidak menyatakan pilihan dialog; spec memilih `[Leave]` agar deterministik.
