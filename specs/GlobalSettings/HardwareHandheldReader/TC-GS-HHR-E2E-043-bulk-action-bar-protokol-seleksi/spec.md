---
id: TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi
title: "Bulk Action Bar dan Protokol Seleksi: Elemen Bar, Checkbox Header, Checkbox Disabled, Select All Lintas Halaman, Retensi Seleksi, dan Ikon ×"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-189
  - TC-GS-HHR-190
  - TC-GS-HHR-191
  - TC-GS-HHR-192
  - TC-GS-HHR-193
  - TC-GS-HHR-194
coverage:
  web: automated
---

# Bulk Action Bar dan Protokol Seleksi: Elemen Bar, Checkbox Header, Checkbox Disabled, Select All Lintas Halaman, Retensi Seleksi, dan Ikon ×

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini tidak mengubah data reader: seluruh seleksi dikosongkan lewat ikon `×` dan tidak ada aksi bulk yang dikonfirmasi.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah ganti akun.
- Akun aktor:
  - Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client L untuk TC-GS-HHR-192 dan 193: login lewat langkah ganti akun eksplisit (langkah 34 sampai 36) dengan `Spectra.env.GS_CLIENTL_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email mengikuti pola Pre-setup TC `totalControl_automated_{namaClient}@qwertysystem.net` dengan `{namaClient}` = Client L; email persisnya disediakan tim FE.
  - Hook `after` mengembalikan sesi ke akun Total Control Client A. Password tidak ditulis di spec atau fixture.
- Data Pre-setup:
  - Client A (Data Dinamis: Seed Reader A, dipulihkan fixture backend): Seed Reader A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), 10 reader DD-01 s.d. DD-10, plan Growth, format tanggal default `dd/MM/yy` 24-hour, ukuran halaman default 10. Reader yang dapat dipilih (bukan Waiting for Approval): DD-01, DD-02, DD-03, DD-04, DD-06, DD-07, DD-08, DD-09 (8 reader); DD-05 dan DD-10 berstatus Waiting for Approval. Spec memakai DD-01 dan DD-07 (Available) serta DD-05 dan DD-10. Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR).
  - Client L: 26 reader berstatus Available (`Large Reader - 1` s.d. `Large Reader - 26`), Rows per page 10 (fixture baru `Fixture.hardwareHandheldReader.clientL`).
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor (Client A dan Client L) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover pada checkbox disabled dan pembacaan tooltip; pembacaan state checkbox (unchecked, indeterminate, checked, disabled), teks Bulk Action Bar, serta posisi dan urutan elemen bar; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite) dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-189: Bulk Action Bar muncul dengan urutan elemen baku

1. Verifikasi sisi kiri area di atas tabel kosong dan Table Tools tampil sendirian (belum ada baris tercentang)
2. Centang checkbox baris DD-01
3. Verifikasi Bulk Action Bar muncul di atas tabel, rata kiri, sejajar dengan Table Tools yang rata kanan
4. Verifikasi urutan elemen Bulk Action Bar dari kiri: tombol `Bulk Action`, teks `1 Reader selected`, tombol `Select All (8 records)`, ikon `×`
5. Centang checkbox baris DD-07
6. Verifikasi teks Bulk Action Bar menjadi `2 Readers selected`
7. Klik ikon `×`

### TC-GS-HHR-191: Checkbox baris Waiting for Approval disabled dan tidak ikut Select All

8. Arahkan kursor ke checkbox baris DD-05
9. Verifikasi checkbox DD-05 disabled dengan tooltip `This device is waiting for approval.`
10. Klik checkbox baris DD-05
11. Verifikasi baris DD-05 tidak tercentang
12. Verifikasi Bulk Action Bar tidak tampil
13. Arahkan kursor ke checkbox baris DD-10
14. Verifikasi checkbox DD-10 disabled dengan tooltip `This device is waiting for approval.`
15. Centang checkbox baris DD-01
16. Verifikasi tombol menampilkan `Select All (8 records)`
17. Klik ikon `×`

### TC-GS-HHR-190: Checkbox header memilih baris halaman aktif dan statusnya mengikuti jumlah baris tercentang

18. Verifikasi checkbox header unchecked
19. Centang checkbox baris DD-01
20. Verifikasi checkbox header indeterminate (`[-]`)
21. Klik checkbox header
22. Verifikasi 8 baris eligible tercentang (DD-01, DD-02, DD-03, DD-04, DD-06, DD-07, DD-08, DD-09)
23. Verifikasi counter `8 Readers selected`
24. Verifikasi baris DD-05 dan DD-10 tidak tercentang
25. Klik checkbox header lagi
26. Verifikasi seluruh centang halaman terlepas
27. Verifikasi Bulk Action Bar hilang

### TC-GS-HHR-194: Ikon × membersihkan seleksi dan menyembunyikan Bulk Action Bar

28. Centang checkbox baris DD-01
29. Centang checkbox baris DD-07
30. Klik ikon `×`
31. Verifikasi kedua checkbox tidak tercentang
32. Verifikasi Bulk Action Bar hilang dan sisi kiri kosong
33. Verifikasi `Status` DD-01 dan DD-07 tidak berubah (`Available`)

### Ganti akun ke Total Control Client L

34. Ganti akun: logout dari akun Total Control Client A
35. Login sebagai Total Control Client L dengan `Spectra.env.GS_CLIENTL_TC_PASSWORD`
36. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-192: Select All memilih seluruh baris eligible lintas halaman lalu menjadi Unselect All

37. Centang checkbox baris pertama
38. Klik tombol `Select All (26 records)`
39. Verifikasi counter `26 Readers selected`
40. Verifikasi tombol berubah menjadi `Unselect All`
41. Buka halaman 2
42. Verifikasi baris halaman 2 tercentang
43. Buka halaman 3
44. Verifikasi baris halaman 3 tercentang
45. Lepas centang satu baris pada halaman 3
46. Verifikasi counter `25 Readers selected`
47. Verifikasi tombol kembali `Select All (26 records)`
48. Klik ikon `×`
49. Verifikasi Bulk Action Bar hilang
50. Verifikasi baris halaman 3 tidak tercentang
51. Buka halaman 2
52. Verifikasi baris halaman 2 tidak tercentang
53. Buka halaman 1

### TC-GS-HHR-193: Seleksi bertahan saat pindah halaman, mengubah Search, Filter, dan Sort

54. Centang checkbox dua baris pertama halaman 1
55. Buka halaman 2 dan centang satu baris
56. Catat `Device Name` ketiga baris tercentang
57. Verifikasi counter `3 Readers selected`
58. Ketik Search `Large Reader - 2`, tekan Enter
59. Verifikasi counter tetap `3 Readers selected` setelah Search
60. Klik `(←)` pada kotak Search
61. Verifikasi counter tetap `3 Readers selected` sesudah Search dihapus
62. Klik ikon Filter untuk membuka panel, pilih `Device Name` = `Large Reader - 2`, lalu klik `[Apply]`
63. Verifikasi counter tetap `3 Readers selected` setelah Filter `Device Name` diterapkan
64. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
65. Verifikasi counter tetap `3 Readers selected` sesudah Filter dihapus
66. Klik ikon Filter untuk menutup panel
67. Klik header kolom `Device Name` untuk mengubah arah sort
68. Verifikasi counter tetap `3 Readers selected` setelah sort diubah
69. Ketik Search `Device Name` persis baris pertama yang dicatat pada langkah 56, tekan Enter
70. Verifikasi baris tersebut tercentang
71. Ganti isi kotak search dengan `Device Name` persis baris kedua yang dicatat pada langkah 56, tekan Enter
72. Verifikasi baris tersebut tercentang
73. Ganti isi kotak search dengan `Device Name` persis baris ketiga yang dicatat pada langkah 56, tekan Enter
74. Verifikasi baris tersebut tercentang
75. Klik `(←)` pada kotak Search
76. Klik ikon `×`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 189, 191, 190, 194 (Client A), ganti akun, lalu 192 dan 193 (Client L). Screening elemen bar dan checkbox disabled lebih dulu, lalu perilaku seleksi. Menyimpang dari urutan nomor TC sumber. Ganti akun ke Client L ditulis eksplisit (langkah 34 sampai 36) dan bagian sesudah ganti akun tetap bermakna bila bagian sebelumnya gagal keras (konvensi bagian 3, kasus b).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 17, 48, dan 76 (mengosongkan seleksi lewat `×`; pada TC-GS-HHR-192 langkah 48 sekaligus aksi yang diuji), langkah 41, 43, 51, dan 53 (pindah halaman), langkah 56 (mencatat nama baris tercentang), langkah 66 (menutup panel Filter agar header kolom dapat diklik), langkah 69, 71, dan 73 (mencari tiap baris tercatat lewat Search `Device Name` persis, Langkah 8 TC-GS-HHR-193), langkah 75 (mengosongkan Search), serta ganti akun 34 sampai 36.
- Asersi absence mengikuti anchor: langkah 12 (bar tidak tampil) didahului langkah 9 (tooltip) dan 11 (baris tidak tercentang). Langkah 12 adalah verifikasi tambahan di luar Expected TC-GS-HHR-191 (b: klik pada checkbox disabled tidak memilih baris), ditulis sebagai asersi pembanding yang dipisah dari langkah 11 (S-01, S-03).
- Pada TC-GS-HHR-192 langkah 42, 44, 50, dan 52 hanya mengasersi keadaan checkbox (tercentang atau tidak) pada halaman yang dibuka sehingga tidak butuh baris pembanding (8b butir 2).
- Pengecualian alasan di atas sekitar 35 langkah (76 langkah): seluruh blok satu kelas (protokol seleksi Bulk Action Bar tanpa aksi bulk yang dikonfirmasi), tidak ada data yang diubah, tiap blok mengosongkan seleksi sebelum blok berikutnya sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan blok Client L berdiri sendiri sesudah ganti akun.
- TC-GS-HHR-195 (kolom Checkbox pada Column Visibility dan export) ada di spec 058.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Sort langkah 67 memindahkan posisi baris yang dicatat pada langkah 54 sampai 56 (dua baris halaman 1 dan satu baris halaman 2), sehingga sesudah langkah 68 tiap baris dicari lewat Search `Device Name` persis (langkah 69 sampai 74) sebelum diasersi tetap tercentang, sesuai Langkah 8 dan Expected c TC-GS-HHR-193 (S-14). Search menyaring dengan kecocokan sebagian nama (mis. `Large Reader - 1` juga memuat `Large Reader - 10` sampai `19`), sehingga yang diasersi adalah baris ber-`Device Name` persis itu.
- Model Filter Panel pada TC-GS-HHR-193: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter (langkah 62 sampai 66).
- Opsi di dalam Bulk Action (eligibility per status) ada di spec 044; Role Matrix visibilitas Bulk Action Bar (TC-GS-HHR-201 sampai 206) ada di spec 008; Selection Limit (TC-GS-HHR-221 dan 222) ada di spec 047.
- Temuan untuk QA:
  - TC-GS-HHR-190 langkah 4 ("Klik checkbox header hingga tercentang penuh") tidak menyebut jumlah klik dari keadaan indeterminate; spec memakai satu klik dan mengasersi hasil 8 baris eligible tercentang.
  - TC-GS-HHR-189 Expected a.i ("rata kiri, sejajar dengan Table Tools yang rata kanan") tidak menyebut cara mengukurnya; spec mengasersi posisi relatif tanpa nilai piksel.
  - TC-GS-HHR-192 dan 193 mensyaratkan Client L (26 reader Available) tetapi email akun Client L tidak tertulis di Pre-setup TC (hanya pola `totalControl_automated_{namaClient}@qwertysystem.net`) dan env var passwordnya belum terdaftar di `spectra.config.ts` maupun `.env.example`; spec memakai `GS_CLIENTL_TC_PASSWORD` (env baru).
  - TC-GS-HHR-193 tidak menyebut urutan default baris pada Client L; spec mencatat nama baris tercentang saat dipilih (langkah 56) dan mencari tiap baris lewat Search `Device Name` persis (langkah 69 sampai 74) sebelum mengasersi tercentang setelah sort.
  - TC-GS-HHR-189 sampai 195 tidak mencantumkan Post Condition.
