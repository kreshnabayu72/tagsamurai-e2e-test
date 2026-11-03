---
id: TC-AC-RP-E2E-042-remove-group-manager
title: "Remove Group Manager: Cancel, Confirm, dan Ancestor Tidak Menyentuh GM Descendant"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-156
  - TC-AC-RP-157
  - TC-AC-RP-158
coverage:
  web: automated
---

# Remove Group Manager: Cancel, Confirm, dan Ancestor Tidak Menyentuh GM Descendant

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #14 (penugasan Group Manager), dan #15 (penugasan peran individual). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Data Dinamis TC #1 (TC-AC-RP-157): `Alex Tan` GM `Region Jawa` dan GM langsung `Jakarta`; dibuat di hook `before` lewat seeding API (kemampuan disediakan tim BE/FE) dan dipulihkan automation baseline.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-158: Cancel dialog Remove Group Manager

1. Klik tab `Group Manager`
2. Klik `⋯` baris `Jane Smith` lalu klik `Remove`
3. Klik `[Cancel]`
4. Verifikasi dialog tertutup
5. Verifikasi baris `Jane Smith` tetap di Tab Group Manager

### TC-AC-RP-156: Screening dan Confirm Remove Group Manager

6. Klik `⋯` baris `Fajar Nugroho` — `Sumatera` lalu klik `Remove`
7. Verifikasi Title dialog "Remove Group Manager"
8. Verifikasi body dialog memuat bullet • Fajar N, "This will remove Group Manager access.", "Their full-control roles in the related group will be reset.", dan "Are you sure you want to remove it?"
9. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` (destructive)
10. Klik `[Remove]`
11. Verifikasi toast "Success, Group Manager has been removed."
12. Verifikasi baris `Fajar Nugroho` — `Sumatera` hilang
13. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tetap
14. Klik tab `System`
15. Klik `⋯` pada baris `Manage partner` di section Group Role lalu klik `Detail`
16. Klik node `Sumatera`
17. Ketik Search `Fajar Nugroho`, tekan Enter
18. Verifikasi Penugasan Peran Grup `Fajar Nugroho` di `Sumatera` direset: `Fajar Nugroho` tidak tampil di node `Sumatera`
19. Pulihkan baseline: penugasan Group Manager `Fajar Nugroho` di `Sumatera` dikembalikan
20. Buka halaman `Settings > Role & Permission`, lalu klik tab `Group Manager`

### TC-AC-RP-157: Remove GM di ancestor tidak menyentuh GM langsung di descendant

21. Klik `⋯` baris `Alex Tan` — `Region Jawa` lalu klik `Remove`
22. Klik `[Remove]`
23. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tampil
24. Verifikasi baris `Alex Tan` — `Region Jawa` hilang
25. Verifikasi baris `Alex Tan` — `Jakarta` tetap ada
26. Pulihkan baseline: `Alex Tan` kembali GM `Region Jawa` lewat kemampuan reset FE/BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 14, 19, 20, 26 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 17.
- Penyimpangan urutan (S-05, S-10): TC-AC-RP-158 (Cancel) diletakkan paling awal, sebelum TC-AC-RP-156 dan 157 (aksi yang menghapus data).
- Pembanding absence (8b butir 2): asersi baris `Fajar Nugroho` — `Sumatera` hilang (langkah 12) berjangkar pada toast Remove langkah 11; baris `Fajar Nugroho` — `Region Jawa` tetap (langkah 13) diasersi sesudah langkah 12 mengikuti urutan Expected TC-AC-RP-156 dan menjadi pembanding, bukan anchor langkah 12. Baris `Fajar Nugroho` — `Region Jawa` tampil (langkah 23, pembanding generik dari Pre-setup #14) mendahului asersi baris `Alex Tan` — `Region Jawa` hilang (langkah 24) pada tabel yang sama. Urutan langkah 24 sebelum langkah 25 mengikuti Expected TC-AC-RP-157.
- Anchor positif asersi absence (S-03, 8b butir 2): toast "Success, Group Manager has been removed." pada langkah 11 (Remove `Fajar Nugroho` — `Sumatera`) menjadi anchor positif untuk asersi absence langkah 18 (`Fajar Nugroho` tidak tampil di node `Sumatera` setelah Search); tidak ada langkah empty state "No results found" tambahan.
- Temuan untuk QA:
  - TC-AC-RP-157 tidak menyebut toast hasil Remove; spec hanya mengasersi baris di Tab Group Manager sesuai Expected.
  - TC-AC-RP-156 Expected c "Penugasan Peran Grup direset (tidak tampil di node Sumatera)" tidak menyebut Group Role mana; spec memakai `Manage partner` yang sama dengan langkah pembuka TC sumber.
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
