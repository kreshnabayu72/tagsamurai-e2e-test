---
id: TC-FA-SU-E2E-300-log-auto-revert-total-control-read-only-dan-group-manager-pada-tiga-surface-log
title: "Log Auto-Revert Total Control, Read Only, dan Group Manager pada Tiga Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-924
  - TC-FA-SU-925
  - TC-FA-SU-926
coverage:
  web: automated
---

# Log Auto-Revert Total Control, Read Only, dan Group Manager pada Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor kedua untuk TC-FA-SU-924: Default User Ahmad Dahlan (Pre-setup #2), `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`; ganti akun dengan langkah eksplisit 43 dan 44, dan hook `after` mengembalikan sesi ke akun default suite (S-07).
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan penugasan (#23). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Lina Marlina {runId}-300`, email `lina.marlina+{runId}-300@qwertysystem.net`: Active; tingkat akses Total Control; Global Role Manage accounting dengan Update tercentang (target TC-FA-SU-924).
  - `Citra Lestari {runId}-300`, email `citra.lestari+{runId}-300@qwertysystem.net`: Active; tingkat akses Read Only (target TC-FA-SU-925).
  - `Oscar Pranata {runId}-300`, email `oscar.pranata+{runId}-300@qwertysystem.net`: Active; Group Manager pada IT Infrastructure dan Accounts Payable dengan baris pola Group Manager pada kedua grup termaterialisasi (Group Role katalog selain Manage user & role dengan CRUD penuh sesuai kolom yang berlaku; Transaction Role Asset Admin serta Approver pada setiap Jenis Transaksi), seperti Oscar Pranata Pre-setup #9 (target TC-FA-SU-926).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field (termasuk Action `Remove (via Group Manager)` untuk TC-FA-SU-926) pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`). Target yang tier-nya dilepas adalah pengguna milik spec, bukan akun aktor Pre-setup.

## Test Steps

### TC-FA-SU-925: Log Auto-Revert Read Only pada tiga surface log

1. Catat jumlah entri Action `Auto-Revert` Field `Access Level` pada Tab Changelog Citra Lestari {runId}-300, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
2. Ketik Search `Citra Lestari {runId}-300`, tekan Enter, klik nama Citra Lestari {runId}-300, lalu buka Tab Role > Sub-tab Global Role
3. Nyalakan switch pada baris Manage asset ID configuration lalu klik `[Remove]` pada dialog
4. Tunggu aksi selesai (dialog tertutup)
5. Buka Detail Citra Lestari {runId}-300 > Tab Changelog, muat ulang sampai entri tampil
6. Verifikasi Tab Changelog memuat satu baris dengan Action `Auto-Revert`, Field `Access Level`, Old Value `Read Only`, New Value `—`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
7. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
8. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Tab Changelog Citra Lestari {runId}-300 bertambah tepat satu dari baseline
9. Buka Tab System Log aktor dan cari Name `Citra Lestari {runId}-300`, muat ulang sampai entri tampil
10. Verifikasi Tab System Log memuat satu baris dengan Action `Auto-Revert`, Object `Read Only`, Name `Citra Lestari {runId}-300`, Field `Access Level`, Old Value `Read Only`, dan New Value `—`
11. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
12. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Tab System Log bertambah tepat satu dari baseline
13. Buka Activity Log dan cari Name `Citra Lestari {runId}-300`, muat ulang sampai entri tampil
14. Verifikasi Activity Log memuat satu baris dengan Action `Auto-Revert`, Object `Read Only`, Name `Citra Lestari {runId}-300`, Field `Access Level`, Old Value `Read Only`, New Value `—`, dan Modified By `Lina M`
15. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Activity Log bertambah tepat satu dari baseline
16. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Citra Lestari {runId}-300`, muat ulang sampai entri tampil
17. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Citra Lestari {runId}-300`, Action `Auto-Revert`, Field `Access Level`, Old Value `Read Only`, dan New Value `—`
18. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Modal Combined Changelog bertambah tepat satu dari baseline
19. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-926: Log Auto-Revert Group Manager per grup pada tiga surface log

20. Catat jumlah entri Action `Auto-Revert` Field `Group Manager — IT Infrastructure` dan jumlah entri Action `Remove (via Group Manager)` pada Tab Changelog Oscar Pranata {runId}-300, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
21. Ketik Search `Oscar Pranata {runId}-300`, tekan Enter, klik nama Oscar Pranata {runId}-300, lalu buka Tab Role > Sub-tab Group Role dan buka popup Assign Group Role Manage group
22. Hapus centang Update pada baris IT Infrastructure, klik `[Save]`, lalu klik `[Remove]` pada dialog
23. Tunggu aksi selesai (dialog dan popup tertutup)
24. Buka Detail Oscar Pranata {runId}-300 > Tab Changelog, muat ulang sampai entri tampil
25. Verifikasi Tab Changelog memuat satu baris dengan Action `Auto-Revert`, Field `Group Manager — IT Infrastructure`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M` (format `[First Name] [Last Initial]`)
26. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
27. Verifikasi jumlah entri Action `Auto-Revert` Field `Group Manager — IT Infrastructure` pada Tab Changelog Oscar Pranata {runId}-300 bertambah tepat satu dari baseline
28. Verifikasi jumlah entri Action `Remove (via Group Manager)` pada Tab Changelog Oscar Pranata {runId}-300 sama dengan baseline (Auto-Revert tidak menulis entri per baris pola)
29. Buka Tab System Log aktor dan cari Name `Oscar Pranata {runId}-300`, muat ulang sampai entri tampil
30. Verifikasi Tab System Log memuat satu baris dengan Action `Auto-Revert`, Object `Group Manager`, Name `Oscar Pranata {runId}-300`, Field `Group Manager — IT Infrastructure`, Old Value `Assigned`, dan New Value `—`
31. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
32. Verifikasi jumlah entri Action `Auto-Revert` Field `Group Manager — IT Infrastructure` pada Tab System Log bertambah tepat satu dari baseline
33. Verifikasi jumlah entri Action `Remove (via Group Manager)` pada Tab System Log aktor sama dengan baseline (Auto-Revert tidak menulis entri per baris pola)
34. Buka Activity Log dan cari Name `Oscar Pranata {runId}-300`, muat ulang sampai entri tampil
35. Verifikasi Activity Log memuat satu baris dengan Action `Auto-Revert`, Object `Group Manager`, Name `Oscar Pranata {runId}-300`, Field `Group Manager — IT Infrastructure`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M`
36. Verifikasi jumlah entri Action `Auto-Revert` Field `Group Manager — IT Infrastructure` pada Activity Log bertambah tepat satu dari baseline
37. Verifikasi jumlah entri Action `Remove (via Group Manager)` pada Activity Log sama dengan baseline (Auto-Revert tidak menulis entri per baris pola)
38. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Oscar Pranata {runId}-300`, muat ulang sampai entri tampil
39. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Oscar Pranata {runId}-300`, Action `Auto-Revert`, Field `Group Manager — IT Infrastructure`, Old Value `Assigned`, dan New Value `—`
40. Verifikasi jumlah entri Action `Auto-Revert` Field `Group Manager — IT Infrastructure` pada Modal Combined Changelog bertambah tepat satu dari baseline
41. Verifikasi jumlah entri Action `Remove (via Group Manager)` pada Modal Combined Changelog sama dengan baseline (Auto-Revert tidak menulis entri per baris pola)
42. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-924: Log Auto-Revert Total Control pada tiga surface log

43. Ganti akun: klik Logout pada akun saat ini
44. Login sebagai Ahmad Dahlan (`defaultUser_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_DU_PASSWORD`) lalu buka Fixed Asset > Settings > User
45. Catat jumlah entri Action `Auto-Revert` Field `Access Level` pada Tab Changelog Lina Marlina {runId}-300, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
46. Ketik Search `Lina Marlina {runId}-300`, tekan Enter, klik nama Lina Marlina {runId}-300, lalu buka Tab Role > Sub-tab Global Role
47. Hapus centang Update pada baris Manage accounting lalu klik `[Remove]` pada dialog
48. Tunggu aksi selesai (dialog tertutup)
49. Buka Detail Lina Marlina {runId}-300 > Tab Changelog, muat ulang sampai entri tampil
50. Verifikasi Tab Changelog memuat satu baris dengan Action `Auto-Revert`, Field `Access Level`, Old Value `Total Control`, New Value `—`, dan Modified By `Ahmad D` (format `[First Name] [Last Initial]`)
51. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan Name
52. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Tab Changelog Lina Marlina {runId}-300 bertambah tepat satu dari baseline
53. Buka Tab System Log aktor dan cari Name `Lina Marlina {runId}-300`, muat ulang sampai entri tampil
54. Verifikasi Tab System Log memuat satu baris dengan Action `Auto-Revert`, Object `Total Control`, Name `Lina Marlina {runId}-300`, Field `Access Level`, Old Value `Total Control`, dan New Value `—`
55. Verifikasi tabel Tab System Log tidak memuat kolom Modified By
56. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Tab System Log bertambah tepat satu dari baseline
57. Buka Activity Log dan cari Name `Lina Marlina {runId}-300`, muat ulang sampai entri tampil
58. Verifikasi Activity Log memuat satu baris dengan Action `Auto-Revert`, Object `Total Control`, Name `Lina Marlina {runId}-300`, Field `Access Level`, Old Value `Total Control`, New Value `—`, dan Modified By `Ahmad D`
59. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Activity Log bertambah tepat satu dari baseline
60. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Lina Marlina {runId}-300`, muat ulang sampai entri tampil
61. Verifikasi Modal Combined Changelog memuat satu baris dengan User Name `Lina Marlina {runId}-300`, Action `Auto-Revert`, Field `Access Level`, Old Value `Total Control`, dan New Value `—`
62. Verifikasi jumlah entri Action `Auto-Revert` Field `Access Level` pada Modal Combined Changelog bertambah tepat satu dari baseline
63. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-924 (aktor Default User) dikerjakan terakhir supaya penggantian akun hanya sekali, dan TC-FA-SU-925 dan TC-FA-SU-926 (aktor Total Control) mengikuti akun hook `before` (S-07, S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 4, 21, 23, 46, 48, 43, 44; langkah baseline jumlah entri (S-12): 1, 20, 45. Langkah 2, 21, dan 46 juga Search untuk menemukan baris target (R-16); langkah 43 dan 44 adalah ganti akun eksplisit.
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 49 dari 63 langkah, sisa 14 langkah.
- Asersi "satu entri" memakai baseline jumlah entri per Action dan Field dan Name bersuffix unik (S-12).
- Pengguna milik spec bernama sama dengan Pre-setup TC (Lina Marlina, Citra Lestari, Oscar Pranata) dengan suffix `{runId}-300` (S-06); akun aktor Lina Marlina Pre-setup #1 tidak menjadi target.
- Expected e TC-FA-SU-926 (Auto-Revert tidak menulis entri `Remove (via Group Manager)` per baris pola pada surface mana pun) ditulis sebagai selisih nol per surface (langkah 28, 33, 37, 41), tiap langkah didahului `Verifikasi` entri `Auto-Revert` surface yang sama sebagai anchor positif (langkah 25, 30, 35, 39; bagian 8b butir 2); modal Changelog User > Group Role dan > Transaction Role diasersi di spec 403 (TC-FA-SU-1098). Tidak ada spec absence yang memuat aksi nyata TC ini sehingga Verifikasi berbaseline ada di spec ini (S-05, S-12).
- Temuan untuk QA (S-15):
  - Post Condition TC-FA-SU-924, TC-FA-SU-925, dan TC-FA-SU-926 butir b (notifikasi in-app view-only terkirim ke pengguna target) tidak punya langkah observasi di ketiga TC dan tidak diasersi; notifikasi diasersi di spec lain (TC-FA-SU-935).
  - TC-FA-SU-924 menyebut "Hapus centang Update pada Manage accounting milik Lina Marlina" sebagai pemicu Auto-Revert Total Control dan TC-FA-SU-925 "Nyalakan switch Manage asset ID configuration milik Citra Lestari" sebagai pemicu Auto-Revert Read Only; spec mengikuti kedua pemicu itu apa adanya.
  - Langkah Uji tidak menyebut toast; spec tidak mengasersinya.
