---
id: TC-FA-RP-E2E-150-tab-total-control-pagination-dan-state-halaman
title: "Tab Total Control: Pagination dan state halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-515
  - TC-FA-RP-516
  - TC-FA-RP-517
  - TC-FA-RP-518
coverage:
  web: automated
---

# Tab Total Control: Pagination dan state halaman

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Position dan Division memiliki dua nilai distinct atau lebih) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Nilai nomor halaman tidak valid untuk TC 518 (tidak tertulis di Data Uji TC): `0`, `99` (melebihi jumlah halaman), dan `abc` (bukan angka), dipilih spec.

## Test Steps

### Default dan pilihan ukuran halaman (TC 515)

1. Verifikasi pagination menampilkan default 10 data per halaman.
2. Buka Overlay Page Size.
3. Verifikasi pilihan ukuran 10, 25, 50, dan 100 tanpa opsi `All`.
4. Tutup Overlay Page Size dengan Esc.

### Ganti ukuran halaman dan sort (TC 516)

5. Buka pilihan ukuran halaman pada pagination.
6. Verifikasi pilihan ukuran halaman 10, 25, 50, dan 100 (tanpa opsi `All`).
7. Verifikasi ukuran terpilih sebelum diganti adalah 10.
8. Pilih ukuran halaman 25.
9. Verifikasi info pagination menampilkan total 9 baris (Pre-setup #36) dan ukuran halaman 25.
10. Verifikasi kesembilan baris tampil dalam satu halaman.
11. Klik header kolom Position sekali (Position ascending).
12. Verifikasi urutan baris: Ahmad Fauzi, Eka Saputra, Fitri Handayani, Siti Rahmawati (sama-sama `Finance Officer`; tie-breaker default sort Name A-Z), Rudi Hartono, Siti Rahayu, Rina Wulandari, Admin Utama, Budi Santoso.
13. Verifikasi total tetap 9 baris.
14. Klik header kolom Position dua kali lagi hingga urutan kembali ke default sort tabel.
15. Ganti ukuran halaman menjadi 10.

### State dipertahankan saat F5, reset saat klik ulang menu (TC 517)

16. Klik ikon Search, ketik Search `Fina`, tekan Enter.
17. Klik ikon Filter, pilih opsi `Finance` pada field Division, lalu klik `[Apply]`.
18. Klik header kolom Name dua kali (Name descending).
19. Ganti ukuran halaman menjadi 25.
20. Muat ulang halaman (F5).
21. Verifikasi Search `Fina` tetap sama.
22. Verifikasi Filter Division `Finance` tetap sama.
23. Verifikasi Sort Name descending tetap sama.
24. Verifikasi ukuran halaman 25 tetap sama.
25. Verifikasi tabel tetap menampilkan Rudi Hartono lalu Fitri Handayani.
26. Klik menu Settings > Role & Permission di sidebar.
27. Verifikasi Search kosong.
28. Verifikasi tanpa Filter.
29. Verifikasi Sort Name A-Z.
30. Verifikasi ukuran halaman 10.
31. Verifikasi tabel menampilkan 9 baris (Pre-setup #36) dalam satu halaman dengan baris pertama Admin Utama.

### Kasus tepi nomor halaman (TC 518)

32. Masukkan nomor halaman `0`.
33. Verifikasi nomor halaman tidak valid diabaikan.
34. Masukkan nomor halaman `99` (melebihi jumlah halaman).
35. Verifikasi nomor halaman tidak valid diabaikan.
36. Masukkan nomor halaman `abc` (bukan angka).
37. Verifikasi nomor halaman tidak valid diabaikan.

## Notes

- Alasan di atas 35 langkah: keempat blok berkelas fungsional sama (pagination dan state halaman tabel yang sama, dataset sama), tiap blok berdiri sendiri dengan pemulihan state di antaranya, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 2, 4, 5, 8, 11, 14, 15, 16, 17, 18, 19, 20, 26, 32, 34, dan 36. Langkah 14 dan 15 memulihkan sort dan ukuran halaman ke default sebelum TC 517 (S-09). Langkah 5 sampai 7 mengikuti TC 516 yang membuka pilihan ukuran halaman lagi.
- Langkah 26 mereset Search, Sort, dan Filter (klik sidebar, bagian 4 konvensi); langkah 31 mengasersi baris pertama Admin Utama sebagai default Name A-Z.
- Temuan untuk QA:
  - TC 518 tidak menyebut nilai Data Uji; spec memakai `0`, `99`, dan `abc`. Pre-setup #36 hanya memuat sembilan baris sehingga ukuran halaman 10 menghasilkan satu halaman; "nomor halaman melebihi jumlah halaman" diasersi pada keadaan satu halaman.
  - TC 518 Expected "diabaikan" tidak merinci wujud di UI; spec mengasersi nomor halaman tidak valid diabaikan tanpa merinci (halaman aktif tidak berubah).
