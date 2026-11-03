---
id: TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1
title: "Home Group constraint: dialog D-10 dan pencabutan assignment (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-402
  - TC-FA-RP-403
  - TC-FA-RP-404
  - TC-FA-RP-405
  - TC-FA-RP-406
coverage:
  web: automated
---

# Home Group constraint: dialog D-10 dan pencabutan assignment (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage global user & role dengan Update (Hendra Wijaya, Pre-setup #6) `murGlobal_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MUR_GLOBAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Seeding state Gunawan Halim antar TC memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #17 (Gunawan Halim), #18 (pohon group). State Gunawan Halim (tanpa Home Group dan daftar assignment) disiapkan ulang lewat seeding API di awal tiap TC sesuai Aturan seed pool pengguna (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca jumlah entri Changelog Detail Role `Manage files` sebagai baseline dan membaca notifikasi in-app target (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: Home Group dan assignment Group Role Gunawan Halim. Hook `after` memulihkan Pre-setup #17 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-402: Penetapan Home Group constraint pada user dengan beberapa assignment di luar constraint, D-10 bentuk jamak

1. Siapkan Gunawan Halim tanpa Home Group, memegang `Manage files` di `Helpdesk`, `Manage group` di `Dock 1`, dan `Manage purchase` di `Data Center` lewat sesi API hingga tersimpan
2. Buka Settings > User > Detail Gunawan Halim
3. Klik field Home Group lalu pilih group `Data Center` pada tree dan klik `[Select]`
4. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`, Body `• Manage files — Helpdesk` `• Manage group — Dock 1` lalu `Setting the Home Group constraint to Data Center for Gunawan Halim will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`, serta tombol `[Cancel]` dan `[Revoke]`
5. Verifikasi assignment `Manage purchase` di `Data Center` tidak didaftar pada dialog
6. Klik `[Cancel]`

### TC-FA-RP-403: Penetapan Home Group constraint dengan satu assignment di luar constraint, D-10 bentuk tunggal

7. Siapkan Gunawan Halim tanpa Home Group, memegang `Manage files` di `Helpdesk` saja, lewat sesi API hingga tersimpan
8. Buka Settings > User > Detail Gunawan Halim
9. Klik field Home Group lalu pilih group `Data Center` dan klik `[Select]`
10. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`, Body `• Manage files — Helpdesk` lalu `Setting the Home Group constraint to Data Center for Gunawan Halim will revoke this assignment outside this group.` dan `Are you sure you want to revoke it?`, serta tombol `[Cancel]` dan `[Revoke]`
11. Klik `[Cancel]`

### TC-FA-RP-404: Confirm D-10, constraint tersimpan dan assignment di luar constraint dicabut secara silent

12. Siapkan Gunawan Halim tanpa Home Group, memegang `Manage files` di `Helpdesk` dan di `Data Center`, lewat sesi API hingga tersimpan
13. Catat jumlah entri Changelog Detail Role `Manage files` sebagai baseline lewat kemampuan baca
14. Buka Settings > User > Detail Gunawan Halim
15. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
16. Klik `[Revoke]`
17. Verifikasi Home Group Gunawan Halim tersimpan `Data Center`
18. Buka Detail Role `Manage files` dari Tab `System` pada Settings > Role & Permission
19. Klik node `All Groups` pada Sidebar Group Tree
20. Verifikasi baris Gunawan Halim di `Data Center` tetap ada
21. Verifikasi baris Gunawan Halim di `Helpdesk` hilang
22. Buka Changelog Detail Role `Manage files`
23. Verifikasi modal Changelog tampil dengan sedikitnya satu entri
24. Verifikasi selisih jumlah entri Changelog Detail Role `Manage files` terhadap baseline langkah 13 nol sehingga Changelog tidak memuat entri pencabutan itu
25. Verifikasi tidak ada notifikasi in-app baru untuk Gunawan Halim lewat kemampuan baca
26. Tutup modal Changelog

