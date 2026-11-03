---
id: TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes
title: "Form Add: Clear Field dan Unsaved Changes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-164
  - TC-AC-CS-162
  - TC-AC-CS-166
  - TC-AC-CS-561
  - TC-AC-CS-165
coverage:
  web: automated
---

# Form Add: Clear Field dan Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-042` (padanan Pre-setup #48: tanpa term dan tanpa trial). Tidak ada Submit sukses pada spec ini.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah term Client seed lewat fixture BE.

## Test Steps

### TC-AC-CS-164: Menutup form bersih tidak memunculkan dialog Unsaved Changes

1. Klik `[+ Subscription]`
2. Klik `[✕]` pada header modal
3. Verifikasi modal tertutup langsung
4. Verifikasi dialog Unsaved Changes tidak muncul
5. Klik `[+ Subscription]`
6. Tekan `Esc`
7. Verifikasi modal tertutup langsung
8. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-CS-162: Clear Field pada Add mengosongkan semua field dan mempertahankan checkbox Stay

9. Klik `[+ Subscription]`
10. Centang "Stay on this form after submitting"
11. Isi Client `Client Tanpa Subscription+{runId}-042`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
12. Kosongkan Duration, lalu klik `[Submit]` sehingga error inline tampil
13. Klik `[Clear Field]`
14. Verifikasi semua field kembali kosong atau default (Duration `1`, Start Date default hari ini)
15. Verifikasi error inline yang ada hilang
16. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
17. Verifikasi modal tetap terbuka
18. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-CS-166: Pilihan Cancel pada dialog Unsaved Changes mempertahankan form

19. Pilih Client `Client Tanpa Subscription+{runId}-042` dan Product `SAMS`
20. Tekan `Esc`
21. Klik `[Cancel]` pada dialog Unsaved Changes
22. Verifikasi dialog tertutup dan modal tetap terbuka
23. Verifikasi nilai Client `Client Tanpa Subscription+{runId}-042` dan Product `SAMS` dipertahankan

### TC-AC-CS-561: Esc pada dialog Unsaved Changes setara Cancel dan form tetap terbuka

24. Tekan `Esc` sehingga dialog Unsaved Changes muncul
25. Tekan `Esc` lagi pada dialog
26. Verifikasi dialog Unsaved Changes tertutup dan modal Add Subscription tetap terbuka (setara tombol `[Cancel]`)
27. Verifikasi nilai Client `Client Tanpa Subscription+{runId}-042` dipertahankan
28. Verifikasi tidak ada term dibuat (jumlah term Client tetap 0, dibaca lewat fixture BE)

### TC-AC-CS-165: Menutup form yang terisi memunculkan dialog Unsaved Changes dan pilihan Leave menutup form

29. Klik `[✕]` pada header modal
30. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` muncul
31. Klik `[Leave]`
32. Verifikasi dialog dan modal tertutup tanpa menyimpan

## Notes

- Urutan TC-AC-CS-166 dan 561 melanjutkan modal TC-AC-CS-162 (satu pembukaan form untuk kasus tanpa submit) dan TC-AC-CS-165 yang menutup form dirty berada di akhir (S-08, S-10). TC-AC-CS-166 melanjutkan TC-AC-CS-165 menurut Dependensi TC; langkah dependensi (mengisi Client lalu `[✕]`) diwakili oleh langkah 19 dan 29 pada modal yang sama.
- Langkah penghubung (S-03): langkah 12 membuat error inline sebelum `[Clear Field]` agar Expected b TC-AC-CS-162 bermakna (TC tidak menyebut error awal).
- Temuan untuk QA:
  - TC-AC-CS-162 Expected b ("Error inline yang ada hilang") tidak punya langkah pembangkit error di TC; langkah 12 menambahkannya.
  - TC-AC-CS-561 Langkah 3 hanya menyebut dialog muncul tanpa Expected; kemunculan dialog tidak diasersi terpisah di langkah 24 dan hanya hasil Esc kedua yang diasersi.
