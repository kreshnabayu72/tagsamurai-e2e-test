---
id: TC-FA-GRP-E2E-229-tab-assets-setup-column-pin-model-type-dan-kolom-category-geser-pin-serta-tampilan-badge
title: "Tab Assets Setup Column: Pin Kolom Model/Type, Geser dan Pin Kolom Category, dan Tampilan Badge Primary Category dengan Truncation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1083
  - TC-FA-GRP-1168
  - TC-FA-GRP-1169
coverage:
  web: automated
---

# Tab Assets Setup Column: Pin Kolom Model/Type, Geser dan Pin Kolom Category, dan Tampilan Badge Primary Category dengan Truncation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi Brand, Model/Type, Category, Label, dan status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal.
- Data Category untuk TC-FA-GRP-1169 (disediakan tim FE/BE; tidak ada di Tabel Data Uji): satu aset Warehouse A ber-Category `Laptop` (parent `IT Equipment`) dan satu aset ber-Category `Environmental Monitoring Equipment` (parent `Sensors`, nama 34 karakter). Kedua aset berada pada halaman pertama tabel (urutan default, 10 baris per halaman).
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 8, 13, 19, 27, 32, dan 38); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 6, 17, 25, dan 36). Kolom Category dicentang di langkah 23 dan tetap tampil untuk TC-FA-GRP-1169 (precondition TC, tidak diasersi). Hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1083: Pin kolom Model/Type

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Klik icon (⋯) pada header kolom terakhir
4. Klik [Setup Column]
5. Klik icon Pin Model/Type
6. Klik [Save]
7. Scroll tabel horizontal ke kanan
8. Verifikasi kolom Model/Type membeku (sticky) saat scroll horizontal
9. Refresh F5
10. Ketik Search `Warehouse A`, tekan Enter
11. Klik angka Total Asset Warehouse A
12. Scroll tabel horizontal ke kanan
13. Verifikasi pin kolom Model/Type bertahan setelah F5 (kolom tetap membeku)
14. Klik icon (⋯) pada header kolom terakhir
15. Klik [Setup Column]
16. Klik icon Pin Model/Type untuk unpin
17. Klik [Save]
18. Scroll tabel horizontal ke kanan
19. Verifikasi kolom Model/Type ikut scroll (tidak membeku) setelah unpin
20. Scroll tabel horizontal kembali ke kiri

### TC-FA-GRP-1168: Pin kolom Category

21. Klik icon (⋯) pada header kolom terakhir
22. Klik [Setup Column]
23. Centang Category
24. Klik icon Pin Category
25. Klik [Save]
26. Scroll tabel horizontal ke kanan
27. Verifikasi kolom Category membeku (sticky) saat scroll horizontal
28. Refresh F5
29. Ketik Search `Warehouse A`, tekan Enter
30. Klik angka Total Asset Warehouse A
31. Scroll tabel horizontal ke kanan
32. Verifikasi pin kolom Category bertahan setelah F5 (kolom tetap membeku)
33. Klik icon (⋯) pada header kolom terakhir
34. Klik [Setup Column]
35. Klik icon Pin Category untuk unpin
36. Klik [Save]
37. Scroll tabel horizontal ke kanan
38. Verifikasi kolom Category ikut scroll (tidak membeku) setelah unpin
39. Scroll tabel horizontal kembali ke kiri

### TC-FA-GRP-1169: Badge Primary Category dengan truncation dan hover hierarki penuh

40. Amati kolom Category pada halaman pertama tabel
41. Verifikasi nilai Category `Laptop` (≤ 25 karakter) tampil sebagai badge Primary berisi nama penuh
42. Verifikasi nilai Category `Environmental Monitoring Equipment` (> 25 karakter) tampil `Environmenta..ng Equipment` (12 huruf pertama + `..` + 12 huruf terakhir)
43. Hover badge Category `Laptop`
44. Verifikasi hover menampilkan hierarki lengkap dari parent paling atas `IT Equipment > Laptop`
45. Hover badge Category `Environmenta..ng Equipment`
46. Verifikasi hover menampilkan hierarki lengkap dari parent paling atas `Sensors > Environmental Monitoring Equipment`
47. Verifikasi setiap baris pada halaman pertama menampilkan badge Category (kolom Category tidak kosong)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 11, 30 membuka ulang Detail Warehouse A sesudah F5; langkah 7, 12, 18, 20, 26, 31, 37, dan 39 mengatur posisi scroll; langkah 14 sampai 17 dan 33 sampai 36 adalah Langkah 8 TC ("Unpin lagi lalu [Save]"); langkah 40 mengamati kolom Category.
- Langkah 6, 17, 25, dan 36 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Langkah 41 dan 42 menjadi pembanding universal untuk langkah 47 (8b butir 2).
- Alasan di atas 35 langkah (47 langkah): semua blok satu kelas (Setup Column Tab Assets, dataset Warehouse A), tiap blok berdiri sendiri (pin diakhiri unpin), dan dua blok pin memakai urutan langkah identik dengan kolom berbeda.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1083 dan 1168 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A.
  - TC-FA-GRP-1083 dan 1168 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport; spec menyatakannya sebagai kemampuan tim FE.
  - TC-FA-GRP-1169 memakai Category `Laptop`, `IT Equipment`, `Environmental Monitoring Equipment`, dan `Sensors` yang tidak ada di Tabel Data Uji Pre-setup maupun Dinamis; spec menyatakannya sebagai data disediakan tim FE/BE.
  - TC-FA-GRP-1169 Expected d ("setiap aset memiliki Category") diasersi pada baris halaman pertama.
