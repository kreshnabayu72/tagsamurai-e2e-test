---
id: TC-GS-NLU-E2E-048-edit-validasi-temporary-user-dan-temporary-until
title: "Edit: validasi Temporary User dan Temporary Until"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-157
  - TC-GS-NLU-158
  - TC-GS-NLU-159
  - TC-GS-NLU-169
coverage:
  web: automated
---

# Edit: validasi Temporary User dan Temporary Until

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations), dan pool Login User Represented By (Ahmad Fauzi).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): satu Non-Login User target Edit Target 16 dengan First Name `Edit Target 16`, Last Name `{runId}-048`, Email `edittarget16+{runId}-048@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active, bukan Temporary User. TC-GS-NLU-157, TC-GS-NLU-158, TC-GS-NLU-169, dan TC-GS-NLU-159 memakai target dan satu pembukaan Popup Edit yang sama (Edit Target 16, 17, 28, dan 18 pada TC); Save yang berhasil hanya pada TC-GS-NLU-159.
- Data uji: Temporary Until besok (dihitung dari tanggal hari ini pada jam browser dan jam server yang sinkron); nilai tanggal hari ini diinjeksi langsung ke state date picker (TC-GS-NLU-169).
- Kemampuan teknis: jumlah total record tabel List Non-Login User dibaca sebagai baseline sebelum aksi pertama; kemampuan baca disediakan tim FE/BE. Injeksi nilai tanggal hari ini ke state date picker (melewati penonaktifan tanggal di UI) disediakan tim FE; TC tidak menyebut mekanismenya.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah total record tabel List Non-Login User sebagai baseline
2. Ketik Search `Edit Target 16 {runId}-048`, tekan Enter
3. Klik `⋯` pada baris Edit Target 16 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-157: Checkbox Set as Temporary User menampilkan dan menyembunyikan Temporary Until pada Popup Edit

4. Centang `Set as Temporary User`
5. Verifikasi muncul date picker `Temporary Until` dengan placeholder `Select date`
6. Pilih Temporary Until besok
7. Hapus centang `Set as Temporary User`
8. Verifikasi field `Temporary Until` hilang
9. Centang kembali `Set as Temporary User`
10. Verifikasi nilai `Temporary Until` dikosongkan dengan placeholder `Select date`

### TC-GS-NLU-158: Temporary User tercentang tanpa Temporary Until ditolak pada Popup Edit

11. Klik `[Save]`
12. Verifikasi pesan inline di bawah Temporary Until `Temporary until must not be empty`
13. Verifikasi Popup Edit tetap terbuka
14. Verifikasi jumlah total record tabel sama dengan baseline langkah 1

### TC-GS-NLU-169: Server menolak Temporary Until hari ini yang lolos date picker pada Popup Edit

15. Injeksi nilai tanggal hari ini langsung ke state date picker `Temporary Until` (melewati penonaktifan tanggal di UI)
16. Klik `[Save]`
17. Verifikasi pesan inline di bawah Temporary Until `Please select a future date.`
18. Verifikasi Popup Edit tetap terbuka
19. Verifikasi jumlah total record tabel sama dengan baseline langkah 1

### TC-GS-NLU-159: Date picker Temporary Until menonaktifkan hari ini dan tanggal lampau serta menerima besok pada Popup Edit

20. Buka date picker `Temporary Until`
21. Verifikasi tanggal kemarin dan hari ini disabled (tidak dapat dipilih)
22. Pilih tanggal besok
23. Klik `[Save]`
24. Verifikasi toast sukses `Success, non-login user has been updated.`
25. Buka Detail record tersebut
26. Verifikasi Detail menampilkan `Temporary until [tanggal besok]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-GS-NLU-157, TC-GS-NLU-158, dan TC-GS-NLU-169 (tanpa Save yang berhasil) lebih dulu dalam satu popup, lalu TC-GS-NLU-159 (aksi sukses), sesuai S-10.
- Langkah penghubung tanpa `Verifikasi`: langkah 1; langkah 2 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List); langkah 6, 7, dan 9 (mengisi Temporary Until lalu mencentang kembali supaya nilai yang dikosongkan dapat diamati, S-14).
- P-5: TC-GS-NLU-169 menyuntikkan nilai tanggal hari ini ke state date picker (manipulasi sisi klien kelas a); satu TC objek-uji ringan yang berada di spec fungsional Popup Edit yang sama permukaannya.
- Temuan untuk QA:
  - TC-GS-NLU-157 Expected butir b ("nilainya dikosongkan") tidak menyebut cara mengamati nilai yang dikosongkan; spec mengisi tanggal besok, menghapus centang, lalu mencentang kembali dan mengasersi field kosong.
  - TC-GS-NLU-157 sampai TC-GS-NLU-159 dan TC-GS-NLU-169 memakai target berbeda (Edit Target 16, 17, 18, 28); spec memakai satu target dan satu pembukaan popup, dengan TC-GS-NLU-158 mengikuti keadaan Temporary User tercentang dan Temporary Until kosong dari TC-GS-NLU-157.
  - TC-GS-NLU-169 langkah 3 menyebut "injeksi nilai tanggal hari ini langsung ke state date picker" tanpa mekanisme; tidak ada mekanisme di TC, PRD, atau LLD.
