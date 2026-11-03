---
id: TC-AC-ACHA-E2E-033-resubmit-dirty-guard-dan-double-submit
title: "Resubmit: Dirty Guard, Clear Field, Dialog Unsaved Changes, dan Double-Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-247
  - TC-AC-ACHA-248
  - TC-AC-ACHA-249
  - TC-AC-ACHA-250
  - TC-AC-ACHA-255
  - TC-AC-ACHA-470
  - TC-AC-ACHA-471
coverage:
  web: automated
---

# Resubmit: Dirty Guard, Clear Field, Dialog Unsaved Changes, dan Double-Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Member Distributor toggle ON MB_ON (Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Nama env baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Data Pre-setup yang dibaca: Distributor PT Global Distribusi (#3), Client PT Sejahtera Logistik (#7), kantong PT Global Distribusi saldo $20,000.00 (#16), harga PT ABC (#14).
- Data seed milik spec (seeding API di hook `before`, disediakan tim FE/BE; Allocation ID ditangkap saat runtime): transaksi Canceled manual milik MB_ON dengan atribut Pre-setup #52 (BLE Gateway, Quantity 50, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch lama`, Total Cost $100.00). Nilai literal `Batch lama` diasersi TC sehingga tidak bersuffix (pengecualian S-12 nama literal, Lampiran A butir A-11). Transaksi lama ini tetap Canceled sampai blok TC-255.
- Kemampuan teknis (disediakan tim FE/BE): fixture API Pre-setup #20 untuk membaca saldo dan Reserved kantong PT Global Distribusi serta total baris List; `Spectra.intercept()` untuk menahan respons Submit TC-255 (hanya untuk mengamati Saving state, bukan kegagalan; intercept dilepas segera setelah asersi Saving state). Penahanan respons adalah pilihan spec karena Saving state hanya teramati selagi respons belum kembali.
- State global: saldo dan Reserved kantong PT Global Distribusi berubah oleh TC-255 (dibersihkan fixture di hook `after`); suite berjalan serial (`parallel: false`).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Device Allocation true untuk akun aktor, sesi API aktor, fixture API Pre-setup #20.

## Test Steps

### Tutup form Resubmit yang belum diubah (TC-AC-ACHA-247)

