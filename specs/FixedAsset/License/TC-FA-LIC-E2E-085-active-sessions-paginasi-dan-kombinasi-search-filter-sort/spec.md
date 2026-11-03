---
id: TC-FA-LIC-E2E-085-active-sessions-paginasi-dan-kombinasi-search-filter-sort
title: "Active Sessions: Paginasi serta Kombinasi Search, Filter, Sort, dan Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-294
  - TC-FA-LIC-295
  - TC-FA-LIC-296
  - TC-FA-LIC-297
coverage:
  web: automated
---

# Active Sessions: Paginasi serta Kombinasi Search, Filter, Sort, dan Page Size

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup (dua fixture sesi, dipasang dan dipulihkan fixture BE; identitas dan nilai dirujuk lewat `Fixture.fixedAssetLicense.*`, berkas fixture belum ada, disiapkan tim FE; nilai pada langkah adalah nilai fixture itu):
  - Fixture 25 sesi (diperlukan TC-FA-LIC-294, 295, 296, dipasang di hook `before`): tabel Active Sessions berisi 25 baris pada client Paid Pre-setup #1 (fixture; berbeda dari Pre-setup #26 yang berisi lima baris). Fixture menyediakan satu kata kunci Search yang mengembalikan lebih dari 10 baris dan satu opsi Filter `Position` yang mengembalikan sedikitnya satu baris, keduanya disimpan sebagai kunci fixture.
  - Pre-setup #26 (diperlukan TC-FA-LIC-297, dipasang oleh langkah penghubung): tepat lima sesi cuplikan Rudi Hartono (Staff Gudang, Divisi Logistik, Safari), Dewi Lestari (Admin Aset, Divisi IT, Windows, Edge), Andi Pratama, Siti Rahma (Staff Keuangan, Divisi Keuangan, macOS, Safari), Budi Santoso (Supervisor Gudang, Divisi Logistik, Windows); Online Users 5/25.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Hook dan kemampuan suite (sesi API aktor, fixture BE pemulih): dinyatakan sekali di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang memasang fixture 25 sesi di hook `before`, menukarnya dengan fixture Pre-setup #26 pada langkah 29, dan memulihkan data di hook `after`.

## Test Steps

### TC-FA-LIC-294: Paginasi default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

1. Klik tab Concurrent User
2. Verifikasi footer menampilkan default 10 baris per halaman
3. Buka pilihan page size
4. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
5. Tutup pilihan page size tanpa mengubah, lalu ketik nomor halaman 2 pada input dan tekan Enter
6. Verifikasi input nomor halaman 2 langsung membuka halaman 2
7. Buka pilihan page size, lalu pilih 25
8. Verifikasi seluruh 25 baris tampil dalam satu halaman
9. Verifikasi tabel kembali ke halaman 1

### TC-FA-LIC-295: Nomor halaman tidak valid diabaikan; ganti sort tetap di halaman sekarang; ganti page size ke halaman 1

10. Buka pilihan page size, pilih 10, lalu pindah ke halaman 2
11. Ketik `0` pada input nomor halaman, tekan Enter
12. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2
13. Ketik `99` pada input nomor halaman, tekan Enter
14. Verifikasi input `99` diabaikan dan tabel tetap di halaman 2
15. Ketik `abc` pada input nomor halaman, tekan Enter
16. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2
17. Klik header kolom `User Name` untuk sort
18. Verifikasi mengganti sort tetap di halaman 2
19. Ganti page size menjadi 25
20. Verifikasi mengganti page size kembali ke halaman 1
21. Klik header kolom `User Name` hingga sort netral

### TC-FA-LIC-296: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

22. Buka pilihan page size, pilih 10, lalu pindah ke halaman 2
23. Ketik Search kata kunci fixture yang mengembalikan lebih dari 10 baris, tekan Enter
24. Verifikasi setelah Search tabel kembali ke halaman 1
25. Pindah ke halaman 2
26. Buka Filter Panel, pilih opsi fixture pada field `Position`, klik `[Apply]`
27. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
28. Klik `[Clear Field]`, lalu klik `[Apply]`, dan kosongkan isi kotak search, tekan Enter

