---
id: TC-GS-NLU-E2E-043-edit-validasi-required-dan-clear-field
title: "Edit: validasi required dan Clear Field"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-141
  - TC-GS-NLU-142
  - TC-GS-NLU-143
  - TC-GS-NLU-144
coverage:
  web: automated
---

# Edit: validasi required dan Clear Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json` sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations, Logistics), dan pool Login User Represented By (Ahmad Fauzi).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): satu Non-Login User target Edit Target 01 dengan First Name `Edit Target 01`, Last Name `{runId}-043`, Email `edittarget01+{runId}-043@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active. Seluruh TC memakai satu target dan satu pembukaan Popup Edit karena tidak ada Save yang berhasil (kasus tanpa submit sukses, konvensi bagian 3).
- Kemampuan teknis: jumlah total record tabel List Non-Login User dibaca sebagai baseline sebelum aksi pertama; kemampuan baca disediakan tim FE/BE.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah total record tabel List Non-Login User sebagai baseline
2. Ketik Search `Edit Target 01 {runId}-043`, tekan Enter
3. Klik `⋯` pada baris `Edit Target 01 {runId}-043` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-141: Clear Field pada Popup Edit mengosongkan seluruh field bukan mengembalikan nilai tersimpan

4. Klik `[Clear Field]`
5. Verifikasi seluruh field kosong (bukan kembali ke nilai tersimpan)
6. Verifikasi Represented By kembali ke `[+ Select User]`
7. Verifikasi Popup Edit tetap terbuka
8. Verifikasi tidak ada dialog konfirmasi

### TC-GS-NLU-142: Validasi required First Name, Last Name, dan Email kosong pada Popup Edit

9. Pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
10. Klik `[Save]`
11. Verifikasi pesan inline First Name `First name must not be empty`
12. Verifikasi pesan inline Last Name `Last name must not be empty`
13. Verifikasi pesan inline Email `Email must not be empty`
14. Verifikasi Popup Edit tetap terbuka
15. Verifikasi tidak ada toast
16. Verifikasi jumlah total record tabel sama dengan baseline langkah 1

### TC-GS-NLU-143: Validasi required Division kosong pada Popup Edit

17. Klik `[Clear Field]`
18. Isi First Name `Fikri`, Last Name `Ramadhan`, Email `fikriramadhan+{runId}-043@qwertysystem.net`
19. Pilih Represented By `Ahmad Fauzi` tanpa memilih Division
20. Klik `[Save]`
21. Verifikasi pesan inline di bawah Division `Division must not be empty`
22. Verifikasi Popup Edit tetap terbuka
23. Verifikasi jumlah total record tabel sama dengan baseline langkah 1

### TC-GS-NLU-144: Validasi required Represented By belum dipilih pada Popup Edit

24. Klik `[Clear Field]`
25. Isi First Name `Fikri`, Last Name `Ramadhan`, Email `fikriramadhan+{runId}-043@qwertysystem.net`
26. Pilih Division `Logistics` tanpa memilih Represented By
27. Klik `[Save]`
28. Verifikasi pesan inline di bawah Represented By `Represented by must not be empty`
29. Verifikasi Popup Edit tetap terbuka
30. Verifikasi jumlah total record tabel sama dengan baseline langkah 1
31. Klik `✕` pada Popup Edit Non-Login User
32. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
33. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (baseline jumlah record), langkah 2 (Search Name bersuffix untuk menemukan baris target (Email bukan kolom Search), R-16), langkah 17 dan 24 (`[Clear Field]` sebagai pembersih antar TC pada form yang sama, R-12), dan langkah 31 sampai 33 (menutup popup yang dirty secara deterministik, S-08).
- Email valid `fikriramadhan+{runId}-043@qwertysystem.net` memakai suffix per run (S-12); TC menulis `fikriramadhan@qwertysystem.net`.
- Temuan untuk QA:
  - TC-GS-NLU-141 sampai TC-GS-NLU-144 memakai target berbeda (Budi Kurniawan, Edit Target 01, 02, 03). Karena tidak ada Save yang berhasil, spec memakai satu target dan satu pembukaan popup; TC-GS-NLU-142 yang mengawali dengan `[Clear Field]` melanjutkan dari keadaan kosong TC-GS-NLU-141.
  - Expected "tidak ada record dibuat/diubah" (TC-GS-NLU-142 sampai TC-GS-NLU-144) tidak menyebut cara mengamati perubahan; spec memakai jumlah total record dan popup yang tetap terbuka tanpa toast sebagai pengamatan.
