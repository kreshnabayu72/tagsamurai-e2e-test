---
id: TC-FA-SU-E2E-235-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-1
title: "Modal Combined Changelog: User: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-714
  - TC-FA-SU-715
  - TC-FA-SU-716
  - TC-FA-SU-717
coverage:
  web: automated
---

# Modal Combined Changelog: User: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.

## Test Steps

### TC-FA-SU-714: Screening Filter Panel

1. Klik icon Changelog di Table Tools halaman User List
2. Klik icon Filter
3. Verifikasi panel terbuka di bawah Table Tools
4. Verifikasi ikon Filter menjadi gelap
5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Verifikasi field ke-1 adalah Date (date range picker) dengan placeholder `Select date`
8. Verifikasi field ke-2 adalah Action (multi-select searchable) dengan placeholder `All actions`
9. Verifikasi field ke-3 adalah User Name (multi-select searchable) dengan placeholder `All users`
10. Verifikasi field ke-4 adalah Field (multi-select searchable) dengan placeholder `All fields`
11. Verifikasi field ke-5 adalah Modified By (multi-select searchable) dengan placeholder `All users`
12. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
13. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply

### TC-FA-SU-715: Filter kelas date (Date)

14. Pilih rentang 10/06/26 sampai 15/06/26 pada Date
15. Klik `[Apply]`
16. Verifikasi rentang inklusif 10/06/26 sampai 15/06/26 menyisakan C-5, C-6 (2 baris)

### TC-FA-SU-716: Filter kelas enum (Action, Field)

17. Klik `[Clear Field]` pada field Date, lalu klik `[Apply]`
18. Buka dropdown Action
19. Verifikasi opsi dropdown = DISTINCT data tabel (`Activate`, `Assign`, `Deactivate`, `Edit`, `Edit Home Group`, `Resend Activation Email`)
20. Centang `Activate`
21. Klik `[Apply]`
22. Verifikasi memilih `Activate` menyisakan C-6 (1 baris)
23. Verifikasi chip `Activate` tampil di dalam field Action
24. Klik `[Clear Field]` pada field Action, lalu klik `[Apply]`
25. Buka dropdown Field
26. Verifikasi opsi dropdown = DISTINCT data tabel (`Activation Email`, `Home Group`, `Manage accounting`, `Manage group — Finance & Accounting — Update`, `Status`)
27. Centang `Activation Email`
28. Klik `[Apply]`
29. Verifikasi memilih `Activation Email` menyisakan C-1 (1 baris)
30. Verifikasi chip `Activation Email` tampil di dalam field Field

### TC-FA-SU-717: Filter kelas fk (User Name, Modified By)

31. Klik `[Clear Field]` pada field Field, lalu klik `[Apply]`
32. Buka dropdown User Name
33. Verifikasi opsi dropdown = DISTINCT data tabel (`Budi Santoso`, `Doni Prasetyo`, `Eka Wulandari`, `Gita Permata`, `Hana Kusuma`)
34. Centang `Budi Santoso`
35. Klik `[Apply]`
36. Verifikasi memilih `Budi Santoso` menyisakan C-3, C-5 (2 baris)
37. Verifikasi chip `Budi Santoso` tampil di dalam field User Name
38. Klik `[Clear Field]` pada field User Name, lalu klik `[Apply]`
39. Buka dropdown Modified By
40. Verifikasi opsi dropdown = DISTINCT data tabel (`Ahmad D`, `Budi S`, `Lina M`)
41. Centang `Ahmad D`
42. Klik `[Apply]`
43. Verifikasi memilih `Ahmad D` menyisakan C-1, C-4, C-5, C-6 (4 baris)
44. Verifikasi chip `Ahmad D` tampil di dalam field Modified By

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Jarak antar field Filter: setiap field diuji terpisah dengan `[Clear Field]` pada field sebelumnya sebagai langkah penghubung.
- Spec ini berjumlah 44 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE.
