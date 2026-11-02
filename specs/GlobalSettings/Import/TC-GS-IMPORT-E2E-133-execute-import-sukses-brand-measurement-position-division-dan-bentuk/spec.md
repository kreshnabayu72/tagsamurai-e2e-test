---
id: TC-GS-IMPORT-E2E-133-execute-import-sukses-brand-measurement-position-division-dan-bentuk
title: "Execute Import sukses: Brand, Measurement, Position, Division, dan bentuk tunggal satu baris pada log, notifikasi, dan banner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-352
  - TC-GS-IMPORT-353
  - TC-GS-IMPORT-354
  - TC-GS-IMPORT-355
  - TC-GS-IMPORT-572
coverage:
  web: automated
---

# Execute Import sukses: Brand, Measurement, Position, Division, dan bentuk tunggal satu baris pada log, notifikasi, dan banner

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Client E), Tab Brand; blok yang memakai Tab lain berpindah Tab di langkah.
- Client E khusus commit; General Settings Client E: Date Format `dd MMM yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`. Master data Pre-setup Client E seperti Client A (Brand `Samsung`, Measurement `Kilogram (kg)`, Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`, Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`).
- Data Dinamis (fixture baru; berkas dan nama literal dari TC karena Client E dedicated commit dan direset di antara blok sesuai D-47, bukan nama bersuffix):
  - `Fixture.import.brand12` (brand-12.csv, D-50): draft Brand 12 baris `pending`: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus.
  - `Fixture.import.measurementCommit6` (measurement-commit-6.csv, D-51): draft Measurement 6 baris `pending` (Unit Name/Symbol): Meter/m, Liter/l, Gram/g, Centimeter/cm, Pack/pk, Dozen/dz.
  - `Fixture.import.positionCommit6` (position-commit-6.csv, D-52): draft Position 6 baris `pending`: Store Supervisor, HR Business Partner, IT Operations Lead, Warehouse Staff, Procurement Officer, Sales Executive.
  - `Fixture.import.divisionCommit6` (division-commit-6.csv, D-53): draft Division 6 baris `pending` (Division Name/Code): Finance & Accounting/FIN, Operations/(kosong), IT Support/ITS, Procurement/PRC, Sales/SLS, Legal/LGL.
  - `Fixture.import.brandNikon1` (brand-nikon-1.csv): draft Brand 1 baris `pending`: `Nikon`.
- Kemampuan teknis yang disediakan tim FE/BE: penyiapan draft Client E lewat fixture sebelum tiap blok (R1, R3); reset Client E sesuai D-47 (hapus Brand, Measurement, Position, Division hasil commit, hapus draft, reset hasil commit terakhir dan penanda Banner Hasil Commit); worker commit berjalan normal (tunggu commit selesai dengan batas 2 menit, muat ulang tiap 5 detik); baca jumlah entri Changelog Import lewat UI; SSE notifikasi lonceng (TC-GS-IMPORT-572).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan pulihkan sesi ke akun default suite. Hook `afterEach` suite juga mereset Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: Client E berubah permanen oleh commit dan dipulihkan oleh reset D-47; spec Client E tidak boleh paralel dengan spec Client E lain, suite berjalan serial (`parallel: false`).
- Jam server dan jam browser disinkronkan; tidak ada manipulasi jam di spec ini.
- Env var yang dipakai: `GS_CLIENTE_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-352: Import 12 baris Brand

1. Siapkan draft Brand 12 baris (brand-12.csv, D-50) di Client E lewat fixture, lalu muat ulang halaman Import > Brand
2. Catat baseline: buka Changelog Import (icon [Changelog] di header halaman), baca total pada teks Pagination (0 bila empty state), lalu tutup modal
3. Klik [Import (12)]
4. Tunggu aksi selesai (permintaan mendapat respons)
5. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
6. Verifikasi Dropzone tampil menggantikan Staging Table
7. Verifikasi Unsaved Banner tidak tampil
8. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman dengan tombol `[×]`
9. Buka halaman Master Reference > Brand
10. Atur Rows per page 100
11. Verifikasi halaman Master Reference > Brand Client E memuat 12 Brand baru: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus
12. Buka halaman Import > Brand
13. Buka Changelog Import (icon [Changelog] di header halaman)
14. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
15. Verifikasi entri teratas (sort default Date descending): Action `Import Brand`, Data `12 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
16. Tutup modal Changelog Import dan reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-353: Import 6 baris Measurement

