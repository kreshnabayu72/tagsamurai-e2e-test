---
id: TC-AC-RP-E2E-073-tab-total-control-sort-kolom-dasar
title: "Sort Tab Total Control: Name, Position, Division, Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-244
  - TC-AC-RP-245
  - TC-AC-RP-246
  - TC-AC-RP-247
coverage:
  web: automated
---

# Sort Tab Total Control: Name, Position, Division, Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.

## Test Steps

### TC-AC-RP-244: Sort Tab Total Control kolom Name

1. Klik header kolom Name sekali
2. Verifikasi urutan Name A-Z
3. Klik header Name kedua kali
4. Verifikasi urutan Name Z-A
5. Klik header Name ketiga kali
6. Verifikasi urutan kembali ke bawaan Name A-Z

### TC-AC-RP-245: Sort Tab Total Control kolom Position

7. Klik header kolom Position sekali
8. Verifikasi urutan Position A-Z
9. Klik header Position kedua kali
10. Verifikasi urutan Position Z-A
11. Klik header Position ketiga kali
12. Verifikasi urutan kembali ke bawaan Name A-Z

### TC-AC-RP-246: Sort Tab Total Control kolom Division

13. Klik header kolom Division sekali
14. Verifikasi urutan Division A-Z
15. Klik header Division kedua kali
16. Verifikasi urutan Division Z-A
17. Klik header Division ketiga kali
18. Verifikasi urutan kembali ke bawaan Name A-Z

### TC-AC-RP-247: Sort Tab Total Control kolom Status

19. Klik header kolom Status sekali
20. Verifikasi urutan Status A-Z (berdasarkan label badge)
21. Klik header Status kedua kali
22. Verifikasi urutan Status Z-A
23. Klik header Status ketiga kali
24. Verifikasi urutan kembali ke bawaan Name A-Z

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Siklus sort tiga klik per kolom (A-Z, Z-A, netral) mengikuti Expected tiap TC; klik ketiga kembali ke urutan bawaan sehingga tiap TC berikutnya mulai dari keadaan netral (S-09).
- Tiap kolom yang diurutkan memiliki sedikitnya dua nilai distinct pada data Pre-setup (S-11).
- Temuan untuk QA: tidak ada.
