---
id: TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3
title: "System Log dan Activity Log: Assign, Remove, dan Edit (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-844
  - TC-FA-RP-845
  - TC-FA-RP-846
  - TC-FA-RP-847
  - TC-FA-RP-848
coverage:
  web: automated
---

# System Log dan Activity Log: Assign, Remove, dan Edit (3/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso), #18 (pohon group), #19 (seed Role Transaksi), #39 (Detail Role terisi). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca System Log (Settings > User > Detail Siti Rahmawati > Tab System Log) dan Activity Log FAMS lewat UI. Baseline jumlah entri kombinasi (Action, Object, Name, Field) pada System Log dan Activity Log dicatat di langkah Test Steps lewat kemampuan baca (disediakan tim FE/BE) sebelum tiap aksi pemicu; entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas (S-12).
- State yang diubah dan pemulihannya: Penugasan Budi Santoso pada `Manage files` di `Helpdesk`, Create baris Ahmad Fauzi pada `Manage accounting`, Delete baris Ahmad Fauzi pada `Manage files` di `Data Center`, serta penugasan Role Transaksi `Disposal` diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-844: System Log dan Activity Log: Remove Group Role

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Group Role`, Name `Budi Santoso`, Field `Manage files — Helpdesk` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Klik Tab `System` lalu buka Detail Role `Manage files`
3. Klik `All Groups`
4. Klik `[⋯]` baris Budi Santoso di `Helpdesk` lalu `Remove`
5. Klik `[Remove]`, lalu tunggu aksi selesai
6. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
7. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Group Role`, Name `Budi Santoso`, Field `Manage files — Helpdesk`, Old Value `Assigned`, New Value `—`
8. Buka Activity Log FAMS (menu Activity Log)
9. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Group Role`, Name `Budi Santoso`, Field `Manage files — Helpdesk`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`

### TC-FA-RP-845: System Log dan Activity Log: Edit Global Role

10. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Global Role`, Name `Ahmad Fauzi`, Field `Manage accounting — Create` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
11. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage accounting`
12. Centang Create pada baris Ahmad Fauzi
13. Tunggu aksi selesai: kotak centang tetap pada kondisi baru dan indikator memuat pada baris hilang
14. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
15. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Global Role`, Name `Ahmad Fauzi`, Field `Manage accounting — Create`, Old Value `Inactive`, New Value `Active`
16. Buka Activity Log FAMS (menu Activity Log)
17. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Global Role`, Name `Ahmad Fauzi`, Field `Manage accounting — Create`, Old Value `Inactive`, New Value `Active`, Modified By `Siti R`

### TC-FA-RP-846: System Log dan Activity Log: Edit Group Role

18. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Group Role`, Name `Ahmad Fauzi`, Field `Manage files — Data Center — Delete` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
19. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage files`
20. Klik `All Groups`
21. Centang Delete pada baris Ahmad Fauzi di `Data Center`
22. Tunggu aksi selesai: kotak centang tetap pada kondisi baru dan indikator memuat pada baris hilang
23. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
24. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Group Role`, Name `Ahmad Fauzi`, Field `Manage files — Data Center — Delete`, Old Value `Inactive`, New Value `Active`
25. Buka Activity Log FAMS (menu Activity Log)
26. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Group Role`, Name `Ahmad Fauzi`, Field `Manage files — Data Center — Delete`, Old Value `Inactive`, New Value `Active`, Modified By `Siti R`

### TC-FA-RP-847: System Log dan Activity Log: Assign Transaction Role

27. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign`, Object `Transaction Role`, Name `Ahmad Fauzi`, Field `Disposal — IT Infrastructure — Asset Admin` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
28. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
29. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
30. Klik `[+ Assign]` pada section Asset Admin
31. Centang Ahmad Fauzi lalu klik `[Assign]`, lalu tunggu aksi selesai
32. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
33. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Transaction Role`, Name `Ahmad Fauzi`, Field `Disposal — IT Infrastructure — Asset Admin`, Old Value `—`, New Value `Assigned`
34. Buka Activity Log FAMS (menu Activity Log)
35. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Transaction Role`, Name `Ahmad Fauzi`, Field `Disposal — IT Infrastructure — Asset Admin`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`

### TC-FA-RP-848: System Log dan Activity Log: Remove Transaction Role

36. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Transaction Role`, Name `Putri Wulandari`, Field `Disposal — IT Infrastructure — Staff` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
37. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
38. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
39. Klik `[⋯]` baris Putri Wulandari lalu `Remove`
40. Klik `[Remove]`, lalu tunggu aksi selesai
41. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
42. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Transaction Role`, Name `Putri Wulandari`, Field `Disposal — IT Infrastructure — Staff`, Old Value `Assigned`, New Value `—`
43. Buka Activity Log FAMS (menu Activity Log)
44. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Transaction Role`, Name `Putri Wulandari`, Field `Disposal — IT Infrastructure — Staff`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 44 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 2, 10, 11, 13, 18, 19, 22, 27, 28, 36, 37. Akun aktor pertama sudah login di hook `before` (S-07).
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Name, dan Field serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan urutan Date tidak diasersi dan total entri tidak diasersi (S-12). Langkah pencatatan baseline adalah langkah penghubung (S-03, aksi tanpa `Verifikasi`). Langkah membuka System Log dan Activity Log adalah langkah TC; langkah "buka Fixed Asset > Settings > Role & Permission" antar blok adalah langkah penghubung.
- Spec ini memuat lebih dari 35 langkah (di atas smell): kelima blok satu kelas (pencatatan System Log dan Activity Log aksi peran dan Role Transaksi), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah tambahan berasal dari lima langkah pencatatan baseline jumlah entri (S-12).
- Temuan untuk QA:
  - TC-FA-RP-845 dan 846 memakai baris Ahmad Fauzi pada Detail Role (Pre-setup #39) dengan Create atau Delete awal tidak aktif; TC tidak menyebut nilai awal itu secara eksplisit selain Old Value pada Expected.
