---
id: TC-FA-FAAM-E2E-087-resilience-edit-5xx-timeout-tabrakan-code-dan-save-tag-type
title: "Resilience Edit: Gagal 5xx, Timeout, Tabrakan Code, dan Save TAG Type Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-231
  - TC-FA-FAAM-232
  - TC-FA-FAAM-234
  - TC-FA-FAAM-660
coverage:
  web: automated
---

# Resilience Edit: Gagal 5xx, Timeout, Tabrakan Code, dan Save TAG Type Gagal

## Prerequisites

- Mode: FE+BE (backend nyata) dengan `Spectra.intercept()` parsial di atas backend nyata karena asersi menyangkut state server (record tidak berubah, tidak ada Tag Non-standard).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; pada spec ini hanya dibuka dan ditolak validasi atau dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`; pada spec ini hanya dibuka dan ditolak atau dibatalkan, tidak ada yang tersimpan sehingga Last Updated tidak berubah (S-06).
- Data Dinamis (salinan seed fixture #13d, Dinamis #33): `Edit Target Item 232 {runId}-087` (Code `ETI232`), tidak berhasil tersimpan (timeout).
- Kemampuan teknis: `Spectra.intercept()` memaksa respons Edit 500 (TC-231, 660) dan menunda respons Edit melewati timeout (TC-232); intercept dilepas segera setelah asersi (S-09). Kemampuan sisi server (disediakan tim BE): menyimulasikan tabrakan kandidat Code saat commit dengan retry yang tetap bertabrakan (TC-234); simulasi dihentikan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah Tag Non-standard pada aset Dell Latitude di `tag/` (mode baca) sebagai baseline sebelum aksi.
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-087` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-231: Edit gagal 5xx: modal terbuka, input dipertahankan, toast error

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Ubah Code menjadi `ETI7`
4. Paksa respons Edit 500 lewat intercept jaringan
5. Klik `[Save]`
6. Verifikasi toast `Error, failed to update asset name.`
7. Verifikasi modal Edit tetap terbuka
8. Verifikasi input `ETI7` dipertahankan
9. Verifikasi `[Save]` aktif kembali
10. Lepas intercept respons Edit 500

### TC-FA-FAAM-234: Tabrakan Code hasil generator saat commit pada Edit: retry sekali lalu gagal 5xx

11. Kosongkan Code
12. Simulasikan tabrakan kandidat Code saat commit dengan retry tetap bertabrakan
13. Klik `[Save]`
14. Verifikasi toast `Error, failed to update asset name.`
15. Verifikasi modal Edit tetap terbuka
16. Verifikasi input dipertahankan (Code tetap kosong)
17. Klik `[Save]` lagi
18. Verifikasi request Edit terkirim ulang sehingga generator Code dijalankan lagi
19. Hentikan simulasi tabrakan kandidat Code
20. Klik `[✕]` pada modal Edit
21. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
22. Klik `[Leave]`

### TC-FA-FAAM-232: Edit timeout: toast koneksi dan form dipertahankan

23. Ganti isi kotak search dengan `Edit Target Item 232 {runId}-087`, tekan Enter
24. Klik `⋯` baris `Edit Target Item 232 {runId}-087` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
25. Ubah Code menjadi `ETI232-7`
26. Tunda respons Edit melewati timeout lewat intercept jaringan
27. Klik `[Save]`
28. Verifikasi toast `Connection problem. Please try again.`
29. Verifikasi modal Edit tetap terbuka
30. Verifikasi input `ETI232-7` dipertahankan
31. Lepas penundaan respons Edit
32. Klik `[✕]` pada modal Edit
33. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
34. Klik `[Leave]`

### TC-FA-FAAM-660: Save TAG Type gagal 5xx setelah dialog dikonfirmasi: modal terbuka dan tidak ada Tag yang menjadi Non-standard

35. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
36. Catat jumlah Tag Non-standard pada aset `Dell Latitude` sebagai baseline
37. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
38. Lepas `RFID` dan pilih `NFC`, klik `[Save]`
39. Paksa respons Edit 500 lewat intercept jaringan
40. Klik `[Save]` pada dialog `Change TAG Type`
41. Verifikasi toast `Error, failed to update asset name.`
42. Verifikasi modal Edit tetap terbuka dengan input dipertahankan
43. Verifikasi jumlah Tag Non-standard pada aset `Dell Latitude` sama dengan baseline
44. Lepas intercept respons Edit 500
45. Klik `[✕]` pada modal Edit
46. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
47. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 23, dan 35 untuk menemukan baris target (R-16); pelepasan intercept dan penghentian simulasi pada langkah 10, 19, 31, dan 44 segera setelah asersi (S-09); penutupan form dirty pada langkah 20, 32, dan 45 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- Spec resilience (kelas b) satu spec per modul, FE+BE dengan intercept parsial (bagian 6); bukan `Mode: mock`.
- Langkah Uji TC-FA-FAAM-234 "Submit ulang menjalankan generator lagi" diasersi sebagai request Edit terkirim ulang sementara simulasi tabrakan masih aktif, supaya Code `Edit Target Item` tidak berubah (S-06).
- Temuan untuk QA:
  - TC-FA-FAAM-234 berlabel Manual Only dua sesi paralel tetapi tidak memuat sesi kedua; Expected c tidak menyebut hasil pengamatan "Submit ulang menjalankan generator lagi" selain request terkirim ulang.
  - TC-FA-FAAM-660 Expected c menyebut "tidak ada entri log" pada kegagalan 5xx; asersi ketiadaan log untuk kondisi gagal dikelola spec absence (kelas g, S-05) dan tidak diasersi di spec resilience ini; spec hanya mengasersi jumlah Tag Non-standard terhadap baseline.
  - TC-FA-FAAM-231 dan 232 tidak menyebut apakah Code diubah pada fixture bersama; TC-FA-FAAM-231 memakai Pre-setup #13d tanpa penyimpanan (respons dipaksa 500), TC-FA-FAAM-232 memakai salinan Dinamis #33.
- Alasan melewati sekitar 35 langkah: empat skenario kegagalan satu kelas (fault injection) pada fixture berbeda yang berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Penutupan form dirty (tiga langkah) dan pelepasan intercept per blok menyumbang sekitar sepertiga langkah.
