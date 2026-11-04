---
id: TC-FA-COA-E2E-053-setup-column-tabel-pin-hidden-reset-to-default-dan-tutup-tanpa-save
title: "Setup Column Tabel: Pin Hidden, Reset to Default, dan Tutup Tanpa Save"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-82
  - TC-FA-COA-83
  - TC-FA-COA-192
  - TC-FA-COA-195
  - TC-FA-COA-196
coverage:
  web: automated
---

# Setup Column Tabel: Pin Hidden, Reset to Default, dan Tutup Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun pengamat TC-82 (user lain di jendela privat, hanya membaca): Read Only `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_PASSWORD` (terdaftar). Hook `before` spec ini hanya login pengamat dan membuka jendela privat tanpa membuka halaman Chart of Accounts (halaman dibuka pada langkah 17 sesudah perubahan disimpan); jendela privat ditutup di hook `after` (P-6). Kemampuan sesi kedua (jendela privat dengan sesi login terpisah) disediakan tim FE.
- Data: tabel Chart of Accounts client default berisi akun Pre-setup dan akun lain hasil seed (lihat Seed dan pemulihan di `suite.md`); spec hanya mengamati kolom tabel dan tidak menyebut akun tertentu.
- Konfigurasi kolom awal: default modul (Active, Account Code, Account Name, Function, Used By, Last Used in Journal tampil; Modified By dan Last Updated hidden; tanpa kolom terpin).
- State yang diubah spec: konfigurasi kolom tersimpan lewat `[Save]` (langkah 4, 14, 23, 26, 36). Dipulihkan dengan langkah eksplisit 9 sampai 10, 21 sampai 23, dan 34 sampai 36 (kembali ke default modul). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor dan akun Read Only (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-83: Column Pinning, maksimal tiga kolom data

1. Klik header Actions ⋯ > `Setup Column...`
2. Verifikasi tidak ada kolom data terpin pada konfigurasi awal
3. Pin kolom Active, Account Code, dan Account Name
4. Klik `[Save]`
5. Gulir tabel horizontal
6. Verifikasi kolom checkbox terpin di kiri dan kolom ⋯ terpin di kanan
7. Verifikasi tepat tiga kolom data terpin (Active, Account Code, dan Account Name)
8. Klik header Actions ⋯ > `Setup Column...`
9. Unpin kolom Active, Account Code, dan Account Name
10. Klik `[Save]`

### TC-FA-COA-82: Modified By dan Last Updated tersimpan di browser pengguna

11. Klik header Actions ⋯ > `Setup Column...`
12. Verifikasi modal Setup Column terbuka
13. Centang kolom Modified By dan Last Updated
14. Klik `[Save]`
15. Muat ulang halaman (F5)
16. Verifikasi kolom Modified By dan Last Updated tampil setelah reload pada browser yang sama
17. Di jendela privat pengamat Read Only, buka halaman Fixed Asset > Settings > Accounting > Chart of Accounts
18. Verifikasi sedikitnya satu kolom data lain (Account Code) tampil pada tabel
19. Verifikasi kolom Modified By dan Last Updated tetap hidden pada jendela privat user lain
20. Kembali ke jendela utama
21. Klik header Actions ⋯ > `Setup Column...`
22. Hapus centang kolom Modified By dan Last Updated
23. Klik `[Save]`

### TC-FA-COA-192: Reset to Default sebagai pratinjau, permanen setelah Save

24. Klik header Actions ⋯ > `Setup Column...`
25. Centang kolom Modified By dan hapus centang kolom Account Name
26. Klik `[Save]`
27. Klik header Actions ⋯ > `Setup Column...`
28. Klik `Reset to Default`
29. Verifikasi daftar modal dan tabel menampilkan Active, Account Code, Account Name, Function, Used By, dan Last Used in Journal, sedangkan Modified By dan Last Updated hidden
30. Verifikasi urutan kolom Active, Account Code, Account Name, Function, Used By, Last Used in Journal, Modified By, Last Updated
31. Verifikasi tidak ada kolom data terpin
32. Tutup modal dengan ikon ✕
33. Verifikasi tabel kembali ke konfigurasi tersimpan sebelumnya (Modified By tampil, Account Name hidden) karena reset belum disimpan
34. Klik header Actions ⋯ > `Setup Column...`
35. Klik `Reset to Default`
36. Klik `[Save]`
37. Muat ulang halaman (F5)
38. Verifikasi tabel menampilkan konfigurasi default modul

### TC-FA-COA-195: Tutup dengan ikon ✕ tanpa Save

39. Klik header Actions ⋯ > `Setup Column...`
40. Hapus centang kolom Used By
41. Seret baris Function ke posisi paling bawah daftar modal
42. Pin kolom Account Code
43. Verifikasi pratinjau tabel mengikuti perubahan
44. Tutup modal dengan ikon ✕
45. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (default modul)
46. Muat ulang halaman (F5)
47. Verifikasi konfigurasi tetap default modul

### TC-FA-COA-196: Tutup dengan tombol Esc tanpa Save

48. Klik header Actions ⋯ > `Setup Column...`
49. Hapus centang kolom Used By
50. Seret baris Function ke posisi paling bawah daftar modal
51. Pin kolom Account Code
52. Verifikasi pratinjau tabel mengikuti perubahan
53. Tekan `Esc`
54. Verifikasi modal tertutup dan tabel kembali ke konfigurasi tersimpan terakhir (default modul)
55. Muat ulang halaman (F5)
56. Verifikasi konfigurasi tetap default modul

## Notes

- Alasan spec di atas sekitar 35 langkah (56 langkah): seluruh blok memakai satu tabel, satu popup Setup Column, dan satu kelas harness (fungsional Setup Column); tiap TC memulai dan mengakhiri dari konfigurasi default modul sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pasangan TC-195 dan TC-196 identik kecuali cara menutup popup.
- TC-83 dijalankan lebih dulu, lalu TC-82, TC-192, TC-195, dan TC-196; setiap TC yang menyimpan konfigurasi dikembalikan ke default modul sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03): langkah 9 dan 10, 21 sampai 23 (pemulihan Setup Column eksplisit, R-24 dan 8b.14); langkah 24 sampai 26 (menyiapkan precondition c TC-192); langkah 17 (membuka halaman Chart of Accounts di jendela pengamat sesudah `[Save]` langkah 14, agar asersi hidden pada langkah 19 menguji persistensi lintas browser; membuka halaman bukan interaksi, P-6) dan langkah 20 (kembali ke jendela utama); login dan penutupan jendela pengamat ada di hook `before` dan `after`.
- P-6: pengamat TC-82 (jendela privat dengan user Read Only; login di hook `before`, ditutup di hook `after`) hanya membuka halaman dan membaca tabel tanpa interaksi (langkah 17 sampai 19), satu TC di spec ini; TC sumber menyebut "user lain atau browser lain" tanpa menentukan akunnya, sehingga akun Read Only dipilih (perlu dikonfirmasi tim FE).
- TC-192 langkah 35 dan 36 (`Reset to Default` lalu `[Save]`) adalah langkah TC itu sendiri dan sekaligus memulihkan konfigurasi.
- Temuan untuk QA:
  - TC-82 tidak menyebut akun atau browser "lain" yang dipakai; spec memakai user Read Only di jendela privat.
  - TC-83 butir b ("tidak ada kolom data terpin bawaan") dan langkah pinnya tidak menyebut kolom yang dipin; spec memakai Active, Account Code, dan Account Name.
  - TC-82 Post Condition tidak ada; persistensi `localStorage` diamati lewat reload dan jendela privat, tanpa endpoint (S-13).
