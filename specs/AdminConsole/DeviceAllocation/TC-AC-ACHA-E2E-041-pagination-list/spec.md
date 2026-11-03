---
id: TC-AC-ACHA-E2E-041-pagination-list
title: "Pagination pada List Device Allocation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-349
  - TC-AC-ACHA-350
  - TC-AC-ACHA-351
  - TC-AC-ACHA-352
  - TC-AC-ACHA-353
  - TC-AC-ACHA-354
  - TC-AC-ACHA-355
  - TC-AC-ACHA-356
coverage:
  web: automated
---

# Pagination pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-11: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Kemampuan teknis (disediakan tim FE): tidak ada kemampuan tambahan selain input nomor halaman, tombol next dan previous, dan dropdown Page size pada tabel.
- State yang diubah: Page size dikembalikan ke `10` dan Search dikosongkan di akhir spec; halaman aktif dikembalikan ke halaman 1.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-349: Page size default dan opsi

1. Verifikasi tabel menampilkan default 10 data per halaman
2. Verifikasi pagination menampilkan tiga halaman
3. Klik dropdown Page size
4. Verifikasi opsi Page size tepat `10`, `25`, `50`, dan `100`
5. Verifikasi tidak ada opsi "All"
6. Tutup dropdown Page size

### TC-AC-ACHA-356: Navigasi next dan previous

7. Verifikasi tombol previous disabled di halaman 1
8. Klik tombol next halaman
9. Verifikasi tabel berpindah satu halaman ke halaman 2
10. Klik tombol next halaman
11. Verifikasi tabel berada di halaman 3 (halaman terakhir)
12. Verifikasi tombol next disabled di halaman terakhir
13. Klik tombol previous
14. Verifikasi tabel berpindah satu halaman ke halaman 2
15. Ketik `1` pada input nomor halaman, tekan Enter

### TC-AC-ACHA-352: Lompat halaman lewat input

16. Ketik `3` pada input nomor halaman, tekan Enter
17. Verifikasi tabel melompat langsung ke halaman 3 dengan 10 baris terakhir dan baris terakhir `HALC-20260901-00001`
18. Ketik `1` pada input nomor halaman, tekan Enter
19. Verifikasi tabel berada di halaman 1

### TC-AC-ACHA-353: Nomor halaman tidak valid diabaikan

20. Ketik `2` pada input nomor halaman, tekan Enter
21. Verifikasi tabel berada di halaman 2
22. Ketik `0` pada input nomor halaman, tekan Enter
23. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2
24. Ketik `4` pada input nomor halaman, tekan Enter
25. Verifikasi input `4` diabaikan dan tabel tetap di halaman 2
26. Ketik `abc` pada input nomor halaman, tekan Enter
27. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2
28. Ketik `-1` pada input nomor halaman, tekan Enter
29. Verifikasi input `-1` diabaikan dan tabel tetap di halaman 2
30. Ketik `1` pada input nomor halaman, tekan Enter

### TC-AC-ACHA-355: Search mereset ke halaman 1

31. Ketik `2` pada input nomor halaman, tekan Enter
32. Verifikasi tabel berada di halaman 2
33. Ketik Search `Budi`, tekan Enter
34. Verifikasi Search `Budi` mengembalikan tabel ke halaman 1
35. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
36. Ketik `2` pada input nomor halaman, tekan Enter
37. Verifikasi tabel berada di halaman 2
38. Klik ikon `(✕)` pada Search, tekan Enter pada input kosong
39. Verifikasi mengosongkan Search mengembalikan tabel ke halaman 1
40. Klik `(←)` pada kotak Search

### TC-AC-ACHA-354: Mengganti Page size kembali ke halaman 1

41. Ketik `3` pada input nomor halaman, tekan Enter
42. Verifikasi tabel berada di halaman 3
43. Ubah Page size menjadi `25`
44. Verifikasi mengganti Page size mengembalikan tabel ke halaman 1
45. Ubah Page size menjadi `10`

