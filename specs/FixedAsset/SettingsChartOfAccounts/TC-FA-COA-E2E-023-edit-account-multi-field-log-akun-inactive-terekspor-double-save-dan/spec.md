---
id: TC-FA-COA-E2E-023-edit-account-multi-field-log-akun-inactive-terekspor-double-save-dan
title: "Edit Account: Multi-Field Log, Akun Inactive Terekspor, Double Save, dan Saving State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-145
  - TC-FA-COA-283
  - TC-FA-COA-290
  - TC-FA-COA-365
coverage:
  web: automated
---

# Edit Account: Multi-Field Log, Akun Inactive Terekspor, Double Save, dan Saving State

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE). Semua akun sekali pakai:

  | Kode | Akun | Kondisi awal | Dipakai |
  |---|---|---|---|
  | P27 | `CAP-6800 – Capitalization Clearing – Edit Function` | Active, Used By 0, belum pernah diekspor, Function Depreciation Expense (kondisi setelah perubahan Function pada TC-144; disediakan lewat seeding, dipakai sebagai precondition TC-145, tidak diasersi) | TC-145 |
  | P82 | `CAP-8212 – Capitalization Clearing – Double Save`, Function Capitalization Offset | Active, Used By 0, Last Used in Journal kosong | TC-283 |
  | P115 | `CAP-8309 – Capitalization Clearing – Delayed Edit`, Function Capitalization Offset | Active, Used By 0, Last Used in Journal kosong | TC-290 |
  | P106 | `1-1103 – Equipment – Inactive Edit`, Function Asset Cost | Inactive, Used By 0, Last Used in Journal `Mar 2025` | TC-365 |

- Akun sekali pakai diubah spec ini; kondisi awalnya (termasuk Function P27 Depreciation Expense) disediakan ulang (seed/pemulihan) oleh tim FE/BE di hook `before` dan `after`, termasuk Last Updated. Nilai Account Code literal dengan batas 15 karakter tidak memakai suffix `{runId}`.
- Nilai `[Month Year]` pada tooltip TC-365 adalah `Mar 2025` (Last Used in Journal P106).
- Kemampuan teknis: kemampuan baca jumlah entri Changelog sebelum aksi (TC-145, TC-283), disediakan tim FE/BE (8b.10); `Spectra.intercept()` untuk menunda respons request Edit (TC-290) di atas backend nyata, endpoint ditetapkan tim FE sesuai PRD/LLD, intercept dilepas pada langkah "Lepas tahanan respons".
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-145: Edit Account Code, Account Name, dan Account Function sekaligus menulis satu baris log per field

1. Ketik Search `CAP-6800`, tekan Enter
2. Buka Changelog, catat jumlah entri sebagai baseline, lalu tutup Changelog
3. Klik row action `Edit` pada akun P27 (`CAP-6800`)
4. Ubah Account Code menjadi `CAP-6810`, Account Name menjadi `Capitalization Clearing – Edit Multi`, dan Account Function menjadi Asset Cost
5. Klik `[Save]`
6. Verifikasi toast "Success, account has been updated."
7. Buka Changelog
8. Verifikasi jumlah entri Changelog bertambah tepat tiga dari baseline langkah 2, semuanya Action Edit
9. Verifikasi baris Field Account Code Old Value `CAP-6800`, New Value `CAP-6810`
10. Verifikasi baris Field Account Name Old Value `Capitalization Clearing – Edit Function`, New Value `Capitalization Clearing – Edit Multi`
11. Verifikasi baris Field Account Function Old Value `Depreciation Expense`, New Value `Asset Cost`
12. Verifikasi kolom Account Code ketiga baris berisi `CAP-6810`
13. Verifikasi tidak ada baris Field Status di antara tiga baris baru
14. Tutup Changelog

### TC-FA-COA-283: Klik ganda `[Save]` pada Edit menghasilkan satu perubahan

15. Ganti isi kotak search dengan `CAP-8212`, tekan Enter
16. Tunggu toast lama hilang otomatis
17. Buka Changelog, catat jumlah entri sebagai baseline, lalu tutup Changelog
18. Klik row action `Edit` pada akun P82 (`CAP-8212`)
19. Ganti isi Account Name dengan `Capitalization Clearing – Double Save Edit`
20. Klik `[Save]` dua kali cepat
21. Verifikasi hanya satu toast "Success, account has been updated."
22. Buka Changelog
23. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline langkah 17 sehingga satu perubahan tersimpan
24. Tutup Changelog

