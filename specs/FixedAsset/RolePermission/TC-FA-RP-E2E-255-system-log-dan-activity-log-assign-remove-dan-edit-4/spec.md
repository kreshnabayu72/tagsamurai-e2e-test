---
id: TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4
title: "System Log dan Activity Log: Assign, Remove, dan Edit (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-849
  - TC-FA-RP-850
  - TC-FA-RP-851
  - TC-FA-RP-852
  - TC-FA-RP-853
coverage:
  web: automated
---

# System Log dan Activity Log: Assign, Remove, dan Edit (4/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #3 (Total Control kedua Rina Wulandari), #12 (target Read Only Maya Anggraeni), #13 (target Group Manager Kevin Susanto), #18 (pohon group), #19 (seed Role Transaksi), #20 (seed approval Transfer), #43 (seed Group Manager). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca System Log (Settings > User > Detail Siti Rahmawati > Tab System Log) dan Activity Log FAMS lewat UI. Baseline jumlah entri kombinasi (Action, Object, Name, Field) pada System Log dan Activity Log dicatat di langkah Test Steps lewat kemampuan baca (disediakan tim FE/BE) sebelum tiap aksi pemicu; entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas (S-12).
- State yang diubah dan pemulihannya: Tingkat akses Rina Wulandari, Maya Anggraeni, dan Kevin Susanto (Auto-Revert), Require Approval `Disposal`, serta Approval Rule `Transfer` diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-849: System Log dan Activity Log: Auto-Revert Total Control

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Auto-Revert`, Object `Total Control`, Name `Rina Wulandari`, Field `Access Level` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Klik Tab `System` lalu buka Detail Role `Manage accounting`
3. Hapus centang Delete pada baris Rina Wulandari
4. Klik `[Remove]` pada dialog, lalu tunggu aksi selesai
5. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
6. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Auto-Revert`, Object `Total Control`, Name `Rina Wulandari`, Field `Access Level`, Old Value `Total Control`, New Value `—`
7. Buka Activity Log FAMS (menu Activity Log)
8. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Auto-Revert`, Object `Total Control`, Name `Rina Wulandari`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti R` (aktor pengedit, bukan System)

### TC-FA-RP-850: System Log dan Activity Log: Auto-Revert Read Only

9. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Auto-Revert`, Object `Read Only`, Name `Maya Anggraeni`, Field `Access Level` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
10. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage accounting`
11. Centang Create pada baris Maya Anggraeni
12. Klik `[Remove]` pada dialog, lalu tunggu aksi selesai
13. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
14. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Auto-Revert`, Object `Read Only`, Name `Maya Anggraeni`, Field `Access Level`, Old Value `Read Only`, New Value `—`
15. Buka Activity Log FAMS (menu Activity Log)
16. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Auto-Revert`, Object `Read Only`, Name `Maya Anggraeni`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti R` (aktor pengedit, bukan System)

### TC-FA-RP-851: System Log dan Activity Log: Auto-Revert Group Manager

17. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Auto-Revert`, Object `Group Manager`, Name `Kevin Susanto`, Field `Group Manager — Data Center` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
18. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage group`
19. Pilih node `Data Center`
20. Hapus centang Delete pada baris Kevin Susanto
21. Klik `[Remove]` pada dialog, lalu tunggu aksi selesai
22. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
23. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Auto-Revert`, Object `Group Manager`, Name `Kevin Susanto`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`
24. Buka Activity Log FAMS (menu Activity Log)
25. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Auto-Revert`, Object `Group Manager`, Name `Kevin Susanto`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`, Modified By `Siti R` (aktor pengedit, bukan System)

### TC-FA-RP-852: System Log dan Activity Log: Edit Transaction Role: Require Approval

26. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Transaction Role`, Name `Disposal`, Field `Require Approval for Disposal — IT Infrastructure` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
27. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
28. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
29. Aktifkan toggle `Require Approval for Disposal`
30. Tunggu aksi selesai: toggle tetap pada kondisi baru dan indikator memuat hilang
31. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
32. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Transaction Role`, Name `Disposal`, Field `Require Approval for Disposal — IT Infrastructure`, Old Value `Off`, New Value `On`
33. Buka Activity Log FAMS (menu Activity Log)
34. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Transaction Role`, Name `Disposal`, Field `Require Approval for Disposal — IT Infrastructure`, Old Value `Off`, New Value `On`, Modified By `Siti R`

### TC-FA-RP-853: System Log dan Activity Log: Edit Transaction Role: Approval Rule

35. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Transaction Role`, Name `Transfer`, Field `Approval Rule — IT Infrastructure` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
36. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
37. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
38. Pilih radio `All approvers (AND)`
39. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
40. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
41. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Transaction Role`, Name `Transfer`, Field `Approval Rule — IT Infrastructure`, Old Value `OR`, New Value `AND`
42. Buka Activity Log FAMS (menu Activity Log)
43. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Transaction Role`, Name `Transfer`, Field `Approval Rule — IT Infrastructure`, Old Value `OR`, New Value `AND`, Modified By `Siti R`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 43 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 2, 9, 10, 17, 18, 26, 27, 30, 35, 36, 39. Akun aktor pertama sudah login di hook `before` (S-07).
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Name, dan Field serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan urutan Date tidak diasersi dan total entri tidak diasersi (S-12). Langkah pencatatan baseline adalah langkah penghubung (S-03, aksi tanpa `Verifikasi`). Langkah membuka System Log dan Activity Log adalah langkah TC; langkah "buka Fixed Asset > Settings > Role & Permission" antar blok adalah langkah penghubung.
- Spec ini memuat lebih dari 35 langkah (di atas smell): kelima blok satu kelas (pencatatan System Log dan Activity Log Auto-Revert dan Edit konfigurasi), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah tambahan berasal dari lima langkah pencatatan baseline jumlah entri (S-12).
- Temuan untuk QA:
  - TC-FA-RP-849 sampai 851 Expected menyebut Modified By `Siti R` "aktor pengedit, bukan System" pada Activity Log; spec menuliskannya pada Verifikasi Activity Log.
