---
id: TC-AC-SU-E2E-172-sinkron-role-permission-tier-dan-banner
title: "Sinkron Tier Total Control, Read Only, dan Group Manager dari Settings > Role & Permission ke Banner, Badge Role, dan Tab Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-591
  - TC-AC-SU-592
  - TC-AC-SU-593
  - TC-AC-SU-594
coverage:
  web: automated
---

# Sinkron Tier Total Control, Read Only, dan Group Manager dari Settings > Role & Permission ke Banner, Badge Role, dan Tab Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (Region A dan Region B dari Group Tree Pre-setup hanya menjadi target Group Manager dan tidak diubah):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-172A` | `miketan+{runId}-172a@qwertysystem.net` | Activated, tanpa tier (TC-591) |
| U2 | `Budi Santoso {runId}-172B` | `budisantoso+{runId}-172b@qwertysystem.net` | Activated, tanpa tier (TC-592) |
| U3 | `Rina Putri {runId}-172C` | `rinaputri+{runId}-172c@qwertysystem.net` | Activated, bertier Total Control (TC-593) |
| U4 | `Dedi Kurnia {runId}-172D` | `dedikurnia+{runId}-172d@qwertysystem.net` | Activated, tanpa tier (TC-594) |

- Kemampuan teknis: Fixture BE (seeding user dan tier). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-591: Assign Total Control
1. Klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu assign U1 (`Mike Tan {runId}-172A`) ke Total Control
2. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-172A`, tekan Enter
3. Verifikasi kolom Role baris U1 menampilkan badge `Total Control` menggantikan label jumlah role
4. Klik Name baris U1 untuk membuka Detail, lalu klik Tab Role
5. Verifikasi banner `"This user has Total Control access."` tampil di atas sub-tab
6. Verifikasi User Type pada Detail U1 bernilai `Total Control`
### TC-AC-SU-592: Assign Read Only
7. Klik menu Settings > Role & Permission di sidebar, klik Tab Read Only, lalu assign U2 (`Budi Santoso {runId}-172B`) ke Read Only
8. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U2 lewat Search nama, lalu klik Tab Role
9. Verifikasi banner `"This user has Read Only access."`
10. Klik menu Settings > User di sidebar, lalu ketik Search `Budi Santoso {runId}-172B`, tekan Enter
11. Verifikasi kolom Role baris U2 menampilkan badge `Read Only`
### TC-AC-SU-593: Remove Total Control
12. Klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu remove U3 (`Rina Putri {runId}-172C`) dari Total Control
13. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U3 lewat Search nama, lalu klik Tab Role
14. Verifikasi sedikitnya satu switch Global Role tampil
15. Verifikasi banner Total Control tidak tampil
16. Verifikasi seluruh switch Global Role OFF
17. Verifikasi sedikitnya satu baris Group Role tampil
18. Verifikasi seluruh Group Role tanpa group dan kolom Group bernilai `—`
19. Klik menu Settings > User di sidebar, lalu ketik Search `Rina Putri {runId}-172C`, tekan Enter
20. Verifikasi kolom Role baris U3 bernilai `0 roles`
### TC-AC-SU-594: Assign Group Manager
21. Klik menu Settings > Role & Permission di sidebar, klik Tab Group Manager, lalu assign Group Manager Region A dan Region B ke U4 (`Dedi Kurnia {runId}-172D`)
22. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U4 lewat Search nama, lalu klik Tab Role
23. Verifikasi banner `"This user is a Group Manager for: Region A, Region B."`
24. Verifikasi sedikitnya satu baris Group Role tampil
25. Verifikasi seluruh Group Role aktif dengan assignment Region A dan Region B full CRUD
26. Verifikasi User Type pada Detail U4 bernilai `Group Manager`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar dan pemilihan tab, serta Search nama target dan pembukaan Detail (langkah 2 dan langkah serupa, R-16).
- Anchor tambahan untuk asersi absence dan keadaan (S-03): banner Total Control tidak tampil (langkah 15) dan seluruh switch Global Role OFF (langkah 16) didahului Verifikasi sedikitnya satu switch Global Role tampil (langkah 14); seluruh Group Role tanpa group (langkah 18) didahului Verifikasi sedikitnya satu baris Group Role tampil (langkah 17).
- Empat blok TC dengan aktor sama dan permukaan yang sama (banner, badge, User Type); user seeding sendiri per blok.
- Temuan untuk QA:
  - TC-591 butir c menyebut `Detail User Type` tanpa menyebut lokasi field pada Detail; spec mengasersi User Type pada Detail U1 tanpa menyebut posisi.
  - TC-593 butir b menyebut "kolom Group `—`" tanpa menyebut surface; spec mengasersi pada sub-tab Group Role.
  - TC memakai nama literal (`Mike Tan`, `Budi Santoso`, `Rina Putri`, `Dedi Kurnia`); spec memakai nama bersuffix (S-12).
