---
id: TC-FA-SU-E2E-066-group-manager-save-0-grup-auto-revert-beberapa-grup-dan-auto-revert-tier-dari-popup
title: "Group Manager: Save 0 Grup, Auto-Revert Beberapa Grup, dan Auto-Revert Tier dari Popup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-215
  - TC-FA-SU-216
  - TC-FA-SU-217
coverage:
  web: automated
---

# Group Manager: Save 0 Grup, Auto-Revert Beberapa Grup, dan Auto-Revert Tier dari Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah terakhir): Group Manager Oscar Pranata (Pre-setup #9), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_GM_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Oscar Pranata, Group Manager IT Infrastructure dan Accounts Payable dengan Group Role `Manage group` penuh pada kedua grup (Pre-setup #9; "role penopang" pada TC adalah `Manage group`); Lina Marlina, Total Control (Pre-setup #1 dan #23: Manage files pada seluruh group, CRUD penuh), dan Citra Lestari, Read Only (Pre-setup #3 dan #23: Manage files pada seluruh group, Read saja), target TC-FA-SU-217.
- Data uji: Save dengan 0 grup (TC-FA-SU-215 dan 216); popup Assign Group Role `Manage files`, baris `Branch Surabaya`: centang Delete dihapus pada Lina Marlina lalu dicentang pada Citra Lestari (TC-FA-SU-217).
- Kemampuan teknis: seed API untuk memulihkan status Group Manager dan penugasan Oscar Pranata serta tier Total Control Lina Marlina dan tier Read Only Citra Lestari (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target dan jumlah notifikasi in-app Oscar Pranata sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager dan penugasan Oscar Pranata, serta tier Total Control Lina Marlina (akun aktor default suite) dan tier Read Only Citra Lestari; dipulihkan ke Pre-setup #1, #3, #9, dan #23 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-215: Save dengan 0 grup pada target Group Manager: dialog Auto-Revert D-05c sebelum penugasan dilepas

1. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role role penopang Manage group
2. Klik `[Clear Field]` lalu klik `[Save]`
3. Verifikasi dialog Title `Remove Group Manager` tampil sebelum penyimpanan
4. Klik `[Remove]`
5. Verifikasi seluruh penugasan grup role penopang Oscar terlepas (kolom Group baris Manage group menjadi `—`)
6. Verifikasi status Group Manager Oscar terlepas (banner Group Manager hilang)
7. Pulihkan status Group Manager dan penugasan Oscar Pranata ke Pre-setup #9 lewat seed API

### TC-FA-SU-216: Auto-Revert lebih dari satu grup Group Manager dalam satu edit: satu dialog D-05d dan satu toast T-06c

8. Catat jumlah entri `Auto-Revert` Oscar Pranata pada Tab Changelog serta jumlah notifikasi in-app Oscar Pranata sebagai baseline
9. Buka ulang Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role role penopang Manage group yang menopang dua grup Group Manager
10. Klik `[Clear Field]` lalu klik `[Save]`
11. Verifikasi satu dialog Title `Remove Group Manager` dengan Body bullet `• Oscar Pranata`, kalimat `This change will remove Group Manager status for these groups:` diikuti bullet IT Infrastructure dan Accounts Payable, lalu `Are you sure you want to remove it?`
12. Tunggu toast lama hilang otomatis
13. Klik `[Remove]`
14. Verifikasi satu toast "Success, permissions have been updated. Oscar Pranata is no longer Group Manager."
15. Buka Tab Changelog, Search `Oscar Pranata`, tekan Enter, lalu muat ulang sampai entri tampil
16. Verifikasi satu entri `Auto-Revert` per grup (IT Infrastructure dan Accounts Payable), dua entri bertambah dibanding baseline pada Tab Changelog
17. Pulihkan status Group Manager dan penugasan Oscar Pranata ke Pre-setup #9 lewat seed API

### TC-FA-SU-217: Save popup Assign Group Role pada target Total Control atau Read Only yang menyimpang dari pola Group Role: dialog Auto-Revert D-05, tier lepas, dan banner hilang

18. Buka Detail Lina Marlina > Tab Role > Sub-tab Group Role
19. Buka popup Assign Group Role Manage files lalu hapus centang Delete pada Branch Surabaya
20. Klik `[Save]`
21. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control` tampil sebelum penyimpanan
22. Verifikasi Body bullet `• Lina Marlina`
23. Verifikasi kalimat `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited.`
24. Verifikasi penutup `Are you sure you want to remove it?`
25. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
26. Verifikasi dialog Remove Group Role biasa tidak tampil
27. Klik `[Remove]`
28. Verifikasi toast T-06a "Success, permissions have been updated. Lina Marlina is no longer Total Control."
29. Verifikasi banner tier hilang di Sub-tab Group Role
30. Klik Sub-tab Global Role
31. Verifikasi banner tier hilang di Sub-tab Global Role
32. Klik Sub-tab Transaction Role
33. Verifikasi banner tier hilang di Sub-tab Transaction Role
34. Verifikasi tingkat akses Lina Marlina kosong
35. Pulihkan tier Total Control Lina Marlina ke Pre-setup #1 dan #23 lewat seed API
36. Buka Detail Citra Lestari > Tab Role > Sub-tab Group Role
37. Buka popup Assign Group Role Manage files lalu centang Delete pada Branch Surabaya
38. Klik `[Save]`
39. Verifikasi dialog Auto-Revert D-05b dengan Title `Remove Read Only` tampil sebelum penyimpanan
40. Verifikasi kalimat `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited.`
41. Verifikasi dialog Remove Group Role biasa tidak tampil
42. Klik `[Remove]`
43. Verifikasi toast T-06a "Success, permissions have been updated. Citra Lestari is no longer Read Only."
44. Verifikasi banner tier hilang di Sub-tab Group Role
45. Klik Sub-tab Global Role
46. Verifikasi banner tier hilang di Sub-tab Global Role
47. Klik Sub-tab Transaction Role
48. Verifikasi banner tier hilang di Sub-tab Transaction Role
49. Verifikasi tingkat akses Citra Lestari kosong
50. Pulihkan tier Read Only Citra Lestari ke Pre-setup #3 dan #23 lewat seed API
51. Logout lalu login sebagai Group Manager Oscar Pranata
52. Buka panel notifikasi
53. Verifikasi notifikasi in-app view-only tetap satu per grup (dua notifikasi baru dibanding baseline)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan, kecuali asersi notifikasi TC-FA-SU-216 butir c yang diletakkan pada langkah terakhir spec agar satu kali ganti akun cukup; baseline notifikasi dicatat sebelum TC-FA-SU-216 sehingga notifikasi TC-FA-SU-215 tidak ikut terhitung.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7, 8, 12, 17, 30, 32, 35, 36, 45, 47, 50 dan 51. Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #1, #3, #9, dan #23 (S-06, S-09).
- Alasan di atas sekitar 35 langkah: seluruh TC satu topik (Auto-Revert pada target Group Manager, Total Control, dan Read Only), tiap TC mengubah state sendiri dan dipulihkan sebelum TC berikutnya, dan kegagalan satu TC tidak membuat TC lain kehilangan makna; langkah TC-FA-SU-217 banyak karena Expected bermajemuk dua target (dialog D-05a dan D-05b, toast, banner di tiga sub-tab) yang wajib satu `Verifikasi` per klausa (S-01).
- Langkah pola baca-log: langkah 15 dan 16. Search `Oscar Pranata` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16). Langkah terakhir spec mengganti akun ke Group Manager Oscar Pranata (ganti akun eksplisit, S-07).
- Temuan untuk QA:
  - TC-FA-SU-217 butir e ("Group Role bagian pola tier") bukan kalimat penuh dan tidak punya Verifikasi tersendiri; spec tidak mengasersinya.
  - TC-FA-SU-217 butir a menyebut "tidak ada request simpan sebelum konfirmasi" tanpa langkah observasi; spec hanya mengasersi dialog tampil sebelum penyimpanan.
  - TC-FA-SU-217 butir d menyebut toast T-06a dan banner hilang untuk kedua target; spec mengasersi banner pada tiga sub-tab untuk Lina Marlina dan Citra Lestari.
  - TC-FA-SU-217 Post Condition butir b dan c (entri `Edit` dan `Auto-Revert` pada tiga surface log; notifikasi in-app ke Lina Marlina dan Citra Lestari) tidak punya langkah observasi dan tidak diasersi; butir d (pemulihan oleh automation baseline) dipenuhi lewat langkah 35 dan 50.
  - TC-FA-SU-215 tidak menyebut Expected untuk log dan notifikasi (hanya Post Condition tanpa langkah observasi); Post Condition TC-FA-SU-215 dan 217 tidak diasersi.
  - TC-FA-SU-216 butir c ("notifikasi tetap satu per grup") tidak menyebut cara menghitung notifikasi; spec memakai baseline jumlah notifikasi dan panel notifikasi Oscar Pranata.
