---
id: TC-FA-COA-E2E-015-add-account-validasi-batas-panjang-dan-whitelist-account-code
title: "Add Account: Validasi Batas Panjang dan Whitelist Account Code"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-23
  - TC-FA-COA-25
  - TC-FA-COA-26
  - TC-FA-COA-359
  - TC-FA-COA-360
coverage:
  web: automated
---

# Add Account: Validasi Batas Panjang dan Whitelist Account Code

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat spec lewat UI). Account Code maksimal 15 karakter dengan whitelist huruf, angka, `-`, `_`, `.`, sehingga Code tidak dapat memuat `{runId}` dan bernilai literal; identitas run dibawa Account Name:

  | Kode | Account Code | Account Name | Dipakai |
  |---|---|---|---|
  | - | `A-1.2_3` | `Format Whitelist {runId}-015` | TC-25 |
  | D12 | `TRIM-CODE-00015` | `Depreciation Expense – Trim Boundary {runId}-015` | TC-359 |
  | D13 | `5-6820` | `A` berulang diikuti `-{runId}-015` sehingga total tepat 120 karakter (suffix dihitung) | TC-360 |

  Account Function semua akun: Depreciation Expense. Nilai yang tidak di-submit (`ABCDEFGHIJKLMNO` ditambah `P`, `TRIM-CODE-000016`, Name 120 dan 121 karakter `A`) literal.
- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `A-1.2_3`, `TRIM-CODE-00015`, dan `5-6820` bila ada; kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman; setelah Create tabel kembali ke sort default pada halaman yang memuat akun baru.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Pembukaan form

1. Klik `+ Account` di toolbar

### TC-FA-COA-23: Batas panjang Account Code 15 dan 16 karakter (V-02)

2. Ketik `ABCDEFGHIJKLMNO` (15 karakter) di Account Code
3. Verifikasi tidak ada caption di field Account Code
4. Tambah satu karakter `P` di Account Code (16 karakter)
5. Verifikasi caption "Max. 15 characters" muncul langsung saat mengetik
6. Verifikasi caption "Max. 15 characters" tetap tampil selama Account Code melebihi 15 karakter

### TC-FA-COA-26: Batas panjang Account Name 120 dan 121 karakter (V-06)

7. Ketik tepat 120 karakter `A` di Account Name
8. Verifikasi tidak ada caption di field Account Name
9. Tambah satu karakter `A` di Account Name (121 karakter)
10. Verifikasi caption "Max. 120 characters" muncul langsung saat mengetik

### TC-FA-COA-25: Account Code huruf, angka, `-`, `_`, dan `.` diterima

11. Klik `[Clear Field]`
12. Isi Account Code `A-1.2_3`, Account Name `Format Whitelist {runId}-015`, dan pilih Account Function Depreciation Expense
13. Verifikasi tidak ada caption error di field Account Code
14. Klik `[Submit]`
15. Verifikasi akun `A-1.2_3` tersimpan: baris dengan Account Code `A-1.2_3` dan Account Name `Format Whitelist {runId}-015` tampil di tabel

### TC-FA-COA-359: Batas Account Code dihitung setelah trim (V-02)

16. Klik `+ Account` di toolbar
17. Ketik satu spasi, lalu `TRIM-CODE-00015` (15 karakter), lalu satu spasi di Account Code
18. Verifikasi tidak ada caption "Max. 15 characters"
19. Isi Account Name `Depreciation Expense – Trim Boundary {runId}-015` dan pilih Account Function Depreciation Expense
20. Klik `[Submit]`
21. Verifikasi toast "Success, account has been created."
22. Verifikasi akun tersimpan sebagai `TRIM-CODE-00015` tanpa spasi di ujung: baris dengan Account Code `TRIM-CODE-00015` tampil di tabel
23. Klik `+ Account` di toolbar
24. Ketik satu spasi, lalu `TRIM-CODE-000016` (16 karakter), lalu satu spasi di Account Code
25. Verifikasi caption "Max. 15 characters" muncul langsung saat mengetik

### TC-FA-COA-360: Batas Account Name dihitung setelah trim (V-06)

26. Klik `[Clear Field]`
27. Ketik satu spasi, lalu Account Name 120 karakter (`A` berulang diikuti `-{runId}-015`), lalu satu spasi di Account Name
28. Verifikasi tidak ada caption "Max. 120 characters"
29. Isi Account Code `5-6820` dan pilih Account Function Depreciation Expense
30. Klik `[Submit]`
31. Verifikasi toast "Success, account has been created."
32. Verifikasi Account Name tersimpan 120 karakter tanpa spasi di ujung: baris dengan Account Code `5-6820` menampilkan Account Name 120 karakter itu
33. Klik `+ Account` di toolbar
34. Ketik satu spasi, lalu 121 karakter `A`, lalu satu spasi di Account Name
35. Verifikasi caption "Max. 120 characters" muncul langsung saat mengetik

### Penutupan form

36. Klik `[✕]` di header modal
37. Verifikasi dialog Unsaved Changes tampil
38. Klik `[Leave]`

## Notes

- Spec ini 38 langkah (di atas 35 langkah). Alasan: lima blok batas panjang dan trim pada form Create yang sama dan satu kelas harness (fungsional, form Create), tiap blok berdiri sendiri; langkah ketik, submit, dan baca baris berulang per kasus batas (15/16 karakter Code, 120/121 karakter Name, dengan dan tanpa trim) sesuai bagian 3 dan 8b butir 7. Urutan mengikuti S-10: validasi diblokir (TC-23, TC-26) sebelum aksi sukses (TC-25, TC-359, TC-360).
- Langkah penghubung (S-03): langkah 11 dan 26 (`[Clear Field]` agar field kembali kosong sebelum isian valid); langkah 16, 23, 33 (buka form baru setelah submit sukses atau untuk kasus 16/121 karakter); langkah 36 sampai 38 (menutup form dirty secara deterministik, S-08, S-09).
- Asersi "tersimpan" pada langkah 15, 22, dan 32 dibaca dari baris tabel yang memuat akun baru; Create mengembalikan tabel ke sort default pada halaman yang memuat akun baru (TC-143), sehingga langkah Search tidak diperlukan.
- Nama uji TC-360 dihitung termasuk suffix `-{runId}-015` agar tepat 120 karakter (R-06); jumlah `A` menyesuaikan panjang `{runId}`.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-23 Expected (c) "Caption tetap tampil selama Account Code melebihi 15 karakter" tidak menyebut aksi yang membuktikan kata "selama"; spec mengasersinya sebagai pengamatan ulang pada Account Code 16 karakter (langkah 6).
  - TC-25 Expected (b) "Akun `A-1.2_3` tersimpan" tidak menyebut toast; spec hanya mengasersi baris di tabel. Post Condition TC-359 dan TC-360 (record D12 dan D13 tersimpan) dibaca lewat Expected (b), bukan langkah observasi tambahan.
  - Account Code `A-1.2_3`, `TRIM-CODE-00015`, dan `5-6820` literal tanpa suffix `{runId}` karena batas 15 karakter dan whitelist V-02 sampai V-03; pembersihan di hook memakai Code literal itu (R-13).
