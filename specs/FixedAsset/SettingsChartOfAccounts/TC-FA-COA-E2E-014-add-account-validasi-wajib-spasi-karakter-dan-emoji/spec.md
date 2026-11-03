---
id: TC-FA-COA-E2E-014-add-account-validasi-wajib-spasi-karakter-dan-emoji
title: "Add Account: Validasi Wajib, Spasi, Karakter, dan Emoji"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-19
  - TC-FA-COA-20
  - TC-FA-COA-21
  - TC-FA-COA-22
  - TC-FA-COA-24
  - TC-FA-COA-27
coverage:
  web: automated
---

# Add Account: Validasi Wajib, Spasi, Karakter, dan Emoji

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis: tidak ada akun yang seharusnya tersimpan. Semua submit diblokir validasi. Nilai pemeriksa yang dipakai:
  - Account Name valid `Depreciation Expense – Validation {runId}-014` (dipakai TC-19, TC-20, TC-22).
  - Account Code valid `5-6300` (dipakai TC-21 dan TC-22). Account Code maksimal 15 karakter dan tidak dapat memuat `{runId}`, sehingga bernilai literal; identitas run dibawa Account Name.
  - Account Function `Depreciation Expense`.
- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `5-6300` bila ada (sisa run sebelumnya atau kegagalan validasi); kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman; pemeriksaan akhir memakai Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Pembukaan form

1. Klik `+ Account` di toolbar

### TC-FA-COA-19: Account Code wajib diisi (V-01)

2. Isi Account Name `Depreciation Expense – Validation {runId}-014` dan pilih Account Function Depreciation Expense; biarkan Account Code kosong
3. Klik `[Submit]`
4. Verifikasi caption "Account code must not be empty" di field Account Code
5. Verifikasi modal Add Account tetap terbuka

### TC-FA-COA-20: Account Code hanya spasi (F-FACO-01.k4)

6. Klik `[Clear Field]`
7. Isi Account Code dengan tiga spasi, Account Name `Depreciation Expense – Validation {runId}-014`, dan pilih Account Function Depreciation Expense
8. Klik `[Submit]`
9. Verifikasi caption "Account code must not be empty"

### TC-FA-COA-21: Account Name wajib diisi (V-05) dan hanya spasi

10. Klik `[Clear Field]`
11. Isi Account Code `5-6300`, pilih Account Function Depreciation Expense, dan isi Account Name dengan dua spasi
12. Klik `[Submit]`
13. Verifikasi caption "Account name must not be empty"

### TC-FA-COA-22: Account Function belum dipilih (V-08)

14. Klik `[Clear Field]`
15. Isi Account Code `5-6300` dan Account Name `Depreciation Expense – Validation {runId}-014`; biarkan Account Function kosong
16. Klik `[Submit]`
17. Verifikasi caption "Account function must not be empty"

### TC-FA-COA-24: Karakter Account Code di luar whitelist (V-03)

18. Klik `[Clear Field]`
19. Ketik `1/1001` di Account Code
20. Verifikasi caption "Account code contains invalid characters" muncul langsung saat mengetik

### TC-FA-COA-27: Account Name berisi emoji (V-07)

21. Klik `[Clear Field]`
22. Ketik `Fixed Assets 🚗` di Account Name
23. Verifikasi karakter emoji tidak masuk ke input Account Name

### Penutupan form dan pembacaan akhir tabel

24. Klik `[✕]` di header modal
25. Verifikasi dialog Unsaved Changes tampil
26. Klik `[Leave]`
27. Ketik Search `5-6300`, tekan Enter
28. Verifikasi tidak ada akun dengan Code `5-6300`: tabel menampilkan "No results found" (Expected TC-21 butir b dan TC-22 butir b)
29. Ganti isi kotak search dengan `Depreciation Expense – Validation {runId}-014`, tekan Enter
30. Verifikasi tidak ada akun dengan Account Name tersebut: tabel menampilkan "No results found" (Expected TC-19 butir c, TC-20 butir b, dan TC-22 butir b)
31. Klik `(←)` pada kotak Search

## Notes

- Spec ini 31 langkah. Satu pembukaan modal dipakai untuk semua kasus; field dikosongkan dengan `[Clear Field]` di antara kasus (bagian 3, halaman yang sama dipakai berulang) dan langkah pembersih itu juga memisahkan TC-19/20 yang captionnya identik (R-12).
- Langkah penghubung (S-03): langkah 6, 10, 14, 18, 21 (`[Clear Field]`); langkah 24 sampai 26 menutup form dirty secara deterministik (S-08, S-09); langkah 27, 29 (Search untuk pembacaan akhir, R-16) dan langkah 31 (kosongkan Search).
- Pembacaan "tidak ada akun dibuat": Expected TC-19 (c), TC-20 (b), TC-21 (b), dan TC-22 (b) tidak dapat dibaca di tabel selama modal terbuka; keempatnya dibaca sekaligus pada langkah 28 dan 30 setelah modal ditutup. Empty state "No results found" hasil Search menjadi anchor absence yang sah (8b butir 2).
- Expected TC-19 (a) hanya diasersi pada field Account Code; TC tidak menyebut apakah caption field lain ikut tampil.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-27 Expected (b) "Bila lolos sampai submit, muncul 'Account name contains invalid characters'" bersyarat dan tidak dapat dicapai selama emoji diblokir di input (Expected a); spec tidak mengasersinya (S-08, tanpa langkah bersyarat). Caption itu tidak teruji sama sekali.
  - Account Code `5-6300` literal tanpa suffix `{runId}` karena batas 15 karakter; Code tidak menjadi data tersimpan di spec ini kecuali kegagalan validasi, sehingga pembersihan hook memakai Code literal itu (R-13).
