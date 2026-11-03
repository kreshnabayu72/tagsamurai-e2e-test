---
id: TC-FA-SU-E2E-184-tab-non-login-user-sort
title: "Tab Non-Login User: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-547
  - TC-FA-SU-548
  - TC-FA-SU-549
  - TC-FA-SU-550
  - TC-FA-SU-1034
coverage:
  web: automated
---

# Tab Non-Login User: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Custom Field Shift (Pre-setup #31, `FaUserMain`): Gudang Cabang Bekasi `Morning`, Kendaraan Operasional B 1234 XY `Night`, Mesin Fotokopi Lt.3 `Morning`, Printer Lantai 5 `Night`, Ruang Meeting Anggrek `Morning`; kolom curated Shift muncul setelah ditampilkan lewat Setup Column.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Kolom curated Temporary User, Temporary Until, dan Shift ditampilkan satu kali lewat Setup Column sebelum TC-FA-SU-549 (menggabungkan langkah penampil kolom TC-FA-SU-549, 550, dan 1034).

## Test Steps

1. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-547: Sort kelas toggle-b (Active)

2. Klik header Active satu kali
3. Verifikasi urutan ascending (↑): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek`, `Printer Lantai 5`
4. Klik header Active kedua kali
5. Verifikasi urutan descending (↓): `Printer Lantai 5`, `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek`
6. Klik header Active ketiga kali
7. Verifikasi urutan netral kembali ke default: `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`

### TC-FA-SU-548: Sort kelas date (Last Update)

8. Klik header Last Update satu kali
9. Verifikasi urutan ascending (↑): `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek`, `Kendaraan Operasional B 1234 XY`, `Printer Lantai 5`, `Gudang Cabang Bekasi`
10. Klik header Last Update kedua kali
11. Verifikasi urutan descending (↓): `Gudang Cabang Bekasi`, `Printer Lantai 5`, `Kendaraan Operasional B 1234 XY`, `Ruang Meeting Anggrek`, `Mesin Fotokopi Lt.3`
12. Klik header Last Update ketiga kali
13. Verifikasi urutan netral kembali ke default: `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`

### TC-FA-SU-549: Sort kelas yesno (Temporary User)

14. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
15. Centang kolom Temporary User, Temporary Until, dan Shift pada daftar Setup Column
16. Klik `[Save]`
17. Klik header Temporary User satu kali
18. Verifikasi urutan ascending (↑): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`
19. Klik header Temporary User kedua kali
20. Verifikasi urutan descending (↓): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`
21. Klik header Temporary User ketiga kali
22. Verifikasi urutan netral kembali ke default: `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`

### TC-FA-SU-550: Sort kelas date-e (Temporary Until)

23. Klik header Temporary Until satu kali
24. Verifikasi urutan ascending (↑): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`
25. Klik header Temporary Until kedua kali
26. Verifikasi urutan descending (↓): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`
27. Klik header Temporary Until ketiga kali
28. Verifikasi urutan netral kembali ke default: `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`

### TC-FA-SU-1034: Sort kelas cf (Shift)

29. Klik header Shift satu kali
30. Verifikasi urutan ascending (↑): tiga baris `Morning` (`Gudang Cabang Bekasi`, `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek`) di atas dua baris `Night` (`Kendaraan Operasional B 1234 XY`, `Printer Lantai 5`)
31. Klik header Shift kedua kali
32. Verifikasi urutan descending (↓): dua baris `Night` di atas tiga baris `Morning`
33. Verifikasi urutan antar baris dengan Shift sama mengikuti default sort tabel
34. Klik header Shift ketiga kali
35. Verifikasi urutan netral kembali ke default: `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; satu kali menampilkan kolom curated lewat Setup Column.
- Jumlah langkah: 35 tertulis, 35 dengan ekspansi iterasi.
- Temuan untuk QA:
  - TC-FA-SU-549 dan TC-FA-SU-550: Temporary User (seluruh `No`) dan Temporary Until (seluruh kosong) tidak memiliki dua nilai distinct, sehingga urutan asc, desc, dan netral identik; asersi tidak membuktikan fungsi sort kolom itu (S-11).
  - TC-FA-SU-1034 Expected: urutan antar baris dengan Shift sama "mengikuti default sort" ditulis satu kali pada klik 2; TC tidak menyebutnya per klik.
