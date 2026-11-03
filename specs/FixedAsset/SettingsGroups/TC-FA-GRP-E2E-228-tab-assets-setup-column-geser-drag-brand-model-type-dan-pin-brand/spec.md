---
id: TC-FA-GRP-E2E-228-tab-assets-setup-column-geser-drag-brand-model-type-dan-pin-brand
title: "Tab Assets Setup Column: Geser (Drag) Kolom Brand dan Model/Type serta Pin Kolom Brand"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1080
  - TC-FA-GRP-1081
  - TC-FA-GRP-1082
coverage:
  web: automated
---

# Tab Assets Setup Column: Geser (Drag) Kolom Brand dan Model/Type serta Pin Kolom Brand

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi Brand, Model/Type, dan status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal (urutan Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated).
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 23, 28, dan 34); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 8, 21, dan 32). Pemulihan tiap iterasi drag (langkah 14 dan 17) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom drag" (posisi tujuan dipilih spec karena TC hanya menyebut "posisi lain"):

| Kolom | Posisi tujuan | Urutan kolom sesudah drag |
|---|---|---|
| Brand | paling atas | Brand, Name, Asset ID, TAG, Model/Type, Status, Last Updated |
| Model/Type | paling atas | Model/Type, Name, Asset ID, TAG, Brand, Status, Last Updated |

## Test Steps

### TC-FA-GRP-1080 dan TC-FA-GRP-1081: Drag kolom Brand dan Model/Type

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Untuk setiap baris tabel "Kolom drag" (langkah 4 sampai 17) dengan `<Kolom>`, `<Posisi tujuan>`, dan `<Urutan>` sebagai nilai baris:
4. Klik icon (⋯) pada header kolom terakhir
5. Klik [Setup Column]
6. Drag `<Kolom>` ke `<Posisi tujuan>`
7. Verifikasi urutan Live Preview mengikuti posisi baru (`<Urutan>`)
8. Klik [Save]
9. Verifikasi urutan kolom tabel berubah menjadi `<Urutan>`
10. Refresh F5
11. Ketik Search `Warehouse A`, tekan Enter
12. Klik angka Total Asset Warehouse A
13. Verifikasi urutan kolom tabel tetap `<Urutan>` setelah F5
14. Hapus preferensi kolom Tab Assets di browser
15. Refresh F5
16. Ketik Search `Warehouse A`, tekan Enter
17. Klik angka Total Asset Warehouse A

### TC-FA-GRP-1082: Pin kolom Brand

18. Klik icon (⋯) pada header kolom terakhir
19. Klik [Setup Column]
20. Klik icon Pin Brand
21. Klik [Save]
22. Scroll tabel horizontal ke kanan
23. Verifikasi kolom Brand membeku (sticky) saat scroll horizontal
24. Refresh F5
25. Ketik Search `Warehouse A`, tekan Enter
26. Klik angka Total Asset Warehouse A
27. Scroll tabel horizontal ke kanan
28. Verifikasi pin kolom Brand bertahan setelah F5 (kolom tetap membeku)
29. Klik icon (⋯) pada header kolom terakhir
30. Klik [Setup Column]
31. Klik icon Pin Brand untuk unpin
32. Klik [Save]
33. Scroll tabel horizontal ke kanan
34. Verifikasi kolom Brand ikut scroll (tidak membeku) setelah unpin
35. Scroll tabel horizontal kembali ke kiri

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Langkah 4 sampai 17 diulang untuk 2 kolom pada tabel "Kolom drag": Brand (TC-FA-GRP-1080), Model/Type (TC-FA-GRP-1081).
- Langkah penghubung (S-03): langkah 12, 17, dan 26 membuka ulang Detail Warehouse A sesudah F5; langkah 14 memulihkan preferensi kolom sebelum iterasi berikutnya; langkah 22, 27, 33, dan 35 mengatur posisi scroll; langkah 29 sampai 32 adalah Langkah 8 TC-FA-GRP-1082 ("Unpin lagi lalu [Save]").
- Langkah 8, 21, dan 32 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1080 sampai 1082 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A.
  - TC-FA-GRP-1080 dan 1081 Langkah 4 "Drag ... ke posisi lain" tidak menyebut posisi tujuan; spec memilih posisi pada tabel iterasi.
  - TC-FA-GRP-1082 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport; spec menyatakannya sebagai kemampuan tim FE di Prerequisites.
