---
id: TC-FA-RP-E2E-300-assign-user-ke-global-role-di-detail-role-2
title: "Assign User ke Global Role di Detail Role (2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-244
  - TC-FA-RP-245
  - TC-FA-RP-246
coverage:
  web: automated
---

# Assign User ke Global Role di Detail Role (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login akun pertama di hook `before`; akun berikutnya lewat langkah ganti akun eksplisit):

| Urutan | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| 1 | Total Control | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage global user & role (Update) | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, ...), #39 (Detail Role terisi; TC-FA-RP-244), #1 (Admin Utama Default User), #3 (Rina Wulandari Total Control kedua), #12 (Maya Anggraeni Read Only), #16 (Siti Rahayu Inactive, Eka Saputra Pending Activation, Fitri Handayani Pending Email Confirmation). Pada TC-FA-RP-244 Ahmad Fauzi memegang `Manage Open API` aktif dan Budi Santoso memegang `Manage Open API` dengan switch dimatikan di Settings > User (inactive-retained), keduanya di-seed lewat seeding API; Dimas Pranata eligible.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-244: Popup Assign User Global Role mengecualikan aktor, penugasan yang sudah ada, Default User, dan Total Control

1. Klik Tab `System`
2. Buka Detail Role `Manage Open API` lalu klik `[+ Assign]`
3. Ketik Search `Siti Rahmawati`, tekan Enter
4. Verifikasi Siti Rahmawati (aktor) tidak ada di daftar (empty state hasil Search)
5. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
6. Verifikasi Ahmad Fauzi (penugasan aktif) tidak ada di daftar (empty state hasil Search)
7. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
8. Verifikasi Budi Santoso (inactive-retained) tidak ada di daftar (empty state hasil Search)
9. Ganti isi kotak search dengan `Admin Utama`, tekan Enter
10. Verifikasi Admin Utama (Default User) tidak ada di daftar (empty state hasil Search)
11. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
12. Verifikasi Rina Wulandari (Total Control) tidak ada di daftar (empty state hasil Search)
13. Ganti isi kotak search dengan `Dimas Pranata`, tekan Enter
14. Verifikasi Dimas Pranata (eligible) ada di daftar

### TC-FA-RP-245: Popup Assign User Global Role: Status dan Activation Status apa pun eligible

15. Tutup popup lewat `✕`
16. Klik `[+ Assign]`
17. Verifikasi Siti Rahayu, Eka Saputra, dan Fitri Handayani ada di daftar picker
18. Centang Siti Rahayu, Eka Saputra, dan Fitri Handayani lalu klik `[Assign]`
19. Verifikasi muncul toast sukses: `Success, Manage Open API has been assigned.`
20. Verifikasi baris Siti Rahayu, Eka Saputra, dan Fitri Handayani tampil dan tersimpan di Detail Role `Manage Open API`

### TC-FA-RP-246: Aktor Manage global user & role tidak melihat kandidat Total Control dan Read Only di popup Assign Global Role

21. Logout dari akun Total Control (Siti Rahmawati)
22. Login sebagai Manage global user & role (Update) (`murGlobal_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MUR_GLOBAL_PASSWORD`)
23. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `System`
24. Buka Detail Role `Manage Open API` lalu klik `[+ Assign]`
25. Ketik Search `Rina Wulandari`, tekan Enter
26. Verifikasi Rina Wulandari tidak ada di daftar picker (empty state hasil Search)
27. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
28. Verifikasi Maya Anggraeni tidak ada di daftar picker (empty state hasil Search)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 28 langkah.
- Langkah penghubung (S-03): langkah 1, 15, 21–23. Akun aktor pertama sudah login di hook `before` (S-07).
- Ganti akun (langkah 21–23) hanya sekali pada TC-FA-RP-246; login akun pertama di hook `before`. Hook `after` mengembalikan sesi ke akun default suite.
- Absence di picker memakai empty state hasil Search sebagai anchor positif (butir 8b.2); pada TC-FA-RP-244 pembanding positifnya ada pada `Verifikasi` Dimas Pranata di langkah akhir blok.
- Pembagian TC lintas spec: TC-FA-RP-241, 242, dan 243 ada di spec 072.
- Temuan untuk QA:
  - TC-FA-RP-244 dan Pre-setup #39 (Detail Role `Manage Open API` terisi dengan Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) berbeda dengan precondition TC-FA-RP-244 (Dimas Pranata eligible); spec mengikuti precondition TC-FA-RP-244 dengan seeding per TC.
  - TC-FA-RP-245 Expected "Ketiga user ada di daftar dan tersimpan" tidak menyebut Search; spec memverifikasi ketiganya pada daftar picker, lalu pada Detail Role setelah Assign.
  - TC-FA-RP-246 precondition a hanya menyebut Login sbg Role Manage global user & role (Update); spec memakai Pre-setup #6 (Hendra Wijaya).
