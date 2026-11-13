---
id: TC-FA-FAREG-UI-026-form-guided-tooltip
title: "Form Register Asset: Guided Tooltip `fa-registration-form`"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.7#r4", "§4.7#r5", "§4.7#r6", "§4.7#r7", "§4.7#p3", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r4": [3, 4, 36]
  "§4.7#r5": [9, 10]
  "§4.7#r6": [13, 14]
  "§4.7#r7": [19, 20]
  "§4.7#p3": [5, 22]
  "EB-TBL-10": [2, 3, 6, 7, 9, 11, 13, 16, 19, 21, 25, 27, 30, 32, 34, 36]
anchor: [24, 29, 33]
coverage:
  web: automated
---

# Form Register Asset: Guided Tooltip `fa-registration-form`

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-026-1: langkah tur `fa-registration-form`: Step 1 `Choose a group` dengan deskripsi `Pick the group these assets belong to.`; Step 2 `Add the items` dengan deskripsi `Add each asset name with its brand, model, and quantity.`; Step 3 `Add another item` dengan deskripsi `Register a different asset name in the same request.`; Step 4 `Save or submit` dengan deskripsi `Save a draft anytime, or submit when the data is complete.`
  - DU-026-2: indikator langkah `Step 1 of 4`, `Step 2 of 4`, `Step 3 of 4`, dan `Step 4 of 4`.
- Kondisi:
  - K1: form `Register Asset` baru dibuka pada tab `General Information`; tur `fa-registration-form` belum pernah dilihat aktor; keempat targetnya (field `Group`, tabel Item, tombol `+ Asset Name`, footer form) tampil.
  - K2: sama dengan K1.
  - K3: sama dengan K1; tur `fa-registration-form` sudah pernah diselesaikan aktor.

## Test Steps
### Tur tampil otomatis dan keempat langkahnya berisi judul serta deskripsi sesuai
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi tur tampil otomatis dengan indikator `Step 1 of 4`
3. Verifikasi judul `Choose a group` dan deskripsi `Pick the group these assets belong to.` tampil
4. Verifikasi field `Group` disorot spotlight
5. Verifikasi tab `General Information` aktif pada Step 1
6. Verifikasi tombol `[Skip]` dan `[Next]` tampil pada Step 1
7. Verifikasi tombol `[Back]` tidak tampil pada Step 1
8. Klik `[Next]`
9. Verifikasi indikator `Step 2 of 4`, judul `Add the items`, dan deskripsi `Add each asset name with its brand, model, and quantity.` tampil
10. Verifikasi tabel Item disorot spotlight
11. Verifikasi tombol `[Back]` tampil pada Step 2
12. Klik `[Next]`
13. Verifikasi indikator `Step 3 of 4`, judul `Add another item`, dan deskripsi `Register a different asset name in the same request.` tampil
14. Verifikasi tombol `+ Asset Name` disorot spotlight
15. Klik `[Back]`
16. Verifikasi tur kembali ke Step 2 dengan judul `Add the items`
17. Klik `[Next]`
18. Klik `[Next]`
19. Verifikasi indikator `Step 4 of 4`, judul `Save or submit`, dan deskripsi `Save a draft anytime, or submit when the data is complete.` tampil
20. Verifikasi footer form disorot spotlight
21. Verifikasi tombol `[Done]` tampil menggantikan `[Next]` pada Step 4
22. Verifikasi tab `General Information` masih aktif pada Step 4
23. Klik `[Done]`
24. Verifikasi footer form memuat `[Save draft]`
25. Verifikasi overlay tur tidak tampil lagi

### Skip menutup tur
26. Tampilkan Halaman `Register Asset` dengan kondisi K2
27. Verifikasi tur tampil otomatis dengan indikator `Step 1 of 4`
28. Klik `[Skip]`
29. Verifikasi footer form memuat `[Submit]`
30. Verifikasi tur tertutup dan overlay tidak tampil

### Tur tidak tampil otomatis sesudah selesai dan dapat diputar ulang lewat tombol tanda tanya
31. Tampilkan Halaman `Register Asset` dengan kondisi K3
32. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
33. Verifikasi footer form memuat `[Save draft]` tanpa sorotan tur
34. Verifikasi tur tidak tampil otomatis
35. Klik `[?]`
36. Verifikasi tur diputar ulang dari indikator `Step 1 of 4` dengan judul `Choose a group`
