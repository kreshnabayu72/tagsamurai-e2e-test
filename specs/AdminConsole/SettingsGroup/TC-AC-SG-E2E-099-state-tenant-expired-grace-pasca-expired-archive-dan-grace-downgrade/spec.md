---
id: TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade
title: "State Tenant: Write-Lockdown Expired, Grace Pasca-Expired, dan Archive, serta Grace Downgrade yang Tidak Memblokir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-374
  - TC-AC-SG-375
  - TC-AC-SG-376
  - TC-AC-SG-377
  - TC-AC-SG-378
  - TC-AC-SG-379
coverage:
  web: automated
---

# State Tenant: Write-Lockdown Expired, Grace Pasca-Expired, dan Archive, serta Grace Downgrade yang Tidak Memblokir

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Distributor Expired, `totalControlExpired_automated_{namaCompany}@qwertysystem.net` (Pre-setup #28), password `Spectra.env.AC_SG_EXPIRED_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun yang diganti (ganti akun di langkah 28, 38, dan 48):

  | Aktor | Email | Env password | Dipakai di |
  |---|---|---|---|
  | Total Control Distributor Grace Expired (Pre-setup #29) | `totalControlGraceExpired_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_GRACEEXPIRED_PASSWORD` | langkah 28 sampai 37 |
  | Total Control Distributor Archive (Pre-setup #31) | `totalControlArchive_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_ARCHIVE_PASSWORD` | langkah 38 sampai 47 |
  | Total Control Distributor Grace Downgrade (Pre-setup #30) | `totalControlGraceDowngrade_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_GRACEDOWNGRADE_PASSWORD` | langkah 48 sampai 53 |

- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite untuk akun UI yang dipakai suite dan dipulihkan hook `after` suite (suite.md).
- Data Pre-setup: pohon uji kecil `Default Group`, `Cabang Uji 1`, `Cabang Uji 2` pada entitas Expired (Pre-setup #28), serta pohon uji kecil pada entitas Grace Expired, Archive, dan Grace Downgrade (Pre-setup #29, #31, #30). Semua aksi tulis pada entitas Expired, Grace pasca-Expired, dan Archive ditolak server sehingga node Pre-setup hanya dibaca dan tidak diubah (Last Updated, Modified By, dan struktur tree tidak berubah); data tidak dapat dimiliki spec karena entitas itu menolak penulisan.
- State global: status entitas Expired, Grace pasca-Expired, Archive, dan Grace karena downgrade (entitas Active) disediakan Fixture BE; spec tidak mengubahnya. Satu-satunya data tulis yang berhasil adalah group `Region Downgrade {runId}-099` pada entitas Grace Downgrade (TC-AC-SG-379), dihapus hook `after` lewat Fixture BE. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: Fixture BE (status entitas dan pemulihan; disediakan tim FE/BE); kemampuan mengamati status respons permintaan yang dipicu UI (untuk `403`) disediakan tim FE.
- Teks toast baku yang diasersi: "Changes can't be saved while this workspace is suspended or expired."

## Test Steps

### TC-AC-SG-374: Create group saat entitas Expired: tombol enabled, server menolak 403 dengan toast baku

1. Verifikasi tombol `[+] Group` tetap enabled (tidak Disabled)
2. Klik `[+] Group` di Sidebar Group Tree
3. Ketik `Region Gagal {runId}-099` lalu klik `[Submit]`
4. Verifikasi server menolak permintaan Create dengan status `403`
5. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
6. Verifikasi group `Region Gagal {runId}-099` tidak dibuat (tidak ada di Sidebar Group Tree dan tabel)
7. Tutup popup New Group dengan `✕`
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`

### TC-AC-SG-375: Edit group saat entitas Expired ditolak server dengan toast baku

10. Tunggu toast lama hilang otomatis
11. Klik ikon `⋯` pada baris `Cabang Uji 1` lalu `Edit`
12. Ubah nama menjadi `Cabang Uji 1 Ubah {runId}-099` lalu klik `[Save]`
13. Verifikasi server menolak permintaan Edit dengan status `403`
14. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
15. Verifikasi baris `Cabang Uji 1` masih ada di tabel
16. Verifikasi `Cabang Uji 1 Ubah {runId}-099` tidak ada di tabel
17. Tutup popup Edit Group dengan `✕`
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`

### TC-AC-SG-376: Delete group saat entitas Expired ditolak server dengan toast baku

20. Tunggu toast lama hilang otomatis
21. Klik ikon `⋯` pada baris `Cabang Uji 2`
22. Verifikasi item `Delete` pada Overlay Row Action enabled
23. Klik `Delete`
24. Verifikasi server menolak permintaan Delete dengan status `403`
25. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired." langsung tampil
26. Verifikasi dialog guard D-04 tidak tampil
27. Verifikasi group `Cabang Uji 2` tetap ada

### TC-AC-SG-377: Create saat entitas dalam Grace setelah Expired ditolak dengan toast baku

28. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Grace Expired`
29. Buka halaman Settings > Group lewat sidebar
30. Klik `[+] Group` di Sidebar Group Tree
31. Ketik `Region Grace {runId}-099` lalu klik `[Submit]`
32. Verifikasi server menolak permintaan Create dengan status `403`
33. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
34. Verifikasi group `Region Grace {runId}-099` tidak dibuat (tidak ada di Sidebar Group Tree dan tabel)
35. Tutup popup New Group dengan `✕`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`

### TC-AC-SG-378: Create saat entitas pada fase Archive ditolak dengan toast baku

38. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Archive`
39. Buka halaman Settings > Group lewat sidebar
40. Klik `[+] Group` di Sidebar Group Tree
41. Ketik `Region Arsip {runId}-099` lalu klik `[Submit]`
42. Verifikasi server menolak permintaan Create dengan status `403`
43. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
44. Verifikasi group `Region Arsip {runId}-099` tidak dibuat (tidak ada di Sidebar Group Tree dan tabel)
45. Tutup popup New Group dengan `✕`
46. Verifikasi dialog `Unsaved Changes` tampil
47. Klik `[Leave]`

### TC-AC-SG-379: Grace karena downgrade (entitas Active) tidak memblokir write

48. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Grace Downgrade`
49. Buka halaman Settings > Group lewat sidebar
50. Klik `[+] Group` di Sidebar Group Tree
51. Ketik `Region Downgrade {runId}-099` lalu klik `[Submit]`
52. Verifikasi toast sukses: "Success, group has been created."
53. Verifikasi group `Region Downgrade {runId}-099` tampil di Sidebar Group Tree dan tabel

## Notes

- Kelas h (state tenant). Urutan akun mengikuti status entitas; TC-AC-SG-379 (satu-satunya write yang berhasil) ditaruh paling akhir (S-10).
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 10, 20 (menunggu toast lama hilang agar toast berulang diasersi sebagai toast baru, R-12) dan langkah 29, 39, 49 (membuka Settings > Group sesudah ganti akun).
- Langkah 28, 38, dan 48 adalah ganti akun eksplisit (S-07); sesi dipulihkan ke akun default spec di hook `after`.
- Absence `Verifikasi` 6, 16, 26, 27, 34, dan 44 didahului `Verifikasi` toast error pada surface yang sama sebagai anchor positif (respons server sudah diproses, bagian 8b butir 2).
- Klausa "Grace akibat downgrade tidak memblokir karena entitas berstatus Active" pada TC-AC-SG-379 Expected adalah kesimpulan dari create berhasil dan tidak teramati terpisah; ditutup oleh `Verifikasi` langkah 52 dan 53 (S-03).
- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (kelas h, state tenant) dan berdiri sendiri; setiap blok memeriksa satu aksi tulis pada satu status entitas, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Penutupan popup dirty (S-08) dan jeda toast (R-12) menambah panjang spec.
- Temuan untuk QA:
  - TC-AC-SG-374, 375, 377, dan 378 tidak menyatakan keadaan popup setelah server menolak 403; spec mengasumsikan popup tetap terbuka dengan input dipertahankan seperti kegagalan server pada TC-AC-SG-105 dan 127, lalu menutupnya dengan alur `Unsaved Changes` (S-08). QA perlu mengonfirmasi.
  - TC-AC-SG-377, 378, dan 379 menyebut pohon uji kecil pada Pre-setup #29, #30, dan #31 tanpa daftar node; spec tidak menarget node tertentu pada entitas itu.
  - TC-AC-SG-379 tidak menyebut cara memulihkan group `Region Downgrade` sesudah TC; dihapus hook `after` lewat Fixture BE.
