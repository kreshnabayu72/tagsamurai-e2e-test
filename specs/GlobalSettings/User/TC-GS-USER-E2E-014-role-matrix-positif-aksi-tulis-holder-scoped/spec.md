---
id: TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped
title: "Role Matrix Positif: Aksi Tulis Holder Scoped (Create-Only, Update-Only, Delete-Only) untuk Create, Edit, Toggle Active, Resend, Bulk Activate, Delete, dan Bulk Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-67
  - TC-GS-USER-68
  - TC-GS-USER-69
  - TC-GS-USER-70
  - TC-GS-USER-71
  - TC-GS-USER-72
  - TC-GS-USER-73
coverage:
  web: automated
---

# Role Matrix Positif: Aksi Tulis Holder Scoped (Create-Only, Update-Only, Delete-Only) untuk Create, Edit, Toggle Active, Resend, Bulk Activate, Delete, dan Bulk Delete

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Tabel Data Uji Pre-setup) | Nama user | Env var password | Aksi yang dieksekusi |
|---|---|---|---|---|
| Manage user and role (Create-Only: C+R) | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` (No. 5) | Lestari Ayu | `Spectra.env.GS_CREATE_PASSWORD` | Create (TC-GS-USER-67) |
| Manage user and role (Update-Only: R+U) | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 6) | Bayu Saputra | `Spectra.env.GS_UPDATE_PASSWORD` | Edit, Toggle Active OFF, Resend Activation Email, Bulk Activate (TC-GS-USER-68, 69, 71, 73) |
| Manage user and role (Delete-Only: R+D) | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` (No. 7) | Citra Melati | `Spectra.env.GS_DELETE_PASSWORD` | Delete, Bulk Delete (TC-GS-USER-70, 72) |

- Login akun Create-Only (aktor pertama spec) dilakukan di hook `before`; Update-Only dan Delete-Only memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Delete-Only, hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Division `Finance` (No. 23), Position `Supervisor` (No. 22), Access `Fixed Asset` (subscription Client PT Maju Bersama, No. 26). Target aksi tulis dan hapus memakai data milik spec, bukan user Pre-setup No. 10-22 (S-06).
- Data Dinamis (suffix per run ditambah nomor spec `{runId}-014`; Division `Finance` dan field wajib lain diisi seeding):
  - `Wulan Sari {runId}-014` (First Name `Wulan`, Last Name `Sari {runId}-014`), Email `wulansari+{runId}-014@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`: dibuat lewat UI di TC-GS-USER-67.
  - `Dewi Lestari {runId}-014`: di-seed lewat API, Activated, Active ON, Position `Staff` (target TC-GS-USER-68).
  - `Ahmad Fauzi {runId}-014`: di-seed lewat API, Activated, Active ON (target TC-GS-USER-69, lalu Inactive untuk TC-GS-USER-73).
  - `Mike Tan {runId}-014`: di-seed lewat API, Pending Activation (target TC-GS-USER-71).
  - `Jane Smith {runId}-014`: di-seed lewat API, Inactive manual (target TC-GS-USER-73).
  - `Rudi Hakim {runId}-014`: di-seed lewat API, Normal tanpa aset dan approval (target TC-GS-USER-70).
  - `Tono Wijaya {runId}-014` dan `Rani Lestari {runId}-014`: di-seed lewat API, Normal tanpa aset dan approval (target TC-GS-USER-72).
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut nama endpoint): seeding dan penghapusan user lewat API dengan status Active, Inactive, dan Pending Activation; memajukan jam server dan jam browser bersama (cooldown Resend 60 detik pada TC-GS-USER-71; countdown UI berjalan di jam browser).
- State global yang diubah: jam server dan jam browser (dimajukan di langkah 33 dan dipulihkan di langkah 39; hook `after` memulihkan sebagai cadangan). Suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): hapus lewat API semua user dengan suffix `{runId}-014` yang masih ada (termasuk `Wulan Sari {runId}-014`), pulihkan jam, lalu pulihkan sesi ke akun default suite.

## Test Steps

