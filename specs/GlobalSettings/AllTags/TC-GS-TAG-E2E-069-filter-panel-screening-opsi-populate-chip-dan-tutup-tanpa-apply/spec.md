---
id: TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply
title: "Filter Panel: Screening Field, Opsi Populate per Tab, Sinkronisasi Chip, Search Dropdown, Tutup Tanpa Apply, Indikator, dan Persist saat Kolom Di-hide"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-201
  - TC-GS-TAG-202
  - TC-GS-TAG-206
  - TC-GS-TAG-207
  - TC-GS-TAG-208
  - TC-GS-TAG-209
  - TC-GS-TAG-210
  - TC-GS-TAG-211
coverage:
  web: automated
---

# Filter Panel: Screening Field, Opsi Populate per Tab, Sinkronisasi Chip, Search Dropdown, Tutup Tanpa Apply, Indikator, dan Persist saat Kolom Di-hide

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan baris (30, 26, 24 Source Official) valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): filter registri dikosongkan dan visibilitas kolom dikembalikan ke default dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Tabel "Field Filter Panel" (parameter langkah 7; urutan field sama dengan Expected TC-GS-TAG-201 butir b):

| Field | Tipe kontrol | Placeholder |
|---|---|---|
| `TAG Type` | multi-select searchable | `All types` |
| `Device Name` | multi-select searchable | `All device names` |
| `Brand` | multi-select searchable | `All brands` |
| `Model/Type` | multi-select searchable | `All model/types` |
| `Source` | multi-select searchable | `All sources` |
| `Type` | multi-select searchable | `All types` |
| `Status` | multi-select searchable | `All statuses` |
| `Last Scanned` | date range | `Select date` |
| `Last Scanned In` | multi-select searchable | `All modules` |
| `Activated At` | date range | `Select date` |
| `Last User` | multi-select searchable | `All users` |

- Kemampuan teknis: membaca keadaan visual ikon Filter (gelap saat panel terbuka) dan titik indikator pada ikon Filter (atribut keadaan atau kelas visual; selektor disediakan tim FE).

## Test Steps

### TC-GS-TAG-201: Screening Filter Panel

1. Arahkan kursor ke ikon Filter
2. Verifikasi tooltip ikon `Filter`
3. Klik ikon `Filter`
4. Verifikasi ikon Filter menjadi gelap saat panel terbuka
5. Verifikasi field berurutan `TAG Type`, `Device Name`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, `Last Scanned`, `Last Scanned In`, `Activated At`, `Last User`
6. Untuk setiap baris tabel "Field Filter Panel" pada Prerequisites, lakukan langkah 7
7. Verifikasi field memiliki tipe kontrol dan placeholder sesuai baris tabel itu
8. Verifikasi footer panel: `Clear Field` (kiri) dan `Apply` (kanan)
9. Verifikasi tidak ada field untuk `SKU` dan `Code`
10. Klik ikon Filter untuk menutup panel

### TC-GS-TAG-202: Opsi dropdown filter di-populate dari data tab aktif

11. Klik ikon Filter
12. Buka dropdown `Status`
13. Verifikasi opsi Status Tab All: `Available`, `Damaged/Missing`, `Paired`, `Reserved`, `Retired`, `To be Returned`, `Waiting for Approval`
14. Klik ikon Filter untuk menutup panel
15. Klik Tab Not Paired
16. Klik ikon Filter, lalu buka dropdown `Status`
17. Verifikasi sedikitnya satu opsi Status tampil di Tab Not Paired
18. Verifikasi opsi `Paired` tidak ada di dropdown `Status` Tab Not Paired
19. Klik ikon Filter untuk menutup panel
20. Klik Tab Paired
21. Klik ikon Filter, lalu buka dropdown `Source`
22. Verifikasi opsi Source hanya `Official`
23. Klik ikon Filter untuk menutup panel

### TC-GS-TAG-206: Menghapus chip via (✕) meng-uncheck opsi di dalam dropdown

24. Klik Tab All
25. Klik ikon Filter
26. Pilih `Status` = Available dan Reserved
27. Klik `(✕)` pada chip `Available` tanpa membuka dropdown
28. Verifikasi chip `Available` hilang
29. Verifikasi chip `Reserved` tetap
30. Buka dropdown `Status`
31. Verifikasi opsi `Available` ter-uncheck di dalam dropdown

### TC-GS-TAG-207: Uncheck opsi di dalam dropdown menghapus chip

32. Klik `Clear Field`
33. Pilih `Status` = Available dan Reserved
34. Buka dropdown `Status`, hapus centang `Reserved`
35. Verifikasi chip `Reserved` hilang dari field
36. Verifikasi chip `Available` tetap

### TC-GS-TAG-208: Search di dalam dropdown filter mempersempit opsi

37. Klik `Clear Field`
38. Buka dropdown `Brand`
39. Ketik `zeb` pada kotak search dropdown
40. Verifikasi opsi menyempit ke `Zebra`
41. Ganti isi kotak search dropdown dengan `zzz`
42. Verifikasi teks `No options available` tampil

### TC-GS-TAG-209: Menutup panel tanpa Apply membuang perubahan

