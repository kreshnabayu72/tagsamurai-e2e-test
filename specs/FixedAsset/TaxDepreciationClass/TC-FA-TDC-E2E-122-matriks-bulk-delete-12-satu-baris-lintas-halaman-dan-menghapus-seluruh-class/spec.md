---
id: TC-FA-TDC-E2E-122-matriks-bulk-delete-12-satu-baris-lintas-halaman-dan-menghapus-seluruh-class
title: "Matriks Bulk Delete 12 Satu Baris Lintas Halaman dan Menghapus Seluruh Class"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-467
  - TC-FA-TDC-468
  - TC-FA-TDC-469
  - TC-FA-TDC-905
  - TC-FA-TDC-906
  - TC-FA-TDC-907
sourceRules: ["D-04", "D-05", "D-06", "§3.6#r12", "S-07a", "D-01", "FATDC-LOGIC-14e", "FATDC-LOGIC-14k", "§3.6#r9", "ST-23", "J-01"]
smoke: []
dependsOn: []
trace:
  "D-04": [3, 4, 5]
  "D-05": [10, 11, 12]
  "D-06": [17, 18, 35]
  "§3.6#r12": 20
  "S-07a": [21, 38]
  "D-01": 27
  "FATDC-LOGIC-14e": 28
  "FATDC-LOGIC-14k": 33
  "§3.6#r9": 37
  "ST-23": [43, 46]
  "J-01": 47
coverage:
  web: automated
---

