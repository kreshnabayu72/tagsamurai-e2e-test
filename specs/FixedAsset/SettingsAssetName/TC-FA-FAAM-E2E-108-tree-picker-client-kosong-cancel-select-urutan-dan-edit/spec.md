---
id: TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit
title: "Tree Picker: Cancel, Select, Urutan A-Z, Mulai dari Pilihan Tersimpan, dan Client Tanpa Kategori"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-323
  - TC-FA-FAAM-324
  - TC-FA-FAAM-325
  - TC-FA-FAAM-326
  - TC-FA-FAAM-327
coverage:
  web: automated
---

# Tree Picker: Cancel, Select, Urutan A-Z, Mulai dari Pilihan Tersimpan, dan Client Tanpa Kategori

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor berurutan (login akun pertama di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite; akun kedua lewat langkah `Ganti akun` eksplisit; hook `after` mengembalikan sesi ke akun default suite, Total Control `Spectra.env.FA_TC_PASSWORD`):
  - Total Control client utama (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (TC-FA-FAAM-324 sampai TC-FA-FAAM-327).
  - Total Control pada client tanpa Asset Name, tanpa Changelog, dan tanpa kategori (Pre-setup #16b). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_NOCAT_PASSWORD` (TC-FA-FAAM-323).
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca: Pre-setup #22 (pohon kategori client utama: Electronics (Laptop, Phone), IT Equipment, Logistics, Office Furniture, Office Equipment, Vehicles, Legacy Category (excess)); Pre-setup #10 `Dell Latitude` (Category `IT Equipment`), fixture `Fixture.faAssetName.dellLatitude`, yang hanya dibuka di Popup Edit lalu ditutup tanpa menyimpan (Last Updated tidak berubah; S-06). Form Create tidak pernah disimpan.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-324: Cancel menutup Tree Picker tanpa mengubah Category

1. Klik `[+ Asset Name]`
2. Klik `[Select Category]`
3. Klik `Laptop`
4. Klik `[Cancel]`
5. Verifikasi Tree Picker tertutup
6. Verifikasi field Category tetap `No category selected`

### TC-FA-FAAM-325: Pilihan baru berlaku hanya setelah klik Select

7. Klik `[Select Category]`
8. Klik `Laptop`
9. Klik `[Select]`
10. Verifikasi teks Category menampilkan `Electronics > Laptop`

### TC-FA-FAAM-326: Node diurut A→Z di tiap level

11. Klik `[Select Category]`
12. Verifikasi level root berurutan `Electronics`, `IT Equipment`, `Legacy Category`, `Logistics`, `Office Furniture`
13. Verifikasi anak `Electronics` berurutan `Laptop`, `Phone`
14. Klik `[Cancel]`
15. Klik `[✕]` pada modal Create
16. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
17. Klik `[Leave]`

### TC-FA-FAAM-327: Edit, Tree Picker dibuka lagi memulai dari pilihan tersimpan dan label tombol tetap

18. Ketik Search `Dell Latitude`, tekan Enter
19. Klik `⋯` baris `Dell Latitude` lalu `Edit`
20. Klik `[Select Category]`
21. Verifikasi label tombol tetap `Select Category`
22. Verifikasi node `IT Equipment` tersorot
23. Klik `[Cancel]`
24. Klik `[✕]` pada Popup Edit tanpa mengubah apa pun

### TC-FA-FAAM-323: Client tanpa kategori menampilkan empty state dan Select nonaktif

25. Ganti akun: logout, lalu login sebagai Total Control pada client tanpa kategori (Pre-setup #16b)
26. Buka Fixed Asset > Settings > Asset Master > Asset Name
27. Klik `[+ Asset Name]`
28. Klik `[Select Category]`
29. Verifikasi empty state Title `No category yet` dan Description `Get started by creating your first category.`
30. Verifikasi tombol `[Select]` nonaktif
31. Verifikasi tombol `[Cancel]` tetap aktif
32. Klik `[Cancel]`
33. Klik `[✕]` pada modal Create

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 18), `[Cancel]` menutup Tree Picker (langkah 14, 23, 32), `[✕]` menutup form (langkah 15, 24, 33), dan membuka halaman Asset Name sesudah login akun baru (langkah 26). Menutup form Create yang dirty pada langkah 15 sampai 17 mengikuti S-08; form Edit pada langkah 24 dan form Create pada langkah 33 tidak dirty sehingga dialog Unsaved Changes tidak muncul.
- Urutan TC di dalam spec: TC-FA-FAAM-324, TC-FA-FAAM-325, TC-FA-FAAM-326, TC-FA-FAAM-327, lalu TC-FA-FAAM-323. TC-FA-FAAM-323 ditaruh paling akhir karena memakai client dan akun berbeda sehingga membutuhkan ganti akun; empat TC lain memakai satu form Create yang sama.
- Temuan untuk QA:
  - TC-FA-FAAM-326 Expected a menyebut lima akar (`Electronics`, `IT Equipment`, `Legacy Category`, `Logistics`, `Office Furniture`), sedangkan Pre-setup #22 memuat tujuh akar (juga `Office Equipment` dan `Vehicles`); urutan A→Z yang benar menyisipkan `Office Equipment` sebelum `Office Furniture` dan `Vehicles` sesudahnya. Spec mengasersi urutan lima akar yang disebut TC sebagai urutan relatif.
  - TC-FA-FAAM-323 memakai client tanpa kategori (Pre-setup #16b) tetapi akun aktornya tidak tertulis di Pre-setup; spec menulisnya sebagai akun yang disediakan tim FE.
  - TC-FA-FAAM-327 mengedit baris `Dell Latitude` Pre-setup (Category `IT Equipment`) tanpa menyimpan; spec hanya membuka dan menutup Popup Edit.
  - TC-FA-FAAM-324 Expected b menyebut field Category `No category selected` tanpa menyebut state awal sebelum Tree Picker dibuka; spec mengikuti TC.
