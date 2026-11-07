---
id: TC-FA-SU-E2E-255-tab-transaction-admin-log-search
title: "Tab Transaction Admin Log: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-769
  - TC-FA-SU-770
  - TC-FA-SU-771
coverage:
  web: automated
---

# Tab Transaction Admin Log: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Nilai Date baris `BRW-20260718-0315` (Pre-setup #29, PRD §4.3g Example Data): `18/07/26`; dipakai TC-FA-SU-770 (kolom Date tidak dapat dicari lewat Search).

## Test Steps


### TC-FA-SU-769: Siklus interaksi Search (reveal, Enter, clear, collapse)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment
2. Hover icon Search
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi kursor fokus di input Search
7. Verifikasi placeholder `Search transaction ID, group, or role...` tampil
8. Ketik 1 karakter dari `0313` (`0`)
9. Verifikasi icon `✕` tampil di kanan input
10. Verifikasi tabel belum tersaring dan masih menampilkan lima baris
11. Ketik sisa `313` pada input, tekan Enter
12. Verifikasi tabel tersaring menjadi `BRW-20260715-0313`
13. Klik `✕`
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input Search
17. Verifikasi tabel tetap menampilkan hasil search terakhir (`BRW-20260715-0313`)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris (lima baris)
20. Ketik Search `0313`, tekan Enter
21. Klik `←` pada kotak Search
22. Verifikasi search bar menutup
23. Verifikasi tabel langsung kembali ke semua baris (lima baris)
24. Klik icon Search
25. Verifikasi keyword dikosongkan (input kosong)
26. Ketik Search `  0313  ` (spasi awal dan akhir), tekan Enter
27. Verifikasi hasil sama dengan `0313` tanpa spasi (`BRW-20260715-0313`)
28. Verifikasi isi input tidak berubah (`  0313  ` dengan spasi awal dan akhir)
29. Klik `←` pada kotak Search

### TC-FA-SU-770: Guard kolom non-searchable Date

30. Verifikasi sel Date baris `BRW-20260718-0315` pada tabel menampilkan `18/07/26`
31. Ketik Search `18/07/26`, tekan Enter
32. Verifikasi empty state `No results found` tampil
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-771: Search terikat visibilitas kolom Transaction ID

34. Ketik Search `0313`, tekan Enter
35. Verifikasi tabel menyisakan `BRW-20260715-0313`
36. Klik header `⋯`, lalu hilangkan centang `Transaction ID`
37. Tutup overlay Column Visibility dengan Esc
38. Verifikasi header kolom `Group` tampil
39. Ganti isi kotak search dengan `0313`, tekan Enter
40. Verifikasi tabel tidak menyisakan baris (kolom tersembunyi tidak dicari)
41. Klik header `⋯`, lalu beri centang `Transaction ID`
42. Tutup overlay Column Visibility dengan Esc
43. Ganti isi kotak search dengan `0313`, tekan Enter
44. Verifikasi tabel kembali menyisakan `BRW-20260715-0313`
45. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan atau penutupan input Search, dan penutupan overlay Column Visibility; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Keadaan awal "tabel belum tersaring" dan "kembali ke semua baris" ditulis sebagai lima baris berdasarkan Pre-setup #29 (bagian 8b butir 10).
- Asersi tambahan di luar Expected (S-03): `Verifikasi` sel Date `18/07/26` pada langkah 30 membuktikan nilai Date seed tampil sebelum asersi kolom non-searchable (bagian 8b butir 15b).
- Anchor positif asersi "tidak menyisakan baris" pada TC-FA-SU-771 adalah `Verifikasi` header kolom `Group` tampil dan hasil Search sebelum kolom disembunyikan (bagian 8b butir 2); asersi anchor ini tambahan atas Expected TC dan dicatat di sini (S-03).
- Temuan untuk QA (S-15): (1) TC-FA-SU-771 butir b menyebut "kolom lain yang tampil tetap dicari" tanpa data uji yang membuktikannya (keyword `0313` hanya cocok di Transaction ID); klausa itu tidak diasersi. (2) TC-FA-SU-770 menyebut "penyaringan kolom ini hanya lewat Filter Panel" sebagai keterangan, bukan asersi; tidak diasersi.
- Spec ini berjumlah 45 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
