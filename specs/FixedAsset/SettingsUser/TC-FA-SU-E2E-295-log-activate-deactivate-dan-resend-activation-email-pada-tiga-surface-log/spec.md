---
id: TC-FA-SU-E2E-295-log-activate-deactivate-dan-resend-activation-email-pada-tiga-surface-log
title: "Log Activate, Deactivate, dan Resend Activation Email pada Tiga Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-909
  - TC-FA-SU-910
  - TC-FA-SU-911
coverage:
  web: automated
---

# Log Activate, Deactivate, dan Resend Activation Email pada Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Doni Prasetyo {runId}-295`, email `doni.prasetyo+{runId}-295@qwertysystem.net`: Inactive, tanpa aset aktif.
  - `Gita Permata {runId}-295`, email `gita.permata+{runId}-295@qwertysystem.net`: Active, tanpa aset aktif dan bukan approver tertunggu.
  - `Hana Kusuma {runId}-295`, email `hana.kusuma+{runId}-295@qwertysystem.net`: Pending Activation, cooldown Resend untuk Hana belum berjalan (prasyarat TC-FA-SU-911 dijamin seed API, disediakan tim FE/BE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`). Cooldown Resend 60 detik berjalan untuk Hana sesudah langkah 41 dan berakhir sendiri; tidak ada pemulihan lain karena pengguna milik spec dihapus di hook `after`.

## Test Steps

### TC-FA-SU-909: Log Activate pada tiga surface log

1. Catat jumlah entri Action `Activate` Field `Status` pada Tab Changelog Doni Prasetyo {runId}-295, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
2. Ketik Search `Doni Prasetyo {runId}-295`, tekan Enter
3. Klik sakelar Active pada baris Doni Prasetyo {runId}-295, lalu klik `[Activate]` pada dialog `Activate User`
4. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke ON)
5. Buka Detail Doni Prasetyo {runId}-295 > Tab Changelog, muat ulang sampai entri tampil
6. Verifikasi Tab Changelog memuat satu baris dengan Action `Activate`, Field `Status`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
7. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
8. Verifikasi jumlah entri Action `Activate` Field `Status` pada Tab Changelog Doni Prasetyo {runId}-295 bertambah tepat satu dari baseline
9. Buka Tab System Log aktor dan cari Name `Doni Prasetyo {runId}-295`, muat ulang sampai entri tampil
10. Verifikasi Tab System Log memuat satu baris dengan Action `Activate`, Object `User`, Name `Doni Prasetyo {runId}-295`, Field `Status`, Old Value `Inactive`, dan New Value `Active`
11. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
12. Verifikasi jumlah entri Action `Activate` Field `Status` pada Tab System Log bertambah tepat satu dari baseline
13. Buka Activity Log dan cari Name `Doni Prasetyo {runId}-295`, muat ulang sampai entri tampil
14. Verifikasi Activity Log memuat satu baris dengan Action `Activate`, Object `Settings > User`, Name `Doni Prasetyo {runId}-295`, Field `Status`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M`
15. Verifikasi jumlah entri Action `Activate` Field `Status` pada Activity Log bertambah tepat satu dari baseline
16. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Doni Prasetyo {runId}-295`, muat ulang sampai entri tampil
17. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Doni Prasetyo {runId}-295`, Action `Activate`, Field `Status`, Old Value `Inactive`, dan New Value `Active`
18. Verifikasi jumlah entri Action `Activate` Field `Status` pada Modal Combined Changelog bertambah tepat satu dari baseline
19. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-910: Log Deactivate pada tiga surface log

20. Catat jumlah entri Action `Deactivate` Field `Status` pada Tab Changelog Gita Permata {runId}-295, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
21. Ketik Search `Gita Permata {runId}-295`, tekan Enter
22. Klik sakelar Active pada baris Gita Permata {runId}-295, lalu klik `[Deactivate]` pada dialog `Deactivate User`
23. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke OFF)
24. Buka Detail Gita Permata {runId}-295 > Tab Changelog, muat ulang sampai entri tampil
25. Verifikasi Tab Changelog memuat satu baris dengan Action `Deactivate`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
26. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
27. Verifikasi jumlah entri Action `Deactivate` Field `Status` pada Tab Changelog Gita Permata {runId}-295 bertambah tepat satu dari baseline
28. Buka Tab System Log aktor dan cari Name `Gita Permata {runId}-295`, muat ulang sampai entri tampil
29. Verifikasi Tab System Log memuat satu baris dengan Action `Deactivate`, Object `User`, Name `Gita Permata {runId}-295`, Field `Status`, Old Value `Active`, dan New Value `Inactive`
30. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
31. Verifikasi jumlah entri Action `Deactivate` Field `Status` pada Tab System Log bertambah tepat satu dari baseline
32. Buka Activity Log dan cari Name `Gita Permata {runId}-295`, muat ulang sampai entri tampil
33. Verifikasi Activity Log memuat satu baris dengan Action `Deactivate`, Object `Settings > User`, Name `Gita Permata {runId}-295`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `Lina M`
34. Verifikasi jumlah entri Action `Deactivate` Field `Status` pada Activity Log bertambah tepat satu dari baseline
35. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Gita Permata {runId}-295`, muat ulang sampai entri tampil
36. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Gita Permata {runId}-295`, Action `Deactivate`, Field `Status`, Old Value `Active`, dan New Value `Inactive`
37. Verifikasi jumlah entri Action `Deactivate` Field `Status` pada Modal Combined Changelog bertambah tepat satu dari baseline
38. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-911: Log Resend Activation Email pada tiga surface log

