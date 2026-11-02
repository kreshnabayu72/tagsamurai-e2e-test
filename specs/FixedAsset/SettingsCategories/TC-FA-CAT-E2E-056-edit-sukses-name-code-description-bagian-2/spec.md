---
id: TC-FA-CAT-E2E-056-edit-sukses-name-code-description-bagian-2
title: "Edit Sukses: Name, Code, Description, dan Snapshot Changelog (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-196
  - TC-FA-CAT-197
  - TC-FA-CAT-198
coverage:
  web: automated
---

# Edit Sukses: Name, Code, Description, dan Snapshot Changelog (Bagian 2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed (`Furniture`, `Electronics`, `Laptop`, dan lainnya) tidak diubah.
- Data milik spec (dibuat lewat seed API di hook `before` dengan jalur Create resmi sehingga Changelog memuat entri Create dengan path saat itu, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Edit Root {runId}-056` | `E056ROOT` | L1; dipilih di sidebar |
  | Target TC-196 | `Furniture {runId}-056` | `E056FURN` | anak `Edit Root`, leaf; menggantikan `Furniture` (Code `FURN`) |
  | Target TC-197 | `Rename Base {runId}-056` | `E056RB` | anak `Edit Root`, leaf; menggantikan `Furniture` pada rename berulang |
  | Ancestor TC-198 | `Electronics {runId}-056` | `E056ELEC` | anak `Edit Root`, internal; menggantikan `Electronics` |
  | Descendant TC-198 | `Laptop {runId}-056` | `E056LT` | anak `Electronics {runId}-056`, leaf; menggantikan `Laptop` |

- Sebelum `before` membuat data, hook membersihkan sisa kategori dengan Code `FMULTI` dari run yang gagal (kode literal TC-196).
- Kemampuan teknis: Modal Changelog dapat dibaca dan dicari; entri Create seed memuat path kategori saat dibuat (jalur Create resmi, disediakan tim FE/BE).
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-196: Edit Name dan Code sekaligus mencatat satu baris log per field

1. Klik node `Edit Root {runId}-056` di sidebar
2. Klik elipsis (⋯) pada baris `Furniture {runId}-056` > `Edit`
3. Ubah Category Name menjadi `Furniture Multi {runId}-056`
4. Ubah Code menjadi `FMULTI`
5. Klik `[Save]`
6. Buka Modal Changelog
7. Ketik Search `Furniture Multi {runId}-056`, tekan Enter
8. Verifikasi baris Edit Field `Category Name` Old Value `Furniture {runId}-056` New Value `Furniture Multi {runId}-056` tampil
9. Verifikasi baris Edit Field `Code` Old Value `E056FURN` New Value `FMULTI` tampil
10. Verifikasi hasil Search memuat tepat dua baris Edit (tidak ada baris ganda)
11. Verifikasi kedua baris memiliki Date dan Category Name path yang sama
12. Verifikasi tidak ada baris Field `Description` pada hasil Search
13. Tutup Modal Changelog

### TC-FA-CAT-197: Rename berulang tidak mengubah entri Changelog lama (snapshot)

14. Klik elipsis (⋯) pada baris `Rename Base {runId}-056` > `Edit`
15. Ubah Category Name menjadi `Furniture B {runId}-056`
16. Klik `[Save]`
17. Klik elipsis (⋯) pada baris `Furniture B {runId}-056` > `Edit`
18. Ubah Category Name menjadi `Furniture C {runId}-056`
19. Klik `[Save]`
20. Buka Modal Changelog
21. Ketik Search `Furniture B {runId}-056`, tekan Enter
22. Verifikasi entri rename pertama tetap Old Value `Rename Base {runId}-056` New Value `Furniture B {runId}-056`
23. Verifikasi entri rename kedua Old Value `Furniture B {runId}-056` New Value `Furniture C {runId}-056`
24. Tutup Modal Changelog

### TC-FA-CAT-198: Rename ancestor tidak mengubah Category Name path pada entri Changelog lama

25. Klik elipsis (⋯) pada baris `Electronics {runId}-056` > `Edit`
26. Ubah Category Name menjadi `Electronics Renamed {runId}-056`
27. Klik `[Save]`
28. Buka Modal Changelog
29. Ketik Search `Laptop {runId}-056`, tekan Enter
30. Verifikasi entri lama `Laptop {runId}-056` tetap menampilkan path snapshot `Edit Root {runId}-056 › Electronics {runId}-056 › Laptop {runId}-056` (tidak berubah menjadi path dengan `Electronics Renamed {runId}-056`)
31. Ganti isi kotak search dengan `Electronics Renamed {runId}-056`, tekan Enter
32. Verifikasi entri rename `Electronics` memuat Category Name path `Edit Root {runId}-056 › Electronics Renamed {runId}-056`
33. Verifikasi entri rename tersebut memuat Old Value `Electronics {runId}-056` dan New Value `Electronics Renamed {runId}-056` (nama exact node)
34. Tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-196, TC-197, dan TC-198 ada di spec ini; TC-193, TC-194, dan TC-195 ada di spec 055.
- Penyesuaian data (S-06, S-12): TC memakai baris Pre-setup #20 (`Furniture`, `Electronics`, `Laptop`) sebagai target; spec memakai node milik spec di bawah `Edit Root {runId}-056`, sehingga Category Name path memuat segmen `Edit Root {runId}-056` di depan path TC (`Electronics › Laptop`). Maknanya sama: path snapshot tidak berubah setelah rename ancestor. Pada TC-197 nama dasar `Rename Base` mewakili `Furniture` agar entri rename pertama tidak tercampur dengan TC-196.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node `Edit Root` di sidebar, serta membuka, Search, dan menutup Modal Changelog. Search memakai nama bersuffix sehingga baseline nol (S-12). Search `Furniture B {runId}-056` pada TC-197 mencocokkan kedua entri rename lewat New Value entri pertama dan Old Value entri kedua.
- Temuan untuk QA:
  - TC-198 mengandalkan entri lama untuk `Electronics › Laptop` dari Pre-setup #23 yang tidak dimiliki spec. Spec membuat sendiri node uji lewat Create resmi dan mengasumsikan entri Create tercatat dengan path saat itu; asumsi ini perlu dikonfirmasi tim BE/FE.
  - TC-196 Expected a tidak menyebut batas ketelitian Date; asersi "Date yang sama" mengikuti ketelitian menit kolom Date Changelog.
