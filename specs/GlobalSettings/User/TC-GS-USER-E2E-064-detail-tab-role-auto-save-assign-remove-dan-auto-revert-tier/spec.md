---
id: TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier
title: "User Detail Tab Role: Auto-save per Cell, Assign Role, Dialog Remove Access (Cancel dan Remove), dan Auto-revert Tier Total Control dan Read Only, serta Edit oleh Holder Update-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-376
  - TC-GS-USER-377
  - TC-GS-USER-379
  - TC-GS-USER-380
  - TC-GS-USER-381
  - TC-GS-USER-1020
  - TC-GS-USER-383
coverage:
  web: automated
---

# User Detail Tab Role: Auto-save per Cell, Assign Role, Dialog Remove Access (Cancel dan Remove), dan Auto-revert Tier Total Control dan Read Only, serta Edit oleh Holder Update-Only

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor (ganti akun eksplisit di Test Steps):
  - Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`): aktor pertama, login di hook `before` (akun default suite).
  - Manage user and role (Update-Only: R+U) (Bayu Saputra) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 6; kredensial `Spectra.env.GS_UPDATE_PASSWORD`): dipakai TC-GS-USER-383.
  - Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_UPDATE_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (dibaca, tidak diubah): tidak ada user Pre-setup yang menjadi target tulis (S-06); role katalog `Manage files`, `Manage hardware`, dan `Manage TAG` serta role `Manage user and role` dibaca dan tidak diubah definisinya.
- Data Dinamis, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`:
  - `Andi Wijaya {runId}-064`, email `andiwijaya+{runId}-064@qwertysystem.net`: tier Total Control, checkbox `Delete` baris `Manage files` tercentang (TC-GS-USER-379, 380, dan 1020).
  - `Doni Pratama {runId}-064`, email `donipratama+{runId}-064@qwertysystem.net`: tier Read Only (TC-GS-USER-381).
  - `Ahmad Fauzi {runId}-064`, email `ahmadfauzi+{runId}-064@qwertysystem.net`: holder `Manage user and role` (non-tier); `Manage TAG` dan `Manage hardware` belum di-assign (TC-GS-USER-376 dan 377).
  - `Ahmad Fauzi 2 {runId}-064`, email `ahmadfauzi2+{runId}-064@qwertysystem.net`: holder `Manage user and role` (non-tier), target Normal; `Manage TAG` belum di-assign (TC-GS-USER-383).
- Kemampuan teknis (disediakan tim FE/BE): seeding user dengan assignment role dan tier (Total Control, Read Only, holder non-tier) lewat API (nama endpoint ditentukan tim FE di tahap script; TC, PRD, dan Tabel Pre-setup tidak menyebut mekanismenya); membaca halaman Global Settings > Role & Permission untuk daftar user pada role `Manage hardware` (TC-GS-USER-377).
- State global yang diubah: tidak ada. Yang berubah hanya assignment role dan tier pada empat user seed milik spec. Hook `after` (tetap berjalan walau spec gagal di tengah) menghapus empat user seed (sehingga keanggotaan role `Manage hardware` dan `Manage TAG` pulih) dan mengembalikan sesi ke akun default suite.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-379: Edit menyimpang pattern tier memunculkan dialog Remove Access

