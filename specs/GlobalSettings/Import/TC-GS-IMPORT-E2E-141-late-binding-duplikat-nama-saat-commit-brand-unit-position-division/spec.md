---
id: TC-GS-IMPORT-E2E-141-late-binding-duplikat-nama-saat-commit-brand-unit-position-division
title: "Late-binding duplikat nama saat commit (Brand, Unit, Position, Division): error retry-able lalu diperbaiki"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-392
  - TC-GS-IMPORT-393
  - TC-GS-IMPORT-394
  - TC-GS-IMPORT-395
coverage:
  web: automated
---

# Late-binding duplikat nama saat commit (Brand, Unit, Position, Division): error retry-able lalu diperbaiki

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua: Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, hanya lewat sesi API sebagai pemicu perubahan state (P-2); tidak ada asersi di sesi itu.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand (Client E); perpindahan Sub-Tab atau halaman lain ditulis sebagai langkah.
- Data Dinamis (draft lewat fixture `Fixture.import.dupAtCommit141`, fixture baru; nama literal dari Data Dinamis karena asersi bergantung pada nama dan jumlah): D-50 (draft Brand 12 baris `pending`: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus); D-51 (draft Measurement 6 baris `pending`: Meter/m, Liter/l, Gram/g, Centimeter/cm, Pack/pk, Dozen/dz); D-52 (draft Position 6 baris `pending`: Store Supervisor, HR Business Partner, IT Operations Lead, Warehouse Staff, Procurement Officer, Sales Executive); D-53 (draft Division 6 baris `pending`: Finance & Accounting/FIN, Operations/(kosong), IT Support/ITS, Procurement/PRC, Sales/SLS, Legal/LGL, tanpa nama yang bentrok dengan Pre-setup). Record bentrok `Asus`, `Dozen` (Symbol `dz`), `Sales Executive`, dan `Legal` (Code `LEG`) dibuat Admin kedua sebagai pemicu.
- Kemampuan teknis (disediakan tim FE/BE): skrip reset Client E sesuai D-47 (hapus record hasil commit dan record bentrok buatan Admin kedua, draft, hasil commit terakhir); permintaan buat Brand, Measurement, Position, dan Division atas nama Admin kedua Client E lewat klien HTTP.
- State global: Client E dimutasi lalu direset. Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan pulihkan state yang diubah spec (lihat kemampuan teknis).

## Test Steps

### TC-GS-IMPORT-392: Brand Name menjadi duplikat tepat saat commit menghasilkan error retry-able pada Tab Brand

