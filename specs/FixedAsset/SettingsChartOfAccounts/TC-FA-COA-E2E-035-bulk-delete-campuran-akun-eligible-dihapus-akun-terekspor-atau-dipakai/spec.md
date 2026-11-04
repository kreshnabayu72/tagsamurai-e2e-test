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
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Active, pernah diekspor (Last Used in Journal Aug 2026); dilewati, tidak berubah | TC-69, TC-115 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1, belum pernah diekspor; dilewati, tidak berubah | TC-132 |
  | P60 | `4-7105 – Gain on Disposal – Mixed Delete Eligible` | Inactive, Used By 0, eligible; sekali pakai, dihapus | TC-69 |
  | P57 | `CAP-8104 – Capitalization Clearing – Mixed Delete Eligible` | Active, Used By 0, bukan nilai default company; sekali pakai, dihapus | TC-115 |
  | P114 | `CAP-8308 – Capitalization Clearing – Mixed Delete Inactive` | Inactive, Used By 0, belum pernah diekspor, bukan nilai default company; sekali pakai, dihapus | TC-132 |

- Riwayat ekspor P2 dan Asset Class pemakai P6 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Pengecualian A-18 (S-06 dan S-12; butir "Pengecualian A-18" di `suite.md`): akun sekali pakai P60, P57, dan P114 menjadi target hapus dengan Account Code literal tanpa suffix `{runId}`. Seed idempotent dan pemulihan ke keadaan awal dijalankan di hook `before` dan `after` spec ini (kemampuan disediakan tim FE/BE); akun dan Code itu hanya dipakai spec ini.
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-69: Bulk Delete campuran: akun eligible dihapus, akun terekspor dilewati dengan keterangan

1. Ketik Search `Fixture.settingsChartOfAccounts.p2.code`, tekan Enter
2. Centang akun P2 (`Fixture.settingsChartOfAccounts.p2.code`)
3. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p60.code`, tekan Enter
4. Centang akun P60 (`Fixture.settingsChartOfAccounts.p60.code`)
5. Klik Bulk `Delete`
6. Verifikasi dialog "Delete Accounts" dengan "The following will be deleted:" memuat `• Fixture.settingsChartOfAccounts.p60.code – Fixture.settingsChartOfAccounts.p60.name`
7. Verifikasi "The following will be skipped:" memuat `• Fixture.settingsChartOfAccounts.p2.code – Fixture.settingsChartOfAccounts.p2.name (last used in a journal)`
8. Verifikasi teks "Are you sure you want to continue?" dengan tombol `[Cancel]` dan `[Continue]`
9. Klik `[Continue]` pada D-09
10. Verifikasi toast "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."
11. Verifikasi seleksi di-reset
12. Verifikasi Bulk Action Bar tidak tampil

### TC-FA-COA-115: Bulk Delete seleksi campuran: hanya akun eligible tunggal yang dihapus dengan dialog D-09

13. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p2.code`, tekan Enter
14. Centang akun P2 (`Fixture.settingsChartOfAccounts.p2.code`)
15. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p57.code`, tekan Enter
16. Centang akun P57 (`Fixture.settingsChartOfAccounts.p57.code`)
17. Klik Bulk `Delete`
18. Verifikasi dialog D-09 "Delete Accounts" untuk seleksi campuran
19. Tunggu toast lama hilang otomatis
20. Klik `[Continue]` pada D-09
21. Verifikasi toast parsial "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."
22. Verifikasi akun P57 (`Fixture.settingsChartOfAccounts.p57.code`) tidak lagi tampil di tabel
23. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p2.code`, tekan Enter
24. Verifikasi akun P2 tetap tampil di tabel

### TC-FA-COA-132: Bulk Delete campuran: akun eligible dihapus, akun yang dipakai Asset Class dilewati dengan D-09

25. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p114.code`, tekan Enter
26. Centang akun P114 (`Fixture.settingsChartOfAccounts.p114.code`)
27. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p6.code`, tekan Enter
28. Centang akun P6 (`Fixture.settingsChartOfAccounts.p6.code`)
29. Klik Bulk `Delete`
30. Verifikasi "The following will be deleted:" memuat `• Fixture.settingsChartOfAccounts.p114.code – Fixture.settingsChartOfAccounts.p114.name`
31. Verifikasi "The following will be skipped:" memuat `• Fixture.settingsChartOfAccounts.p6.code – Fixture.settingsChartOfAccounts.p6.name (still in use)`
32. Verifikasi tombol `[Cancel]` dan `[Continue]`
33. Tunggu toast lama hilang otomatis
34. Klik `[Continue]` pada D-09
35. Verifikasi toast "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)."

## Notes

- Spec 35 langkah. Seluruh TC menghapus data, sehingga spec ini adalah kasus akhir kelompok Bulk Delete (S-10).
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Tunggu toast lama hilang otomatis" (langkah 19, 33) karena teks toast sama dengan TC sebelumnya; seleksi di-reset otomatis oleh hasil parsial sehingga tidak perlu langkah pembersih antar-TC.
- Asersi langkah 22 memakai toast langkah 21 sebagai anchor (8b.2).
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- A-18: akun sekali pakai P60 (TC-69), P57 (TC-115), dan P114 (TC-132) dihapus spec ini dengan Account Code literal tanpa suffix `{runId}` (batas 15 karakter); akun dan Code itu hanya dipakai spec ini, dan seed idempotent dipulihkan di hook `before` dan `after`.
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition TC-69 (P60 terhapus, P2 tetap tanpa log, log L-04 hanya P60) dan TC-132 (P114 terhapus dengan log L-04, P6 tetap tanpa log) tidak punya langkah observasi di TC sehingga tidak diasersi.
