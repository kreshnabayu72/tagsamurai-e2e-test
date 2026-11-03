---
id: TC-FA-COA-E2E-035-bulk-delete-campuran-akun-eligible-dihapus-akun-terekspor-atau-dipakai
title: "Bulk Delete Campuran: Akun Eligible Dihapus, Akun Terekspor atau Dipakai Asset Class Dilewati"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-69
  - TC-FA-COA-115
  - TC-FA-COA-132
coverage:
  web: automated
---

# Bulk Delete Campuran: Akun Eligible Dihapus, Akun Terekspor atau Dipakai Asset Class Dilewati

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Active, pernah diekspor (Last Used in Journal Aug 2026); dilewati, tidak berubah | TC-69, TC-115 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1, belum pernah diekspor; dilewati, tidak berubah | TC-132 |
  | P60 | `4-7105 – Gain on Disposal – Mixed Delete Eligible` | Inactive, Used By 0, eligible; sekali pakai, dihapus | TC-69 |
  | P57 | `CAP-8104 – Capitalization Clearing – Mixed Delete Eligible` | Active, Used By 0, bukan nilai default company; sekali pakai, dihapus | TC-115 |
  | P114 | `CAP-8308 – Capitalization Clearing – Mixed Delete Inactive` | Inactive, Used By 0, belum pernah diekspor, bukan nilai default company; sekali pakai, dihapus | TC-132 |

- Riwayat ekspor P2 dan Asset Class pemakai P6 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-69: Bulk Delete campuran: akun eligible dihapus, akun terekspor dilewati dengan keterangan

1. Ketik Search `6-2001`, tekan Enter
2. Centang akun P2 (`6-2001`)
3. Ganti isi kotak search dengan `4-7105`, tekan Enter
4. Centang akun P60 (`4-7105`)
5. Klik Bulk `Delete`
6. Verifikasi dialog "Delete Accounts" dengan "The following will be deleted:" memuat `• 4-7105 – Gain on Disposal – Mixed Delete Eligible`
7. Verifikasi "The following will be skipped:" memuat `• 6-2001 – Repairs & Maintenance Expense (last used in a journal)`
8. Verifikasi teks "Are you sure you want to continue?" dengan tombol `[Cancel]` dan `[Continue]`
9. Klik `[Continue]` pada D-09
10. Verifikasi toast "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."
11. Verifikasi seleksi di-reset dan Bulk Action Bar tidak tampil

### TC-FA-COA-115: Bulk Delete seleksi campuran: hanya akun eligible tunggal yang dihapus dengan dialog D-09

12. Ganti isi kotak search dengan `6-2001`, tekan Enter
13. Centang akun P2 (`6-2001`)
14. Ganti isi kotak search dengan `CAP-8104`, tekan Enter
15. Centang akun P57 (`CAP-8104`)
16. Klik Bulk `Delete`
17. Verifikasi dialog D-09 "Delete Accounts" untuk seleksi campuran
18. Tunggu toast lama hilang otomatis
19. Klik `[Continue]` pada D-09
20. Verifikasi toast parsial "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."
21. Verifikasi akun P57 (`CAP-8104`) tidak lagi tampil di tabel
22. Ganti isi kotak search dengan `6-2001`, tekan Enter
23. Verifikasi akun P2 tetap tampil di tabel

### TC-FA-COA-132: Bulk Delete campuran: akun eligible dihapus, akun yang dipakai Asset Class dilewati dengan D-09

24. Ganti isi kotak search dengan `CAP-8308`, tekan Enter
25. Centang akun P114 (`CAP-8308`)
26. Ganti isi kotak search dengan `5-6002`, tekan Enter
27. Centang akun P6 (`5-6002`)
28. Klik Bulk `Delete`
29. Verifikasi "The following will be deleted:" memuat `• CAP-8308 – Capitalization Clearing – Mixed Delete Inactive`
30. Verifikasi "The following will be skipped:" memuat `• 5-6002 – Depreciation Expense – Warehouse (still in use)`
31. Verifikasi tombol `[Cancel]` dan `[Continue]`
32. Tunggu toast lama hilang otomatis
33. Klik `[Continue]` pada D-09
34. Verifikasi toast "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."

## Notes

- Spec 34 langkah. Seluruh TC menghapus data, sehingga spec ini adalah kasus akhir kelompok Bulk Delete (S-10).
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Tunggu toast lama hilang otomatis" (langkah 18, 32) karena teks toast sama dengan TC sebelumnya; seleksi di-reset otomatis oleh hasil parsial sehingga tidak perlu langkah pembersih antar-TC.
- Asersi langkah 21 memakai toast langkah 20 sebagai anchor (8b.2).
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition TC-69 (P60 terhapus, P2 tetap tanpa log, log L-04 hanya P60) dan TC-132 (P114 terhapus dengan log L-04, P6 tetap tanpa log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-8308` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