# Matriks Bulk Delete 12 Satu Baris Lintas Halaman dan Menghapus Seluruh Class

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset122`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): blok pertama (TC-FA-TDC-468, 469, 467) memakai tabel satu halaman berisi NB-KHS (Last Posted Tax Year 2026, Used By 0), NB-2 (Used By 3, tanpa Last Posted Tax Year), dan NB-3 (Used By 0, tanpa Last Posted Tax Year). Blok kedua (TC-FA-TDC-905, 906, 907) memakai tabel 25 class Active dengan Used By 0 dan tanpa Last Posted Tax Year, 10 baris per halaman, yang dibentuk pada langkah 22 (22 class tambahan lewat API). NB-3 dan class pada blok kedua menjadi target hapus (milik dataset spec ini). TC-FA-TDC-907 menghabiskan seluruh class sehingga ada di akhir spec. Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris dan header; berpindah halaman Pagination; mengganti dataset lewat API di tengah spec (sesi API aktor sesuai `suite.md`); menggulir daftar dalam dialog.
- State global yang diubah: seluruh class pada dataset (dihapus oleh spec; dipulihkan di hook `after` ke seed awal).

## Test Steps

### TC-FA-TDC-468: Bulk Delete satu baris tercentang terkena Guard 1 memakai dialog blok single D-04

1. Centang checkbox baris NB-KHS
2. Klik `Delete` pada Bulk Action Bar
3. Verifikasi dialog "Cannot Delete Tax Depreciation Class" (judul tunggal) tampil dengan bullet `• NB-KHS – Kelompok khusus pernah diposting`
4. Verifikasi kalimat dialog "It was used for fiscal depreciation in 2026."
5. Verifikasi footer dialog memuat satu tombol `[OK]`
6. Klik `[OK]` pada dialog blok
7. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-469: Bulk Delete satu baris tercentang terkena Guard 2 memakai dialog blok single D-05

8. Centang checkbox baris NB-2
9. Klik `Delete` pada Bulk Action Bar
10. Verifikasi dialog "Cannot Delete Tax Depreciation Class" (judul tunggal) tampil dengan bullet `• NB-2 – Bukan bangunan – Kelompok 2`
11. Verifikasi kalimat dialog "This class is used by 3 asset classes."
12. Verifikasi footer dialog memuat satu tombol `[OK]`
13. Klik `[OK]` pada dialog blok
14. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-467: Matriks 12: Bulk Delete dari satu baris tercentang memakai dialog single D-06

15. Centang checkbox baris NB-3
16. Klik `Delete` pada Bulk Action Bar
17. Verifikasi dialog "Delete Tax Depreciation Class" (judul tunggal) tampil dengan satu bullet `• NB-3 – Bukan bangunan – Kelompok 3`
18. Verifikasi kalimat dialog "This action cannot be undone. Are you sure you want to delete it?"
19. Klik `[Delete]` pada dialog
20. Verifikasi toast "Success, tax depreciation class has been deleted." tampil
21. Verifikasi baris NB-3 tidak ada di tabel
22. Ganti dataset lewat API menjadi tabel 25 class Active dengan Used By 0 tanpa Last Posted Tax Year (22 class tambahan), lalu muat ulang tabel

### TC-FA-TDC-905: Dialog bulk memuat seluruh nama class dalam daftar scrollable tanpa ringkasan

23. Centang checkbox satu baris agar Bulk Action Bar tampil
24. Klik `Select All (25 records)`
25. Klik `Deactivate` pada Bulk Action Bar
26. Gulir daftar bullet pada dialog sampai bullet terakhir
27. Verifikasi dialog memuat 25 bullet `• [Class Code] – [Class Name]` pada container yang dapat digulir
28. Verifikasi tidak ada kalimat ringkasan seperti "25 items are selected." atau "...and N more"
29. Klik `[Cancel]` pada dialog
30. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-906: Bulk Delete memproses seleksi dari beberapa halaman

31. Pada halaman 1 centang dua baris pertama
32. Pindah ke halaman 3 dan centang satu baris
33. Verifikasi Bulk Action Bar menampilkan counter jumlah terpilih bernilai 3
34. Klik `Delete` pada Bulk Action Bar
35. Verifikasi dialog Delete jamak memuat tiga bullet dari kedua halaman
36. Klik `[Delete]` pada dialog
37. Verifikasi toast "Success, tax depreciation class has been deleted." tampil
38. Verifikasi ketiga class yang dicentang terhapus (tidak ada lagi di tabel)

### TC-FA-TDC-907: Menghapus seluruh class lewat Bulk Delete menampilkan Empty State dan seed tidak dibuat ulang

39. Centang checkbox satu baris agar Bulk Action Bar tampil
40. Klik `Select All (22 records)` pada Bulk Action Bar
41. Klik `Delete` pada Bulk Action Bar
42. Klik `[Delete]` pada dialog
43. Verifikasi tabel menampilkan Empty State dengan judul "No tax depreciation class", deskripsi "Tax depreciation cannot be calculated.", dan tombol `Restore default classes`
44. Buka tab Asset Class
45. Kembali ke tab Tax Depreciation Class
46. Verifikasi tabel masih menampilkan Empty State yang sama
47. Verifikasi tidak ada class seed baru di tabel

## Notes

- Urutan TC dalam spec: TC-FA-TDC-468, 469, 467, 905, 906, 907. Dialog blok lebih dulu, aksi hapus kemudian, dan TC-FA-TDC-907 yang menghabiskan seluruh class paling akhir (S-10).
- Langkah penghubung (S-03, S-09): langkah 7, 14 dan 30 (klik icon `×` agar seleksi TC berikutnya bersih), langkah 22 (mengganti dataset ke tabel 25 class; TC-FA-TDC-905 dan 906 mensyaratkan 25 class Used By 0 tanpa Last Posted Tax Year, sedangkan NB-KHS dan NB-2 pada blok pertama tidak memenuhinya), serta langkah 23 dan 39 (mencentang satu baris agar Bulk Action Bar tampil, karena bar hilang bila tidak ada baris tercentang dan `Select All` hanya tersedia di bar; langkah 1 TC-FA-TDC-905 dan 907 tidak menyebut cara bar muncul).
- Pada TC-FA-TDC-467 dan 906, toast sukses `Verifikasi` lebih dulu dari "baris tidak ada di tabel" karena toast menjadi anchor respons server selesai (8b.2).
- Di atas sekitar 35 langkah (47 langkah): satu topik (Bulk Delete satu baris, lintas halaman, dan seluruh class, kelas harness `-`); seleksi dibersihkan di akhir blok. Dua sambungan antar blok: langkah 22 (mengganti dataset ke tabel 25 class) menjadi precondition blok TC-FA-TDC-905, 906, dan 907, dan angka 22 pada langkah 40 (TC-FA-TDC-907) bergantung pada penghapusan tiga class di blok TC-FA-TDC-906 (langkah 36 sampai 38). Blok 468, 469, dan 467 berdiri sendiri; blok 905 sampai 907 bergantung pada langkah 22, dan blok 907 bergantung pada blok 906.
- Temuan untuk QA:
  - TC-FA-TDC-905 dan 907 langkah 1 (`Select All`) tidak menyebut cara memunculkan Bulk Action Bar; spec mencentang satu baris lebih dulu (langkah 23 dan 39). Pola sama dengan TC-FA-TDC-419 (spec 110), 420, 421 (spec 111), dan 459 (spec 120).
  - TC-FA-TDC-906 Expected b menyebut "kedua halaman" padahal baris dicentang pada halaman 1 dan halaman 3; Expected c "ketiga class terhapus" tidak menyebut kode class, sehingga asersi memakai baris yang dicentang.
  - TC-FA-TDC-907 memakai `[N]` tanpa nilai; N diturunkan dari seeding (22 sesudah TC-FA-TDC-906).
  - TC-FA-TDC-907 Expected b "tidak ada class seed baru" diasersi sebagai tidak ada baris class di tabel.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
