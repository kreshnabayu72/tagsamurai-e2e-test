---
id: TC-FA-SU-E2E-197-tab-changelog-filter-dan-kontrol-filter-bagian-1
title: "Tab Changelog: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-587
  - TC-FA-SU-588
  - TC-FA-SU-589
  - TC-FA-SU-590
coverage:
  web: automated
---

# Tab Changelog: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Date, Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Date `18/08/26, 13:10`, Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Date `12/08/26, 11:41`, Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Date `12/08/26, 11:40`, Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Date `02/08/26, 10:05`, Field `Home Group`, Modified By `Lina M`
  - T-5: Date `20/07/26, 14:30`, Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Date `15/07/26, 09:15`, Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Date `10/06/26, 08:02`, Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-587: Filter kelas date (Date)

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
3. Klik icon Filter
4. Pilih rentang 10/06/26 sampai 15/07/26 pada Date
5. Klik `[Apply]`
6. Verifikasi rentang inklusif 10/06/26 sampai 15/07/26 menyisakan `Manage accounting`, `Status` (T-6, T-7; 2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
7. Verifikasi sel Date baris T-6 menampilkan `15/07/26, 09:15`
8. Verifikasi sel Date baris T-7 menampilkan `10/06/26, 08:02`

### TC-FA-SU-588: Filter kelas enum (Action, Field)

9. Klik `[Clear Field]` pada field Date, lalu klik `[Apply]`
10. Buka dropdown Action
11. Verifikasi opsi dropdown = DISTINCT data tabel (`Activate`, `Assign`, `Edit`, `Edit Home Group`)
12. Centang `Activate`
13. Klik `[Apply]`
14. Verifikasi memilih `Activate` menyisakan `Status` (T-7; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
15. Verifikasi chip `Activate` tampil di dalam field Action
16. Klik `[Clear Field]` pada field Action, lalu klik `[Apply]`
17. Buka dropdown Field
18. Verifikasi opsi dropdown = DISTINCT data tabel (`Home Group`, `Manage accounting`, `Manage asset master data — Delete`, `Manage files — IT Infrastructure`, `Manage group — IT Infrastructure — Delete`, `Manage group — IT Infrastructure — Update`, `Status`)
19. Centang `Manage files — IT Infrastructure`
20. Klik `[Apply]`
21. Verifikasi memilih `Manage files — IT Infrastructure` menyisakan `Manage files — IT Infrastructure` (T-1; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
22. Verifikasi chip `Manage files — IT Infrastructure` tampil di dalam field Field

### TC-FA-SU-589: Filter kelas fk (Modified By)

23. Klik `[Clear Field]` pada field Field, lalu klik `[Apply]`
24. Buka dropdown Modified By
25. Verifikasi opsi dropdown = DISTINCT data tabel (`Ahmad D`, `Lina M`)
26. Centang `Ahmad D`
27. Klik `[Apply]`
28. Verifikasi memilih `Ahmad D` menyisakan T-1, T-2, T-3, T-5, T-6, T-7 (6 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
29. Verifikasi chip `Ahmad D` tampil di dalam field Modified By

### TC-FA-SU-590: Kombinasi Search dan Filter dua arah

30. Klik `[Clear Field]` pada field Modified By, lalu klik `[Apply]`
31. Ketik Search `Home`, tekan Enter
32. Klik icon Filter
33. Buka dropdown Action, centang `Activate`
34. Klik `[Apply]`
35. Verifikasi Search `Home` lalu Filter Action `Activate`: tidak ada baris (0 baris), empty state `No results found` tampil
36. Verifikasi keyword Search `Home` tidak dikosongkan oleh Filter
37. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
38. Buka dropdown Action, centang `Activate`
39. Klik `[Apply]`
40. Ketik Search `Home`, tekan Enter
41. Verifikasi Filter Action `Activate` lalu Search `Home`: hasil identik, tidak ada baris (0 baris), empty state `No results found` tampil
42. Verifikasi Filter Action `Activate` tidak direset oleh Search
43. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- Asersi tambahan di luar Expected (S-03): langkah 7 dan 8 (sel Date baris T-6 dan T-7 berada di dalam rentang Filter Date), supaya nilai Date yang disaring tampil; nilai Date seed mengikuti Example Data PRD dan dicatat di alias baris Prerequisites.
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris, sebagai anchor positif absence (bagian 8b butir 2); alasannya sama dengan temuan QA butir terakhir.
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) TC menulis hasil 0 baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2), mengacu pada Expected TC-FA-SU-580 butir a.
