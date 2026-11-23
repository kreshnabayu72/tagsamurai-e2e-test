---
id: TC-FA-SU-E2E-444-tab-transaction-admin-log-assignment-search-filter-dan-sort-assignee
title: "Tab Transaction Admin Log Sub-tab Assignment: Search, Filter, dan Sort Assignee"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1140
  - TC-FA-SU-1141
  - TC-FA-SU-1142
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Search, Filter, dan Sort Assignee

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup, hanya dibaca dan tidak diubah (S-06): Client `FaUserMain` (#20) dan Transaction Admin Log Budi Santoso (#29), sub-tab Assignment 4 baris (satu halaman, ukuran halaman 10): `ASG-20260720-0071` (`20/07/26`, `Handed over`, `Laptop Dell Latitude - 8`, Assignee `Rina W`, Group `Branch Surabaya`), `ASG-20260719-0070` (`19/07/26`, `Approved`, `Monitor LG 24 - 4`, Assignee Division `General Affairs`, Group `IT Infrastructure`), `ASG-20260717-0069` (`17/07/26`, `Requested`, `Camera Sony A7 - 3`, Assignee `Andi P`, Group `Logistics Warehouse`), dan `ASG-20260715-0068` (`15/07/26`, `Rejected`, `Printer HP LaserJet - 2`, Assignee `Dewi L`, Group `Finance & Accounting`). Nama pengguna dan Division dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec hanya membaca, memfilter, dan mengurutkan sub-tab; tidak ada aksi tulis ke data Pre-setup.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, klik Name Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Verifikasi tabel memuat sedikitnya empat baris data uji (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`)

### TC-FA-SU-1140: Search kelas teks, kolom Transaction ID, Name, dan Assignee

3. Klik icon Search
4. Ketik Search `0071`, tekan Enter
5. Verifikasi tabel menyisakan `ASG-20260720-0071` (1 baris)
6. Kosongkan isi kotak search, tekan Enter
7. Ketik Search `Monitor`, tekan Enter
8. Verifikasi tabel menyisakan `ASG-20260719-0070` (1 baris, `Monitor LG 24 - 4`)
9. Kosongkan isi kotak search, tekan Enter
10. Ketik Search `Andi`, tekan Enter
11. Verifikasi tabel menyisakan `ASG-20260717-0069` (1 baris, Assignee `Andi P`)
12. Kosongkan isi kotak search, tekan Enter
13. Ketik Search `General Affairs`, tekan Enter
14. Verifikasi tabel menyisakan `ASG-20260719-0070` (1 baris, Assignee `General Affairs`)
15. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1141: Filter kelas fk, Assignee termasuk Assignee Division

16. Klik icon Filter
17. Buka dropdown Assignee
18. Verifikasi field `Assignee` (placeholder `All assignees`) berupa multi-select searchable
19. Verifikasi opsi dropdown = DISTINCT nilai kolom Assignee pada tabel: `Andi P`, `Dewi L`, `General Affairs`, `Rina W` (nama pengguna dan nama Division)
20. Centang `General Affairs` (Division)
21. Klik `[Apply]`
22. Verifikasi tabel menyisakan `ASG-20260719-0070` (1 baris)
23. Verifikasi chip `General Affairs` tampil di dalam field `Assignee`
24. Buka dropdown Assignee, lalu centang `Rina W` (pengguna)
25. Klik `[Apply]`
26. Verifikasi tabel menyisakan `ASG-20260720-0071` dan `ASG-20260719-0070` (2 baris, logika OR dalam field)
27. Verifikasi panel Filter tetap terbuka setelah `[Apply]`
28. Klik icon Filter untuk menutup panel
29. Verifikasi panel Filter tertutup
30. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
31. Klik icon Filter untuk menutup panel

### TC-FA-SU-1142: Sort kelas teks, Assignee

32. Klik header Assignee satu kali
33. Verifikasi urutan ascending: `ASG-20260717-0069` (`Andi P`), `ASG-20260715-0068` (`Dewi L`), `ASG-20260719-0070` (`General Affairs`), `ASG-20260720-0071` (`Rina W`)
34. Klik header Assignee kedua kali
35. Verifikasi urutan descending: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260715-0068`, `ASG-20260717-0069`
36. Klik header Assignee ketiga kali
37. Verifikasi urutan netral kembali ke default Date newest first: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna lewat Search di User List, R-16, lalu membuka tab dan sub-tab), langkah 3, 16, 17, 20, 21, 24, 25, dan 28 (membuka input Search, panel Filter, dropdown), pengosongan Search di langkah 6, 9, 12, dan 15 (S-09), serta langkah 30 dan 31 (membersihkan Filter sebelum blok sort, S-09). Langkah 2 adalah `Verifikasi` pembanding yang membuktikan tabel memuat data uji sebelum asersi "menyisakan" (8b.2) dan sebelum asersi sort (8b.15d).
- Alasan melewati sekitar 35 langkah (37 langkah): ketiga TC satu kelas (fungsional baca) pada satu pengguna dengan seed Pre-setup yang sama, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ukuran berasal dari satu `Verifikasi` per klausa Expected (S-01) dan empat anggota Search yang berurutan.
- Temuan untuk QA (S-15): TC-FA-SU-1140, 1141, dan 1142 memakai seed Assignment Budi Santoso dari Pre-setup #29 (`ASG-20260720-0071` sampai `ASG-20260715-0068`) tanpa menyatakan mekanisme seed; spec membaca seed itu apa adanya dan tidak mengarang endpoint. Post Condition tidak ada.