1. Catat total baris List (B) dan saldo kantong PT Global Distribusi (S0) lewat fixture API
2. Ketik Search Allocation ID transaksi Canceled seed milik MB_ON (Pre-setup #52), tekan Enter
3. Klik `Resubmit` pada transaksi Canceled milik MB_ON
4. Klik `[×]` tanpa mengubah apa pun
5. Verifikasi List tampil
6. Verifikasi dialog Unsaved Changes tidak muncul

### Resubmit yang dikembalikan identik dianggap bersih (TC-AC-ACHA-249)

7. Klik `Resubmit` pada transaksi Canceled milik MB_ON
8. Ubah Quantity menjadi `60`
9. Ubah Quantity kembali menjadi `50`
10. Klik `[×]`
11. Verifikasi List tampil
12. Verifikasi dialog Unsaved Changes tidak muncul

### Clear Field pada Resubmit (TC-AC-ACHA-250)

13. Klik `Resubmit` pada transaksi Canceled milik MB_ON
14. Klik `[Clear Field]`
15. Verifikasi Category dikosongkan
16. Verifikasi Type dikosongkan
17. Verifikasi Client dikosongkan
18. Verifikasi Quantity dikosongkan
19. Verifikasi Notes dikosongkan
20. Verifikasi Pay From `PT ABC (Principal)` pre-filled disabled dan From tidak berubah
21. Verifikasi tidak ada dialog
22. Verifikasi form tetap terbuka
23. Klik `[×]`
24. Verifikasi dialog Unsaved Changes: judul "Unsaved Changes", body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` dan `[Leave]`
25. Klik `[Leave]`

### Dialog Unsaved Changes, Cancel, dan Leave (TC-AC-ACHA-248, TC-AC-ACHA-470, TC-AC-ACHA-471)

26. Klik `Resubmit` pada transaksi Canceled milik MB_ON
27. Ubah Quantity menjadi `60`
28. Klik `[×]`
29. Verifikasi dialog Unsaved Changes: judul "Unsaved Changes", body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` dan `[Leave]` (severity warning)
30. Klik `[Cancel]` pada dialog
31. Verifikasi dialog Unsaved Changes tertutup
32. Verifikasi form Resubmit tetap terbuka
33. Verifikasi Quantity `60` dipertahankan
34. Verifikasi Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Notes `Batch lama` tetap terisi
35. Klik `[×]`
36. Klik `[Leave]` pada dialog Unsaved Changes
37. Verifikasi dialog Unsaved Changes tertutup
38. Verifikasi form Resubmit tertutup tanpa menyimpan
39. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
40. Verifikasi List menampilkan sedikitnya satu baris
41. Verifikasi total baris sama dengan B (tidak ada transaksi baru)
42. Verifikasi saldo kantong PT Global Distribusi sama dengan S0
43. Ketik Search Allocation ID transaksi lama (seed Pre-setup #52), tekan Enter
44. Buka menu row action `⋯` transaksi lama
45. Verifikasi transaksi lama tetap Status `Canceled`
46. Verifikasi `Resubmit` tetap tersedia pada menu row action
47. Tutup menu dengan Esc

### Double-submit Resubmit (TC-AC-ACHA-255)

48. Tahan respons Submit lewat intercept
49. Klik `Resubmit` pada transaksi Canceled milik MB_ON
50. Klik `[Submit]` dua kali cepat
51. Verifikasi `[Submit]` masuk Saving state
52. Lepas tahanan respons dan hapus intercept
53. Tunggu aksi selesai (form Resubmit tertutup)
54. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
55. Verifikasi total baris List bertambah tepat satu dari B (hanya satu transaksi baru dibuat)

## Notes

- Langkah penghubung (S-03, R-16): Search Allocation ID transaksi seed (sesudah baseline B dicatat dalam keadaan Search kosong) dan pembersihan Search (klik `(←)`, lalu muat ulang halaman (F5)) sebelum asersi total baris, mencatat baseline, menutup menu dengan Esc, menahan dan melepas respons, dan menunggu form tertutup tidak punya `Verifikasi`. `Verifikasi` dialog Unsaved Changes pada blok TC-250 dan `Leave` pada akhir blok dipakai karena form dirty ditutup deterministik (S-08).
- Satu form dirty dipakai berurutan untuk TC-248, TC-470, dan TC-471 (Quantity `60`): dialog diamati (TC-248), `[Cancel]` (TC-470), lalu `[×]` dan `[Leave]` (TC-471), sehingga jumlah buka form tidak melebihi jumlah penutupan (prinsip 6). Asersi "tidak ada transaksi baru" milik TC-470 butir c dan TC-471 butir b diperiksa sekali setelah form ditutup; tidak ada aksi yang dapat membuat transaksi di antara keduanya. TC-249 memakai form sendiri karena menguji nilai kembali identik.
- Aksi pembuat data (TC-255) ditaruh paling akhir (prinsip 3 butir 5 dan 7).
- Alasan di atas 35 langkah: semua blok satu topik (dirty guard dan Saving state pada form Resubmit), akun sama, tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-255 tidak menyatakan cara mengamati Saving state; spec menahan respons Submit lewat intercept (bukan kelas b, prinsip 13b).
  - TC-247 dan TC-249: "tanpa dialog" diasersi dengan List tampil dan dialog tidak muncul; TC tidak menyediakan anchor selain List.
  - Post Condition TC-255 (Wallet, Approvals Active Tab, Dashboard, notifikasi) tidak punya langkah observasi di TC sehingga tidak diasersi; Expected TC-255 tidak menyebut toast.
  - TC-470 dan TC-471 mengulang langkah buka dan ubah TC-248; spec menggabungkannya pada satu form dirty (lihat Notes).
