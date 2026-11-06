---
id: TC-FA-RP-E2E-121-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-3
title: "Home Group constraint: dialog D-10 dan pencabutan assignment (3/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-411
  - TC-FA-RP-1040
  - TC-FA-RP-1041
  - TC-FA-RP-1097
coverage:
  web: automated
---

# Home Group constraint: dialog D-10 dan pencabutan assignment (3/3)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji dan akun (ganti akun eksplisit pada langkah 25 dan 26, 30 dan 31, 35 dan 36, 40 dan 41; akun pertama login di hook `before`):

  | Role | Pre-setup | Akun | Env |
  |---|---|---|---|
  | Manage global user & role (Update), akun awal | #6 | `murGlobal_automated_{namaCompany}@qwertysystem.net` (Hendra Wijaya) | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
  | Pengguna target TC-FA-RP-1040 | #17 | akun login Gunawan Halim; email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE | `Spectra.env.FA_GUNAWAN_PASSWORD` |
  | Group Manager | #5 | `groupManager_automated_{namaCompany}@qwertysystem.net` (Fajar Nugroho) | `Spectra.env.FA_GM_PASSWORD` |
  | Manage user & role (Group, Update) | #7 | `murGroup_automated_{namaCompany}@qwertysystem.net` (Gita Maharani) | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
  | Total Control | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (Siti Rahmawati) | `Spectra.env.FA_TC_PASSWORD` |

  Landing halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control) untuk akun awal. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Seeding state pengguna antar TC memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15, #17 (Gunawan Halim, Hesti Rahma), #18 (pohon group). State tiap pengguna (Home Group dan daftar assignment) disiapkan ulang lewat seeding API di awal tiap TC sesuai Aturan seed pool pengguna (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca jumlah entri Changelog Detail Role `Manage files` dan jumlah notifikasi in-app Gunawan Halim sebagai baseline dan hasil (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: Home Group dan assignment Group Role dan Group Manager pada Gunawan Halim dan Hesti Rahma. Hook `after` memulihkan Pre-setup #17 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-1041: Cancel D-10 yang memuat penugasan Group Manager

1. Siapkan Hesti Rahma tanpa Home Group ditugaskan Group Manager di `Data Center` lewat sesi API hingga tersimpan
2. Buka Settings > User > Detail Hesti Rahma
3. Klik field Home Group, pilih `Logistics Warehouse`, klik `[Select]`
4. Klik `[Cancel]` pada dialog D-10
5. Verifikasi Home Group Hesti Rahma tidak berubah (tanpa constraint)
6. Buka Tab `Group Manager` pada Settings > Role & Permission
7. Verifikasi baris Hesti Rahma di `Data Center` tetap ada di Tab `Group Manager`

### TC-FA-RP-1040: Confirm D-10 dengan Group Role dan Group Manager

8. Siapkan Gunawan Halim tanpa Home Group memegang `Manage files` di `Helpdesk` dan ditugaskan Group Manager di `Dock 1`, dengan akun login, lewat sesi API hingga tersimpan
9. Catat jumlah entri Changelog Detail Role `Manage files` selain entri `Remove (via Group Manager)` dan jumlah notifikasi in-app Gunawan Halim sebagai baseline lewat kemampuan baca
10. Buka Settings > User > Detail Gunawan Halim
11. Klik field Home Group lalu pilih `Data Center`, klik `[Select]`
12. Klik `[Revoke]`
13. Verifikasi Home Group Gunawan Halim tersimpan `Data Center`
14. Buka Detail Role `Manage files` dari Tab `System` pada Settings > Role & Permission
15. Klik node `All Groups` pada Sidebar Group Tree
16. Verifikasi sedikitnya satu baris lain tampil pada Detail Role `Manage files`
17. Verifikasi baris `Manage files` Gunawan Halim di `Helpdesk` hilang
18. Buka Changelog Detail Role `Manage files`
19. Verifikasi modal Changelog memuat entri `Remove (via Group Manager)` untuk baris pola GM Gunawan Halim di `Dock 1` (satu entri per baris, Modified By `Hendra W`)
20. Verifikasi selisih jumlah entri Changelog Detail Role `Manage files` selain `Remove (via Group Manager)` terhadap baseline langkah 9 nol sehingga tidak ada entri log per baris Group Role itu
21. Tutup modal Changelog
22. Buka Tab `Group Manager` pada Settings > Role & Permission
23. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
24. Verifikasi baris Gunawan Halim di `Dock 1` tidak ada di Tab `Group Manager`
25. Logout dari akun Manage global user & role dengan Update
26. Login sebagai Gunawan Halim
27. Buka Overlay Notifikasi
28. Verifikasi notifikasi untuk penugasan Group Manager `Dock 1` tampil
29. Verifikasi jumlah notifikasi baru Gunawan Halim terhadap baseline langkah 9 tepat satu sehingga tidak ada notifikasi untuk baris Group Role

### TC-FA-RP-411: Kontrol Home Group constraint Hidden bagi Group Manager dan Manage user & role tingkat Group

30. Logout dari akun Gunawan Halim
31. Login sebagai Group Manager (Fajar Nugroho)
32. Buka Settings > User > Detail Gunawan Halim
33. Verifikasi field Home Group tidak dapat diubah
34. Verifikasi aksi `Edit Home Group` Hidden bagi Group Manager
35. Logout dari akun Group Manager
36. Login sebagai Manage user & role tingkat Group (Gita Maharani)
37. Buka Settings > User > Detail Gunawan Halim
38. Verifikasi field Home Group tidak dapat diubah
39. Verifikasi aksi `Edit Home Group` Hidden bagi Manage user & role tingkat Group

