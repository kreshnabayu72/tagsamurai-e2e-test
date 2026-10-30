---
id: TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing
title: "Sinkron Custom Field (Create, Deactivate, Activate, Delete, Ubah Data Type, Required) ke User Existing"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-950
  - TC-GS-USER-951
  - TC-GS-USER-952
  - TC-GS-USER-953
  - TC-GS-USER-954
  - TC-GS-USER-955
coverage:
  web: automated
---

# Sinkron Custom Field (Create, Deactivate, Activate, Delete, Ubah Data Type, Required) ke User Existing

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User). Tab Custom Field dan User List berada di modul User yang sama sehingga spec memakai satu akun tanpa ganti akun. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 24: Blood Type, Skills, Emergency Phone) dibaca saja dan tidak diubah; spec memakai Custom Field milik sendiri bersuffix (S-06). Data Pre-setup lain tidak dipakai.
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` oleh akun Total Control (kemampuan seeding Custom Field, Login User, dan nilai Custom Field user lewat API; nilai field wajib lain user mengikuti fixture `fixtures/user.json` yang belum ada, disediakan tim FE):
  - Custom Field `Skills {runId}-151`: Data Type Dropdown, Dropdown Values `Excel` dan `SQL`, Active, Required No (setara `Skills`; target TC-GS-USER-951, 952, 955).
  - Custom Field `Blood Type {runId}-151`: Data Type Dropdown, Dropdown Values `A`, `B`, `O`, `AB`, Active (setara `Blood Type`; target TC-GS-USER-954; juga pembanding di TC-GS-USER-951 dan 953).
  - Login User `Dewi Lestari {runId}-151`, email `dewilestari+{runId}-151@qwertysystem.net`, Activated, Active, Access `Fixed Asset`, nilai `Skills {runId}-151` = `Excel`, nilai `Blood Type {runId}-151` = `A`.
  - Login User `Rahmat Hidayat {runId}-151`, email `rahmathidayat+{runId}-151@qwertysystem.net`, Activated, Active, Access `Fixed Asset`, tanpa nilai `Skills {runId}-151` (untuk Expected TC-GS-USER-955), nilai `Blood Type {runId}-151` = `B` (untuk Expected TC-GS-USER-954 "semua user").
- Data Dinamis yang dibuat spec lewat UI: Custom Field `Shirt Size {runId}-151` (Data Type Dropdown, Dropdown Values `S` dan `M`, Active) pada TC-GS-USER-950, dihapus pada TC-GS-USER-953. Nilai `Shirt Size {runId}-151` = `M` untuk `Dewi Lestari {runId}-151` diisi lewat API pada langkah 14.
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah berhasil penuh): hapus lewat API Login User `dewilestari+{runId}-151@qwertysystem.net` dan `rahmathidayat+{runId}-151@qwertysystem.net`, lalu Custom Field `Skills {runId}-151`, `Blood Type {runId}-151`, dan `Shirt Size {runId}-151` bila masih ada.
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-USER-950: Create Custom Field aktif muncul di form dan Detail user lama

1. Buka Global Settings > User > Tab Custom Field
2. Klik `[+ Custom Field]`, isi Field Name `Shirt Size {runId}-151`, pilih Data Type `Dropdown`, isi Dropdown Values `S` dan `M`, klik `[Submit]`
3. Tunggu aksi selesai
4. Buka Tab User List, klik `[+ User]`
5. Verifikasi field `Shirt Size {runId}-151` tampil di Popup Create User
6. Klik `✕` di header form Create User
7. Klik icon Search, ketik `Dewi Lestari {runId}-151`, tekan Enter
8. Klik `⋯` pada baris `Dewi Lestari {runId}-151` > Edit
9. Verifikasi field `Shirt Size {runId}-151` tampil di Popup Edit
10. Klik `✕` di header form Edit User
11. Klik Name `Dewi Lestari {runId}-151`
12. Verifikasi Section Custom Fields Detail memuat field `Shirt Size {runId}-151`
13. Verifikasi nilai field `Shirt Size {runId}-151` pada Detail kosong `—`
14. Isi nilai `Shirt Size {runId}-151` = `M` untuk `Dewi Lestari {runId}-151` lewat API
15. Kembali ke User List dengan klik Back

### TC-GS-USER-951: Deactivate Custom Field menyembunyikan field dari form dan Detail tanpa menghapus nilai

16. Buka Tab Custom Field, klik icon Search, ketik `Skills {runId}-151`, tekan Enter
17. Matikan switch Active baris `Skills {runId}-151`, klik `[Deactivate]` pada dialog
18. Tunggu aksi selesai
19. Buka Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-151`, tekan Enter
20. Klik `⋯` pada baris `Dewi Lestari {runId}-151` > Edit
21. Verifikasi field `Blood Type {runId}-151` tampil di Popup Edit
22. Verifikasi field `Skills {runId}-151` tidak tampil di Popup Edit
23. Klik `✕` di header form Edit User
24. Klik Name `Dewi Lestari {runId}-151`
25. Verifikasi Section Custom Fields Detail memuat field `Blood Type {runId}-151`
26. Verifikasi field `Skills {runId}-151` tidak tampil di Detail
27. Verifikasi (dibaca lewat fixture BE) nilai `Skills {runId}-151` `Dewi Lestari {runId}-151` tetap `Excel`
28. Kembali ke User List dengan klik Back

