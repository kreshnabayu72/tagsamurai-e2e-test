---
id: TC-FA-SU-E2E-179-sub-tab-pending-tasks-pagination-tooltip-icon-dan-state-per-sub-tab
title: "Sub-tab Pending Tasks: Pagination, Tooltip Icon, dan State per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-530
  - TC-FA-SU-535
  - TC-FA-SU-537
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Pagination, Tooltip Icon, dan State per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Tabel parameter "Nomor halaman tidak valid":

| Input |
|---|
| `0` |
| `-1` |
| `999` |
| `abc` |
- Tabel parameter "Ikon dan header tooltip":

| Ikon | Tooltip |
|---|---|
| `Search` | `Search` |
| `Filter` | `Filter` |
| `Download` | `Download` |
| header kolom Actions (⋯) | `Column Visibility` |
- Sub-tab lain untuk TC-FA-SU-537: Sub-tab Borrowed Assets (state diubah hanya dengan page size).

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-530: Pagination: page size, navigasi, dan kasus tepi

2. Verifikasi footer pagination menampilkan default 10 baris per halaman
3. Klik dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
5. Tekan Esc
6. Untuk setiap baris tabel "Nomor halaman tidak valid" (langkah 6 sampai 7): isi nomor halaman input baris itu, tekan Enter
7. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
8. Ganti page size ke 25
9. Ganti page size ke 10
10. Verifikasi tabel menampilkan halaman 1 setelah page size diganti
11. Klik header Transaction ID satu kali
12. Verifikasi tabel menampilkan halaman 1 setelah sort diganti
13. Ketik Search `ASG-2026`, tekan Enter
14. Verifikasi tabel menampilkan halaman 1 setelah Search mengubah hasil (`ASG-20260715-0045`, `ASG-20260718-0067`)
15. Klik `←` pada kotak Search
16. Klik header Transaction ID dua kali (kembali ke netral)

### TC-FA-SU-535: Tooltip icon Table Tools dan header Actions

17. Untuk setiap baris tabel "Ikon dan header tooltip" (langkah 17 sampai 18): hover ikon baris itu
18. Verifikasi tooltip sama dengan kolom "Tooltip" baris itu

### TC-FA-SU-537: State sub-tab dipertahankan per sub-tab

19. Ketik Search `ASG-2026`, tekan Enter
20. Klik icon Filter
21. Buka dropdown Transaction lalu centang `Assignment`
22. Klik `[Apply]`
23. Klik header Request Date satu kali
24. Ganti page size ke 25
25. Klik Sub-tab Borrowed Assets
26. Ganti page size ke 50
27. Verifikasi Sub-tab Borrowed Assets tidak memuat Search dan Filter dari Sub-tab Pending Tasks (kotak Search kosong dan ikon Filter tanpa badge titik)
28. Klik Sub-tab Pending Tasks
29. Verifikasi Search `ASG-2026` Sub-tab Pending Tasks dipulihkan
30. Verifikasi Filter Transaction `Assignment` Sub-tab Pending Tasks dipulihkan
31. Verifikasi Sort Request Date ascending (↑) Sub-tab Pending Tasks dipulihkan
32. Verifikasi page size 25 Sub-tab Pending Tasks dipulihkan
33. Klik Back breadcrumb ke List
34. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks
35. Verifikasi state Sub-tab Pending Tasks (Search, Filter, Sort, page size) dipulihkan setelah Back breadcrumb
36. Tekan F5
37. Verifikasi state Sub-tab Pending Tasks (Search, Filter, Sort, page size) dipulihkan setelah refresh
38. Klik menu Settings > User pada sidebar
39. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks
40. Verifikasi state Sub-tab Pending Tasks kembali ke default setelah keluar lewat menu sidebar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13) (langkah 1; langkah 34 memakai ganti isi kotak search karena Search dipertahankan sesudah Back breadcrumb, langkah 39 mengetik ulang sesudah menu sidebar); membuka dropdown page size (langkah 3) dan menutupnya dengan Esc (langkah 5); mengosongkan Search dan mengembalikan sort ke netral di akhir TC-FA-SU-530 (S-09); langkah Back, buka Detail ulang, dan klik menu sidebar pada TC-FA-SU-537 adalah aksi TC.
- Langkah berulang per baris tabel parameter: tabel "Nomor halaman tidak valid" pada langkah 6 sampai 7 (4 iterasi); tabel "Ikon dan header tooltip" pada langkah 17 sampai 18 (4 iterasi).
- Jumlah langkah: 40 tertulis, 52 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (52 langkah). Seluruh blok berada pada satu surface (satu sub-tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-530 Expected e adalah catatan fixture (satu halaman data) tanpa perilaku UI untuk diasersi; perilaku multi-halaman diuji pada TC-FA-SU-359 dan TC-FA-SU-1057 menurut Expected itu.
  - TC-FA-SU-537 tidak menyebut kontrol "berbeda" yang diterapkan pada sub-tab lain dan nomor halaman aktif tidak diuji (fixture satu halaman); spec memakai page size 50 pada Sub-tab Borrowed Assets.