17. Buka Tab Measurement pada halaman Import, siapkan draft Measurement 6 baris (measurement-commit-6.csv, D-51) di Client E lewat fixture, lalu muat ulang halaman Import > Measurement
18. Catat baseline: buka Changelog Import, baca total pada teks Pagination (0 bila empty state), lalu tutup modal
19. Klik [Import (6)]
20. Tunggu aksi selesai (permintaan mendapat respons)
21. Muat ulang halaman Import > Measurement setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
22. Verifikasi Dropzone tampil menggantikan Staging Table
23. Verifikasi Unsaved Banner tidak tampil
24. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman dengan tombol `[×]`
25. Buka halaman Master Reference > Measurement
26. Verifikasi halaman Master Reference > Measurement Client E memuat 6 Measurement baru dengan Symbol: Meter `m`, Liter `l`, Gram `g`, Centimeter `cm`, Pack `pk`, Dozen `dz`
27. Buka halaman Import > Measurement
28. Buka Changelog Import (icon [Changelog] di header halaman)
29. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
30. Verifikasi entri teratas (sort default Date descending): Action `Import Measurement`, Data `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
31. Tutup modal Changelog Import dan reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-354: Import 6 baris Position

32. Buka Tab Position pada halaman Import, siapkan draft Position 6 baris (position-commit-6.csv, D-52) di Client E lewat fixture, lalu muat ulang halaman Import > Position
33. Catat baseline: buka Changelog Import, baca total pada teks Pagination (0 bila empty state), lalu tutup modal
34. Klik [Import (6)]
35. Tunggu aksi selesai (permintaan mendapat respons)
36. Muat ulang halaman Import > Position setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
37. Verifikasi Dropzone tampil menggantikan Staging Table
38. Verifikasi Unsaved Banner tidak tampil
39. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman dengan tombol `[×]`
40. Buka halaman User > Position
41. Atur Rows per page 100
42. Verifikasi halaman User > Position Client E memuat 6 Position baru: Store Supervisor, HR Business Partner, IT Operations Lead, Warehouse Staff, Procurement Officer, Sales Executive
43. Buka halaman Import > Position
44. Buka Changelog Import (icon [Changelog] di header halaman)
45. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
46. Verifikasi entri teratas (sort default Date descending): Action `Import Position`, Data `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
47. Tutup modal Changelog Import dan reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-355: Import 6 baris Division