### TC-GS-USER-952: Activate kembali Custom Field menampilkan nilai lama

29. Buka Tab Custom Field, klik icon Search, ketik `Skills {runId}-151`, tekan Enter
30. Nyalakan switch Active baris `Skills {runId}-151`, klik `[Activate]` pada dialog
31. Tunggu aksi selesai
32. Buka Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-151`, tekan Enter
33. Klik Name `Dewi Lestari {runId}-151`
34. Verifikasi Section Custom Fields Detail menampilkan `Skills {runId}-151` dengan nilai `Excel`
35. Kembali ke User List dengan klik Back

### TC-GS-USER-955: Custom Field diubah menjadi Required

36. Buka Tab Custom Field, klik icon Search, ketik `Skills {runId}-151`, tekan Enter
37. Klik `⋯` pada baris `Skills {runId}-151` > Edit, ubah switch Required Field menjadi Yes, klik `[Save]`
38. Tunggu aksi selesai
39. Buka Tab User List, klik icon Search, ketik `Rahmat Hidayat {runId}-151`, tekan Enter
40. Klik Name `Rahmat Hidayat {runId}-151`
41. Verifikasi Detail menampilkan alert `⚠ "Skills {runId}-151 is required."`
42. Kembali ke User List dengan klik Back

### TC-GS-USER-954: Ubah Data Type Custom Field mereset nilai semua user

43. Buka Tab Custom Field, klik icon Search, ketik `Blood Type {runId}-151`, tekan Enter
44. Klik `⋯` pada baris `Blood Type {runId}-151` > Edit, ubah Data Type menjadi `Text`, klik `[Save]`
45. Klik `[Change Data Type]` pada dialog `Change Data Type`
46. Tunggu aksi selesai
47. Buka Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-151`, tekan Enter
48. Klik `⋯` pada baris `Dewi Lestari {runId}-151` > Edit
49. Verifikasi field `Blood Type {runId}-151` pada Popup Edit kosong
50. Klik `✕` di header form Edit User
51. Klik Name `Dewi Lestari {runId}-151`
52. Verifikasi nilai `Blood Type {runId}-151` pada Detail `Dewi Lestari {runId}-151` kosong `—`
53. Kembali ke User List dengan klik Back
54. Ganti isi kotak search dengan `Rahmat Hidayat {runId}-151`, tekan Enter
55. Klik Name `Rahmat Hidayat {runId}-151`
56. Verifikasi nilai `Blood Type {runId}-151` pada Detail `Rahmat Hidayat {runId}-151` kosong `—`
57. Kembali ke User List dengan klik Back

### TC-GS-USER-953: Delete Custom Field menghapus field dan nilainya permanen

