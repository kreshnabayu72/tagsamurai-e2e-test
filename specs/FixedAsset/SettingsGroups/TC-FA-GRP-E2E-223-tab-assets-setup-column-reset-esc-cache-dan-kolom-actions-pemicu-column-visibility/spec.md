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
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (langkah 8, 15, dan 42). Hook `after` menghapus preferensi kolom Tab Assets di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`.
- Lebar viewport 900px disetel pada langkah 18 supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin pada langkah 20) dan dipulihkan pada langkah 21; hook `after` memulihkan viewport bila spec berhenti sebelum langkah 21.
- Tab Users Detail Group Warehouse A (Group yang sama) dipakai hanya dibaca; daftar kolom default Tab Users disediakan tim FE sebagai pembanding langkah 44.
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-719: [Reset to Default]

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Klik icon (⋯) pada header kolom terakhir
4. Klik [Setup Column]
5. Uncheck Brand
6. Drag Status ke posisi paling atas
7. Klik icon Pin Asset ID
8. Klik [Save]
9. Klik icon (⋯) pada header kolom terakhir
10. Klik [Setup Column]
11. Klik [Reset to Default]
12. Verifikasi Live Preview menampilkan kolom default (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated)
13. Verifikasi Live Preview tidak menampilkan kolom curated
14. Verifikasi Live Preview tanpa kolom terpin
15. Klik [Save]
16. Verifikasi tabel menampilkan kolom default (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated)
17. Verifikasi tabel tanpa kolom curated
18. Setel lebar viewport 900px
19. Scroll tabel horizontal ke kanan
20. Verifikasi tidak ada kolom yang membeku saat tabel di-scroll horizontal
21. Pulihkan lebar viewport
22. Refresh F5
23. Ketik Search `Warehouse A`, tekan Enter
24. Klik angka Total Asset Warehouse A
25. Verifikasi tabel tetap menampilkan kolom default (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated) setelah F5

### TC-FA-GRP-720: (X) dan Esc membatalkan perubahan

26. Klik icon (⋯) pada header kolom terakhir
27. Klik [Setup Column]
28. Uncheck Brand
29. Verifikasi footer popup memuat `[Save]` dan tidak memuat `[Cancel]`
30. Klik (X) pada header popup
31. Verifikasi popup tertutup tanpa menerapkan perubahan
32. Verifikasi tabel masih menampilkan kolom Brand
33. Klik icon (⋯) pada header kolom terakhir
34. Klik [Setup Column]
35. Drag Status ke posisi paling atas
36. Tekan Esc
37. Verifikasi popup tertutup tanpa menerapkan perubahan
38. Verifikasi urutan kolom tabel tetap Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated

### TC-FA-GRP-721: Cache tidak memengaruhi tabel lain

39. Klik icon (⋯) pada header kolom terakhir
40. Klik [Setup Column]
41. Uncheck Brand
42. Klik [Save]
43. Klik Tab Users pada Popup Detail Group Warehouse A
44. Verifikasi tabel Tab Users tetap memakai konfigurasi kolomnya sendiri (kolom default Tab Users)
45. Klik Tab Assets
46. Verifikasi tabel Tab Assets tetap menyembunyikan kolom Brand

### TC-FA-GRP-955: Kolom Actions hanya pemicu Column Visibility

47. Verifikasi kolom Actions tampil paling kanan pada Tab Assets
48. Klik header kolom Actions (⋯)
49. Verifikasi dropdown Column Visibility terbuka
50. Verifikasi baris data tampil (sedikitnya satu baris) dan tidak memuat row action per baris

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 24 membuka ulang Detail Warehouse A sesudah F5 (sesudah `[Save]` popup Detail tetap terbuka, sama seperti spec 224 sampai 229, sehingga tidak ada langkah buka ulang); langkah 3 sampai 5 dan 26 sampai 28 membuka popup lewat icon (⋯) dan [Setup Column]; langkah 6 menetapkan posisi tujuan drag Status paling atas dan langkah 7 menetapkan kolom pin Asset ID (TC-FA-GRP-719 hanya menulis "beberapa kolom").
- Langkah 39 sampai 42 menyimpan Brand tersembunyi untuk TC-FA-GRP-721; TC-FA-GRP-955 tidak bergantung pada konfigurasi itu.
- Alasan di atas 35 langkah: seluruh blok satu kelas (Setup Column Tab Assets, dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan TC-FA-GRP-719 memerlukan satu `Verifikasi` per klausa untuk Live Preview dan tabel (default, tanpa curated, tanpa pin).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Langkah penghubung (S-03, 8b butir 2): langkah 18 (Setel lebar viewport 900px) dan langkah 21 (Pulihkan lebar viewport) menjamin tabel lebih lebar dari viewport sehingga asersi "tidak ada kolom yang membeku" tidak lulus kosong, pola spec 187.
- Temuan untuk QA:
  - TC-FA-GRP-719 Langkah 3 "Ubah urutan, hide, dan pin beberapa kolom" tidak menyebut kolom dan posisi tujuan; spec memilih Brand (hide), Status (drag ke atas), Asset ID (pin).
  - TC-FA-GRP-721 Expected a tidak menyebut isi konfigurasi kolom Tab Users sebagai pembanding; spec memakai daftar kolom default Tab Users dari tim FE.
  - TC-FA-GRP-955 Post Condition tidak ada; Expected c "tidak ada row action per baris" diasersi pada baris yang tampil.