43. Klik `Clear Field`
44. Pilih `Source` = Official
45. Klik `Apply`
46. Ubah `Source` menjadi Self-Purchased tanpa `Apply`
47. Klik ikon Filter untuk menutup panel
48. Klik ikon Filter untuk membuka panel lagi
49. Verifikasi panel menampilkan `Source` = Official (nilai ter-Apply terakhir)
50. Verifikasi sedikitnya satu baris tampil
51. Verifikasi tabel tetap menampilkan hasil Official (24 baris)

### TC-GS-TAG-210: Ikon Filter menampilkan titik indikator selama ada filter ter-Apply

52. Klik `Clear Field`, lalu klik `Apply`
53. Pilih `Source` = Official
54. Klik `Apply`
55. Verifikasi titik indikator tampil di ikon Filter saat panel terbuka
56. Klik ikon Filter untuk menutup panel
57. Verifikasi titik indikator tetap tampil di ikon Filter saat panel tertutup
58. Klik ikon Filter untuk membuka panel
59. Klik `Clear Field`, lalu klik `Apply`
60. Verifikasi titik indikator hilang dari ikon Filter

### TC-GS-TAG-211: Filter tetap tersedia dan persist walau kolom di-hide

61. Pilih `Source` = Official
62. Klik `Apply`
63. Klik ikon Filter untuk menutup panel
64. Sembunyikan kolom `Source` lewat overlay Column Visibility (⋯)
65. Klik ikon Filter untuk membuka panel
66. Verifikasi field `Source` tetap ada dengan nilai Official
67. Verifikasi sedikitnya satu baris tampil
68. Verifikasi hasil tabel tetap tersaring (24 baris)
69. Klik `Clear Field`, lalu klik `Apply`
70. Klik ikon Filter untuk menutup panel
71. Tampilkan kembali kolom `Source` lewat overlay Column Visibility (⋯)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 201 (screening di awal), 202, 206, 207, 208, 209, 210, 211. TC-GS-TAG-203, 204, 205, 212 (nilai filter, rentang tanggal, logika OR/AND) ada di spec `TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or`. Spec ini tidak menghapus data.
- Panjang spec: 71 langkah tertulis (sekitar 81 langkah setelah ekspansi 11 field pada langkah 7), di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu topik (Filter Panel) pada satu dataset (Seed Registri A) dan satu kelas harness biasa (bagian 3 prinsip 1), memakai satu pembukaan layar, dan tiap blok diawali `Clear Field` atau pindah tab sehingga tidak bergantung pada hasil blok sebelumnya. Kegagalan keras pada pembukaan Filter Panel akan membuat blok sesudah screening tidak berjalan; hal ini diakui dan pemisahan tidak dilakukan karena semua blok memakai panel dan dataset yang sama. Langkah yang diulang: langkah 7 (11 iterasi, satu per baris tabel Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 14, 19, 23 (menutup panel supaya perpindahan tab dan pembukaan panel berikutnya deterministik), langkah 24 (kembali ke Tab All karena Tab Paired tidak punya filter `Status`), langkah 32, 37, 43, 52, 69 (mengosongkan panel), langkah 63, 70 (menutup panel), langkah 71 (memulihkan kolom `Source`). TC tidak menyebut keadaan panel setelah pindah tab; spec menutup panel sebelum pindah tab dan membukanya kembali sesudahnya (langkah 14 sampai 16 dan 19 sampai 21).
- Pemisahan dari spec nilai Filter, Search, Sort, dan Pagination registri: ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Asersi absence opsi `Paired` (langkah 18) didahului langkah 17 sebagai anchor positif (opsi Status lain tampil di surface yang sama, bagian 8b butir 2).
- Langkah 50 dan 67 adalah pembanding positif (sedikitnya satu baris tampil) sebelum asersi hasil tabel pada langkah 51 dan 68.
- Hasil tabel 24 baris (langkah 51, 68) diturunkan dari Seed Registri A (24 baris Source Official, TC-GS-TAG-203 butir e); Expected TC-GS-TAG-209 dan 211 hanya menyebut "tetap menampilkan hasil Official" dan "tetap tersaring".
- Temuan untuk QA:
  - TC-GS-TAG-201 butir b menyebut tipe kontrol `multi-select searchable` hanya pada `TAG Type`; spec memakai tipe yang sama untuk field pilihan lain berdasarkan judul TC-GS-TAG-203 ("Filter per field multi-select searchable"). Perlu konfirmasi tipe kontrol tiap field.
  - TC-GS-TAG-201 butir a ("ikon menjadi gelap") tidak mendefinisikan cara mengamati keadaan gelap; spec memakai keadaan visual yang selektornya disediakan tim FE.
  - TC-GS-TAG-202 langkah 2 dan 3 tidak menyebut apakah Filter Panel tetap terbuka setelah pindah tab; spec menutup panel dan membukanya lagi (langkah 14 sampai 16 dan 19 sampai 21).
  - TC-GS-TAG-202 butir b/c menguji Status di Tab Not Paired dan Source di Tab Paired, sedangkan TC-GS-TAG-206 sampai 208 mensyaratkan Tab All; spec kembali ke Tab All pada langkah 24.
  - TC-GS-TAG-210 butir a menyebut titik indikator "baik panel terbuka maupun tertutup" tanpa menyebut bentuk titik; spec mengasersi keberadaannya saja.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
