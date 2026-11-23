---
id: TC-FA-SU-E2E-458-tab-transaction-admin-log-assignment-screening-filter-panel-dan-filter-group-name
title: "Tab Transaction Admin Log Sub-tab Assignment: Screening Filter Panel dan Filter Kolom Group dan Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1151
  - TC-FA-SU-1152
  - TC-FA-SU-1153
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Screening Filter Panel dan Filter Kolom Group dan Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

### TC-FA-SU-1151: Screening Filter Panel (field, label, placeholder, dan tombol)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Hover icon Filter
3. Verifikasi tooltip `Filter` tampil
4. Klik icon Filter
5. Verifikasi panel terbuka di bawah Table Tools
6. Verifikasi icon Filter menjadi gelap
7. Verifikasi field berurutan `Date`, `Activity`, `Name`, `Assignee`, `Group`
8. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
9. Verifikasi field `Activity` berupa multi-select searchable dengan placeholder `All activities`
10. Verifikasi field `Name` berupa multi-select searchable dengan placeholder `All assets`
11. Verifikasi field `Assignee` berupa multi-select searchable dengan placeholder `All assignees`
12. Verifikasi field `Group` berupa multi-select searchable dengan placeholder `All groups`
13. Verifikasi field `Role` dan `Transaction Status` tidak ada
14. Verifikasi `Transaction ID` tidak memiliki field filter
15. Verifikasi footer panel menampilkan `[Clear Field]` di kiri dan `[Apply]` di kanan
16. Verifikasi icon Filter tanpa badge titik selama belum ada filter ter-Apply
17. Klik icon Filter untuk menutup panel

### TC-FA-SU-1152: Filter kelas fk, kolom Group

18. Klik icon Filter
19. Buka dropdown `Group`
20. Verifikasi opsi dropdown = DISTINCT data tabel: `Branch Surabaya`, `Finance & Accounting`, `IT Infrastructure`, `Logistics Warehouse`
21. Centang `Branch Surabaya`
22. Klik `[Apply]`
23. Verifikasi tabel menyisakan `ASG-20260720-0071` (1 baris)
24. Verifikasi chip `Branch Surabaya` tampil di dalam field `Group`
25. Verifikasi panel Filter tetap terbuka setelah `[Apply]` (tidak menutup otomatis)
26. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
27. Klik icon Filter untuk menutup panel
28. Verifikasi panel Filter tertutup

### TC-FA-SU-1153: Filter kelas fk, kolom Name

29. Klik icon Filter
30. Buka dropdown `Name`
31. Verifikasi field `Name` (placeholder `All assets`) berupa multi-select searchable dengan opsi = DISTINCT nilai kolom Name pada tabel: `Camera Sony A7 - 3`, `Laptop Dell Latitude - 8`, `Monitor LG 24 - 4`, `Printer HP LaserJet - 2`
32. Ketik `Monitor` di kotak cari dropdown
33. Verifikasi opsi dropdown menyempit menjadi `Monitor LG 24 - 4`
34. Centang `Monitor LG 24 - 4`
35. Klik `[Apply]`
36. Verifikasi tabel menyisakan `ASG-20260719-0070` (1 baris)
37. Verifikasi chip `Monitor LG 24 - 4` tampil di dalam field `Name`
38. Verifikasi panel Filter tetap terbuka setelah `[Apply]` (tidak menutup otomatis)
39. Klik `[Clear Field]` pada field `Name`, lalu klik `[Apply]`
40. Klik icon Filter untuk menutup panel
41. Verifikasi panel Filter tertutup

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan, penutupan, dan `[Clear Field]` pada panel Filter; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: Filter kolom Assignee (TC-FA-SU-1141) ada di spec 444; Filter kolom Activity (TC-FA-SU-1154) ada di spec 449; Filter kolom Date, kombinasi Search dan Filter, dan pelepasan kontrol ada di spec 459; perilaku Filter Panel dan chip dropdown ada di spec 460.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1151 butir a menyebut "tooltip hover `Filter`" tanpa menyebut kapan; spec menaruhnya sebelum klik karena tooltip dibaca saat hover. (2) TC-FA-SU-1152 dan 1153 butir b / c menyebut panel Filter tertutup setelah icon Filter diklik; spec melepas filter dengan `[Clear Field]` dan `[Apply]` sebelum menutup panel supaya blok berikutnya mulai tanpa filter. (3) TC-FA-SU-1153 hanya menyebut Search `Monitor` di dalam dropdown; asersi opsi menyempit mengikuti butir a.
- Spec ini berjumlah 41 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
