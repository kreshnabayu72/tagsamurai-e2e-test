---
id: TC-FA-CF-E2E-044-global-value-currency
title: "Global Value Currency: Prefix Simbol, Nilai Negatif, Batas Dua Desimal, dan Batas 15 Digit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-135
  - TC-FA-CF-618
  - TC-FA-CF-619
coverage:
  web: automated
---

# Global Value Currency: Prefix Simbol, Nilai Negatif, Batas Dua Desimal, dan Batas 15 Digit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Currency Code tenant `IDR` (simbol `Rp`) pada General Settings Company Alpha (Pre-setup #11); format tidak diubah.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-044`): `Global Currency {runId}-044` (Currency, nilai `-5`, tidak tersimpan), `Global Currency 2 {runId}-044` (Currency, nilai `10.55`, tersimpan), `Global Currency 15 {runId}-044` (Currency, nilai `1234567890123.45`, tersimpan), `Global Currency 16 {runId}-044` (Currency, nilai 16 digit `12345678901234.45`, tidak tersimpan). Nilai yang diketik: `-5`, `10.555`, `10.55`.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-044`.
- Kemampuan teknis: pembacaan nilai yang tampil di input Value setelah pengetikan.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-135: Global Value Currency menampilkan simbol mata uang tenant sebagai prefix dan menolak nilai negatif

2. Isi Field Name `Global Currency {runId}-044`, pilih Data Type `Currency`, Scope `General`, Value Type `Global`
3. Verifikasi input Value menampilkan prefix simbol "Rp"
4. Isi Value `-5`
5. Klik [Submit]
6. Verifikasi nilai negatif ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
7. Verifikasi Submit tidak menyimpan field: modal tetap terbuka
8. Klik [Clear Field]

### TC-FA-CF-618: Global Value Currency menerima paling banyak dua desimal

9. Isi Field Name `Global Currency 2 {runId}-044`, pilih Data Type `Currency`, Scope `General`, Value Type `Global`
10. Ketik `10.555` pada input Value
11. Verifikasi Value tetap `10.55`: digit desimal ke-3 tidak masuk ke input
12. Verifikasi tidak ada pesan inline pada input Value (diblokir di level input)
13. Kosongkan input Value, lalu isi Value `10.55`
14. Klik [Submit]
15. Verifikasi nilai `10.55` diterima: modal tertutup
16. Verifikasi toast "Success, custom field has been created." tampil

### TC-FA-CF-619: Global Value Currency 15 digit termasuk desimal diterima dan 16 digit ditolak

17. Klik [+ Custom Field]
18. Isi Field Name `Global Currency 15 {runId}-044`, pilih Data Type `Currency`, Scope `General`, Value Type `Global`
19. Isi Value 15 digit `1234567890123.45`
20. Tunggu toast lama hilang otomatis
21. Klik [Submit]
22. Verifikasi Submit sukses: toast "Success, custom field has been created." tampil
23. Klik [+ Custom Field]
24. Isi Field Name `Global Currency 16 {runId}-044`, pilih Data Type `Currency`, Scope `General`, Value Type `Global`
25. Isi Value 16 digit `12345678901234.45`
26. Klik [Submit]
27. Verifikasi input ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
28. Verifikasi field tidak tersimpan: modal tetap terbuka
29. Klik `[✕]`
30. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
31. Klik `[Leave]`

### Penutup: field yang ditolak tidak tersimpan

32. Ketik Search `{runId}-044`, tekan Enter
33. Verifikasi tabel menampilkan tepat 2 baris: `Global Currency 2 {runId}-044` dan `Global Currency 15 {runId}-044` (field `Global Currency {runId}-044` dan `Global Currency 16 {runId}-044` tidak tersimpan)
34. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 135, 618, 619 (urutan sumber 135, 618, 619). Kasus yang diblokir memakai modal yang sama (langkah 1 sampai 8); [Clear Field] (langkah 8) mengosongkan modal tanpa menutupnya. TC-FA-CF-618 berakhir dengan Submit sukses yang menutup modal sehingga TC-FA-CF-619 membuka modal baru (langkah 17).
- TC-FA-CF-619: bagian 15 digit (diterima) dijalankan sebelum bagian 16 digit (ditolak) pada pembukaan modal terpisah (langkah 17 dan 23). Digit tambahan ke-16 ditambahkan pada bagian bulat.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 13, 17, 23, 32, 34, serta pengisian form sebagai bagian langkah TC. Langkah 29 sampai 31 menutup form dirty secara deterministik (S-08). Langkah 32 sampai 34 membuktikan lewat dua baris tersimpan sebagai anchor positif bahwa dua field yang ditolak tidak muncul.
- Asersi "Submit sukses" pada TC-FA-CF-619 ditulis sebagai toast sukses baku `Success, custom field has been created.` (tertulis di TC-FA-CF-141, 143, dan 155); asersi tambahan itu dicatat sesuai S-03. "Submit ditolak" diamati lewat modal yang tetap terbuka.
- Langkah penghubung toast (S-03, R-22): langkah 20 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-619: Expected a menyebut "Pada 15 digit Submit sukses", tetapi Langkah Uji hanya mengklik [Submit] sesudah digit ke-16 ditambahkan; spec menambah Submit pada 15 digit (langkah 21) dan menguji 16 digit pada pembukaan terpisah. TC juga tidak menyebut posisi digit tambahan.
  - TC-FA-CF-618: nilai `10.55` diterima diasersi lewat modal tertutup (langkah 15) dan toast (langkah 16); Expected hanya menulis "diterima dan toast tampil".
  - Nama field memakai suffix `{runId}-044` (S-12) sehingga tidak sama dengan `Global Currency`, `Global Currency 2`, dan `Global Currency 15` pada Data Uji TC.
