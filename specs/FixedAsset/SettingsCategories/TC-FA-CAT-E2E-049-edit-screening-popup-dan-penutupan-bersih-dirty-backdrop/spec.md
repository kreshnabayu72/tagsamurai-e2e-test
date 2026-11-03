---
id: TC-FA-CAT-E2E-049-edit-screening-popup-dan-penutupan-bersih-dirty-backdrop
title: "Edit Category: Screening Popup Edit, Penutupan Bersih dan Dirty, Backdrop, serta Revert Perubahan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-170
  - TC-FA-CAT-173
  - TC-FA-CAT-174
  - TC-FA-CAT-575
  - TC-FA-CAT-175
  - TC-FA-CAT-176
coverage:
  web: automated
---

# Edit Category: Screening Popup Edit, Penutupan Bersih dan Dirty, Backdrop, serta Revert Perubahan

## Prerequisites

- Mode: FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #20 (CatMain): baris `Furniture` (Code `FURN`, leaf, Total Asset 5) dibuka di popup Edit. Spec tidak menyimpan perubahan apa pun, sehingga data Pre-setup dan Last Updated tidak berubah (S-06).
- Kemampuan teknis: membaca state BE kategori `Furniture` (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-170: Screening popup Edit Category

1. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
2. Verifikasi Zona Header: title `Edit Category` dan icon close (✕)
3. Verifikasi Zona Body: Category Name `Furniture`
4. Verifikasi Zona Body: Category Code `FURN`
5. Verifikasi Zona Body: Description pre-filled dengan nilai tersimpan
6. Verifikasi label dan helper text sama dengan popup New Category
7. Verifikasi Zona Footer: `[Clear Field]` (text, primary) dan `[Save]` (success)
8. Verifikasi tidak ada `[Cancel]` dan tidak ada checkbox `Stay on this form after submitting`
9. Klik icon close (✕) pada popup Edit

### TC-FA-CAT-173: Menutup popup Edit tanpa perubahan

10. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
11. Klik icon close (✕)
12. Verifikasi popup langsung tertutup tanpa dialog
13. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
14. Tekan `Esc`
15. Verifikasi popup langsung tertutup tanpa dialog

### TC-FA-CAT-174: Menutup popup Edit yang berubah, [Cancel] mempertahankan popup dan input

16. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
17. Ubah Category Name menjadi `Furniture X`
18. Klik icon close (✕)
19. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]` tampil
20. Klik `[Cancel]` pada dialog
21. Verifikasi dialog tertutup
22. Verifikasi popup Edit tetap terbuka
23. Verifikasi input Category Name `Furniture X` dipertahankan
24. Klik icon close (✕)
25. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
26. Klik `[Leave]`

### TC-FA-CAT-575: Menutup popup Edit yang berubah lewat [Leave]

27. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
28. Ubah Category Name menjadi `Furniture X`
29. Klik icon close (✕)
30. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]` tampil
31. Klik `[Leave]` pada dialog
32. Verifikasi dialog tertutup
33. Verifikasi popup Edit tertutup
34. Verifikasi baris kategori di tabel tetap bernama `Furniture`
35. Verifikasi tidak ada perubahan data tersimpan (dibaca dari state BE)

### TC-FA-CAT-175: Perubahan yang dikembalikan identik dianggap bersih

36. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
37. Ubah Category Name menjadi `Furniture X` lalu ketik ulang kembali menjadi `Furniture`
38. Klik icon close (✕)
39. Verifikasi popup langsung tertutup
40. Verifikasi dialog Unsaved Changes tidak tampil

### TC-FA-CAT-176: Klik backdrop popup Edit tidak menutup popup

41. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
42. Ubah Description menjadi `Backdrop desc`
43. Klik area backdrop di luar popup
44. Verifikasi popup tetap terbuka
45. Verifikasi input Description `Backdrop desc` dipertahankan
46. Verifikasi dialog Unsaved Changes tidak muncul
47. Klik icon close (✕)
48. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
49. Klik `[Leave]`

## Notes

- Mode: FE+BE. Enam blok berdiri sendiri (screening dan penutupan popup Edit pada satu baris, tanpa menyimpan data) sehingga jumlah langkah (49) melewati sekitar 35; kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (S-03, S-08, S-09): langkah 9 (menutup popup yang bersih setelah screening), langkah 24 sampai 26 dan 47 sampai 49 (menutup form dirty secara deterministik: ✕, dialog Unsaved Changes, `[Leave]`).
- Langkah 6 mengikuti Expected TC ("label dan helper text sama dengan popup New Category"); teks persis label tidak tertulis di TC-FA-CAT-170 dan dirujuk ke popup New Category.
- Temuan untuk QA:
  - TC-FA-CAT-170 Expected b tidak menyebut teks label dan helper text (hanya "sama dengan popup New Category"); asersi bergantung pada TC Create.
  - TC-FA-CAT-170 tidak menyebut nilai Description tersimpan `Furniture`; spec memverifikasi bahwa Description pre-filled dengan nilai tersimpan.
- Spec melewati 35 langkah (49 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
