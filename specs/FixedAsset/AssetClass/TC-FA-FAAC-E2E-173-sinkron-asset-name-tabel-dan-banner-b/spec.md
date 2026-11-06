---
id: TC-FA-FAAC-E2E-173-sinkron-asset-name-tabel-dan-banner-b
title: "Sinkronisasi Move, Unassign, dan Asset Name Baru: Kolom Asset Names dan Assets serta Banner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-574
  - TC-FA-FAAC-575
  - TC-FA-FAAC-576
  - TC-FA-FAAC-577
coverage:
  web: automated
---

# Sinkronisasi Move, Unassign, dan Asset Name Baru: Kolom Asset Names dan Assets serta Banner

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`) memiliki Asset Name `City Car` dan `Bumper Stock` (0 aset aktif) pada TC-574, `City Car` (2 aset aktif) dan `Spare Tire Rack` (0 aset aktif) pada TC-575 (Assets = 2), dan `Rear Rack` (0 aset aktif) pada TC-576; `Machinery` (`MACHINERY`) dengan Asset Names = 1; pada TC-576 semua Asset Name ter-assign sehingga banner tidak tampil; pada TC-577 banner menampilkan hitungan awal H.
- Nilai form Create Asset Name valid TC-577 (TC hanya menyebut nama dan Category; field wajib lain menurut form Settings > Asset Master > Asset Name): Asset Name `Trolley Jack`; Category `Machinery > Warehouse`; TAG Type `QR`; Brand dan UoM satu opsi master yang tersedia (nilai tepatnya disediakan fixture BE); field opsional dikosongkan.
- Keadaan awal dinamis: `LT-VEH` memiliki `City Car` dan `Bumper Stock` pada TC-574 dan `City Car` dan `Spare Tire Rack` pada TC-575 (precondition masing-masing TC); fixture BE menyetel keadaan itu pada langkah 1 dan 19 karena TC-574 memindahkan `Bumper Stock` ke `MACHINERY` sebelum TC-575. Untuk TC-576 (precondition: tidak ada Asset Name tanpa Asset Class dan `LT-VEH` memiliki `Rear Rack`) fixture BE menyetelnya pada langkah 30 karena hitungan banner bergantung pada data bersama client. Untuk TC-577 (precondition: banner menampilkan hitungan awal H dan `Trolley Jack` belum ada) fixture BE menyetelnya pada langkah 46. Fixture BE memulihkan keadaan semula di hook `after`.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Bumper Stock kembali ke LT-VEH; Spare Tire Rack dan Rear Rack kembali ter-assign ke LT-VEH; Asset Name Trolley Jack dihapus. Banner Asset Name tanpa Asset Class bergantung pada data bersama client sehingga suite berjalan serial.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-574: Move Asset Name tanpa aset aktif memperbarui Asset Names pada kedua Asset Class

1. Setel keadaan awal lewat fixture BE: `LT-VEH` memiliki Asset Name `City Car` dan `Bumper Stock` (0 aset aktif) (precondition TC-574)
2. Buka Fixed Asset > Settings > Accounting > tab Asset Class
3. Ketik Search `LT-VEH`, tekan Enter
4. Catat nilai Assets baris `LT-VEH` (L0)
5. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
6. Catat nilai Assets baris `MACHINERY` (M0)
7. Ganti isi kotak search dengan `LT-VEH`, tekan Enter
8. Klik link Class Code `LT-VEH` di tabel
9. Klik tab `Asset Names`
10. Klik ikon `⋯` pada baris `Bumper Stock`, lalu pilih `Move`
11. Pilih `Destination Asset Class` = `MACHINERY – Machinery`, lalu klik `[Move]`
12. Tunggu aksi selesai
13. Klik kembali ke tabel Asset Class
14. Verifikasi baris `LT-VEH` menampilkan Asset Names = 1
15. Verifikasi kolom Assets baris `LT-VEH` tidak berubah dari L0 (Asset Name tanpa aset aktif)
16. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
17. Verifikasi baris `MACHINERY` menampilkan Asset Names = 2
18. Verifikasi kolom Assets baris `MACHINERY` tidak berubah dari M0 (Asset Name tanpa aset aktif)

### TC-FA-FAAC-575: Unassign Asset Name memperbarui Asset Names dan Assets pada Asset Class

19. Setel keadaan awal lewat fixture BE: `LT-VEH` memiliki Asset Name `City Car` (2 aset aktif) dan `Spare Tire Rack` (0 aset aktif) (precondition TC-575)
20. Buka Fixed Asset > Settings > Accounting > tab Asset Class
21. Ketik Search `LT-VEH`, tekan Enter
22. Verifikasi baris `LT-VEH` menampilkan Asset Names = 2 dan Assets = 2 (keadaan awal)
23. Klik link Class Code `LT-VEH` di tabel
24. Klik tab `Asset Names`
25. Klik ikon `⋯` pada baris `Spare Tire Rack`, lalu pilih `Unassign`
26. Klik `[Unassign]`
27. Tunggu aksi selesai
28. Klik kembali ke tabel Asset Class
29. Verifikasi baris `LT-VEH` menampilkan Asset Names = 1 dan Assets = 2 (tidak berubah karena Asset Name yang dilepas tanpa aset aktif)

### TC-FA-FAAC-576: Unassign Asset Name menambah hitungan banner Asset Name tanpa Asset Class

30. Setel keadaan awal lewat fixture BE: tidak ada Asset Name tanpa Asset Class dan `LT-VEH` memiliki Asset Name `Rear Rack` (0 aset aktif) (precondition TC-576)
31. Buka Fixed Asset > Settings > Accounting > tab Asset Class
32. Verifikasi Table Tools tabel Asset Class tampil
33. Verifikasi banner `Asset Name tanpa Asset Class` tidak tampil (semua Asset Name ter-assign)
34. Ketik Search `LT-VEH`, tekan Enter
35. Klik link Class Code `LT-VEH` di tabel
36. Klik tab `Asset Names`
37. Klik ikon `⋯` pada baris `Rear Rack`, lalu pilih `Unassign`
38. Klik `[Unassign]`
39. Tunggu aksi selesai
40. Kembali ke tabel Asset Class lewat Breadcrumb
41. Verifikasi banner Alert warning `1 asset name has no asset class and will not be depreciated.` tampil
42. Klik `[View asset names]`
43. Ketik Search `Rear Rack`, tekan Enter
44. Verifikasi dialog `Asset Names Without Asset Class` memuat `Rear Rack`
45. Tutup dialog `Asset Names Without Asset Class`

### TC-FA-FAAC-577: Asset Name baru di Settings > Asset Master > Asset Name masuk banner, D-23, dan picker Assign

46. Setel keadaan awal lewat fixture BE: banner Asset Name tanpa Asset Class menampilkan hitungan awal H dan Asset Name `Trolley Jack` belum ada (precondition TC-577)
47. Buka Fixed Asset > Settings > Accounting > tab Asset Class
48. Catat hitungan awal banner (H)
49. Buka Settings > Asset Master > Asset Name
50. Buat Asset Name `Trolley Jack` dengan Category `Machinery > Warehouse` dan nilai form valid di Prerequisites
51. Tunggu aksi selesai
52. Buka Fixed Asset > Settings > Accounting > tab Asset Class
53. Verifikasi banner naik satu dari H menjadi H+1
54. Klik `[View asset names]`
55. Ketik Search `Trolley Jack`, tekan Enter
56. Verifikasi `Trolley Jack` tampil pada dialog `Asset Names Without Asset Class`
57. Tutup dialog
58. Ketik Search `LT-VEH`, tekan Enter
59. Klik link Class Code `LT-VEH` di tabel
60. Klik tab `Asset Names`
61. Klik tombol `+ Assign Asset Names`
62. Ketik Search `Trolley Jack`, tekan Enter
63. Verifikasi `Trolley Jack` tampil pada picker Assign dengan Current Class `—`
64. Klik `[Cancel]` pada dialog Assign

## Notes

1. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena empat TC sinkronisasi Move, Unassign, dan Asset Name baru yang tiap bloknya memuat keadaan awal, aksi, dan dua asersi kolom; semua TC satu topik dan tiap blok berdiri sendiri dengan seed sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 4, 6, dan 48 (pencatatan nilai awal sebagai baseline selisih), langkah 1, 19, 30, dan 46 (fixture BE menyetel keadaan awal dinamis TC-574, TC-575, TC-576, dan TC-577, S-14), langkah "Tunggu aksi selesai" (12, 27, 39, 51) sesudah `[Move]`, `[Unassign]`, dan pembuatan Asset Name yang hasilnya tidak diasersi langsung sebelum pindah surface (8b butir 8), Search kode di tabel (langkah 3, 5, 7, 16, 21, 34, dan 58; tabel Asset Class memuat lebih dari 25 baris, dua baris yang harus terlihat sekaligus diganti Search per baris) dan di dialog serta picker untuk menemukan baris target (R-16 dan R-22), menutup dialog, dan kembali ke layar awal.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: (a) TC-574 tidak menyebut nilai Assets awal; spec mencatatnya sebagai baseline untuk asersi "tidak berubah". (b) TC-576 dan TC-577 tidak menyebut hitungan awal banner kecuali "tidak tampil" dan "H"; spec mengikuti. (c) TC-577 tidak menyebut field wajib lain Asset Name `Trolley Jack`; spec memakai nilai yang tertulis di Prerequisites (TAG Type, Brand, dan UoM mengikuti field wajib form Asset Name). (d) Precondition TC-575 dan TC-574 memakai Asset Class yang sama dengan nilai awal berbeda; keadaan awal per TC disetel fixture BE (Keadaan awal dinamis, langkah 1, 19, 30, dan 46).
