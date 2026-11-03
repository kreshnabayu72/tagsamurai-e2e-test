---
id: TC-AC-RP-E2E-041-assign-group-manager-aksi-berhasil
title: "Assign Group Manager: Happy Path, Child dengan Ancestor Ber-GM, dan User yang Sama di Group Kedua"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-150
  - TC-AC-RP-151
  - TC-AC-RP-152
coverage:
  web: automated
---

# Assign Group Manager: Happy Path, Child dengan Ancestor Ber-GM, dan User yang Sama di Group Kedua

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-150: Assign Group Manager happy path

1. Klik tab `Group Manager`
2. Klik tombol "+ Assign"
3. Buka field Group lalu pilih node `Region A`
4. Ketik Search `John Dohan`, tekan Enter
5. Centang `John Dohan`
6. Klik `[Assign]`
7. Verifikasi toast "Success, Group Manager has been assigned."
8. Verifikasi baris `John Dohan` — `Region A` muncul di Tab Group Manager
9. Klik tab `System`
10. Klik `⋯` pada baris `Manage partner` di section Group Role lalu klik `Detail`
11. Klik node `Region A`
12. Ketik Search `John Dohan`, tekan Enter
13. Verifikasi `John Dohan` tampil dengan C/R/U/D penuh pada node `Region A`
14. Verifikasi tidak ada baris tambahan untuk `Branch 1`
15. Pulihkan baseline: penugasan Group Manager `John Dohan` di `Region A` dihapus
16. Buka halaman `Settings > Role & Permission`, lalu klik tab `Group Manager`

### TC-AC-RP-151: Assign GM ke child yang ancestor-nya sudah punya GM lain

17. Klik tombol "+ Assign"
18. Buka field Group lalu pilih node `Jakarta`
19. Ketik Search `Alex Tan`, tekan Enter
20. Centang `Alex Tan`
21. Klik `[Assign]`
22. Verifikasi popup tertutup
23. Verifikasi Tab Group Manager memuat baris `Fajar Nugroho` — `Region Jawa`
24. Verifikasi Tab Group Manager memuat baris `Alex Tan` — `Jakarta`
25. Pulihkan baseline: penugasan Group Manager `Alex Tan` di `Jakarta` dihapus

### TC-AC-RP-152: Assign GM user yang sama di group kedua

26. Klik tombol "+ Assign"
27. Buka field Group lalu pilih node `Region A`
28. Ketik Search `Fajar Nugroho`, tekan Enter
29. Centang `Fajar Nugroho`
30. Klik `[Assign]`
31. Verifikasi popup tertutup
32. Verifikasi `Fajar Nugroho` memiliki tiga baris GM (`Region A`, `Region Jawa`, `Sumatera`)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 9, 15, 16, 25 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 4, 12, 19, 28.
- Penghapusan penugasan di langkah 15 dan 25 dilakukan lewat kemampuan reset baseline; penugasan `Fajar Nugroho` di `Region A` (TC-AC-RP-152) dipulihkan hook `after`.
- Temuan untuk QA:
  - TC-AC-RP-150 Expected b "tidak ada baris tambahan untuk Branch 1" tidak menyebut surface (Role Detail atau Tab Group Manager); spec mengasersinya di Role Detail node `Region A` setelah baris `John Dohan` tampil, padahal Pre-setup #15 menyebut `John Dohan` memegang R di `Branch 1` untuk `Manage distributor` (kurang precondition).
  - TC-AC-RP-151 dan 152 Expected "Assign sukses" tidak menyebut teks toast; spec mengasersi popup tertutup dan hasil di Tab Group Manager.
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