### TC-FA-RP-1097: Edit Home Group bulk, dialog D-10 tampil per pengguna dengan nama pengguna pada kalimat

40. Logout dari akun Manage user & role tingkat Group
41. Login sebagai Total Control
42. Siapkan Gunawan Halim memegang Group Role `Manage files` di `Helpdesk` dan Hesti Rahma Group Manager di `Data Center`, keduanya tanpa Home Group constraint, lewat sesi API hingga tersimpan
43. Buka Fixed Asset > Settings > User
44. Centang Gunawan Halim dan Hesti Rahma
45. Klik `Bulk Action` lalu `Edit Home Group`
46. Pilih group `Logistics Warehouse` lalu simpan
47. Verifikasi dialog D-10 tampil per pengguna (satu dialog untuk tiap pengguna), bukan satu dialog gabungan
48. Verifikasi dialog untuk Gunawan Halim memuat bullet `• Manage files — Helpdesk` dan kalimat `Setting the Home Group constraint to Logistics Warehouse for Gunawan Halim will revoke this assignment outside this group.`
49. Klik `[Cancel]` pada dialog Gunawan Halim
50. Verifikasi dialog untuk Hesti Rahma memuat bullet `• Group Manager — Data Center` dan kalimat `Setting the Home Group constraint to Logistics Warehouse for Hesti Rahma will revoke this assignment outside this group.`
51. Klik `[Cancel]` pada dialog Hesti Rahma

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 1041, 1040, 411, 1097 agar akun aktor berurutan (Hendra Wijaya, Gunawan Halim, Group Manager, Manage user & role Group, Total Control) dengan satu ganti akun tiap pergantian; spec ditulis per blok akun karena ganti akun menuntut Step eksplisit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, dan 42 (menyiapkan state per TC lewat sesi API sesuai Pre-setup #32), langkah 9 (baseline, S-12), langkah 21 (menutup modal Changelog), langkah 49 dan 51 (menutup dialog D-10 dengan `[Cancel]` karena TC hanya mengasersi dialog), langkah 6, 14 sampai 15, dan 22 (navigasi untuk mengamati hasil). Verifikasi pembanding pada langkah 16, 19, dan 23 adalah anchor absence atas asersi absence berikutnya (bagian 8b butir 2).
- `P-1` (TC-FA-RP-1040): klausa absence ("tidak ada entri log per baris Group Role", "tidak ada notifikasi untuk baris Group Role") bergantung pada state berat yang baru dibangun aksi pada langkah 8 sampai 12 (penetapan constraint dan pencabutan assignment dalam satu transaksi), sehingga tetap di spec ini dengan baseline langkah 9 yang dibandingkan pada langkah 20 dan 29 serta anchor positif (langkah 16 dan 19), bukan di spec absence.
- Pembagian TC lintas spec: klausa absence "tidak ada entri log dan tidak ada notifikasi" TC-FA-RP-1041 butir b diasersi di spec absence 291 dengan aksi nyata, baseline, dan anchor positif sendiri; id TC-FA-RP-1041 tetap di `sourceTc` spec ini dan spec 291 (S-05). Spec ini mengasersi Home Group tidak berubah dan baris Group Manager tetap ada.
- Pada TC-FA-RP-411 pengulangan pada akun Manage user & role tingkat Group dipakai sesuai kalimat TC ("diulang pada akun Manage user & role tingkat Group dengan hasil sama"); Group Manager dan Manage user & role tingkat Group ditulis sebagai dua blok akun karena ganti akun menuntut Step eksplisit.
- Gunawan Halim pada TC-FA-RP-1040 adalah akun yang diasersi notifikasinya (objek asersi), bukan pemicu state; dipakai lewat ganti akun berurutan (langkah 25 dan 26), bukan konteks paralel.
- Alasan di atas sekitar 35 langkah (51 langkah): empat TC satu topik (Home Group constraint D-10) dengan lima akun berbeda yang masing-masing menuntut ganti akun eksplisit; tiap blok akun berdiri sendiri. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Teks bertanda `copy usulan, PRD 12 #1` (kalimat dialog D-10 pada TC-FA-RP-1097) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - Email akun login Gunawan Halim tidak tertulis di Pre-setup #17; akun disediakan tim FE. Nama env `FA_GUNAWAN_PASSWORD` sudah terdaftar di `suite.md`.
  - TC-FA-RP-1097 butir a menyebut dialog tampil "per pengguna" tanpa menjelaskan urutan dan mekanik pergantian dialog; spec menutup dialog pertama dengan `[Cancel]` sebelum mengasersi dialog kedua (langkah 49).
  - TC-FA-RP-1040 butir b yang baru menyebut entri `Remove (via Group Manager)` per baris pola GM di `Dock 1` tanpa menyebut Object, Field, Old/New Value maupun Role yang memuatnya; spec hanya mengasersi keberadaan entri di Changelog Detail Role `Manage files` dan Modified By aktor (Hendra Wijaya, `Hendra W`; langkah 19), dan memisahkannya dari asersi tidak ada entri log baris Group Role lewat baseline yang mengecualikan entri `Remove (via Group Manager)` (langkah 9 dan 20). Perlu konfirmasi QA.
  - TC-FA-RP-1040 butir d ("hanya satu notifikasi") tidak memberi teks notifikasi Group Manager `Dock 1`; spec mengasersi keberadaan dan jumlahnya saja (langkah 28 dan 29).
