---
id: TC-FA-SU-E2E-440-tab-transaction-admin-log-state-per-sub-tab
title: "Tab Transaction Admin Log: State per Sub-tab"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-796
coverage:
  web: automated
---

# Tab Transaction Admin Log: State per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc`, hover, dan muat ulang halaman (`F5`).
- Sub-tab Transfer milik Budi Santoso dipakai hanya sebagai tempat menerapkan kontrol berbeda (Search `TRF` dan sort `Date`); isinya tidak diasersi (NC-23).

## Test Steps

### TC-FA-SU-796: State sub-tab Borrow dipertahankan per sub-tab

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Ketik Search `Latitude`, tekan Enter
3. Klik icon Filter
4. Buka dropdown Group lalu centang `General Affairs` dan `Finance & Accounting`
5. Klik `[Apply]`
6. Klik icon Filter untuk menutup panel
7. Klik header kolom `Name` satu kali
8. Ganti page size ke 25
9. Klik Sub-tab Transfer
10. Verifikasi kotak Search sub-tab Transfer kosong
11. Verifikasi ikon Filter sub-tab Transfer tanpa badge titik
12. Verifikasi page size sub-tab Transfer 10
13. Ketik Search `TRF`, tekan Enter
14. Klik header kolom `Date` satu kali
15. Klik Sub-tab Borrow
16. Verifikasi kotak Search sub-tab Borrow berisi `Latitude`
17. Verifikasi ikon Filter sub-tab Borrow menampilkan badge titik
18. Verifikasi header kolom `Name` menampilkan sort ascending
19. Verifikasi page size sub-tab Borrow 25
20. Klik Back breadcrumb ke User List
21. Klik Name `Budi Santoso` pada hasil Search User List (kotak Search mempertahankan nilainya sesudah Back), klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
22. Verifikasi kotak Search sub-tab Borrow berisi `Latitude`
23. Verifikasi ikon Filter sub-tab Borrow menampilkan badge titik
24. Verifikasi header kolom `Name` menampilkan sort ascending
25. Verifikasi page size sub-tab Borrow 25
26. Klik `F5`
27. Klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
28. Verifikasi kotak Search sub-tab Borrow berisi `Latitude`
29. Verifikasi ikon Filter sub-tab Borrow menampilkan badge titik
30. Verifikasi header kolom `Name` menampilkan sort ascending
31. Verifikasi page size sub-tab Borrow 25
32. Klik menu Settings > User pada sidebar
33. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
34. Verifikasi kotak Search sub-tab Borrow kosong
35. Verifikasi ikon Filter sub-tab Borrow tanpa badge titik
36. Verifikasi tabel sub-tab Borrow mengikuti sort default Date terbaru lebih dulu
37. Verifikasi page size sub-tab Borrow 10

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 dan langkah 33 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan Detail dari hasil Search User List sesudah Back breadcrumb (langkah 21; kotak Search User List mempertahankan nilainya sesudah Back, bagian 8b butir 9) dan pembukaan ulang tab dan sub-tab sesudah `F5` (langkah 27).
- Pilihan spec: Search `Latitude`, Filter Group `General Affairs` dan `Finance & Accounting`, sort `Name`, dan page size 25 pada sub-tab Borrow; Search `TRF` dan sort `Date` pada sub-tab Transfer. TC-FA-SU-796 tidak menyebut nilai kontrolnya. Search `Latitude` dan Filter Group tersebut menyisakan `BRW-2026-0315` dan `BRW-2026-0312`.
- Pembagian TC lintas spec: pagination dan tooltip icon Borrow (TC-FA-SU-789 dan TC-FA-SU-794) ada di spec 261.
- Temuan untuk QA (S-15): (1) TC-FA-SU-796 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (#1) dari hook suite. (2) TC-FA-SU-796 Expected a menyebut nomor halaman aktif tidak diuji karena fixture sub-tab satu halaman; spec tidak mengasersi nomor halaman. (3) Expected b menyatakan state satu sub-tab tidak memengaruhi sub-tab lain; spec mengasersinya pada sub-tab Transfer untuk Search, Filter, dan page size (sort tidak diasersi karena isi sub-tab Transfer tidak diasersi, NC-23). (4) Post Condition tidak ada.
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01) (empat kontrol state diasersi pada empat kondisi navigasi), bukan dari langkah tambahan.
