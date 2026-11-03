---
id: TC-FA-SU-E2E-273-tab-user-log-sub-tab-borrow-setup-column-pagination-dan-tooltip-icon
title: "Tab User Log sub-tab Borrow: Setup Column, Pagination, dan Tooltip Icon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-829
  - TC-FA-SU-830
  - TC-FA-SU-835
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Setup Column, Pagination, dan Tooltip Icon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-830: Pagination (page size, navigasi, dan kasus tepi)

2. Verifikasi footer pagination menampilkan 10 baris per halaman
3. Klik dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi `All`
5. Tutup dropdown page size dengan Esc
6. Isi nomor halaman `0`, tekan Enter
7. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
8. Isi nomor halaman `-1`, tekan Enter
9. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
10. Isi nomor halaman `999`, tekan Enter
11. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
12. Isi nomor halaman `abc`, tekan Enter
13. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
14. Ganti page size ke 25
15. Verifikasi tabel menampilkan halaman 1
16. Ganti page size kembali ke 10
17. Verifikasi tabel menampilkan halaman 1
18. Klik header `Date` satu kali
19. Verifikasi tabel menampilkan halaman 1
20. Klik header `Date` dua kali lagi hingga sort kembali netral
21. Ketik Search `Returned`, tekan Enter
22. Verifikasi tabel menampilkan halaman 1
23. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-835: Tooltip icon Table Tools dan header Actions

24. Hover icon Search
25. Verifikasi tooltip `Search` tampil
26. Hover icon Filter
27. Verifikasi tooltip `Filter` tampil
28. Hover icon Download
29. Verifikasi tooltip `Download` tampil
30. Hover header kolom Actions (`⋯`)
31. Verifikasi tooltip `Column Visibility` tampil

### TC-FA-SU-829: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

32. Klik header kolom `⋯`, lalu klik item `Setup Column...`
33. Ubah pengaturan: hilangkan centang `Activity`, drag kolom `Transaction ID` satu posisi, dan klik icon Pin pada kolom `Date`
34. Klik `[Reset to Default]`
35. Verifikasi preview mengembalikan visibility, urutan, dan pin ke default modul
36. Klik `[Save]`
37. Verifikasi tabel menampilkan visibility, urutan, dan pin default setelah `[Save]`
38. Buka Setup Column, hilangkan centang `Activity`, lalu klik `✕`
39. Verifikasi perubahan preview dibuang
40. Verifikasi tabel memakai konfigurasi tersimpan terakhir
41. Buka Setup Column, hilangkan centang `Activity`, lalu tekan Esc
42. Verifikasi perubahan preview dibuang
43. Verifikasi tabel memakai konfigurasi tersimpan terakhir
44. Klik Back breadcrumb ke User List
45. Verifikasi konfigurasi kolom tabel User List tidak berubah (tidak terpengaruh perubahan tabel ini)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan Search, pemulihan sort ke netral, dan penutupan dropdown; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Urutan TC sumber diubah: TC-FA-SU-829 diletakkan terakhir karena langkah terakhirnya meninggalkan Detail lewat Back breadcrumb (S-10).
- Fixture sub-tab Borrow satu halaman; perpindahan antar halaman tidak dapat dicapai pada surface ini (butir e TC-FA-SU-830 menyatakan perilaku multi-halaman diuji pada TC-FA-SU-359 dan TC-FA-SU-1057) sehingga tidak diasersi di sini.
- Temuan untuk QA (S-15): (1) TC-FA-SU-829 Langkah Uji nomor 6 ("Buka tabel lain yang punya Setup Column dan bandingkan") tidak menyebut tabel; spec memakai tabel User List dan mengasersi konfigurasinya tidak berubah. Karena konfigurasi tabel ini sudah kembali ke default, perbandingan itu tidak membuktikan independensi cache sepenuhnya. (2) Post Condition TC-FA-SU-829 tidak punya langkah observasi dan tidak diasersi.
- Spec ini berjumlah 45 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
