---
id: TC-FA-CAT-E2E-045-resilience-create-dan-add-subcategory-5xx-dan-timeout
title: "Resilience Create dan Add Subcategory: Respons 5xx dan Timeout Jaringan Mempertahankan Popup dan Input"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-139
  - TC-FA-CAT-167
  - TC-FA-CAT-577
  - TC-FA-CAT-628
coverage:
  web: automated
---

# Resilience Create dan Add Subcategory: Respons 5xx dan Timeout Jaringan Mempertahankan Popup dan Input

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Create dan Add Subcategory dipaksa lewat `Spectra.intercept()`, sedangkan submit ulang diproses backend nyata dan state kategori diasersi).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #20 (CatMain): `Vehicle` (Code `VEH`, leaf, Total Asset 0) dan `Peripheral` (Code `PERI`, internal) menjadi parent; keduanya tidak diubah selain penambahan anak milik spec yang dihapus di hook `after` (efek Last Updated parent dicatat di sini, S-06).
- Data Dinamis (dibuat spec, dihapus hook `before` dan `after` lewat API): kategori L1 `Fail Cat {runId}-045` (Code `FAIL1`), `Timeout Cat {runId}-045`; subkategori `Timeout Sub {runId}-045` di bawah `Vehicle`, `Fail Sub {runId}-045` (Code `FSUB1`) di bawah `Peripheral`. Code literal `FAIL1` dan `FSUB1` dibersihkan di hook `before` sebelum spec berjalan (R-13).
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`):
  - TC-FA-CAT-139: respons Create dipaksa 500.
  - TC-FA-CAT-167: respons Create tidak diberikan (timeout jaringan).
  - TC-FA-CAT-577: respons Add Subcategory tidak diberikan (timeout jaringan).
  - TC-FA-CAT-628: respons Add Subcategory dipaksa 500.
  Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah. Endpoint yang di-intercept mengikuti halaman; tidak ada endpoint karangan.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-139: Create gagal 5xx

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Fail Cat {runId}-045` dan Code `FAIL1`
3. Paksa respons Create menjadi 500 lewat intercept jaringan
4. Klik `[Submit]`
5. Verifikasi toast error `Error, failed to create category.` tampil tanpa tombol aksi
6. Verifikasi popup New Category tetap terbuka
7. Verifikasi input Category Name dan Code dipertahankan
8. Verifikasi `[Submit]` kembali enabled
9. Lepas intercept respons Create
10. Klik `[Submit]`
11. Verifikasi toast `Success, category has been created.` tampil

### TC-FA-CAT-167: Create tanpa respons (timeout jaringan)

12. Klik `[+] Category` pada sidebar
13. Isi Category Name `Timeout Cat {runId}-045`
14. Putus respons Create lewat intercept jaringan (tidak ada respons)
15. Klik `[Submit]`
16. Verifikasi toast error baku `Connection problem. Please try again.` tampil tanpa tombol aksi
17. Verifikasi popup New Category tetap terbuka
18. Verifikasi input Category Name dipertahankan
19. Verifikasi `[Submit]` kembali enabled
20. Pulihkan jaringan (lepas intercept respons Create)
21. Klik `[Submit]`
22. Verifikasi submit ulang berhasil: popup New Category tertutup
23. Ketik Search `Timeout Cat {runId}-045`, tekan Enter
24. Verifikasi tabel memuat tepat satu baris `Timeout Cat {runId}-045` (tidak ada duplikat)
25. Klik `(←)` pada kotak Search

### TC-FA-CAT-577: Add Subcategory tanpa respons (timeout jaringan)

26. Klik elipsis (⋯) pada baris `Vehicle` > `+ Add Subcategory`
27. Isi Category Name `Timeout Sub {runId}-045`
28. Putus respons Add Subcategory lewat intercept jaringan (tidak ada respons)
29. Klik `[Submit]`
30. Verifikasi toast error baku `Connection problem. Please try again.` tampil tanpa tombol aksi
31. Verifikasi toast error T-02 `Error, failed to create category.` tidak tampil
32. Verifikasi popup New Subcategory tetap terbuka
33. Verifikasi input Category Name `Timeout Sub {runId}-045` dipertahankan
34. Verifikasi `[Submit]` kembali enabled
35. Verifikasi toast sukses T-01 tidak tampil
36. Pulihkan jaringan (lepas intercept respons Add Subcategory)
37. Klik `[Submit]`
38. Verifikasi submit ulang berhasil: popup New Subcategory tertutup
39. Klik node `Vehicle` di sidebar
40. Verifikasi tabel memuat tepat satu baris `Timeout Sub {runId}-045` di bawah `Vehicle` (tidak ada duplikat)
41. Klik node `All Categories` di sidebar

### TC-FA-CAT-628: Add Subcategory gagal 5xx

42. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
43. Isi Category Name `Fail Sub {runId}-045` dan Code `FSUB1`
44. Paksa respons Add Subcategory menjadi 500 lewat intercept jaringan
45. Klik `[Submit]`
46. Verifikasi toast error `Error, failed to create category.` tampil tanpa tombol aksi
47. Verifikasi popup New Subcategory tetap terbuka
48. Verifikasi input Category Name dan Code dipertahankan
49. Verifikasi `[Submit]` kembali enabled
50. Lepas intercept respons Add Subcategory
51. Klik `[Submit]`
52. Verifikasi toast `Success, category has been created.` tampil

## Notes

- Mode: FE+BE (kelas b, fault injection). Empat blok berdiri sendiri dan satu kelas harness yang sama; kegagalan satu blok tidak menghilangkan makna blok lain, sehingga jumlah langkah (52) melewati sekitar 35 tanpa dipecah.
- Langkah penghubung (S-03, S-09): langkah 9, 20, 36, 50 (melepas intercept agar tidak bocor ke blok berikutnya), langkah 23 sampai 25 (Search untuk menemukan baris target dan mengosongkannya, R-16), langkah 39 dan 41 (membuka node `Vehicle` untuk melihat anak, lalu kembali ke `All Categories`).
- Hook `after` menghapus kategori milik spec lewat API (kategori `Fail Cat`, `Timeout Cat`, `Timeout Sub`, `Fail Sub` yang tersimpan setelah submit ulang).
- Temuan untuk QA:
  - TC-FA-CAT-167 Expected b menyebut "submit ulang berhasil" tanpa teks toast; spec memverifikasi popup tertutup dan keberadaan satu baris.
  - TC-FA-CAT-139 dan 628 memakai Code literal `FAIL1` dan `FSUB1`; spec membersihkannya di hook `before` karena Code tidak dapat bersuffix run.
- Spec melewati 35 langkah (52 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
