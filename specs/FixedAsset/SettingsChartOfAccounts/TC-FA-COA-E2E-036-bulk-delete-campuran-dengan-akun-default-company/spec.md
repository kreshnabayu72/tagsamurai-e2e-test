---
id: TC-FA-COA-E2E-036-bulk-delete-campuran-dengan-akun-default-company
title: "Bulk Delete Campuran dengan Akun Default Company"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-169
  - TC-FA-COA-170
coverage:
  web: automated
---

# Bulk Delete Campuran dengan Akun Default Company

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P33 | `CAP-7020 – Capitalization Clearing – Bulk Delete Eligible` | Active, Used By 0, belum pernah diekspor, bukan nilai default company; sekali pakai, dihapus | TC-169 |
  | P30 | `CAP-7010 – Default Capitalization Offset – Main` | Active, Used By 0; Default Capitalization Offset (`SET-08`); dilewati, tidak berubah | TC-169 |
  | P34 | `CAP-7030 – Capitalization Clearing – Bulk Delete Mixed` | Active, Used By 0, belum pernah diekspor, bukan nilai default company; sekali pakai, dihapus | TC-170 |
  | P32 | `5-6970 – Depreciation Expense – Used Default` | Active, Used By 1 (Asset Class `Vehicles Fleet`); Found Asset Credit Account (`SET-09`); dilewati, tidak berubah | TC-170 |

- State global di Settings > Accounting > Preferences: hook `before` men-set `SET-08` = P30 dan `SET-09` = P32 lewat fixture BE; hook `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE.
- Asset Class pemakai P32 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-169: Bulk Delete campuran: akun eligible dihapus, akun default company dilewati pada kelompok default company D-09

1. Ketik Search `CAP-7020`, tekan Enter
2. Centang akun P33 (`CAP-7020`)
3. Ganti isi kotak search dengan `CAP-7010`, tekan Enter
4. Centang akun P30 (`CAP-7010`)
5. Klik Bulk `Delete`
6. Verifikasi dialog "Delete Accounts" (D-09) dengan "The following will be deleted:" memuat `• CAP-7020 – Capitalization Clearing – Bulk Delete Eligible`
7. Verifikasi kelompok default company diawali kalimat pengantar "The following are default company accounts and will be skipped:"
8. Verifikasi kelompok default company memuat `• CAP-7010 – Default Capitalization Offset – Main` diikuti "This account is the default company account for Default Capitalization Offset in Settings > Accounting > Preferences. Change the default there before deleting it."
9. Verifikasi teks "Are you sure you want to continue?" dengan tombol `[Cancel]` dan `[Continue]`
10. Klik `[Continue]`
11. Verifikasi toast "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."

### TC-FA-COA-170: Akun Asset Class sekaligus default company hanya tampil di kelompok Asset Class, tidak diulang di kelompok default company

12. Ganti isi kotak search dengan `CAP-7030`, tekan Enter
13. Centang akun P34 (`CAP-7030`)
14. Ganti isi kotak search dengan `5-6970`, tekan Enter
15. Centang akun P32 (`5-6970`)
16. Klik Bulk `Delete`
17. Verifikasi dialog "Delete Accounts" (D-09) dengan "The following will be deleted:" memuat `• CAP-7030 – Capitalization Clearing – Bulk Delete Mixed`
18. Verifikasi "The following will be skipped:" memuat `• 5-6970 – Depreciation Expense – Used Default (still in use)`
19. Verifikasi dua alasan berurutan di bawah bullet itu: kalimat cabang (a) "This account is used by 1 Asset Class and cannot be deleted." lalu satu kalimat cabang (b) "This account is the default company account for Found Asset Credit Account in Settings > Accounting > Preferences. Change the default there before deleting it."
20. Verifikasi kelompok default company tidak tampil, sehingga kalimat pengantar "The following are default company accounts and will be skipped:" tidak tampil
21. Tunggu toast lama hilang otomatis
22. Klik `[Continue]`
23. Verifikasi toast "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."

## Notes

- Spec ini menghapus data (P33 dan P34) sehingga menjadi kasus akhir kelompok Bulk Delete (S-10).
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Tunggu toast lama hilang otomatis" (langkah 21) karena teks toast sama dengan TC-169; seleksi di-reset otomatis oleh hasil parsial.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition TC-169 dan TC-170 (P33 dan P34 terhapus dengan log L-04, P30 dan P32 tetap tanpa log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-7020` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