### Pembukaan layar (akun Create-Only)

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-67: Create user sukses oleh aktor Create-Only

2. Klik `[+ User]`
3. Isi First Name `Wulan`, Last Name `Sari {runId}-014`, Division `Finance`, Email `wulansari+{runId}-014@qwertysystem.net`
4. Centang Access `Fixed Asset`
5. Klik `[Submit]`
6. Verifikasi popup tertutup
7. Verifikasi toast sukses `Success, user has been created.`
8. Klik icon Search, ketik `{runId}-014`, tekan Enter
9. Verifikasi baris `Wulan Sari {runId}-014` muncul di User List
10. Verifikasi switch Active baris `Wulan Sari {runId}-014` ON
11. Verifikasi badge `Pending Activation` pada baris `Wulan Sari {runId}-014`

### TC-GS-USER-68: Edit user sukses oleh aktor Update-Only

12. Logout, lalu login sebagai Manage user and role (Update-Only: R+U)
13. Buka Global Settings > User > User List (sub-tab Login User)
14. Klik icon Search, ketik `{runId}-014`, tekan Enter
15. Klik (⋯) baris `Dewi Lestari {runId}-014` → `Edit`
16. Ubah Position ke `Supervisor`
17. Klik `[Save]`
18. Verifikasi toast sukses `Success, user has been updated.`
19. Verifikasi sel Position baris `Dewi Lestari {runId}-014` bernilai `Supervisor`

### TC-GS-USER-69: Toggle Active OFF sukses oleh aktor Update-Only

20. Klik switch Active baris `Ahmad Fauzi {runId}-014` (ON)
21. Klik `[Deactivate]` pada dialog
22. Verifikasi toast sukses `Success, user has been deactivated.`
23. Verifikasi switch Active baris `Ahmad Fauzi {runId}-014` OFF

### TC-GS-USER-73: Bulk Activate sukses oleh aktor Update-Only

24. Centang baris `Jane Smith {runId}-014` dan `Ahmad Fauzi {runId}-014`
25. Klik `Bulk Action`
26. Verifikasi overlay Bulk Action memuat opsi `Activate`
27. Verifikasi overlay Bulk Action tanpa opsi `Delete`
28. Klik `Activate`
29. Klik `[Activate]` pada dialog
30. Verifikasi toast sukses `Success, user has been activated.`
31. Verifikasi switch Active baris `Jane Smith {runId}-014` ON
32. Verifikasi switch Active baris `Ahmad Fauzi {runId}-014` ON

### TC-GS-USER-71: Resend Activation Email sukses oleh aktor Update-Only

33. Majukan jam server dan jam browser bersama 120 detik sehingga cooldown resend `Mike Tan {runId}-014` sudah lewat
34. Klik (⋯) baris `Mike Tan {runId}-014` → `Resend Activation Email`
35. Verifikasi toast sukses `Success, activation email has been sent.`
36. Klik (⋯) baris `Mike Tan {runId}-014`
37. Verifikasi opsi `Resend Activation Email` untuk `Mike Tan {runId}-014` masuk cooldown
38. Tekan Esc untuk menutup overlay baris
39. Pulihkan jam server dan jam browser ke waktu semula

### TC-GS-USER-70: Delete user sukses oleh aktor Delete-Only

40. Logout, lalu login sebagai Manage user and role (Delete-Only: R+D)
41. Buka Global Settings > User > User List (sub-tab Login User)
42. Klik icon Search, ketik `{runId}-014`, tekan Enter
43. Klik (⋯) baris `Rudi Hakim {runId}-014` → `Delete`
44. Klik `[Delete]` pada dialog
45. Verifikasi toast sukses `Success, user has been deleted.`
46. Verifikasi baris `Tono Wijaya {runId}-014` masih tampil di User List
47. Verifikasi baris `Rudi Hakim {runId}-014` hilang dari User List

### TC-GS-USER-72: Bulk Delete sukses oleh aktor Delete-Only tanpa Update

