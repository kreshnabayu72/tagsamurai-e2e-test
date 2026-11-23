---
id: TC-FA-SU-E2E-256-tab-transaction-admin-log-sort-dan-filter-dan-kontrol-filter
title: "Tab Transaction Admin Log: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-772
  - TC-FA-SU-773
  - TC-FA-SU-774
  - TC-FA-SU-775
coverage:
  web: automated
---

# Tab Transaction Admin Log: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso. Sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC: `18/07/26` `Returned · Self-processed` `BRW-2026-0315` `Laptop Dell Latitude - 3` `Rina Wijaya` `General Affairs`; `16/07/26` `Rejected` `BRW-2026-0314` `Projector Epson - 1` `Andi Pratama` `Branch Surabaya`; `15/07/26` `Handed over` `BRW-2026-0313` `Camera Sony A7 - 2` `Budi Santoso` `Logistics Warehouse`; `13/07/26` `Requested` `BRW-2026-0312` `Laptop Dell Latitude - 5` `Dewi Lestari` `Finance & Accounting`; `12/07/26` `Draft created` `—` `Tablet Samsung Tab - 4` `—` `IT Infrastructure`. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Kemampuan teknis: hover ikon dan header kolom.
- State: yang berubah hanya Sort dan Filter Panel di sisi klien; tiap kolom dikembalikan ke urutan default lewat klik ketiga (netral) dan Filter Panel ditutup di akhir spec. Tidak ada state global dan tidak ada data yang dibuat spec.

## Test Steps

### TC-FA-SU-772: Sort kelas teks, Transaction ID, Name, Borrower, dan Group

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Verifikasi tabel memuat sedikitnya dua baris data uji (lima baris sesuai Pre-setup #29)
3. Klik header `Transaction ID` satu kali
4. Verifikasi urutan ascending (↑): `BRW-2026-0312`, `BRW-2026-0313`, `BRW-2026-0314`, `BRW-2026-0315`, `Draft created` (nilai kosong `—` di akhir)
5. Klik header `Transaction ID` kedua kali
6. Verifikasi urutan descending (↓): `Draft created`, `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312` (nilai kosong `—` di awal)
7. Klik header `Transaction ID` ketiga kali
8. Verifikasi urutan netral kembali ke default: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`
9. Klik header `Name` satu kali
10. Verifikasi urutan ascending (↑): `BRW-2026-0313`, `BRW-2026-0315`, `BRW-2026-0312`, `BRW-2026-0314`, `Draft created`
11. Klik header `Name` kedua kali
12. Verifikasi urutan descending (↓): `Draft created`, `BRW-2026-0314`, `BRW-2026-0312`, `BRW-2026-0315`, `BRW-2026-0313`
13. Klik header `Name` ketiga kali
14. Verifikasi urutan netral kembali ke default: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`
15. Klik header `Borrower` satu kali
16. Verifikasi urutan ascending (↑): `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `BRW-2026-0315`, `Draft created` (nilai kosong `—` di akhir)
17. Klik header `Borrower` kedua kali
18. Verifikasi urutan descending (↓): `Draft created`, `BRW-2026-0315`, `BRW-2026-0312`, `BRW-2026-0313`, `BRW-2026-0314` (nilai kosong `—` di awal)
19. Klik header `Borrower` ketiga kali
20. Verifikasi urutan netral kembali ke default: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`
21. Klik header `Group` satu kali
22. Verifikasi urutan ascending (↑): `BRW-2026-0314`, `BRW-2026-0312`, `BRW-2026-0315`, `Draft created`, `BRW-2026-0313`
23. Klik header `Group` kedua kali
24. Verifikasi urutan descending (↓): `BRW-2026-0313`, `Draft created`, `BRW-2026-0315`, `BRW-2026-0312`, `BRW-2026-0314`
25. Klik header `Group` ketiga kali
26. Verifikasi urutan netral kembali ke default: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`

### TC-FA-SU-773: Sort kelas date, Date

27. Klik header `Date` satu kali
28. Verifikasi urutan ascending (↑): `Draft created`, `BRW-2026-0312`, `BRW-2026-0313`, `BRW-2026-0314`, `BRW-2026-0315`
29. Klik header `Date` kedua kali
30. Verifikasi urutan descending (↓): `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`
31. Klik header `Date` ketiga kali
32. Verifikasi urutan netral kembali ke default: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`

### TC-FA-SU-774: Guard kolom non-sortable, Activity

33. Hover header `Activity`
34. Verifikasi header `Activity` tidak memiliki icon sort
35. Klik header `Activity`
36. Verifikasi urutan tidak berubah (tetap default: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, `Draft created`)

### TC-FA-SU-775: Screening Filter Panel, field, label, placeholder, dan tombol

37. Klik icon Filter
38. Verifikasi panel Filter terbuka di bawah Table Tools
39. Verifikasi icon Filter menjadi gelap
40. Hover icon Filter
41. Verifikasi tooltip `Filter` tampil
42. Verifikasi field berurutan: `Date` (date range picker, placeholder `Select date`), `Activity` (multi-select searchable, placeholder `All activities`), `Name` (multi-select searchable, placeholder `All assets`), `Borrower` (multi-select searchable, placeholder `All borrowers`), `Group` (multi-select searchable, placeholder `All groups`)
43. Verifikasi label field `Date`, `Activity`, `Name`, `Borrower`, dan `Group`
44. Verifikasi tidak ada field `Role` dan `Transaction Status`, dan `Transaction ID` tidak memiliki field filter
45. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
46. Verifikasi icon Filter tanpa badge titik (belum ada filter ter-Apply)
47. Klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna di User List lalu membuka sub-tab; R-16) dan penutupan Filter Panel (langkah 47, S-09). Klik ketiga tiap header (langkah 7, 13, 19, 25, 31) mengembalikan urutan default sehingga TC berikutnya tidak mewarisi sort (S-09); `Verifikasi`-nya adalah butir Expected klik 3 TC.
- Langkah 2 adalah anchor bahwa tabel memuat sedikitnya dua baris data uji sebelum asersi sort pertama (8b.15 butir d, S-11); lima baris itu sudah dijamin Pre-setup #29. Pada urutan tiap kolom, nilai kosong `—` (baris Draft) pada kolom Transaction ID dan Borrower ditulis di akhir saat ascending dan di awal saat descending (`prd-conventions.md` §9.15) sesuai TC-FA-SU-772 butir a dan c.
- Temuan untuk QA (S-15): (1) Kolom ACC TC-FA-SU-772 sampai 775 berisi `#20`, yang di Pre-setup adalah Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (2) TC-FA-SU-774 langkah 2 ("Hover dan klik tiap header kolom yang dicantumkan") hanya memuat kolom Activity; spec mengasersi tanpa icon sort dan urutan tidak berubah, dua klausa yang disebut TC. (3) Post Condition tidak ada pada keempat TC.
- Spec ini berjumlah 47 langkah dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface dengan data seed yang sama, berdiri sendiri; ukuran berasal dari TC-FA-SU-772 (empat kolom, tiga klik tiap kolom, masing-masing satu `Verifikasi` urutan, S-01) dan klausa Expected TC-FA-SU-775, bukan dari langkah tambahan. Langkah berulang per kolom (langkah 3 sampai 26) tidak dijadikan loop karena nilai urutan berbeda tiap iterasi.
