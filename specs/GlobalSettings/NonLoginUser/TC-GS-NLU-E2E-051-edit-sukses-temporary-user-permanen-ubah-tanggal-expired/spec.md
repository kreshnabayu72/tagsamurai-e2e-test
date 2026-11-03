---
id: TC-GS-NLU-E2E-051-edit-sukses-temporary-user-permanen-ubah-tanggal-expired
title: "Edit sukses: Temporary User permanen, ubah tanggal, expired"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-175
  - TC-GS-NLU-176
  - TC-GS-NLU-177
  - TC-GS-NLU-178
  - TC-GS-NLU-179
coverage:
  web: automated
---

# Edit sukses: Temporary User permanen, ubah tanggal, expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations), dan pool Login User Represented By (Ahmad Fauzi).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan, termasuk Temporary Until pada tanggal lampau, disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Non-Login User Edit Target 43 (bukan Temporary), Edit Target 44 (Temporary aktif, Temporary Until +5 hari), Edit Target 45 (Temporary aktif), `Agus Salim {runId}-051` (Contractor, Operations, Temporary-expired, Inactive; TC-GS-NLU-178), dan Edit Target 46 (Temporary-expired, Inactive). Setiap target: First Name `Edit Target NN` (atau `Agus Salim`), Last Name `{runId}-051`, Email `edittargetNN+{runId}-051@qwertysystem.net` (atau `agussalim+{runId}-051@qwertysystem.net`), Division `Operations`, Represented By `Ahmad Fauzi`. TC-GS-NLU-178 memakai `Agus Salim {runId}-051` milik spec, bukan Agus Salim Pre-setup, karena Save menulis Temporary Until (S-06).
- Data uji: Temporary Until +10 hari (TC-GS-NLU-175), +20 hari (TC-GS-NLU-176), dan besok (TC-GS-NLU-178), dihitung dari tanggal hari ini pada jam browser dan jam server yang sinkron; First Name `Edit46` (TC-GS-NLU-179).
- State global: tidak ada yang diubah. Visibilitas kolom Temporary User dan Temporary Until diatur lewat overlay Column Visibility tanpa menyimpan lewat Setup Column dan dipulihkan dengan langkah eksplisit.

## Test Steps

1. Ketik Search `Edit Target 43 {runId}-051`, tekan Enter
2. Klik `⋯` pada baris Edit Target 43 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-175: Edit mengatur Temporary User pada user permanen

3. Centang `Set as Temporary User`
4. Pilih Temporary Until +10 hari
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, non-login user has been updated.`
7. Buka Detail record tersebut
8. Verifikasi Detail menampilkan `Temporary until [tanggal +10 hari]` di bawah Represented By
9. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-176: Edit Temporary Until ke tanggal lain pada Temporary User aktif

10. Ketik Search `Edit Target 44 {runId}-051`, tekan Enter
11. Klik `⋯` pada baris Edit Target 44 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
12. Ubah Temporary Until menjadi +20 hari
13. Klik `[Save]`
14. Verifikasi toast sukses `Success, non-login user has been updated.`
15. Buka Detail record tersebut
16. Verifikasi Detail menampilkan `Temporary until [tanggal +20 hari]`
17. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-177: Menghapus centang Temporary User mengosongkan Temporary Until dan menjadikan user permanen

18. Ganti isi kotak search dengan `Edit Target 45 {runId}-051`, tekan Enter
19. Klik `⋯` pada baris Edit Target 45 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
20. Hapus centang `Set as Temporary User`
21. Klik `[Save]`
22. Verifikasi toast sukses `Success, non-login user has been updated.`
23. Buka Detail record tersebut
24. Verifikasi Detail tidak menampilkan baris `Temporary until`
25. Kembali ke daftar Non-Login User lewat breadcrumb
26. Klik ikon `⋯` pada header kolom tabel dan centang kolom Temporary User dan Temporary Until pada overlay Column Visibility
27. Verifikasi kolom Temporary User baris Edit Target 45 menampilkan `No`
28. Verifikasi kolom Temporary Until baris Edit Target 45 menampilkan `—`
29. Klik ikon `⋯` pada header kolom tabel dan hapus centang kolom Temporary User dan Temporary Until

### TC-GS-NLU-178: Edit Temporary Until pada Temporary User yang sudah expired tidak mengaktifkan user

30. Ganti isi kotak search dengan `Agus Salim {runId}-051`, tekan Enter
31. Klik `⋯` pada baris Agus Salim > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
32. Ubah Temporary Until menjadi besok
33. Klik `[Save]`
34. Verifikasi toast sukses `Success, non-login user has been updated.`
35. Verifikasi switch Active baris Agus Salim tetap OFF (user tetap Inactive sampai di-toggle ON)

### TC-GS-NLU-179: Edit nama pada Temporary-expired dengan Temporary Until pre-filled lampau tetap lolos

36. Ganti isi kotak search dengan `Edit Target 46 {runId}-051`, tekan Enter
37. Klik `⋯` pada baris Edit Target 46 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
38. Ubah First Name menjadi `Edit46`
39. Klik `[Save]`
40. Verifikasi toast sukses `Success, non-login user has been updated.`
41. Verifikasi tidak ada pesan error `Please select a future date.`
42. Ganti isi kotak search dengan `Edit46 {runId}-051`, tekan Enter
43. Verifikasi user `Edit46 {runId}-051` tetap Inactive

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Spec ini melewati sekitar 35 langkah (nominal 43). Alasan: kelima TC adalah Edit sukses yang berdiri sendiri dengan target milik spec masing-masing (Edit Target 43, 44, 45, `Agus Salim`, 46), sehingga hasil satu blok tidak dipakai blok lain dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 10, 18, 30, dan 36 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List); langkah 42 (Search Name baru `Edit46 {runId}-051` sesudah rename, karena Search lama `Edit Target 46 {runId}-051` tidak lagi cocok dengan Name baris; S-14, R-16); langkah 9, 17, dan 25 (kembali ke daftar setelah Detail); langkah 26 dan 29 (mengaktifkan dan memulihkan kolom curated Temporary User dan Temporary Until untuk Expected TC-GS-NLU-177 butir b).
- Absence pada Detail (TC-GS-NLU-177) memakai toast sukses server sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-NLU-177 Expected butir b memuat "bila diaktifkan"; spec mengaktifkan kolom lewat overlay Column Visibility supaya klausa itu teramati.
  - TC-GS-NLU-178 menyebut record Agus Salim dari Pre-setup, tetapi Save menulis Temporary Until; spec memakai data milik spec `Agus Salim {runId}-051`.
  - TC-GS-NLU-179 langkah 3 ("Biarkan Temporary Until pre-filled apa adanya") tidak diperlakukan sebagai langkah terpisah karena tidak ada aksi.
