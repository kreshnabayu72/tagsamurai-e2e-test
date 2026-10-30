---
id: TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state
title: "Kombinasi Search, Filter, Sort, dan Pagination: Irisan, Independensi Clear, Pemulihan Empty State, dan Seleksi Bertahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-213
  - TC-GS-TAG-214
  - TC-GS-TAG-215
  - TC-GS-TAG-216
  - TC-GS-TAG-217
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination: Irisan, Independensi Clear, Pemulihan Empty State, dan Seleksi Bertahan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data (seleksi checkbox TC-GS-TAG-217 hanya state UI, tanpa aksi bulk); hitungan baris (16 baris RFID bermerek `Generic`, 3 baris Self-Purchased `alien`) valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): Search, Filter, Sort, dan seleksi pada Tab All dan Tab Not Paired dikosongkan.
- Kemampuan teknis: membaca indikator sort pada header kolom, titik indikator pada ikon Filter, dan teks pagination `Showing ... of N TAGs` (selektor disediakan tim FE).

## Test Steps

### TC-GS-TAG-213: Search lalu Filter dan Filter lalu Search menghasilkan irisan identik

1. Ketik Search `alien`, tekan Enter
2. Klik ikon Filter untuk membuka panel
3. Pilih `Source` = Self-Purchased
4. Klik `Apply`
5. Verifikasi baris DD-02, DD-08, dan DD-11 tampil (3 baris; DD-11 cocok lewat Brand `Alien`)
6. Verifikasi keyword `alien` tetap pada kotak Search (menerapkan filter tidak mereset keyword)
7. Klik `Clear Field`, lalu klik `Apply`
8. Klik ikon Filter untuk menutup panel
9. Klik `(←)` pada kotak Search
10. Klik ikon Filter untuk membuka panel
11. Pilih `Source` = Self-Purchased
12. Klik `Apply`
13. Ketik Search `alien`, tekan Enter
14. Verifikasi baris DD-02, DD-08, dan DD-11 tampil (identik dengan urutan pertama, 3 baris)
15. Verifikasi filter `Source` = Self-Purchased tetap aktif (menerapkan keyword tidak mereset filter)
16. Klik `(←)` pada kotak Search
17. Klik `Clear Field`, lalu klik `Apply`
18. Klik ikon Filter untuk menutup panel

### TC-GS-TAG-214: Kombinasi Search, Filter, Sort, dan Pagination aktif bersamaan

19. Klik ikon Filter untuk membuka panel
20. Pilih `TAG Type` = RFID
21. Klik `Apply`
22. Ketik Search `generic`, tekan Enter
23. Klik ikon Filter untuk menutup panel
24. Klik header `Code` dua kali (descending)
25. Ubah Rows per page menjadi 10
26. Pindah ke halaman 2
27. Verifikasi sedikitnya satu baris tampil
28. Verifikasi hanya baris RFID bermerek `Generic` yang tampil (16 baris filler, dibaca dari teks pagination `of 16 TAGs`)
29. Verifikasi urutan Code descending
30. Verifikasi halaman 2 menampilkan 6 baris
31. Verifikasi keyword `generic` tetap aktif pada kotak Search
32. Verifikasi filter `TAG Type` = RFID tetap aktif
33. Verifikasi sort `Code` descending tetap aktif
34. Klik `(←)` pada kotak Search
35. Klik ikon Filter untuk membuka panel
36. Klik `Clear Field`, lalu klik `Apply`
37. Klik ikon Filter untuk menutup panel
38. Klik header `Code` sekali (kembali netral)

### TC-GS-TAG-215: Clear Filter, Clear Search, dan ganti kolom sort tidak saling mereset

39. Ketik Search `generic`, tekan Enter
40. Klik ikon Filter untuk membuka panel
41. Pilih `Source` = Official
42. Klik `Apply`
43. Klik ikon Filter untuk menutup panel
44. Klik header `Code` sekali (ascending)
45. Klik ikon Filter untuk membuka panel
46. Klik `Clear Field`, lalu klik `Apply`
47. Verifikasi keyword `generic` tetap aktif (Clear Filter tidak mereset keyword)
48. Verifikasi sort `Code` ascending tetap aktif (Clear Filter tidak mereset sort)
49. Pilih `Source` = Official
50. Klik `Apply`
51. Klik ikon Filter untuk menutup panel
52. Kosongkan isi kotak search, tekan Enter
53. Verifikasi filter `Source` = Official tetap aktif (titik indikator pada ikon Filter)
54. Verifikasi sort `Code` ascending tetap aktif
55. Klik header `Device Name`
56. Verifikasi kotak Search tetap kosong
57. Verifikasi filter `Source` = Official tetap aktif
58. Verifikasi kolom `Code` kembali netral
59. Klik header `Device Name` dua kali lagi (kembali netral)

