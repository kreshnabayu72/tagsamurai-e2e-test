---
id: TC-FA-GRP-E2E-227-tab-assets-setup-column-pin-last-updated-dan-uncheck-kolom-brand-model-type
title: "Tab Assets Setup Column: Pin Kolom Last Updated serta Uncheck Kolom Brand dan Model/Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-717
  - TC-FA-GRP-1078
  - TC-FA-GRP-1079
coverage:
  web: automated
---

# Tab Assets Setup Column: Pin Kolom Last Updated serta Uncheck Kolom Brand dan Model/Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi Brand, Model/Type, dan status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated tampil).
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 7, 11, dan 17); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 5, 15, dan 24). Pemulihan tiap iterasi uncheck (langkah 30) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uncheck":

| Kolom |
|---|
| Brand |
| Model/Type |

## Test Steps

### TC-FA-GRP-717: Pin kolom Last Updated

1. Klik angka Total Asset Warehouse A
2. Klik icon (⋯) pada header kolom terakhir
3. Klik [Setup Column]
4. Klik icon Pin Last Updated
5. Klik [Save]
6. Scroll tabel horizontal ke kanan
7. Verifikasi kolom Last Updated membeku (sticky) saat scroll horizontal
8. Refresh F5
9. Klik angka Total Asset Warehouse A
10. Scroll tabel horizontal ke kanan
11. Verifikasi pin kolom Last Updated bertahan setelah F5 (kolom tetap membeku)
12. Klik icon (⋯) pada header kolom terakhir
13. Klik [Setup Column]
14. Klik icon Pin Last Updated untuk unpin
15. Klik [Save]
16. Scroll tabel horizontal ke kanan
17. Verifikasi kolom Last Updated ikut scroll (tidak membeku) setelah unpin
18. Scroll tabel horizontal kembali ke kiri

### TC-FA-GRP-1078 dan TC-FA-GRP-1079: Uncheck kolom Brand dan Model/Type

19. Untuk setiap baris tabel "Kolom uncheck" (langkah 20 sampai 30) dengan `<Kolom>` sebagai nilai baris:
20. Klik icon (⋯) pada header kolom terakhir
21. Klik [Setup Column]
22. Uncheck `<Kolom>`
23. Verifikasi Live Preview langsung menyembunyikan `<Kolom>`
24. Klik [Save]
25. Verifikasi kolom `<Kolom>` hilang dari tabel
26. Refresh F5
27. Klik angka Total Asset Warehouse A
28. Verifikasi tabel menampilkan sedikitnya satu kolom lain
29. Verifikasi kolom `<Kolom>` tetap tidak ada pada tabel setelah F5
30. Hapus preferensi kolom Tab Assets di browser, Refresh F5, lalu klik angka Total Asset Warehouse A

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Langkah 20 sampai 30 diulang untuk 2 kolom pada tabel "Kolom uncheck": Brand (TC-FA-GRP-1078), Model/Type (TC-FA-GRP-1079).
- Langkah penghubung (S-03): langkah 9, 27, dan 30 membuka ulang Detail Warehouse A sesudah F5; langkah 10, 16, dan 18 mengatur posisi scroll; langkah 12 sampai 15 adalah Langkah 8 TC-FA-GRP-717 ("Unpin lagi lalu [Save]"); langkah 30 memulihkan preferensi kolom.
- Langkah 5, 15, dan 24 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Langkah 28 menjadi anchor positif untuk absence pada langkah 29.
- Alasan di atas 35 langkah (ekspansi 18 + 1 + 2 iterasi x 11 = 41): semua blok satu kelas (Setup Column Tab Assets, dataset Warehouse A), tiap blok berdiri sendiri (pin diakhiri unpin; tiap iterasi memulihkan preferensi), dan iterasi per kolom memakai parameter dari tabel (8b butir 7).
- Temuan untuk QA:
  - TC-FA-GRP-717, 1078, dan 1079 Expected tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A.
  - TC-FA-GRP-717 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport; spec menyatakannya sebagai kemampuan tim FE di Prerequisites.
