---
id: TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2
title: "Home Group constraint: dialog D-10 dan pencabutan assignment (2/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-407
  - TC-FA-RP-408
  - TC-FA-RP-409
  - TC-FA-RP-410
  - TC-FA-RP-412
  - TC-FA-RP-1039
coverage:
  web: automated
---

# Home Group constraint: dialog D-10 dan pencabutan assignment (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Manage global user & role dengan Update (Hendra Wijaya, Pre-setup #6) `murGlobal_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MUR_GLOBAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Role yang diuji untuk TC-FA-RP-412 (langkah 40 sampai 51, ganti akun eksplisit untuk dua akun terakhir):

  | Role | Pre-setup | Akun | Env |
  |---|---|---|---|
  | Manage global user & role (Update) | #6 | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
  | Default User | #1 | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
  | Total Control | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Seeding state pengguna antar TC memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #17 (Gunawan Halim, Hesti Rahma, Indra Kusuma), #18 (pohon group), #19 (Gunawan Halim sebagai Asset Admin pada `Helpdesk` sub-tab `Disposal` disiapkan untuk TC-FA-RP-409). State tiap pengguna (Home Group dan daftar assignment) disiapkan ulang lewat seeding API di awal tiap TC sesuai Aturan seed pool pengguna (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: Home Group dan assignment Group Role, Group Manager, dan Role Transaksi pada Gunawan Halim, Hesti Rahma, dan Indra Kusuma. Hook `after` memulihkan Pre-setup #17 dan #19 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-407: Melepas constraint tidak mengembalikan assignment yang sudah dicabut

1. Siapkan Gunawan Halim ber-Home Group `Data Center` tanpa baris `Manage files` di `Helpdesk` (assignment sudah dicabut sebelumnya) lewat sesi API hingga tersimpan
2. Buka Settings > User > Detail Gunawan Halim
3. Hapus Home Group (kosongkan constraint)
4. Klik `[Save]`
5. Buka Detail Role `Manage files` dari Tab `System` pada Settings > Role & Permission
6. Klik node `All Groups` pada Sidebar Group Tree
7. Verifikasi sedikitnya satu baris lain tampil pada Detail Role `Manage files`
8. Verifikasi baris Gunawan Halim di `Helpdesk` tidak kembali
9. Verifikasi tidak ada riwayat role yang dicabut yang ditampilkan pada Detail Role `Manage files`

### TC-FA-RP-408: Mengubah constraint dari satu group ke group lain mencabut assignment di luar constraint baru

10. Siapkan Gunawan Halim ber-Home Group `Data Center` memegang `Manage files` di `Data Center` lewat sesi API hingga tersimpan
11. Buka Settings > User > Detail Gunawan Halim
12. Klik field Home Group lalu pilih `Helpdesk` dan klik `[Select]`
13. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`, Body `• Manage files — Data Center` lalu `Setting the Home Group constraint to Helpdesk for Gunawan Halim will revoke this assignment outside this group.` dan `Are you sure you want to revoke it?`, serta tombol `[Cancel]` dan `[Revoke]`
14. Klik `[Revoke]`
15. Buka Detail Role `Manage files` dari Tab `System` pada Settings > Role & Permission
16. Klik node `All Groups` pada Sidebar Group Tree
17. Verifikasi sedikitnya satu baris lain tampil pada Detail Role `Manage files`
18. Verifikasi baris Gunawan Halim di `Data Center` hilang

### TC-FA-RP-409: Penetapan constraint tidak mencabut penugasan Role Transaksi di luar constraint

19. Siapkan Gunawan Halim tanpa Home Group ditugaskan Asset Admin pada `Helpdesk` sub-tab `Disposal` lewat sesi API hingga tersimpan
20. Buka Settings > User > Detail Gunawan Halim
21. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
22. Buka Tab `Transaction Role` pada Settings > Role & Permission
23. Klik node `Helpdesk` pada Sidebar Group Tree
24. Klik sub-tab `Disposal`
25. Verifikasi Gunawan Halim tetap tampil sebagai Asset Admin pada `Helpdesk`

### TC-FA-RP-410: Penetapan constraint mencabut penugasan Group Manager di luar constraint

26. Siapkan Hesti Rahma tanpa Home Group ditugaskan Group Manager di `Data Center` lewat sesi API hingga tersimpan
27. Buka Settings > User > Detail Hesti Rahma
28. Klik field Home Group lalu pilih `Logistics Warehouse` dan klik `[Select]`
29. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`, Body `• Group Manager — Data Center` lalu `Setting the Home Group constraint to Logistics Warehouse for Hesti Rahma will revoke this assignment outside this group.` dan `Are you sure you want to revoke it?`, serta tombol `[Cancel]` dan `[Revoke]`
30. Klik `[Revoke]`
31. Verifikasi Home Group Hesti Rahma tersimpan `Logistics Warehouse`
32. Buka Tab `Group Manager` pada Settings > Role & Permission
33. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
34. Verifikasi baris Hesti Rahma di `Data Center` tidak ada di Tab `Group Manager`