### Pindah ke fixture sesi Pre-setup #26

29. Terapkan fixture sesi Pre-setup #26 lewat fixture BE
30. Klik menu License pada sidebar, lalu tab Concurrent User

### TC-FA-LIC-297: Kombinasi Search, Filter, Sort, dan paginasi bekerja bersamaan dan lepas secara independen

31. Ketik Search `Safari`, tekan Enter
32. Verifikasi tabel menampilkan: Rudi Hartono, Siti Rahma
33. Buka Filter Panel, pilih `Division` = `Divisi Logistik`, klik `[Apply]`
34. Verifikasi semua kontrol berlaku bersamaan: tabel menampilkan Rudi Hartono
35. Klik header kolom `Email` untuk sort, lalu ubah page size menjadi 25
36. Verifikasi mengganti kolom sort tidak mereset Search dan Filter: kotak Search tetap `Safari`, filter `Divisi Logistik` tetap, tabel menampilkan Rudi Hartono
37. Klik `[Clear Field]`, lalu klik `[Apply]` pada Filter Panel
38. Verifikasi Clear Filter tidak mereset Search dan Sort: kotak Search tetap `Safari`, indikator sort kolom `Email` tetap aktif, tabel menampilkan Rudi Hartono, Siti Rahma
39. Pilih `Division` = `Divisi Logistik`, klik `[Apply]`, lalu kosongkan isi kotak search, tekan Enter
40. Verifikasi mengosongkan Search tidak mereset Filter dan Sort: filter `Divisi Logistik` tetap, indikator sort kolom `Email` tetap aktif, tabel menampilkan Budi Santoso, Rudi Hartono
41. Ketik Search `Edge`, tekan Enter
42. Verifikasi hasil kosong dari Search dan Filter: tabel menampilkan empty state `No results found`
43. Klik `[Clear Field]`, lalu klik `[Apply]` pada Filter Panel
44. Verifikasi tabel pulih saat Filter dilepas: tabel menampilkan Dewi Lestari
45. Kosongkan isi kotak search, tekan Enter, lalu klik header kolom `Email` hingga sort netral

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup pilihan page size, memilih page size 10 dan pindah ke halaman 2 sebagai awal TC-FA-LIC-295 dan TC-FA-LIC-296, membersihkan Search, Filter, dan Sort di akhir blok (S-09), dan blok "Pindah ke fixture sesi Pre-setup #26" (menukar fixture lalu membuka ulang tab lewat sidebar yang mereset Search, Sort, dan Filter).
- Spec berada di atas sekitar 35 langkah. Alasan: seluruh blok adalah perilaku paginasi dan kombinasi kontrol satu tabel, kegagalan satu blok tidak membuat blok lain kehilangan makna, dan dua fixture dipakai berurutan dengan penukaran eksplisit.
- Temuan untuk QA: (1) TC-FA-LIC-294 menyebut tabel berisi 25 baris (fixture) padahal Pre-setup #26 berisi lima baris; spec memakai fixture 25 sesi terpisah. (2) TC-FA-LIC-294 butir d menyebut "halaman 2 (bila tersedia)" sesudah page size 25, ketika 25 baris sudah muat satu halaman; spec mengasersi halaman 2 pada page size 10 sebelum memilih 25. (3) TC-FA-LIC-295 dan TC-FA-LIC-296 menyebut "kolom" sort, "kata kunci yang mengembalikan >10 baris", dan "Apply Filter" tanpa nilai; spec memakai `User Name` dan nilai dari fixture 25 sesi. (4) TC-FA-LIC-297 langkah 5 mengosongkan filter lalu Search, sehingga Expected b ("mengosongkan Search tidak mereset Filter"), c ("mengganti kolom sort"), dan d ("hasil kosong dari Search dan Filter pulih") tidak dapat diamati dengan urutan itu; spec mengatur ulang urutan aksi dan menambah Search `Edge` untuk hasil kosong. Hasil kombinasi diturunkan dari oracle TC-FA-LIC-274, TC-FA-LIC-263, dan TC-FA-LIC-268 (Rudi Hartono dan Budi Santoso di Divisi Logistik; Dewi Lestari satu-satunya Edge).
