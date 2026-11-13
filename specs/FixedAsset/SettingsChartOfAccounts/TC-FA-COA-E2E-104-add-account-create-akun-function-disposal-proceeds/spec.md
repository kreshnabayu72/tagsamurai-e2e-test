---
id: TC-FA-COA-E2E-104-add-account-create-akun-function-disposal-proceeds
title: "Add Account: Create Akun dengan Account Function Disposal Proceeds"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-368
coverage:
  web: automated
---

# Add Account: Create Akun dengan Account Function Disposal Proceeds

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (D16, dibuat spec lewat UI, tetap Active sampai pembersihan). Account Code maksimal 15 karakter dan tidak dapat memuat `{runId}`, sehingga bernilai literal; identitas run dibawa Account Name:

  | Kode | Account Code | Account Name | Function | Dipakai |
  |---|---|---|---|---|
  | D16 | `CLR-9100` | `Disposal Proceeds Clearing – Create {runId}-104` | Disposal Proceeds | TC-368 |

- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `CLR-9100` bila ada (sisa run sebelumnya atau akhir run); kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris akun baru dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-368: Create akun dengan Account Function Disposal Proceeds

1. Klik `+ Account` di toolbar
2. Isi Account Code `CLR-9100` dan Account Name `Disposal Proceeds Clearing – Create {runId}-104`
3. Pilih Account Function Disposal Proceeds dari dropdown
4. Klik `[Submit]`
5. Verifikasi toast "Success, account has been created."
6. Verifikasi modal Add Account tertutup
7. Ketik Search `CLR-9100`, tekan Enter
8. Verifikasi baris akun `CLR-9100` tampil dengan badge Function Disposal Proceeds
9. Verifikasi baris `CLR-9100` menampilkan Status Active, Used By 0, dan Last Used in Journal kosong
10. Arahkan kursor ke badge Function pada baris `CLR-9100`
11. Verifikasi badge Function tidak menampilkan tooltip saat di-hover
12. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7 (Search Account Code untuk membaca baris sesudah modal ditutup, R-16) dan langkah 12 (kosongkan Search, S-09). Langkah 10 (hover pada badge) menjadi anchor asersi tidak adanya tooltip pada langkah 11 (8b butir 2).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-FA-COA-368 menyebut Account Name literal `Disposal Proceeds Clearing – Create` (D16); spec menambah suffix `{runId}-104` pada Account Name agar identitas run terbawa, Account Code tetap literal karena batas 15 karakter.
  - TC-FA-COA-368 menyebut Expected c "Akun `CLR-9100` tampil" tanpa menyebut sort atau highlight baris baru; spec membaca baris lewat Search dan tidak mengasersi highlight.
  - Post Condition TC-FA-COA-368 (record tersimpan; log L-01 di Changelog, System Log, dan Activity Log dalam satu transaksi) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - Opsi Disposal Proceeds pada dropdown Account Function dan copy popover-nya adalah usulan yang menunggu persetujuan PM (Changelog TC 2026-11-12).
