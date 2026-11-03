---
id: TC-FA-SU-E2E-297-log-assign-remove-dan-edit-global-role-pada-tiga-surface-log
title: "Log Assign, Remove, dan Edit Global Role pada Tiga Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-915
  - TC-FA-SU-916
  - TC-FA-SU-917
coverage:
  web: automated
---

# Log Assign, Remove, dan Edit Global Role pada Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan penugasan (#23). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Gita Permata {runId}-297`, email `gita.permata+{runId}-297@qwertysystem.net`: Active; Global Role Manage accounting ON dengan Create dan Read tercentang, Update dan Delete tidak tercentang; tanpa Global Role Manage asset ID configuration.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-915: Log Assign Global Role pada tiga surface log

1. Catat jumlah entri Action `Assign` Field `Manage asset ID configuration` pada Tab Changelog Gita Permata {runId}-297, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
2. Ketik Search `Gita Permata {runId}-297`, tekan Enter, klik nama Gita Permata {runId}-297, lalu buka Tab Role > Sub-tab Global Role
3. Nyalakan switch pada baris Manage asset ID configuration
4. Tunggu aksi selesai
5. Buka Detail Gita Permata {runId}-297 > Tab Changelog, muat ulang sampai entri tampil
6. Verifikasi Tab Changelog memuat satu baris dengan Action `Assign`, Field `Manage asset ID configuration`, Old Value `—`, New Value `Assigned`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
7. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
8. Verifikasi jumlah entri Action `Assign` Field `Manage asset ID configuration` pada Tab Changelog Gita Permata {runId}-297 bertambah tepat satu dari baseline
9. Buka Tab System Log aktor dan cari Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
10. Verifikasi Tab System Log memuat satu baris dengan Action `Assign`, Object `Global Role`, Name `Gita Permata {runId}-297`, Field `Manage asset ID configuration`, Old Value `—`, dan New Value `Assigned`
11. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
12. Verifikasi jumlah entri Action `Assign` Field `Manage asset ID configuration` pada Tab System Log bertambah tepat satu dari baseline
13. Buka Activity Log dan cari Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
14. Verifikasi Activity Log memuat satu baris dengan Action `Assign`, Object `Global Role`, Name `Gita Permata {runId}-297`, Field `Manage asset ID configuration`, Old Value `—`, New Value `Assigned`, dan Modified By `Lina M`
15. Verifikasi jumlah entri Action `Assign` Field `Manage asset ID configuration` pada Activity Log bertambah tepat satu dari baseline
16. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
17. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Gita Permata {runId}-297`, Action `Assign`, Field `Manage asset ID configuration`, Old Value `—`, dan New Value `Assigned`
18. Verifikasi jumlah entri Action `Assign` Field `Manage asset ID configuration` pada Modal Combined Changelog bertambah tepat satu dari baseline
19. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-917: Log Edit Global Role per permission pada tiga surface log

20. Catat jumlah entri Action `Edit` Field `Manage accounting — Update` pada Tab Changelog Gita Permata {runId}-297, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
21. Ketik Search `Gita Permata {runId}-297`, tekan Enter, klik nama Gita Permata {runId}-297, lalu buka Tab Role > Sub-tab Global Role
22. Centang Update pada baris Manage accounting
23. Tunggu aksi selesai
24. Buka Detail Gita Permata {runId}-297 > Tab Changelog, muat ulang sampai entri tampil
25. Verifikasi Tab Changelog memuat satu baris dengan Action `Edit`, Field `Manage accounting — Update`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
26. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
27. Verifikasi jumlah entri Action `Edit` Field `Manage accounting — Update` pada Tab Changelog Gita Permata {runId}-297 bertambah tepat satu dari baseline
28. Buka Tab System Log aktor dan cari Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
29. Verifikasi Tab System Log memuat satu baris dengan Action `Edit`, Object `Global Role`, Name `Gita Permata {runId}-297`, Field `Manage accounting — Update`, Old Value `Inactive`, dan New Value `Active`
30. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
31. Verifikasi jumlah entri Action `Edit` Field `Manage accounting — Update` pada Tab System Log bertambah tepat satu dari baseline
32. Buka Activity Log dan cari Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
33. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Global Role`, Name `Gita Permata {runId}-297`, Field `Manage accounting — Update`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M`
34. Verifikasi jumlah entri Action `Edit` Field `Manage accounting — Update` pada Activity Log bertambah tepat satu dari baseline
35. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
36. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Gita Permata {runId}-297`, Action `Edit`, Field `Manage accounting — Update`, Old Value `Inactive`, dan New Value `Active`
37. Verifikasi jumlah entri Action `Edit` Field `Manage accounting — Update` pada Modal Combined Changelog bertambah tepat satu dari baseline
38. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-916: Log Remove Global Role pada tiga surface log

