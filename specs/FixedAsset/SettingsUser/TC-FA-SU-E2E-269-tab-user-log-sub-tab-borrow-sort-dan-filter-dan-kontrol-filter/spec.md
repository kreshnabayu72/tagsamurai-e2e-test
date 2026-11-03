---
id: TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter
title: "Tab User Log sub-tab Borrow: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-813
  - TC-FA-SU-814
  - TC-FA-SU-815
  - TC-FA-SU-816
  - TC-FA-SU-817
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-813: Sort kelas teks, kolom Transaction ID dan Name

2. Klik header `Transaction ID` satu kali
3. Verifikasi ascending (↑), lima baris teratas: `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260205-0102`, `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260615-0305`
4. Klik header `Transaction ID` kedua kali
5. Verifikasi descending (↓), lima baris teratas: `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`
6. Klik header `Transaction ID` ketiga kali
7. Verifikasi netral kembali ke default, lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`
8. Klik header `Name` satu kali
9. Verifikasi ascending (↑), lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260205-0102`
10. Klik header `Name` kedua kali
11. Verifikasi descending (↓), lima baris teratas: `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260205-0102`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260320-0188`
12. Klik header `Name` ketiga kali
13. Verifikasi netral kembali ke default, lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`

### TC-FA-SU-814: Sort kelas user, kolom PIC

14. Klik header `PIC` satu kali
15. Verifikasi ascending (↑), lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260205-0102`
16. Klik header `PIC` kedua kali
17. Verifikasi descending (↓), lima baris teratas: `Returned|BRW-20260615-0305`, `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`
18. Klik header `PIC` ketiga kali
19. Verifikasi netral kembali ke default, lima baris teratas: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`

### TC-FA-SU-815: Guard kolom non-sortable Activity

20. Hover dan klik header `Activity`
21. Verifikasi header `Activity` tidak memiliki icon sort
22. Verifikasi klik header `Activity` tidak mengubah urutan baris

### TC-FA-SU-816: Screening Filter Panel (field, label, placeholder, dan tombol)

23. Hover icon Filter
24. Verifikasi tooltip `Filter` tampil
25. Klik icon Filter
26. Verifikasi panel terbuka di bawah Table Tools
27. Verifikasi icon Filter menjadi gelap
28. Verifikasi field berurutan `Date`, `Activity`, `PIC`
29. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
30. Verifikasi field `Activity` berupa multi-select searchable dengan placeholder `All activities`
31. Verifikasi field `PIC` berupa multi-select searchable dengan placeholder `All PICs`
32. Verifikasi footer panel menampilkan `[Clear Field]` di kiri dan `[Apply]` di kanan
33. Verifikasi icon Filter tanpa badge titik selama belum ada filter ter-Apply

### TC-FA-SU-817: Filter kelas date, kolom Date

34. Pilih rentang 05/02/26 sampai 12/02/26 pada field `Date`
35. Klik `[Apply]`
36. Verifikasi rentang inklusif 05/02/26 sampai 12/02/26 menyisakan `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260205-0102` (2 baris)
37. Klik `[Clear Field]` pada field `Date`, lalu klik `[Apply]`
38. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan penutupan panel Filter; klik ketiga tiap header sort mengembalikan sort ke default; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pre-setup #30 menyatakan sub-tab Borrow berisi 6 baris, sedangkan TC mencantumkan lima baris pada daftar urutan; spec mengasersi lima baris teratas sesuai daftar TC dan keenam baris untuk jumlah total (S-14).
- Panel Filter pada TC-FA-SU-817 sudah terbuka dari TC-FA-SU-816 (urutan tidak berubah).
- Temuan untuk QA (S-15): daftar urutan descending pada TC-FA-SU-805 butir c dan TC-FA-SU-812 butir a bukan kebalikan daftar ascending (descending dimulai `Returned|BRW-20260320-0188`, ascending berakhir `Borrowed|BRW-20260712-0347`) bila hanya lima baris teratas yang dicantumkan; enam baris Pre-setup #30 membuat daftar TC kemungkinan terpotong dari baris keenam. Spec mengikuti daftar TC.
- Temuan untuk QA (S-15) tambahan: (1) TC-FA-SU-815 Langkah Uji nomor 2 "Hover dan klik tiap header" tidak menyebut apa yang diamati saat hover; spec mengasersi ketiadaan icon sort dan urutan tidak berubah. (2) Daftar urutan sort Name dan PIC pada TC-FA-SU-813 dan TC-FA-SU-814 mencantumkan lima dari enam baris; spec mengikuti daftar TC.
- Spec ini berjumlah 38 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
