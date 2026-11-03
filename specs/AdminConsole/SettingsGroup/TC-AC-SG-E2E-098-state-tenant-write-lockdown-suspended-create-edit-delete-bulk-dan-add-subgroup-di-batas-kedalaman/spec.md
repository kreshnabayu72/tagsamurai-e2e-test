---
id: TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman
title: "State Tenant: Write-Lockdown Suspended pada Create, Edit, Delete, Bulk Delete, dan Add Subgroup di Batas Kedalaman"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-370
  - TC-AC-SG-371
  - TC-AC-SG-372
  - TC-AC-SG-373
  - TC-AC-SG-403
  - TC-AC-SG-404
coverage:
  web: automated
---

# State Tenant: Write-Lockdown Suspended pada Create, Edit, Delete, Bulk Delete, dan Add Subgroup di Batas Kedalaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Distributor Suspended, `totalControlSuspended_automated_{namaCompany}@qwertysystem.net` (Pre-setup #27), password `Spectra.env.AC_SG_SUSPENDED_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun di langkah 37): Total Control entitas Distributor Suspended Dalam, `totalControlSuspendedDalam_automated_{namaCompany}@qwertysystem.net` (Pre-setup #46), password `Spectra.env.AC_SG_SUSPENDEDDALAM_PASSWORD`.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite untuk akun UI yang dipakai suite dan dipulihkan hook `after` suite (suite.md).
- Data Pre-setup: pohon uji kecil `Default Group`, `Cabang Uji 1`, `Cabang Uji 2` (Pre-setup #27) dan rantai `Level 1` sampai `Level 5` (Pre-setup #46). Semua aksi tulis pada spec ini ditolak server sehingga node Pre-setup hanya dibaca dan tidak diubah (Last Updated, Modified By, dan struktur tree tidak berubah); data tidak dapat dimiliki spec karena entitas Suspended menolak seluruh penulisan.
- State global: status entitas `Distributor Suspended` dan `Distributor Suspended Dalam` adalah Suspended (disediakan Fixture BE; tidak diubah spec). Hierarchy Depth Limit entitas `Distributor Suspended Dalam` bernilai 5 pada awal spec; TC-AC-SG-404 menurunkannya ke 4 di langkah 47 (kemampuan mengubah System Limits entitas ini disediakan tim FE tanpa akun karangan) dan langkah 56 serta hook `after` memulihkannya ke 5. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: Fixture BE (status entitas, System Limits, pemulihan baseline; disediakan tim FE/BE); kemampuan mengamati status respons permintaan yang dipicu UI (untuk `403`) disediakan tim FE.
- Teks toast baku yang diasersi: "Changes can't be saved while this workspace is suspended or expired."

## Test Steps

### TC-AC-SG-370: Create group saat entitas Suspended: tombol enabled, server menolak 403 dengan toast baku

1. Verifikasi tombol `[+] Group` tetap enabled (tidak Disabled)
2. Klik `[+] Group` di Sidebar Group Tree
3. Ketik `Region Gagal {runId}-098` lalu klik `[Submit]`
4. Verifikasi server menolak permintaan Create dengan status `403`
5. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
6. Verifikasi group `Region Gagal {runId}-098` tidak dibuat (tidak ada di Sidebar Group Tree dan tabel)
7. Tutup popup New Group dengan `✕`
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`

### TC-AC-SG-371: Edit group saat entitas Suspended ditolak server dengan toast baku

10. Tunggu toast lama hilang otomatis
11. Klik ikon `⋯` pada baris `Cabang Uji 1` lalu `Edit`
12. Ubah nama menjadi `Cabang Uji 1 Ubah {runId}-098` lalu klik `[Save]`
13. Verifikasi server menolak permintaan Edit dengan status `403`
14. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
15. Verifikasi baris `Cabang Uji 1` masih ada di tabel
16. Verifikasi `Cabang Uji 1 Ubah {runId}-098` tidak ada di tabel
17. Tutup popup Edit Group dengan `✕`
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`

### TC-AC-SG-372: Delete group saat entitas Suspended ditolak server dengan toast baku

20. Tunggu toast lama hilang otomatis
21. Klik ikon `⋯` pada baris `Cabang Uji 2`
22. Verifikasi item `Delete` pada Overlay Row Action enabled
23. Klik `Delete`
24. Verifikasi server menolak permintaan Delete dengan status `403`
25. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired." langsung tampil
26. Verifikasi dialog guard D-04 tidak tampil
27. Verifikasi group `Cabang Uji 2` tetap ada

### TC-AC-SG-373: Bulk Delete saat entitas Suspended ditolak server dengan toast baku

28. Tunggu toast lama hilang otomatis
29. Verifikasi kolom Checkbox tetap enabled
30. Centang kolom Checkbox pada baris `Cabang Uji 1` dan `Cabang Uji 2`
31. Pilih `Bulk Action` > `Delete` pada Bulk Actions Bar
32. Verifikasi server menolak permintaan Bulk Delete dengan status `403`
33. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
34. Verifikasi dialog guard D-06 sampai D-09 tidak tampil
35. Verifikasi `Cabang Uji 1` dan `Cabang Uji 2` tetap ada (tidak ada group terhapus)
36. Klik `Unselect All` pada Bulk Actions Bar

### TC-AC-SG-403: Add Subgroup pada parent di batas kedalaman saat entitas Suspended: D-01 tampil lebih dulu dari pemeriksaan status entitas

37. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Suspended Dalam`
38. Buka halaman Settings > Group lewat sidebar
39. Klik ikon `⋯` pada node `Level 5` di sidebar lalu `+ Add Subgroup`
40. Verifikasi dialog blok D-01 tampil: Title "Cannot Add Group", body "You've reached the platform limit of 5 levels. Contact support if you need a higher limit.", tombol `[OK]`
41. Verifikasi tidak ada toast 403 "Changes can't be saved while this workspace is suspended or expired."
42. Klik `[OK]` pada dialog
43. Verifikasi Popup Create tidak dibuka
44. Verifikasi tidak ada group baru

### TC-AC-SG-404: Submit Add Subgroup saat entitas Suspended ditolak server dengan toast baku tanpa dialog D-01

45. Klik ikon `⋯` pada node `Level 4` di sidebar lalu `+ Add Subgroup`
46. Ketik `Level 5 Baru {runId}-098` pada popup Add Subgroup
47. Turunkan Hierarchy Depth Limit entitas `Distributor Suspended Dalam` di System Limits dari 5 ke 4 sebelum klik `[Submit]`
48. Klik `[Submit]`
49. Verifikasi server menolak permintaan Create dengan status `403`
50. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
51. Verifikasi dialog blok D-01 tidak tampil
52. Verifikasi group `Level 5 Baru {runId}-098` tidak dibuat
53. Tutup popup Add Subgroup dengan `✕`
54. Verifikasi dialog `Unsaved Changes` tampil
55. Klik `[Leave]`
56. Pulihkan Hierarchy Depth Limit entitas `Distributor Suspended Dalam` ke 5

## Notes

- Kelas h (state tenant). TC-AC-SG-403 dan TC-AC-SG-404 memakai entitas Suspended yang dalam batas kedalaman dan menjadi objek uji urutan pemeriksaan (D-01 sebelum status entitas, dan status entitas sebelum re-cek kedalaman server).
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 10, 20, dan 28 (menunggu toast lama hilang agar toast berulang diasersi sebagai toast baru, R-12), langkah 36 (`Unselect All` memulihkan seleksi, S-09), langkah 38 (membuka Settings > Group sesudah ganti akun), dan langkah 56 (pemulihan Hierarchy Depth Limit, S-09).
- Langkah 37 adalah ganti akun eksplisit (S-07); sesi dipulihkan ke akun default spec di hook `after`.
- Absence `Verifikasi` 6, 16, 26, 27, 34, 35, 41, 44, 51, dan 52 didahului `Verifikasi` toast error atau dialog blok pada surface yang sama sebagai anchor positif (respons server sudah diproses, bagian 8b butir 2).
- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (kelas h, write-lockdown entitas Suspended) dan berdiri sendiri; setiap blok memeriksa satu aksi tulis (Create, Edit, Delete, Bulk Delete, Add Subgroup) dengan hasil yang sama pada permukaan berbeda, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah tambahan dari penutupan popup dirty (S-08, langkah 7 sampai 9, 17 sampai 19, dan 53 sampai 55) dan jeda toast (R-12) menambah panjang spec.
- TC-AC-SG-404 berstatus Automation `Manual Only` di TC sumber (menurunkan System Limits saat berjalan); perubahan System Limits dibatasi pada entitas `Distributor Suspended Dalam` dan dipulihkan.
- Temuan untuk QA:
  - TC-AC-SG-370, 371, dan 404 tidak menyatakan keadaan popup Create/Edit setelah server menolak 403 (tetap terbuka atau tertutup); spec mengasumsikan popup tetap terbuka dengan input dipertahankan seperti kegagalan server pada TC-AC-SG-105 dan 127, lalu menutupnya dengan alur `Unsaved Changes` (S-08). QA perlu mengonfirmasi.
  - TC-AC-SG-370 sampai 373 menarget node Pre-setup `Cabang Uji 1` dan `Cabang Uji 2` yang hanya menjadi sasaran aksi yang ditolak server; dinyatakan tidak diubah (S-06).
  - TC-AC-SG-404 Langkah Uji 4 tidak menyebut akun atau mekanisme penurun System Limits; ditulis sebagai kemampuan disediakan tim FE (S-13). Pre-setup #34 hanya menyebut konfigurasi System Limits secara umum.
  - TC-AC-SG-373 menulis "pilih `Bulk Action` > `Delete`" sedangkan TC-AC-SG-171 menulis "Klik `[Delete]`" pada Bulk Actions Bar; spec ini mengikuti catatan TC (header TC, Bulk Actions Bar PRD §4.2).
