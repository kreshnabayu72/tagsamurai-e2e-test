---
id: TC-AC-RP-E2E-085-download-berkas-tab-total-control-dan-system
title: "Download isi berkas: Tab Total Control, Read Only, Group Manager, dan Tab System (CSV, XLSX)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-256
  - TC-AC-RP-257
  - TC-AC-RP-275
  - TC-AC-RP-424
coverage:
  web: automated
---

# Download isi berkas: Tab Total Control, Read Only, Group Manager, dan Tab System (CSV, XLSX)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Kemampuan teknis: membaca isi berkas yang terunduh (CSV dan XLSX: nilai sel, jumlah sheet, urutan kolom dan baris) dari folder unduhan browser (disediakan tim FE); tidak memakai intercept atau klien HTTP.
- Tab Group Manager memuat penugasan Pre-setup #14; Tab System memuat katalog Global Role dan Group Role (Pre-setup #15). Kolom berkas Tab System adalah kolom Setup Column bawaan (Role Type, Role Name, Users).

## Test Steps

### TC-AC-RP-256: Download Tab Total Control CSV dan XLSX

1. Klik ikon Download
2. Verifikasi popover memuat "Download as CSV" dan "Download as XLSX"
3. Klik "Download as CSV"
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas `Role-Permission-Total-Control.csv` terunduh
6. Verifikasi isi berkas CSV mengikuti kolom visible (Name, Position, Division, Status, Modified By, Last Updated) dengan seluruh baris Tab Total Control, tanpa Search atau Filter aktif
7. Verifikasi Modified By dan Last Updated `Bambang Hartono` ditulis `-` pada berkas CSV
8. Klik ikon Download
9. Klik "Download as XLSX"
10. Verifikasi tidak ada toast sukses
11. Verifikasi berkas `Role-Permission-Total-Control.xlsx` terunduh
12. Verifikasi isi berkas XLSX mengikuti kolom visible (Name, Position, Division, Status, Modified By, Last Updated) dengan seluruh baris Tab Total Control, tanpa Search atau Filter aktif
13. Verifikasi Modified By dan Last Updated `Bambang Hartono` ditulis `-` pada berkas XLSX

### TC-AC-RP-257: Download Tab Read Only dan Tab Group Manager memakai filename masing-masing

14. Klik tab `Read Only`
15. Klik ikon Download
16. Klik "Download as CSV"
17. Verifikasi berkas `Role-Permission-Read-Only.csv` terunduh
18. Klik tab `Group Manager`
19. Klik ikon Download
20. Klik "Download as CSV"
21. Verifikasi berkas `Role-Permission-Group-Manager.csv` terunduh
22. Verifikasi kolom Group pada berkas `Role-Permission-Group-Manager.csv` ditulis full path

### TC-AC-RP-275: Download Tab System sebagai XLSX berisi satu sheet dengan kolom Role Type

23. Klik tab `System`
24. Klik ikon Download
25. Klik "Download as XLSX"
26. Verifikasi tidak ada toast sukses
27. Verifikasi berkas `Role-Permission-System.xlsx` terunduh
28. Buka berkas hasil unduhan
29. Verifikasi berkas hanya berisi satu sheet
30. Verifikasi kolom berurutan `Role Type`, `Role Name`, `Users`
31. Verifikasi urutan baris sama dengan UI: seluruh baris `Global Role` (urutan katalog Global Role) lebih dulu, lalu seluruh baris `Group Role` (urutan katalog Group Role)
32. Verifikasi `Role Type` tiap baris sama dengan section asal role (`Global Role` atau `Group Role`)
33. Verifikasi `Role Name` dan `Users` tiap baris sama dengan tabel di UI
34. Verifikasi `Users` ditulis sebagai sel angka

### TC-AC-RP-424: Download Tab System sebagai CSV berisi satu tabel dengan kolom Role Type

35. Klik ikon Download
36. Klik "Download as CSV"
37. Verifikasi tidak ada toast sukses
38. Verifikasi berkas `Role-Permission-System.csv` terunduh
39. Buka berkas hasil unduhan
40. Verifikasi berkas berisi satu tabel tunggal (tanpa pemisahan per section)
41. Verifikasi kolom berurutan `Role Type`, `Role Name`, `Users`
42. Verifikasi urutan baris sama dengan UI: seluruh baris `Global Role` (urutan katalog Global Role) lebih dulu, lalu seluruh baris `Group Role` (urutan katalog Group Role)
43. Verifikasi `Role Type` tiap baris sama dengan section asal role (`Global Role` atau `Group Role`)
44. Verifikasi `Role Name` dan `Users` tiap baris sama dengan tabel di UI
45. Verifikasi `Users` ditulis sebagai nilai numerik

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec ini di atas smell 35 langkah (45 langkah): empat TC sumber memverifikasi isi berkas unduhan (CSV dan XLSX, kolom, nama berkas) dengan langkah unduh dan baca berkas yang berulang per format dan per tab; dipertahankan satu spec agar pembacaan berkas memakai kemampuan baca berkas yang sama, keputusan pemecahan diserahkan ke tinjauan QA.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Spec kelas f (isi berkas unduhan). Nama berkas dan toast diasersi sebagai asersi fungsional.
- Asersi absence toast sukses diletakkan segera setelah pemicu pilihan format, sebelum Verifikasi berkas terunduh yang menjadi anchor positifnya (bagian 8b butir 11).
- Ukuran spec (45 langkah, melewati sekitar 35): seluruh blok satu kelas harness (isi berkas unduhan, kelas f), satu akun, tanpa aksi tulis, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena tiap klausa Expected menjadi satu Verifikasi (S-01).
- Temuan untuk QA:
  - TC-AC-RP-256 Expected b menyebut isi berkas "mengikuti kolom visible dan Search/Filter aktif" tanpa langkah mengaktifkan Search atau Filter sebelum Download; spec mengasersi kolom visible bawaan dengan seluruh baris dan klausa Search/Filter aktif tidak teruji.
  - TC-AC-RP-257 menyebut kolom Group pada berkas Tab Group Manager "ditulis full path" tanpa contoh nilai; penugasan GM Pre-setup #14 hanya pada group tingkat atas (`Region Jawa`, `Sumatera`), sehingga nilai full path berbeda dari nama group belum dapat dipastikan; Verifikasi tidak menyebut nilai.
  - TC-AC-RP-275 dan 424 menyebut "sama dengan tabel di UI" untuk seluruh baris tanpa daftar nilai; pembandingan dilakukan antara berkas dan tabel di UI saat run.
