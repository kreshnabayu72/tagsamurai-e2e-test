---
id: TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2
title: "System Log dan Activity Log: Assign, Remove, dan Edit (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-839
  - TC-FA-RP-840
  - TC-FA-RP-841
  - TC-FA-RP-842
  - TC-FA-RP-843
coverage:
  web: automated
---

# System Log dan Activity Log: Assign, Remove, dan Edit (2/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #13 (target Group Manager Kevin Susanto), #15 (kolam pengguna Standard: Budi Santoso), #18 (pohon group: `Data Center`), #43 (seed Group Manager). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca System Log (Settings > User > Detail Siti Rahmawati > Tab System Log) dan Activity Log FAMS lewat UI. Baseline jumlah entri kombinasi (Action, Object, Name, Field) pada System Log dan Activity Log dicatat di langkah Test Steps lewat kemampuan baca (disediakan tim FE/BE) sebelum tiap aksi pemicu; entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas (S-12). Penghapusan group `Data Center` lewat UI Settings > Groups dan pemulihannya lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Penugasan Group Manager Kevin Susanto, group `Data Center`, serta penugasan Budi Santoso pada `Manage Open API` dan `Manage files` diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-840: System Log dan Activity Log: Remove Group Manager (Group Deleted)

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Kevin Susanto`, Field `Group Manager — Data Center` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Buka Settings > Groups
3. Hapus group `Data Center` (konfirmasi dialog `Delete Group`), lalu tunggu aksi selesai
4. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
5. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Kevin Susanto`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`
6. Buka Activity Log FAMS (menu Activity Log)
7. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Kevin Susanto`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`
8. Pulihkan group `Data Center` dan penugasan Group Manager Kevin Susanto lewat seeding API, hingga tersimpan

### TC-FA-RP-839: System Log dan Activity Log: Remove Group Manager

9. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Group Manager`, Name `Kevin Susanto`, Field `Group Manager — Data Center` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
10. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Group Manager`
11. Klik `[⋯]` baris Kevin Susanto di `Data Center` di Tab `Group Manager` lalu `Remove`
12. Klik `[Remove]`, lalu tunggu aksi selesai
13. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
14. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Group Manager`, Name `Kevin Susanto`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`
15. Buka Activity Log FAMS (menu Activity Log)
16. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Group Manager`, Name `Kevin Susanto`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`

### TC-FA-RP-841: System Log dan Activity Log: Assign Global Role

17. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign`, Object `Global Role`, Name `Budi Santoso`, Field `Manage Open API` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
18. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage Open API`
19. Klik `[+ Assign]`
20. Centang Budi Santoso lalu klik `[Assign]`, lalu tunggu aksi selesai
21. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
22. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Global Role`, Name `Budi Santoso`, Field `Manage Open API`, Old Value `—`, New Value `Assigned`
23. Buka Activity Log FAMS (menu Activity Log)
24. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Global Role`, Name `Budi Santoso`, Field `Manage Open API`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`

### TC-FA-RP-842: System Log dan Activity Log: Remove Global Role

25. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Global Role`, Name `Budi Santoso`, Field `Manage Open API` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
26. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage Open API`
27. Klik `[⋯]` baris Budi Santoso lalu `Remove`
28. Klik `[Remove]`, lalu tunggu aksi selesai
29. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
30. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Global Role`, Name `Budi Santoso`, Field `Manage Open API`, Old Value `Assigned`, New Value `—`
31. Buka Activity Log FAMS (menu Activity Log)
32. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Global Role`, Name `Budi Santoso`, Field `Manage Open API`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`

### TC-FA-RP-843: System Log dan Activity Log: Assign Group Role

33. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign`, Object `Group Role`, Name `Budi Santoso`, Field `Manage files — Data Center` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
34. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage files`
35. Pilih node `Data Center`
36. Klik `[+ Assign]`
37. Centang Budi Santoso lalu klik `[Assign]`, lalu tunggu aksi selesai
38. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
39. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Group Role`, Name `Budi Santoso`, Field `Manage files — Data Center`, Old Value `—`, New Value `Assigned`
40. Buka Activity Log FAMS (menu Activity Log)
41. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Group Role`, Name `Budi Santoso`, Field `Manage files — Data Center`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 41 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 2, 9, 10, 17, 18, 25, 26, 33, 34. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 8; tidak ada `Verifikasi`.
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Name, dan Field serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan urutan Date tidak diasersi dan total entri tidak diasersi (S-12). Langkah pencatatan baseline adalah langkah penghubung (S-03, aksi tanpa `Verifikasi`). Langkah membuka System Log dan Activity Log adalah langkah TC; langkah "buka Fixed Asset > Settings > Role & Permission" antar blok adalah langkah penghubung.
- Urutan TC: TC-FA-RP-840, 839, 841, 842, 843 (TC-FA-RP-840 lebih dulu): group `Data Center` dan penugasan Group Manager Kevin Susanto dipulihkan lewat seeding API sesudah TC-FA-RP-840 sehingga TC-FA-RP-839 dan TC-FA-RP-843 memakai `Data Center` yang utuh.
- Spec ini memuat lebih dari 35 langkah (di atas smell): kelima blok satu kelas (pencatatan System Log dan Activity Log aksi tingkat akses dan peran), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah tambahan berasal dari lima langkah pencatatan baseline jumlah entri (S-12).
- Temuan untuk QA:
  - TC-FA-RP-840 Expected memuat Object `Group Manager (Group Deleted)` pada baris System Log dan Activity Log; Action `Remove` dan Object berbeda dari konvensi entri Changelog `Remove (Group Deleted)`; spec mengikuti teks TC.
  - TC-FA-RP-839 langkah 3 menyebut "entri `Remove Group Manager`" sebagai pencarian entri di Activity Log; spec mengenali entri lewat kombinasi kolom dan selisih terhadap baseline.
  - Post Condition TC-FA-RP-840 (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
