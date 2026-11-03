---
id: TC-FA-COA-E2E-017-add-account-create-sukses-name-sama-trim-dan-stay-on-this-form
title: "Add Account: Create Sukses, Name Sama, Trim, dan Stay on this Form"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-14
  - TC-FA-COA-17
  - TC-FA-COA-30
  - TC-FA-COA-260
coverage:
  web: automated
---

# Add Account: Create Sukses, Name Sama, Trim, dan Stay on this Form

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Function Depreciation Expense, Active; hanya dibaca | TC-14 (akun sudah ada), TC-30 (Account Name yang sama dengan akun baru) |

- Data Dinamis (dibuat spec lewat UI, tetap Active sampai pembersihan). Account Code maksimal 15 karakter dan tidak dapat memuat `{runId}`, sehingga bernilai literal; identitas run dibawa Account Name:

  | Kode | Account Code | Account Name | Function | Dipakai |
  |---|---|---|---|---|
  | D1 | `5-6100` | `Depreciation Expense – Branch Jakarta {runId}-017` | Depreciation Expense | TC-14 |
  | - | `5-6400` | `Depreciation Expense – Admin` (literal, sama dengan P1 sesuai TC-30) | Depreciation Expense | TC-30 |
  | D4 | `5-6800` | `  Depreciation Expense – Trim Name {runId}-017  ` (spasi di awal dan akhir) | Depreciation Expense | TC-260 |
  | D2 | `5-6200  ` (spasi di ujung; tersimpan `5-6200`) | `Depreciation Expense – Warehouse QA {runId}-017` | Depreciation Expense | TC-17 |

- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `5-6100`, `5-6400`, `5-6800`, dan `5-6200` bila ada (sisa run sebelumnya atau akhir run); kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); setelah Create tabel kembali ke sort default pada halaman yang memuat akun baru.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-14: Create akun baru dengan nilai valid

1. Klik `+ Account` di toolbar
2. Isi Account Code `5-6100`, Account Name `Depreciation Expense – Branch Jakarta {runId}-017`, dan pilih Account Function Depreciation Expense
3. Klik `[Submit]`
4. Verifikasi toast "Success, account has been created."
5. Verifikasi modal Add Account tertutup
6. Verifikasi baris akun `5-6100` di-highlight
7. Verifikasi tabel menampilkan halaman yang memuat akun baru `5-6100`
8. Verifikasi tabel kembali ke sort default Account Code A-Z
9. Verifikasi highlight pada baris `5-6100` hilang tanpa interaksi pengguna
10. Verifikasi baris `5-6100` menampilkan Status Active, Used By 0, dan Last Used in Journal kosong

### TC-FA-COA-30: Create dengan Account Name yang sama dengan akun lain

11. Klik `+ Account` di toolbar
12. Isi Account Code `5-6400`, Account Name `Depreciation Expense – Admin`, dan pilih Account Function Depreciation Expense
13. Klik `[Submit]`
14. Verifikasi toast "Success, account has been created."
15. Verifikasi akun tersimpan: baris dengan Account Code `5-6400` dan Account Name `Depreciation Expense – Admin` tampil di tabel

### TC-FA-COA-260: Spasi di awal dan akhir Account Name dibuang

16. Klik `+ Account` di toolbar
17. Isi Account Code `5-6800`, Account Name `  Depreciation Expense – Trim Name {runId}-017  ` (spasi di awal dan akhir), dan pilih Account Function Depreciation Expense
18. Klik `[Submit]`
19. Verifikasi toast "Success, account has been created."
20. Verifikasi baris `5-6800` menampilkan Account Name `Depreciation Expense – Trim Name {runId}-017` tanpa spasi di ujung

### TC-FA-COA-17: Stay on this form

21. Klik `+ Account` di toolbar
22. Centang checkbox "Stay on this form after submitting"
23. Isi Account Code `5-6200  ` (ada spasi di ujung), Account Name `Depreciation Expense – Warehouse QA {runId}-017`, dan pilih Account Function Depreciation Expense
24. Klik `[Submit]`
25. Verifikasi toast "Success, account has been created."
26. Verifikasi form di-reset (Account Code, Account Name, dan Account Function kembali kosong)
27. Verifikasi modal Add Account tetap terbuka
28. Hapus centang checkbox "Stay on this form after submitting"
29. Klik `[✕]` di header modal
30. Ketik Search `5-6200`, tekan Enter
31. Verifikasi akun tersimpan sebagai `5-6200` (spasi di ujung dihapus): baris dengan Account Code `5-6200` dan Account Name `Depreciation Expense – Warehouse QA {runId}-017` tampil di tabel
32. Klik `(←)` pada kotak Search

## Notes

- Spec ini 32 langkah. TC-33 (klik ganda `[Submit]`) dan TC-289 (Saving state) ada di spec 086.
- Langkah penghubung (S-03): langkah 28 dan 29 (pulihkan checkbox Stay on this form lalu tutup modal; form sudah di-reset sehingga tidak ada dialog Unsaved Changes), langkah 30 (Search Account Code untuk membaca baris sesudah modal ditutup, R-16), dan langkah 32 (kosongkan Search, S-09).
- Urutan TC-17 di akhir spec: modal tetap terbuka setelah Create, sehingga TC lain tidak menumpang state itu (S-10). Langkah 6 sampai 9 mengikuti urutan state (highlight sementara diasersi sebelum asersi lain, 8b butir 5).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-30 mensyaratkan Account Name identik dengan akun P1 (`Depreciation Expense – Admin`), sehingga Account Name akun baru literal tanpa suffix `{runId}` dan akun diidentifikasi lewat Account Code `5-6400`. Dua baris Name sama tidak diasersi bersama karena Post Condition TC-30 ("Dua akun dengan Name sama tampil di tabel") tidak punya langkah observasi di TC (S-01).
  - Post Condition TC-14 (log L-01 di tiga surface; dampak ke modul lain), TC-17, dan TC-260 tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Account Code `5-6100`, `5-6400`, `5-6800`, `5-6200` literal tanpa suffix `{runId}` karena batas 15 karakter; pembersihan hook memakai Code literal itu (R-13).
