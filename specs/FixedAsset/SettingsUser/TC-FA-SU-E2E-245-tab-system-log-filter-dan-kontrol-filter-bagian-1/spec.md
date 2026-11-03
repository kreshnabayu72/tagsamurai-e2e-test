---
id: TC-FA-SU-E2E-245-tab-system-log-filter-dan-kontrol-filter-bagian-1
title: "Tab System Log: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-744
  - TC-FA-SU-745
  - TC-FA-SU-746
  - TC-FA-SU-747
coverage:
  web: automated
---

# Tab System Log: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-744: Screening Filter Panel

1. Buka Detail pengguna Budi Santoso lalu klik tab System Log
2. Klik icon Filter
3. Verifikasi panel terbuka di bawah Table Tools
4. Verifikasi ikon Filter menjadi gelap
5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Verifikasi field ke-1 adalah Date (date range picker) dengan placeholder `Select date`
8. Verifikasi field ke-2 adalah Action (multi-select searchable) dengan placeholder `All actions`
9. Verifikasi field ke-3 adalah Object (multi-select searchable) dengan placeholder `All objects`
10. Verifikasi field ke-4 adalah Name (multi-select searchable) dengan placeholder `All users`
11. Verifikasi field ke-5 adalah Field (multi-select searchable) dengan placeholder `All fields`
12. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
13. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply

### TC-FA-SU-745: Filter kelas date (Date)

14. Pilih rentang 10/06/26 sampai 15/06/26 pada Date
15. Klik `[Apply]`
16. Verifikasi rentang inklusif 10/06/26 sampai 15/06/26 menyisakan S-6, S-7 (2 baris)

### TC-FA-SU-746: Filter kelas enum (Action, Object, Field)

17. Klik `[Clear Field]` pada field Date, lalu klik `[Apply]`
18. Buka dropdown Action
19. Verifikasi opsi dropdown = DISTINCT data tabel (`Activate`, `Assign`, `Auto-Revert`, `Edit`, `Resend Activation Email`)
20. Centang `Activate`
21. Klik `[Apply]`
22. Verifikasi memilih `Activate` menyisakan S-7 (1 baris)
23. Verifikasi chip `Activate` tampil di dalam field Action
24. Klik `[Clear Field]` pada field Action, lalu klik `[Apply]`
25. Buka dropdown Object
26. Verifikasi opsi dropdown = DISTINCT data tabel (`Global Role`, `Group Manager`, `Group Role`, `Total Control`, `User`)
27. Centang `Global Role`
28. Klik `[Apply]`
29. Verifikasi memilih `Global Role` menyisakan S-6 (1 baris)
30. Verifikasi chip `Global Role` tampil di dalam field Object
31. Klik `[Clear Field]` pada field Object, lalu klik `[Apply]`
32. Buka dropdown Field
33. Verifikasi opsi dropdown = DISTINCT data tabel (`Access Level`, `Activation Email`, `Group Manager — IT Infrastructure`, `Manage accounting`, `Manage group — Finance & Accounting`, `Manage group — IT Infrastructure — Update`, `Status`)
34. Centang `Access Level`
35. Klik `[Apply]`
36. Verifikasi memilih `Access Level` menyisakan S-4 (1 baris)
37. Verifikasi chip `Access Level` tampil di dalam field Field

### TC-FA-SU-747: Filter kelas fk (Name)

38. Klik `[Clear Field]` pada field Field, lalu klik `[Apply]`
39. Buka dropdown Name
40. Verifikasi opsi dropdown = DISTINCT data tabel (`Eka Wulandari`, `Hana Kusuma`, `Lina Marlina`, `Oscar Pranata`)
41. Centang `Lina Marlina`
42. Klik `[Apply]`
43. Verifikasi memilih `Lina Marlina` menyisakan S-4 (1 baris)
44. Verifikasi chip `Lina Marlina` tampil di dalam field Name

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Jarak antar field Filter: setiap field diuji terpisah dengan `[Clear Field]` pada field sebelumnya sebagai langkah penghubung.
- Spec ini berjumlah 44 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) Tanggal baris seed System Log (Pre-setup #28) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE.
