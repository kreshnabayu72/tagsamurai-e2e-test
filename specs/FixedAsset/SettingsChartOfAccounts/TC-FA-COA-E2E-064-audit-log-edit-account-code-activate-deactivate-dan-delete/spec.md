---
id: TC-FA-COA-E2E-064-audit-log-edit-account-code-activate-deactivate-dan-delete
title: "Audit Log: Edit Account Code, Activate Deactivate, dan Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-93
  - TC-FA-COA-94
  - TC-FA-COA-95
coverage:
  web: automated
---

# Audit Log: Edit Account Code, Activate Deactivate, dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Akun Pre-setup sekali pakai (P62, P64, dan P116 milik spec ini; identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; kunci ditetapkan tim FE; fixture belum ada):

  | Akun | Account Code | Account Name | Kondisi | Aksi |
  |---|---|---|---|---|
  | P62 | `5-6104` | Depreciation Expense – Edit Code Log | Active, Used By 0, Last Used in Journal kosong | Account Code diubah menjadi `5-6011` (TC-93) |
  | P64 | `4-7107` | Gain on Disposal – Log Toggle | Inactive, Used By 0, Last Used in Journal kosong | Activate lalu Deactivate (TC-94); status akhir kembali Inactive |
  | P116 | `CAP-8110` | Capitalization Clearing – Delete Log | Active, Used By 0, Last Used in Journal kosong, belum pernah diekspor, bukan nilai default company di Settings > Accounting > Preferences, Function Capitalization Offset | Delete (TC-95) |

  Kode tujuan `5-6011` hanya dipakai spec ini (spec 073 memakai kode tujuan lain pada akun P69); spec ini memulihkan P62 ke `5-6104` pada langkah 56 sampai 58 sehingga `5-6011` bebas kembali.
