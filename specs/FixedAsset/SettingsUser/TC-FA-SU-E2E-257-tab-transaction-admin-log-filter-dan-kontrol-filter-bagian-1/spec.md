---
id: TC-FA-SU-E2E-257-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-1
title: "Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-776
  - TC-FA-SU-777
  - TC-FA-SU-778
coverage:
  web: automated
---

# Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps


### TC-FA-SU-776: Filter kelas fk, kolom Group

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment
2. Klik icon Filter
3. Buka dropdown `Group`
4. Verifikasi opsi dropdown = DISTINCT data tabel: `Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`
5. Centang `Branch Surabaya`
6. Klik `[Apply]`
7. Verifikasi tabel menyisakan `BRW-20260716-0314` (1 baris)
8. Verifikasi chip `Branch Surabaya` tampil di dalam field `Group`
9. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`

### TC-FA-SU-777: Filter kelas enum, kolom Role, Action Taken, dan Transaction Status

10. Buka dropdown `Role`
11. Verifikasi opsi dropdown = DISTINCT data tabel: `Approver`, `Asset Admin`
12. Centang `Approver`
13. Klik `[Apply]`
14. Verifikasi tabel menyisakan `BRW-20260716-0314`, `BRW-20260712-0311` (2 baris)
15. Verifikasi chip `Approver` tampil di dalam field `Role`
16. Klik `[Clear Field]` pada field `Role`, lalu klik `[Apply]`
17. Buka dropdown `Action Taken`
18. Verifikasi opsi dropdown = DISTINCT data tabel: `Approved`, `Confirmed`, `Processed`, `Rejected`
19. Centang `Approved`
20. Klik `[Apply]`
21. Verifikasi tabel menyisakan `BRW-20260712-0311` (1 baris)
22. Verifikasi chip `Approved` tampil di dalam field `Action Taken`
23. Klik `[Clear Field]` pada field `Action Taken`, lalu klik `[Apply]`
24. Buka dropdown `Transaction Status`
25. Verifikasi opsi dropdown = DISTINCT data tabel: `Active`, `Completed`, `Rejected`
26. Centang `Active`
27. Klik `[Apply]`
28. Verifikasi tabel menyisakan `BRW-20260718-0315`, `BRW-20260713-0312` (2 baris)
29. Verifikasi chip `Active` tampil di dalam field `Transaction Status`
30. Klik `[Clear Field]` pada field `Transaction Status`, lalu klik `[Apply]`

### TC-FA-SU-778: Filter kelas date, kolom Date

31. Pilih rentang 12/07/26 sampai 13/07/26 pada field `Date`
32. Klik `[Apply]`
33. Verifikasi rentang inklusif 12/07/26 sampai 13/07/26 menyisakan `BRW-20260713-0312`, `BRW-20260712-0311` (2 baris)
34. Klik `[Clear Field]` pada field `Date`, lalu klik `[Apply]`
35. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan seluruh langkah `[Clear Field]` lalu `[Apply]` serta penutupan panel; TC-FA-SU-777 menuntut tiap field diuji terpisah tanpa filter field lain, dan pemulihan yang sama dipakai pada TC-FA-SU-776 dan TC-FA-SU-778 (S-09).
- Panel Filter diasumsikan tetap terbuka sesudah `[Apply]` (mengikuti urutan langkah TC-FA-SU-777).
- Opsi dropdown ditulis sebagai DISTINCT data tabel sesuai Expected TC (lima baris seed; S-11).
- Temuan untuk QA (S-15): (1) TC-FA-SU-776 dan TC-FA-SU-778 tidak memiliki langkah pemulihan filter; spec menambahkan `[Clear Field]` lalu `[Apply]` sebagai langkah penghubung. (2) Pre-setup tidak menyebut nilai Role/Action Taken/Transaction Status per baris selain yang tercantum di Expected; spec hanya memakai nilai itu.
