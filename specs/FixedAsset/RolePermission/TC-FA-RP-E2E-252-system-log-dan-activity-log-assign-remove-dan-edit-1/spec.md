---
id: TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1
title: "System Log dan Activity Log: Assign, Remove, dan Edit (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-834
  - TC-FA-RP-835
  - TC-FA-RP-836
  - TC-FA-RP-837
  - TC-FA-RP-838
coverage:
  web: automated
---

# System Log dan Activity Log: Assign, Remove, dan Edit (1/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #12 (target Read Only Maya Anggraeni), #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group: `Data Center`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca System Log (Settings > User > Detail Siti Rahmawati > Tab System Log) dan Activity Log FAMS lewat UI. Baseline jumlah entri kombinasi (Action, Object, Name, Field) pada System Log dan Activity Log dicatat di langkah Test Steps lewat kemampuan baca (disediakan tim FE/BE) sebelum tiap aksi pemicu; entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas (S-12).
- State yang diubah dan pemulihannya: Tingkat akses Ahmad Fauzi dan Maya Anggraeni serta penugasan Group Manager Ahmad Fauzi diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-834: System Log dan Activity Log: Assign Total Control

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign`, Object `Total Control`, Name `Ahmad Fauzi`, Field `Access Level` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Klik `[+ Assign]` di Tab `Total Control`
3. Centang Ahmad Fauzi lalu klik `[Assign]`, lalu tunggu aksi selesai
4. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
5. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Total Control`, Name `Ahmad Fauzi`, Field `Access Level`, Old Value `—`, New Value `Total Control`
6. Buka Activity Log FAMS (menu Activity Log)
7. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Total Control`, Name `Ahmad Fauzi`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti R`

### TC-FA-RP-835: System Log dan Activity Log: Remove Total Control

8. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi`, Field `Access Level` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
9. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Total Control`
10. Klik `[⋯]` baris Ahmad Fauzi di Tab `Total Control` lalu `Remove`
11. Klik `[Remove]`, lalu tunggu aksi selesai
12. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
13. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi`, Field `Access Level`, Old Value `Total Control`, New Value `—`
14. Buka Activity Log FAMS (menu Activity Log)
15. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti R`

### TC-FA-RP-836: System Log dan Activity Log: Assign Read Only

16. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign`, Object `Read Only`, Name `Ahmad Fauzi`, Field `Access Level` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
17. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Read Only`
18. Klik `[+ Assign]` di Tab `Read Only`
19. Centang Ahmad Fauzi lalu klik `[Assign]`, lalu tunggu aksi selesai
20. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
21. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Read Only`, Name `Ahmad Fauzi`, Field `Access Level`, Old Value `—`, New Value `Read Only`
22. Buka Activity Log FAMS (menu Activity Log)
23. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Read Only`, Name `Ahmad Fauzi`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti R`

### TC-FA-RP-837: System Log dan Activity Log: Remove Read Only

24. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Read Only`, Name `Maya Anggraeni`, Field `Access Level` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
25. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Read Only`
26. Klik `[⋯]` baris Maya Anggraeni di Tab `Read Only` lalu `Remove`
27. Klik `[Remove]`, lalu tunggu aksi selesai
28. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
29. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Read Only`, Name `Maya Anggraeni`, Field `Access Level`, Old Value `Read Only`, New Value `—`
30. Buka Activity Log FAMS (menu Activity Log)
31. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Remove`, Object `Read Only`, Name `Maya Anggraeni`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti R`

### TC-FA-RP-838: System Log dan Activity Log: Assign Group Manager

32. Pulihkan Ahmad Fauzi ke tanpa tingkat akses lewat seeding API, hingga tersimpan
33. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign`, Object `Group Manager`, Name `Ahmad Fauzi`, Field `Group Manager — Data Center` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
34. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Group Manager`
35. Klik `[+ Assign]` di Tab `Group Manager`
36. Pilih group `Data Center`, centang Ahmad Fauzi, klik `[Assign]`, lalu tunggu aksi selesai
37. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
38. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Group Manager`, Name `Ahmad Fauzi`, Field `Group Manager — Data Center`, Old Value `—`, New Value `Assigned`
39. Buka Activity Log FAMS (menu Activity Log)
40. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Assign`, Object `Group Manager`, Name `Ahmad Fauzi`, Field `Group Manager — Data Center`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 40 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, 9, 16, 17, 24, 25, 33, 34. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 32; tidak ada `Verifikasi`.
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Name, dan Field serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan urutan Date tidak diasersi dan total entri tidak diasersi (S-12). Langkah pencatatan baseline adalah langkah penghubung (S-03, aksi tanpa `Verifikasi`). Langkah membuka System Log dan Activity Log adalah langkah TC; langkah "buka Fixed Asset > Settings > Role & Permission" antar blok adalah langkah penghubung.
- Ahmad Fauzi menjadi Total Control pada TC-FA-RP-834 dan dilepas pada TC-FA-RP-835, lalu menjadi Read Only pada TC-FA-RP-836; pemulihan ke tanpa tingkat akses sebelum TC-FA-RP-838 dilakukan lewat seeding API.
- Spec ini memuat lebih dari 35 langkah (di atas smell): kelima blok satu kelas (pencatatan System Log dan Activity Log aksi tingkat akses), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan berasal dari lima langkah pencatatan baseline jumlah entri (S-12).
- TC-FA-RP-839 sampai TC-FA-RP-854 ada di spec 253 sampai 256.
- Temuan untuk QA:
  - TC-FA-RP-834 sampai 838 memakai Pre-setup #15, #18, #43, #13, #3, #12, #19, #20, #21, #39, dan #42 sebagai rujukan tunggal tanpa memisah data tiap TC; spec hanya mencantumkan rujukan yang dipakai langkah.
  - Expected TC-FA-RP-834 sampai 838 tidak menyebut Date entri log; kolom Date tidak diasersi.
