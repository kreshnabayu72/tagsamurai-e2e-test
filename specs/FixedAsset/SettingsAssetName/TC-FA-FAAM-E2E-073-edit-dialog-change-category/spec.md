---
id: TC-FA-FAAM-E2E-073-edit-dialog-change-category
title: "Edit Ber-Aset: Dialog Change Category (Jamak, Tunggal, Cancel, Save)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-238
  - TC-FA-FAAM-239
  - TC-FA-FAAM-240
  - TC-FA-FAAM-241
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Change Category (Jamak, Tunggal, Cancel, Save)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan; TC-240 menyimpan Category `Office Equipment`. Pemulihan ke keadaan Pre-setup #10 dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after`. Efek yang tersisa: Last Updated dan entri audit trail Changelog bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Data Pre-setup #14h: `Single Asset Item` (Total Asset 1, Default Label `Interior`), hanya dibuka dan dibatalkan (tidak disimpan). Pohon kategori #22: leaf `Office Equipment`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log aktor (Detail User aktor > tab System Log), dan Activity Log FAMS per Asset Name sebelum aksi sebagai baseline dengan filter Search `Dell Latitude`, sama dengan filter pembandingan sesudah Cancel (langkah 24 sampai 30) dan sesudah Save (langkah 38), agar jumlah dibandingkan pada cakupan yang sama; asersi memakai selisih terhadap baseline (S-12).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-239: Dialog Change Category bentuk tunggal untuk 1 aset

1. Ketik Search `Single Asset Item`, tekan Enter
2. Klik `⋯` baris `Single Asset Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Klik `[Select Category]`, pilih leaf `Office Equipment`, klik `[Select]`
4. Klik `[Save]`
5. Verifikasi dialog `Change Category` dengan teks `1 asset will be moved to Office Equipment. Are you sure you want to save this change?`
6. Klik `[Cancel]` pada dialog
7. Klik `[✕]` pada modal Edit
8. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
9. Klik `[Leave]`

### TC-FA-FAAM-238: Ubah Category pada Asset Name ber-aset memunculkan dialog Change Category jamak

10. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
11. Buka Changelog (icon Changelog), System Log aktor (Detail User aktor > tab System Log), dan Activity Log FAMS satu per satu, ketik Search `Dell Latitude` pada masing-masing, catat jumlah entri hasil filter sebagai baseline, lalu tutup
12. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
13. Klik `[Select Category]`, pilih leaf `Office Equipment`, klik `[Select]`
14. Klik `[Save]`
15. Verifikasi dialog `Change Category` dengan teks `42 assets will be moved to Office Equipment. Are you sure you want to save this change?` dan tombol `[Cancel]` serta `[Save]`

### TC-FA-FAAM-241: Cancel pada dialog dampak membatalkan seluruh penyimpanan

16. Klik `[Cancel]` pada dialog
17. Verifikasi dialog tertutup
18. Verifikasi modal Edit tetap terbuka
19. Verifikasi input Category `Office Equipment` dipertahankan
20. Klik `[✕]` pada modal Edit
21. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
22. Klik `[Leave]`
23. Verifikasi Category baris `Dell Latitude` tetap `IT Equipment` (tanpa mutasi)
24. Buka Changelog (icon Changelog), ketik Search `Dell Latitude`, tekan Enter
25. Verifikasi jumlah entri Changelog sama dengan baseline
26. Tutup Modal Changelog
27. Buka System Log (Detail User aktor > tab System Log), ketik Search `Dell Latitude`, tekan Enter
28. Verifikasi jumlah entri System Log sama dengan baseline
29. Buka Activity Log FAMS, ketik Search `Dell Latitude`, tekan Enter
30. Verifikasi jumlah entri Activity Log sama dengan baseline
31. Buka Fixed Asset > Settings > Asset Master > Asset Name lalu ketik Search `Dell Latitude`, tekan Enter

### TC-FA-FAAM-240: Save pada Change Category menyimpan dan mencatat satu baris Edit Category

32. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
33. Klik `[Select Category]`, pilih leaf `Office Equipment`, klik `[Select]`
34. Klik `[Save]`
35. Klik `[Save]` pada dialog
36. Verifikasi toast `Success, asset name has been updated.` tampil
37. Verifikasi Category baris `Dell Latitude` menjadi `Office Equipment`
38. Buka Changelog (icon Changelog) dan ketik Search `Dell Latitude`, tekan Enter
39. Verifikasi Changelog memuat baris Field `Category`, Old `IT Equipment`, New `Office Equipment`
40. Verifikasi jumlah entri Changelog bertambah tepat satu dibanding baseline (tanpa baris log tingkat aset atau baris tambahan akibat cascade)
41. Tutup Modal Changelog
42. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 10, dan 31 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 6; penutupan form dirty pada langkah 7 dan 20 (✕, dialog Unsaved Changes, `[Leave]`, S-08); pembacaan baseline Changelog, System Log, dan Activity Log serta penutupannya pada langkah 11; membuka Changelog, System Log, dan Activity Log dengan Search pada langkah 24, 27, dan 29 serta menutup Modal Changelog pada langkah 26 dan 41; kembali ke halaman Asset Name pada langkah 31; pemulihan fixture pada langkah 42.
- Urutan TC: TC-FA-FAAM-239 (dibatalkan) lebih dulu, lalu TC-FA-FAAM-238 dan TC-FA-FAAM-241 pada satu dialog yang sama (dialog dibuka oleh TC-FA-FAAM-238, dibatalkan oleh TC-FA-FAAM-241), kemudian TC-FA-FAAM-240 yang menyimpan (S-10).
- "Tanpa log" pada Expected TC-FA-FAAM-241 diasersi sebagai jumlah entri Changelog (langkah 25), System Log (langkah 28), dan Activity Log (langkah 30) sama dengan baseline langkah 11, satu Verifikasi per surface, dengan Search `Dell Latitude` yang sama pada baseline dan pembandingan. "Tanpa mutasi" diasersi pada Category baris sesudah form ditutup (langkah 23).
- Temuan untuk QA:
  - TC-FA-FAAM-238, 240, dan 241 memakai fixture Pre-setup #10 langsung dan TC-FA-FAAM-240 menyimpannya; Tabel Data Dinamis tidak memuat salinan. Fixture tidak dapat digandakan, sehingga spec memulihkannya lewat seed reset (S-06, pengecualian 2026-10-30).
  - TC-FA-FAAM-240 Expected d menyebut "baris log tingkat aset" tanpa menyebut surface pengamatan; spec hanya mengasersi jumlah entri Changelog (langkah 40).
- Alasan melewati sekitar 35 langkah: empat blok satu topik (dialog Change Category) dengan dua pembukaan fixture berbeda; kegagalan satu blok tidak membuat blok lain kehilangan makna.
