---
id: TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2
title: "Assign User ke Group Role di Detail Role (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-255
  - TC-FA-RP-256
  - TC-FA-RP-257
  - TC-FA-RP-258
  - TC-FA-RP-259
  - TC-FA-RP-260
coverage:
  web: automated
---

# Assign User ke Group Role di Detail Role (2/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #17 (Gunawan Halim Home Group `Data Center`, Hesti Rahma Home Group `Logistics Warehouse`, Joko Santoso Home Group `IT Infrastructure`, Indra Kusuma tanpa Home Group; semuanya Active, Activated) dan #18 (pohon group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-255: Kandidat ber-Home Group constraint pada picker Group Role: Gunawan Halim (Data Center) pada node Data Center

1. Klik Tab `System`
2. Buka Detail Role `Manage files`
3. Klik `[+ Assign]`
4. Pilih group `Data Center`
5. Ketik Search `Gunawan Halim`, tekan Enter
6. Verifikasi Gunawan Halim ada di daftar picker (node sama dengan constraint)

### TC-FA-RP-256: Kandidat ber-Home Group constraint pada picker Group Role: Gunawan Halim (Data Center) pada node Rack A1

7. Ubah field Group menjadi `Rack A1`
8. Ganti isi kotak search dengan `Gunawan Halim`, tekan Enter
9. Verifikasi Gunawan Halim ada di daftar picker (descendant tingkat berikut dari constraint)

### TC-FA-RP-257: Kandidat ber-Home Group constraint pada picker Group Role: Gunawan Halim (Data Center) pada node Helpdesk

10. Ubah field Group menjadi `Helpdesk`
11. Ganti isi kotak search dengan `Gunawan Halim`, tekan Enter
12. Verifikasi Gunawan Halim tidak ada di daftar picker (node sibling di luar constraint; empty state hasil Search)

### TC-FA-RP-258: Kandidat ber-Home Group constraint pada picker Group Role: Gunawan Halim (Data Center) pada node IT Infrastructure

13. Ubah field Group menjadi `IT Infrastructure`
14. Ganti isi kotak search dengan `Gunawan Halim`, tekan Enter
15. Verifikasi Gunawan Halim tidak ada di daftar picker (node ancestor di luar constraint; empty state hasil Search)

### TC-FA-RP-259: Kandidat ber-Home Group constraint pada picker Group Role: Indra Kusuma (tanpa Home Group) pada node Helpdesk

16. Ubah field Group menjadi `Helpdesk`
17. Ganti isi kotak search dengan `Indra Kusuma`, tekan Enter
18. Verifikasi Indra Kusuma ada di daftar picker (user tanpa constraint bebas di group mana pun)

### TC-FA-RP-260: Kandidat ber-Home Group constraint pada picker Group Role: Joko Santoso (IT Infrastructure) pada node Rack A1

19. Ubah field Group menjadi `Rack A1`
20. Ganti isi kotak search dengan `Joko Santoso`, tekan Enter
21. Verifikasi Joko Santoso ada di daftar picker (descendant tiga tingkat di bawah constraint)
22. Tutup popup lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- Langkah penghubung (S-03): langkah 1, 22. Akun aktor pertama sudah login di hook `before` (S-07).
- Keenam TC memakai satu pembukaan popup `[+ Assign]` pada Detail Role `Manage files`; group dan kotak search diganti antar TC (halaman yang dipakai berulang, konvensi bagian 3 prinsip 13) karena semua kasus hanya memilih group dan mengamati daftar picker tanpa submit. Langkah "Klik `[+ Assign]` dan pilih group" pada TC-FA-RP-256 sampai 260 menjadi "Ubah field Group".
- Absence pada TC-FA-RP-257 dan 258 memakai empty state hasil Search sebagai anchor positif (butir 8b.2).
- Temuan untuk QA:
  - TC-FA-RP-255 sampai 260: tidak dinyatakan apakah kotak search tetap berisi sesudah field Group diubah; spec mengganti isi kotak search sesudah tiap perubahan group.
