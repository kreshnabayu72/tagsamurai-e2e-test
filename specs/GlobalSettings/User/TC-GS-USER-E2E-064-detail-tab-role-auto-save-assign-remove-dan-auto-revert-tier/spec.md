---
id: TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier
title: "User Detail Tab Role: Auto-save per Cell, Assign Role, Dialog Remove Total Control dan Remove Read Only (Cancel dan Remove), dan Auto-revert Tier Total Control dan Read Only, serta Edit oleh Holder Update-Only"
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

# User Detail Tab Role: Auto-save per Cell, Assign Role, Dialog Remove Total Control dan Remove Read Only (Cancel dan Remove), dan Auto-revert Tier Total Control dan Read Only, serta Edit oleh Holder Update-Only

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor (ganti akun eksplisit di Test Steps):
  - Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`): aktor pertama, login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite.
  - Manage user and role (Update-Only: R+U) (Bayu Saputra) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 6; kredensial `Spectra.env.GS_UPDATE_PASSWORD`): dipakai TC-GS-USER-383.
  - Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_UPDATE_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (dibaca, tidak diubah): tidak ada user Pre-setup yang menjadi target tulis (S-06); role katalog `Manage files`, `Manage hardware`, dan `Manage TAG` serta role `Manage user and role` dibaca dan tidak diubah definisinya.
- Data Dinamis, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`:
  - `Andi Wijaya {runId}-064`, email `andiwijaya+{runId}-064@qwertysystem.net`: tier Total Control, checkbox `Delete` baris `Manage files` tercentang (TC-GS-USER-379, 380, dan 1020).
  - `Doni Pratama {runId}-064`, email `donipratama+{runId}-064@qwertysystem.net`: tier Read Only (TC-GS-USER-381).
  - `Ahmad Fauzi {runId}-064`, email `ahmadfauzi+{runId}-064@qwertysystem.net`: holder `Manage user and role` (non-tier); `Manage TAG` sudah ter-assign (switch Active ON, Update belum tercentang) sehingga checkbox-nya enabled (TC-GS-USER-376); `Manage hardware` belum pernah di-assign (TC-GS-USER-377).
  - `Ahmad Fauzi 2 {runId}-064`, email `ahmadfauzi2+{runId}-064@qwertysystem.net`: holder `Manage user and role` (non-tier), target Normal; `Manage TAG` sudah ter-assign (switch Active ON, Update belum tercentang) (TC-GS-USER-383).
- Kemampuan teknis (disediakan tim FE/BE): seeding user dengan assignment role dan tier (Total Control, Read Only, holder non-tier) lewat API (nama endpoint ditentukan tim FE di tahap script; TC, PRD, dan Tabel Pre-setup tidak menyebut mekanismenya); membaca halaman Global Settings > Role & Permission untuk daftar user pada role `Manage hardware` (TC-GS-USER-377).
- State global yang diubah: tidak ada. Yang berubah hanya assignment role dan tier pada empat user seed milik spec. Hook `after` (tetap berjalan walau spec gagal di tengah) menghapus empat user seed (sehingga keanggotaan role `Manage hardware` dan `Manage TAG` pulih) dan mengembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-USER-379: Edit menyimpang pattern tier memunculkan dialog Remove Total Control

