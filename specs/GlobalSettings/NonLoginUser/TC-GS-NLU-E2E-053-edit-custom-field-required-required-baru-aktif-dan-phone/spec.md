---
id: TC-GS-NLU-E2E-053-edit-custom-field-required-required-baru-aktif-dan-phone
title: "Edit: Custom Field Required, Required baru aktif, dan Phone"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-181
  - TC-GS-NLU-458
  - TC-GS-NLU-466
  - TC-GS-NLU-505
coverage:
  web: automated
---

# Edit: Custom Field Required, Required baru aktif, dan Phone

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations), pool Login User Represented By (Ahmad Fauzi), dan Custom Field dasar Blood Type (Dropdown A/B/O/AB) dan Emergency Phone (Phone, tidak Required), keduanya Active.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Custom Field uji `Badge Required` (Text; dibuat dan diaktifkan hook `before` lalu dihapus atau dinonaktifkan hook `after`). Urutan hook `before`: record dibuat saat Badge Required belum Required, yaitu Edit Target 54 (Badge Required `Kartu B`; TC-GS-NLU-458) dan Edit Target 55 (Badge Required kosong; TC-GS-NLU-466); sesudahnya hook mengubah Badge Required menjadi Required (Global Settings > Custom Field User > Edit > Required Field `On`). Hook `after` mengembalikan Badge Required menjadi non-Required (Post Condition TC-GS-NLU-458 dan TC-GS-NLU-466). Non-Login User Edit Target 48 (TC-GS-NLU-181; Blood Type `O`) dan `Gilang Pratama {runId}-053` (TC-GS-NLU-505; Emergency Phone Country Code `+62`, Number `81234567890`, nilai Pre-setup TC-GS-NLU-94 yang di-seed sebagai data milik spec). Setiap target: First Name `Edit Target NN` (atau `Gilang`), Last Name `{runId}-053` (atau `Pratama {runId}-053`), Email `edittargetNN+{runId}-053@qwertysystem.net` (atau `gilangpratama+{runId}-053@qwertysystem.net`), Division `Operations`, Represented By `Ahmad Fauzi`, Active.
- Data uji: Position `Driver`; Blood Type `B`; Country Code `+65`, Number `81234567890`.
- State global: status Required Custom Field `Badge Required` (diatur dan dipulihkan hook).

## Test Steps

1. Ketik Search `Edit Target 54 {runId}-053`, tekan Enter
2. Klik `⋯` pada baris Edit Target 54 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-458: Custom Field Required yang dikosongkan ditolak pada Popup Edit

3. Kosongkan isi Badge Required (nilai tersimpan `Kartu B`)
4. Ubah Position menjadi `Driver`
5. Klik `[Save]`
6. Verifikasi pesan inline `Badge required must not be empty` di bawah field Badge Required
7. Verifikasi Popup Edit tetap terbuka
8. Klik `✕` pada Popup Edit Non-Login User
9. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
10. Klik `[Leave]`
11. Verifikasi Position baris Edit Target 54 di tabel tidak berubah menjadi `Driver` (perubahan Position belum tersimpan)

### TC-GS-NLU-466: Custom Field Required yang baru aktif tidak retroaktif: nilai lama kosong yang tidak disentuh tetap boleh disimpan

12. Ganti isi kotak search dengan `Edit Target 55 {runId}-053`, tekan Enter
13. Klik `⋯` pada baris Edit Target 55 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
14. Verifikasi tanda Required tampil pada label Badge Required di form
15. Ubah Position menjadi `Driver` tanpa menyentuh Badge Required
16. Klik `[Save]`
17. Verifikasi toast sukses `Success, non-login user has been updated.`
18. Verifikasi tidak ada pesan error Required pada Badge Required
19. Verifikasi Position baris Edit Target 55 tersimpan `Driver`

### TC-GS-NLU-181: Edit Custom Field tersimpan dan terlihat di Detail

20. Ganti isi kotak search dengan `Edit Target 48 {runId}-053`, tekan Enter
21. Klik `⋯` pada baris Edit Target 48 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
22. Ubah Blood Type menjadi `B`
23. Klik `[Save]`
24. Verifikasi toast sukses `Success, non-login user has been updated.`
25. Buka Detail record tersebut dan perluas Custom Fields
26. Verifikasi Detail menampilkan Blood Type `B`
27. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-505: Popup Edit memuat Country Code dan Number tersimpan; mengganti Country Code menyimpan kode baru dan Detail menampilkan satu spasi

28. Ketik Search `Gilang Pratama {runId}-053`, tekan Enter
29. Klik `⋯` pada baris Gilang Pratama > `Edit` sehingga Popup Edit Non-Login User terbuka
30. Verifikasi Emergency Phone menampilkan Country Code `🇮🇩 +62` dan Number `81234567890` dari nilai tersimpan
31. Ganti Country Code Emergency Phone menjadi `+65` tanpa mengubah Number
32. Klik `[Save]`
33. Verifikasi toast sukses `Success, non-login user has been updated.`
34. Buka Detail Gilang Pratama dan perluas bagian Custom Fields
35. Verifikasi Detail menampilkan Emergency Phone `+65 81234567890` dengan satu spasi setelah kode negara

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-GS-NLU-458 (ditolak) lebih dulu, lalu TC-GS-NLU-466, TC-GS-NLU-181, dan TC-GS-NLU-505 (aksi sukses), sesuai S-10.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 12, 20, dan 28 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List); langkah 8 dan 10 (menutup popup yang dirty secara deterministik, S-08); langkah 27 (kembali ke daftar setelah Detail).
- Nama Custom Field uji `Badge Required` literal (bukan bersuffix `{runId}`) karena pesan error TC-GS-NLU-458 memuat nama field; ini butir Lampiran A yang masih tertunda untuk modul Non-Login User dan dicatat di sini saja.
- Temuan untuk QA:
  - TC-GS-NLU-458 langkah 2 ("Biarkan Badge Required kosong") bertentangan dengan precondition e (Edit Target 54 memiliki Badge Required `Kartu B`); spec mengosongkan isi field yang tersimpan.
  - TC-GS-NLU-458 Expected butir b ("perubahan Position belum tersimpan") tidak menyebut cara mengamati; spec menutup popup lalu mengasersi Position baris di tabel.
  - TC-GS-NLU-505 bergantung pada Gilang Pratama hasil TC-GS-NLU-94 (Dependensi); spec men-seed record itu sebagai data milik spec dengan Emergency Phone awal `+62 81234567890`.
