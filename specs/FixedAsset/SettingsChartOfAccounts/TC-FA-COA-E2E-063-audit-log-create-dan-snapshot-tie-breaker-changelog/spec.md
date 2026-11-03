---
id: TC-FA-COA-E2E-063-audit-log-create-dan-snapshot-tie-breaker-changelog
title: "Audit Log: Create dan Snapshot, Tie-Breaker Changelog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-92
  - TC-FA-COA-97
  - TC-FA-COA-235
coverage:
  web: automated
---

# Audit Log: Create dan Snapshot, Tie-Breaker Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Dinamis (dibuat spec lewat UI, Pre-setup P1 sudah ada):

  | Data | Account Code | Account Name | Function |
  |---|---|---|---|
  | D1 (TC-92, TC-97) | `5-6100` | `Depreciation Expense – Branch Jakarta {runId}-063`; setelah Edit di TC-97: `Depreciation Expense – Branch Jakarta Edit {runId}-063` | Depreciation Expense |
  | D8 (TC-235) | `5-6250`, lalu diubah menjadi `5-6251` | `Depreciation Expense – Branch Surabaya {runId}-063`, lalu `Depreciation Expense – Branch Surabaya Edit {runId}-063` | Depreciation Expense, lalu Asset Cost |

  Account Code tidak dapat bersuffix `{runId}` karena batas 15 karakter (lihat Temuan untuk QA); kode `5-6100`, `5-6250`, dan `5-6251` hanya dipakai spec ini. Hook `before` menghapus akun dengan kode itu bila tersisa dari run sebelumnya (R-13), dan hook `after` menghapus akun milik spec ini.
- Kemampuan teknis: membaca jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS lewat BE sebelum aksi (8b.10, S-12); disediakan tim FE/BE. Baseline dicatat ulang sebelum aksi pemicu tiap TC.
- Jam server dan jam browser sinkron (tidak ada asersi Date pada spec ini).
- State yang diubah spec: akun D1 dan D8 dibuat dan tetap Active; audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-92: Create tercatat di tiga surface (langkah Create menyalin TC-FA-COA-14)

1. Catat jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS sebagai baseline TC-92
2. Klik `+ Account`
3. Isi Account Code `5-6100`, Account Name `Depreciation Expense – Branch Jakarta {runId}-063`, dan Account Function Depreciation Expense
4. Klik `[Submit]`
5. Verifikasi toast "Success, account has been created."
6. Verifikasi modal tertutup
7. Verifikasi tabel kembali ke sort default
8. Verifikasi tabel memuat akun baru dengan baris di-highlight
9. Verifikasi highlight hilang tanpa interaksi pengguna
10. Verifikasi akun baru tampil dengan Status Active, Used By 0, dan Last Used in Journal kosong
11. Klik ikon Changelog di toolbar
12. Verifikasi jumlah entri Changelog bertambah satu dari baseline
13. Verifikasi entri teratas: Action Create, Account Code `5-6100`, Field Account Code, Old Value `—`, New Value `5-6100`
14. Tutup modal Changelog dengan ikon ✕
15. Buka System Log pada Detail User aktor
16. Verifikasi jumlah entri System Log bertambah satu dari baseline
17. Verifikasi entri teratas System Log: Object `Chart of Accounts`, Name `5-6100`
18. Buka Activity Log FAMS
19. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
20. Verifikasi Modified By pada entri teratas Activity Log adalah user aktor

### TC-FA-COA-97: Entri log lama tidak berubah setelah akun diubah namanya

21. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
22. Catat jumlah entri Changelog sebagai baseline TC-97
23. Ketik Search `5-6100`, tekan Enter
24. Klik row action `Edit` pada baris akun `5-6100`
25. Ubah Account Name menjadi `Depreciation Expense – Branch Jakarta Edit {runId}-063`
26. Klik `[Save]`
27. Tunggu aksi selesai (modal Edit Account tertutup)
28. Klik ikon Changelog di toolbar
29. Verifikasi jumlah entri Changelog bertambah satu dari baseline TC-97
30. Verifikasi entri baru teratas: Action Edit, Account Code `5-6100`, Field Account Name, Old Value `Depreciation Expense – Branch Jakarta {runId}-063`, New Value `Depreciation Expense – Branch Jakarta Edit {runId}-063`
31. Ketik Search `5-6100`, tekan Enter
32. Verifikasi entri lama tetap memuat Action Create, Account Code `5-6100`, Field Account Code, Old Value `—`, New Value `5-6100`
33. Klik `(←)` pada kotak Search
34. Tutup modal Changelog dengan ikon ✕

### TC-FA-COA-235: Tie-breaker Changelog