1. Reset Client E ke tanpa draft (D-47), siapkan draft Brand 12 baris dari brand-12.csv (D-50) lewat fixture
2. Buka Import > Brand dan tunggu Staging Table termuat
3. Verifikasi footer menampilkan `[Import (12)]` Enabled
4. Buat Brand `Asus` di halaman Master Reference > Brand atas nama Admin kedua Client E lewat sesi API hingga tersimpan
5. Pada halaman yang sama (tanpa memuat ulang) klik [Import (12)]
6. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
7. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
8. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Brand Name `Asus` (kolom # bernilai 1)
9. Verifikasi Error Summary Callout memuat "Brand name already exists"
10. Verifikasi Error Summary Callout menampilkan badge "1 row"
11. Buka halaman Master Reference > Brand
12. Atur Rows per page 100
13. Verifikasi halaman Master Reference > Brand Client E memuat 11 Brand baru dari baris #1-#11 (Acme Corp sampai Cisco)
14. Verifikasi Brand `Asus` buatan Admin kedua tampil satu kali
15. Buka halaman Import > Brand
16. Buka row action Edit pada baris `error`
17. Ubah Brand Name menjadi `Asus Baru`
18. Klik [Save]
19. Verifikasi baris yang diperbaiki berstatus `pending`
20. Verifikasi kartu Ready to Import menampilkan 1

### TC-GS-IMPORT-393: Unit Name menjadi duplikat tepat saat commit menghasilkan error retry-able pada Tab Measurement

21. Reset Client E ke tanpa draft (D-47), siapkan draft Measurement 6 baris dari measurement-commit-6.csv (D-51) lewat fixture
22. Buka Import > Measurement dan tunggu Staging Table termuat
23. Verifikasi footer menampilkan `[Import (6)]` Enabled
24. Buat Measurement `Dozen` dengan Symbol `dz` di halaman Master Reference > Measurement atas nama Admin kedua Client E lewat sesi API hingga tersimpan
25. Pada halaman yang sama (tanpa memuat ulang) klik [Import (6)]
26. Muat ulang halaman Import > Measurement setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
27. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
28. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Unit Name `Dozen` (kolom # bernilai 1)
29. Verifikasi Error Summary Callout memuat "Unit name already exists"
30. Verifikasi Error Summary Callout menampilkan badge "1 row"
31. Buka halaman Master Reference > Measurement
32. Verifikasi halaman Master Reference > Measurement Client E memuat 5 Measurement baru dari baris #1-#5 (Meter sampai Pack)
33. Verifikasi Measurement `Dozen` buatan Admin kedua tampil satu kali
34. Buka halaman Import > Measurement
35. Buka row action Edit pada baris `error`
36. Ubah Unit Name menjadi `Dozen Baru`
37. Klik [Save]
38. Verifikasi baris yang diperbaiki berstatus `pending`
39. Verifikasi kartu Ready to Import menampilkan 1

### TC-GS-IMPORT-394: Position Name menjadi duplikat tepat saat commit menghasilkan error retry-able pada Tab Position

40. Reset Client E ke tanpa draft (D-47), siapkan draft Position 6 baris dari position-commit-6.csv (D-52) lewat fixture
41. Buka Import > Position dan tunggu Staging Table termuat
42. Verifikasi footer menampilkan `[Import (6)]` Enabled
43. Buat Position `Sales Executive` di halaman User > Position atas nama Admin kedua Client E lewat sesi API hingga tersimpan
44. Pada halaman yang sama (tanpa memuat ulang) klik [Import (6)]
45. Muat ulang halaman Import > Position setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
46. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
47. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Position Name `Sales Executive` (kolom # bernilai 1)
48. Verifikasi Error Summary Callout memuat "Position name already exists"
49. Verifikasi Error Summary Callout menampilkan badge "1 row"
50. Buka halaman User > Position
51. Atur Rows per page 100
52. Verifikasi halaman User > Position Client E memuat 5 Position baru dari baris #1-#5 (Store Supervisor sampai Procurement Officer)
53. Verifikasi Position `Sales Executive` buatan Admin kedua tampil satu kali
54. Buka halaman Import > Position
55. Buka row action Edit pada baris `error`
56. Ubah Position Name menjadi `Sales Executive Baru`
57. Klik [Save]
58. Verifikasi baris yang diperbaiki berstatus `pending`
59. Verifikasi kartu Ready to Import menampilkan 1

### TC-GS-IMPORT-395: Division Name menjadi duplikat tepat saat commit menghasilkan error retry-able pada Tab Division

60. Reset Client E ke tanpa draft (D-47), siapkan draft Division 6 baris dari division-commit-6.csv (D-53) lewat fixture
61. Buka Import > Division dan tunggu Staging Table termuat
62. Verifikasi footer menampilkan `[Import (6)]` Enabled
63. Buat Division `Legal` dengan Code `LEG` di halaman User > Division atas nama Admin kedua Client E lewat sesi API hingga tersimpan
64. Pada halaman yang sama (tanpa memuat ulang) klik [Import (6)]
65. Muat ulang halaman Import > Division setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
66. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
67. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Division Name `Legal` (kolom # bernilai 1)
68. Verifikasi Error Summary Callout memuat "Division name already exists"
69. Verifikasi Error Summary Callout menampilkan badge "1 row"
70. Buka halaman User > Division
71. Atur Rows per page 100
72. Verifikasi halaman User > Division Client E memuat 5 Division baru dari baris #1-#5 (Finance & Accounting sampai Sales)
73. Verifikasi Division `Legal` buatan Admin kedua tampil satu kali
74. Buka halaman Import > Division
75. Buka row action Edit pada baris `error`
76. Ubah Division Name menjadi `Legal Baru`
77. Klik [Save]
78. Verifikasi baris yang diperbaiki berstatus `pending`
79. Verifikasi kartu Ready to Import menampilkan 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (392, 393, 394, 395) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah pertama tiap blok (reset Client E dan penyiapan draft karena Precondition tiap TC mensyaratkan Client E direset sebelum TC), langkah pemicu Admin kedua, langkah menunggu commit, langkah pindah halaman dan Rows per page 100, serta langkah perbaikan baris (buka row action Edit, ubah nama, klik [Save]) yang diikuti `Verifikasi` hasilnya.
- P-2: Admin kedua Client E hanya memicu nama bentrok lewat sesi API dan bukan objek asersi.
- Spec melewati sekitar 35 langkah. Alasan: empat blok TC homogen (pola identik per Tab: nama bentrok saat commit, error retry-able, lalu diperbaiki) yang berdiri sendiri, masing-masing mereset Client E dan memakai Tab berbeda; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berulang per Tab: dari langkah penyiapan draft sampai langkah kartu Ready to Import menampilkan 1 pada tiap blok.
- Pola halaman basi (late-binding saat commit, TC-GS-IMPORT-392..395): halaman Import dimuat dan Staging Table dibaca sebelum pemicu, lalu `[Import (N)]` diklik pada halaman yang sama tanpa dimuat ulang, dengan N dari sebelum pemicu. Referensi, duplikat, dan opsi dievaluasi ulang saat commit selain saat pembacaan Staging Table (PRD `import.md` baris 994, 1164, 1195). `Verifikasi` footer `[Import (N)]` sebelum pemicu adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan draft sudah dibaca pada halaman itu.
- Temuan untuk QA:
  - TC-GS-IMPORT-392 sampai 395: Post Condition (draft berisi 1 baris `pending` dan record baru tersimpan) hanya teramati lewat Expected d dan e; tidak ada observasi tambahan. Langkah Edit dan [Save] pada TC sumber tidak tertulis di kolom Langkah Uji, hanya di Expected e; spec menyalin langkah Edit sesuai Expected e.
  - TC-GS-IMPORT-393: halaman Master Reference > Measurement tidak memakai Rows per page 100 pada langkah sumber (5 baris baru ditambah Pre-setup); spec mengikuti TC.
  - Nama bentrok (`Asus`, `Dozen`, `Sales Executive`, `Legal`) dan nama draft D-50 sampai D-53 literal tanpa suffix per run karena asersi bergantung pada nama; pengecualian S-12 untuk data ini belum dinyatakan di konvensi, dipertahankan dengan reset D-47 dan suite serial.
