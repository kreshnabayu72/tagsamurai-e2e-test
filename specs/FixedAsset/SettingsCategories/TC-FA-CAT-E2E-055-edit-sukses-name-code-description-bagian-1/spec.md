---
id: TC-FA-CAT-E2E-055-edit-sukses-name-code-description-bagian-1
title: "Edit Sukses: Name, Code, Description, dan Snapshot Changelog (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-193
  - TC-FA-CAT-194
  - TC-FA-CAT-195
coverage:
  web: automated
---

# Edit Sukses: Name, Code, Description, dan Snapshot Changelog (Bagian 1)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed (`Furniture`, `Electronics`, dan lainnya) tidak diubah.
- Data milik spec (dibuat lewat seed API di hook `before` dengan jalur Create resmi sehingga Changelog memuat entri Create, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Edit Root {runId}-055` | `E055ROOT` | L1; dipilih di sidebar agar baris target tampil di tabel |
  | Target Edit | `Furniture {runId}-055` | `E055FURN` | anak `Edit Root`, leaf, Description kosong; menggantikan baris `Furniture` Pre-setup #20 pada TC-193, TC-194, TC-195 |

- Sebelum `before` membuat data, hook membersihkan sisa kategori dengan Code `FURN-2` dari run yang gagal (kode literal TC-194).
- Kemampuan teknis: pembacaan nama tampil akun aktor untuk asersi Modified By; jam server dan jam browser sinkron untuk asersi Last Updated (S-12).
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-193: Edit Category Name: toast sukses, refleksi di tabel dan sidebar

1. Klik node `Edit Root {runId}-055` di sidebar
2. Klik elipsis (⋯) pada baris `Furniture {runId}-055` > `Edit`
3. Ubah Category Name menjadi `Office Furniture {runId}-055`
4. Klik `[Save]` lalu catat waktu aksi
5. Verifikasi toast `Success, category has been updated.`
6. Verifikasi popup Edit tertutup
7. Verifikasi baris `Office Furniture {runId}-055` tampil di tabel
8. Verifikasi node `Office Furniture {runId}-055` tampil di sidebar
9. Verifikasi Modified By baris `Office Furniture {runId}-055` adalah aktor (format `[First Name] [Last Initial]`)
10. Verifikasi Last Updated baris `Office Furniture {runId}-055` sesuai waktu Save (toleransi satu menit)

### TC-FA-CAT-194: Edit Code manual

11. Klik elipsis (⋯) pada baris `Office Furniture {runId}-055` > `Edit`
12. Ubah Code menjadi `furn-2`
13. Klik `[Save]`
14. Verifikasi toast `Success, category has been updated.`
15. Verifikasi kolom Code baris `Office Furniture {runId}-055` tampil `FURN-2`

### TC-FA-CAT-195: Edit Description dari kosong ke terisi dan kembali kosong

16. Klik elipsis (⋯) pada baris `Office Furniture {runId}-055` > `Edit`
17. Isi Description `Desc baru`
18. Klik `[Save]`
19. Klik elipsis (⋯) pada baris `Office Furniture {runId}-055` > `Edit`
20. Kosongkan Description
21. Klik `[Save]`
22. Buka Modal Changelog
23. Ketik Search `Office Furniture {runId}-055`, tekan Enter
24. Verifikasi baris Edit Field `Description` Old Value `—` New Value `Desc baru` tampil
25. Verifikasi baris Edit Field `Description` Old Value `Desc baru` New Value `—` tampil
26. Verifikasi nilai kosong ditampilkan sebagai strip `—` pada Old Value baris pertama dan New Value baris kedua
27. Tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-193, TC-194, dan TC-195 ada di spec ini; TC-196, TC-197, dan TC-198 ada di spec 056.
- Penyesuaian data (S-06, S-12): TC memakai baris `Furniture` Pre-setup #20 sebagai target Edit; spec memakai node milik spec bersuffix `{runId}-055`. Old Value dan New Value Changelog mengikuti nama bersuffix. Code awal `E055FURN` menggantikan `FURN`; Code baru `furn-2` dan hasil `FURN-2` dipertahankan dari TC-194.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node `Edit Root` di sidebar agar baris target tampil di tabel tanpa Search; membuka, Search, dan menutup Modal Changelog di TC-195 (Search memakai nama bersuffix sehingga baseline nol, S-12).
- Perubahan urutan Expected tidak ada; Expected TC-193 butir b ditulis per klausa (tabel, sidebar, Modified By, Last Updated).
- Temuan untuk QA:
  - TC-193 Post Condition (Changelog Edit Field `Category Name`, System Log aktor, Activity Log) tanpa langkah observasi di TC sehingga tidak diasersi (S-01); pencatatan log diuji di spec pencatatan log.
  - TC-193 butir b menyebut Modified By "menjadi aktor"; nama tampil akun Total Control tidak tertulis di Pre-setup #1, spec mengasersi format `[First Name] [Last Initial]` (R-14).
  - TC-195 menyebut "dua baris Field `Description` terbaru" tanpa menyatakan urutan sort Changelog pada Date berketelitian menit; spec mengasersi isi kedua baris, bukan posisinya.
  - TC-194 mengetik `furn-2` dan mengharapkan tampil `FURN-2`; konversi huruf kapital otomatis tidak dijelaskan di langkah TC.
