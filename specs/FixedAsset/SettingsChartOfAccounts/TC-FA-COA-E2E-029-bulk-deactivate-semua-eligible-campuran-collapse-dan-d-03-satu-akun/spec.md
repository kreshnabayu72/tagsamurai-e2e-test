---
id: TC-FA-COA-E2E-029-bulk-deactivate-semua-eligible-campuran-collapse-dan-d-03-satu-akun
title: "Bulk Deactivate: Semua Eligible, Campuran, Collapse, dan D-03 Satu Akun"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-55
  - TC-FA-COA-56
  - TC-FA-COA-299
  - TC-FA-COA-354
coverage:
  web: automated
---

# Bulk Deactivate: Semua Eligible, Campuran, Collapse, dan D-03 Satu Akun

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Active, Used By 0; hanya dibaca (dialog dibatalkan) | TC-299 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1 (Asset Class `Office Equipment`); hanya dibaca, tidak berubah | TC-354 |
  | P7 | `4-7002 – Gain and Loss on Disposal` | Active, Used By 2 (Asset Class `Delivery Vehicles` dan `Heavy Equipment`); hanya dibaca, tidak berubah | TC-354 |
  | P51 | `5-6102 – Depreciation Expense – Bulk Deactivate A` | Active, Used By 0; sekali pakai | TC-55 |
  | P52 | `CAP-8101 – Capitalization Clearing – Bulk Deactivate B` | Active, Used By 0; sekali pakai | TC-55 |
  | P53 | `5-6103 – Depreciation Expense – Mixed Deactivate` | Active, Used By 0; sekali pakai | TC-56 |
  | P54 | `4-7103 – Gain on Disposal – Mixed Skip` | Inactive, Used By 0; tidak berubah | TC-56 |
  | P105 | `5-6113 – Depreciation Expense – D-03 Single Eligible` | Active, Used By 0; sekali pakai | TC-354 |

- Pengecualian A-18 (butir "Data bersama" di `suite.md`): akun sekali pakai P51, P52, P53, dan P105 dinonaktifkan spec ini. Seed idempotent dan pemulihan ke kondisi awal (termasuk status dan Last Updated) dijalankan fixture backend (disediakan tim FE/BE) di hook `before` dan `after` spec ini; suite berjalan serial. P1, P6, P7, dan P54 hanya dibaca atau tidak berubah.
- P53 dan P54 hanya dipakai spec ini; kondisi awal: P53 Active dan P54 Inactive, Used By 0. Fixture memulihkan keduanya ke kondisi awal itu di hook `before` dan `after` spec ini.
- Asset Class pemakai P6 dan P7 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-55: Bulk Deactivate semua akun Active yang eligible memproses seluruh akun

1. Ketik Search `5-6102`, tekan Enter
2. Centang akun P51 (`5-6102`)
3. Ganti isi kotak search dengan `CAP-8101`, tekan Enter
4. Centang akun P52 (`CAP-8101`)
5. Klik Bulk `Deactivate`
6. Verifikasi dialog "Deactivate Accounts" (severity danger) dengan bullet `• 5-6102 – Depreciation Expense – Bulk Deactivate A`, `• CAP-8101 – Capitalization Clearing – Bulk Deactivate B`, dan teks "Are you sure you want to deactivate them?"
7. Klik `[Deactivate]` pada dialog D-02
8. Verifikasi toast "Success, account has been deactivated."
9. Verifikasi seleksi di-reset

### TC-FA-COA-56: Bulk Deactivate pada seleksi campuran hanya memproses akun Active

10. Ganti isi kotak search dengan `5-6103`, tekan Enter
11. Centang akun P53 (`5-6103`)
12. Ganti isi kotak search dengan `4-7103`, tekan Enter
13. Centang akun P54 (`4-7103`)
14. Klik Bulk `Deactivate`
15. Verifikasi dialog berisi hanya `• 5-6103 – Depreciation Expense – Mixed Deactivate` (akun Inactive tidak tampil)
16. Verifikasi dialog berjudul "Deactivate Account" (versi single D-01)
17. Tunggu toast lama hilang otomatis
18. Klik `[Deactivate]`
19. Verifikasi toast "Success, account has been deactivated."
20. Verifikasi akun P54 tetap Inactive

### TC-FA-COA-299: Bulk Deactivate tepat satu akun collapse ke dialog single D-01

21. Ganti isi kotak search dengan `5-6001`, tekan Enter
22. Centang akun P1 (`5-6001`)
23. Klik Bulk `Deactivate`
24. Verifikasi dialog "Deactivate Account" (single, D-01), bukan "Deactivate Accounts"
25. Verifikasi bullet `• 5-6001 – Depreciation Expense – Admin`
26. Klik `[Cancel]`
27. Hapus centang akun P1

### TC-FA-COA-354: Bulk Deactivate campuran yang meloloskan tepat satu akun tetap memakai D-03

28. Ganti isi kotak search dengan `5-6113`, tekan Enter
29. Centang akun P105 (`5-6113`)
30. Ganti isi kotak search dengan `5-6002`, tekan Enter
31. Centang akun P6 (`5-6002`)
32. Ganti isi kotak search dengan `4-7002`, tekan Enter
33. Centang akun P7 (`4-7002`)
34. Klik Bulk `Deactivate`
35. Verifikasi dialog berjudul "Deactivate Accounts" (D-03), bukan versi single "Deactivate Account" (D-01)
36. Verifikasi "The following will be deactivated:" memuat tepat satu bullet `• 5-6113 – Depreciation Expense – D-03 Single Eligible`
37. Verifikasi "The following are still in use and will be skipped:" memuat `• 5-6002 – Depreciation Expense – Warehouse (still in use)` dan `• 4-7002 – Gain and Loss on Disposal (still in use)`
38. Verifikasi teks "Are you sure you want to continue?" dengan tombol `[Cancel]` dan `[Continue]`
39. Klik `[Continue]`
40. Verifikasi toast "Success, account has been deactivated. Some items were skipped (still in use)."

## Notes

- Spec 40 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik aksi (Bulk Deactivate) dengan akun sekali pakai milik blok masing-masing; langkah Search dan Centang berulang per akun karena tabel berhalaman banyak; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; `[Cancel]` dan hapus centang P1 (langkah 26, 27) membersihkan seleksi sebelum TC-354 (S-09); "Tunggu toast lama hilang otomatis" (langkah 17) karena teks toast sama dengan TC-55.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- `A-18`: P51 dan P52 (TC-55), P53 (TC-56), dan P105 (TC-354) menjadi target ubah status sekali pakai; syarat A-18 dinyatakan di `## Prerequisites`. P53 dan P54 hanya dipakai spec ini.
- Pembagian TC lintas spec (S-05): TC-56 ada di spec ini dan di spec 103 (absence log). Spec ini mengasersi isi dialog, toast, dan status P54 tetap Inactive (langkah 15 sampai 20); klausa "Changelog, Activity Log, dan System Log tidak memuat baris untuk P54" beserta Langkah 4 TC (membuka ketiga surface log) diasersi di spec 103 dengan akun milik spec 103 dan baseline sendiri.
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition TC-55 dan TC-354 (status akun dan log L-03 per akun) dan TC-299 (data tidak berubah) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-8101` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
