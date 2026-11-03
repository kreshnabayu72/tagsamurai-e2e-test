---
id: TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2
title: "Resilience: kegagalan 5xx dan timeout pada Assign serta Edit (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-264
  - TC-FA-RP-274
  - TC-FA-RP-275
  - TC-FA-RP-441
  - TC-FA-RP-447
coverage:
  web: automated
---

# Resilience: kegagalan 5xx dan timeout pada Assign serta Edit (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Group Manager Fajar Nugroho (Pre-setup #5), `groupManager_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (dipakai TC-FA-RP-447 pada Fixed Asset > Settings > Groups).
- Akun aktor 2: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Dipakai sesudah ganti akun (langkah 6). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_GM_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi tanpa tingkat akses; Budi Santoso), #18, #5 (Fajar Nugroho sebagai Group Manager di `IT Infrastructure`). Detail Role `Manage accounting` memuat baris Ahmad Fauzi dengan Create dan Update tidak aktif. Disiapkan lewat seeding di hook `before`.
- Data Dinamis: Subgroup `Fail Room {runId}-285` (nama dari Data Uji Dinamis TC dengan suffix run dan nomor spec); tidak tersisa karena pembuatan gagal.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept. Untuk TC-FA-RP-447 pemaksaan kegagalan pembuatan Group disediakan tim FE (mekanismenya tidak disebut TC; tanpa endpoint karangan). Penahanan respons pada TC-FA-RP-274 dipakai agar state in-flight teramati sebelum respons 5xx dilepas (bagian 8b butir 5).
- State global: spec tidak mengubah state global; intercept dilepas segera dan data Pre-setup yang diubah dipulihkan di hook `after`.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-447: Pembuatan Group gagal membatalkan penugasan pembuat

1. Buka Fixed Asset > Settings > Groups
2. Blokir respons pembuatan Group dengan status 5xx (kemampuan disediakan tim FE)
3. Buat Subgroup `Fail Room {runId}-285` di bawah `IT Infrastructure` lewat row action `Add Subgroup`
4. Lepas pemblokiran respons pembuatan Group
5. Tunggu aksi selesai: pembuatan Group yang ditolak selesai sebelum berpindah akun
6. Ganti akun: logout, lalu login sebagai Total Control Siti Rahmawati dengan `Spectra.env.FA_TC_PASSWORD`
7. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, klik Role Name `Manage group` pada section Group Role
8. Klik `All Groups` di Sidebar Group Tree
9. Verifikasi node `IT Infrastructure` tampil di Sidebar Group Tree
10. Verifikasi Group `Fail Room {runId}-285` tidak terbentuk dan tidak tampil di Sidebar Group Tree
11. Verifikasi tabel Detail Role `Manage group` termuat dengan sedikitnya satu baris
12. Verifikasi tidak ada baris Fajar Nugroho dengan badge Group `Fail Room {runId}-285`

### TC-FA-RP-264: Assign User ke Group Role gagal 5xx, popup tetap terbuka

13. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role, pilih `Data Center`
14. Klik `[+ Assign]`
15. Centang Budi Santoso
16. Blokir respons submit dengan status 5xx
17. Klik `[Assign]`
18. Verifikasi muncul toast error: `Error, failed to assign Manage files.`
19. Verifikasi popup tetap terbuka
20. Verifikasi Budi Santoso tetap tercentang
21. Lepas pemblokiran respons
22. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-274: Edit CRUD gagal 5xx, cell kembali ke nilai tersimpan

23. Tunggu toast lama hilang otomatis
24. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
25. Tahan respons permintaan update permission dan siapkan status 5xx saat dilepas
26. Centang Create pada baris Ahmad Fauzi
27. Verifikasi cell Create sempat berubah (tercentang) selama proses
28. Verifikasi cell Create Disabled selama proses (in-flight)
29. Lepas tahanan respons dengan status 5xx
30. Verifikasi muncul toast error: `Error, failed to update permissions.`
31. Verifikasi cell Create kembali ke nilai tersimpan (tidak tercentang)
32. Lepas intercept permintaan update permission

### TC-FA-RP-275: Edit CRUD timeout jaringan, cell kembali dan toast koneksi

33. Tunggu toast lama hilang otomatis
34. Tunda respons update permission hingga timeout
35. Centang Update pada baris Ahmad Fauzi
36. Verifikasi muncul toast: `Connection problem. Please try again.`
37. Verifikasi cell Update kembali ke nilai tersimpan
38. Lepas penundaan respons

### TC-FA-RP-441: Assign User ke Global Role gagal 5xx, popup tetap terbuka

39. Tunggu toast lama hilang otomatis
40. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
41. Klik `[+ Assign]`
42. Centang Ahmad Fauzi
43. Blokir respons submit dengan status 5xx
44. Klik `[Assign]`
45. Verifikasi muncul toast error: `Error, failed to assign Manage Open API.` (pola `Error, failed to assign [Role Name].`)
46. Verifikasi popup tetap terbuka
47. Verifikasi seleksi Ahmad Fauzi dipertahankan
48. Lepas pemblokiran respons
49. Klik `[Cancel]` pada popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-264, 274, 275, 441, 447).
- Urutan TC: TC-FA-RP-447 dijalankan lebih dulu karena akun Group Manager login di hook `before` dan satu kali ganti akun menuju Total Control (S-07).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): membuka halaman Groups dan membuat Subgroup; ganti akun dan membuka Detail Role (langkah 6); "Tunggu aksi selesai" sebelum ganti akun (bagian 8b butir 8); "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); menutup popup dengan `[Cancel]` (langkah 22 dan 49); melepas intercept (S-09).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` node `IT Infrastructure` tampil dan tabel Detail Role termuat sebagai anchor positif untuk asersi absence Group dan baris Fajar Nugroho (bagian 8b butir 2).
- Langkah penahanan respons pada TC-FA-RP-274 (Tahan respons lalu 5xx saat dilepas) menggantikan "Blokir respons" supaya Expected a (cell sempat berubah dan Disabled selama proses) teramati sebelum Expected b dan c.
- Spec melewati sekitar 35 langkah (49 langkah). Semua blok satu kelas harness (resilience 5xx dan timeout) pada Assign dan Edit. Tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya mengulang hook dan navigasi.
- Temuan untuk QA:
  - TC-FA-RP-447 tidak menyebut mekanisme memaksa kegagalan pembuatan Group; spec menulisnya sebagai kemampuan yang disediakan tim FE tanpa endpoint karangan.
  - TC-FA-RP-447 tidak menyebut lokasi pembuatan Subgroup; spec memakai Fixed Asset > Settings > Groups dengan row action `Add Subgroup` seperti TC penugasan otomatis pembuat Group.
  - TC-FA-RP-275 dan TC-FA-RP-274 tidak menyebut nilai awal baris Ahmad Fauzi pada `Manage accounting`; spec memakai Create dan Update tidak aktif.