1. Klik icon Search, ketik `Andi Wijaya {runId}-064`, tekan Enter
2. Klik Name `Andi Wijaya {runId}-064` di User List
3. Klik Tab `Role`
4. Uncheck Delete baris `Manage files`
5. Verifikasi dialog Title `Remove Total Control`
6. Verifikasi body dialog `• Andi Wijaya {runId}-064`
7. Verifikasi body dialog `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited. Are you sure you want to remove it?`
8. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`

### TC-GS-USER-380: Cancel dialog Remove Total Control mengembalikan checkbox

9. Klik `[Cancel]` (langkah 1 sampai 3 TC-GS-USER-380 dipenuhi langkah 2 sampai 4)
10. Verifikasi checkbox Delete baris `Manage files` kembali tercentang
11. Verifikasi banner Total Control `This user has Total Control access.` tetap tampil
12. Tekan F5
13. Verifikasi checkbox Delete baris `Manage files` tetap tercentang setelah muat ulang (tidak ada perubahan tersimpan)

### TC-GS-USER-376: Klik checkbox permission auto-save per cell

14. Klik menu User di sidebar Global Settings
15. Klik icon Search, ketik `Ahmad Fauzi {runId}-064`, tekan Enter
16. Klik Name `Ahmad Fauzi {runId}-064` di User List
17. Klik Tab `Role`
18. Centang Update baris `Manage TAG`
19. Verifikasi toast sukses `Success, permissions have been updated.`
20. Tekan F5
21. Verifikasi checkbox Update baris `Manage TAG` tetap tercentang setelah refresh

### TC-GS-USER-377: Switch Active ON pada role yang belum pernah di-assign meng-assign role

22. Nyalakan switch Active baris `Manage hardware` (belum pernah di-assign)
23. Verifikasi toast sukses `Success, role has been updated.`
24. Verifikasi tidak ada popup atau dialog
25. Verifikasi baris `Manage hardware` menjadi role ter-assign: switch Active ON
26. Verifikasi checkbox Read baris `Manage hardware` tercentang dan disabled (baseline)
27. Verifikasi checkbox Create, Update, dan Delete baris `Manage hardware` tidak tercentang
28. Verifikasi checkbox Create, Update, dan Delete baris `Manage hardware` dapat diubah (enabled)
29. Buka Global Settings > Role & Permission
30. Klik icon Search, ketik `Manage hardware`, tekan Enter
31. Verifikasi `Ahmad Fauzi {runId}-064` muncul sebagai user pada role `Manage hardware`

### TC-GS-USER-381: Remove memicu auto-revert tier dan banner hilang (Read Only)

32. Klik menu User di sidebar Global Settings
33. Klik icon Search, ketik `Doni Pratama {runId}-064`, tekan Enter
34. Klik Name `Doni Pratama {runId}-064` di User List
35. Klik Tab `Role`
36. Centang Create baris `Manage TAG`
37. Klik `[Remove]` pada dialog Remove Read Only
38. Verifikasi toast sukses `Success, permissions have been updated. Doni Pratama {runId}-064 is no longer Read Only.`
39. Verifikasi baris `Manage TAG` tampil di tabel Tab Role
40. Verifikasi banner `This user has Read Only access.` hilang
41. Verifikasi User Type di Access & Status General Information bukan lagi `Read Only`

### TC-GS-USER-1020: Tab Role Total Control, Remove menampilkan toast auto-revert dengan tier Total Control

42. Klik menu User di sidebar Global Settings
43. Klik icon Search, ketik `Andi Wijaya {runId}-064`, tekan Enter
44. Klik Name `Andi Wijaya {runId}-064` di User List
45. Klik Tab `Role`
46. Uncheck Delete baris `Manage files`
47. Klik `[Remove]` pada dialog Remove Total Control
48. Verifikasi toast sukses `Success, permissions have been updated. Andi Wijaya {runId}-064 is no longer Total Control.`
49. Verifikasi baris `Manage files` tampil di tabel Tab Role
50. Verifikasi banner `This user has Total Control access.` hilang

### TC-GS-USER-383: Edit sukses oleh holder Update terhadap target Normal

51. Logout, lalu login sebagai Manage user and role (Update-Only: R+U)
52. Buka Global Settings > User > User List (sub-tab Login User)
53. Klik icon Search, ketik `Ahmad Fauzi 2 {runId}-064`, tekan Enter
54. Klik Name `Ahmad Fauzi 2 {runId}-064` di User List
55. Klik Tab `Role`
56. Centang Update baris `Manage TAG`
57. Verifikasi toast sukses `Success, permissions have been updated.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (57 langkah, di antaranya 15 langkah pembukaan Detail berulang berupa klik menu User, Search, dan klik Name) karena tujuh TC berada di satu kelas harness (fungsional, aksi tulis pada user milik spec), satu layar (Tab Role User Detail), dan tiap blok TC berdiri sendiri dengan user seed sendiri (kecuali Andi Wijaya yang dipakai berurutan oleh TC-GS-USER-379, 380, dan 1020).
- Urutan TC sumber diubah: TC-GS-USER-379 dan 380 (dialog diblokir lewat Cancel) mendahului TC-GS-USER-376 dan 377 (aksi sukses) sesuai bagian 3; TC-GS-USER-1020 sesudah TC-GS-USER-381 karena menghapus tier Total Control Andi Wijaya yang masih dibutuhkan TC-GS-USER-379 dan 380; TC-GS-USER-383 paling akhir agar ganti akun hanya dilakukan sekali. Remove (TC-GS-USER-381 dan 1020) hanya menyangkut user seed masing-masing sehingga tidak memengaruhi TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 14 sampai 15, 32 sampai 33, 42 sampai 43, dan 52 sampai 53 (membuka User List dan mencari user target), 12 dan 20 (muat ulang untuk mengamati penyimpanan), 29 sampai 30 (membuka Role & Permission dan mencari role), 51 (ganti akun). Langkah 9 (`[Cancel]`) dan 4 (Uncheck Delete baris `Manage files`) dipakai bersama oleh TC-GS-USER-379 dan 380 (langkah 3 TC-GS-USER-380 dipenuhi langkah 4).
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC dan hanya sebagai anchor): langkah 39 dan 49 (baris tabel Tab Role tampil sebagai pembanding untuk "banner hilang"). Langkah 12 sampai 13 dan 20 sampai 21 adalah langkah observasi untuk "tidak ada perubahan tersimpan" (Expected c TC-GS-USER-380) dan "setelah refresh" (Expected b TC-GS-USER-376).
- Pembagian TC lintas spec: Tab Role untuk user non-tier tanpa aksi tulis (screening, banner, Read baseline, Column Visibility) diverifikasi di spec 063.
- Temuan untuk QA:
  - TC-GS-USER-381 Post Condition ("Notifikasi in-app view-only ke Doni Pratama" dan "Terdampak: Role & Permission tab Read Only") tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-376 Post Condition ("Terdampak: Role & Permission (role Ahmad Fauzi)") tanpa langkah observasi; diverifikasi sebagian lewat langkah 31 untuk role `Manage hardware` (TC-GS-USER-377).
  - TC-GS-USER-381 Expected c ("User Type berubah dari `Read Only`") tidak menyebut nilai User Type sesudahnya; spec mengasersi User Type bukan lagi `Read Only`.
  - TC-GS-USER-377 langkah 4 dan Expected c tidak menyebut surface yang menampilkan daftar user per role di Role & Permission; spec mencari role `Manage hardware` dan mengasersi user muncul pada role tersebut.
  - TC-GS-USER-380 Expected c ("Tidak ada perubahan tersimpan") tanpa cara mengamati; spec memuat ulang halaman (F5) dan mengasersi checkbox tetap tercentang.
  - TC-GS-USER-376 dan 383: precondition tidak menyebut role `Manage TAG` sudah ter-assign (checkbox role yang belum di-assign disabled menurut TC-GS-USER-1051); TC-GS-USER-377: precondition tidak menyebut `Manage hardware` belum pernah di-assign. Spec men-seed holder `Manage user and role` dengan `Manage TAG` ter-assign dan tanpa `Manage hardware`.
  - TC-GS-USER-379, 380, 381, 1020: mekanisme pembentukan tier Total Control dan Read Only pada user tidak disebut TC (Tabel Pre-setup hanya menyebut tier); disediakan tim FE/BE.
