---
id: TC-AC-RP-E2E-039-assign-group-manager-screening-tree-pool
title: "Assign Group Manager: Screening Popup, Tree Group, Pool Kandidat, dan Ganti Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-146
  - TC-AC-RP-147
  - TC-AC-RP-148
  - TC-AC-RP-149
coverage:
  web: automated
---

# Assign Group Manager: Screening Popup, Tree Group, Pool Kandidat, dan Ganti Group

## Prerequisites

- Mode: FE+BE (backend nyata; spec ini tidak menyimpan perubahan)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Spec ini tidak mengubah data Pre-setup; tidak ada state yang perlu dipulihkan.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-146: Screening popup Assign Group Manager

1. Klik tab `Group Manager`
2. Klik tombol "+ Assign"
3. Susuri popup dari atas ke bawah
4. Verifikasi header popup "Assign Group Manager"
5. Verifikasi field User berupa Table User Picker dengan Search (placeholder "Search..."), Filter, dan kolom Name, Email, Position, Division, Status
6. Verifikasi field Group berupa Tree Group single-select dengan placeholder "Select group"
7. Verifikasi footer memuat tombol `[Cancel]` dan `[Assign]`

### TC-AC-RP-147: Tree Group popup Assign GM menampilkan seluruh node termasuk yang ancestor-nya punya GM

8. Buka field Group
9. Expand seluruh node pada Tree Group
10. Verifikasi seluruh node (`Default Group`, `Region A`, `Branch 1`, `Region Jawa`, `Jakarta`, `Surabaya`, `Sumatera`) dapat dipilih
11. Verifikasi `Jakarta` dan `Surabaya` tidak disabled walau `Region Jawa` sudah punya GM
12. Pilih node `Region A`
13. Verifikasi node terpilih di-highlight tanpa checkbox

### TC-AC-RP-148: Pool Assign GM menerima status apa pun dan mengecualikan TC, RO, Default User, GM di group terpilih, dan aktor

14. Buka field Group lalu pilih node `Region Jawa`
15. Telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat
16. Verifikasi kandidat memuat user Standard berstatus apa pun (Active, Pending Activation, Pending Email Confirmation, dan Inactive `Teguh Santoso`)
17. Verifikasi kandidat tidak memuat `Fajar Nugroho` dan `Jane Smith` (sudah GM di `Region Jawa`)
18. Verifikasi kandidat tidak memuat pemegang Total Control, pemegang Read Only, Default User, maupun aktor

### TC-AC-RP-149: Mengubah field Group mengosongkan pilihan User dan me-refetch kandidat

19. Buka field Group lalu pilih node `Region A`
20. Ketik Search `John Dohan`, tekan Enter
21. Centang `John Dohan`
22. Buka field Group lalu pilih node `Region Jawa`
23. Verifikasi centangan `John Dohan` hilang
24. Verifikasi daftar kandidat diambil ulang sesuai `Region Jawa` dan memuat `John Dohan`
25. Verifikasi daftar kandidat tidak memuat `Fajar Nugroho` dan `Jane Smith`
26. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 15, 26 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 20.
- Popup yang dibuka di langkah 2 dipakai bersama TC-AC-RP-146 sampai 149 (jumlah buka tidak melebihi jumlah tutup, prinsip 6) dan ditutup di langkah 26.
- Temuan untuk QA:
  - Picker memuat lebih dari 10 kandidat (Pagination default 10) dan TC tidak menyatakan cara menelusuri halaman; spec menelusuri seluruh halaman Pagination untuk asersi daftar kandidat dan memakai Search untuk menemukan baris target (S-14, S-15).
  - TC-AC-RP-149 Expected menulis "Fajar Nugroho dan Jane Smith yang Inactive" sehingga kata "Inactive" ambigu (melekat ke Jane Smith saja atau keduanya); spec mengasersi keduanya tidak muncul karena alasan yang sama (sudah GM di `Region Jawa`).
  - TC-AC-RP-149 tidak menyatakan apakah isi Search bertahan setelah Group diganti; spec mengikuti Expected tanpa mengasumsikan kotak Search kosong atau terisi.
