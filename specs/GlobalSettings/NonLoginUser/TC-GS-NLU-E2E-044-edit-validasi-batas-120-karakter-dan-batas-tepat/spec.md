---
id: TC-GS-NLU-E2E-044-edit-validasi-batas-120-karakter-dan-batas-tepat
title: "Edit: validasi batas 120 karakter dan batas tepat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-145
  - TC-GS-NLU-146
coverage:
  web: automated
---

# Edit: validasi batas 120 karakter dan batas tepat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json` sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations, Logistics), dan pool Login User Represented By (Ahmad Fauzi).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Non-Login User Edit Target 04 (TC-GS-NLU-145) dan Edit Target 05 (TC-GS-NLU-146), masing-masing First Name `Edit Target 0N`, Last Name `{runId}-044`, Email `edittarget0N+{runId}-044@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active.
- Data uji: First Name, Last Name, dan Employee ID dengan panjang tepat 121 atau 120 karakter, serta Email `a` x 112 + `@test.com` (121 karakter, tidak tersimpan). Data Dinamis TC-GS-NLU-146 (record tersimpan): First Name 120 karakter `a`, Last Name 120 karakter `b`; Employee ID 120 karakter `e` dan Email 120 karakter yang keduanya dihitung termasuk suffix per run: Employee ID = `e` × (120 − panjang `-{runId}-044`) + `-{runId}-044`; Email = `f` × n + `+{runId}-044@test.com` dengan total tepat 120 karakter. First Name dan Last Name tidak butuh suffix (tidak unik). Record Edit Target 05 yang menyimpannya dihapus hook `after` lewat API (ber-Email `+{runId}-044`).
- Kemampuan teknis: panjang karakter diketik lewat fixture string; tidak ada kemampuan tambahan.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target 04 {runId}-044`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 04 {runId}-044` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-145: Validasi batas 120 karakter First Name, Last Name, Employee ID, dan Email pada Popup Edit

3. Isi First Name dengan 121 karakter `a`
4. Verifikasi pesan inline First Name `Max. 120 characters` muncul langsung
5. Isi Last Name dengan 121 karakter `a`
6. Verifikasi pesan inline Last Name `Max. 120 characters` muncul langsung
7. Isi Employee ID dengan 121 karakter `a`
8. Verifikasi pesan inline Employee ID `Max. 120 characters` muncul langsung
9. Isi Email dengan 121 karakter (`a` x 112 + `@test.com`)
10. Verifikasi pesan inline Email `Max. 120 characters` muncul langsung
11. Klik `[Save]`
12. Verifikasi Popup Edit tetap terbuka
13. Verifikasi tidak ada toast sukses
14. Verifikasi keempat pesan `Max. 120 characters` tetap tampil
15. Klik `✕` pada Popup Edit Non-Login User
16. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
17. Klik `[Leave]`
18. Verifikasi baris Edit Target 04 di tabel tetap menampilkan Name `Edit Target 04 {runId}-044` (nilai tersimpan tidak berubah)

### TC-GS-NLU-146: Batas tepat 120 karakter First Name, Last Name, Employee ID, dan Email diterima pada Popup Edit

19. Ganti isi kotak search dengan `Edit Target 05 {runId}-044`, tekan Enter
20. Klik `⋯` pada baris `Edit Target 05 {runId}-044` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
21. Isi First Name dengan 120 karakter `a`
22. Isi Last Name dengan 120 karakter `b`
23. Isi Employee ID dengan 120 karakter (`e` × (120 − panjang `-{runId}-044`) + `-{runId}-044`)
24. Isi Email dengan 120 karakter valid (`f` × n + `+{runId}-044@test.com`, total tepat 120)
25. Klik `[Save]`
26. Verifikasi tidak ada pesan `Max. 120 characters` pada keempat field
27. Verifikasi toast sukses `Success, non-login user has been updated.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan (validasi diblokir sebelum aksi sukses).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 dan 19 (Search Name bersuffix untuk menemukan baris target (Email bukan kolom Search), R-16); langkah 15 sampai 17 (menutup popup yang dirty secara deterministik, S-08).
- Target seed sudah memiliki Division dan Represented By terisi sehingga langkah 6 TC-GS-NLU-146 ("isi `Logistics` dan `Ahmad Fauzi` bila kosong") tidak ditulis sebagai langkah bersyarat.
- Temuan untuk QA:
  - TC-GS-NLU-145 Expected butir e ("nilai tersimpan Edit Target 04 tidak berubah") tidak menyebut cara mengamatinya; spec memakai Name baris di tabel setelah popup ditutup.
  - TC-GS-NLU-146 membuat Employee ID tepat 120 karakter; literal ID dirangkai ulang hingga 120 karakter termasuk suffix `-{runId}-044` (S-12) sehingga panjang batas tetap tepat 120.
  - TC-GS-NLU-146 Expected butir b ("Data tersimpan (toast sukses ...)") tidak meminta pembacaan ulang nilai tersimpan; spec hanya mengasersi toast.