### TC-FA-RP-405: Cancel D-10, tidak ada perubahan

27. Siapkan Gunawan Halim tanpa Home Group, memegang `Manage files` di `Helpdesk`, lewat sesi API hingga tersimpan
28. Buka Settings > User > Detail Gunawan Halim
29. Klik field Home Group, pilih `Data Center`, klik `[Select]`
30. Klik `[Cancel]` pada dialog D-10
31. Verifikasi Home Group Gunawan Halim tidak berubah
32. Buka Detail Role `Manage files` dari Tab `System` pada Settings > Role & Permission
33. Klik node `All Groups` pada Sidebar Group Tree
34. Verifikasi baris `Manage files` Gunawan Halim di `Helpdesk` tetap ada

### TC-FA-RP-406: Penetapan constraint tanpa assignment di luar constraint tidak menampilkan dialog

35. Siapkan Gunawan Halim tanpa Home Group, memegang `Manage files` hanya di `Rack A1`, lewat sesi API hingga tersimpan
36. Buka Settings > User > Detail Gunawan Halim
37. Klik field Home Group, pilih `Data Center`, klik `[Select]`
38. Verifikasi constraint tersimpan `Data Center`
39. Verifikasi dialog D-10 tidak tampil
40. Buka Detail Role `Manage files` dari Tab `System` pada Settings > Role & Permission
41. Klik node `All Groups` pada Sidebar Group Tree
42. Verifikasi baris Gunawan Halim di `Rack A1` tetap ada

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 7, 12, 27, dan 35 (menyiapkan state Gunawan Halim per TC lewat sesi API sesuai Pre-setup #32), langkah 6 dan 11 (menutup dialog D-10 dengan `[Cancel]` karena TC hanya mengasersi dialog), langkah 13 (baseline log, S-12), langkah 26 (menutup modal Changelog), langkah 18 sampai 19, 32 sampai 33, dan 40 sampai 41 (navigasi ke Detail Role untuk mengamati baris). Langkah Search untuk menemukan Gunawan Halim pada Settings > User tidak ditulis eksplisit karena TC menulis "Buka Settings > User > Detail Gunawan Halim" sebagai satu langkah.
- `P-1` (TC-FA-RP-404): Expected butir c ("Changelog tidak memuat entri pencabutan itu dan tidak ada notifikasi") adalah asersi absence yang bergantung pada state berat yang baru dibangun langkah 12 sampai 16 (pencabutan assignment oleh konfirmasi D-10), sehingga tetap di spec ini dengan baseline (langkah 13 dan 24) dan anchor positif (langkah 23), bukan di spec absence.
- Klausa Expected TC-FA-RP-402 butir a memuat dua bullet pada satu dialog D-10 dan kalimat penutup; ditulis satu `Verifikasi` dialog karena judul, isi, dan tombol disebut utuh (S-01).
- Teks bertanda `copy usulan, PRD 12 #1` (Body dialog D-10) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Alasan di atas sekitar 35 langkah (42 langkah): lima TC satu topik (D-10 pada Detail User Gunawan Halim) yang masing-masing menyiapkan state Gunawan Halim dengan satu langkah seeding dan memakai halaman Detail User dan Detail Role yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Pre-setup #17 menyatakan Gunawan Halim ber-Home Group `Data Center`, sedangkan TC-FA-RP-402 sampai TC-FA-RP-406 menyatakan "tanpa Home Group"; spec menyiapkan state tiap TC lewat seeding API.
  - TC-FA-RP-404 butir c tidak menyebut cara mengamati "tidak ada notifikasi untuk Gunawan Halim" tanpa login sebagai Gunawan Halim; spec memakai kemampuan baca notifikasi in-app yang disediakan tim FE/BE (langkah 25).
  - TC-FA-RP-405 butir a ("Home Group tidak berubah") tidak menyebut cara mengamatinya; spec memakai tampilan Home Group pada Detail User (langkah 31).
