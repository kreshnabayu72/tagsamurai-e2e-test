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
  - Pre-setup #40 (diperlukan TC-FA-LIC-294, 295, 296, dipasang di hook `before`): Active Sessions berisi 25 sesi pada client Paid Pre-setup #1: lima sesi Pre-setup #26 ditambah 20 sesi fixture berdomain email `example.co.id`; Online Users 25/25; sesi fixture disisipkan BE setelah aktor login dan tidak ada login baru selama TC.
  - Test Data TC-FA-LIC-296 (nilai default Pre-setup #40): Search `example` (hasil lebih dari 10 baris) dan Filter `Device / OS` = `Windows`.
  - Pre-setup #26 (diperlukan TC-FA-LIC-297, dipasang oleh langkah penghubung): tepat lima sesi cuplikan Rudi Hartono (Staff Gudang, Divisi Logistik, Safari), Dewi Lestari (Admin Aset, Divisi IT, Windows, Edge), Andi Pratama, Siti Rahma (Staff Keuangan, Divisi Keuangan, macOS, Safari), Budi Santoso (Supervisor Gudang, Divisi Logistik, Windows); Online Users 5/25.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Hook dan kemampuan suite (sesi API aktor, fixture BE pemulih): dinyatakan sekali di `suite.md`.
- Kemampuan teknis (disediakan tim FE): mengirim tombol `Esc` ke browser (langkah 6).
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang memasang fixture 25 sesi di hook `before`, menukarnya dengan fixture Pre-setup #26 pada langkah 34, dan memulihkan data di hook `after`.

## Test Steps

### TC-FA-LIC-294: Paginasi default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

1. Klik tab Concurrent User
2. Verifikasi footer menampilkan page size 10 secara default
3. Verifikasi halaman 1 menampilkan 10 baris
4. Buka pilihan page size
5. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
6. Tutup pilihan page size dengan Esc
7. Verifikasi page size tetap 10
8. Ketik nomor halaman `2` pada input nomor halaman, tekan Enter
9. Verifikasi input nomor halaman 2 langsung membuka halaman 2
10. Verifikasi halaman 2 menampilkan 10 baris (baris ke-11 sampai ke-20)
11. Buka pilihan page size, lalu pilih `25`
12. Verifikasi seluruh 25 baris tampil dalam satu halaman
13. Verifikasi tabel kembali ke halaman 1

### TC-FA-LIC-295: Nomor halaman tidak valid diabaikan; ganti sort tetap di halaman sekarang; ganti page size ke halaman 1

14. Buka pilihan page size, pilih `10`, lalu pindah ke halaman 2
15. Ketik `0` pada input nomor halaman, tekan Enter
16. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2
17. Ketik `99` pada input nomor halaman, tekan Enter
18. Verifikasi input `99` diabaikan dan tabel tetap di halaman 2
19. Ketik `abc` pada input nomor halaman, tekan Enter
20. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2
21. Klik header kolom `User Name` untuk sort
22. Verifikasi mengganti sort tetap di halaman 2
23. Ganti page size menjadi `25`
24. Verifikasi mengganti page size kembali ke halaman 1
25. Klik header kolom `User Name` hingga sort netral

### TC-FA-LIC-296: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

26. Buka pilihan page size, pilih `10`, lalu pindah ke halaman 2
27. Ketik Search `example`, tekan Enter
28. Verifikasi setelah Search tabel kembali ke halaman 1
29. Pindah ke halaman 2
30. Buka Filter Panel, pada field `Device / OS` centang `Windows`, lalu klik `[Apply]`
31. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
32. Klik `[Clear Field]`, lalu klik `[Apply]`, dan kosongkan isi kotak search, tekan Enter

### Pindah ke fixture sesi Pre-setup #26

33. Klik ikon Filter untuk menutup panel
34. Terapkan fixture sesi Pre-setup #26 lewat fixture BE hingga berhasil tersimpan
35. Klik menu License pada sidebar, lalu tab Concurrent User

### TC-FA-LIC-297: Kombinasi Search, Filter, Sort, dan paginasi bekerja bersamaan dan lepas secara independen

36. Ketik Search `Divisi`, tekan Enter
37. Verifikasi tabel menampilkan: Rudi Hartono, Dewi Lestari, Siti Rahma, Budi Santoso
38. Verifikasi Andi Pratama tidak tampil (Division `—`)
39. Buka Filter Panel, pada field `Device / OS` centang `Windows` dan `Android`, lalu klik `[Apply]`
40. Verifikasi tabel menampilkan: Dewi Lestari, Budi Santoso
41. Verifikasi Filter Panel tetap terbuka
42. Klik header kolom `User Name` sekali
43. Ubah page size menjadi `25`
44. Verifikasi tabel menampilkan: Budi Santoso, Dewi Lestari
45. Verifikasi indikator Ascending pada `User Name`
46. Verifikasi page size 25
47. Verifikasi Search `Divisi` tidak berubah
48. Verifikasi Filter `Device / OS` `Windows` dan `Android` tidak berubah
49. Klik header kolom `Division` sekali
50. Verifikasi tabel menampilkan: Dewi Lestari, Budi Santoso
51. Verifikasi `User Name` kembali netral
52. Verifikasi indikator Ascending pada `Division`
53. Verifikasi Search `Divisi` tidak berubah
54. Verifikasi Filter `Device / OS` `Windows` dan `Android` tidak berubah
55. Pada Filter Panel yang masih terbuka, klik `[Clear Field]`, lalu klik `[Apply]`
56. Verifikasi tabel menampilkan: Dewi Lestari, Siti Rahma, Rudi Hartono, Budi Santoso
57. Verifikasi Search `Divisi` tetap aktif
58. Verifikasi Sort `Division` tetap aktif
59. Pada field `Device / OS` centang lagi `Windows` dan `Android`, lalu klik `[Apply]`
60. Kosongkan isi kotak search, tekan Enter
61. Verifikasi tabel menampilkan: Dewi Lestari, Budi Santoso, Andi Pratama
62. Verifikasi Rudi Hartono dan Siti Rahma tidak tampil
63. Verifikasi Filter tetap aktif
64. Verifikasi Sort `Division` Ascending tetap aktif
65. Ketik Search `Safari`, tekan Enter
66. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
67. Kosongkan isi kotak search, tekan Enter
68. Verifikasi tabel pulih otomatis menampilkan: Dewi Lestari, Budi Santoso, Andi Pratama
69. Verifikasi Filter tetap aktif
70. Verifikasi Sort `Division` Ascending tetap aktif
71. Klik `[Clear Field]`, lalu klik `[Apply]`
72. Klik header kolom `Division` hingga sort netral
73. Ubah page size menjadi `10`
74. Klik ikon Filter untuk menutup panel

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 14 dan 26 (memilih page size 10 dan pindah ke halaman 2 sebagai awal TC-FA-LIC-295 dan TC-FA-LIC-296), langkah 32 (membersihkan Filter dan Search; S-09), blok "Pindah ke fixture sesi Pre-setup #26" (langkah 33: menutup Filter Panel sebelum navigasi sidebar, S-03; langkah 34 dan 35: menukar fixture lalu membuka ulang tab lewat sidebar yang mereset Search, Sort, dan Filter), serta langkah 71 sampai 74 (memulihkan Filter, Sort `Division`, page size, dan panel; S-09). Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions.md §9.8), sehingga mengubah Filter dari panel itu tidak didahului membuka panel.
- Spec di atas 35 langkah (74 langkah nominal). Alasan: seluruh blok adalah perilaku paginasi dan kombinasi kontrol satu tabel, kegagalan satu blok tidak membuat blok lain kehilangan makna, dan dua fixture dipakai berurutan dengan penukaran eksplisit.
- Langkah 33 (S-03): Filter Panel dari TC-FA-LIC-296 ditutup dengan klik ikon Filter sebelum navigasi sidebar, agar langkah `Buka Filter Panel` di TC-FA-LIC-297 (langkah 39) membuka panel dari keadaan tertutup.
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-295 kolom sort `User Name` dipilih spec (TC menulis "klik header kolom untuk sort").
- Temuan untuk QA:
  - TC-FA-LIC-294, 295, dan 296 memuat precondition 25 sesi (Pre-setup #40), sedangkan TC-FA-LIC-297 memuat lima sesi Pre-setup #26; spec menukar fixture lewat fixture BE sebelum TC-FA-LIC-297. Pre-setup #40 menyatakan Online Users 25/25 (seat penuh) dan sesi fixture disisipkan BE setelah aktor login tanpa login baru selama TC; perilaku seat penuh tidak diuji.
  - TC-FA-LIC-295 menyebut "kolom" sort tanpa nilai; spec memakai `User Name`.
  - TC-FA-LIC-294, 295, 296, dan 297 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
