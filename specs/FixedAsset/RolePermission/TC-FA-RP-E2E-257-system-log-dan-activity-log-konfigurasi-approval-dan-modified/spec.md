---
id: TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified
title: "System Log dan Activity Log: konfigurasi approval dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-855
  - TC-FA-RP-856
  - TC-FA-RP-857
  - TC-FA-RP-1055
  - TC-FA-RP-1056
  - TC-FA-RP-1057
  - TC-FA-RP-1058
coverage:
  web: automated
---

# System Log dan Activity Log: konfigurasi approval dan Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #3 (Total Control kedua Rina Wulandari), #12 (target Read Only Maya Anggraeni), #13 (target Group Manager Kevin Susanto), #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso), #18 (pohon group), #19 (seed Role Transaksi), #20 (seed approval Transfer), #21 (seed pemegang Update `Manage asset & TAG`), #39 (Detail Role terisi), #42 (Changelog Tab Total Control), #43 (seed Group Manager). #24 (`Company Changelog`). Awal spec: Approval Scope `Transfer` pada `IT Infrastructure` bernilai `Destination only` (precondition TC-FA-RP-1057, disiapkan lewat seeding API di hook `before`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca System Log (Settings > User > Detail Siti Rahmawati > Tab System Log) dan Activity Log FAMS lewat UI. Baseline jumlah entri kombinasi (Action, Object, Name, Field) pada System Log dan Activity Log dicatat di langkah Test Steps lewat kemampuan baca (disediakan tim FE/BE) sebelum tiap aksi pemicu; entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas (S-12). Waktu aksi dicatat sesudah aksi pemicu TC-FA-RP-1055 sampai 1057 untuk asersi Date Changelog (jam server dan jam browser sinkron; toleransi satu menit).
- State yang diubah dan pemulihannya: Require Approval `Disposal`, Approval Scope `Transfer`, serta tingkat akses Ahmad Fauzi dan Rina Wulandari diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-855: System Log baris konfigurasi approval memakai Name = jenis transaksi bukan user

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Transaction Role`, Name `Disposal` pada System Log aktor Siti Rahmawati (baseline System Log)
2. Klik Tab `Transaction Role`
3. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
4. Aktifkan toggle `Require Approval for Disposal`
5. Tunggu aksi selesai: toggle tetap pada kondisi baru dan indikator memuat hilang
6. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
7. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri Action `Edit`, Object `Transaction Role`, Name `Disposal` bertambah tepat satu) berisi Name `Disposal` (tidak ada user target) dengan Object `Transaction Role`

### TC-FA-RP-856: Activity Log: Modified By aktor pengklik untuk Assign, Remove, dan Edit

8. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Activity Log FAMS Action `Assign` dan jumlah entri Action `Remove`, masing-masing dengan Object `Total Control` dan Name `Ahmad Fauzi` (baseline Activity Log)
9. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Total Control`
10. Klik `[+ Assign]` di Tab `Total Control`
11. Centang Ahmad Fauzi lalu klik `[Assign]`
12. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
13. Klik `[Remove]`, lalu tunggu aksi selesai
14. Buka Activity Log FAMS (menu Activity Log)
15. Verifikasi satu entri baru Activity Log di atas baseline untuk Action `Assign`, Object `Total Control`, Name `Ahmad Fauzi` memuat Modified By `Siti R`
16. Verifikasi satu entri baru Activity Log di atas baseline untuk Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` memuat Modified By `Siti R`

### TC-FA-RP-857: Activity Log: Modified By Auto-Revert adalah admin pengedit, bukan System

17. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Activity Log FAMS Action `Auto-Revert`, Object `Total Control`, Name `Rina Wulandari` (baseline Activity Log)
18. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage accounting`
19. Hapus centang Delete pada baris Rina Wulandari
20. Klik `[Remove]` pada dialog, lalu tunggu aksi selesai
21. Buka Activity Log FAMS (menu Activity Log)
22. Verifikasi satu entri baru Activity Log di atas baseline untuk Action `Auto-Revert`, Object `Total Control`, Name `Rina Wulandari` memuat Modified By `Siti R`
23. Verifikasi entri baru Activity Log Action `Auto-Revert`, Object `Total Control`, Name `Rina Wulandari` tersebut tidak memuat Modified By `System`