58. Buka Tab Custom Field, klik icon Search, ketik `Shirt Size {runId}-151`, tekan Enter
59. Klik `⋯` pada baris `Shirt Size {runId}-151` > Delete, klik `[Delete]` pada dialog
60. Tunggu aksi selesai
61. Buka Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-151`, tekan Enter
62. Klik `⋯` pada baris `Dewi Lestari {runId}-151` > Edit
63. Verifikasi field `Blood Type {runId}-151` tampil di Popup Edit
64. Verifikasi field `Shirt Size {runId}-151` tidak tampil di Popup Edit
65. Klik `✕` di header form Edit User
66. Klik Name `Dewi Lestari {runId}-151`
67. Verifikasi Section Custom Fields Detail memuat field `Blood Type {runId}-151`
68. Verifikasi field `Shirt Size {runId}-151` tidak tampil di Detail
69. Verifikasi nilai `M` milik `Shirt Size {runId}-151` tidak tampil di Detail

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Sinkron Custom Field ke user existing; tidak ada TC kelas harness.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-GS-USER-955 dan 954 sebelum TC-GS-USER-953, karena TC-GS-USER-953 menghapus data dan ditaruh paling akhir (bagian 3 prinsip 5); TC-GS-USER-952 langsung sesudah TC-GS-USER-951 karena Activate membutuhkan `Skills` dalam keadaan Inactive dari TC-GS-USER-951; TC-GS-USER-955 sesudah TC-GS-USER-952 karena membutuhkan `Skills` Active.
- Spec melewati sekitar 35 langkah (69 langkah). Alasan: enam TC memakai satu tema (siklus hidup Custom Field yang diamati di Detail dan Popup Edit user yang sama) dan state `Skills` dibangun berurutan antar blok (Inactive di TC-GS-USER-951 menjadi precondition TC-GS-USER-952; Active kembali menjadi precondition TC-GS-USER-955) dan `Shirt Size` dibuat di TC-GS-USER-950 untuk dihapus di TC-GS-USER-953, sehingga memecahnya mengulang seeding dan aksi di Tab Custom Field; tiap blok punya Verifikasi sendiri pada surface sendiri dan sebagian besar langkah adalah Search, navigasi tab, serta Verifikasi per klausa (S-01).
- Popup Edit pada Langkah Uji TC-GS-USER-952, 955 tidak dibuka karena Expected kedua TC hanya mengasersi Detail; Popup Create hanya dibuka pada TC-GS-USER-950 karena hanya Expected itu yang menyebutnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 4, 16, 19, 29, 32, 36, 39, 43, 47, 58, 61 (membuka tab dan Search); langkah 3, 18, 31, 38, 46, 60 (menunggu aksi selesai); langkah 6, 10, 23, 50, 65 (menutup Popup tanpa isian, tanpa dialog `Unsaved Changes`); langkah 14 (mengisi nilai `Shirt Size` lewat API agar Expected "nilainya hilang permanen" TC-GS-USER-953 dapat diamati); langkah 15, 28, 35, 42, 53, 57 (Back ke User List); langkah 45 (mengonfirmasi dialog `Change Data Type`, bagian aksi Save TC-GS-USER-954).
- Asersi absence (langkah 22, 26, 64, 68, 69) didahului `Verifikasi` field pembanding `Blood Type {runId}-151` pada surface yang sama (langkah 21, 25, 63, 67; bagian 8b butir 2).
- Nama field bersuffix ikut ke teks aplikasi: alert TC-GS-USER-955 `⚠ "Skills is required."` ditulis `⚠ "Skills {runId}-151 is required."`.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-952 dan 955 menyebut "Buka Detail Dewi Lestari dan Popup Edit Dewi" tetapi Expected hanya Detail; TC-GS-USER-951 menyatakan nilai `Skills` tidak dihapus tanpa menyebut cara mengamatinya selagi field disembunyikan; spec membacanya lewat fixture BE (langkah 27) dan menampilkannya kembali di TC-GS-USER-952.
  - TC-GS-USER-951, 952, 955 memakai `Dewi Lestari` untuk keadaan "punya nilai Skills" (TC-GS-USER-951 dan 952) dan "tanpa nilai Skills" (TC-GS-USER-955) padahal Tabel Pre-setup No. 12 tidak menyebut nilai Skills Dewi; spec memakai Dewi seed dengan nilai `Excel` dan Rahmat Hidayat seed tanpa nilai.
  - TC-GS-USER-953: Expected "nilainya hilang permanen" mengandaikan `Shirt Size` punya nilai, sedangkan TC-GS-USER-950 membuat field kosong; spec mengisi nilai `M` lewat API (langkah 14).
  - TC-GS-USER-954: TC tidak menyebut Data Type tujuan; spec memakai `Text`. TC tidak menyebut dialog `Change Data Type` tetapi PRD (`D-01`) mewajibkannya; spec mengonfirmasinya.
  - Pre-setup No. 24 menyebut `Skills` sebagai Multi-Dropdown sedangkan daftar Data Type PRD Custom Field User tidak memuat Multi-Dropdown; spec men-seed `Skills {runId}-151` sebagai Dropdown.
  - TC sumber tidak menyebut apakah Search dipertahankan saat berpindah tab; spec membuka Search ulang tiap kunjungan tab dan menganggap Search dipertahankan sesudah Back.
