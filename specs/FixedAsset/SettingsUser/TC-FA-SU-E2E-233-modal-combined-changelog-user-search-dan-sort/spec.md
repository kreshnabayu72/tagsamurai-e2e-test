---
id: TC-FA-SU-E2E-233-modal-combined-changelog-user-search-dan-sort
title: "Modal Combined Changelog: User: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-707
  - TC-FA-SU-708
  - TC-FA-SU-709
  - TC-FA-SU-710
coverage:
  web: automated
---

# Modal Combined Changelog: User: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.

## Test Steps

### TC-FA-SU-707: Siklus interaksi Search

1. Klik icon Changelog di Table Tools halaman User List
2. Klik icon Search
3. Verifikasi input melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search action, field, or value...`
6. Hover icon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter dari `Resend` (`R`)
9. Verifikasi icon ✕ tampil di kanan input
10. Verifikasi tabel belum tersaring
11. Ketik sisa `Resend` (`esend`) lalu tekan Enter
12. Verifikasi tabel tersaring menjadi C-1
13. Klik ✕
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris
20. Ketik `Resend`, tekan Enter, lalu klik icon ←
21. Verifikasi search bar menutup
22. Verifikasi keyword dikosongkan
23. Verifikasi tabel langsung kembali ke semua baris
24. Klik icon Search
25. Ketik `  Resend  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Resend` tanpa spasi (C-1)
27. Verifikasi isi input tidak berubah

### TC-FA-SU-708: Guard kolom non-searchable Date

28. Ganti isi kotak search dengan `15/06/26` (nilai kolom Date), tekan Enter
29. Verifikasi nilai Date `15/06/26` tidak mencocokkan baris melalui Search; empty state `No results found` tampil
30. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-709: Search terikat visibilitas kolom Action

31. Ketik Search `Resend`, tekan Enter
32. Verifikasi sebelum hide: keyword `Resend` menyisakan C-1 (1 baris)
33. Klik header Column Visibility (⋯), hilangkan centang Action
34. Ganti isi kotak search dengan `Resend`, tekan Enter
35. Verifikasi setelah kolom Action di-hide: keyword yang sama menyisakan tidak ada baris (0 baris), empty state `No results found` tampil
36. Klik header Column Visibility (⋯), centang kembali Action
37. Ganti isi kotak search dengan `Resend`, tekan Enter
38. Verifikasi setelah kolom Action di-unhide: hasil kembali C-1 (1 baris)
39. Klik `(←)` pada kotak Search

### TC-FA-SU-710: Sort kelas date (Date)

40. Klik header Date satu kali
41. Verifikasi urutan lima baris pertama klik 1 ascending (↑): C-6, C-5, C-4, C-3, C-2
42. Klik header Date kedua kali
43. Verifikasi urutan lima baris pertama klik 2 descending (↓): C-1, C-2, C-3, C-4, C-5
44. Klik header Date ketiga kali
45. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: C-1, C-2, C-3, C-4, C-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris TC-FA-SU-709, sebagai anchor positif absence (bagian 8b butir 2).
- Spec ini berjumlah 45 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) TC-FA-SU-709 butir b menulis hasil tanpa baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2).
