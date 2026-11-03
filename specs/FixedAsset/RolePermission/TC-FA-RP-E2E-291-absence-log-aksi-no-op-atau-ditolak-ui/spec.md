---
id: TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui
title: "Absence log: aksi no-op atau ditolak UI"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-283
  - TC-FA-RP-300
  - TC-FA-RP-357
  - TC-FA-RP-413
  - TC-FA-RP-461
  - TC-FA-RP-1041
coverage:
  web: automated
---

# Absence log: aksi no-op atau ditolak UI

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor 2: Manage global user & role (Update) Hendra Wijaya (Pre-setup #6), `murGlobal_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MUR_GLOBAL_PASSWORD`. Dipakai sesudah ganti akun (langkah 34) untuk TC-FA-RP-300 dan TC-FA-RP-1041. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Pelaku kedua (Sesi 2) lewat sesi API (hanya memicu perubahan state, bukan konteks UI kedua): Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD` (TC-FA-RP-283 dan TC-FA-RP-461); Total Control Siti Rahmawati (Pre-setup #2), `Spectra.env.FA_TC_PASSWORD` (TC-FA-RP-300 dan penghapusan identitas pada TC-FA-RP-413).
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`, `FA_MUR_GLOBAL_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Budi Setiawan), #17 (Hesti Rahma tanpa Home Group, TC-FA-RP-1041), #18, #19 (Putri Wulandari sebagai Staff pada `IT Infrastructure` sub-tab `Disposal`, TC-FA-RP-461), #20 (sub-tab `Transfer` pada `IT Infrastructure` dengan Require Approval On dan Approval Scope `Both`), #6 (Hendra Wijaya), dan #3 (Rina Wulandari). Budi Santoso memegang `Manage Open API` (TC-FA-RP-283); Budi Santoso dan Budi Setiawan memegang `Manage Open API` tanpa tingkat akses (TC-FA-RP-300). Disiapkan lewat seeding di hook `before` dan sebagai langkah penghubung.
- Kemampuan teknis: kemampuan baca jumlah entri (disediakan tim FE/BE, tanpa endpoint karangan, bagian 8b butir 10) untuk Changelog surface terkait, System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Hesti Rahma (disediakan tim FE/BE, tanpa endpoint karangan); baseline dicatat per TC sebelum aksi pemicu dan asersi memakai perbandingan dengan baseline, bukan angka absolut (S-12).
- State global: spec mengubah penugasan pool #15 dan tingkat akses yang diberikan Sesi 2 serta menghapus identitas Ahmad Fauzi (TC-FA-RP-413), menghapus penugasan Putri Wulandari oleh Sesi 2 (TC-FA-RP-461), dan menugaskan Hesti Rahma sebagai Group Manager (TC-FA-RP-1041); dipulihkan di hook `after` (pemulihan dijamin fixture backend yang disediakan tim FE/BE, termasuk identitas yang dihapus).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-283: Remove atas baris yang sudah hilang tetap selesai tanpa efek dan tanpa entri log

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Verifikasi baris Budi Santoso tampil di Detail Role `Manage Open API` pada Sesi 1
3. Sesi 2 (sesi API Total Control kedua Rina Wulandari) meng-Remove baris Budi Santoso pada Detail Role `Manage Open API` hingga penghapusan tersimpan
4. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
5. Catat baseline jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri sesudah Sesi 2 selesai
6. Di Sesi 1, klik `[⋯]` baris Budi Santoso lalu `Remove`, klik `[Remove]`
7. Verifikasi tindakan Sesi 1 selesai: dialog Remove tertutup
8. Verifikasi jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-357: Approval Scope nilai yang sama, toast netral tanpa log

9. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Transfer`
10. Catat baseline jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
11. Pilih opsi `Both` yang sudah terpilih
12. Verifikasi muncul toast netral (Info): `No changes to save.`
13. Verifikasi jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-413: Submit Assign, satu user stale menolak seluruh submit, tidak ada entri log

14. Tunggu toast lama hilang otomatis
15. Pulihkan state lewat seed API: pool #15 (Ahmad Fauzi dan Budi Santoso) tanpa tingkat akses
16. Klik Tab `Total Control`
17. Klik `[+ Assign]` di Tab Total Control
18. Centang Ahmad Fauzi dan Budi Santoso
19. Sesi 2 (sesi API) menghapus identitas Ahmad Fauzi di Global Settings > User hingga terhapus
20. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
21. Catat baseline jumlah entri Changelog Tab Total Control, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
22. Klik `[Assign]`
23. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
24. Verifikasi jumlah entri Changelog Tab Total Control, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
25. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-461: Remove Role Transaksi atas baris yang sudah hilang tetap selesai tanpa efek dan tanpa entri log tambahan

26. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
27. Verifikasi baris Putri Wulandari (Staff) tampil pada Sesi 1
28. Sesi 2 (sesi API Total Control kedua Rina Wulandari) meng-Remove baris Putri Wulandari (Staff) pada `IT Infrastructure` sub-tab `Disposal` hingga penghapusan tersimpan
29. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
30. Catat baseline jumlah entri Changelog Tab Transaction Role, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri sesudah Sesi 2 selesai
31. Di Sesi 1, klik `[⋯]` baris Putri Wulandari lalu `Remove`, klik `[Remove]`
32. Verifikasi tindakan Sesi 1 selesai: dialog Remove tertutup
33. Verifikasi jumlah entri Changelog Tab Transaction Role, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-300: Bulk Remove tanpa satu baris pun berhasil, dialog blok tanpa toast dan tanpa entri log

34. Ganti akun: logout, lalu login sebagai Manage global user & role (Update) Hendra Wijaya dengan `Spectra.env.FA_MUR_GLOBAL_PASSWORD`
35. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `System`
36. Pulihkan state lewat seed API: Budi Santoso dan Budi Setiawan memegang `Manage Open API` tanpa tingkat akses, lalu muat ulang halaman
37. Klik Role Name `Manage Open API` pada section Global Role
38. Centang baris Budi Santoso dan Budi Setiawan
39. Klik `Bulk Action` > `Remove` hingga dialog Bulk Remove terbuka
40. Sesi 2 (sesi API Total Control Siti Rahmawati) meng-Assign Total Control ke Budi Santoso dan Budi Setiawan hingga penugasan tersimpan
41. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
42. Catat baseline jumlah entri Changelog Detail Role `Manage Open API`, System Log Hendra Wijaya, dan Activity Log lewat kemampuan baca jumlah entri
43. Di Sesi 1, klik `[Remove]`
44. Verifikasi tampil dialog blok severity warning: Title `Cannot Remove`; Body `None of the selected users could be removed.`; satu tombol `[OK]`
45. Verifikasi jumlah entri Changelog Detail Role `Manage Open API`, System Log Hendra Wijaya, dan Activity Log sama dengan baseline (tidak ada entri log baru)
46. Klik `[OK]`
47. Perhatikan tabel Detail Role, Bulk Action Bar, dan seleksi

### TC-FA-RP-1041: Cancel D-10 yang memuat penugasan Group Manager, tidak ada entri log dan tidak ada notifikasi

48. Siapkan Hesti Rahma tanpa Home Group ditugaskan Group Manager di `Data Center` lewat sesi API hingga tersimpan
49. Klik Tab `Group Manager` pada Settings > Role & Permission
50. Verifikasi baris Hesti Rahma di `Data Center` tampil di Tab `Group Manager`
51. Catat baseline jumlah entri Changelog Tab Group Manager, System Log Hendra Wijaya, dan Activity Log, serta jumlah notifikasi in-app Hesti Rahma lewat kemampuan baca
52. Buka Settings > User > Detail Hesti Rahma
53. Klik field Home Group, pilih `Logistics Warehouse`, klik `[Select]`
54. Klik `[Cancel]` pada dialog D-10
55. Buka Tab `Group Manager` pada Settings > Role & Permission
56. Verifikasi baris Hesti Rahma di `Data Center` tetap ada di Tab `Group Manager`
57. Verifikasi jumlah entri Changelog Tab Group Manager, System Log Hendra Wijaya, dan Activity Log sama dengan baseline (tidak ada entri log baru)
58. Verifikasi jumlah notifikasi in-app Hesti Rahma sama dengan baseline (tidak ada notifikasi baru)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-283, 300, 357, 413, 461, 1041).
- Kelas g (absence log): tiap TC punya aksi pemicu nyata, baseline sendiri (S-12), dan anchor positif sebelum asersi absence (bagian 8b butir 2). Pemicu berkelas lain (state tenant, permintaan langsung, dua sesi) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5` butir a).
- Pembagian TC lintas spec: klausa "tanpa entri log tambahan" TC-FA-RP-283 (presence di spec 083), klausa "tidak ada entri log" TC-FA-RP-300 (presence di spec 302), TC-FA-RP-357 (presence di spec 106), TC-FA-RP-413 (presence di spec 122), TC-FA-RP-461 (presence di spec 305), dan TC-FA-RP-1041 (presence di spec 121) diasersi di spec ini dengan aksi nyata dan baseline sendiri. Id keenam TC tetap di `sourceTc` spec asal dan spec ini (S-05).
- Baseline TC-FA-RP-283, TC-FA-RP-413, dan TC-FA-RP-461 dicatat sesudah Sesi 2 selesai (langkah 5, 21, dan 30) supaya entri yang ditulis Sesi 2 tidak terhitung sebagai entri baru Sesi 1.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): membuka tab, Detail Role, node, dan sub-tab; "Tunggu aksi selesai" tiap kali sesi aktif berpindah sesudah aksi tanpa asersi (bagian 8b butir 8); "Tunggu toast lama hilang otomatis" (R-12); pemulihan state seed; menutup popup dan dialog (langkah 25); mengamati tabel Detail Role, Bulk Action Bar, dan seleksi sesudah `[OK]` (langkah 47); ganti akun (langkah 34); membuka Tab, node, sub-tab, dan Detail User untuk TC-FA-RP-461 dan TC-FA-RP-1041; menyiapkan state Hesti Rahma lewat sesi API (langkah 48).
- Urutan TC: TC-FA-RP-283, 357, 413, 461 dijalankan sebagai Total Control, lalu satu kali ganti akun ke pemegang Manage global user & role untuk TC-FA-RP-300 dan TC-FA-RP-1041 (S-07). Anchor positif TC-FA-RP-461 adalah langkah 27 dan 32; anchor TC-FA-RP-1041 adalah langkah 50 dan 56.
- Spec melewati sekitar 35 langkah (58 langkah). Semua blok satu kelas harness (absence log) dengan enam TC yang masing-masing memerlukan aksi, baseline, dan anchor sendiri; satu kali ganti akun. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Expected "entri log" pada TC-FA-RP-283, 300, 357, 413, 461, dan 1041 tidak menyebut surface; spec membandingkan jumlah entri Changelog surface yang disentuh aksi, System Log aktor, dan Activity Log terhadap baseline.
  - TC-FA-RP-283 dan TC-FA-RP-413 menulis "Dua sesi" tanpa akun Sesi 2; spec memakai sesi API Total Control kedua Rina Wulandari (TC-FA-RP-283) dan Total Control Siti Rahmawati (TC-FA-RP-413); TC-FA-RP-413 tidak menyebut akun yang berwenang menghapus identitas di Global Settings > User.
  - TC-FA-RP-300 menyebut "System Log aktor" tanpa menyebut aktor bila Sesi 2 menulis entri; spec memakai System Log aktor Sesi 1 (Hendra Wijaya).
  - TC-FA-RP-461 menulis "Dua sesi" tanpa akun Sesi 2; spec memakai sesi API Total Control kedua Rina Wulandari. Klausa toast netral TC-FA-RP-461 butir b diasersi di spec 305, bukan di sini.
  - TC-FA-RP-1041 menyebut "tidak ada notifikasi" tanpa cara mengamati dan tanpa akun pengamat; spec memakai kemampuan baca jumlah notifikasi in-app Hesti Rahma sebagai baseline dan hasil, tanpa login sebagai Hesti Rahma.
