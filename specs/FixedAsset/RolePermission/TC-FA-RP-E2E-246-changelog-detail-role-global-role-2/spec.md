---
id: TC-FA-RP-E2E-246-changelog-detail-role-global-role-2
title: "Changelog Detail Role Global Role (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-811
  - TC-FA-RP-812
  - TC-FA-RP-813
  - TC-FA-RP-814
  - TC-FA-RP-1130
coverage:
  web: automated
---

# Changelog Detail Role Global Role (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi), #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi), #24 (`Company Changelog`). Precondition TC-FA-RP-813: Ahmad Fauzi Total Control dengan `Manage Open API` aktif dan `Import data` nonaktif (dipakai sebagai precondition TC, disiapkan lewat seeding API). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Entri pembanding (8b.2): modal Changelog `Manage Open API` dan `Import data` yang diasersi absence memuat sedikitnya satu entri lama dari riwayat Pre-setup #24 atau entri yang dibuat seeding API milik spec di hook `before` (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: Membaca modal Changelog Detail Role lewat UI; waktu aksi dicatat sesudah aksi pemicu. Seeding tingkat akses Ahmad Fauzi (Total Control parsial untuk TC-FA-RP-813) lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Tingkat akses Ahmad Fauzi dan Global Role-nya diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-811: Changelog Detail Role Global Role: Assign (via Total Control) untuk role yang baru diaktifkan

1. Klik `[+ Assign]` di Tab `Total Control`
2. Centang Ahmad Fauzi lalu klik `[Assign]`, catat waktu sesudah `[Assign]`, lalu tunggu aksi selesai
3. Klik Tab `System` lalu buka Detail Role `Manage asset transactional policy`
4. Klik ikon Changelog di toolbar Detail Role
5. Verifikasi Modal memuat entri terbaru: Action `Assign (via Total Control)`; Role Name — User `Manage asset transactional policy — Ahmad Fauzi`; Field `Access`; Old Value `—`; New Value `Assigned`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
6. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, lalu buka Detail Role `Manage Open API` (role yang sudah aktif bagi Ahmad Fauzi sebelum Assign)
7. Klik ikon Changelog di toolbar Detail Role
8. Verifikasi Modal Changelog `Manage Open API` terbuka
9. Verifikasi Modal Changelog `Manage Open API` memuat sedikitnya satu entri lama (entri pembanding selain entri `Assign (via Total Control)` pada waktu aksi)
10. Verifikasi Modal tidak memuat entri `Assign (via Total Control)` untuk Ahmad Fauzi pada waktu aksi

### TC-FA-RP-1130: Changelog Detail Role Global Role: Remove (via Total Control) tidak menulis entri Edit untuk pengosongan C/U/D

11. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, lalu klik Tab `Total Control`
12. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
13. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
14. Klik Tab `System` lalu buka Detail Role `Manage accounting`
15. Klik ikon Changelog di toolbar Detail Role
16. Verifikasi Modal memuat satu entri Action `Remove (via Total Control)`; Role Name — User `Manage accounting — Ahmad Fauzi`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
17. Verifikasi Modal tidak memuat entri Action `Edit` dengan Field `Create`, `Update`, atau `Delete` untuk Ahmad Fauzi pada waktu aksi (pengosongan C/U/D bagian dari pelepasan)

### TC-FA-RP-812: Changelog Detail Role Global Role: Assign (via Read Only) untuk role yang baru diaktifkan

18. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, lalu klik Tab `Read Only`
19. Klik `[+ Assign]` di Tab `Read Only`
20. Centang Ahmad Fauzi lalu klik `[Assign]`, catat waktu sesudah `[Assign]`, lalu tunggu aksi selesai
21. Klik Tab `System` lalu buka Detail Role `Manage asset transactional policy`
22. Klik ikon Changelog di toolbar Detail Role
23. Verifikasi Modal memuat entri terbaru: Action `Assign (via Read Only)`; Role Name — User `Manage asset transactional policy — Ahmad Fauzi`; Field `Access`; Old Value `—`; New Value `Assigned`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)

