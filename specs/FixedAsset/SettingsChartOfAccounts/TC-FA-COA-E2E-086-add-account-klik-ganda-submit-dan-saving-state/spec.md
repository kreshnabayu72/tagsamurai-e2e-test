---
id: TC-FA-COA-E2E-086-add-account-klik-ganda-submit-dan-saving-state
title: "Add Account: Klik Ganda Submit dan Saving State"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-33
  - TC-FA-COA-289
coverage:
  web: automated
---

# Add Account: Klik Ganda Submit dan Saving State

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat spec lewat UI, tetap Active sampai pembersihan). Account Code maksimal 15 karakter dan tidak dapat memuat `{runId}`, sehingga bernilai literal; identitas run dibawa Account Name:

  | Kode | Account Code | Account Name | Function | Dipakai |
  |---|---|---|---|---|
  | D6 | `5-6500` | `Depreciation Expense – Double Submit {runId}-086` | Depreciation Expense | TC-33 |
  | D11 | `5-6901` | `Depreciation Expense – Saving State {runId}-086` | Depreciation Expense | TC-289 |

- Kemampuan teknis: menunda respons request Create akun lewat `Spectra.intercept()` di atas backend nyata dan melepaskannya pada langkah yang ditentukan; pencocokan request Create mengikuti kontrak API modul (disediakan tim FE).
- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `5-6500` dan `5-6901` bila ada; kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Intercept dilepas di langkah 16 dan di hook `after` bila spec berhenti sebelum itu.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-33: Klik ganda `[Submit]` menghasilkan satu akun

1. Tunggu toast lama hilang otomatis
2. Klik `+ Account` di toolbar
3. Isi Account Code `5-6500`, Account Name `Depreciation Expense – Double Submit {runId}-086`, dan pilih Account Function Depreciation Expense
4. Klik `[Submit]` dua kali cepat
5. Verifikasi hanya satu toast "Success, account has been created."
6. Ketik Search `5-6500`, tekan Enter
7. Verifikasi tabel memuat tepat satu baris dengan Account Code `5-6500`
8. Klik `(←)` pada kotak Search

### TC-FA-COA-289: Saving state pada `[Submit]`

9. Klik `+ Account` di toolbar
10. Isi Account Code `5-6901`, Account Name `Depreciation Expense – Saving State {runId}-086`, dan pilih Account Function Depreciation Expense
11. Tunda respons Create (network delay)
12. Klik `[Submit]`
13. Verifikasi tombol `[Submit]` menampilkan Saving state (loading)
14. Verifikasi tombol `[Submit]` tidak dapat diklik ulang selama respons belum diterima
15. Verifikasi `[Clear Field]` dan `[✕]` ter-disabled selama request berlangsung
16. Lepas tahanan respons Create
17. Tunggu aksi selesai (modal tertutup)

## Notes

- Spec ini 17 langkah. TC-33 dan TC-289 ada di spec ini; TC Create lain pada form yang sama ada di spec 017.
- Langkah penghubung (S-03): langkah 1 ("Tunggu toast lama hilang otomatis" sebelum hitungan toast, R-12), langkah 6 dan 8 (Search `5-6500` untuk membaca baris target karena tabel dapat memuat lebih dari satu halaman, lalu `(←)` mereset tabel; R-16, R-23, bagian 8b butir 13), langkah 11 dan 16 (menahan lalu melepas respons Create; intercept dilepas segera setelah asersi state sementara selesai, S-09) dan langkah 17 ("Tunggu aksi selesai", 8b butir 8, sebelum hook mengakhiri spec).
- Asersi state sementara (langkah 13 sampai 15) ditulis sebelum respons dilepas (8b butir 5). Penundaan respons hanya untuk mengamati state UI, bukan kegagalan yang dipaksa, sehingga spec ini fungsional dan bukan kelas resilience (bagian 3 prinsip 13).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- `A-18`: Account Code literal `5-6500` menjadi objek asersi (TC-FA-COA-33: tabel memuat tepat satu baris `5-6500`; langkah 7); dibersihkan di hook `before` dan `after`. `5-6901` (TC-FA-COA-289) tidak menjadi objek asersi.
- Temuan untuk QA:
  - Post Condition TC-33 (satu record dan satu entri L-01 per surface) dan TC-289 (satu akun `5-6901` dibuat setelah respons diterima) tidak punya langkah observasi di TC; hanya "tepat satu baris `5-6500`" yang diasersi lewat Expected TC-33.
  - Account Code `5-6500` dan `5-6901` literal tanpa suffix `{runId}` karena batas 15 karakter; pembersihan hook memakai Code literal itu (R-13).