39. Catat jumlah entri Action `Remove` Field `Manage accounting` pada Tab Changelog Gita Permata {runId}-297, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
40. Ketik Search `Gita Permata {runId}-297`, tekan Enter, klik nama Gita Permata {runId}-297, lalu buka Tab Role > Sub-tab Global Role
41. Matikan switch pada baris Manage accounting
42. Tunggu aksi selesai
43. Buka Detail Gita Permata {runId}-297 > Tab Changelog, muat ulang sampai entri tampil
44. Verifikasi Tab Changelog memuat satu baris dengan Action `Remove`, Field `Manage accounting`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
45. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
46. Verifikasi jumlah entri Action `Remove` Field `Manage accounting` pada Tab Changelog Gita Permata {runId}-297 bertambah tepat satu dari baseline
47. Buka Tab System Log aktor dan cari Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
48. Verifikasi Tab System Log memuat satu baris dengan Action `Remove`, Object `Global Role`, Name `Gita Permata {runId}-297`, Field `Manage accounting`, Old Value `Assigned`, dan New Value `—`
49. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
50. Verifikasi jumlah entri Action `Remove` Field `Manage accounting` pada Tab System Log bertambah tepat satu dari baseline
51. Buka Activity Log dan cari Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
52. Verifikasi Activity Log memuat satu baris dengan Action `Remove`, Object `Global Role`, Name `Gita Permata {runId}-297`, Field `Manage accounting`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M`
53. Verifikasi jumlah entri Action `Remove` Field `Manage accounting` pada Activity Log bertambah tepat satu dari baseline
54. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Gita Permata {runId}-297`, muat ulang sampai entri tampil
55. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Gita Permata {runId}-297`, Action `Remove`, Field `Manage accounting`, Old Value `Assigned`, dan New Value `—`
56. Verifikasi jumlah entri Action `Remove` Field `Manage accounting` pada Modal Combined Changelog bertambah tepat satu dari baseline
57. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-917 dikerjakan sebelum TC-FA-SU-916, karena TC-FA-SU-917 mensyaratkan baris Manage accounting masih ON dengan Update belum tercentang dan TC-FA-SU-916 mematikan switch baris itu (S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 4, 21, 23, 40, 42; langkah baseline jumlah entri (S-12): 1, 20, 39. Langkah 2, 21, dan 40 juga Search untuk menemukan baris target (R-16).
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 45 dari 57 langkah, sisa 12 langkah.
- Asersi "satu entri" memakai baseline jumlah entri per Action dan Field dan Name bersuffix unik (S-12).
- Pengguna milik spec bernama sama dengan Pre-setup TC (Gita Permata) dengan suffix `{runId}-297` (S-06).
- Temuan untuk QA (S-15):
  - Langkah Uji TC-FA-SU-915 sampai TC-FA-SU-917 tidak menyebut dialog konfirmasi atau toast untuk switch dan checkbox Global Role; spec tidak mengasersi keduanya. Post Condition ketiga TC (penugasan target berubah) tidak punya langkah observasi dan tidak diasersi.
  - Object TC-FA-SU-915 sampai TC-FA-SU-917 pada System Log dan Activity Log bernilai `Global Role` (Action pendek dengan Object jenis peran, keputusan NC-06).
