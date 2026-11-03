---
id: TC-FA-SU-E2E-296-log-resend-confirmation-email-dan-edit-home-group-pada-tiga-surface-log
title: "Log Resend Confirmation Email dan Edit Home Group pada Tiga Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-912
  - TC-FA-SU-913
  - TC-FA-SU-914
coverage:
  web: automated
---

# Log Resend Confirmation Email dan Edit Home Group pada Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan layanan email (#37). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Indra Wijaya {runId}-296`, email `indra.wijaya+{runId}-296@qwertysystem.net`: Pending Email Confirmation dengan alamat email baru pending `indra.wijaya.baru+{runId}-296@qwertysystem.net`, cooldown Resend untuk Indra belum berjalan (prasyarat TC-FA-SU-912 dijamin seed API, disediakan tim FE/BE).
  - `Hana Kusuma {runId}-296`, email `hana.kusuma+{runId}-296@qwertysystem.net`: Active, sudah aktivasi, Home Group General Affairs.
  - `Gita Permata {runId}-296`, email `gita.permata+{runId}-296@qwertysystem.net`: Active, Home Group Finance & Accounting.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`). Cooldown Resend 60 detik berjalan untuk Indra sesudah langkah 3 dan berakhir sendiri.

## Test Steps

### TC-FA-SU-912: Log Resend Confirmation Email pada tiga surface log

1. Catat jumlah entri Action `Resend Confirmation Email` Field `Confirmation Email` pada Tab Changelog Indra Wijaya {runId}-296, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
2. Ketik Search `Indra Wijaya {runId}-296`, tekan Enter
3. Klik ⋯ pada baris Indra Wijaya {runId}-296 lalu klik `Resend Confirmation Email`
4. Tunggu aksi selesai
5. Buka Detail Indra Wijaya {runId}-296 > Tab Changelog, muat ulang sampai entri tampil
6. Verifikasi Tab Changelog memuat satu baris dengan Action `Resend Confirmation Email`, Field `Confirmation Email`, Old Value `—`, New Value `alamat email baru pending Indra Wijaya {runId}-296 (indra.wijaya.baru+{runId}-296@qwertysystem.net)`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
7. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
8. Verifikasi jumlah entri Action `Resend Confirmation Email` Field `Confirmation Email` pada Tab Changelog Indra Wijaya {runId}-296 bertambah tepat satu dari baseline
9. Buka Tab System Log aktor dan cari Name `Indra Wijaya {runId}-296`, muat ulang sampai entri tampil
10. Verifikasi Tab System Log memuat satu baris dengan Action `Resend Confirmation Email`, Object `User`, Name `Indra Wijaya {runId}-296`, Field `Confirmation Email`, Old Value `—`, dan New Value `alamat email baru pending Indra Wijaya {runId}-296 (indra.wijaya.baru+{runId}-296@qwertysystem.net)`
11. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
12. Verifikasi jumlah entri Action `Resend Confirmation Email` Field `Confirmation Email` pada Tab System Log bertambah tepat satu dari baseline
13. Buka Activity Log dan cari Name `Indra Wijaya {runId}-296`, muat ulang sampai entri tampil
14. Verifikasi Activity Log memuat satu baris dengan Action `Resend Confirmation Email`, Object `Settings > User`, Name `Indra Wijaya {runId}-296`, Field `Confirmation Email`, Old Value `—`, New Value `alamat email baru pending Indra Wijaya {runId}-296 (indra.wijaya.baru+{runId}-296@qwertysystem.net)`, dan Modified By `Lina M`
15. Verifikasi jumlah entri Action `Resend Confirmation Email` Field `Confirmation Email` pada Activity Log bertambah tepat satu dari baseline
16. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Indra Wijaya {runId}-296`, muat ulang sampai entri tampil
17. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Indra Wijaya {runId}-296`, Action `Resend Confirmation Email`, Field `Confirmation Email`, Old Value `—`, dan New Value `alamat email baru pending Indra Wijaya {runId}-296 (indra.wijaya.baru+{runId}-296@qwertysystem.net)`
18. Verifikasi jumlah entri Action `Resend Confirmation Email` Field `Confirmation Email` pada Modal Combined Changelog bertambah tepat satu dari baseline
19. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-913: Log Edit Home Group pada tiga surface log

20. Catat jumlah entri Action `Edit Home Group` Field `Home Group` pada Tab Changelog Hana Kusuma {runId}-296, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
21. Ketik Search `Hana Kusuma {runId}-296`, tekan Enter
22. Klik ⋯ pada baris Hana Kusuma {runId}-296, klik `Edit Home Group`, klik node IT Infrastructure pada popup `Select Home Group`, lalu klik `[Select]`
23. Tunggu aksi selesai (popup tertutup)
24. Buka Detail Hana Kusuma {runId}-296 > Tab Changelog, muat ulang sampai entri tampil
25. Verifikasi Tab Changelog memuat satu baris dengan Action `Edit Home Group`, Field `Home Group`, Old Value `General Affairs`, New Value `IT Infrastructure`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
26. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
27. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Tab Changelog Hana Kusuma {runId}-296 bertambah tepat satu dari baseline
28. Buka Tab System Log aktor dan cari Name `Hana Kusuma {runId}-296`, muat ulang sampai entri tampil
29. Verifikasi Tab System Log memuat satu baris dengan Action `Edit Home Group`, Object `User`, Name `Hana Kusuma {runId}-296`, Field `Home Group`, Old Value `General Affairs`, dan New Value `IT Infrastructure`
30. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
31. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Tab System Log bertambah tepat satu dari baseline
32. Buka Activity Log dan cari Name `Hana Kusuma {runId}-296`, muat ulang sampai entri tampil
33. Verifikasi Activity Log memuat satu baris dengan Action `Edit Home Group`, Object `Settings > User`, Name `Hana Kusuma {runId}-296`, Field `Home Group`, Old Value `General Affairs`, New Value `IT Infrastructure`, dan Modified By `Lina M`
34. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Activity Log bertambah tepat satu dari baseline
35. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Hana Kusuma {runId}-296`, muat ulang sampai entri tampil
36. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Hana Kusuma {runId}-296`, Action `Edit Home Group`, Field `Home Group`, Old Value `General Affairs`, dan New Value `IT Infrastructure`
37. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Modal Combined Changelog bertambah tepat satu dari baseline
38. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-914: Log Edit Home Group saat Home Group dikosongkan mencatat New Value strip

39. Catat jumlah entri Action `Edit Home Group` Field `Home Group` pada Tab Changelog Gita Permata {runId}-296, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
40. Ketik Search `Gita Permata {runId}-296`, tekan Enter
41. Klik ⋯ pada baris Gita Permata {runId}-296, klik `Edit Home Group`, klik ulang node Finance & Accounting yang ter-highlight pada popup `Select Home Group`, lalu klik `[Select]`
42. Tunggu aksi selesai (popup tertutup)
43. Buka Detail Gita Permata {runId}-296 > Tab Changelog, muat ulang sampai entri tampil
44. Verifikasi Tab Changelog memuat satu baris dengan Action `Edit Home Group`, Field `Home Group`, Old Value `Finance & Accounting`, New Value `—`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
45. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
46. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Tab Changelog Gita Permata {runId}-296 bertambah tepat satu dari baseline
47. Buka Tab System Log aktor dan cari Name `Gita Permata {runId}-296`, muat ulang sampai entri tampil
48. Verifikasi Tab System Log memuat satu baris dengan Action `Edit Home Group`, Object `User`, Name `Gita Permata {runId}-296`, Field `Home Group`, Old Value `Finance & Accounting`, dan New Value `—`
49. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
50. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Tab System Log bertambah tepat satu dari baseline
51. Buka Activity Log dan cari Name `Gita Permata {runId}-296`, muat ulang sampai entri tampil
52. Verifikasi Activity Log memuat satu baris dengan Action `Edit Home Group`, Object `Settings > User`, Name `Gita Permata {runId}-296`, Field `Home Group`, Old Value `Finance & Accounting`, New Value `—`, dan Modified By `Lina M`
53. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Activity Log bertambah tepat satu dari baseline
54. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Gita Permata {runId}-296`, muat ulang sampai entri tampil
55. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Gita Permata {runId}-296`, Action `Edit Home Group`, Field `Home Group`, Old Value `Finance & Accounting`, dan New Value `—`
56. Verifikasi jumlah entri Action `Edit Home Group` Field `Home Group` pada Modal Combined Changelog bertambah tepat satu dari baseline
57. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 4, 21, 23, 40, 42; langkah baseline jumlah entri (S-12): 1, 20, 39. Langkah 2, 21, dan 40 adalah Search untuk menemukan baris target (R-16).
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 45 dari 57 langkah, sisa 12 langkah.
- Asersi "satu entri" memakai baseline jumlah entri per Action dan Field dan Name bersuffix unik (S-12).
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-296` (S-06).
- Temuan untuk QA (S-15):
  - New Value TC-FA-SU-912 `alamat email baru pending Indra Wijaya` berupa deskripsi, bukan nilai literal; spec menuliskannya sebagai deskripsi diikuti email pending bersuffix milik spec `indra.wijaya.baru+{runId}-296@qwertysystem.net`.
  - Langkah Uji TC-FA-SU-912 sampai TC-FA-SU-914 tidak menyebut dialog atau toast; spec tidak mengasersi keduanya. Post Condition TC-FA-SU-912 (cooldown 60 detik berjalan) dan TC-FA-SU-913 serta TC-FA-SU-914 (Home Group target berubah) tidak punya langkah observasi dan tidak diasersi.
  - Prasyarat "cooldown Resend belum berjalan" TC-FA-SU-912 tidak memberi cara membuat kondisinya; spec memakai pengguna baru seed.
