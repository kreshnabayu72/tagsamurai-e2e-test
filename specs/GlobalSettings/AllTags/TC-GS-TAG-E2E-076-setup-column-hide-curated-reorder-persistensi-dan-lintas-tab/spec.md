---
id: TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab
title: "Setup Column Registri: Hide/Show Hideable dan Curated, Reorder, Persistensi setelah Refresh, dan Dibagi Tiga Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-220
  - TC-GS-TAG-229
  - TC-GS-TAG-230
  - TC-GS-TAG-231
  - TC-GS-TAG-232
coverage:
  web: automated
---

# Setup Column Registri: Hide/Show Hideable dan Curated, Reorder, Persistensi setelah Refresh, dan Dibagi Tiga Tab

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data tabel; yang diubah hanya konfigurasi kolom.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Konfigurasi kolom awal: default (10 kolom Hideable tampil: `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, `Last Scanned`; 3 kolom Curated tersembunyi: `Last Scanned In`, `Activated At`, `Last User`; urutan awal; tanpa pin). Hook `before` memastikan keadaan ini.
- Suite serial (`parallel: false`): konfigurasi kolom registri adalah state global yang dipakai spec lain.
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom ketiga tab dikembalikan ke default dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Kemampuan teknis: memuat ulang halaman (F5) pada konteks browser yang sama supaya penyimpanan preferensi kolom tetap ada; drag and drop elemen daftar kolom pada modal Setup Column; membaca urutan header kolom data pada tabel dan pada live preview. Mekanisme penyimpanan preferensi kolom tidak didefinisikan di TC (lihat Temuan untuk QA).

## Test Steps

### TC-GS-TAG-220: Setup Column dibagi ketiga tab; kolom Status tidak tampil di Tab Paired

1. Sembunyikan kolom `Brand` lewat overlay Column Visibility (⋯) di Tab All, lalu tutup overlay
2. Verifikasi kolom `Brand` tersembunyi di Tab All
3. Klik Tab Paired
4. Verifikasi kolom `Brand` tersembunyi di Tab Paired
5. Klik Tab Not Paired
6. Verifikasi kolom `Brand` tersembunyi di Tab Not Paired
7. Klik Tab Paired
8. Buka overlay Column Visibility lewat header kolom Actions (⋯)
9. Verifikasi daftar overlay Tab Paired memuat kolom lain (mis. `Code` dan `Device Name`)
10. Verifikasi kolom `Status` tidak tercantum sebagai baris pada overlay Tab Paired
11. Tutup overlay
12. Klik Tab All
13. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
14. Klik `Reset to Default`
15. Klik `Save`

### TC-GS-TAG-229: Ceklis/unceklis kolom Hideable lalu Save dan persist setelah refresh

16. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
17. Hapus centang berurutan `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status` (sisakan `Last Scanned`)
18. Verifikasi live preview menyembunyikan kolom `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, dan `Status`
19. Verifikasi checkbox `Last Scanned` disabled saat hanya `Last Scanned` yang tersisa
20. Klik `Save`
21. Verifikasi tabel menyembunyikan kolom `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, dan `Status`
22. Verifikasi hanya kolom `Last Scanned` yang tampil pada tabel
23. Tekan F5
24. Verifikasi kolom `Last Scanned` tampil
25. Verifikasi kesembilan kolom tetap tersembunyi setelah F5
26. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
27. Klik `Reset to Default`
28. Klik `Save`

### TC-GS-TAG-230: Ceklis kolom Curated menampilkannya di tabel

29. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
30. Centang `Last Scanned In`, `Activated At`, dan `Last User`
31. Klik `Save`
32. Verifikasi kolom `Last Scanned In`, `Activated At`, dan `Last User` tampil pada tabel
33. Tekan F5
34. Verifikasi kolom `Last Scanned In`, `Activated At`, dan `Last User` tetap tampil setelah F5
35. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
36. Klik `Reset to Default`
37. Klik `Save`

### TC-GS-TAG-231: Drag reorder kolom Hideable di modal lalu Save

38. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
39. Seret `Status` ke posisi pertama
40. Verifikasi kolom `Status` menjadi kolom data pertama pada live preview
41. Klik `Save`
42. Verifikasi kolom `Status` menjadi kolom data pertama pada tabel
43. Tekan F5
44. Verifikasi kolom `Status` tetap menjadi kolom data pertama setelah F5
45. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
46. Klik `Reset to Default`
47. Klik `Save`

### TC-GS-TAG-232: Drag reorder kolom Curated di modal lalu Save

48. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
49. Centang `Last User`
50. Klik `Save`
51. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
52. Seret `Last User` ke posisi kedua
53. Klik `Save`
54. Verifikasi kolom `Last User` menjadi kolom data kedua pada tabel
55. Tekan F5
56. Verifikasi kolom `Last User` tetap menjadi kolom data kedua setelah F5
57. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
58. Klik `Reset to Default`
59. Klik `Save`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (220, 229, 230, 231, 232). Spec tidak menghapus data; yang berubah hanya konfigurasi kolom, dan tiap TC diakhiri `Reset to Default` + `Save` supaya TC berikutnya mulai dari konfigurasi default (precondition tiap TC memakai Seed Registri A tanpa kolom yang diubah).
- Panjang spec: 59 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu topik (Setup Column registri) pada satu dataset dan satu kelas harness biasa (bagian 3: Setup Column tetap satu spec selama dataset dan harness sama); tiap TC diakhiri pemulihan ke default sehingga berdiri sendiri; 15 langkah adalah pemulihan (langkah 13 sampai 15, 26 sampai 28, 35 sampai 37, 45 sampai 47, 57 sampai 59). Kegagalan keras pada pembukaan modal Setup Column akan memengaruhi semua blok; hal ini diakui dan pemisahan tidak dilakukan karena topiknya sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (menutup overlay), langkah 12 (kembali ke Tab All), langkah 13 sampai 15, 26 sampai 28, 35 sampai 37, 45 sampai 47, 57 sampai 59 (pemulihan konfigurasi default), langkah 48 sampai 50 (precondition TC-GS-TAG-232 butir d: `Last User` dicentang dan tersimpan, dipakai sebagai precondition TC, tidak diasersi).
- Asersi tambahan di luar Expected TC (S-03): langkah 9 (anchor positif bahwa daftar overlay Tab Paired termuat sebelum absence `Status` pada langkah 10, bagian 8b butir 2); langkah 24 (anchor positif sebelum absence sesudah F5, bagian 8b butir 2). Kalimat dalam kurung TC-GS-TAG-220 butir b ("konfigurasi tidak berpengaruh di tab itu") adalah kesimpulan yang tidak teramati terpisah (S-03).
- Pemisahan dari spec topik registri lain (Search, Filter, Sort, Pagination, Setup Column): ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Temuan untuk QA:
  - Mekanisme persistensi konfigurasi kolom (penyimpanan browser atau API) tidak didefinisikan di TC; TC-GS-TAG-229 sampai 232 hanya menyatakan "persist setelah F5". Spec ini `FE+BE` dan tidak mengarang endpoint; "tekan F5" dilakukan pada konteks browser yang sama.
  - TC-GS-TAG-229 butir a memadukan live preview (diamati sebelum `Save`, langkah 3 TC) dan tabel (sesudah `Save`); spec memisahkannya menjadi langkah 18 dan 21.
  - TC-GS-TAG-232 langkah 2 ("Seret `Last User` ke posisi kedua") tidak menyebut apakah posisi kedua dihitung pada daftar modal atau pada kolom data tabel; spec menafsirkannya sebagai kolom data kedua (Expected: "kolom data kedua").
  - TC-GS-TAG-220 langkah 1 tidak menyebut cara menyembunyikan `Brand` (overlay Column Visibility atau modal Setup Column); spec memakai overlay Column Visibility.
  - TC-GS-TAG-220 mensyaratkan konfigurasi dibagi tiga tab tetapi mengasersi Tab Not Paired hanya sebagai `Brand` tersembunyi; kolom `Status` pada Tab Not Paired tidak diuji.
  - Hitungan baris tidak diasersi; kebutuhan Seed Registri A utuh mengikuti Q-4.
