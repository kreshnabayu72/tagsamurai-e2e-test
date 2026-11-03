---
id: TC-FA-COA-E2E-034-blokir-bulk-delete-seluruh-seleksi-diblokir
title: "Blokir Bulk Delete: Seluruh Seleksi Diblokir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-70
  - TC-FA-COA-131
coverage:
  web: automated
---

# Blokir Bulk Delete: Seluruh Seleksi Diblokir

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca dan tidak berubah karena Bulk Delete selalu diblokir guard (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Active, pernah diekspor (Last Used in Journal Aug 2026) | TC-70 |
  | P4 | `1-1002 – Equipment – Legacy Code` | Inactive, pernah diekspor (Last Used in Journal Mar 2025) | TC-70 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1, belum pernah diekspor | TC-131 |
  | P7 | `4-7002 – Gain and Loss on Disposal` | Active, Used By 2, belum pernah diekspor | TC-131 |

- Riwayat ekspor P2 dan P4 serta Asset Class pemakai P6 dan P7 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-70: Bulk Delete seluruh akun diblokir karena pernah diekspor: dialog D-12 tanpa perubahan data

1. Ketik Search `6-2001`, tekan Enter
2. Centang akun P2 (`6-2001`)
3. Ganti isi kotak search dengan `1-1002`, tekan Enter
4. Centang akun P4 (`1-1002`)
5. Klik Bulk `Delete`
6. Verifikasi dialog "Cannot Delete Accounts" dengan "The following were last used in a journal and cannot be deleted:" memuat `• 6-2001 – Repairs & Maintenance Expense` dan `• 1-1002 – Equipment – Legacy Code`
7. Verifikasi tombol `[OK]`
8. Klik `[OK]`
9. Verifikasi seleksi tetap dipertahankan

### TC-FA-COA-131: Bulk Delete seluruh akun terpilih yang dipakai Asset Class menampilkan D-12

10. Muat ulang halaman (F5)
11. Ketik Search `5-6002`, tekan Enter
12. Centang akun P6 (`5-6002`)
13. Ganti isi kotak search dengan `4-7002`, tekan Enter
14. Centang akun P7 (`4-7002`)
15. Klik Bulk `Delete`
16. Verifikasi dialog "Cannot Delete Accounts" dengan "The following are in use and cannot be deleted:" memuat `• 5-6002 – Depreciation Expense – Warehouse` dan `• 4-7002 – Gain and Loss on Disposal`
17. Verifikasi bagian "The following were last used in a journal and cannot be deleted:" tidak tampil
18. Verifikasi tombol `[OK]`
19. Klik `[OK]`
20. Verifikasi seleksi dipertahankan

## Notes

- Dua TC default company (TC-FA-COA-168, 355) ada di spec 089.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Muat ulang halaman (F5)" (langkah 10) membersihkan seleksi dan Search sebelum TC berikutnya (S-09); `[OK]` pada langkah 8 dan 19 mengikuti Expected TC (seleksi dipertahankan setelah `[OK]`).
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition TC-131 (tidak ada data berubah, tidak ada log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; data Pre-setup di-seed tim FE/BE dan Account Code dibatasi 15 karakter.
