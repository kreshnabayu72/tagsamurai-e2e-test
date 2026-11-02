---
id: TC-AC-RP-E2E-071-tab-total-control-filter-dasar
title: "Filter Tab Total Control: Position, Division, Status, dan panel Filter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-236
  - TC-AC-RP-237
  - TC-AC-RP-238
  - TC-AC-RP-239
coverage:
  web: automated
---

# Filter Tab Total Control: Position, Division, Status, dan panel Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Custom field User aktif (Pre-setup #12): `Employee Grade` (Dropdown) dan `Nickname` (Text); tidak ada custom field bertipe lain.
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.

## Test Steps

### TC-AC-RP-236: Screening Filter Panel Tab Total Control

1. Klik ikon Filter
2. Verifikasi field default Filter Panel: Position ("All positions"), Division ("All divisions"), Status ("All statuses"), Modified By ("All users"), Last Updated (date range, "Select date")
3. Verifikasi field curated tersedia terlepas dari status show/hide kolomnya: Activation Status ("All statuses"), Temporary User ("All"), Temporary Until ("Select date"), serta field Custom Field sesuai tipe custom field yang aktif: `Employee Grade` (Dropdown) dan `Nickname` (Text)
4. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
5. Verifikasi Filter Panel kosong saat dibuka (tanpa nilai default)

### TC-AC-RP-237: Filter Tab Total Control berdasarkan Position

6. Buka dropdown Position
7. Verifikasi opsi dropdown Position berasal dari nilai unik kolom Position pada data tabel
8. Ketik `Man` pada kotak pencarian dropdown Position
9. Verifikasi opsi `Manager` tampil pada hasil pencarian dropdown Position (dropdown dapat dicari)
10. Pilih Position `Manager`
11. Klik `[Apply]`
12. Verifikasi baris `John Doe` tampil
13. Verifikasi tidak ada baris selain `John Doe`

### TC-AC-RP-238: Filter Tab Total Control berdasarkan Division

14. Klik `[Clear Field]`, lalu klik `[Apply]`
15. Buka dropdown Division
16. Verifikasi opsi dropdown Division berasal dari nilai unik kolom Division pada data tabel
17. Ketik `Fin` pada kotak pencarian dropdown Division
18. Verifikasi opsi `Finance` tampil pada hasil pencarian dropdown Division (dropdown dapat dicari)
19. Pilih Division `Finance`
20. Klik `[Apply]`
21. Verifikasi baris `John Doe` dan `Rina Wijaya` tampil
22. Verifikasi tidak ada baris selain `John Doe` dan `Rina Wijaya`

### TC-AC-RP-239: Filter Tab Total Control berdasarkan Status

23. Klik `[Clear Field]`, lalu klik `[Apply]`
24. Buka dropdown Status
25. Verifikasi opsi dropdown Status berasal dari nilai unik kolom Status pada data tabel
26. Ketik `Inac` pada kotak pencarian dropdown Status
27. Verifikasi opsi `Inactive` tampil pada hasil pencarian dropdown Status (dropdown dapat dicari)
28. Pilih Status `Inactive`
29. Klik `[Apply]`
30. Verifikasi baris `Sarah Kim` tampil
31. Verifikasi tidak ada baris selain `Sarah Kim`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 14 dan 23 (`[Clear Field]` lalu `[Apply]`) mengosongkan filter sebelum TC berikutnya (S-09); Filter Panel dibuka sekali di langkah 1 dan tidak dibuka ulang.
- Asersi tambahan (S-03): langkah 3 menyebut field Custom Field `Employee Grade` (Dropdown) dan `Nickname` (Text) sebagai tipe custom field yang aktif di Pre-setup #12; TC-AC-RP-236 Expected b hanya menyebut "field Custom Field sesuai tipe custom field yang aktif".
- Langkah mengetik pada kotak pencarian dropdown dan Verifikasi opsi tampil menjabarkan klausa "dapat dicari" pada Expected TC-AC-RP-237 sampai 239 (S-03).
- Temuan untuk QA:
  - TC-AC-RP-237 sampai 239 menyebut "opsi dropdown berasal dari nilai unik data tabel dan dapat dicari" tanpa cara mengamati; spec membuka dropdown dan mengetik sebagian nilai.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`; TC-AC-RP-242 memakai `[Clear Field]` tanpa membuka ulang panel, spec mengikuti pola itu.
