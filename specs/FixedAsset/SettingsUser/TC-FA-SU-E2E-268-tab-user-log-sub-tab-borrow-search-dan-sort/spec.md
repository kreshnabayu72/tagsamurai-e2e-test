---
id: TC-FA-SU-E2E-268-tab-user-log-sub-tab-borrow-search-dan-sort
title: "Tab User Log sub-tab Borrow: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-809
  - TC-FA-SU-810
  - TC-FA-SU-811
  - TC-FA-SU-812
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Nilai Date seed untuk Search kolom non-searchable (Pre-setup #30, TC-FA-SU-810): `18/07/26`; nilai ini harus tampil pada sel kolom Date tabel Borrow sebelum dipakai sebagai keyword.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-809: Siklus interaksi Search (reveal, Enter, clear, collapse)

2. Hover icon Search
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi kursor fokus di input Search
7. Verifikasi placeholder `Search transaction ID, name, or PIC...` tampil
8. Ketik 1 karakter dari `Returned` (`R`)
9. Verifikasi icon `✕` tampil di kanan input
10. Verifikasi tabel belum tersaring dan masih menampilkan enam baris
11. Ketik sisa `eturned` pada input, tekan Enter
12. Verifikasi tabel tersaring menjadi `Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`
13. Klik `✕`
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input Search
17. Verifikasi tabel tetap menampilkan hasil search terakhir (`Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris (enam baris)
20. Ketik Search `Returned`, tekan Enter
21. Klik `←` pada kotak Search
22. Verifikasi search bar menutup
23. Verifikasi tabel langsung kembali ke semua baris (enam baris)
24. Klik icon Search
25. Verifikasi keyword dikosongkan (input kosong)
26. Ketik Search `  Returned  ` (spasi awal dan akhir), tekan Enter
27. Verifikasi hasil sama dengan `Returned` tanpa spasi (`Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`)
28. Verifikasi isi input tidak berubah (`  Returned  ` dengan spasi awal dan akhir)
29. Klik `←` pada kotak Search

### TC-FA-SU-810: Guard kolom non-searchable Date

30. Verifikasi nilai Date `18/07/26` tampil pada sel kolom Date tabel
31. Ketik Search `18/07/26`, tekan Enter
32. Verifikasi empty state `No results found` tampil
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-811: Search terikat visibilitas kolom Activity

34. Ketik Search `Returned`, tekan Enter
35. Verifikasi tabel menyisakan `Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`
36. Klik header `⋯`, lalu hilangkan centang `Activity`
37. Tutup overlay Column Visibility dengan Esc
38. Verifikasi header kolom `Name` tampil
39. Ganti isi kotak search dengan `Returned`, tekan Enter
40. Verifikasi tabel tidak menyisakan baris (kolom tersembunyi tidak dicari)
41. Klik header `⋯`, lalu beri centang `Activity`
42. Tutup overlay Column Visibility dengan Esc
43. Ganti isi kotak search dengan `Returned`, tekan Enter
44. Verifikasi tabel kembali menyisakan `Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`
45. Klik `←` pada kotak Search

### TC-FA-SU-812: Sort kelas date, kolom Date

46. Klik header `Date` satu kali
47. Verifikasi ascending (↑), lima baris teratas: `Borrowed|BRW-20260205-0102`, `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260712-0347`
48. Klik header `Date` kedua kali
49. Verifikasi descending (↓), lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`
50. Klik header `Date` ketiga kali
51. Verifikasi netral kembali ke default, lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan atau penutupan input Search, dan penutupan overlay Column Visibility; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah 30 (`Verifikasi nilai Date 18/07/26 tampil pada sel kolom Date tabel`) adalah asersi tambahan di luar Expected TC dan dicatat di sini (S-03): anchor positif bahwa nilai Date seed tampil sebelum asersi Search kolom non-searchable tanpa hasil (bagian 8b butir 2 dan butir 15b). TC-FA-SU-810 tidak memetakan `18/07/26` ke baris seed tertentu; spec mengasumsikan nilai itu tampil pada salah satu baris Borrow (Pre-setup #30).
- Keadaan "tabel belum tersaring" dan "kembali ke semua baris" pada TC-FA-SU-809 ditulis sebagai enam baris berdasarkan Pre-setup #30 (bagian 8b butir 10).
- Anchor positif asersi "tidak menyisakan baris" pada TC-FA-SU-811 adalah `Verifikasi` hasil Search sebelum kolom disembunyikan dan header kolom `Name` tampil (bagian 8b butir 2); asersi header tersebut tambahan atas Expected TC dan dicatat di sini (S-03).
- Pre-setup #30 menyatakan sub-tab Borrow berisi 6 baris, sedangkan TC mencantumkan lima baris pada daftar urutan; spec mengasersi lima baris teratas sesuai daftar TC dan keenam baris untuk jumlah total (S-14).
- Temuan untuk QA (S-15): daftar urutan descending pada TC-FA-SU-805 butir c dan TC-FA-SU-812 butir a bukan kebalikan daftar ascending (descending dimulai `Returned|BRW-20260320-0188`, ascending berakhir `Borrowed|BRW-20260712-0347`) bila hanya lima baris teratas yang dicantumkan; enam baris Pre-setup #30 membuat daftar TC kemungkinan terpotong dari baris keenam. Spec mengikuti daftar TC.
- Temuan untuk QA (S-15) tambahan: TC-FA-SU-811 butir b menyebut "kolom lain yang tampil tetap dicari" tanpa data uji yang membuktikannya; klausa itu tidak diasersi.
- Spec ini berjumlah 51 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
