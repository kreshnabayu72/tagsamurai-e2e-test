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
- Data Dinamis (dibuat spec lewat UI):

  | Data | Account Code | Account Name | Function |
  |---|---|---|---|
  | D14 (TC-92) | `5-6160` | `Depreciation Expense – Create Log {runId}-063` | Depreciation Expense |
  | D15 (TC-97) | `5-6170` | `Depreciation Expense – Snapshot Log {runId}-063`; setelah Edit: `Depreciation Expense – Snapshot Log Edit {runId}-063` | Depreciation Expense |
  | D8 (TC-235) | `5-6250`, lalu diubah menjadi `5-6251` | `Depreciation Expense – Branch Surabaya {runId}-063`, lalu `Depreciation Expense – Branch Surabaya Edit {runId}-063` | Depreciation Expense, lalu Asset Cost |

  Account Code tidak dapat bersuffix `{runId}` karena batas 15 karakter (lihat Temuan untuk QA); kode `5-6160`, `5-6170`, `5-6250`, dan `5-6251` dibersihkan oleh hook spec ini. Hook `before` menghapus akun dengan kode itu bila tersisa dari run sebelumnya (R-13), dan hook `after` menghapus akun milik spec ini.
- Pengecualian A-18 (S-06 dan S-12; butir "Pengecualian A-18" di `suite.md`): Account Code literal `5-6160`, `5-6170`, `5-6250`, dan `5-6251` tanpa suffix `{runId}` (batas 15 karakter). Pemulihan ke keadaan awal (tidak ada akun ber-Code itu) dijalankan di hook `before` dan `after` spec ini (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: membaca jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS lewat BE sebelum aksi (8b.10, S-12); disediakan tim FE/BE. Baseline dicatat ulang sebelum aksi pemicu tiap TC.
- State yang diubah spec: akun D14, D15, dan D8 dibuat dan tetap Active; audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-92: Create tercatat di tiga surface

1. Catat jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS sebagai baseline TC-92
2. Klik `+ Account`
3. Isi Account Code `5-6160`, Account Name `Depreciation Expense – Create Log {runId}-063`, dan Account Function Depreciation Expense
4. Klik `[Submit]`
5. Tunggu aksi selesai (modal Add Account tertutup)
6. Klik ikon Changelog di toolbar
7. Verifikasi jumlah entri Changelog bertambah satu dari baseline
8. Verifikasi entri teratas: Action Create, Account Code `5-6160`, Field Account Code, Old Value `—`, New Value `5-6160`
9. Tutup modal Changelog dengan ikon ✕
10. Buka System Log pada Detail User aktor
11. Verifikasi jumlah entri System Log bertambah satu dari baseline
12. Verifikasi entri teratas System Log: Object `Chart of Accounts`, Name `5-6160`
13. Buka Activity Log FAMS
14. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
15. Verifikasi Modified By pada entri teratas Activity Log adalah user aktor

### TC-FA-COA-97: Entri log lama tidak berubah setelah akun diubah namanya

16. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
17. Klik `+ Account`
18. Isi Account Code `5-6170`, Account Name `Depreciation Expense – Snapshot Log {runId}-063`, dan Account Function Depreciation Expense
19. Klik `[Submit]`
20. Tunggu aksi selesai (modal Add Account tertutup)
21. Catat jumlah entri Changelog sebagai baseline TC-97
22. Ketik Search `5-6170`, tekan Enter
23. Klik row action `Edit` pada baris akun `5-6170`
24. Ubah Account Name menjadi `Depreciation Expense – Snapshot Log Edit {runId}-063`
25. Klik `[Save]`
26. Tunggu aksi selesai (modal Edit Account tertutup)
27. Klik ikon Changelog di toolbar
28. Verifikasi jumlah entri Changelog bertambah satu dari baseline TC-97
29. Verifikasi entri baru teratas: Action Edit, Account Code `5-6170`, Field Account Name, Old Value `Depreciation Expense – Snapshot Log {runId}-063`, New Value `Depreciation Expense – Snapshot Log Edit {runId}-063`
30. Ketik Search `5-6170`, tekan Enter
31. Verifikasi entri lama tetap memuat Action Create, Account Code `5-6170`, Field Account Code, Old Value `—`, New Value `5-6170`
32. Klik `(←)` pada kotak Search
33. Tutup modal Changelog dengan ikon ✕

### TC-FA-COA-235: Tie-breaker Changelog

34. Catat jumlah entri Changelog sebagai baseline TC-235
35. Klik `+ Account`
36. Isi Account Code `5-6250`, Account Name `Depreciation Expense – Branch Surabaya {runId}-063`, dan Account Function Depreciation Expense
37. Klik `[Submit]`
38. Ganti isi kotak search dengan `5-6250`, tekan Enter
39. Klik row action `Edit` pada baris akun `5-6250`
40. Ubah Account Code menjadi `5-6251`, Account Name menjadi `Depreciation Expense – Branch Surabaya Edit {runId}-063`, dan Account Function menjadi Asset Cost
41. Klik `[Save]`
42. Tunggu aksi selesai (modal Edit Account tertutup)
43. Klik ikon Changelog di toolbar tanpa mengubah sort (default Date Newest First)
44. Verifikasi jumlah entri Changelog bertambah empat dari baseline TC-235 (satu baris Create dan tiga baris Edit)
45. Verifikasi urutan default Date Newest First: baris kejadian Edit di atas baris kejadian Create
46. Verifikasi kejadian Edit (Action Edit, Account Code `5-6251`, timestamp sama) dari atas ke bawah: Field Account Function (Old Value `Depreciation Expense`, New Value `Asset Cost`); Field Account Name (Old Value `Depreciation Expense – Branch Surabaya {runId}-063`, New Value `Depreciation Expense – Branch Surabaya Edit {runId}-063`); Field Account Code (Old Value `5-6250`, New Value `5-6251`)
47. Verifikasi kejadian Create (Action Create, Account Code `5-6250`) hanya satu baris: Field Account Code (Old Value `—`, New Value `5-6250`)
48. Verifikasi dalam kejadian Edit, field yang ditulis paling akhir tampil paling atas dan urutan penulisan field mengikuti Account Code, Account Name, Account Function
49. Tutup modal Changelog dengan ikon ✕
50. Klik `(←)` pada kotak Search

## Notes

- Alasan spec di atas sekitar 35 langkah (50 langkah): tiga blok memakai satu halaman, satu kelas harness (pencatatan log tiga surface), dan tiap blok memuat baseline sendiri; sebagian besar langkah adalah Search untuk membuka baris target (8b.13) dan pembacaan tiga surface log (blok baca-log berpola); kegagalan satu TC tidak membuat TC lain kehilangan makna.
- TC-FA-COA-92 dan TC-FA-COA-97 mandiri (Dependensi `—`): masing-masing membuat akunnya sendiri (D14 `5-6160`, D15 `5-6170`) lewat UI pada langkah 2 sampai 5 dan 17 sampai 20. Asersi hasil Create (toast, highlight, nilai baris) tidak diulang karena bukan Expected TC-92 dan TC-97; langkah 5 dan 20 hanya menunggu aksi selesai sebelum membuka log (8b.8).
- Cara baca entri baru (S-14): setelah selisih jumlah dari baseline dibuktikan, entri baru dibaca pada baris teratas urutan default Date Newest First. Pada TC-235 empat baris baru berada dalam menit yang sama; urutan di dalam kejadian Edit dan antara kejadian Edit dan Create adalah objek asersi TC itu sendiri (langkah 45 sampai 48).
- Langkah penghubung (S-03): langkah 16 (navigasi kembali ke modul asal setelah membaca System Log dan Activity Log, S-14), langkah 21 (baseline TC-97 dicatat sesudah Create dan sebelum Edit), langkah 22, 30, dan 38 (Search untuk menemukan baris target, R-16), langkah 5, 20, 26, dan 42 (menunggu aksi selesai sebelum membuka log atau berpindah langkah), langkah 32, 33, 49, dan 50 (menutup Search dan modal).
- Asersi "tidak ada pencatatan/log" tidak ada di spec ini (S-05).
- Pembersihan: akun D14, D15, dan D8 (`5-6160`, `5-6170`, dan `5-6251`) dihapus di hook `after`; penghapusan itu menambah entri log permanen yang tidak diasersi.
- A-18: Account Code literal `5-6160` (TC-92), `5-6170` (TC-97), `5-6250`, dan `5-6251` (TC-235) tanpa suffix `{runId}`; hanya dipakai spec ini dan dibersihkan di hook `before` dan `after` (suite serial).
- Temuan untuk QA:
  - Account Code Data Dinamis (D14 `5-6160`, D15 `5-6170`, D8 `5-6250` dan `5-6251`) tidak dapat bersuffix `{runId}` karena batas Account Code 15 karakter dengan whitelist huruf, angka, `-`, `_`, `.` (S-12); nilai literal TC dipakai (pengecualian A-18), dengan pembersihan di `before` dan `after`. Account Name bersuffix `{runId}-063`.
  - TC-92 Post Condition a ("Data dan tiga surface tercatat dalam satu transaksi") tidak memiliki langkah observasi di TC dan tidak diasersi.
  - TC-92 butir b dan c tidak menyebut jalur menu menuju System Log pada Detail User aktor dan Activity Log FAMS; spec mengikuti penamaan TC ("Detail User aktor", "Activity Log FAMS").
  - TC-92 butir c hanya menyebut Modified By pada Activity Log; Object dan Name Activity Log tidak diasersi pada TC-92.
  - TC-97 menyebut Account Name edit `Depreciation Expense – Snapshot Log Edit`; spec menambahkan suffix `{runId}-063`.
