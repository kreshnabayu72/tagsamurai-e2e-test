---
id: TC-FA-FAAM-E2E-081-edit-dialog-berurutan-category-addon-label
title: "Edit Ber-Aset: Dialog Dampak Berurutan, Cancel Dialog Ketiga, dan Total Asset Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-251
  - TC-FA-FAAM-252
  - TC-FA-FAAM-253
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Dampak Berurutan, Cancel Dialog Ketiga, dan Total Asset Berubah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan Pre-setup #10 dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Varian Pre-setup #10d: 42 aset Active (36 ter-pairing, 6 belum TAG pairing); lisensi Tracking tersedia (30). Label `Urgent` (Pre-setup #25) dan leaf `Office Equipment` (Pre-setup #22).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog sebelum aksi sebagai baseline; asersi memakai selisih terhadap baseline (S-12).
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-252: Cancel pada dialog ketiga membatalkan seluruh penyimpanan termasuk perubahan sebelumnya

1. Ketik Search `Dell Latitude`, tekan Enter
2. Catat jumlah entri Changelog sebagai baseline
3. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Ubah Category ke `Office Equipment`, tambahkan Default Addon `Tracking`, dan ganti Default Label ke `Urgent`
5. Klik `[Save]`
6. Klik `[Save]` pada dialog pertama `Change Category`
7. Klik `[Save]` pada dialog kedua `Change Default Addon`
8. Klik `[Cancel]` pada dialog ketiga `Change Default Label`
9. Verifikasi modal Edit tetap terbuka
10. Verifikasi input Category `Office Equipment`, Default Addon `Tracking`, dan Default Label `Urgent` dipertahankan
11. Klik `[✕]` pada modal Edit
12. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
13. Klik `[Leave]`
14. Verifikasi Category baris `Dell Latitude` tetap `IT Equipment` (tidak ada perubahan tersimpan)
15. Buka Changelog (icon Changelog)
16. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada log)
17. Tutup Modal Changelog

### TC-FA-FAAM-251: Beberapa dialog dampak tampil berurutan Category lalu Default Addon lalu Default Label

18. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10d lewat seed reset, lalu Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
19. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
20. Ubah Category ke `Office Equipment`, tambahkan Default Addon `Tracking`, dan ganti Default Label ke `Urgent`
21. Klik `[Save]`
22. Verifikasi dialog pertama `Change Category` tampil
23. Klik `[Save]` pada dialog pertama
24. Verifikasi dialog kedua `Change Default Addon` tampil
25. Klik `[Save]` pada dialog kedua
26. Verifikasi dialog ketiga `Change Default Label` tampil
27. Klik `[Save]` pada dialog ketiga
28. Verifikasi toast `Success, asset name has been updated.` tampil
29. Verifikasi seluruh perubahan tersimpan: Category `Office Equipment`, Default Addon `Tracking`, dan Default Label `Urgent` pada baris `Dell Latitude`

### TC-FA-FAAM-253: Total Asset berubah antara pratinjau dan Save: angka dialog informatif, cascade memakai hitungan transaksi

30. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset, lalu Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
31. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
32. Ubah Category ke `Office Equipment`
33. Klik `[Save]`
34. Verifikasi dialog `Change Category` menampilkan `42 assets will be moved to Office Equipment.`
35. Daftarkan satu aset baru ke `Dell Latitude` lewat sesi API aktor hingga aset tersimpan
36. Klik `[Save]` pada dialog
37. Verifikasi toast `Success, asset name has been updated.` tampil
38. Verifikasi cascade memindahkan 43 aset ke `Office Equipment` (kolom Total Asset baris `Dell Latitude` menampilkan `43`)
39. Verifikasi angka dialog `42` tidak menggagalkan Save
40. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 18, dan 30 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 11 (✕, dialog Unsaved Changes, `[Leave]`, S-08); penutupan Modal Changelog pada langkah 17; pemulihan fixture pada langkah 18, 30, dan 40 (antar-blok, S-09; seed reset dijalankan tanpa syarat karena idempotent, termasuk langkah 18 setelah blok 252 yang dibatalkan).
- Urutan TC: TC-FA-FAAM-252 (dibatalkan) lebih dulu, lalu TC-FA-FAAM-251 dan TC-FA-FAAM-253 yang menyimpan (S-10). "Tidak ada log" pada TC-FA-FAAM-252 diasersi sebagai selisih nol terhadap baseline atas aksi yang dibatalkan, bukan asersi absence kelas g.
- Langkah Uji TC-FA-FAAM-253 "Di sesi lain daftarkan satu aset baru" ditulis sebagai langkah pemicu pelaku kedua lewat sesi API aktor (R-20).
- Temuan untuk QA:
  - TC-FA-FAAM-251, 252, dan 253 memakai fixture Pre-setup #10 langsung dan 251 serta 253 menyimpannya; fixture tidak dapat digandakan sehingga dipulihkan seed reset (S-06, pengecualian 2026-10-30).
  - TC-FA-FAAM-253 Expected c ("angka dialog tidak menggagalkan Save") bertumpang dengan Expected a ("Save sukses"); spec mengasersi keduanya sebagai verifikasi terpisah.
  - TC-FA-FAAM-253 "Cascade memindahkan 43 aset" tidak menyebut cara mengamati; spec memakai kolom Total Asset baris `Dell Latitude`.
- Alasan melewati sekitar 35 langkah: tiga blok satu topik (dialog dampak berurutan pada `Dell Latitude`) dengan pemulihan fixture antar-blok; kegagalan satu blok tidak membuat blok lain kehilangan makna. Penutupan form dirty, pembacaan Changelog, dan pemulihan fixture menyumbang sekitar sepertiga langkah.
