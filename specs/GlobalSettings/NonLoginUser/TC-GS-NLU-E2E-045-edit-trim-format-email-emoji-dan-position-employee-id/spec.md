---
id: TC-GS-NLU-E2E-045-edit-trim-format-email-emoji-dan-position-employee-id
title: "Edit: trim, format Email, emoji, dan Position Employee ID opsional"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-147
  - TC-GS-NLU-148
  - TC-GS-NLU-154
  - TC-GS-NLU-156
coverage:
  web: automated
---

# Edit: trim, format Email, emoji, dan Position Employee ID opsional

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json` sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations, Logistics), dan pool Login User Represented By (Ahmad Fauzi).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Non-Login User Edit Target 06 (TC-GS-NLU-147), Edit Target 07 (TC-GS-NLU-148 dan TC-GS-NLU-154), dan Edit Target 15 (TC-GS-NLU-156, dengan Position dan Employee ID terisi). Setiap target: First Name `Edit Target NN`, Last Name `{runId}-045`, Email `edittargetNN+{runId}-045@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active.
- Data uji: First Name `  Joko  `, Last Name `  Lestari {runId}-045  `, Employee ID `  NL-7002-{runId}-045  `, Email `  jokolestari2+{runId}-045@qwertysystem.net  ` (TC-GS-NLU-147); Email `fikri.at.qwertysystem.net` (TC-GS-NLU-148); `Budi😊` dan `Santoso🔥` (TC-GS-NLU-154); First Name `Lia`, Last Name `Amelia {runId}-045`, Email `liaamelia2+{runId}-045@qwertysystem.net` (TC-GS-NLU-156).
- Kemampuan teknis: mengetik dan menempel emoji pada input (TC-GS-NLU-154).
- Kemampuan teknis: jumlah total record tabel List Non-Login User dibaca sebagai baseline sebelum aksi pertama; kemampuan baca disediakan tim FE/BE.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah total record tabel List Non-Login User sebagai baseline
2. Ketik Search `Edit Target 07 {runId}-045`, tekan Enter
3. Klik `⋯` pada baris `Edit Target 07 {runId}-045` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-148: Validasi format Email tidak valid pada Popup Edit

4. Isi Email `fikri.at.qwertysystem.net`
5. Klik `[Save]`
6. Verifikasi pesan inline di bawah Email `Invalid email format`
7. Verifikasi Popup Edit tetap terbuka
8. Verifikasi jumlah total record tabel sama dengan baseline langkah 1

### TC-GS-NLU-154: Karakter emoji diblok saat mengetik dan menempel di First Name dan Last Name pada Popup Edit

9. Ganti isi First Name dengan mengetik `Budi😊`
10. Ganti isi Last Name dengan menempel `Santoso🔥`
11. Verifikasi First Name hanya berisi `Budi` tanpa pesan error
12. Verifikasi Last Name hanya berisi `Santoso`
13. Klik `✕` pada Popup Edit Non-Login User
14. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
15. Klik `[Leave]`

### TC-GS-NLU-147: Spasi awal dan akhir di-trim saat Save pada Popup Edit

16. Ganti isi kotak search dengan `Edit Target 06 {runId}-045`, tekan Enter
17. Klik `⋯` pada baris `Edit Target 06 {runId}-045` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
18. Isi First Name `  Joko  `, Last Name `  Lestari {runId}-045  `, Employee ID `  NL-7002-{runId}-045  `, Email `  jokolestari2+{runId}-045@qwertysystem.net  `
19. Klik `[Save]`
20. Verifikasi toast sukses `Success, non-login user has been updated.`
21. Ganti isi kotak search dengan `Joko Lestari {runId}-045`, tekan Enter
22. Buka Detail record tersebut
23. Verifikasi Detail menampilkan Name `Joko Lestari {runId}-045` tanpa spasi tepi
24. Verifikasi Detail menampilkan Employee ID `NL-7002-{runId}-045` tanpa spasi tepi
25. Verifikasi Detail menampilkan Email `jokolestari2+{runId}-045@qwertysystem.net` tanpa spasi tepi
26. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-156: Position dan Employee ID boleh dikosongkan pada Popup Edit

27. Ketik Search `Edit Target 15 {runId}-045`, tekan Enter
28. Klik `⋯` pada baris `Edit Target 15 {runId}-045` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
29. Klik `[Clear Field]`
30. Isi First Name `Lia`, Last Name `Amelia {runId}-045`, Email `liaamelia2+{runId}-045@qwertysystem.net`, pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
31. Klik `[Save]`
32. Verifikasi toast sukses `Success, non-login user has been updated.`
33. Verifikasi tidak ada pesan error
34. Ganti isi kotak search dengan `Lia Amelia {runId}-045`, tekan Enter
35. Verifikasi sel Position dan Employee ID baris `Lia Amelia {runId}-045` menampilkan `—`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-GS-NLU-148 dan TC-GS-NLU-154 (validasi diblokir, satu pembukaan popup) lebih dulu, lalu TC-GS-NLU-147 dan TC-GS-NLU-156 (aksi sukses), sesuai S-10.
- Langkah penghubung tanpa `Verifikasi`: langkah 1; langkah 2, 16, dan 27 (Search Name bersuffix untuk menemukan baris target (Email bukan kolom Search), R-16); langkah 21 dan 34 (Search Name baru bersuffix sesudah rename, karena Search lama `Edit Target NN {runId}-045` tidak lagi cocok dengan Name baris yang diubah; S-14, R-16); langkah 13, 14, dan 15 (menutup popup yang dirty secara deterministik, S-08); langkah 26 (kembali ke daftar setelah Detail).
- Email pada TC-GS-NLU-147 dan TC-GS-NLU-156 memakai suffix per run (S-12); Employee ID `NL-7002-{runId}-045` memakai suffix per run (S-12); TC menulis `NL-7002`.
- Last Name TC-GS-NLU-147 (`Lestari`) dan TC-GS-NLU-156 (`Amelia`) diberi suffix ` {runId}-045` (tersimpan `Lestari {runId}-045` dan `Amelia {runId}-045`; First Name tetap sesuai TC) agar kunci Search unik dan tidak bentrok dengan baris spec lain (mis. `Lia Amelia` juga dipakai spec 017); Name baris menjadi `Joko Lestari {runId}-045` dan `Lia Amelia {runId}-045`. Deviasi dari nilai TC; trim Last Name tetap teramati lewat spasi tepi.
- Target seed sudah memiliki Division dan Represented By terisi sehingga langkah "lengkapi field wajib lain" pada TC-GS-NLU-148 tidak ditulis sebagai langkah tambahan.
- Temuan untuk QA:
  - TC-GS-NLU-148 Expected butir b ("tidak ada record dibuat/diubah") tidak menyebut cara mengamati; spec memakai jumlah total record dan popup yang tetap terbuka.
  - TC-GS-NLU-147 Expected butir a ("Tersimpan sukses") tidak menyebut teks toast; spec mengasersi toast `Success, non-login user has been updated.` seperti TC edit sukses lainnya.
  - TC-GS-NLU-154 tidak menyebut apakah First Name dan Last Name dikosongkan sebelum mengetik; spec mengganti isi field.
