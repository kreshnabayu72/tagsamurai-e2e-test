---
id: TC-FA-SU-E2E-185-tab-non-login-user-filter-dan-kontrol-filter-bagian-1
title: "Tab Non-Login User: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-551
  - TC-FA-SU-552
  - TC-FA-SU-553
  - TC-FA-SU-554
coverage:
  web: automated
---

# Tab Non-Login User: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Custom Field Shift (Pre-setup #31, `FaUserMain`): Gudang Cabang Bekasi `Morning`, Kendaraan Operasional B 1234 XY `Night`, Mesin Fotokopi Lt.3 `Morning`, Printer Lantai 5 `Night`, Ruang Meeting Anggrek `Morning`; kolom curated Shift muncul setelah ditampilkan lewat Setup Column.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-551: Screening Filter Panel

2. Hover icon Filter
3. Verifikasi tooltip `Filter`
4. Klik icon Filter
5. Verifikasi panel terbuka di bawah Table Tools
6. Verifikasi ikon Filter menjadi gelap
7. Verifikasi field berurutan: Position (multi-select searchable, placeholder `All positions`) | Division (multi-select searchable, placeholder `All divisions`) | Status (multi-select searchable, placeholder `All statuses`) | Last Update (date range picker, placeholder `Select date`) | Temporary User (multi-select searchable, placeholder `All options`) | Temporary Until (date range picker, placeholder `Select date`) | Shift (multi-select searchable, placeholder `All shifts`)
8. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
9. Verifikasi tanpa badge titik pada ikon Filter selama belum ada filter ter-Apply

### TC-FA-SU-552: Filter kelas fk (Position, Division)

10. Buka dropdown Division
11. Verifikasi opsi dropdown = DISTINCT data tabel (`Facility`, `General Affairs`, `Logistics`, `Logistics Warehouse`)
12. Buka dropdown Position
13. Verifikasi dropdown Position terbuka tanpa opsi data dan tanpa chip yang dapat dipilih
14. Buka dropdown Division
15. Centang `Facility`
16. Klik `[Apply]`
17. Verifikasi `Facility` menyisakan `Ruang Meeting Anggrek` (1 baris)
18. Verifikasi chip `Facility` tampil di dalam field Division

### TC-FA-SU-553: Filter kelas enum (Status, Temporary User)

19. Klik `[Clear Field]` pada field Division
20. Klik `[Apply]`
21. Buka dropdown Status
22. Verifikasi opsi dropdown = DISTINCT data tabel (`Active`, `Inactive`)
23. Centang `Active`
24. Klik `[Apply]`
25. Verifikasi `Active` menyisakan `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek` (4 baris)
26. Verifikasi chip `Active` tampil di dalam field Status
27. Klik `[Clear Field]` pada field Status
28. Klik `[Apply]`
29. Buka dropdown Temporary User
30. Verifikasi opsi dropdown = DISTINCT data tabel (`No`)
31. Centang `No`
32. Klik `[Apply]`
33. Verifikasi `No` menyisakan `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` (5 baris)
34. Verifikasi chip `No` tampil di dalam field Temporary User

### TC-FA-SU-554: Filter kelas date (Last Update, Temporary Until)

35. Klik `[Clear Field]` pada field Temporary User
36. Klik `[Apply]`
37. Pilih rentang 10/06/26 sampai 15/06/26 pada Last Update
38. Klik `[Apply]`
39. Verifikasi rentang inklusif 10/06/26 sampai 15/06/26 menyisakan `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek` (2 baris)
40. Klik `[Clear Field]` pada field Last Update
41. Klik `[Apply]`
42. Buka field Temporary Until
43. Verifikasi date range picker Temporary Until dengan placeholder `Select date`
44. Pilih rentang 01/01/26 sampai 31/12/26 pada Temporary Until
45. Klik `[Apply]`
46. Verifikasi tidak ada baris dengan nilai tanggal Temporary Until sehingga rentang tersebut tidak menyisakan baris

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13); `[Clear Field]` lalu `[Apply]` antar field supaya tiap field diuji terpisah (S-09).
- Langkah `Pilih rentang 01/01/26 sampai 31/12/26` dan `Klik [Apply]` pada TC-FA-SU-554 ditambahkan karena Expected b menyebut "rentang apa pun tidak menyisakan baris" sementara langkah TC hanya membuka field Temporary Until (S-03).
- Daftar field Filter Panel pada TC-FA-SU-551 diasersi sebagai satu `Verifikasi` karena daftar disebut utuh dalam satu butir Expected (S-01).
- Jumlah langkah: 46 tertulis, 46 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (46 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-552 menempatkan dropdown Position tanpa opsi sebelum dropdown Division yang berisi opsi; asersi "tanpa opsi" dibuktikan dengan dropdown Position terbuka dan chip; agar anchor positif mendahului asersi absence (bagian 8b butir 2), spec membuka dan memverifikasi opsi dropdown Division lebih dulu, baru membuka dropdown Position, lalu membuka Division lagi untuk memilih `Facility`.
  - TC-FA-SU-554 langkah 5 hanya membuka field Temporary Until tanpa memilih rentang; Expected b (rentang apa pun tidak menyisakan baris) membutuhkan rentang.
