---
id: TC-FA-COA-E2E-088-cancel-dialog-bulk-deactivate-dan-delete-campuran
title: "Cancel Dialog Bulk Deactivate dan Delete Campuran (D-03 dan D-09)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-295
  - TC-FA-COA-297
coverage:
  web: automated
---

# Cancel Dialog Bulk Deactivate dan Delete Campuran (D-03 dan D-09)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca (Cancel tidak mengubah data; identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Active, Used By 0 (eligible) | TC-295 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1 (Asset Class `Office Equipment`) | TC-295 |
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Active, pernah diekspor (Last Used in Journal Aug 2026) | TC-297 |
  | P5 | `CAP-6100 – Capitalization Clearing – Repairs` | Active, Used By 0 (eligible) | TC-297 |

- Asset Class pemakai P6 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-295: Cancel pada dialog Bulk Deactivate campuran (D-03) mempertahankan seleksi dan data

1. Ketik Search `5-6001`, tekan Enter
2. Centang akun P1 (`5-6001`)
3. Ganti isi kotak search dengan `5-6002`, tekan Enter
4. Centang akun P6 (`5-6002`)
5. Klik Bulk `Deactivate`
6. Klik `[Cancel]` pada dialog D-03
7. Verifikasi dialog "Deactivate Accounts" (D-03) tertutup
8. Verifikasi tidak ada toast
9. Verifikasi akun P6 tetap Active
10. Ganti isi kotak search dengan `5-6001`, tekan Enter
11. Verifikasi akun P1 tetap Active
12. Verifikasi seleksi dan Bulk Action Bar tetap tampil

### TC-FA-COA-297: Cancel pada dialog Bulk Delete campuran (D-09) mempertahankan seleksi dan data

13. Muat ulang halaman (F5)
14. Ketik Search `6-2001`, tekan Enter
15. Centang akun P2 (`6-2001`)
16. Ganti isi kotak search dengan `CAP-6100`, tekan Enter
17. Centang akun P5 (`CAP-6100`)
18. Klik Bulk `Delete`
19. Klik `[Cancel]` pada dialog D-09
20. Verifikasi dialog "Delete Accounts" (D-09) tertutup
21. Verifikasi tidak ada toast
22. Verifikasi akun P5 tetap ada di tabel
23. Ganti isi kotak search dengan `6-2001`, tekan Enter
24. Verifikasi akun P2 tetap ada di tabel
25. Verifikasi seleksi dan Bulk Action Bar tetap tampil

## Notes

- TC-FA-COA-293, 294, 296 ada di spec 030.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Muat ulang halaman (F5)" (langkah 13) membersihkan seleksi dan Search sebelum TC berikutnya (S-09).
- Asersi tidak ada toast ditaruh segera setelah dialog tertutup, sebelum asersi data (8b.11); urutan Expected TC berubah untuk itu.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition "tidak ada log" kedua TC tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-6100` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
