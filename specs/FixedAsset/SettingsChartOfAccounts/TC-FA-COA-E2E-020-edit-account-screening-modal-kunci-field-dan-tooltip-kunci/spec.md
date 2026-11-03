---
id: TC-FA-COA-E2E-020-edit-account-screening-modal-kunci-field-dan-tooltip-kunci
title: "Edit Account: Screening Modal, Kunci Field, dan Tooltip Kunci"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-34
  - TC-FA-COA-35
  - TC-FA-COA-42
coverage:
  web: automated
---

# Edit Account: Screening Modal, Kunci Field, dan Tooltip Kunci

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE). Kedua akun hanya dibaca dan tidak diubah:

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin`, Function Depreciation Expense | Active, Used By 0, Last Used in Journal kosong, belum pernah diekspor | TC-34 |
  | P2 | `6-2001 – Repairs & Maintenance Expense`, Function Capitalization Offset | Active, Used By 0, Last Used in Journal `Aug 2026` | TC-35, TC-42 |

- Nilai `[Month Year]` pada tooltip TC-35 adalah `Aug 2026` (Last Used in Journal P2).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-34: Modal Edit Account terisi nilai tersimpan dan seluruh field dapat diubah

1. Ketik Search `5-6001`, tekan Enter
2. Klik row action `Edit` pada akun P1 (`5-6001`)
3. Verifikasi modal "Edit Account" terbuka dengan Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, dan Account Function Depreciation Expense terisi
4. Verifikasi ketiga field Enabled
5. Verifikasi tombol `[Clear Field]` dan `[Save]` tampil
6. Verifikasi checkbox "Stay on this form after submitting" tidak ada pada modal Edit
7. Klik `[✕]` di header modal

### TC-FA-COA-35: Account Code dan Function terkunci pada akun yang pernah diekspor

8. Ganti isi kotak search dengan `6-2001`, tekan Enter
9. Klik row action `Edit` pada akun P2 (`6-2001`)
10. Arahkan kursor ke field Account Code
11. Verifikasi Account Code Disabled dengan tooltip "Account Code can't be changed because this account was used in a journal in Aug 2026. Create a new account if needed."
12. Arahkan kursor ke field Account Function
13. Verifikasi Account Function Disabled dengan tooltip "Account Function can't be changed because this account was used in a journal in Aug 2026."
14. Verifikasi Account Name Enabled
15. Klik `[✕]` di header modal

### TC-FA-COA-42: Clear Field pada Edit: field terkunci tetap berisi nilai tersimpan dan field lain divalidasi

16. Klik row action `Edit` pada akun P2 (`6-2001`)
17. Klik `[Clear Field]`
18. Klik `[Save]`
19. Verifikasi Account Code tetap `6-2001` dan tetap Disabled
20. Verifikasi Account Function tetap terkunci dengan nilai tersimpan
21. Verifikasi Account Name kosong
22. Verifikasi caption "Account name must not be empty" muncul
23. Klik `[✕]` di header modal
24. Verifikasi dialog Unsaved Changes tampil
25. Klik `[Leave]`
26. Verifikasi baris P2 pada tabel tetap menampilkan Account Name `Repairs & Maintenance Expense` sehingga tidak ada perubahan tersimpan

## Notes

- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka baris target (langkah 1, 8; pada langkah 16 Search `6-2001` dari langkah 8 masih berlaku); `[✕]` pada langkah 7, 15, dan 23 menutup modal Edit Account (pada langkah 7 dan 15 form tidak dirty sehingga tidak ada dialog Unsaved Changes; pada langkah 23 form dirty dan ditutup deterministik lewat langkah 24 dan 25, S-08).
- Asersi tooltip (langkah 11, 13) ditulis tepat sesudah hover karena state sementara (8b.5). Nilai `[Month Year]` pada teks tooltip diganti `Aug 2026` sesuai kolom Data TC-35.
- Asersi "tidak ada perubahan tersimpan" TC-42 (langkah 26) dibaca dari baris P2 sesudah modal ditutup lewat `[Leave]`, karena TC tidak memberi cara cek lain.
- TC-122, TC-123, dan TC-343 (tooltip kunci Account Function karena Used By dan Last Used in Journal) ada di spec 087.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-42 menyebut "Account Function tetap terkunci dengan nilai tersimpan" tanpa menyebut nilainya; spec mengasersi terkunci dan nilai tidak berubah dari nilai tersimpan P2 (Capitalization Offset menurut tabel Pre-setup).
