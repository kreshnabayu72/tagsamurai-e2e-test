---
id: TC-FA-CAT-E2E-060-resilience-edit-dan-delete-single-5xx-dan-timeout
title: "Resilience Edit dan Delete Single: 5xx dan Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-207
  - TC-FA-CAT-211
  - TC-FA-CAT-236
  - TC-FA-CAT-240
coverage:
  web: automated
---

# Resilience Edit dan Delete Single: 5xx dan Timeout

## Prerequisites

- Mode: FE+BE. Backend nyata; kegagalan 5xx dan timeout dipaksa lewat `Spectra.intercept()` di atas backend nyata (bagian 6 konvensi), bukan mock penuh.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed tidak diubah.
- Data milik spec (seed API di hook `before` lewat jalur Create resmi, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Resil Root {runId}-060` | `E060ROOT` | L1; dipilih di sidebar |
  | Target TC-207, TC-211 | `Furniture {runId}-060` | `E060FURN` | anak `Resil Root`, leaf; menggantikan `Furniture` |
  | Target TC-236 | `Vehicle {runId}-060` | `E060VEH` | anak `Resil Root`, leaf; menggantikan `Vehicle` |
  | Target TC-240 | `Vehicle Timeout {runId}-060` | `E060VEHT` | anak `Resil Root`, leaf; menggantikan `Vehicle` agar hasil timeout tidak mengganggu TC-236 |

- Kemampuan intercept jaringan (disediakan tim FE): memaksa respons Edit 500, memutus respons Edit dan Delete (timeout), dan melepas intercept. Intercept dilepas segera setelah pemicu selesai dan di hook `after` (S-09).
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-207: Edit gagal 5xx: popup tetap terbuka dan toast error T-04

1. Klik node `Resil Root {runId}-060` di sidebar
2. Klik elipsis (⋯) pada baris `Furniture {runId}-060` > `Edit`
3. Ubah Description menjadi `Fail desc`
4. Paksa respons Edit 500 lewat intercept jaringan
5. Klik `[Save]`
6. Verifikasi toast error `Error, failed to update category.` tanpa tombol aksi
7. Verifikasi popup Edit tetap terbuka
8. Verifikasi input Description `Fail desc` dipertahankan
9. Verifikasi `[Save]` kembali enabled
10. Hapus intercept
11. Klik `[Save]` lagi
12. Verifikasi toast `Success, category has been updated.`

### TC-FA-CAT-211: Edit tanpa respons (timeout jaringan)

13. Klik elipsis (⋯) pada baris `Furniture {runId}-060` > `Edit`
14. Ubah Description menjadi `Timeout desc`
15. Putus respons Edit lewat intercept jaringan
16. Klik `[Save]`
17. Verifikasi toast error baku `Connection problem. Please try again.` tanpa tombol aksi
18. Verifikasi popup Edit tetap terbuka
19. Verifikasi input Description `Timeout desc` dipertahankan
20. Verifikasi `[Save]` kembali enabled
21. Verifikasi aksi tidak diasumsikan sukses maupun gagal: toast `Success, category has been updated.` dan toast `Error, failed to update category.` tidak tampil
22. Hapus intercept
23. Klik `✕` pada header popup
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`

### TC-FA-CAT-236: Delete gagal 5xx: toast error T-06 dan data tidak berubah

26. Klik elipsis (⋯) pada baris `Vehicle {runId}-060` > `Delete`
27. Paksa respons Delete 500 lewat intercept jaringan
28. Klik `[Delete]` pada dialog
29. Verifikasi toast error `Error, failed to delete category.` tanpa tombol aksi
30. Verifikasi `Vehicle {runId}-060` tetap ada di tabel
31. Verifikasi `Vehicle {runId}-060` tetap ada di sidebar
32. Verifikasi `[Delete]` pada dialog kembali enabled sehingga aksi Delete dapat dicoba ulang
33. Hapus intercept
34. Klik `[Cancel]` pada dialog

### TC-FA-CAT-240: Delete tanpa respons (timeout jaringan): aksi dapat dicoba ulang

35. Klik elipsis (⋯) pada baris `Vehicle Timeout {runId}-060` > `Delete`
36. Putus respons Delete lewat intercept jaringan
37. Klik `[Delete]` pada dialog
38. Verifikasi toast error baku `Connection problem. Please try again.` tanpa tombol aksi
39. Verifikasi `Vehicle Timeout {runId}-060` tidak dianggap terhapus: baris masih tampil di tabel sebelum data di-refresh
40. Verifikasi aksi Delete dapat dicoba ulang: tombol `[Delete]` pada dialog tersedia untuk diklik ulang
41. Verifikasi dialog Delete tetap terbuka
42. Verifikasi tombol `[Delete]` pada dialog kembali enabled setelah toast timeout
43. Hapus intercept
44. Klik `[Cancel]` pada dialog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-207, TC-211, TC-236, dan TC-240 ada di spec ini; TC-262 dan TC-271 (Bulk Delete) ada di spec 186.
- Kelas b (fault injection): satu spec resilience untuk Edit dan Delete single sesuai bagian 3 prinsip 13. Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01) dan setiap blok memasang serta melepas intercept sendiri. Keempat blok berkelas sama, memakai node milik sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Penyesuaian data (S-06, S-12): TC memakai kategori Pre-setup #20 (`Furniture`, `Vehicle`); spec memakai node milik spec bersuffix `{runId}-060`. TC-240 memakai `Vehicle Timeout` terpisah dari `Vehicle` TC-236 karena permintaan Delete yang diputus responsnya dapat sudah diproses server.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node `Resil Root` di sidebar; menghapus intercept; menutup popup dirty lewat `✕` dan `[Leave]` setelah TC-211 (S-08, S-09); membatalkan dialog Delete lewat `[Cancel]` setelah TC-236 dan TC-240 (S-09).
- Langkah 32 dan 40 sampai 42 mengasersi bahwa dialog Delete tetap terbuka dan `[Delete]` enabled kembali; keadaan ini mengikuti PRD §7.2 poin 4 dan 5, sedangkan Expected TC-236 hanya menyebut "aksi Delete dapat dicoba ulang".
- Langkah 21 menurunkan "aksi tidak diasumsikan sukses maupun gagal" menjadi asersi tidak adanya toast hasil spesifik; anchor positif adalah toast `Connection problem. Please try again.` pada langkah 17.
- Temuan untuk QA:
  - TC-211 dan TC-240 tidak menyatakan apakah permintaan yang diputus sampai ke server; spec tidak mengasersi state server pasca-timeout (tidak ada langkah refresh di TC).
  - TC-211 Expected b ("tidak diasumsikan sukses maupun gagal") tidak dapat diamati langsung; diturunkan seperti pada Notes.
  - TC-236 tidak menyebut keadaan dialog sesudah 5xx; spec mengikuti PRD §7.2 poin 4 (dialog tetap terbuka).
