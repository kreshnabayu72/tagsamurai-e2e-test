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
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 8, 13, dan 19); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 6, 17, dan 26). Pemulihan tiap iterasi uncheck (langkah 36) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uncheck":

| Kolom |
|---|
| Brand |
| Model/Type |

## Test Steps

### TC-FA-GRP-717: Pin kolom Last Updated

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Klik icon (⋯) pada header kolom terakhir
4. Klik [Setup Column]
5. Klik icon Pin Last Updated
6. Klik [Save]
7. Scroll tabel horizontal ke kanan
8. Verifikasi kolom Last Updated membeku (sticky) saat scroll horizontal
9. Refresh F5
10. Ketik Search `Warehouse A`, tekan Enter
11. Klik angka Total Asset Warehouse A
12. Scroll tabel horizontal ke kanan
13. Verifikasi pin kolom Last Updated bertahan setelah F5 (kolom tetap membeku)
14. Klik icon (⋯) pada header kolom terakhir
15. Klik [Setup Column]
16. Klik icon Pin Last Updated untuk unpin
17. Klik [Save]
18. Scroll tabel horizontal ke kanan
19. Verifikasi kolom Last Updated ikut scroll (tidak membeku) setelah unpin
20. Scroll tabel horizontal kembali ke kiri

### TC-FA-GRP-1078 dan TC-FA-GRP-1079: Uncheck kolom Brand dan Model/Type

21. Untuk setiap baris tabel "Kolom uncheck" (langkah 22 sampai 36) dengan `<Kolom>` sebagai nilai baris:
22. Klik icon (⋯) pada header kolom terakhir
23. Klik [Setup Column]
24. Uncheck `<Kolom>`
25. Verifikasi Live Preview langsung menyembunyikan `<Kolom>`
26. Klik [Save]
27. Verifikasi kolom `<Kolom>` hilang dari tabel
28. Refresh F5
29. Ketik Search `Warehouse A`, tekan Enter
30. Klik angka Total Asset Warehouse A
31. Verifikasi tabel menampilkan sedikitnya satu kolom lain
32. Verifikasi kolom `<Kolom>` tetap tidak ada pada tabel setelah F5
33. Hapus preferensi kolom Tab Assets di browser
34. Refresh F5
35. Ketik Search `Warehouse A`, tekan Enter
36. Klik angka Total Asset Warehouse A

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Langkah 22 sampai 36 diulang untuk 2 kolom pada tabel "Kolom uncheck": Brand (TC-FA-GRP-1078), Model/Type (TC-FA-GRP-1079).
- Langkah penghubung (S-03): langkah 11, 30, dan 36 membuka ulang Detail Warehouse A sesudah F5; langkah 12, 18, dan 20 mengatur posisi scroll; langkah 14 sampai 17 adalah Langkah 8 TC-FA-GRP-717 ("Unpin lagi lalu [Save]"); langkah 33 memulihkan preferensi kolom.
- Langkah 6, 17, dan 26 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Langkah 31 menjadi anchor positif untuk absence pada langkah 32.
- Alasan di atas 35 langkah (ekspansi 20 + 1 + 2 iterasi x 15 = 51): semua blok satu kelas (Setup Column Tab Assets, dataset Warehouse A), tiap blok berdiri sendiri (pin diakhiri unpin; tiap iterasi memulihkan preferensi), dan iterasi per kolom memakai parameter dari tabel (8b butir 7).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-717, 1078, dan 1079 Expected tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A.
  - TC-FA-GRP-717 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport; spec menyatakannya sebagai kemampuan tim FE di Prerequisites.
