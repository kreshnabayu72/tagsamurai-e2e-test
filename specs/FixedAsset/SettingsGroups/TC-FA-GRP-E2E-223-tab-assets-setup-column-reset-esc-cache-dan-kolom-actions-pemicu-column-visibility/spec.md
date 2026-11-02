---
id: TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility
title: "Tab Assets Setup Column: [Reset to Default], (X) dan Esc, Cache Tidak Memengaruhi Tabel Lain, dan Kolom Actions Hanya Pemicu Column Visibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-719
  - TC-FA-GRP-720
  - TC-FA-GRP-721
  - TC-FA-GRP-955
coverage:
  web: automated
---

# Tab Assets Setup Column: [Reset to Default], (X) dan Esc, Cache Tidak Memengaruhi Tabel Lain, dan Kolom Actions Hanya Pemicu Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal; susunan default: Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated; kolom curated tersembunyi; tanpa pin.
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (langkah 7, 14, dan 38). Hook `after` menghapus preferensi kolom Tab Assets di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`.
- Lebar viewport diatur supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin pada langkah 17); hook `after` memulihkan viewport.
- Tab Users Detail Group Warehouse A (Group yang sama) dipakai hanya dibaca; daftar kolom default Tab Users disediakan tim FE sebagai pembanding langkah 40.
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-719: [Reset to Default]

1. Klik angka Total Asset Warehouse A
2. Klik icon (⋯) pada header kolom terakhir
3. Klik [Setup Column]
4. Uncheck Brand
5. Drag Status ke posisi paling atas
6. Klik icon Pin Asset ID
7. Klik [Save]
8. Klik icon (⋯) pada header kolom terakhir
9. Klik [Setup Column]
10. Klik [Reset to Default]
11. Verifikasi Live Preview menampilkan kolom default (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated)
12. Verifikasi Live Preview tidak menampilkan kolom curated
13. Verifikasi Live Preview tanpa kolom terpin
14. Klik [Save]
15. Verifikasi tabel menampilkan kolom default (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated)
16. Verifikasi tabel tanpa kolom curated
17. Scroll tabel horizontal ke kanan
18. Verifikasi tidak ada kolom yang membeku saat tabel di-scroll horizontal
19. Refresh F5
20. Klik angka Total Asset Warehouse A
21. Verifikasi tabel tetap menampilkan kolom default (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated) setelah F5

### TC-FA-GRP-720: (X) dan Esc membatalkan perubahan

22. Klik icon (⋯) pada header kolom terakhir
23. Klik [Setup Column]
24. Uncheck Brand
25. Verifikasi footer popup memuat `[Save]` dan tidak memuat `[Cancel]`
26. Klik (X) pada header popup
27. Verifikasi popup tertutup tanpa menerapkan perubahan
28. Verifikasi tabel masih menampilkan kolom Brand
29. Klik icon (⋯) pada header kolom terakhir
30. Klik [Setup Column]
31. Drag Status ke posisi paling atas
32. Tekan Esc
33. Verifikasi popup tertutup tanpa menerapkan perubahan
34. Verifikasi urutan kolom tabel tetap Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated

### TC-FA-GRP-721: Cache tidak memengaruhi tabel lain

35. Klik icon (⋯) pada header kolom terakhir
36. Klik [Setup Column]
37. Uncheck Brand
38. Klik [Save]
39. Klik Tab Users pada Popup Detail Group Warehouse A
40. Verifikasi tabel Tab Users tetap memakai konfigurasi kolomnya sendiri (kolom default Tab Users)
41. Klik Tab Assets
42. Verifikasi tabel Tab Assets tetap menyembunyikan kolom Brand

### TC-FA-GRP-955: Kolom Actions hanya pemicu Column Visibility

43. Verifikasi kolom Actions tampil paling kanan pada Tab Assets
44. Klik header kolom Actions (⋯)
45. Verifikasi dropdown Column Visibility terbuka
46. Verifikasi baris data tampil (sedikitnya satu baris) dan tidak memuat row action per baris

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 20 membuka ulang Detail Warehouse A sesudah F5 (sesudah `[Save]` popup Detail tetap terbuka, sama seperti spec 224 sampai 229, sehingga tidak ada langkah buka ulang); langkah 2 sampai 4 dan 22 sampai 24 membuka popup lewat icon (⋯) dan [Setup Column]; langkah 5 menetapkan posisi tujuan drag Status paling atas dan langkah 6 menetapkan kolom pin Asset ID (TC-FA-GRP-719 hanya menulis "beberapa kolom").
- Langkah 35 sampai 38 menyimpan Brand tersembunyi untuk TC-FA-GRP-721; TC-FA-GRP-955 tidak bergantung pada konfigurasi itu.
- Alasan di atas 35 langkah: seluruh blok satu kelas (Setup Column Tab Assets, dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan TC-FA-GRP-719 memerlukan satu `Verifikasi` per klausa untuk Live Preview dan tabel (default, tanpa curated, tanpa pin).
- Temuan untuk QA:
  - TC-FA-GRP-719 Langkah 3 "Ubah urutan, hide, dan pin beberapa kolom" tidak menyebut kolom dan posisi tujuan; spec memilih Brand (hide), Status (drag ke atas), Asset ID (pin).
  - TC-FA-GRP-721 Expected a tidak menyebut isi konfigurasi kolom Tab Users sebagai pembanding; spec memakai daftar kolom default Tab Users dari tim FE.
  - TC-FA-GRP-955 Post Condition tidak ada; Expected c "tidak ada row action per baris" diasersi pada baris yang tampil.