### TC-FA-RP-1039: D-10 memuat Group Role dan penugasan Group Manager sekaligus

35. Siapkan Gunawan Halim tanpa Home Group memegang `Manage files` di `Helpdesk` dan ditugaskan Group Manager di `Dock 1` lewat sesi API hingga tersimpan
36. Buka Settings > User > Detail Gunawan Halim
37. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
38. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`, Body `• Manage files — Helpdesk` `• Group Manager — Dock 1` lalu `Setting the Home Group constraint to Data Center for Gunawan Halim will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`, serta tombol `[Cancel]` dan `[Revoke]`
39. Klik `[Cancel]`

### TC-FA-RP-412: Default User, Total Control, dan Manage user & role Global dapat menetapkan Home Group constraint

40. Siapkan Indra Kusuma tanpa Home Group lewat sesi API hingga tersimpan
41. Buka Settings > User > Detail Indra Kusuma
42. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
43. Verifikasi constraint tersimpan `Data Center`
44. Verifikasi dialog D-10 tidak tampil

Untuk setiap akun Default User dan Total Control pada tabel "Role yang diuji" (langkah 45 sampai 51):

45. Logout dari akun yang sedang aktif
46. Login sebagai akun pada tabel "Role yang diuji"
47. Siapkan Indra Kusuma tanpa Home Group lewat sesi API hingga tersimpan
48. Buka Settings > User > Detail Indra Kusuma
49. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
50. Verifikasi constraint tersimpan `Data Center`
51. Verifikasi dialog D-10 tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan, dengan TC-FA-RP-412 di akhir karena memuat ganti akun.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 10, 19, 26, 35, 40, dan 47 (menyiapkan state per TC lewat sesi API sesuai Pre-setup #32), langkah 14 dan 30 (`[Revoke]` adalah langkah TC), langkah 39 (menutup dialog D-10 dengan `[Cancel]` karena TC hanya mengasersi dialog), langkah 5 sampai 6, 15 sampai 16, 22 sampai 24, dan 32 (navigasi untuk mengamati hasil). Verifikasi pembanding pada langkah 7, 17, dan 33 adalah anchor absence atas langkah 8, 18, dan 34 (bagian 8b butir 2).
- Langkah 45 sampai 51 diulang untuk Default User lalu Total Control sesuai kalimat TC ("diulang pada akun Default User dan Total Control dengan hasil sama"); ekspansi memberi 58 langkah efektif.
- Alasan di atas sekitar 35 langkah (51 langkah nominal, 58 efektif): enam TC satu topik (Home Group constraint pada Detail User) yang masing-masing menyiapkan state dengan satu langkah seeding; TC-FA-RP-412 mengulang tujuh langkah pada dua akun. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Teks bertanda `copy usulan, PRD 12 #1` (Body dialog D-10) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - Pre-setup #17 menyatakan Gunawan Halim ber-Home Group `Data Center` dan Hesti Rahma ber-Home Group `Logistics Warehouse`, sedangkan TC-FA-RP-408 sampai TC-FA-RP-410 menyatakan state berbeda per TC; spec menyiapkan state tiap TC lewat seeding API.
  - TC-FA-RP-407 butir "tidak ada riwayat role yang dicabut yang ditampilkan" tidak menyebut lokasi tampilan; spec mengasersi pada Detail Role `Manage files` (langkah 9).
  - TC-FA-RP-407 menyebut "lalu simpan" tanpa label tombol; spec memakai `[Save]` mengikuti konvensi label form Edit.
  - TC-FA-RP-412 menyebut Manage user & role Global pada judul tetapi hanya meminta pengulangan pada Default User dan Total Control; Hendra Wijaya (Manage global user & role) menjadi akun pertama.