39. Catat jumlah entri Action `Resend Activation Email` Field `Activation Email` pada Tab Changelog Hana Kusuma {runId}-295, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
40. Ketik Search `Hana Kusuma {runId}-295`, tekan Enter
41. Klik ⋯ pada baris Hana Kusuma {runId}-295 lalu klik `Resend Activation Email`
42. Tunggu aksi selesai
43. Buka Detail Hana Kusuma {runId}-295 > Tab Changelog, muat ulang sampai entri tampil
44. Verifikasi Tab Changelog memuat satu baris dengan Action `Resend Activation Email`, Field `Activation Email`, Old Value `—`, New Value `hana.kusuma+{runId}-295@qwertysystem.net`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
45. Verifikasi Old Value dan New Value pada baris Tab Changelog itu tidak keduanya `—`
46. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
47. Verifikasi jumlah entri Action `Resend Activation Email` Field `Activation Email` pada Tab Changelog Hana Kusuma {runId}-295 bertambah tepat satu dari baseline
48. Buka Tab System Log aktor dan cari Name `Hana Kusuma {runId}-295`, muat ulang sampai entri tampil
49. Verifikasi Tab System Log memuat satu baris dengan Action `Resend Activation Email`, Object `User`, Name `Hana Kusuma {runId}-295`, Field `Activation Email`, Old Value `—`, dan New Value `hana.kusuma+{runId}-295@qwertysystem.net`
50. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
51. Verifikasi jumlah entri Action `Resend Activation Email` Field `Activation Email` pada Tab System Log bertambah tepat satu dari baseline
52. Buka Activity Log dan cari Name `Hana Kusuma {runId}-295`, muat ulang sampai entri tampil
53. Verifikasi Activity Log memuat satu baris dengan Action `Resend Activation Email`, Object `Settings > User`, Name `Hana Kusuma {runId}-295`, Field `Activation Email`, Old Value `—`, New Value `hana.kusuma+{runId}-295@qwertysystem.net`, dan Modified By `Lina M`
54. Verifikasi jumlah entri Action `Resend Activation Email` Field `Activation Email` pada Activity Log bertambah tepat satu dari baseline
55. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Hana Kusuma {runId}-295`, muat ulang sampai entri tampil
56. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Hana Kusuma {runId}-295`, Action `Resend Activation Email`, Field `Activation Email`, Old Value `—`, dan New Value `hana.kusuma+{runId}-295@qwertysystem.net`
57. Verifikasi jumlah entri Action `Resend Activation Email` Field `Activation Email` pada Modal Combined Changelog bertambah tepat satu dari baseline
58. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 4, 21, 23, 40, 42; langkah baseline jumlah entri (S-12): 1, 20, 39. Langkah 2, 21, dan 40 adalah Search untuk menemukan baris target (R-16); pencarian entri berdasarkan Name di surface log dan penutupan Modal Combined Changelog adalah bagian blok baca-log.
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 46 dari 58 langkah, sisa 12 langkah.
- Asersi "satu entri" memakai baseline jumlah entri per Action dan Field dan Name bersuffix unik (S-12); tidak ada total absolut audit trail yang diasersi.
- Pengguna milik spec bernama sama dengan Pre-setup TC (Doni Prasetyo, Gita Permata, Hana Kusuma) dengan suffix `{runId}-295` (S-06). New Value TC-FA-SU-911 `hana.kusuma@corp.id` ditulis sebagai email bersuffix milik spec `hana.kusuma+{runId}-295@qwertysystem.net`.
- Temuan untuk QA (S-15):
  - TC-FA-SU-909 butir e menyebut "kegagalan penulisan log tidak membatalkan toggle" tanpa langkah pemicu; hanya bagian eventual (entri muncul sesudah commit) yang diasersi lewat muat ulang sampai entri tampil. TC-FA-SU-911 butir e "entri ditulis di background setelah email terkirim" tidak punya langkah observasi dan tidak diasersi selain Old Value dan New Value tidak keduanya `—`.
  - Post Condition TC-FA-SU-909 dan TC-FA-SU-910 (status aktif target berubah) dan TC-FA-SU-911 (cooldown 60 detik berjalan) tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-SU-911 dan TC-FA-SU-912 mensyaratkan cooldown Resend belum berjalan tanpa cara membuat kondisi itu; spec memakai pengguna baru seed (cooldown belum pernah berjalan).
  - Langkah Uji TC-FA-SU-909 sampai TC-FA-SU-911 tidak menyebut dialog konfirmasi; spec mengikuti dialog `Activate User` dan `Deactivate User` yang dipakai TC-FA-SU-87 dan TC-FA-SU-88. Jalur navigasi Tab System Log aktor dan Activity Log ditentukan di Page Object.
