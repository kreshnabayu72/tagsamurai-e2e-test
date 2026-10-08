---
id: TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom
title: "Pengurutan 3-State Tabel Utama Tab TC & RO: Siklus A-Z / Z-A / Default pada 8 Kolom Data dan Penanganan Default User di Akhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-152
  - TC-GS-ROLE-153
  - TC-GS-ROLE-154
  - TC-GS-ROLE-155
  - TC-GS-ROLE-156
coverage:
  web: automated
---

# Pengurutan 3-State Tabel Utama Tab TC & RO: Siklus A-Z / Z-A / Default pada 8 Kolom Data dan Penanganan Default User di Akhir

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup data tabel utama
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda

## Test Steps

### Sort kolom teks Name, Position, Division, Modified By (TC-GS-ROLE-152)

1. Tab Total Control: untuk tiap kolom pada Data Uji klik header 3 kali, amati tiap klik
2. Ulangi langkah 1 di Tab Read Only
3. Verifikasi Name: klik 1 A-Z, klik 2 Z-A, klik 3 kembali default Name A-Z
4. Verifikasi Position: A-Z / Z-A / default; baris Default User (—) selalu di akhir pada klik 1 (ascending) maupun klik 2 (descending)
5. Verifikasi Division: idem Position
6. Verifikasi Modified By: urut nama lengkap; — selalu di akhir untuk kedua arah
7. Verifikasi Tab Read Only: siklus Name, Position, Division, Modified By sama dengan a–d (Rina Putri dan Siti Nurhaliza bertukar posisi sesuai arah sort)

### Sort kolom Status (Active First / Inactive First) (TC-GS-ROLE-153)

8. Tab Total Control: klik header Status 3 kali
9. Tab Read Only: klik header Status 3 kali
10. Verifikasi Klik 1: Active dulu (Ahmad Fauzi dan Budi Santoso Default User, Status "Active"), lalu Inactive (Dewi Lestari)
11. Verifikasi Klik 2: Inactive dulu lalu Active
12. Verifikasi Klik 3: default Name A-Z
13. Verifikasi Tab Read Only: klik 1 Siti Nurhaliza (Active) sebelum Rina Putri (Inactive); klik 2 sebaliknya; klik 3 default Name A-Z

### Sort kolom Temporary User (Yes First / No First) (TC-GS-ROLE-154)

14. Tampilkan kolom Temporary User
15. Klik header 3 kali
16. Verifikasi Klik 1: Yes First
17. Verifikasi Klik 2: No First
18. Verifikasi Klik 3: default

### Sort kolom tanggal Last Updated dan Temporary Until (TC-GS-ROLE-155)

19. Tab Total Control: klik header Last Updated 3 kali
20. Tampilkan Temporary Until, klik header 3 kali
21. Tab Read Only: klik header Last Updated 3 kali
22. Verifikasi Last Updated: klik 1 Oldest First, klik 2 Newest First, klik 3 default; — (Default User) selalu di akhir untuk kedua arah
23. Verifikasi Temporary Until: klik 1 Oldest First, klik 2 Newest First, klik 3 default; kosong selalu di akhir untuk kedua arah
24. Verifikasi Tab Read Only Last Updated: klik 1 Rina Putri (3 Jun) sebelum Siti Nurhaliza (12 Jun); klik 2 sebaliknya; klik 3 default

### Sort kolom Activation Status dan TAG (TC-GS-ROLE-156)

25. Tampilkan Activation Status dan TAG
26. Klik header Activation Status 3 kali
27. Klik header TAG 3 kali
28. Verifikasi Activation Status: A-Z (Activated, Pending Activation, Pending Email Confirmation) / Z-A / default
29. Verifikasi TAG: A-Z by TAG code / Z-A / default; belum paired (—) selalu di akhir untuk kedua arah

## Notes

- Memvalidasi alur skenario "Pengurutan 3-State Tabel Utama Tab TC & RO: Siklus A-Z / Z-A / Default pada 8 Kolom Data dan Penanganan Default User di Akhir".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §4.1 Sort kolom boolean Yes/No.
- Sumber pemetaan test case granular: TC-GS-ROLE-152, TC-GS-ROLE-153, TC-GS-ROLE-154, TC-GS-ROLE-155, TC-GS-ROLE-156.