- Pengecualian A-18 (S-06 dan S-12; butir "Pengecualian A-18" di `suite.md`): akun sekali pakai P62, P64, dan P116 dengan Account Code literal tanpa suffix `{runId}` (termasuk kode tujuan `5-6011`). Seed idempotent dan pemulihan ke keadaan awal dijalankan di hook `before` dan `after` spec ini (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: membaca jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS lewat BE sebelum aksi (8b.10, S-12); disediakan tim FE/BE. Baseline dicatat ulang sebelum aksi pemicu tiap TC.
- State yang diubah spec: akun P62 diubah lalu dipulihkan (langkah 56 sampai 58), P64 diubah dua kali dan kembali Inactive, P116 dihapus (dipulihkan fixture di `before` dan `after`); audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-93: Edit Account Code tercatat di tiga surface

1. Catat jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS sebagai baseline TC-93
2. Ketik Search `Fixture.settingsChartOfAccounts.p62.code`, tekan Enter
3. Klik row action `Edit` pada baris akun P62
4. Ubah Account Code menjadi `5-6011`
5. Klik `[Save]`
6. Tunggu aksi selesai (modal Edit Account tertutup)
7. Klik ikon Changelog di toolbar
8. Verifikasi jumlah entri Changelog bertambah satu dari baseline
9. Verifikasi entri teratas: Field Account Code, Old Value `Fixture.settingsChartOfAccounts.p62.code`, New Value `5-6011`
10. Verifikasi kolom Account Code pada seluruh baris entri dari Save tersebut berisi `5-6011`
11. Tutup modal Changelog dengan ikon ✕
12. Buka System Log pada Detail User aktor
13. Verifikasi jumlah entri System Log bertambah satu dari baseline
14. Verifikasi Name pada entri teratas System Log adalah `5-6011`
15. Buka Activity Log FAMS
16. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
17. Verifikasi Name pada entri teratas Activity Log adalah `5-6011`

### TC-FA-COA-94: Activate dan Deactivate dicatat sebagai Edit atas Status

18. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
19. Catat jumlah entri Changelog, System Log, dan Activity Log sebagai baseline TC-94
20. Ketik Search `Fixture.settingsChartOfAccounts.p64.code`, tekan Enter
21. Klik switch Status baris akun P64
22. Klik `[Activate]` pada dialog "Activate Account"
23. Tunggu aksi selesai (dialog tertutup dan switch berubah)
24. Klik switch Status baris akun P64
25. Klik `[Deactivate]` pada dialog "Deactivate Account"
26. Tunggu aksi selesai (dialog tertutup dan switch berubah)
27. Klik ikon Changelog di toolbar
28. Verifikasi jumlah entri Changelog bertambah dua dari baseline
29. Verifikasi dua entri teratas (tanpa mengandalkan urutan di antaranya) dengan Action Edit, Field Status, dengan Old Value dan New Value `Inactive` ke `Active` dan `Active` ke `Inactive`
30. Verifikasi Modified By pada kedua entri adalah user aktor
31. Tutup modal Changelog dengan ikon ✕
32. Buka System Log pada Detail User aktor
33. Verifikasi jumlah entri System Log bertambah dua dari baseline
34. Verifikasi dua entri teratas System Log: Object `Chart of Accounts`, Name `Fixture.settingsChartOfAccounts.p64.code`, Field Status, Old Value dan New Value `Inactive` ke `Active` dan `Active` ke `Inactive`
35. Buka Activity Log FAMS
36. Verifikasi jumlah entri Activity Log bertambah dua dari baseline
37. Verifikasi dua entri teratas Activity Log: Object `Chart of Accounts`, Name `Fixture.settingsChartOfAccounts.p64.code`, Field Status, Old Value dan New Value yang sama, Modified By = user aktor

### TC-FA-COA-95: Delete tercatat satu baris dan Account Code tetap terbaca

38. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
39. Catat jumlah entri Changelog, System Log, dan Activity Log sebagai baseline TC-95
40. Ketik Search `Fixture.settingsChartOfAccounts.p116.code`, tekan Enter
41. Klik row action `Delete` pada baris akun P116 sehingga dialog D-07 terbuka
42. Klik `[Delete]`
43. Tunggu aksi selesai (dialog tertutup)
44. Klik ikon Changelog di toolbar
45. Verifikasi jumlah entri Changelog bertambah satu dari baseline
46. Verifikasi entri teratas: Action Delete, Account Code `Fixture.settingsChartOfAccounts.p116.code`, Field Account Code, Old Value `Fixture.settingsChartOfAccounts.p116.code`, New Value `—`
47. Tutup modal Changelog dengan ikon ✕
48. Buka Activity Log FAMS
49. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
50. Verifikasi entri teratas Activity Log menampilkan Object `Chart of Accounts` dan Name `Fixture.settingsChartOfAccounts.p116.code`
51. Buka System Log pada Detail User aktor
52. Verifikasi jumlah entri System Log bertambah satu dari baseline
53. Verifikasi satu baris System Log: Object `Chart of Accounts`, Name `Fixture.settingsChartOfAccounts.p116.code`, Field Account Code, Old Value `Fixture.settingsChartOfAccounts.p116.code`, New Value `—`

### Pemulihan

54. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
55. Ketik Search `5-6011`, tekan Enter
56. Klik row action `Edit` pada baris akun P62
57. Ubah Account Code menjadi `Fixture.settingsChartOfAccounts.p62.code`
58. Klik `[Save]`
59. Tunggu aksi selesai (modal Edit Account tertutup)
60. Klik `(←)` pada kotak Search

## Notes

- Alasan spec di atas sekitar 35 langkah (60 langkah): tiga blok memakai satu halaman dan satu kelas harness (pencatatan log tiga surface); sebagian besar langkah adalah blok baca-log berpola (buka surface, baca selisih, `Verifikasi` kolom) dan Search untuk membuka baris target (8b.13); tiap TC memakai akun dan baseline sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna. Aksi menghapus data berada di blok terakhir (S-10).
- Prinsip 1: Edit Account Code, Activate dan Deactivate, serta Delete berada dalam satu spec karena objek ujinya satu topik, pencatatan log di tiga surface, bukan fungsi aksinya; tiap TC memakai akun sekali pakai dan baseline sendiri sehingga tidak butuh variasi data target, dan blok Delete ada di akhir (S-10). Urutan blok TC (TC-93, TC-94, TC-95) sama dengan `sourceTc`.
- Cara baca entri baru (S-14): setelah selisih jumlah dari baseline dibuktikan, entri baru dibaca pada baris teratas urutan default Date Newest First. Pada TC-94 dua entri berada dalam menit yang sama; spec mengasersi himpunan dua entri teratas tanpa urutan di antaranya.
- Langkah penghubung (S-03): langkah 18, 38, dan 54 (navigasi kembali ke modul asal setelah membaca log, S-14), langkah 2, 20, 40, dan 55 (Search untuk menemukan baris target, R-16), langkah 6, 23, 26, 43, dan 59 (menunggu aksi selesai sebelum membuka log atau pindah langkah), langkah 11, 31, dan 47 (menutup modal), langkah 60 (Search dikosongkan).
- Langkah 56 sampai 58 memulihkan Account Code P62 ke nilai awal (pemulihan state, S-03 dan S-09); entri log pemulihan bertambah permanen dan tidak diasersi.
- Asersi "tidak ada pencatatan/log" tidak ada di spec ini (S-05). Pengecekan isolasi log per aktor tidak dilakukan.
- A-18: akun sekali pakai P62 (TC-93), P64 (TC-94), dan P116 (TC-95) dengan Account Code literal tanpa suffix `{runId}`; seed idempotent dipulihkan di hook `before` dan `after`. Kode tujuan `5-6011` (TC-93) hanya dipakai spec ini; spec ini memulihkan P62 ke `5-6104` sehingga kode itu bebas kembali.
- Temuan untuk QA:
  - TC-93 Post Condition a (label akun di Asset Class, segmen Custom Asset ID, dan Preferences memakai Account Code terbaru; Asset ID yang sudah terbit tidak berubah) tidak memiliki langkah observasi di TC dan tidak diasersi.
  - TC-93 butir b ("seluruh baris L-02 dari Save tersebut") dibaca sebagai baris dari satu Save; karena hanya Account Code yang diubah, selisihnya satu baris (langkah 8 dan 10).
  - TC-94 tidak menyebut toast atau dialog; konfirmasi memakai `[Activate]` dan `[Deactivate]` seperti TC-46 dan TC-50.
  - TC-93, TC-94, dan TC-95 tidak menyebut jalur menu menuju System Log pada Detail User aktor dan Activity Log FAMS; spec mengikuti penamaan TC.
