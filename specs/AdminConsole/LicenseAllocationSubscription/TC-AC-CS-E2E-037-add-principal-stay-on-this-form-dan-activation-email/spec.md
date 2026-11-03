---
id: TC-AC-CS-E2E-037-add-principal-stay-on-this-form-dan-activation-email
title: "Add: Principal, SIEM, dan Checkbox Stay on this Form"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-160
  - TC-AC-CS-161
  - TC-AC-CS-145
  - TC-AC-CS-154
coverage:
  web: automated
---

# Add: Principal, SIEM, dan Checkbox Stay on this Form

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta term yang dibuat spec): Client `Client Tanpa Subscription A+{runId}-037` untuk TC-AC-CS-160, `Client Tanpa Subscription B+{runId}-037` untuk TC-AC-CS-161, dan `Client Tanpa Subscription C+{runId}-037` untuk TC-AC-CS-145 (padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term dan tanpa trial); Client `PT Sejahtera+{runId}-037` (padanan Pre-setup #38: binaan Principal dan PT Maju Bersama, tanpa term SIEM) untuk TC-AC-CS-154.
- Kemampuan teknis (disediakan tim FE/BE): membaca saldo `Main Pocket` PT Maju Bersama (Pre-setup #20) lewat fixture BE untuk baseline TC-AC-CS-145.

## Test Steps

### TC-AC-CS-160: Checkbox Stay on this form pada varian Add tercentang mereset form setelah Submit sukses

1. Klik `[+ Subscription]`
2. Centang "Stay on this form after submitting"
3. Pilih Client `Client Tanpa Subscription A+{runId}-037`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, subscription has been added." muncul
6. Verifikasi modal tetap terbuka dan semua field kembali bersih
7. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang

### TC-AC-CS-161: Tanpa Stay on this form modal tertutup setelah Submit sukses

8. Hilangkan centang "Stay on this form after submitting"
9. Pilih Client `Client Tanpa Subscription B+{runId}-037`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
10. Klik `[Submit]`
11. Verifikasi modal tertutup
12. Verifikasi toast sukses "Success, subscription has been added." muncul
13. Ketik Search `Client Tanpa Subscription B+{runId}-037`, tekan Enter
14. Verifikasi List menampilkan baris baru
15. Klik `(←)` pada kotak Search

### TC-AC-CS-145: Add mode New oleh Total Control Principal langsung Active tanpa Wallet

16. Baca saldo `Main Pocket` PT Maju Bersama lewat fixture BE sebagai baseline
17. Klik `[+ Subscription]`
18. Pilih Client `Client Tanpa Subscription C+{runId}-037`, Product `SIEM`, Plan `SIEM`, Duration `1`, Start Date `19/08/26`
19. Klik `[Submit]`
20. Verifikasi toast sukses "Success, subscription has been added." muncul
21. Ketik Search `Client Tanpa Subscription C+{runId}-037`, tekan Enter
22. Verifikasi baris baru berstatus Active
23. Verifikasi Plan Owner `PT ABC (Principal)`
24. Verifikasi saldo `Main Pocket` sama dengan baseline, tanpa Reserve maupun Capture (Principal tidak punya Wallet)
25. Klik `(←)` pada kotak Search

### TC-AC-CS-154: Add mode New untuk Product SIEM

26. Klik `[+ Subscription]`
27. Pilih Client `PT Sejahtera+{runId}-037`, Product `SIEM`, Plan `SIEM`, Duration `1`, Start Date `19/08/26`
28. Klik `[Submit]`
29. Verifikasi toast sukses "Success, subscription has been added." muncul
30. Ketik Search `PT Sejahtera+{runId}-037`, tekan Enter
31. Verifikasi baris SIEM berstatus Active tampil di tab `Current`
32. Buka Subscription Detail baris SIEM dengan klik baris
33. Verifikasi License Quota Detail memuat baris tetap Concurrent User dan Log Source

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular; urutan TC-AC-CS-160 sebelum TC-AC-CS-161 mengikuti state checkbox Stay.
- Langkah penghubung (S-03): menghilangkan centang Stay (langkah 8), baseline saldo (langkah 16), Search untuk menemukan baris target (R-16; langkah 13, 21, 30), dan `(←)` pada kotak Search (langkah 15, 25).
- TC-AC-CS-156 (Activation Email dan App Access hanya pada term pertama) ada di spec 148.
- Temuan untuk QA:
  - TC-AC-CS-154 Expected b tidak menyebut kolom License Quota Detail selain nama baris "Concurrent User" dan "Log Source"; spec mengasersi keberadaan keduanya.
  - TC-AC-CS-145 Expected c "tidak ada Reserve maupun Capture karena Principal tidak punya Wallet" tidak menyebut cara cek; spec memakai saldo Wallet entitas Plan Owner lewat fixture BE.
