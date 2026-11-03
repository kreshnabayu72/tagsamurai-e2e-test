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
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps


### TC-FA-SU-772: Sort kelas teks, kolom Transaction ID dan Group

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment
2. Klik header `Transaction ID` satu kali
3. Verifikasi ascending (↑): `BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`
4. Klik header `Transaction ID` kedua kali
5. Verifikasi descending (↓): `BRW-20260718-0315`, `BRW-20260716-0314`, `BRW-20260715-0313`, `BRW-20260713-0312`, `BRW-20260712-0311`
6. Klik header `Transaction ID` ketiga kali
7. Verifikasi netral kembali ke default: `BRW-20260718-0315`, `BRW-20260716-0314`, `BRW-20260715-0313`, `BRW-20260713-0312`, `BRW-20260712-0311`
8. Klik header `Group` satu kali
9. Verifikasi ascending (↑): `BRW-20260716-0314`, `BRW-20260713-0312`, `BRW-20260718-0315`, `BRW-20260712-0311`, `BRW-20260715-0313`
10. Klik header `Group` kedua kali
11. Verifikasi descending (↓): `BRW-20260715-0313`, `BRW-20260712-0311`, `BRW-20260718-0315`, `BRW-20260713-0312`, `BRW-20260716-0314`
12. Klik header `Group` ketiga kali
13. Verifikasi netral kembali ke default: `BRW-20260718-0315`, `BRW-20260716-0314`, `BRW-20260715-0313`, `BRW-20260713-0312`, `BRW-20260712-0311`

### TC-FA-SU-773: Sort kelas date, kolom Date

14. Klik header `Date` satu kali
15. Verifikasi ascending (↑): `BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`
16. Klik header `Date` kedua kali
17. Verifikasi descending (↓): `BRW-20260718-0315`, `BRW-20260716-0314`, `BRW-20260715-0313`, `BRW-20260713-0312`, `BRW-20260712-0311`
18. Klik header `Date` ketiga kali
19. Verifikasi netral kembali ke default: `BRW-20260718-0315`, `BRW-20260716-0314`, `BRW-20260715-0313`, `BRW-20260713-0312`, `BRW-20260712-0311`

### TC-FA-SU-774: Guard kolom non-sortable Role, Action Taken, dan Transaction Status

20. Hover dan klik header `Role`
21. Verifikasi header `Role` tidak memiliki icon sort
22. Verifikasi klik header `Role` tidak mengubah urutan baris
23. Hover dan klik header `Action Taken`
24. Verifikasi header `Action Taken` tidak memiliki icon sort
25. Verifikasi klik header `Action Taken` tidak mengubah urutan baris
26. Hover dan klik header `Transaction Status`
27. Verifikasi header `Transaction Status` tidak memiliki icon sort
28. Verifikasi klik header `Transaction Status` tidak mengubah urutan baris

### TC-FA-SU-775: Screening Filter Panel (field, label, placeholder, dan tombol)

29. Hover icon Filter
30. Verifikasi tooltip `Filter` tampil
31. Klik icon Filter
32. Verifikasi panel terbuka di bawah Table Tools
33. Verifikasi icon Filter menjadi gelap
34. Verifikasi field berurutan `Group`, `Role`, `Action Taken`, `Date`, `Transaction Status`
35. Verifikasi field `Group` berupa multi-select searchable dengan placeholder `All groups`
36. Verifikasi field `Role` berupa multi-select searchable dengan placeholder `All roles`
37. Verifikasi field `Action Taken` berupa multi-select searchable dengan placeholder `All actions`
38. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
39. Verifikasi field `Transaction Status` berupa multi-select searchable dengan placeholder `All statuses`
40. Verifikasi footer panel menampilkan `[Clear Field]` di kiri dan `[Apply]` di kanan
41. Verifikasi icon Filter tanpa badge titik selama belum ada filter ter-Apply
42. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan penutupan panel Filter. Klik ketiga tiap header sort mengembalikan sort ke default sehingga tidak perlu reset lain (S-09).
- Order yang diasersi pada TC-FA-SU-772 dan TC-FA-SU-773 mengikuti Expected TC (lima baris seed, dua nilai distinct atau lebih per kolom, S-11).
- Temuan untuk QA (S-15): (1) TC-FA-SU-774 Langkah Uji nomor 2 "Hover dan klik tiap header" tidak menyebut apa yang diamati saat hover; spec mengasersi hanya ketiadaan icon sort dan urutan tidak berubah sesuai Expected. (2) TC-FA-SU-775 butir a menyebut "tooltip hover `Filter`" tanpa menyebut kapan; spec menaruhnya sebelum klik karena tooltip dibaca saat hover.
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
