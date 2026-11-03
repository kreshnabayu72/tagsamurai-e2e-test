---
id: TC-AC-RP-E2E-035-assign-total-control-beralih-dari-tingkat-akses-lain
title: "Assign Total Control: Beralih dari Read Only dan dari Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-125
  - TC-AC-RP-126
coverage:
  web: automated
---

# Assign Total Control: Beralih dari Read Only dan dari Group Manager

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-125: Assign Total Control ke user Read Only (beralih langsung)

1. Klik tombol "+ Assign"
2. Ketik Search `Dewi Anggraini`, tekan Enter
3. Centang `Dewi Anggraini`
4. Klik `[Assign]`
5. Verifikasi toast "Success, Total Control has been assigned."
6. Verifikasi `Dewi Anggraini` muncul di Tab Total Control
7. Klik tab `Read Only`
8. Verifikasi Tab Read Only masih memuat baris `Lisa Wong`
9. Verifikasi `Dewi Anggraini` hilang dari Tab Read Only
10. Pulihkan baseline: `Dewi Anggraini` kembali Read Only
11. Klik tab `Total Control`

### TC-AC-RP-126: Assign Total Control ke Group Manager melepas seluruh penugasan GM

12. Klik tombol "+ Assign"
13. Ketik Search `Fajar Nugroho`, tekan Enter
14. Centang `Fajar Nugroho`
15. Klik `[Assign]`
16. Verifikasi `Fajar Nugroho` muncul di Tab Total Control
17. Klik tab `Group Manager`
18. Verifikasi Tab Group Manager masih memuat baris `Jane Smith` — `Region Jawa`
19. Verifikasi kedua baris Group Manager `Fajar Nugroho` (`Region Jawa` dan `Sumatera`) hilang dari Tab Group Manager
20. Pulihkan baseline: penugasan Group Manager `Fajar Nugroho` di `Region Jawa` dan `Sumatera` dikembalikan

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 10, 11, 20 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 2, 13.
- Pembanding absence: baris `Lisa Wong` (Pre-setup #13) dan baris `Jane Smith` — `Region Jawa` (Pre-setup #14) membuktikan tabel sudah termuat sebelum asersi hilang.
- Temuan untuk QA:
  - TC-AC-RP-126 Expected "dalam transaksi yang sama" tidak dapat diamati dari UI; spec hanya mengasersi hasil akhir (Fajar Nugroho di Tab Total Control dan kedua baris GM hilang).
  - TC-AC-RP-125 dan 126 tidak mencantumkan teks toast pada TC-AC-RP-126; spec tidak mengasersi toast di blok itu karena tidak ada di Expected.
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