### TC-GS-TAG-216: Empty state hasil kombinasi pulih saat salah satu kontrol dilepas

60. Klik ikon Filter untuk membuka panel
61. Klik `Clear Field`, lalu klik `Apply`
62. Pilih `TAG Type` = GPS
63. Klik `Apply`
64. Klik ikon Filter untuk menutup panel
65. Ketik Search `zebra`, tekan Enter
66. Verifikasi `No results found` tampil
67. Kosongkan isi kotak search, tekan Enter
68. Verifikasi baris GPS (DD-09) tampil kembali

### TC-GS-TAG-217: Seleksi checkbox bertahan saat Search/Filter diubah di Tab Not Paired

69. Klik ikon Filter untuk membuka panel
70. Klik `Clear Field`, lalu klik `Apply`
71. Klik ikon Filter untuk menutup panel
72. Klik `(←)` pada kotak Search
73. Klik Tab Not Paired
74. Centang baris DD-02
75. Ketik Search `alien`, tekan Enter
76. Kosongkan isi kotak search, tekan Enter
77. Verifikasi counter tetap `1 TAG selected` setelah Search diubah dan dikosongkan
78. Klik ikon Filter untuk membuka panel
79. Pilih `TAG Type` = BLE
80. Klik `Apply`
81. Verifikasi counter tetap `1 TAG selected` setelah filter BLE diterapkan
82. Klik `Clear Field`, lalu klik `Apply`
83. Verifikasi counter tetap `1 TAG selected` setelah filter dikosongkan
84. Verifikasi baris DD-02 tetap tercentang
85. Klik ikon Filter untuk menutup panel
86. Hapus centang baris DD-02

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (213 sampai 217). TC-GS-TAG-217 di akhir karena satu-satunya yang memakai Tab Not Paired dan menyisakan seleksi (dibersihkan pada langkah 86). Spec tidak menghapus data.
- Panjang spec: 86 langkah tertulis, di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu topik (kombinasi kontrol tabel) pada satu dataset (Seed Registri A) dan satu kelas harness biasa, dan tiap blok diakhiri pengosongan Search, Filter, dan Sort (langkah 7 sampai 9 dan 16 sampai 18, 34 sampai 38, 59, 60 sampai 64, 69 sampai 72) sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya dan kegagalan asersi satu blok tidak menutup makna blok lain. Kegagalan keras pada pembukaan Filter Panel akan memengaruhi semua blok; hal ini diakui.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 sampai 18, 34 sampai 38, 59, 60 sampai 61, 69 sampai 72 (mengosongkan Search, Filter, dan Sort), langkah 8, 23, 37, 43, 51, 64, 71, 85 (menutup panel supaya klik tabel tidak terhalang panel), langkah 86 (menghapus seleksi). Langkah 27 adalah pembanding positif (sedikitnya satu baris tampil) sebelum asersi universal pada langkah 28. Langkah 7 sampai 9 adalah langkah TC-GS-TAG-213 ("Reset keduanya"), bukan penghubung.
- Pemisahan dari spec Search, Filter, Sort, dan Pagination registri tunggal: kelas harness tidak sama dan tidak semua memakai data yang sama; ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Hitungan 16 baris, 6 baris halaman 2, dan 3 baris irisan diturunkan dari Seed Registri A; teks pagination `of 16 TAGs` diambil dari format TC-GS-TAG-245.
- Temuan untuk QA:
  - TC-GS-TAG-217 butir "setelah dimuat kembali" ambigu: tidak jelas apakah memuat ulang halaman (F5) atau memuat ulang daftar setelah `Clear Field` + `Apply`. Spec mengasersi tercentang setelah daftar dimuat ulang oleh `Clear Field` + `Apply` (langkah 84) dan tidak memakai F5 karena retensi seleksi lintas refresh tidak dinyatakan TC.
  - TC-GS-TAG-217 tidak menyebut counter sesudah tiap perubahan; spec mengasersi counter `1 TAG selected` sesudah Search, sesudah filter BLE, dan sesudah filter dikosongkan (langkah 77, 81, 83) sebagai penjabaran "melewati seluruh perubahan".
  - TC-GS-TAG-214 langkah 4 meminta "Ubah Rows per page menjadi 10" padahal nilai default sudah 10 (TC-GS-TAG-245); spec mengikuti TC.
  - TC-GS-TAG-215 langkah 3 ("Isi ulang filter") tidak menyebut nilai; spec memakai `Source` = Official seperti langkah 1.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
