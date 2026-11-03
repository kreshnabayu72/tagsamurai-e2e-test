---
id: TC-FA-SU-E2E-298-log-assign-edit-dan-remove-group-role-pada-tiga-surface-log
title: "Log Assign, Edit, dan Remove Group Role pada Tiga Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-918
  - TC-FA-SU-919
  - TC-FA-SU-920
coverage:
  web: automated
---

# Log Assign, Edit, dan Remove Group Role pada Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan penugasan (#23). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Wawan Setiawan {runId}-298`, email `wawan.setiawan+{runId}-298@qwertysystem.net`: Active; Group Role Manage files pada IT Infrastructure dan Branch Surabaya (Delete pada Branch Surabaya belum tercentang), tanpa Manage files pada General Affairs.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-918: Log Assign Group Role per grup pada tiga surface log

1. Catat jumlah entri Action `Assign` Field `Manage files — General Affairs` pada Tab Changelog Wawan Setiawan {runId}-298, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
2. Ketik Search `Wawan Setiawan {runId}-298`, tekan Enter, klik nama Wawan Setiawan {runId}-298, lalu buka Tab Role > Sub-tab Group Role dan buka popup Assign Group Role Manage files
3. Klik `[+ Assign Group]`, centang node General Affairs pada popup Select Group, klik `[Select]`, lalu klik `[Save]`
4. Tunggu aksi selesai (popup tertutup)
5. Buka Detail Wawan Setiawan {runId}-298 > Tab Changelog, muat ulang sampai entri tampil
6. Verifikasi Tab Changelog memuat satu baris dengan Action `Assign`, Field `Manage files — General Affairs`, Old Value `—`, New Value `Assigned`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
7. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
8. Verifikasi jumlah entri Action `Assign` Field `Manage files — General Affairs` pada Tab Changelog Wawan Setiawan {runId}-298 bertambah tepat satu dari baseline
9. Buka Tab System Log aktor dan cari Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
10. Verifikasi Tab System Log memuat satu baris dengan Action `Assign`, Object `Group Role`, Name `Wawan Setiawan {runId}-298`, Field `Manage files — General Affairs`, Old Value `—`, dan New Value `Assigned`
11. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
12. Verifikasi jumlah entri Action `Assign` Field `Manage files — General Affairs` pada Tab System Log bertambah tepat satu dari baseline
13. Buka Activity Log dan cari Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
14. Verifikasi Activity Log memuat satu baris dengan Action `Assign`, Object `Group Role`, Name `Wawan Setiawan {runId}-298`, Field `Manage files — General Affairs`, Old Value `—`, New Value `Assigned`, dan Modified By `Lina M`
15. Verifikasi jumlah entri Action `Assign` Field `Manage files — General Affairs` pada Activity Log bertambah tepat satu dari baseline
16. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
17. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Wawan Setiawan {runId}-298`, Action `Assign`, Field `Manage files — General Affairs`, Old Value `—`, dan New Value `Assigned`
18. Verifikasi jumlah entri Action `Assign` Field `Manage files — General Affairs` pada Modal Combined Changelog bertambah tepat satu dari baseline
19. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-919: Log Edit Group Role per permission dan grup pada tiga surface log

20. Catat jumlah entri Action `Edit` Field `Manage files — Branch Surabaya — Delete` pada Tab Changelog Wawan Setiawan {runId}-298, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
21. Ketik Search `Wawan Setiawan {runId}-298`, tekan Enter, klik nama Wawan Setiawan {runId}-298, lalu buka Tab Role > Sub-tab Group Role dan buka popup Assign Group Role Manage files
22. Centang Delete pada baris Branch Surabaya lalu klik `[Save]`
23. Tunggu aksi selesai (popup tertutup)
24. Buka Detail Wawan Setiawan {runId}-298 > Tab Changelog, muat ulang sampai entri tampil
25. Verifikasi Tab Changelog memuat satu baris dengan Action `Edit`, Field `Manage files — Branch Surabaya — Delete`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
26. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
27. Verifikasi jumlah entri Action `Edit` Field `Manage files — Branch Surabaya — Delete` pada Tab Changelog Wawan Setiawan {runId}-298 bertambah tepat satu dari baseline
28. Buka Tab System Log aktor dan cari Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
29. Verifikasi Tab System Log memuat satu baris dengan Action `Edit`, Object `Group Role`, Name `Wawan Setiawan {runId}-298`, Field `Manage files — Branch Surabaya — Delete`, Old Value `Inactive`, dan New Value `Active`
30. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
31. Verifikasi jumlah entri Action `Edit` Field `Manage files — Branch Surabaya — Delete` pada Tab System Log bertambah tepat satu dari baseline
32. Buka Activity Log dan cari Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
33. Verifikasi Activity Log memuat satu baris dengan Action `Edit`, Object `Group Role`, Name `Wawan Setiawan {runId}-298`, Field `Manage files — Branch Surabaya — Delete`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M`
34. Verifikasi jumlah entri Action `Edit` Field `Manage files — Branch Surabaya — Delete` pada Activity Log bertambah tepat satu dari baseline
35. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
36. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Wawan Setiawan {runId}-298`, Action `Edit`, Field `Manage files — Branch Surabaya — Delete`, Old Value `Inactive`, dan New Value `Active`
37. Verifikasi jumlah entri Action `Edit` Field `Manage files — Branch Surabaya — Delete` pada Modal Combined Changelog bertambah tepat satu dari baseline
38. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-920: Log Remove Group Role per grup pada tiga surface log

39. Catat jumlah entri Action `Remove` Field `Manage files — Branch Surabaya` pada Tab Changelog Wawan Setiawan {runId}-298, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
40. Ketik Search `Wawan Setiawan {runId}-298`, tekan Enter, klik nama Wawan Setiawan {runId}-298, lalu buka Tab Role > Sub-tab Group Role dan buka popup Assign Group Role Manage files
41. Klik ikon hapus pada baris Branch Surabaya lalu klik `[Save]`
42. Tunggu aksi selesai (popup tertutup)
43. Buka Detail Wawan Setiawan {runId}-298 > Tab Changelog, muat ulang sampai entri tampil
44. Verifikasi Tab Changelog memuat satu baris dengan Action `Remove`, Field `Manage files — Branch Surabaya`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
45. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
46. Verifikasi jumlah entri Action `Remove` Field `Manage files — Branch Surabaya` pada Tab Changelog Wawan Setiawan {runId}-298 bertambah tepat satu dari baseline
47. Buka Tab System Log aktor dan cari Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
48. Verifikasi Tab System Log memuat satu baris dengan Action `Remove`, Object `Group Role`, Name `Wawan Setiawan {runId}-298`, Field `Manage files — Branch Surabaya`, Old Value `Assigned`, dan New Value `—`
49. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
50. Verifikasi jumlah entri Action `Remove` Field `Manage files — Branch Surabaya` pada Tab System Log bertambah tepat satu dari baseline
51. Buka Activity Log dan cari Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
52. Verifikasi Activity Log memuat satu baris dengan Action `Remove`, Object `Group Role`, Name `Wawan Setiawan {runId}-298`, Field `Manage files — Branch Surabaya`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M`
53. Verifikasi jumlah entri Action `Remove` Field `Manage files — Branch Surabaya` pada Activity Log bertambah tepat satu dari baseline
54. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Wawan Setiawan {runId}-298`, muat ulang sampai entri tampil
55. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Wawan Setiawan {runId}-298`, Action `Remove`, Field `Manage files — Branch Surabaya`, Old Value `Assigned`, dan New Value `—`
56. Verifikasi jumlah entri Action `Remove` Field `Manage files — Branch Surabaya` pada Modal Combined Changelog bertambah tepat satu dari baseline
57. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 4, 21, 23, 40, 42; langkah baseline jumlah entri (S-12): 1, 20, 39. Langkah 2, 21, dan 40 juga Search untuk menemukan baris target (R-16).
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 45 dari 57 langkah, sisa 12 langkah.
- Asersi "satu entri" memakai baseline jumlah entri per Action dan Field dan Name bersuffix unik (S-12).
- Pengguna milik spec bernama sama dengan Pre-setup TC (Wawan Setiawan) dengan suffix `{runId}-298` (S-06).
- Temuan untuk QA (S-15):
  - Langkah Uji TC-FA-SU-918 sampai TC-FA-SU-920 tidak menyebut toast Save; spec tidak mengasersinya. Post Condition ketiga TC (penugasan target berubah) tidak punya langkah observasi dan tidak diasersi. TC-FA-SU-919 mensyaratkan baris Branch Surabaya ada dan TC-FA-SU-920 menghapusnya, sehingga urutan TC sumber dipertahankan.
