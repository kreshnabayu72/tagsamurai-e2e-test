---
id: TC-FA-FAAC-E2E-172-sinkron-asset-name-tabel-dan-banner-a
title: "Sinkronisasi Assign, Move, dan Banner: Kolom Asset Names dan Assets, Badge Current Class, dan Hitungan Banner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-570
  - TC-FA-FAAC-571
  - TC-FA-FAAC-572
  - TC-FA-FAAC-573
coverage:
  web: automated
---

# Sinkronisasi Assign, Move, dan Banner: Kolom Asset Names dan Assets, Badge Current Class, dan Hitungan Banner

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`) memiliki Asset Name `City Car` (2 aset aktif; kolom Asset Names = 1 dan Assets = 2 pada TC-570) dan `Panel Van` (4 aset aktif; pada TC-573 `LT-VEH` Asset Names = 2, Assets = 6); Asset Name tanpa Asset Class `Pickup Truck 2` (3 aset aktif), `Hand Cart 2`, dan tepat 3 Asset Name tanpa Asset Class `Hand Truck Pro`, `Drum Dolly Pro`, `Sack Truck` (0 aset aktif) pada TC-572; `Machinery` (`MACHINERY`) dengan Asset Names = 1 dan Assets = 1.
- Keadaan awal dinamis: precondition TC-570 (`LT-VEH` memiliki `City Car`) disetel fixture BE pada langkah 1; selain itu `LT-VEH` memiliki `City Car` dan `Panel Van` menurut precondition TC-573; fixture BE menyetelnya pada langkah 42 sebelum blok TC-573, karena TC-570 sampai TC-572 sudah meng-assign `Pickup Truck 2`, `Hand Cart 2`, dan `Hand Truck Pro` ke `LT-VEH`. Banner pada blok TC-572 memerlukan tepat 3 Asset Name tanpa Asset Class (`Hand Truck Pro`, `Drum Dolly Pro`, `Sack Truck`, 0 aset aktif) menurut precondition TC-572; fixture BE menyetelnya pada langkah 30 karena hitungan banner bergantung pada data bersama client (TC-35 dan TC-579 memakai keadaan lain). Fixture BE memulihkan keadaan semula di hook `after`.
- Move pada TC-573 memakai Effective From bulan berjalan menurut zona waktu General Settings (NC-11); jam server dan jam browser tidak digeser spec ini.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Pickup Truck 2, Hand Cart 2, dan Hand Truck Pro kembali tanpa Asset Class; Panel Van kembali ke LT-VEH. Banner Asset Name tanpa Asset Class bergantung pada data bersama client sehingga suite berjalan serial.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-570: Assign Asset Name memperbarui kolom Asset Names dan Assets pada tabel Asset Class

1. Setel keadaan awal lewat fixture BE: `LT-VEH` memiliki Asset Name `City Car` (precondition TC-570)
2. Ketik Search `LT-VEH`, tekan Enter
3. Verifikasi baris `LT-VEH` menampilkan Asset Names = 1 dan Assets = 2 (keadaan awal)
4. Klik link Class Code `LT-VEH` di tabel
5. Klik tab `Asset Names`
6. Klik tombol `+ Assign Asset Names`
7. Centang `Pickup Truck 2`
8. Klik `[Assign]`
9. Tunggu aksi selesai
10. Klik kembali ke tabel Asset Class
11. Verifikasi baris `LT-VEH` menampilkan Asset Names = 2 dan Assets = 5

### TC-FA-FAAC-571: Asset Name yang baru di-assign menampilkan badge Current Class di picker Asset Class lain

12. Klik link Class Code `LT-VEH` di tabel
13. Klik tab `Asset Names`
14. Klik tombol `+ Assign Asset Names`
15. Centang `Hand Cart 2`
16. Klik `[Assign]`
17. Tunggu aksi selesai
18. Kembali ke tabel Asset Class lewat Breadcrumb
19. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
20. Klik link Class Code `MACHINERY` di tabel
21. Klik tab `Asset Names`
22. Klik tombol `+ Assign Asset Names`
23. Hilangkan centang `Without asset class only`
24. Ketik Search `Hand Cart 2`, tekan Enter
25. Verifikasi `Hand Cart 2` tampil di picker `MACHINERY` dengan badge Current Class `Light Vehicles`
26. Klik `[Cancel]` pada dialog Assign
27. Buka Settings > Asset Master > Asset Name
28. Verifikasi sedikitnya satu kolom Asset Name lain tampil pada daftar
29. Verifikasi daftar Asset Name tidak memiliki field Asset Class (Asset Class hanya terlihat dari tab Asset Names dan picker)

### TC-FA-FAAC-572: Assign Asset Name mengurangi hitungan banner Asset Name tanpa Asset Class

30. Setel keadaan awal lewat fixture BE: tepat 3 Asset Name tanpa Asset Class, yaitu `Hand Truck Pro`, `Drum Dolly Pro`, dan `Sack Truck` (precondition TC-572)
31. Buka Fixed Asset > Settings > Accounting > tab Asset Class
32. Verifikasi banner tab `Asset Class`: `3 asset names have no asset class and will not be depreciated.`
33. Ketik Search `LT-VEH`, tekan Enter
34. Klik link Class Code `LT-VEH` di tabel
35. Klik tab `Asset Names`
36. Klik tombol `+ Assign Asset Names`
37. Centang `Hand Truck Pro`
38. Klik `[Assign]`
39. Tunggu aksi selesai
40. Kembali ke tabel Asset Class lewat Breadcrumb
41. Verifikasi banner: `2 asset names have no asset class and will not be depreciated.`

### TC-FA-FAAC-573: Move Asset Name dengan aset aktif memperbarui Asset Names dan Assets pada kedua Asset Class

42. Setel keadaan awal lewat fixture BE: `LT-VEH` memiliki Asset Name `City Car` dan `Panel Van` (precondition TC-573)
43. Buka Fixed Asset > Settings > Accounting > tab Asset Class
44. Ketik Search `MACHINERY`, tekan Enter
45. Verifikasi baris `MACHINERY` menampilkan Asset Names = 1 dan Assets = 1 (keadaan awal)
46. Ganti isi kotak search dengan `LT-VEH`, tekan Enter
47. Verifikasi baris `LT-VEH` menampilkan Asset Names = 2 dan Assets = 6 (keadaan awal)
48. Klik link Class Code `LT-VEH` di tabel
49. Klik tab `Asset Names`
50. Klik ikon `⋯` pada baris `Panel Van`, lalu pilih `Move`
51. Pilih `Destination Asset Class` = `MACHINERY – Machinery`, biarkan Effective From bulan berjalan, lalu klik `[Move]`
52. Tunggu aksi selesai
53. Klik kembali ke tabel Asset Class
54. Verifikasi baris `LT-VEH` menampilkan Asset Names = 1 dan Assets = 2
55. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
56. Verifikasi baris `MACHINERY` menampilkan Asset Names = 2 dan Assets = 5
57. Verifikasi perubahan berlaku langsung saat Move dikonfirmasi, bukan terjadwal: nilai dua baris sudah berubah tanpa menunggu penerapan versi

## Notes

1. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena empat TC sinkronisasi Assign dan Move yang tiap bloknya memuat keadaan awal, aksi, dan dua asersi kolom; semua TC satu topik dan tiap blok berdiri sendiri dengan seed sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 30, dan 42 (fixture BE menyetel keadaan awal TC-570 dan keadaan awal dinamis TC-572 dan TC-573, S-14), awal tiap blok TC (kembali ke layar awal), Search kode di tabel (langkah 2, 19, 33, 44, 46, dan 55) dan di picker untuk menemukan baris target (R-16: tabel Asset Class memuat lebih dari 25 baris, dua baris yang harus terlihat sekaligus diganti Search per baris), menutup dialog Assign, serta langkah "Tunggu aksi selesai" (9, 17, 39, 52) sesudah `[Assign]` dan `[Move]` yang hasilnya tidak diasersi langsung sebelum kembali ke tabel (8b butir 8).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: (a) Precondition TC-570 dan TC-573 memakai nilai kolom Asset Names dan Assets awal yang berbeda untuk Asset Class yang sama (`LT-VEH`); spec memakai seed per TC dan keduanya ditulis di Prerequisites. (b) Expected c TC-573 "Perubahan berlaku langsung saat Confirm" tidak punya indikator UI terpisah; spec mengasersinya lewat nilai kolom yang berubah tepat setelah Move. (c) TC-571 mengasersi Asset Name di picker tanpa menyebut paginasi picker; spec mencari lewat Search (R-22). (d) TC-570 dan TC-573 mencantumkan keadaan awal di Precondition; spec mengasersinya sebagai langkah `Verifikasi` keadaan awal sebelum aksi (S-14).
5. Keadaan awal dinamis (S-14): TC-572 membutuhkan tepat 3 Asset Name tanpa Asset Class; langkah 30 menyetelnya lewat fixture BE sehingga `Verifikasi` banner pada langkah 32 tidak bergantung pada data global. TC-573 membutuhkan `LT-VEH` dengan `City Car` dan `Panel Van` (Asset Names = 2, Assets = 6); langkah 42 menyetelnya lewat fixture BE karena keadaan sesudah TC-570 sampai TC-572 berbeda, sehingga `Verifikasi` keadaan awal pada langkah 47 membaca keadaan yang disetel itu, bukan sisa blok sebelumnya. Ketiga langkah fixture bukan bagian TC dan tanpa `Verifikasi`.
