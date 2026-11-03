---
id: TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain
title: "Edit: Brand dan UoM Dikosongkan serta Label, Brand, dan UoM Dihapus Sesi Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-211
  - TC-FA-FAAM-212
  - TC-FA-FAAM-213
  - TC-FA-FAAM-220
  - TC-FA-FAAM-221
coverage:
  web: automated
---

# Edit: Brand dan UoM Dikosongkan serta Label, Brand, dan UoM Dihapus Sesi Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; pada spec ini hanya dibuka dan ditolak validasi atau dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup: Label `Finance` (#25) dan Brand `Dell` (#23) yang sudah tersimpan pada `Edit Target Item`; #25e `Temp Label 211`, #23b `Temp Brand 213`, dan #24b `Temp UoM 221` (satu per TC). Ketiganya dihapus oleh sesi API aktor di dalam spec dan dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seed API Label, Brand, dan UoM sementara (#25e, #23b, #24b) dan sesi API aktor yang menghapusnya.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-212: Brand dikosongkan saat Edit ditolak

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas chip Brand `Dell`
4. Klik `[Save]`
5. Verifikasi error inline `Brand must not be empty`

### TC-FA-FAAM-220: UoM dikosongkan saat Edit ditolak

6. Klik `[Clear Field]`
7. Isi ulang Asset Name `Edit Target Item`, Code `ETI`, Category `IT Equipment`, TAG Type `QR`, dan Brand `Dell` tanpa mengisi UoM
8. Klik `[Save]`
9. Verifikasi error inline `UoM must not be empty`
10. Klik `[✕]` pada modal Edit
11. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
12. Klik `[Leave]`

### TC-FA-FAAM-211: Label dihapus sesi lain saat Edit: chip stale dikosongkan, chip lain bertahan

13. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
14. Pilih Default Label `Temp Label 211` dan `Finance`
15. Hapus `Temp Label 211` lewat sesi API aktor hingga penghapusan tersimpan
16. Klik `[Save]`
17. Verifikasi error inline `Temp Label 211 no longer exists. Please select another.`
18. Verifikasi chip `Finance` bertahan
19. Klik `[✕]` pada modal Edit
20. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
21. Klik `[Leave]`

### TC-FA-FAAM-213: Brand dihapus sesi lain saat Edit: chip stale dikosongkan

22. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
23. Pilih Brand `Temp Brand 213` dan `Dell`
24. Hapus `Temp Brand 213` lewat sesi API aktor hingga penghapusan tersimpan
25. Klik `[Save]`
26. Verifikasi error inline `Temp Brand 213 no longer exists. Please select another.`
27. Verifikasi chip `Dell` bertahan
28. Klik `[✕]` pada modal Edit
29. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
30. Klik `[Leave]`

### TC-FA-FAAM-221: UoM dihapus sesi lain saat Edit ditolak

31. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
32. Pilih UoM `Temp UoM 221`
33. Hapus `Temp UoM 221` lewat sesi API aktor hingga penghapusan tersimpan
34. Klik `[Save]`
35. Verifikasi error inline `This UoM no longer exists. Please select another.`
36. Verifikasi field UoM ter-clear
37. Klik `[✕]` pada modal Edit
38. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
39. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 10, 19, 28, dan 37 (✕, dialog Unsaved Changes, `[Leave]`, S-08) agar blok berikutnya mulai dari form bersih.
- Urutan TC: validasi kosong (TC-FA-FAAM-212, 220) lebih dulu, lalu validasi data stale oleh sesi lain (TC-FA-FAAM-211, 213, 221). Seluruh blok tanpa simpan. Pelaku kedua memakai sesi API aktor (bukan konteks UI kedua), sehingga tidak memakai P-2.
- Langkah Uji TC-FA-FAAM-220 "isi ulang semua field kecuali UoM" dijalankan dengan nilai tersimpan `Edit Target Item`; Brand `Dell` diisi tanpa model.
- Temuan untuk QA:
  - TC-FA-FAAM-211, 213, dan 221 berlabel Manual Only dua sesi paralel; spec memakai sesi API aktor sebagai pelaku kedua sesuai keputusan 2026-10-21.
- Alasan melewati sekitar 35 langkah: seluruh blok memakai popup Edit dari satu dataset yang tidak disimpan (`Edit Target Item`) dan berdiri sendiri; tiap TC membuka dan menutup form sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Penutupan form dirty (tiga langkah) setelah tiap blok stale menyumbang sepertiga langkah.
