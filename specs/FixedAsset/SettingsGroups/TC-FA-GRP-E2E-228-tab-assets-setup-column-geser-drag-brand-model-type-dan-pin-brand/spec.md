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
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 19, 23, dan 29); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 7, 17, dan 27). Pemulihan tiap iterasi drag (langkah 12 dan 13) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom drag" (posisi tujuan dipilih spec karena TC hanya menyebut "posisi lain"):

| Kolom | Posisi tujuan | Urutan kolom sesudah drag |
|---|---|---|
| Brand | paling atas | Brand, Name, Asset ID, TAG, Model/Type, Status, Last Updated |
| Model/Type | paling atas | Model/Type, Name, Asset ID, TAG, Brand, Status, Last Updated |

## Test Steps

### TC-FA-GRP-1080 dan TC-FA-GRP-1081: Drag kolom Brand dan Model/Type

1. Klik angka Total Asset Warehouse A
2. Untuk setiap baris tabel "Kolom drag" (langkah 3 sampai 13) dengan `<Kolom>`, `<Posisi tujuan>`, dan `<Urutan>` sebagai nilai baris:
3. Klik icon (⋯) pada header kolom terakhir
4. Klik [Setup Column]
5. Drag `<Kolom>` ke `<Posisi tujuan>`
6. Verifikasi urutan Live Preview mengikuti posisi baru (`<Urutan>`)
7. Klik [Save]
8. Verifikasi urutan kolom tabel berubah menjadi `<Urutan>`
9. Refresh F5
10. Klik angka Total Asset Warehouse A
11. Verifikasi urutan kolom tabel tetap `<Urutan>` setelah F5
12. Hapus preferensi kolom Tab Assets di browser
13. Refresh F5, lalu klik angka Total Asset Warehouse A

### TC-FA-GRP-1082: Pin kolom Brand

14. Klik icon (⋯) pada header kolom terakhir
15. Klik [Setup Column]
16. Klik icon Pin Brand
17. Klik [Save]
18. Scroll tabel horizontal ke kanan
19. Verifikasi kolom Brand membeku (sticky) saat scroll horizontal
20. Refresh F5
21. Klik angka Total Asset Warehouse A
22. Scroll tabel horizontal ke kanan
23. Verifikasi pin kolom Brand bertahan setelah F5 (kolom tetap membeku)
24. Klik icon (⋯) pada header kolom terakhir
25. Klik [Setup Column]
26. Klik icon Pin Brand untuk unpin
27. Klik [Save]
28. Scroll tabel horizontal ke kanan
29. Verifikasi kolom Brand ikut scroll (tidak membeku) setelah unpin
30. Scroll tabel horizontal kembali ke kiri

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Langkah 3 sampai 13 diulang untuk 2 kolom pada tabel "Kolom drag": Brand (TC-FA-GRP-1080), Model/Type (TC-FA-GRP-1081).
- Langkah penghubung (S-03): langkah 10, 13, dan 21 membuka ulang Detail Warehouse A sesudah F5; langkah 12 memulihkan preferensi kolom sebelum iterasi berikutnya; langkah 18, 22, 28, dan 30 mengatur posisi scroll; langkah 24 sampai 27 adalah Langkah 8 TC-FA-GRP-1082 ("Unpin lagi lalu [Save]").
- Langkah 7, 17, dan 27 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Temuan untuk QA:
  - TC-FA-GRP-1080 sampai 1082 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A.
  - TC-FA-GRP-1080 dan 1081 Langkah 4 "Drag ... ke posisi lain" tidak menyebut posisi tujuan; spec memilih posisi pada tabel iterasi.
  - TC-FA-GRP-1082 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport; spec menyatakannya sebagai kemampuan tim FE di Prerequisites.