35. Catat jumlah entri Changelog sebagai baseline TC-235
36. Klik `+ Account`
37. Isi Account Code `5-6250`, Account Name `Depreciation Expense – Branch Surabaya {runId}-063`, dan Account Function Depreciation Expense
38. Klik `[Submit]`
39. Ketik Search `5-6250`, tekan Enter
40. Klik row action `Edit` pada baris akun `5-6250`
41. Ubah Account Code menjadi `5-6251`, Account Name menjadi `Depreciation Expense – Branch Surabaya Edit {runId}-063`, dan Account Function menjadi Asset Cost
42. Klik `[Save]`
43. Tunggu aksi selesai (modal Edit Account tertutup)
44. Klik ikon Changelog di toolbar tanpa mengubah sort (default Date Newest First)
45. Verifikasi jumlah entri Changelog bertambah empat dari baseline TC-235 (satu baris Create dan tiga baris Edit)
46. Verifikasi urutan default Date Newest First: baris kejadian Edit di atas baris kejadian Create
47. Verifikasi kejadian Edit (Action Edit, Account Code `5-6251`, timestamp sama) dari atas ke bawah: Field Account Function (Old Value `Depreciation Expense`, New Value `Asset Cost`); Field Account Name (Old Value `Depreciation Expense – Branch Surabaya {runId}-063`, New Value `Depreciation Expense – Branch Surabaya Edit {runId}-063`); Field Account Code (Old Value `5-6250`, New Value `5-6251`)
48. Verifikasi kejadian Create (Action Create, Account Code `5-6250`) hanya satu baris: Field Account Code (Old Value `—`, New Value `5-6250`)
49. Verifikasi dalam kejadian Edit, field yang ditulis paling akhir tampil paling atas dan urutan penulisan field mengikuti Account Code, Account Name, Account Function
50. Tutup modal Changelog dengan ikon ✕
51. Klik `(←)` pada kotak Search

## Notes

- Alasan spec di atas sekitar 35 langkah (51 langkah): tiga blok memakai satu halaman, satu kelas harness (pencatatan log tiga surface), dan tiap blok memuat baseline sendiri; sebagian besar langkah adalah Search untuk membuka baris target (8b.12) dan pembacaan tiga surface log (blok baca-log berpola); kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah Create TC-92 (langkah 2 sampai 10) menyalin langkah TC-FA-COA-14 (S-04); langkah TC-14 mengasersi toast, modal tertutup, tabel, highlight, dan nilai baris, yang di spec ini menjadi langkah 5 sampai 10.
- Cara baca entri baru (S-14): setelah selisih jumlah dari baseline dibuktikan, entri baru dibaca pada baris teratas urutan default Date Newest First. Pada TC-235 empat baris baru berada dalam menit yang sama; urutan di dalam kejadian Edit dan antara kejadian Edit dan Create adalah objek asersi TC itu sendiri (langkah 46 sampai 49).
- Langkah penghubung (S-03): langkah 21 (navigasi kembali ke modul asal setelah membaca System Log dan Activity Log, S-14), langkah 23, 31, dan 39 (Search untuk menemukan baris target, R-16), langkah 27 dan 43 (menunggu aksi selesai sebelum membuka log), langkah 33, 34, 50, dan 51 (menutup Search dan modal).
- Asersi "tidak ada pencatatan/log" tidak ada di spec ini (S-05).
- Pembersihan: akun D1 dan D8 (`5-6100` dan `5-6251`) dihapus di hook `after`; penghapusan itu menambah entri log permanen yang tidak diasersi.
- Temuan untuk QA:
  - Account Code Data Dinamis (D1 `5-6100`, D8 `5-6250` dan `5-6251`) tidak dapat bersuffix `{runId}` karena batas Account Code 15 karakter dengan whitelist huruf, angka, `-`, `_`, `.` (S-12); nilai literal TC dipakai, unik antar spec, dengan pembersihan di `before` dan `after`. Account Name bersuffix `{runId}-063`.
  - TC-92 Post Condition a ("Data dan tiga surface tercatat dalam satu transaksi") tidak memiliki langkah observasi di TC dan tidak diasersi.
  - TC-92 butir b dan c tidak menyebut jalur menu menuju System Log pada Detail User aktor dan Activity Log FAMS; spec mengikuti penamaan TC ("Detail User aktor", "Activity Log FAMS").
  - TC-92 butir c hanya menyebut Modified By pada Activity Log; Object dan Name Activity Log tidak diasersi pada TC-92.
  - TC-97 tidak menyebut nilai Account Name baru; spec memakai `Depreciation Expense – Branch Jakarta Edit {runId}-063`.
  - TC-92 dan TC-97 bergantung pada TC-14; langkah Create disalin ke spec ini (S-04).
