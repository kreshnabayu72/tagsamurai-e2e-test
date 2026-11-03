---
id: TC-FA-RP-E2E-256-system-log-dan-activity-log-assign-remove-dan-edit-5
title: "System Log dan Activity Log: Assign, Remove, dan Edit (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-854
coverage:
  web: automated
---

# System Log dan Activity Log: Assign, Remove, dan Edit (5/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #21 (seed pemegang Update `Manage asset & TAG`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca System Log (Settings > User > Detail Siti Rahmawati > Tab System Log) dan Activity Log FAMS lewat UI. Baseline jumlah entri kombinasi (Action, Object, Name, Field) pada System Log dan Activity Log dicatat di langkah Test Steps lewat kemampuan baca (disediakan tim FE/BE) sebelum tiap aksi pemicu; entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas (S-12).
- State yang diubah dan pemulihannya: Toggle Require Approval for Registration pada `IT Infrastructure` diubah spec ini; dipulihkan ke Pre-setup #21 di hook `after`.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-854: System Log dan Activity Log: Edit Group Role: Require Approval for Registration

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Edit`, Object `Group Role`, Name `Manage asset & TAG`, Field `Require Approval for Registration — IT Infrastructure` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Klik Tab `System` lalu buka Detail Role `Manage asset & TAG`
3. Klik node `IT Infrastructure`
4. Aktifkan toggle `Require Approval for Registration`
5. Tunggu aksi selesai: toggle tetap pada kondisi baru dan indikator memuat hilang
6. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
7. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Group Role`, Name `Manage asset & TAG`, Field `Require Approval for Registration — IT Infrastructure`, Old Value `Off`, New Value `On`
8. Buka Activity Log FAMS (menu Activity Log)
9. Verifikasi Activity Log memuat satu entri baru di atas baseline (jumlah entri kombinasi ini bertambah tepat satu): Action `Edit`, Object `Group Role`, Name `Manage asset & TAG`, Field `Require Approval for Registration — IT Infrastructure`, Old Value `Off`, New Value `On`, Modified By `Siti R`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 9 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 2, 5. Akun aktor pertama sudah login di hook `before` (S-07).
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Name, dan Field serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan urutan Date tidak diasersi dan total entri tidak diasersi (S-12). Langkah pencatatan baseline adalah langkah penghubung (S-03, aksi tanpa `Verifikasi`). Langkah membuka System Log dan Activity Log adalah langkah TC; langkah "buka Fixed Asset > Settings > Role & Permission" antar blok adalah langkah penghubung.
- Temuan untuk QA:
  - TC-FA-RP-854 Expected memuat Name `Manage asset & TAG` (nama role, bukan user) pada Object `Group Role`; spec mengikuti teks TC.