48. Buka Tab Division pada halaman Import, siapkan draft Division 6 baris (division-commit-6.csv, D-53) di Client E lewat fixture, lalu muat ulang halaman Import > Division
49. Catat baseline: buka Changelog Import, baca total pada teks Pagination (0 bila empty state), lalu tutup modal
50. Klik [Import (6)]
51. Tunggu aksi selesai (permintaan mendapat respons)
52. Muat ulang halaman Import > Division setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
53. Verifikasi Dropzone tampil menggantikan Staging Table
54. Verifikasi Unsaved Banner tidak tampil
55. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman dengan tombol `[×]`
56. Buka halaman User > Division
57. Atur Rows per page 100
58. Verifikasi halaman User > Division Client E memuat 6 Division baru: Finance & Accounting (Code `FIN`), Operations, IT Support (Code `ITS`), Procurement (Code `PRC`), Sales (Code `SLS`), Legal (Code `LGL`)
59. Verifikasi Division `Operations` (Code kosong pada berkas) tampil dengan kolom Code terisi
60. Buka halaman Import > Division
61. Buka Changelog Import (icon [Changelog] di header halaman)
62. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
63. Verifikasi entri teratas (sort default Date descending): Action `Import Division`, Data `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
64. Tutup modal Changelog Import dan reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-572: Commit satu baris memakai bentuk tunggal

65. Buka Tab Brand pada halaman Import, siapkan draft Brand 1 baris (brand-nikon-1.csv) di Client E lewat fixture, lalu muat ulang halaman Import > Brand
66. Catat baseline: buka Changelog Import, baca total pada teks Pagination (0 bila empty state), lalu tutup modal
67. Klik [Import (1)]
68. Tunggu aksi selesai (permintaan mendapat respons)
69. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
70. Verifikasi Dropzone tampil
71. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
72. Buka notifikasi lonceng
73. Verifikasi notifikasi lonceng memuat judul "Import Brand completed" dengan isi "1 record imported."
74. Buka Changelog Import (icon [Changelog] di header halaman)
75. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
76. Verifikasi entri teratas (sort default Date descending) memuat Data `1 record imported, 0 duplicates ignored, 0 errors remaining`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-352, 353, 354, 355, 572).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 17, 32, 48, 65 (penyiapan draft sebagai precondition TC lewat fixture dan berpindah Tab); langkah 2, 18, 33, 49, 66 (baseline jumlah entri Changelog Import sebelum aksi pemicu pertama yang diasersi, S-12); langkah 16, 31, 47, 64 (menutup modal dan reset Client E sesuai D-47 sebelum TC berikutnya, Kontrak Fixture R1); langkah 10, 41, 57 (Rows per page 100 agar seluruh record baru tampil); langkah 4, 20, 35, 51, 68 (tunggu aksi selesai sesudah klik [Import (N)] sebelum memuat ulang halaman).
- Baseline Changelog: entri yang diasersi dicari sebagai entri teratas sesuai sort default Date descending setelah total bertambah tepat satu; total Changelog tidak diasersi sebagai angka absolut (S-12).
- Tunggu commit: pemuatan ulang tiap 5 detik dengan batas 2 menit adalah bagian langkah TC (worker commit normal), bukan manipulasi jam.
- Spec ini di atas sekitar 35 langkah (76 langkah). Alasan: lima blok homogen (siapkan draft, Import, tunggu commit, periksa banner, periksa halaman master data, periksa Changelog Import) yang berdiri sendiri dengan draft dan reset Client E sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: commit User Login dan User Non Login ada di spec 134; Partial Commit (draft berisi baris error dan duplicate) di spec 135; kontrol worker commit D-47 dan late-binding di spec kelas d dan 140 sampai 143. Spec ini tidak memakai kontrol worker (worker berjalan normal).
- Temuan untuk QA:
  - TC-GS-IMPORT-352 sampai 355 dan 572 tidak punya asersi isi lain yang dapat dibaca untuk Post Condition "Draft ... dihapus (state belum ada draft)" selain Dropzone tampil (sudah diasersi); Post Condition record tersimpan diasersi lewat halaman master data.
  - TC-GS-IMPORT-355 Expected d menyatakan Division `Operations` (Code kosong pada berkas) tampil dengan "kolom Code terisi" tanpa menyebut nilai Code hasil auto-generate; spec hanya mengasersi bahwa Code terisi.
  - TC-GS-IMPORT-352 sampai 355 dan 572 tidak merujuk D-47 pada kolom D-ref meski Precondition menyebut Client E direset (R1) dan Post Condition menyebut reset; kebutuhan reset ditulis di Prerequisites sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-572 tidak menyebut berkas `brand-nikon-1.csv` pada Data Dinamis (tidak ada ID D); spec memakai berkas itu sebagai fixture baru.
  - TC-GS-IMPORT-352 sampai 355 dan 572 bertanda FE Test `Need API` tanpa menyebut endpoint; spec tidak menyebut endpoint (S-13).
  - Baseline Changelog tidak ada pada TC; spec menambah langkah baseline (S-12) sebagai langkah penghubung.
