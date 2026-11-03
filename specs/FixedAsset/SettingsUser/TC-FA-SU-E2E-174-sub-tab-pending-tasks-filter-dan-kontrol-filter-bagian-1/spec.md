---
id: TC-FA-SU-E2E-174-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-1
title: "Sub-tab Pending Tasks: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-517
  - TC-FA-SU-518
  - TC-FA-SU-519
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.

## Test Steps

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks
2. Klik icon Filter

### TC-FA-SU-517: Filter kelas fk (Group, PIC)

3. Buka dropdown Group
4. Verifikasi opsi dropdown = DISTINCT data tabel (`Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`)
5. Centang `Branch Surabaya`
6. Klik `[Apply]`
7. Verifikasi `Branch Surabaya` menyisakan `ASG-20260718-0067` (1 baris)
8. Verifikasi chip `Branch Surabaya` tampil di dalam field Group
9. Klik `[Clear Field]` pada field Group
10. Klik `[Apply]`
11. Buka dropdown PIC
12. Verifikasi opsi dropdown = DISTINCT data tabel (`Ahmad D`, `Budi S`, `Citra L`, `Eka W`)
13. Centang `Ahmad D`
14. Klik `[Apply]`
15. Verifikasi `Ahmad D` menyisakan `BRW-20260712-0346` (1 baris)
16. Verifikasi chip `Ahmad D` tampil di dalam field PIC

### TC-FA-SU-518: Filter kelas num (Total Asset)

17. Klik `[Clear Field]` pada field PIC
18. Klik `[Apply]`
19. Verifikasi placeholder `Min` dan `Max` pada field Total Asset
20. Isi Total Asset Min `1` dan Max `1`
21. Klik `[Apply]`
22. Verifikasi rentang inklusif 1 sampai 1 menyisakan `BRW-20260713-0355`, `ASG-20260715-0045`, `ASG-20260718-0067` (3 baris)

### TC-FA-SU-519: Filter kelas date (Request Date, Last Updated)

23. Klik `[Clear Field]` pada field Total Asset
24. Klik `[Apply]`
25. Pilih rentang 12/07/26 sampai 13/07/26 pada Request Date
26. Klik `[Apply]`
27. Verifikasi rentang inklusif 12/07/26 sampai 13/07/26 menyisakan `BRW-20260712-0346`, `BRW-20260713-0355` (2 baris)
28. Klik `[Clear Field]` pada field Request Date
29. Klik `[Apply]`
30. Pilih rentang 12/07/26 sampai 14/07/26 pada Last Updated
31. Klik `[Apply]`
32. Verifikasi rentang inklusif 12/07/26 sampai 14/07/26 menyisakan `BRW-20260712-0346`, `BRW-20260713-0355` (2 baris)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso dan Filter Panel; `[Clear Field]` lalu `[Apply]` antar field supaya tiap field diuji terpisah (S-09, sesuai langkah TC).
- Jumlah langkah: 32 tertulis, 32 dengan ekspansi iterasi.
- Temuan untuk QA:
  - Klik `[Clear Field]` pada TC-FA-SU-517 sampai 519 tidak menyebut apakah panel tetap terbuka sesudah `[Apply]`; spec mengikuti TC (field berikutnya langsung dibuka).