### TC-AC-ACHA-350: Page size 25 membagi 30 baris menjadi 25 dan 5

46. Pilih Page size `25`
47. Verifikasi halaman 1 memuat 25 baris
48. Klik halaman 2
49. Verifikasi halaman 2 memuat 5 baris
50. Verifikasi pagination menampilkan dua halaman

### TC-AC-ACHA-351: Page size 50 dan 100

51. Pilih Page size `50`
52. Verifikasi Page size `50` menampilkan seluruh 30 baris pada satu halaman tanpa halaman berikutnya
53. Pilih Page size `100`
54. Verifikasi Page size `100` menampilkan seluruh 30 baris pada satu halaman tanpa halaman berikutnya
55. Ubah Page size menjadi `10`

## Notes

- Ukuran spec (55 langkah, di atas 35 langkah): delapan TC Pagination satu topik memakai satu dataset Seed List; tiap Expected (jumlah baris, tombol halaman, nomor halaman) menjadi `Verifikasi` sendiri (S-01) dan TC saling memulihkan state (Page size, halaman 1).
- Pemisahan topik satu dataset (prinsip 1): Search, Filter Panel, Sort, Setup Column, kombinasi kontrol, dan Pagination List memakai dataset Seed List yang sama (Pre-setup #48) dan dipisah menjadi spec 036 sampai 041 karena gabungannya jauh melewati batas ukuran (spec Pagination ini saja 55 langkah). Pemisahan per kontrol dipertahankan karena tiap spec memulai dari kondisi default yang dipulihkan di akhir spec dan di hook `after` (Page size 10 dan halaman 1), sehingga kegagalan keras satu spec tidak membuat spec lain kehilangan makna; di dalam spec ini tiap TC mengakhiri dengan pemulihan state (S-09) dan tidak bergantung pada hasil TC lain, sehingga spec tetap satu (tanpa pemisah nyata: akun, kelas harness, dan dataset sama).
- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-6). Seluruh TC primer spec ini (TC-AC-ACHA-349 sampai 356) dikerjakan di sini.
- Urutan dalam spec menyimpang dari urutan nomor TC: TC-AC-ACHA-349 (screening), TC-AC-ACHA-356, TC-AC-ACHA-352, TC-AC-ACHA-353, TC-AC-ACHA-355, TC-AC-ACHA-354, lalu TC-AC-ACHA-350 dan TC-AC-ACHA-351 yang mengubah Page size di akhir, supaya TC lain berjalan pada Page size default 10 (tiga halaman).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): kembali ke halaman 1 lewat input nomor halaman sesudah TC-AC-ACHA-356 dan TC-AC-ACHA-353; penutupan dropdown Page size; penutupan Search `(←)` di akhir TC-AC-ACHA-355; Page size kembali `10` (akhir TC-AC-ACHA-354 dan TC-AC-ACHA-351).
- Asersi tambahan (S-03): `Verifikasi` tabel berada di halaman 2 atau 3 sebelum aksi yang diuji (TC-AC-ACHA-353, 355, 354) supaya klausa "tetap" dan "kembali ke halaman 1" bermakna; pada TC-AC-ACHA-356 tombol next disabled diamati di halaman 3 (halaman terakhir Seed List pada Page size 10).
- Temuan untuk QA:
  - TC-AC-ACHA-355 langkah uji ketiga ("Pindah ke halaman 2 lagi lalu hapus Search") tidak dapat dijalankan dengan Search `Budi`: hasil `Budi` hanya 6 baris sehingga hanya satu halaman pada Page size 10. Spec memakai Search `Sejahtera` (16 baris, dua halaman) untuk paruh kedua; paruh pertama tetap `Budi`.
  - TC-AC-ACHA-353 mensyaratkan tabel berada di halaman 2 tanpa langkah menuju halaman itu; spec menambah langkah pindah ke halaman 2 (S-14).