### TC-FA-RP-814: Changelog Detail Role Global Role: Remove (via Read Only)

24. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, lalu klik Tab `Read Only`
25. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
26. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
27. Klik Tab `System` lalu buka Detail Role `Manage Open API`
28. Klik ikon Changelog di toolbar Detail Role
29. Verifikasi Modal memuat entri terbaru: Action `Remove (via Read Only)`; Role Name — User `Manage Open API — Ahmad Fauzi`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)

### TC-FA-RP-813: Changelog Detail Role Global Role: Remove (via Total Control) hanya untuk role yang berubah aktif ke nonaktif

30. Tetapkan Ahmad Fauzi Total Control dengan `Manage Open API` aktif dan `Import data` nonaktif lewat seeding API, hingga tersimpan
31. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, lalu klik Tab `Total Control`
32. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
33. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
34. Klik Tab `System` lalu buka Detail Role `Manage Open API`
35. Klik ikon Changelog di toolbar Detail Role
36. Verifikasi Modal memuat entri terbaru: Action `Remove (via Total Control)`; Role Name — User `Manage Open API — Ahmad Fauzi`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
37. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, lalu buka Detail Role `Import data` (nonaktif sebelumnya)
38. Klik ikon Changelog di toolbar Detail Role
39. Verifikasi Modal Changelog `Import data` terbuka
40. Verifikasi Modal Changelog `Import data` memuat sedikitnya satu entri lama (entri pembanding yang membuktikan modal tidak kosong)
41. Verifikasi Detail Role `Import data` tidak mendapat entri untuk Ahmad Fauzi pada waktu aksi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 41 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 3, 6, 11, 14, 18, 21, 24, 27, 31, 34, 37. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 30; tidak ada `Verifikasi`.
- Urutan TC: TC-FA-RP-811, 1130, 812, 814, 813 (bukan urutan nomor) supaya hasil tiap TC menjadi precondition TC berikutnya tanpa seeding ulang: TC-FA-RP-811 membuat Ahmad Fauzi Total Control (precondition TC-FA-RP-1130), TC-FA-RP-1130 melepasnya, TC-FA-RP-812 menjadikannya Read Only (precondition TC-FA-RP-814), TC-FA-RP-814 melepasnya; TC-FA-RP-813 membutuhkan Total Control parsial sehingga memakai seeding API.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Anchor tambahan (S-03, bukan dari TC sumber): langkah 9 dan 40 membuktikan sedikitnya satu entri pembanding tampil di modal Changelog yang sama sebelum asersi absence pada langkah 10 dan 41 (butir 8b.2).
- Spec ini memuat lebih dari 35 langkah (di atas smell): kelima blok satu kelas (membaca Changelog Detail Role Global Role setelah Assign atau Remove tingkat akses), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan berasal dari dua asersi absence (tiap satu anchor modal dan satu entri pembanding) dan navigasi antar Detail Role.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-811 Expected "role yang sudah aktif sebelum Assign tidak mendapat entri baru" tidak menyebut role mana; Ahmad Fauzi memegang `Manage Open API` menurut Pre-setup #39 (tidak dirujuk precondition TC), sehingga spec memakai `Manage Open API`.
  - TC-FA-RP-813 menyebut Detail Role `Import data` tidak mendapat entri; spec mengasersinya lewat modal Changelog Detail Role `Import data`.
  - TC-FA-RP-811 sampai 814 memakai Ahmad Fauzi; Pre-setup #15 menyatakan Ahmad Fauzi tanpa tingkat akses dan Pre-setup #39 menyatakan Ahmad Fauzi memegang `Manage Open API` dan `Manage accounting`; spec memakai keduanya dan menyiapkan keadaan lewat seeding API.
