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
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Field `Home Group`, Modified By `Lina M`
  - T-5: Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-587: Filter kelas date (Date)

1. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
2. Klik icon Filter
3. Pilih rentang 10/06/26 sampai 15/07/26 pada Date
4. Klik `[Apply]`
5. Verifikasi rentang inklusif 10/06/26 sampai 15/07/26 menyisakan `Manage accounting`, `Status` (T-6, T-7; 2 baris)

### TC-FA-SU-588: Filter kelas enum (Action, Field)

6. Klik `[Clear Field]` pada field Date, lalu klik `[Apply]`
7. Buka dropdown Action
8. Verifikasi opsi dropdown = DISTINCT data tabel (`Activate`, `Assign`, `Edit`, `Edit Home Group`)
9. Centang `Activate`
10. Klik `[Apply]`
11. Verifikasi memilih `Activate` menyisakan `Status` (T-7; 1 baris)
12. Verifikasi chip `Activate` tampil di dalam field Action
13. Klik `[Clear Field]` pada field Action, lalu klik `[Apply]`
14. Buka dropdown Field
15. Verifikasi opsi dropdown = DISTINCT data tabel (`Home Group`, `Manage accounting`, `Manage asset master data — Delete`, `Manage files — IT Infrastructure`, `Manage group — IT Infrastructure — Delete`, `Manage group — IT Infrastructure — Update`, `Status`)
16. Centang `Manage files — IT Infrastructure`
17. Klik `[Apply]`
18. Verifikasi memilih `Manage files — IT Infrastructure` menyisakan `Manage files — IT Infrastructure` (T-1; 1 baris)
19. Verifikasi chip `Manage files — IT Infrastructure` tampil di dalam field Field

### TC-FA-SU-589: Filter kelas fk (Modified By)

20. Klik `[Clear Field]` pada field Field, lalu klik `[Apply]`
21. Buka dropdown Modified By
22. Verifikasi opsi dropdown = DISTINCT data tabel (`Ahmad D`, `Lina M`)
23. Centang `Ahmad D`
24. Klik `[Apply]`
25. Verifikasi memilih `Ahmad D` menyisakan T-1, T-2, T-3, T-5, T-6, T-7 (6 baris)
26. Verifikasi chip `Ahmad D` tampil di dalam field Modified By

### TC-FA-SU-590: Kombinasi Search dan Filter dua arah

27. Ketik Search `Home`, tekan Enter
28. Klik icon Filter
29. Buka dropdown Action, centang `Activate`
30. Klik `[Apply]`
31. Verifikasi Search `Home` lalu Filter Action `Activate`: tidak ada baris (0 baris), empty state `No results found` tampil
32. Verifikasi keyword Search `Home` tidak dikosongkan oleh Filter
33. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
34. Buka dropdown Action, centang `Activate`
35. Klik `[Apply]`
36. Ketik Search `Home`, tekan Enter
37. Verifikasi Filter Action `Activate` lalu Search `Home`: hasil identik, tidak ada baris (0 baris), empty state `No results found` tampil
38. Verifikasi Filter Action `Activate` tidak direset oleh Search
39. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris, sebagai anchor positif absence (bagian 8b butir 2); alasannya sama dengan temuan QA butir terakhir.
- Spec ini berjumlah 39 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) TC menulis hasil 0 baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2), mengacu pada Expected TC-FA-SU-580 butir a.