### TC-FA-RP-1057: Changelog Approval Config: Approval Scope Destination only ke Origin only

24. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
25. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
26. Pilih `Origin only`, catat waktu sesudahnya
27. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
28. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
29. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Scope — IT Infrastructure`; Old Value `Destination only`; New Value `Origin only`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
30. Tutup modal Changelog

### TC-FA-RP-1056: Changelog Approval Config: Approval Scope Origin only ke Destination only

31. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
32. Pilih `Destination only`, catat waktu sesudahnya
33. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
34. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
35. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Scope — IT Infrastructure`; Old Value `Origin only`; New Value `Destination only`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
36. Tutup modal Changelog

### TC-FA-RP-1055: Changelog Approval Config: Approval Scope Destination only ke Both

37. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
38. Pilih `Both`, catat waktu sesudahnya
39. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
40. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
41. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Scope — IT Infrastructure`; Old Value `Destination only`; New Value `Both`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
42. Tutup modal Changelog

### TC-FA-RP-1058: System Log dan Activity Log: Edit Transaction Role: Approval Scope

43. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Transaction Role`, Name `Transfer`, Field `Approval Scope — IT Infrastructure`, Old Value `Both`, New Value `Destination only` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
44. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
45. Pilih `Destination only`
46. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
47. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
48. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Transaction Role`, Name `Transfer`, Field `Approval Scope — IT Infrastructure`, Old Value `Both`, New Value `Destination only`
49. Buka Activity Log FAMS (menu Activity Log)
50. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Transaction Role`, Name `Transfer`, Field `Approval Scope — IT Infrastructure`, Old Value `Both`, New Value `Destination only`, Modified By `Siti R`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 50 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 2, 5, 8, 9, 17, 18, 24, 27, 30, 33, 36, 39, 42, 43, 46. Akun aktor pertama sudah login di hook `before` (S-07).
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Name, dan Field serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan urutan Date tidak diasersi dan total entri tidak diasersi (S-12). Langkah pencatatan baseline adalah langkah penghubung (S-03, aksi tanpa `Verifikasi`). Langkah membuka System Log dan Activity Log adalah langkah TC; langkah "buka Fixed Asset > Settings > Role & Permission" antar blok adalah langkah penghubung.
- Urutan TC: TC-FA-RP-855, 856, 857, 1057, 1056, 1055, 1058 (bukan urutan nomor): Approval Scope `Transfer` berpindah berantai (Destination only, Origin only, Destination only, Both, Destination only) sehingga hasil tiap TC menjadi precondition TC berikutnya; nilai awal tiap TC 1057, 1056, dan 1055 yang di-seed ulang menurut TC (Destination only, Origin only, Destination only; menggantikan nilai awal `Both` pada Pre-setup #20) sama dengan hasil TC sebelumnya, sehingga urutan berantai memenuhinya; nilai awal Destination only disiapkan lewat seeding API di hook `before`.
- Spec ini memuat lebih dari 35 langkah (di atas smell): ketujuh blok satu kelas (pencatatan System Log, Activity Log, dan Changelog atas aksi konfigurasi dan tingkat akses oleh Siti Rahmawati), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan berasal dari empat langkah pencatatan baseline jumlah entri (S-12).
- Asersi absence `System` pada TC-FA-RP-857 didahului Verifikasi entri `Auto-Revert` yang sama (anchor positif, butir 8b.2).
- TC-FA-RP-1055 sampai 1057 mengasersi Date entri Changelog (waktu aksi, toleransi satu menit, S-12); TC-FA-RP-1058 dan TC-FA-RP-855 sampai 857 tidak mengasersi Date.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-855 langkah 1 menyebut mengaktifkan toggle `Disposal` tanpa menyebut Approver; Pre-setup #19 memuat Approver Pandu Wijaya untuk `Disposal` di `IT Infrastructure`.
  - TC-FA-RP-857 Expected tidak menyebut cara menentukan entri `Auto-Revert` terbaru selain Action dan Object; spec memakai Action, Object, dan Name Rina Wulandari dari langkah aksi dengan selisih terhadap baseline.
