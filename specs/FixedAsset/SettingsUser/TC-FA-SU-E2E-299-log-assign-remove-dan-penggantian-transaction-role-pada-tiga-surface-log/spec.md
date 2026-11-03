---
id: TC-FA-SU-E2E-299-log-assign-remove-dan-penggantian-transaction-role-pada-tiga-surface-log
title: "Log Assign, Remove, dan Penggantian Transaction Role pada Tiga Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-921
  - TC-FA-SU-922
  - TC-FA-SU-923
coverage:
  web: automated
---

# Log Assign, Remove, dan Penggantian Transaction Role pada Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Mira Anggraini {runId}-299`, email `mira.anggraini+{runId}-299@qwertysystem.net`: Active; Transaction Role Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting (Pre-setup #39); tanpa Transaction Role Transfer.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-921: Log Assign Transaction Role per Jenis Transaksi dan grup pada tiga surface log

1. Catat jumlah entri Action `Assign` Field `Transfer — Finance & Accounting — Asset Admin` pada Tab Changelog Mira Anggraini {runId}-299, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
2. Ketik Search `Mira Anggraini {runId}-299`, tekan Enter, klik nama Mira Anggraini {runId}-299, lalu buka Tab Role > Sub-tab Transaction Role
3. Klik `[+ Assign]`, pilih Group Finance & Accounting, Transaction Transfer, dan Role Asset Admin pada modal Assign Transaction Role, lalu klik `[Submit]`
4. Tunggu aksi selesai (modal tertutup)
5. Buka Detail Mira Anggraini {runId}-299 > Tab Changelog, muat ulang sampai entri tampil
6. Verifikasi Tab Changelog memuat satu baris dengan Action `Assign`, Field `Transfer — Finance & Accounting — Asset Admin`, Old Value `—`, New Value `Assigned`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
7. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
8. Verifikasi jumlah entri Action `Assign` Field `Transfer — Finance & Accounting — Asset Admin` pada Tab Changelog Mira Anggraini {runId}-299 bertambah tepat satu dari baseline
9. Buka Tab System Log aktor dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
10. Verifikasi Tab System Log memuat satu baris dengan Action `Assign`, Object `Transaction Role`, Name `Mira Anggraini {runId}-299`, Field `Transfer — Finance & Accounting — Asset Admin`, Old Value `—`, dan New Value `Assigned`
11. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
12. Verifikasi jumlah entri Action `Assign` Field `Transfer — Finance & Accounting — Asset Admin` pada Tab System Log bertambah tepat satu dari baseline
13. Buka Activity Log dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
14. Verifikasi Activity Log memuat satu baris dengan Action `Assign`, Object `Transaction Role`, Name `Mira Anggraini {runId}-299`, Field `Transfer — Finance & Accounting — Asset Admin`, Old Value `—`, New Value `Assigned`, dan Modified By `Lina M`
15. Verifikasi jumlah entri Action `Assign` Field `Transfer — Finance & Accounting — Asset Admin` pada Activity Log bertambah tepat satu dari baseline
16. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
17. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Mira Anggraini {runId}-299`, Action `Assign`, Field `Transfer — Finance & Accounting — Asset Admin`, Old Value `—`, dan New Value `Assigned`
18. Verifikasi jumlah entri Action `Assign` Field `Transfer — Finance & Accounting — Asset Admin` pada Modal Combined Changelog bertambah tepat satu dari baseline
19. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-922: Log Remove Transaction Role per kombinasi pada tiga surface log

20. Catat jumlah entri Action `Remove` Field `Borrowing & Assignment — Finance & Accounting — Approver` pada Tab Changelog Mira Anggraini {runId}-299, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
21. Ketik Search `Mira Anggraini {runId}-299`, tekan Enter, klik nama Mira Anggraini {runId}-299, lalu buka Tab Role > Sub-tab Transaction Role
22. Klik Remove pada baris Borrowing & Assignment × Approver
23. Tunggu aksi selesai
24. Buka Detail Mira Anggraini {runId}-299 > Tab Changelog, muat ulang sampai entri tampil
25. Verifikasi Tab Changelog memuat satu baris dengan Action `Remove`, Field `Borrowing & Assignment — Finance & Accounting — Approver`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
26. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
27. Verifikasi jumlah entri Action `Remove` Field `Borrowing & Assignment — Finance & Accounting — Approver` pada Tab Changelog Mira Anggraini {runId}-299 bertambah tepat satu dari baseline
28. Buka Tab System Log aktor dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
29. Verifikasi Tab System Log memuat satu baris dengan Action `Remove`, Object `Transaction Role`, Name `Mira Anggraini {runId}-299`, Field `Borrowing & Assignment — Finance & Accounting — Approver`, Old Value `Assigned`, dan New Value `—`
30. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
31. Verifikasi jumlah entri Action `Remove` Field `Borrowing & Assignment — Finance & Accounting — Approver` pada Tab System Log bertambah tepat satu dari baseline
32. Buka Activity Log dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
33. Verifikasi Activity Log memuat satu baris dengan Action `Remove`, Object `Transaction Role`, Name `Mira Anggraini {runId}-299`, Field `Borrowing & Assignment — Finance & Accounting — Approver`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M`
34. Verifikasi jumlah entri Action `Remove` Field `Borrowing & Assignment — Finance & Accounting — Approver` pada Activity Log bertambah tepat satu dari baseline
35. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
36. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Mira Anggraini {runId}-299`, Action `Remove`, Field `Borrowing & Assignment — Finance & Accounting — Approver`, Old Value `Assigned`, dan New Value `—`
37. Verifikasi jumlah entri Action `Remove` Field `Borrowing & Assignment — Finance & Accounting — Approver` pada Modal Combined Changelog bertambah tepat satu dari baseline
38. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-923: Penggantian Transaction Role karena naik atau turun tangga dicatat dua entri Remove lalu Assign

39. Catat jumlah entri Action `Remove`, `Assign`, dan `Edit` dengan Field Disposal pada Tab Changelog Mira Anggraini {runId}-299, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
40. Ketik Search `Mira Anggraini {runId}-299`, tekan Enter, klik nama Mira Anggraini {runId}-299, lalu buka Tab Role > Sub-tab Transaction Role
41. Klik `[+ Assign]`, pilih Group Finance & Accounting, Transaction Disposal, dan Role Asset Admin (saat ini Staff), lalu klik `[Submit]`
42. Verifikasi toast "Success, Asset Admin has been assigned." tampil
43. Tunggu aksi selesai (modal tertutup)
44. Buka Detail Mira Anggraini {runId}-299 > Tab Changelog, muat ulang sampai entri tampil
45. Verifikasi Tab Changelog memuat berurutan `Remove` Field `Disposal — Finance & Accounting — Staff` (Old Value `Assigned`, New Value `—`) lalu `Assign` Field `Disposal — Finance & Accounting — Asset Admin` (Old Value `—`, New Value `Assigned`)
46. Verifikasi jumlah entri `Remove` dan `Assign` untuk Field itu pada Tab Changelog masing-masing bertambah tepat satu dari baseline
47. Buka Tab System Log aktor dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
48. Verifikasi Tab System Log memuat pasangan entri yang sama dengan Object `Transaction Role`
49. Buka Activity Log dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
50. Verifikasi Activity Log memuat pasangan entri yang sama dengan Object `Transaction Role` dan Modified By `Lina M`
51. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
52. Verifikasi Modal Combined Changelog memuat pasangan entri yang sama
53. Tutup Modal Combined Changelog dengan `[✕]`
54. Buka Detail Mira Anggraini {runId}-299 > Tab Role > Sub-tab Transaction Role lalu buka modal Changelog User > Transaction Role, muat ulang sampai entri tampil
55. Verifikasi modal Changelog User > Transaction Role memuat pasangan entri yang sama
56. Tutup modal Changelog User > Transaction Role dengan `[✕]`
57. Verifikasi jumlah entri Action `Edit` dengan Field Disposal pada Tab Changelog, Tab System Log, Activity Log, dan Modal Combined Changelog sama dengan baseline (tidak ada entri `Edit` untuk penggantian role)
58. Turunkan Disposal × Asset Admin pada Finance & Accounting kembali ke Staff lewat modal Assign Transaction Role, lalu klik `[Change]` pada dialog konfirmasi `Are you sure you want to change it?`
59. Tunggu aksi selesai (modal dan dialog tertutup)
60. Buka Detail Mira Anggraini {runId}-299 > Tab Changelog, muat ulang sampai entri tampil
61. Verifikasi Tab Changelog memuat pasangan `Remove` Field `Disposal — Finance & Accounting — Asset Admin` (Old Value `Assigned`, New Value `—`) lalu `Assign` Field `Disposal — Finance & Accounting — Staff` (Old Value `—`, New Value `Assigned`)
62. Buka Tab System Log aktor dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
63. Verifikasi Tab System Log memuat pasangan entri yang sama dengan Object `Transaction Role`
64. Buka Activity Log dan cari Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
65. Verifikasi Activity Log memuat pasangan entri yang sama dengan Object `Transaction Role` dan Modified By `Lina M`
66. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Mira Anggraini {runId}-299`, muat ulang sampai entri tampil
67. Verifikasi Modal Combined Changelog memuat pasangan entri yang sama
68. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 4, 21, 23, 40, 43, 59; langkah baseline jumlah entri (S-12): 1, 20, 39. Langkah 2, 21, 40 juga Search untuk menemukan baris target (R-16).
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 53 dari 68 langkah, sisa 15 langkah.
- Asersi "satu entri" memakai baseline jumlah entri per Action dan Field dan Name bersuffix unik (S-12).
- Pengguna milik spec bernama sama dengan Pre-setup TC (Mira Anggraini) dengan suffix `{runId}-299` (S-06).
- Temuan untuk QA (S-15):
  - Langkah Uji TC-FA-SU-921 dan TC-FA-SU-922 tidak menyebut toast; spec tidak mengasersinya. Post Condition kedua TC (penugasan target berubah) tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-SU-923 butir d (turun tangga dengan konfirmasi) tidak punya langkah di Langkah Uji; spec menambah langkah turun tangga Asset Admin ke Staff memakai dialog `Are you sure you want to change it?` dan tombol `[Change]` dari Catatan TC (keputusan NC-22) dan mengasersi pasangan entri pada empat surface, tanpa modal Changelog User > Transaction Role karena butir d tidak menyebutnya.
  - Langkah Uji TC-FA-SU-923 tidak menyebut pemilihan Role Staff secara eksplisit sebagai keadaan awal; keadaan awal mengikuti Pre-setup #39 (Disposal × Staff pada Finance & Accounting). Klausa "tidak ada entri `Edit`" ditulis sebagai asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g; anchor positifnya pasangan entri `Remove` dan `Assign` yang diasersi tepat sebelumnya.
