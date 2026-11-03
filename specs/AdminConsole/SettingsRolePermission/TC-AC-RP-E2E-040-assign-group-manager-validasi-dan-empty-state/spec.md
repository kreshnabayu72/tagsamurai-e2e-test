---
id: TC-AC-RP-E2E-040-assign-group-manager-validasi-dan-empty-state
title: "Assign Group Manager: Validasi Tanpa Group atau User dan Empty State Kandidat"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-153
  - TC-AC-RP-154
  - TC-AC-RP-155
coverage:
  web: automated
---

# Assign Group Manager: Validasi Tanpa Group atau User dan Empty State Kandidat

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Akun aktor kedua (TC-AC-RP-155): Default User Partner `defaultUserPartRP_automated_{namaCompany}@qwertysystem.net` (`Wulan Sari`, entitas `Partner Mandiri`, Pre-setup #19), password `Spectra.env.AC_RP_PART_DU_PASSWORD` (nama ini juga perlu terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login lewat langkah "Ganti akun"; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pre-setup #19: `Partner Mandiri` dengan `Wulan Sari` sebagai satu-satunya user dan pohon group hanya `Default Group`.
- Spec ini tidak mengubah data Pre-setup; tidak ada state yang perlu dipulihkan.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-153: Assign GM tanpa memilih Group

1. Klik tab `Group Manager`
2. Klik tombol "+ Assign"
3. Ketik Search `John Dohan`, tekan Enter
4. Centang `John Dohan` tanpa memilih Group
5. Klik `[Assign]`
6. Verifikasi error field-level pada field Group "You must select a group"
7. Verifikasi popup tetap terbuka

### TC-AC-RP-154: Assign GM tanpa memilih User

8. Hapus centang `John Dohan`
9. Buka field Group lalu pilih node `Region A`
10. Klik `[Assign]` tanpa memilih user
11. Verifikasi inline alert "You must pick a user"
12. Klik `[Cancel]`

### TC-AC-RP-155: Empty state popup Assign GM saat tidak ada kandidat eligible

13. Ganti akun: Logout dari `Siti Nurhaliza`, lalu login sebagai `Wulan Sari` (`defaultUserPartRP_automated_{namaCompany}@qwertysystem.net`)
14. Buka halaman `Settings > Role & Permission`
15. Klik tab `Group Manager`
16. Klik tombol "+ Assign"
17. Buka field Group lalu pilih node `Default Group`
18. Verifikasi picker menampilkan Illustration, Title "All eligible users have been assigned", dan Description "There are no additional eligible users available to select."
19. Verifikasi popup tetap terbuka

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 8, 12 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 3.
- Popup yang dibuka di langkah 2 dipakai bersama TC-AC-RP-153 dan 154 dan ditutup di langkah 12; TC-AC-RP-155 membuka popup sendiri sebagai `Wulan Sari`.
- Langkah 13 adalah Ganti akun eksplisit (S-07); hook `after` memulihkan sesi ke akun default suite.
- Temuan untuk QA:
  - TC-AC-RP-153 dan 154 tidak menyebut apakah popup tetap terbuka setelah alert pada TC-AC-RP-154; spec tidak mengasersinya.
  - TC-AC-RP-155 Precondition menyebut `Partner Mandiri` "tanpa user Standard aktif" sedangkan Pre-setup #19 menyebut `Wulan Sari` Default User sebagai satu-satunya user; spec mengikuti Pre-setup #19.