2. Klik icon Search, ketik `Andi Wijaya {runId}-064`, tekan Enter
3. Klik Name `Andi Wijaya {runId}-064` di User List
4. Klik Tab `Role`
5. Uncheck Delete baris `Manage files`
6. Verifikasi dialog Title `Remove Access`
7. Verifikasi body dialog `• Andi Wijaya {runId}-064`
8. Verifikasi body dialog `Editing this permission will remove Total Control access from this user. Are you sure you want to remove it?`
9. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`

### TC-GS-USER-380: Cancel dialog Remove Access mengembalikan checkbox

10. Klik `[Cancel]` (langkah 1 sampai 3 TC-GS-USER-380 dipenuhi langkah 3 sampai 5)
11. Verifikasi checkbox Delete baris `Manage files` kembali tercentang
12. Verifikasi banner Total Control `This user has Total Control access.` tetap tampil
13. Tekan F5
14. Verifikasi checkbox Delete baris `Manage files` tetap tercentang setelah muat ulang (tidak ada perubahan tersimpan)

### TC-GS-USER-376: Klik checkbox permission auto-save per cell

15. Klik menu User di sidebar Global Settings
16. Klik icon Search, ketik `Ahmad Fauzi {runId}-064`, tekan Enter
17. Klik Name `Ahmad Fauzi {runId}-064` di User List
18. Klik Tab `Role`
19. Centang Update baris `Manage TAG`
20. Verifikasi toast sukses `Success, permissions have been updated.`
21. Tekan F5
22. Verifikasi checkbox Update baris `Manage TAG` tetap tercentang setelah refresh

### TC-GS-USER-377: Centang checkbox pada role yang belum di-assign meng-assign role

23. Centang checkbox Read baris `Manage hardware` (belum di-assign)
24. Verifikasi toast sukses `Success, permissions have been updated.`
25. Verifikasi baris `Manage hardware` menjadi role ter-assign: checkbox Read tercentang dan disabled (baseline)
26. Verifikasi checkbox Create, Update, dan Delete baris `Manage hardware` tetap dapat diubah (enabled)
27. Buka Global Settings > Role & Permission
28. Klik icon Search, ketik `Manage hardware`, tekan Enter
29. Verifikasi `Ahmad Fauzi {runId}-064` muncul sebagai user pada role `Manage hardware`

### TC-GS-USER-381: Remove memicu auto-revert tier dan banner hilang (Read Only)

30. Klik menu User di sidebar Global Settings
31. Klik icon Search, ketik `Doni Pratama {runId}-064`, tekan Enter
32. Klik Name `Doni Pratama {runId}-064` di User List
33. Klik Tab `Role`
34. Centang Create baris `Manage TAG`
35. Klik `[Remove]` pada dialog Remove Access
36. Verifikasi toast sukses `Success, permissions have been updated. Doni Pratama {runId}-064 is no longer Read Only.`
37. Verifikasi baris `Manage TAG` tampil di tabel Tab Role
38. Verifikasi banner `This user has Read Only access.` hilang
39. Verifikasi User Type di Access & Status General Information bukan lagi `Read Only`

### TC-GS-USER-1020: Tab Role Total Control, Remove menampilkan toast auto-revert dengan tier Total Control

40. Klik menu User di sidebar Global Settings
41. Klik icon Search, ketik `Andi Wijaya {runId}-064`, tekan Enter
42. Klik Name `Andi Wijaya {runId}-064` di User List
43. Klik Tab `Role`
44. Uncheck Delete baris `Manage files`
45. Klik `[Remove]` pada dialog Remove Access
46. Verifikasi toast sukses `Success, permissions have been updated. Andi Wijaya {runId}-064 is no longer Total Control.`
47. Verifikasi baris `Manage files` tampil di tabel Tab Role
48. Verifikasi banner `This user has Total Control access.` hilang

### TC-GS-USER-383: Edit sukses oleh holder Update terhadap target Normal

49. Logout, lalu login sebagai Manage user and role (Update-Only: R+U)
50. Buka Global Settings > User > User List (sub-tab Login User)
51. Klik icon Search, ketik `Ahmad Fauzi 2 {runId}-064`, tekan Enter
52. Klik Name `Ahmad Fauzi 2 {runId}-064` di User List
53. Klik Tab `Role`
54. Centang Update baris `Manage TAG`
55. Verifikasi toast sukses `Success, permissions have been updated.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (55 langkah, di antaranya 15 langkah pembukaan Detail berulang berupa klik menu User, Search, dan klik Name) karena tujuh TC berada di satu kelas harness (fungsional, aksi tulis pada user milik spec), satu layar (Tab Role User Detail), dan tiap blok TC berdiri sendiri dengan user seed sendiri (kecuali Andi Wijaya yang dipakai berurutan oleh TC-GS-USER-379, 380, dan 1020).
- Urutan TC sumber diubah: TC-GS-USER-379 dan 380 (dialog diblokir lewat Cancel) mendahului TC-GS-USER-376 dan 377 (aksi sukses) sesuai bagian 3; TC-GS-USER-1020 sesudah TC-GS-USER-381 karena menghapus tier Total Control Andi Wijaya yang masih dibutuhkan TC-GS-USER-379 dan 380; TC-GS-USER-383 paling akhir agar ganti akun hanya dilakukan sekali. Remove (TC-GS-USER-381 dan 1020) hanya menyangkut user seed masing-masing sehingga tidak memengaruhi TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 2, 15 sampai 16, 30 sampai 31, 40 sampai 41, dan 50 sampai 51 (membuka User List dan mencari user target), 13 dan 21 (muat ulang untuk mengamati penyimpanan), 27 sampai 28 (membuka Role & Permission dan mencari role), 49 (ganti akun). Langkah 10 (`[Cancel]`) dan 5 (Uncheck Delete baris `Manage files`) dipakai bersama oleh TC-GS-USER-379 dan 380 (langkah 3 TC-GS-USER-380 dipenuhi langkah 5).
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC dan hanya sebagai anchor): langkah 37 dan 47 (baris tabel Tab Role tampil sebagai pembanding untuk "banner hilang"). Langkah 13 sampai 14 dan 21 sampai 22 adalah langkah observasi untuk "tidak ada perubahan tersimpan" (Expected c TC-GS-USER-380) dan "setelah refresh" (Expected b TC-GS-USER-376).
- Pembagian TC lintas spec: Tab Role untuk user non-tier tanpa aksi tulis (screening, banner, Read baseline, Column Visibility) diverifikasi di spec 063.
- Temuan untuk QA:
  - TC-GS-USER-381 Post Condition ("Notifikasi in-app view-only ke Doni Pratama" dan "Terdampak: Role & Permission tab Read Only") tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-376 Post Condition ("Terdampak: Role & Permission (role Ahmad Fauzi)") tanpa langkah observasi; diverifikasi sebagian lewat langkah 29 untuk role `Manage hardware` (TC-GS-USER-377).
  - TC-GS-USER-381 Expected c ("User Type berubah dari `Read Only`") tidak menyebut nilai User Type sesudahnya; spec mengasersi User Type bukan lagi `Read Only`.
  - TC-GS-USER-377 langkah 4 dan Expected c tidak menyebut surface yang menampilkan daftar user per role di Role & Permission; spec mencari role `Manage hardware` dan mengasersi user muncul pada role tersebut.
  - TC-GS-USER-380 Expected c ("Tidak ada perubahan tersimpan") tanpa cara mengamati; spec memuat ulang halaman (F5) dan mengasersi checkbox tetap tercentang.
  - TC-GS-USER-376, 377, 383: precondition tidak menyebut role `Manage TAG` dan `Manage hardware` belum di-assign untuk Ahmad Fauzi; spec men-seed holder `Manage user and role` tanpa role tersebut.
  - TC-GS-USER-379, 380, 381, 1020: mekanisme pembentukan tier Total Control dan Read Only pada user tidak disebut TC (Tabel Pre-setup hanya menyebut tier); disediakan tim FE/BE.