### TC-FA-COA-290: Tombol `[Save]` menampilkan Saving state selama request Edit tertunda

25. Ganti isi kotak search dengan `CAP-8309`, tekan Enter
26. Tunggu toast lama hilang otomatis
27. Klik row action `Edit` pada akun P115 (`CAP-8309`)
28. Ganti isi Account Name dengan `Capitalization Clearing – Saving State`
29. Tunda respons Edit (network delay)
30. Klik `[Save]`
31. Verifikasi tombol `[Save]` menampilkan Saving state (loading)
32. Klik `[Save]` lagi selama request tertunda
33. Verifikasi tombol `[Save]` tidak dapat diklik ulang: klik kedua tidak memicu request baru
34. Verifikasi `[Clear Field]` dan `[✕]` ter-disabled selama request berlangsung
35. Lepas tahanan respons
36. Tunggu aksi selesai

### TC-FA-COA-365: Edit akun Inactive yang pernah diekspor: Code dan Function Disabled, Name tersimpan, Status tetap Inactive

37. Ganti isi kotak search dengan `1-1103`, tekan Enter
38. Tunggu toast lama hilang otomatis
39. Klik row action `Edit` pada akun P106 (`1-1103`)
40. Verifikasi modal Edit Account terbuka
41. Arahkan kursor ke field Account Code
42. Verifikasi Account Code Disabled dengan tooltip "Account Code can't be changed because this account was used in a journal in Mar 2025. Create a new account if needed."
43. Arahkan kursor ke field Account Function
44. Verifikasi Account Function Disabled dengan tooltip "Account Function can't be changed because this account was used in a journal in Mar 2025."
45. Ganti isi Account Name dengan `Equipment – Inactive Edit Renamed`
46. Klik `[Save]`
47. Verifikasi toast "Success, account has been updated."
48. Verifikasi baris P106 menampilkan Account Name baru `Equipment – Inactive Edit Renamed`
49. Verifikasi Status P106 tetap Inactive (switch Off)

## Notes

- Spec 49 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik aksi (Edit sukses pada akun sekali pakai) dengan akun milik blok masing-masing; pola Search, baseline Changelog, buka Edit, ubah field, `[Save]`, lalu `Verifikasi` berulang per akun (8b.7), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka baris target (langkah 1, 15, 25, 37); "Tunggu toast lama hilang otomatis" (langkah 16, 26, 38) mencegah toast sebelumnya dengan teks sama lolos sebagai asersi (R-12); langkah 2 dan 17 mencatat baseline Changelog sebelum aksi pemicu TC-nya masing-masing (S-12); langkah 14 dan 24 menutup Changelog; langkah 36 menunggu aksi `[Save]` TC-290 selesai sebelum berpindah baris (8b.8).
- Precondition TC-145 "Function Depreciation Expense setelah TC-144" dipenuhi lewat seeding P27 (S-04): langkah TC-144 tidak disalin karena TC-144 ada di spec 022 dan spec ini tidak bergantung pada spec lain (S-06).
- Cara baca Changelog (S-14): tiga entri TC-145 jatuh di menit yang sama sehingga spec mengasersi himpunan baris teratas sebanyak selisih (langkah 8 sampai 13) tanpa mengandalkan urutan di antaranya.
- Urutan TC-290 (8b.5): Saving state (langkah 31) dan tombol disabled (langkah 33, 34) diasersi sebelum respons dilepas (langkah 35). Perubahan tersimpan sesudah respons diterima tidak diasersi karena hanya Post Condition tanpa langkah observasi.
- Asersi "satu perubahan tersimpan" TC-283 dibaca dari selisih jumlah entri Changelog (langkah 23), karena TC tidak memberi cara cek lain untuk butir b.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-145 (tiga entri L-02 di System Log dan Activity Log dengan Name `CAP-6810`), TC-283 (satu entri L-02 per surface), TC-290, dan TC-365 (satu baris log L-02) tidak punya langkah observasi di TC sehingga tidak diasersi di surface selain Changelog.
  - TC-145 mensyaratkan Function P27 Depreciation Expense "setelah TC-144", yaitu hasil TC lain; spec menyediakannya lewat seeding (mekanisme disediakan tim FE/BE).
