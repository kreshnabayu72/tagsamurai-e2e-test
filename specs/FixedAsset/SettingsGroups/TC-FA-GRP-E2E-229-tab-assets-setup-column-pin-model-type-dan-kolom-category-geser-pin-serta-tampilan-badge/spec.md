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
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 7, 11, 17, 25, 29, dan 35); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 5, 15, 23, dan 33). Kolom Category dicentang di langkah 21 dan tetap tampil untuk TC-FA-GRP-1169 (precondition TC, tidak diasersi). Hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1083: Pin kolom Model/Type

1. Klik angka Total Asset Warehouse A
2. Klik icon (⋯) pada header kolom terakhir
3. Klik [Setup Column]
4. Klik icon Pin Model/Type
5. Klik [Save]
6. Scroll tabel horizontal ke kanan
7. Verifikasi kolom Model/Type membeku (sticky) saat scroll horizontal
8. Refresh F5
9. Klik angka Total Asset Warehouse A
10. Scroll tabel horizontal ke kanan
11. Verifikasi pin kolom Model/Type bertahan setelah F5 (kolom tetap membeku)
12. Klik icon (⋯) pada header kolom terakhir
13. Klik [Setup Column]
14. Klik icon Pin Model/Type untuk unpin
15. Klik [Save]
16. Scroll tabel horizontal ke kanan
17. Verifikasi kolom Model/Type ikut scroll (tidak membeku) setelah unpin
18. Scroll tabel horizontal kembali ke kiri

### TC-FA-GRP-1168: Pin kolom Category

19. Klik icon (⋯) pada header kolom terakhir
20. Klik [Setup Column]
21. Centang Category
22. Klik icon Pin Category
23. Klik [Save]
24. Scroll tabel horizontal ke kanan
25. Verifikasi kolom Category membeku (sticky) saat scroll horizontal
26. Refresh F5
27. Klik angka Total Asset Warehouse A
28. Scroll tabel horizontal ke kanan
29. Verifikasi pin kolom Category bertahan setelah F5 (kolom tetap membeku)
30. Klik icon (⋯) pada header kolom terakhir
31. Klik [Setup Column]
32. Klik icon Pin Category untuk unpin
33. Klik [Save]
34. Scroll tabel horizontal ke kanan
35. Verifikasi kolom Category ikut scroll (tidak membeku) setelah unpin
36. Scroll tabel horizontal kembali ke kiri

### TC-FA-GRP-1169: Badge Primary Category dengan truncation dan hover hierarki penuh

37. Amati kolom Category pada halaman pertama tabel
38. Verifikasi nilai Category `Laptop` (≤ 25 karakter) tampil sebagai badge Primary berisi nama penuh
39. Verifikasi nilai Category `Environmental Monitoring Equipment` (> 25 karakter) tampil `Environmenta..ng Equipment` (12 huruf pertama + `..` + 12 huruf terakhir)
40. Hover badge Category `Laptop`
41. Verifikasi hover menampilkan hierarki lengkap dari parent paling atas `IT Equipment > Laptop`
42. Hover badge Category `Environmenta..ng Equipment`
43. Verifikasi hover menampilkan hierarki lengkap dari parent paling atas `Sensors > Environmental Monitoring Equipment`
44. Verifikasi setiap baris pada halaman pertama menampilkan badge Category (kolom Category tidak kosong)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 9, 27 membuka ulang Detail Warehouse A sesudah F5; langkah 6, 10, 16, 18, 24, 28, 34, dan 36 mengatur posisi scroll; langkah 12 sampai 15 dan 30 sampai 33 adalah Langkah 8 TC ("Unpin lagi lalu [Save]"); langkah 37 mengamati kolom Category.
- Langkah 5, 15, 23, dan 33 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Langkah 38 dan 39 menjadi pembanding universal untuk langkah 44 (8b butir 2).
- Alasan di atas 35 langkah (44 langkah): semua blok satu kelas (Setup Column Tab Assets, dataset Warehouse A), tiap blok berdiri sendiri (pin diakhiri unpin), dan dua blok pin memakai urutan langkah identik dengan kolom berbeda.
- Temuan untuk QA:
  - TC-FA-GRP-1083 dan 1168 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A.
  - TC-FA-GRP-1083 dan 1168 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport; spec menyatakannya sebagai kemampuan tim FE.
  - TC-FA-GRP-1169 memakai Category `Laptop`, `IT Equipment`, `Environmental Monitoring Equipment`, dan `Sensors` yang tidak ada di Tabel Data Uji Pre-setup maupun Dinamis; spec menyatakannya sebagai data disediakan tim FE/BE.
  - TC-FA-GRP-1169 Expected d ("setiap aset memiliki Category") diasersi pada baris halaman pertama.
