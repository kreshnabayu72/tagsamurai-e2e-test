---
id: TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama
title: "Multi-konteks: konflik dua admin pada objek yang sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-995
  - TC-FA-RP-996
  - TC-FA-RP-997
  - TC-FA-RP-998
  - TC-FA-RP-999
coverage:
  web: automated
---

# Multi-konteks: konflik dua admin pada objek yang sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor Sesi 1: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor Sesi 2: Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD`. Dibuka sebagai konteks UI kedua pada langkah 1 (objek asersi: toast dan alert yang diterima Sesi 2) dan ditutup pada langkah 41; pada TC-FA-RP-999 Sesi 2 memakai sesi API akun yang sama sebagai pemicu. Dua akun berbeda dipakai karena satu akun hanya punya satu sesi web.
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso), #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi; TC-FA-RP-995), #18 (group `Data Center`), #19 (Require Approval Off di semua node `IT Infrastructure`; Approver Pandu Wijaya pada `Disposal`), dan #3 (Rina Wulandari, Total Control). Detail Role `Manage accounting` memuat baris Ahmad Fauzi dengan Read dan Update aktif (Create dan Delete tidak aktif) dan baris Budi Santoso; disiapkan lewat seeding di hook `before` dan langkah 17, 24, 33.
- Kemampuan teknis: konteks browser kedua (Sesi 2) untuk UI, sesi API aktor untuk pemicu dan pembacaan state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan). Nilai akhir baris, toggle, dan aturan dibaca lewat kemampuan baca state.
- State global: spec tidak mengubah state global; data Pre-setup yang diubah dipulihkan di hook `after` (Ahmad Fauzi, Budi Santoso, nilai Require Approval `Disposal` pada `IT Infrastructure`).
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-995: Dua admin mengedit baris yang sama, last-write-wins tanpa dialog konflik

1. Buka Sesi 2: jendela browser kedua, login sebagai Total Control kedua Rina Wulandari dengan `Spectra.env.FA_TC2_PASSWORD`
2. Sesi 2: buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
3. Sesi 1: klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
4. Sesi 1: centang Create pada baris Ahmad Fauzi
5. Tunggu aksi selesai: Sesi 1 selesai sebelum berpindah ke Sesi 2
6. Sesi 2 (belum disegarkan): hapus centang Update pada baris Ahmad Fauzi
7. Sesi 2: centang Delete pada baris Ahmad Fauzi
8. Verifikasi tidak ada dialog konflik versi pada Sesi 1 dan Sesi 2
9. Verifikasi lewat kemampuan baca nilai akhir baris Ahmad Fauzi pada `Manage accounting` mengikuti Sesi 2: Update tidak aktif dan Delete aktif

### TC-FA-RP-996: Dua admin mengubah toggle node yang sama, last-write-wins

10. Sesi 1: klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
11. Sesi 2: klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
12. Sesi 1: aktifkan toggle `Require Approval for Disposal`
13. Tunggu aksi selesai: Sesi 1 selesai sebelum berpindah ke Sesi 2
14. Sesi 2 (belum disegarkan): pilih radio `All approvers (AND)`
15. Verifikasi tidak ada dialog konflik versi pada Sesi 1 dan Sesi 2
16. Verifikasi lewat kemampuan baca nilai akhir toggle `Require Approval for Disposal` pada `IT Infrastructure` ON dengan aturan `All approvers (AND)`

### TC-FA-RP-997: Remove baris oleh satu admin dan Edit CRUD oleh admin lain, yang kedua mendapat toast netral

17. Pulihkan state lewat seed API: Budi Santoso memegang `Manage accounting`, lalu muat ulang halaman pada Sesi 1 dan Sesi 2
18. Sesi 1: klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
19. Sesi 2: klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
20. Sesi 1: klik `[⋯]` baris Budi Santoso lalu `Remove`, klik `[Remove]`
21. Tunggu aksi selesai: Sesi 1 selesai sebelum berpindah ke Sesi 2
22. Sesi 2: centang Create pada baris Budi Santoso
23. Verifikasi Sesi 2 menerima toast netral `This permission is no longer available.`

### TC-FA-RP-998: Dua admin meng-Assign user yang sama ke role yang sama, yang kedua ditolak

