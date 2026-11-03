---
id: TC-FA-RP-E2E-072-assign-user-ke-global-role-di-detail-role
title: "Assign User ke Global Role di Detail Role (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-241
  - TC-FA-RP-242
  - TC-FA-RP-243
coverage:
  web: automated
---

# Assign User ke Global Role di Detail Role (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, dan kolam pengguna Standard). Pada TC-FA-RP-243 Budi Santoso di-seed tanpa penugasan `Manage accounting`.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-241: Assign satu user ke Global Role: baris baru dengan Read terkunci dan C/U/D tidak aktif

1. Klik Tab `System`
2. Catat kolom Users baris `Manage accounting` sebagai baseline
3. Buka Detail Role `Manage accounting`
4. Klik `[+ Assign]`
5. Centang Budi Santoso lalu klik `[Assign]`
6. Verifikasi muncul toast sukses: `Success, Manage accounting has been assigned.` (pola `Success, [Role Name] has been assigned.` dengan `[Role Name]` = `Manage accounting`)
7. Verifikasi baris Budi Santoso tampil dengan Read tercentang dan Disabled
8. Verifikasi Create, Update, dan Delete pada baris Budi Santoso tidak tercentang
9. Klik segmen `System` pada breadcrumb
10. Verifikasi kolom Users baris `Manage accounting` di Tab System bertambah satu dari baseline

### TC-FA-RP-242: Assign ke Global Role dengan kolom tidak berlaku menampilkan `—` pada sel tersebut

11. Buka Detail Role `Import data`
12. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]`
13. Amati sel baris Budi Santoso
14. Verifikasi Create dan Read berupa checkbox
15. Verifikasi Update dan Delete berupa teks `—` tanpa elemen interaktif
16. Verifikasi Read tercentang dan Disabled

### TC-FA-RP-243: Assign tiga user ke Global Role menghasilkan satu toast tunggal

17. Hapus penugasan `Manage accounting` Budi Santoso lewat seeding API
18. Klik segmen `System` pada breadcrumb
19. Tunggu toast lama hilang otomatis
20. Buka Detail Role `Manage accounting`
21. Klik `[+ Assign]`
22. Centang Ahmad Fauzi, Budi Santoso, dan Dimas Pranata lalu klik `[Assign]`
23. Verifikasi muncul satu toast sukses: `Success, Manage accounting has been assigned.`
24. Verifikasi ketiga baris tampil dengan Read terkunci (tercentang dan Disabled)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 24 langkah.
- Langkah penghubung (S-03): langkah 1–2, 9, 18–19. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 17; tidak ada `Verifikasi`.
- Baris yang baru ditambahkan pada Detail Role dibaca langsung pada tabel Detail Role (jumlah baris kecil); tidak ada Search penemu baris.
- Post Condition TC-FA-RP-241 (Tab Role Settings > User milik Budi Santoso menampilkan switch `Manage accounting` aktif) tidak punya langkah observasi dan tidak diasersi (S-01, S-15).
- Baseline kolom Users dicatat sebelum Assign (S-12); asersi memakai selisih satu terhadap baseline. Klik breadcrumb pada langkah 9 dan 18 adalah langkah penghubung menuju Tab System.
- Pembagian TC lintas spec: TC-FA-RP-244, 245, dan 246 ada di spec 300.
- Temuan untuk QA:
  - TC-FA-RP-241 Expected c ("kolom Users bertambah satu") tidak menyebut baseline; spec mencatatnya sebelum Assign.
  - TC-FA-RP-241 Expected d adalah pola toast PRD yang sama dengan Expected a; digabung dalam satu `Verifikasi` toast (S-03).
