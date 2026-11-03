---
id: TC-FA-COA-E2E-013-add-account-screening-modal-dropdown-function-popover-dan-clear-field
title: "Add Account: Screening Modal, Dropdown Function, Popover, dan Clear Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-13
  - TC-FA-COA-15
  - TC-FA-COA-16
  - TC-FA-COA-18
coverage:
  web: automated
---

# Add Account: Screening Modal, Dropdown Function, Popover, dan Clear Field

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Function Depreciation Expense, Active; hanya dibaca | TC-15 (hover badge Function) |

- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris P1 dibuka lewat Search.
- Tidak ada akun dibuat oleh spec ini; nilai yang diketik di form (`5-6300` dan Name `Depreciation Expense – Clear Test`) tidak pernah di-submit, sehingga tidak memakai suffix `{runId}`.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-13: Screening modal Add Account

1. Klik `+ Account` di toolbar
2. Verifikasi modal "Add Account" tampil dengan header judul dan `[✕]`
3. Verifikasi field Account Code dengan placeholder "Enter account code"
4. Verifikasi helper Account Code "Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)"
5. Verifikasi field Account Name dengan placeholder "Enter account name"
6. Verifikasi field Account Function dengan placeholder "Select account function"
7. Verifikasi ikon `[ℹ]` tampil di label Account Function
8. Verifikasi checkbox "Stay on this form after submitting" berada di atas tombol dan rata kanan
9. Verifikasi checkbox "Stay on this form after submitting" tidak tercentang
10. Verifikasi tombol `[Clear Field]` dan `[Submit]` tampil

### TC-FA-COA-15: Pilihan Account Function dari dropdown

11. Klik dropdown Account Function
12. Verifikasi enam opsi: Asset Cost, Accumulated Depreciation, Depreciation Expense, Gain on Disposal, Loss on Disposal, Capitalization Offset
13. Verifikasi tidak ada opsi kosong ("None")
14. Verifikasi opsi dropdown tidak memiliki tooltip per opsi
15. Klik `[✕]` di header modal
16. Ketik Search `5-6001`, tekan Enter
17. Arahkan kursor ke badge Function pada baris P1 (`5-6001`)
18. Verifikasi badge Function pada tabel tidak menampilkan tooltip saat di-hover
19. Klik `(←)` pada kotak Search

### TC-FA-COA-16: Popover `[ℹ]` Account Function

20. Klik `+ Account` di toolbar
21. Klik ikon `[ℹ]` di label Account Function
22. Verifikasi penjelasan Asset Cost: "Where the asset's acquisition cost is recorded on the balance sheet."
23. Verifikasi penjelasan Accumulated Depreciation: "Reduces the asset's value on the balance sheet; increases every month."
24. Verifikasi penjelasan Depreciation Expense: "Monthly depreciation expense on the income statement."
25. Verifikasi penjelasan Gain on Disposal: "Gain when an asset is sold above its book value."
26. Verifikasi penjelasan Loss on Disposal: "Loss on disposal, write-off, lost assets, and the value of replaced components."
27. Verifikasi penjelasan Capitalization Offset: "The account where the cost is currently recorded, before FAMS moves it to the asset."
28. Tekan `Esc`
29. Verifikasi field Account Function tetap belum terpilih (placeholder "Select account function")
30. Verifikasi popover tertutup
31. Verifikasi modal Add Account tetap terbuka

### TC-FA-COA-18: Clear Field mengosongkan seluruh field

32. Isi Account Code `5-6300`, Account Name `Depreciation Expense – Clear Test`, dan pilih Account Function Depreciation Expense
33. Klik `[Clear Field]`
34. Verifikasi Account Code kosong
35. Verifikasi Account Name kosong
36. Verifikasi Account Function kembali ke placeholder "Select account function"
37. Verifikasi modal Add Account tetap terbuka
38. Klik `[✕]` di header modal

## Notes

- Spec ini lebih dari 35 langkah (38): tiga dari empat blok adalah screening satu modal Add Account yang sama (dropdown, popover, Clear Field) tanpa submit, berurutan, dan tiap Expected dipecah satu `Verifikasi` per klausa (S-01): TC-13 saja enam butir Expected menjadi sembilan `Verifikasi`, TC-16 delapan butir menjadi sembilan. Tidak ada langkah yang diulang; satu kelas (fungsional form Create) dan kegagalan satu blok tidak menghilangkan makna blok lain (bagian 3, 8b butir 7).
- Langkah penghubung (S-03): langkah 15 (tutup modal agar badge Function di tabel dapat di-hover, form belum diisi sehingga tidak ada dialog Unsaved Changes), langkah 19 (kosongkan Search, 8b butir 9), langkah 20 (buka form baru), dan langkah 38 (tutup modal; form kosong setelah `[Clear Field]` sehingga tidak ada dialog Unsaved Changes). Langkah 16 (Search `5-6001`) membuka baris P1 target hover (R-16).
- Langkah 17 dan 18: hover pada badge sendiri menjadi anchor untuk asersi tidak adanya tooltip (8b butir 2).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-15 Expected (c) "Opsi dropdown tidak memiliki tooltip per opsi" tidak menyebut aksi hover pada opsi; spec mengasersinya tanpa hover pada langkah 14.
  - TC-16 langkah 3 menyebut "Tekan Esc" tanpa menyebut elemen terfokus; spec menekan `Esc` langsung sesudah popover dibuka (langkah 28).