24. Pulihkan state lewat seed API: Ahmad Fauzi tanpa penugasan `Manage Open API`, lalu muat ulang halaman pada Sesi 1 dan Sesi 2
25. Sesi 1: klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role, klik `[+ Assign]`, centang Ahmad Fauzi
26. Sesi 2: klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role, klik `[+ Assign]`, centang Ahmad Fauzi
27. Sesi 1: klik `[Assign]`
28. Tunggu aksi selesai: Sesi 1 selesai sebelum berpindah ke Sesi 2
29. Sesi 2: klik `[Assign]`
30. Verifikasi Sesi 2 menampilkan alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
31. Verifikasi lewat kemampuan baca hanya satu baris Ahmad Fauzi pada Detail Role `Manage Open API`
32. Sesi 2: klik `[Cancel]`

### TC-FA-RP-999: Assign Group Manager dan Assign Total Control pada user yang sama bersamaan, salah satu menang tanpa kombinasi terlarang

33. Pulihkan state lewat seed API: Ahmad Fauzi tanpa tingkat akses dan tanpa penugasan Group Manager, lalu muat ulang halaman pada Sesi 1
34. Sesi 1: klik Tab `Group Manager`, klik `[+ Assign]`, pilih group `Data Center`, centang Ahmad Fauzi
35. Sesi 2 (sesi API Total Control Rina Wulandari) meng-Assign Total Control ke Ahmad Fauzi hingga penugasan tersimpan
36. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
37. Sesi 1: klik `[Assign]`
38. Verifikasi Sesi 1 ditolak dengan alert `Ahmad Fauzi is no longer eligible. Please select another.`
39. Verifikasi lewat kemampuan baca Ahmad Fauzi hanya berstatus Total Control tanpa penugasan Group Manager
40. Sesi 1: klik `[Cancel]`
41. Tutup Sesi 2: logout dan tutup jendela browser kedua

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-995, 996, 997, 998, 999).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): membuka Sesi 2 dan menutupnya (langkah 1 dan 41); membuka tab, Detail Role, node, sub-tab, dan popup Assign pada tiap sesi; "Tunggu aksi selesai" tiap kali sesi aktif berpindah sesudah aksi tanpa asersi (bagian 8b butir 8); pemulihan state seed (langkah 17, 24, 33); menutup popup dengan `[Cancel]`.
- Kelas c (multi-konteks): dua admin pada objek yang sama; Sesi 2 UI menjadi objek asersi (TC-FA-RP-997 dan TC-FA-RP-998). Pada TC-FA-RP-999 Sesi 2 hanya pemicu lewat sesi API.
- Spec melewati sekitar 35 langkah (41 langkah). Semua blok satu kelas harness (multi-konteks, dua admin) dengan Sesi 2 yang dibuka satu kali dan dipakai ulang oleh lima TC pada objek berbeda. Tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya mengulang hook dan navigasi.
- Temuan untuk QA:
  - TC-FA-RP-995 sampai TC-FA-RP-999 menulis "Dua sesi Total Control" tanpa akun sesi kedua; spec memakai Total Control kedua Pre-setup #3 (Rina Wulandari) karena satu akun tidak dapat memegang dua sesi web.
  - TC-FA-RP-995 tidak menyebut nilai awal baris Ahmad Fauzi pada `Manage accounting` maupun nilai akhir Create; spec memakai nilai awal Read dan Update aktif dan hanya mengasersi nilai akhir Update dan Delete (Create tidak diasersi karena TC tidak menyatakannya).
  - TC-FA-RP-996 meminta Sesi 2 yang belum disegarkan memilih radio `All approvers (AND)` padahal toggle masih Off di tampilan Sesi 2 (radio tampil hanya saat toggle On menurut TC-FA-RP-1098 dan sejenisnya); spec mengikuti TC dan langkah itu bergantung pada radio yang dapat dipilih di Sesi 2 yang belum disegarkan.
  - TC-FA-RP-997 menyebut baris Budi Santoso pada `Manage accounting` tanpa Precondition; spec menyiapkannya lewat seeding. TC-FA-RP-998 dan TC-FA-RP-999 menyebut "hanya satu baris" dan "hanya berstatus Total Control" tanpa surface pengamat; spec memakai kemampuan baca state.
