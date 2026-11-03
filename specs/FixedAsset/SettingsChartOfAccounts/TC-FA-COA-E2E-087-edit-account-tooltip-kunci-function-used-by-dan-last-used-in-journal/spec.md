---
id: TC-FA-COA-E2E-087-edit-account-tooltip-kunci-function-used-by-dan-last-used-in-journal
title: "Edit Account: Tooltip Kunci Function karena Used By dan Last Used in Journal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-122
  - TC-FA-COA-123
  - TC-FA-COA-343
coverage:
  web: automated
---

# Edit Account: Tooltip Kunci Function karena Used By dan Last Used in Journal

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE). Ketiga akun hanya dibaca dan tidak diubah:

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1 (Asset Class `Office Equipment`), Last Used in Journal kosong | TC-122 |
  | P7 | `4-7002 – Gain and Loss on Disposal` | Active, Used By 2 (Asset Class `Delivery Vehicles` dan `Heavy Equipment`), Last Used in Journal kosong | TC-123 |
  | P8 | `1-2001 – Accumulated Depreciation – Equipment` | Active, Used By 2, Last Used in Journal `Sep 2026` | TC-343 |

- Asset Class pemakai P6, P7, dan P8 disediakan tim FE/BE (fixture Asset Class tidak punya identitas lain di TC).
- Nilai `[Month Year]` pada tooltip TC-343 adalah `Sep 2026` (Last Used in Journal P8).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-122: Function terkunci dengan tooltip untuk akun yang dipakai satu Asset Class

1. Ketik Search `5-6002`, tekan Enter
2. Klik row action `Edit` pada akun P6 (`5-6002`)
3. Arahkan kursor ke field Account Function
4. Verifikasi Account Function Disabled dengan tooltip "Account Function can't be changed because this account is used by 1 Asset Class."
5. Verifikasi Account Code tetap Enabled
6. Verifikasi Account Name Enabled
7. Klik `[✕]` di header modal

### TC-FA-COA-123: Tooltip Function untuk akun yang dipakai dua Asset Class

8. Ganti isi kotak search dengan `4-7002`, tekan Enter
9. Klik row action `Edit` pada akun P7 (`4-7002`)
10. Arahkan kursor ke field Account Function
11. Verifikasi tooltip "Account Function can't be changed because this account is used by 2 Asset Classes."
12. Verifikasi Account Code Enabled
13. Klik `[✕]` di header modal

### TC-FA-COA-343: Akun yang pernah diekspor dan dipakai Asset Class: tooltip kunci Account Function memakai alasan Last Used in Journal

14. Ganti isi kotak search dengan `1-2001`, tekan Enter
15. Klik row action `Edit` pada akun P8 (`1-2001`)
16. Arahkan kursor ke field Account Function
17. Verifikasi Account Function Disabled
18. Verifikasi tooltip "Account Function can't be changed because this account was used in a journal in Sep 2026." (alasan Last Used in Journal didahulukan atas alasan Used By)
19. Klik `[✕]` di header modal

## Notes

- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka baris target (langkah 1, 8, 14); `[✕]` pada langkah 7, 13, dan 19 menutup modal Edit Account yang tidak dirty sehingga tidak ada dialog Unsaved Changes.
- Asersi tooltip (langkah 4, 11, 18) ditulis tepat sesudah hover karena state sementara (8b.5). Nilai `[Month Year]` pada teks tooltip diganti `Sep 2026` sesuai kolom Data TC-343.
- TC-34, TC-35, dan TC-42 (screening modal Edit dan kunci karena Last Used in Journal) ada di spec 020.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
