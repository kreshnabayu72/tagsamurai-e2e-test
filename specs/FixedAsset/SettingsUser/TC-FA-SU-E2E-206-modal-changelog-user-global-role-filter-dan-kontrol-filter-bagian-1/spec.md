---
id: TC-FA-SU-E2E-206-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-1
title: "Modal Changelog User > Global Role: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-620
  - TC-FA-SU-621
  - TC-FA-SU-622
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-620: Filter kelas enum (Action, Field)

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Klik icon Filter
3. Buka dropdown Action
4. Verifikasi opsi dropdown = DISTINCT data tabel dan memuat sekurangnya nilai seed (`Assign`, `Assign (via Total Control)`, `Edit`, `Remove`, `Remove (via Total Control)`)
5. Centang `Assign`
6. Klik `[Apply]`
7. Verifikasi memilih `Assign` menyisakan G-5 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
8. Verifikasi chip `Assign` tampil di dalam field Action
9. Klik `[Clear Field]` pada field Action, lalu klik `[Apply]`
10. Buka dropdown Field
11. Verifikasi opsi dropdown = DISTINCT data tabel dan memuat sekurangnya nilai seed (`Access`, `Manage accounting`, `Manage asset master data — Delete`, `Manage global license`)
12. Centang `Access`
13. Klik `[Apply]`
14. Verifikasi memilih `Access` menyisakan G-2, G-3 (2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
15. Verifikasi chip `Access` tampil di dalam field Field

### TC-FA-SU-621: Filter kelas fk (Role Name, Modified By)

16. Klik `[Clear Field]` pada field Field, lalu klik `[Apply]`
17. Buka dropdown Role Name
18. Verifikasi opsi dropdown = DISTINCT data tabel dan memuat sekurangnya nilai seed (`Import Data`, `Manage accounting`, `Manage asset master data`, `Manage global license`)
19. Centang `Import Data`
20. Klik `[Apply]`
21. Verifikasi memilih `Import Data` menyisakan G-3 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
22. Verifikasi chip `Import Data` tampil di dalam field Role Name
23. Klik `[Clear Field]` pada field Role Name, lalu klik `[Apply]`
24. Buka dropdown Modified By
25. Verifikasi opsi dropdown = DISTINCT data tabel dan memuat sekurangnya nilai seed (`Ahmad D`, `Lina M`)
26. Centang `Ahmad D`
27. Klik `[Apply]`
28. Verifikasi memilih `Ahmad D` menyisakan G-2, G-3, G-4, G-5 (4 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
29. Verifikasi chip `Ahmad D` tampil di dalam field Modified By

### TC-FA-SU-622: Kombinasi Search dan Filter dua arah

30. Klik `[Clear Field]` pada field Modified By, lalu klik `[Apply]`
31. Ketik Search `Assign`, tekan Enter
32. Klik icon Filter
33. Buka dropdown Action, centang `Assign`
34. Klik `[Apply]`
35. Verifikasi Search `Assign` lalu Filter Action `Assign`: hasil irisan G-5 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
36. Verifikasi keyword Search `Assign` tidak dikosongkan oleh Filter
37. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
38. Buka dropdown Action, centang `Assign`
39. Klik `[Apply]`
40. Ketik Search `Assign`, tekan Enter
41. Verifikasi Filter Action `Assign` lalu Search `Assign`: hasil identik, hasil irisan G-5 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
42. Verifikasi Filter Action `Assign` tidak direset oleh Search
43. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber. Opsi dropdown Filter ditulis `= DISTINCT data tabel dan memuat sekurangnya nilai seed`.
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14).
