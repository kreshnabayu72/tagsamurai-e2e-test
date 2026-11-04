---
id: TC-FA-COA-E2E-038-used-by-berubah-saat-asset-class-memakai-atau-melepas-akun
title: "Used By Berubah Saat Asset Class Memakai atau Melepas Akun"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-157
  - TC-FA-COA-158
coverage:
  web: automated
---

# Used By Berubah Saat Asset Class Memakai atau Melepas Akun

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P14 | `5-6950 – Depreciation Expense – Plant` | Active, Used By 0, belum pernah diekspor, bukan nilai default company | TC-157, TC-158 |
  | P15 | `5-6960 – Depreciation Expense – Spare` | Active, Used By 1 (Asset Class `Mobile Equipment`, field Depreciation Expense) | TC-157, TC-158 |

- Asset Class `Mobile Equipment` Active dengan 2 Asset Name yang memetakan P15 pada field Depreciation Expense disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pemetaan dipulihkan ke P15 oleh langkah 30 dan 31 spec ini dan oleh hook `after` sebagai cadangan.
- Tabel akun dan tabel Asset Class dapat memuat lebih dari satu halaman; baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-157: Asset Class mulai memakai akun: Used By akun bertambah dan Deactivate akun ditolak

1. Ketik Search `Fixture.settingsChartOfAccounts.p14.code`, tekan Enter
2. Verifikasi nilai Used By akun P14 adalah `0`
3. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p15.code`, tekan Enter
4. Verifikasi nilai Used By akun P15 adalah `1`
5. Buka Settings > Accounting > Asset Class
6. Ketik Search `Mobile Equipment`, tekan Enter
7. Klik Class Code `Mobile Equipment`
8. Buka tab Accounts
9. Pilih `Fixture.settingsChartOfAccounts.p14.code – Fixture.settingsChartOfAccounts.p14.name` pada field Depreciation Expense
10. Klik `[Save]`
11. Tunggu aksi selesai
12. Kembali ke tab Chart of Accounts
13. Ketik Search `Fixture.settingsChartOfAccounts.p14.code`, tekan Enter
14. Verifikasi nilai Used By akun P14 adalah `1`
15. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p15.code`, tekan Enter
16. Verifikasi nilai Used By akun P15 adalah `0`
17. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p14.code`, tekan Enter
18. Klik angka Used By akun P14
19. Verifikasi popup "Used By" memuat teks polos satu baris `Fixture.settingsChartOfAccounts.p14.code – Fixture.settingsChartOfAccounts.p14.name (1)` di bawah judul
20. Verifikasi popup memuat bullet `• Mobile Equipment — 2 Asset Names`
21. Klik `[✕]` pada popup Used By
22. Klik switch Status akun P14
23. Verifikasi dialog "Cannot Deactivate Account" dengan bullet `• Fixture.settingsChartOfAccounts.p14.code – Fixture.settingsChartOfAccounts.p14.name` dan teks "This account is used by 1 Asset Class and cannot be deactivated."
24. Klik `[OK]`
25. Verifikasi switch Status P14 tetap Active

### TC-FA-COA-158: Asset Class melepas akun: Used By akun berkurang dan Deactivate serta Delete kembali diizinkan

26. Buka Settings > Accounting > Asset Class
27. Ketik Search `Mobile Equipment`, tekan Enter
28. Klik Class Code `Mobile Equipment`
29. Buka tab Accounts
30. Pilih `Fixture.settingsChartOfAccounts.p15.code – Fixture.settingsChartOfAccounts.p15.name` pada field Depreciation Expense
31. Klik `[Save]`
32. Tunggu aksi selesai
33. Kembali ke tab Chart of Accounts
34. Ketik Search `Fixture.settingsChartOfAccounts.p14.code`, tekan Enter
35. Verifikasi nilai Used By akun P14 adalah `0`
36. Verifikasi nilai Used By akun P14 berupa teks biasa (bukan link)
37. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p15.code`, tekan Enter
38. Verifikasi nilai Used By akun P15 adalah `1`
39. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p14.code`, tekan Enter
40. Klik switch Status akun P14
41. Verifikasi dialog "Deactivate Account" (D-01) dengan bullet `• Fixture.settingsChartOfAccounts.p14.code – Fixture.settingsChartOfAccounts.p14.name`, bukan dialog blok D-04
42. Klik `[Cancel]`
43. Klik row action `Delete` pada akun P14
44. Verifikasi dialog "Delete Account" (D-07) dengan bullet `• Fixture.settingsChartOfAccounts.p14.code – Fixture.settingsChartOfAccounts.p14.name`, bukan dialog blok D-06
45. Klik `[Cancel]`
46. Verifikasi akun P14 tetap Active
47. Verifikasi akun P14 ada di tabel

## Notes

- Spec 47 langkah, di atas ambang 35 langkah. Alasan: TC-158 bergantung pada keadaan akhir TC-157 (S-04), sehingga keduanya berurutan dalam satu spec; tiap TC memuat perjalanan ke modul Asset Class dan kembali ke Chart of Accounts.
- Langkah penghubung (S-03, R-16): Search Account Code dan Search Asset Class untuk membuka baris target (langkah 1, 3, 6, 13, 15, 17, 27, 34, 37, 39); "Tunggu aksi selesai" (langkah 11, 32) sebelum pindah surface; langkah 5 dan 26 membuka modul Asset Class, dan langkah 12 dan 33 kembali ke modul asal (S-14); `[✕]` popup (langkah 21) dan `[OK]` (langkah 24) menutup popup dan dialog blok.
- Pemetaan Asset Class `Mobile Equipment` dipulihkan ke P15 oleh langkah 30 sampai 31 (Post Condition TC-158 menyatakan kondisi awal pemetaan dipulihkan).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-157 butir b (tidak ada log L-03 pada P14) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC tidak menyebut Search pada tabel Asset Class; langkah 6 dan 27 ditambahkan sebagai penghubung bila tabel berhalaman banyak.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `5-6950` adalah data Pre-setup di-seed tim FE/BE dan Account Code dibatasi 15 karakter.