48. Centang baris `Tono Wijaya {runId}-014` dan `Rani Lestari {runId}-014`
49. Klik `Bulk Action`
50. Verifikasi overlay Bulk Action memuat opsi `Delete`
51. Verifikasi overlay Bulk Action tanpa opsi `Activate`, `Deactivate`, dan `Resend`
52. Klik `Delete`
53. Klik `[Delete]` pada dialog
54. Verifikasi toast sukses `Success, user has been deleted.`
55. Verifikasi baris `Wulan Sari {runId}-014` masih tampil di User List
56. Verifikasi baris `Tono Wijaya {runId}-014` dan `Rani Lestari {runId}-014` hilang dari User List

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (56 langkah) karena tujuh TC aksi tulis berada di satu kelas harness (Role Matrix positif, bagian 3a) dan tiap blok TC berdiri sendiri dengan target seed sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah ganti akun hanya dua kali dan tidak ada blok yang bergantung pada hasil blok role lain.
- Urutan TC sumber diubah: TC dikelompokkan per akun (Create-Only, Update-Only, Delete-Only) supaya ganti akun hanya dua kali. TC-GS-USER-73 mengikuti TC-GS-USER-69 karena `Ahmad Fauzi {runId}-014` menjadi Inactive di TC-GS-USER-69 dan dipakai TC-GS-USER-73 (precondition TC-GS-USER-73 "Jane Smith dan Ahmad Fauzi Inactive"). TC-GS-USER-71 mendahului aksi hapus. TC-GS-USER-70 dan TC-GS-USER-72 paling akhir karena aksi menghapus data (bagian 3 prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 14, dan 42 (Search `{runId}-014` untuk menampilkan data milik spec di antara user Pre-setup; bukan bagian asersi TC), 12 dan 40 (ganti akun), 13 dan 41 (membuka User List sesudah ganti akun), 33 dan 39 (memajukan dan memulihkan jam; jam dipulihkan sebelum ganti akun berikutnya), 36 (membuka ulang overlay baris untuk mengamati cooldown), 38 (menutup overlay). Langkah 46, 55 (Verifikasi baris pembanding) adalah anchor absence (bagian 8b butir 2) untuk langkah 47 dan 56; asersi ini tidak ada di TC dan ditambahkan hanya sebagai anchor.
- Langkah 26 dan 27, 50 dan 51: overlay Bulk Action dicek dengan anchor positif (opsi yang diharapkan tampil) sebelum asersi opsi yang tidak tampil.
- Nama user memakai suffix `{runId}-014` karena Dewi Lestari, Ahmad Fauzi, Mike Tan, dan Jane Smith juga ada sebagai data Pre-setup bersama (No. 12, 13, 14, 17) dan tidak boleh diubah (S-06); TC sumber memakai nama Pre-setup tanpa suffix.
- Temuan untuk QA:
  - TC-GS-USER-67 Post Condition a (Access `Fixed Asset` tersimpan) dan b (Activation Email dikirim oleh modul Auth) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-USER-68, 69, 71, dan 73 memakai user Pre-setup (Dewi Lestari, Ahmad Fauzi, Mike Tan, Jane Smith) sebagai target aksi tulis; spec memakai user seed milik spec dengan nilai awal yang sama (Position `Staff`, Active, Pending Activation, Inactive).
  - TC-GS-USER-69 Post Condition "Ahmad Fauzi Inactive (Global)" dan TC-GS-USER-70 Post Condition "Rudi Hakim ter-soft-delete" tidak punya langkah observasi; tidak diasersi (state OFF dan baris hilang sudah teramati di Expected).
  - TC-GS-USER-71 precondition "cooldown resend sudah lewat" tanpa cara memenuhinya; spec memajukan jam server dan jam browser bersama (bagian 6). TC-GS-USER-71 Expected b ("masuk cooldown") tidak menyebut tampilannya; spec mengasersi opsi masuk cooldown tanpa asersi teks tooltip.
  - TC-GS-USER-70 dan TC-GS-USER-72 precondition "tersedia" untuk user dinamis (Rudi Hakim, Tono Wijaya, Rani Lestari) tanpa cara menyediakan; spec men-seed lewat API (nama endpoint ditentukan tim FE di tahap script).
