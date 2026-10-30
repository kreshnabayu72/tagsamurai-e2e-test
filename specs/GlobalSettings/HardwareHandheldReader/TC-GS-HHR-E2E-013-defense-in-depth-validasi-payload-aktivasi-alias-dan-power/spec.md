---
id: TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power
title: "Defense-in-Depth: Validasi Payload Aktivasi, Alias Name, dan Reader Power Lewat Request Langsung ke Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-417
  - TC-GS-HHR-418
  - TC-GS-HHR-419
  - TC-GS-HHR-420
  - TC-GS-HHR-421
  - TC-GS-HHR-422
  - TC-GS-HHR-423
  - TC-GS-HHR-424
  - TC-GS-HHR-425
  - TC-GS-HHR-448
  - TC-GS-HHR-449
  - TC-GS-HHR-482
  - TC-GS-HHR-483
coverage:
  web: automated
---

# Defense-in-Depth: Validasi Payload Aktivasi, Alias Name, dan Reader Power Lewat Request Langsung ke Server

## Prerequisites

- Mode: FE+BE. Kelas harness: defense-in-depth (kelas a, request langsung ke server tanpa melalui UI; injeksi markup pada TC-GS-HHR-425). Suite `parallel: false`.
- Klien HTTP: klien HTTP yang mengirim request langsung ke server dengan sesi Sari Dewi (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi pada request langsung hanya respons server (status dan pesan) dan state data; perilaku FE untuk respons yang sama tidak diasersi pada langkah request (bagian 8b butir 1). Event Log dibaca lewat UI sebagai state data (baris `Failed`). Endpoint request tidak didefinisikan di TC dan tidak ditulis di spec ini; kontrak operasi mengikuti dokumen API modul yang disediakan tim FE/BE.
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar reader Client A beserta `Status`, `Alias Name`, `Reader Power` per reader, dan jumlah reader.
- Kemampuan teknis: penangkap dialog JavaScript browser (untuk memastikan `alert` tidak berjalan pada TC-GS-HHR-425) dan simulator reader USB tidak dibutuhkan (semua aktivasi dikirim sebagai request langsung).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun aktor (Tabel Data Uji Pre-setup #1, Client A):

| Role | Nama user | Email | Env var password |
|---|---|---|---|
| Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |

- Login Sari Dewi dilakukan di hook `before` (UI dan sesi klien HTTP); hook `after` memulihkan Seed Reader A dan kolom `Model/Type` ke keadaan awal, lalu mengembalikan sesi ke akun default suite.
- Data: Client A (plan Growth, toggle BYO aktif, alokasi `Short Range` 8 dan `Long Range` 6) dengan Seed Reader A (DD-01 s.d. DD-10) dan katalog Device Name Client A DN-01 s.d. DN-07 (dibaca read-only; DN-01 `Chainway C72`, DN-03 `Unitech EA520`). Target Edit memakai DD-01 (Available, Long Range, `Reader Power` `30 dBm`, `Alias Name` `—`) dan DD-02 (Short Range). Serial Number: `SN-HHR-00201` (stok HS-01, Long Range) untuk TC-GS-HHR-448 dan TC-GS-HHR-449; `SN-HHR-00302` (Jalur B, bebas) untuk TC-GS-HHR-421, TC-GS-HHR-422, TC-GS-HHR-423, TC-GS-HHR-482, dan TC-GS-HHR-483. Request yang ditolak tidak membuat data; satu-satunya request yang diterima (TC-GS-HHR-422) dan perubahan `Alias Name` DD-01 (TC-GS-HHR-425) memakai Seed Reader A bersama dan dipulihkan fixture BE (lihat Temuan untuk QA tentang S-06).
- Nilai request: Reader Power 25 pada TC-GS-HHR-417; `Alias Name` dan `Brand` 121 karakter `A` pada TC-GS-HHR-423, TC-GS-HHR-424, dan TC-GS-HHR-449 (nilai batas, tanpa suffix karena ditolak); Reader Power 4 dan 31 (TC-GS-HHR-418, TC-GS-HHR-419, TC-GS-HHR-448).
- State global yang diubah: Seed Reader A (`Alias Name` DD-01 dan satu reader baru pada TC-GS-HHR-422), kolom `Model/Type` pada Column Visibility; dipulihkan oleh langkah pemulihan dan hook `after`.
- Tanggal pada Event Log mengikuti format default Client A (`dd/MM/yy`, 24-hour, Asia/Jakarta); spec tidak mengasersi nilai tanggal.

## Test Steps

### Edit Reader Power: TC-GS-HHR-417, TC-GS-HHR-418, TC-GS-HHR-419

1. Kirim request langsung Edit Reader Power DD-02 (Short Range) dengan nilai 25
2. Verifikasi server menolak dengan pesan `Reader power configuration is only supported for Long Range devices`
3. Verifikasi (lewat fixture BE) `Reader Power` DD-02 tidak berubah (tetap `—`)
4. Kirim request langsung Edit Reader Power DD-01 dengan nilai 4
5. Verifikasi server menolak dengan pesan `Reader power must be between 5 and 30 dBm`
6. Verifikasi (lewat fixture BE) `Reader Power` DD-01 tetap `30 dBm`
7. Kirim request langsung Edit Reader Power DD-01 dengan nilai 31
8. Verifikasi server menolak dengan pesan `Reader power must be between 5 and 30 dBm`
9. Verifikasi (lewat fixture BE) `Reader Power` DD-01 tetap `30 dBm`

### Edit Alias Name: TC-GS-HHR-424

10. Kirim request langsung Edit Alias Name DD-01 dengan 121 karakter `A`
11. Verifikasi server menolak dengan status 422
12. Verifikasi (lewat fixture BE) `Alias Name` DD-01 tetap `—`

### Aktivasi langsung ditolak: TC-GS-HHR-420, TC-GS-HHR-448, TC-GS-HHR-449, TC-GS-HHR-421, TC-GS-HHR-423, TC-GS-HHR-482, TC-GS-HHR-483

13. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
14. Kirim request aktivasi langsung tanpa Serial Number untuk Long Range
15. Verifikasi server menolak dengan status 422 dan pesan `Serial number must not be empty`
16. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
17. Klik ikon Event Log
18. Verifikasi jumlah baris Event Log sama dengan baseline (tidak ada baris baru)
19. Tutup popup Event Log
20. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
21. Kirim request aktivasi langsung untuk `SN-HHR-00201` Long Range dengan Reader Power 31
22. Verifikasi server menolak dengan status 422 dan pesan `Reader power must be between 5 and 30 dBm`
23. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
24. Verifikasi kartu `Long Range` tetap `5 of 6`
25. Klik ikon Event Log
26. Verifikasi jumlah baris Event Log bertambah satu dari baseline
27. Verifikasi baris `Failed` baru memuat `Range Type` `Long Range`, `Device Name` `Zebra RFID Reader (SKU-HHR-01)`, dan `PIC` `Sari D`
28. Tutup popup Event Log
29. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
30. Kirim request aktivasi langsung untuk `SN-HHR-00201` Long Range dengan `Alias Name` 121 karakter `A`
31. Verifikasi server menolak dengan status 422 dan pesan `Max. 120 characters`
32. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
33. Klik ikon Event Log
34. Verifikasi jumlah baris Event Log bertambah satu dari baseline
35. Verifikasi baris `Failed` baru memuat `Range Type` `Long Range`, `Device Name` `Zebra RFID Reader (SKU-HHR-01)`, dan `PIC` `Sari D`
36. Verifikasi alias yang ditolak tidak tampil pada baris `Failed` baru
37. Tutup popup Event Log
38. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
39. Kirim request aktivasi langsung Jalur B untuk `SN-HHR-00302` dengan ID Device Name `Chainway C72`, `SKU` kosong, `Brand` kosong, dan `Model/Type` `C72`
40. Verifikasi server menolak dengan status 422 dan pesan `Brand is required when SKU is empty.`
41. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
42. Klik ikon Event Log
43. Verifikasi jumlah baris Event Log bertambah satu dari baseline
44. Verifikasi baris `Failed` baru memuat `Device Name` `Chainway C72` (tanpa ` - [N]`)
45. Tutup popup Event Log
46. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
47. Kirim request aktivasi langsung Jalur B untuk `SN-HHR-00302` dengan ID Device Name `Chainway C72`, `Brand` 121 karakter `A`, dan `Model/Type` `C72`
48. Verifikasi server menolak dengan status 422 dan pesan `Max. 120 characters`
49. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
50. Klik ikon Event Log
51. Verifikasi jumlah baris Event Log bertambah satu dari baseline
52. Verifikasi baris `Failed` baru memuat `Device Name` `Chainway C72`
53. Tutup popup Event Log
54. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
55. Kirim request aktivasi langsung Jalur B untuk `SN-HHR-00302` tanpa ID Device Name, dengan `Brand` `Chainway` dan `Model/Type` `C72`
56. Verifikasi server menolak dengan status 422 dan pesan `Device name is required.`
57. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
58. Klik ikon Event Log
59. Verifikasi jumlah baris Event Log bertambah satu dari baseline
60. Verifikasi baris `Failed` baru memuat `Device Name` `—` dan `SKU` `—`
61. Tutup popup Event Log
62. Klik ikon Event Log, catat jumlah baris sebagai baseline, lalu tutup popup
63. Kirim request aktivasi langsung Jalur B untuk `SN-HHR-00302` dengan ID Device Name yang tidak ada di katalog Client A, `Brand` `Chainway`, dan `Model/Type` `C72`
64. Verifikasi server menolak dengan status 422 dan pesan `Device name is required.`
65. Verifikasi (lewat fixture BE) tidak ada reader baru (jumlah reader Client A tetap 10)
66. Klik ikon Event Log
67. Verifikasi jumlah baris Event Log bertambah satu dari baseline
68. Verifikasi baris `Failed` baru memuat `Device Name` `—` dan `SKU` `—`
69. Tutup popup Event Log

### Markup pada Alias Name: TC-GS-HHR-425

70. Buka Overlay row action DD-01, klik `Edit Alias Name`
71. Isi `Alias Name` dengan `<script>alert(1)</script>`, klik `[Save]`
72. Verifikasi tidak ada dialog JavaScript `alert` yang berjalan
73. Verifikasi kolom `Alias Name` baris DD-01 pada tabel menampilkan teks `<script>alert(1)</script>` apa adanya
74. Klik `Zebra RFID Reader - 1` untuk membuka Popup Detail DD-01
75. Verifikasi Popup Detail menampilkan teks `<script>alert(1)</script>` apa adanya
76. Tutup Popup Detail
77. Klik ikon Changelog
78. Verifikasi Modal Changelog menampilkan teks `<script>alert(1)</script>` apa adanya
79. Tutup Modal Changelog

### Aktivasi Jalur B tanpa Model/Type diterima: TC-GS-HHR-422

80. Kirim request aktivasi langsung Jalur B untuk `SN-HHR-00302` dengan ID Device Name `Unitech EA520`, `Brand` `Unitech`, dan `Model/Type` kosong
81. Verifikasi server menerima request tanpa pesan penolakan
82. Muat ulang halaman Handheld Reader
83. Aktifkan kolom `Model/Type` lewat Column Visibility
84. Verifikasi baris baru `Unitech EA520 - 2` tampil dengan `Source` `Self-Purchased`
85. Verifikasi kolom `Model/Type` baris `Unitech EA520 - 2` menampilkan `—`
86. Nonaktifkan kembali kolom `Model/Type` lewat Column Visibility
87. Pulihkan Seed Reader A lewat fixture BE (menghapus reader hasil TC-GS-HHR-422 dan memulihkan `Alias Name` DD-01)

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 8 Security & Defense-in-Depth). Kelas harness: defense-in-depth (a), prinsip 13a konvensi bagian 3. Keputusan P-4 user: TC defense-in-depth yang Expected-nya berupa respons API tetap dimasukkan sebagai spec FE+BE. TC-GS-HHR-425 memakai jalur UI hanya sebagai pemicu injeksi markup (objek uji defense-in-depth XSS, kelas a). TC defense-in-depth lain ada di `TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server` dan `TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server`.
- Spec melewati sekitar 35 langkah (87 langkah nominal). Alasan: seluruh blok satu kelas harness (defense-in-depth, satu akun aktor, tanpa harness eksternal) dan tiap request punya baseline, request, dan asersi sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pola baseline Event Log, request, lalu pembacaan Event Log diulang untuk tujuh request aktivasi (langkah 13 sampai 69).
- Urutan: validasi diblokir lebih dulu, lalu TC yang mengubah data (TC-GS-HHR-425 mengubah `Alias Name` DD-01 sehingga berada sesudah TC-GS-HHR-424 yang mengasersi `Alias Name` DD-01 tetap `—`), dan TC-GS-HHR-422 (request yang diterima, membuat reader) paling akhir karena `SN-HHR-00302` dipakai TC-GS-HHR-421, TC-GS-HHR-423, TC-GS-HHR-482, dan TC-GS-HHR-483 yang harus berstatus belum aktif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): mencatat baseline Event Log (langkah 13, 20, 29, 38, 46, 54, 62), menutup popup Event Log (langkah 19, 28, 37, 45, 53, 61, 69), menutup Popup Detail dan Modal Changelog (langkah 76, 79), memuat ulang halaman dan mengaktifkan lalu menonaktifkan kolom `Model/Type` (langkah 83, 86, S-09), dan pemulihan Seed Reader A (langkah 87).
- Asersi "tidak ada baris baru" di Event Log (TC-GS-HHR-420) memakai baseline jumlah baris yang dicatat sebelum request (S-12) dan didahului request yang ditolak server sebagai anchor positif (bagian 8b butir 2); spec absence kelas g untuk TC ini tidak ada sehingga asersi ditulis di spec ini (S-05).
- TC-GS-HHR-448 dan TC-GS-HHR-449 (juga TC-GS-HHR-482 dan TC-GS-HHR-483) membaca Event Log sebagai asersi pencatatan baris `Failed` (Expected TC); baris baru diidentifikasi lewat selisih jumlah baris terhadap baseline dan isi baris `Failed` terbaru.
- Temuan untuk QA:
  - TC-GS-HHR-417 tidak menyebut nilai Reader Power request (spec memakai 25). TC-GS-HHR-421, TC-GS-HHR-422, TC-GS-HHR-423, TC-GS-HHR-482, dan TC-GS-HHR-483 tidak menyebut Range Type request; spec tidak menebaknya (nilai valid disediakan tim FE).
  - TC-GS-HHR-417 dan TC-GS-HHR-422 menyatakan server menolak atau menerima tanpa menyebut kode status; spec memakai pesan penolakan dan state data. TC-GS-HHR-422 tidak menyebut Range Type request sehingga kuota yang terpakai tidak diketahui; Seed Reader A memuat `Unitech EA520 - 1` (DD-08, Short Range) sehingga hasil `Unitech EA520 - 2` mengikuti counter `N` Device Name tersebut.
  - TC-GS-HHR-420 menetapkan "Tidak ada baris baru di Event Log karena permintaan tidak memiliki Serial Number" tanpa langkah baseline; spec menambah baseline jumlah baris (S-12). TC-GS-HHR-421, TC-GS-HHR-423, TC-GS-HHR-482, dan TC-GS-HHR-483 juga tidak menyebut baseline.
  - TC-GS-HHR-483 menyebut "ID Device Name yang tidak ada di katalog" tanpa nilai; nilai ID disediakan tim FE.
  - TC-GS-HHR-421 menyebut Device Name `Chainway C72` untuk baris `Failed` tanpa ` - [N]`, sedangkan TC-GS-HHR-448 dan TC-GS-HHR-449 memakai `Zebra RFID Reader (SKU-HHR-01)` (Jalur A dengan nama SKU); aturan penamaan baris `Failed` mengikuti TC.
  - TC-GS-HHR-425 mengubah `Alias Name` DD-01 (Seed Reader A bersama) lewat UI tanpa langkah pemulihan di TC; TC-GS-HHR-422 dan TC-GS-HHR-424 menarget Seed Reader A pula, padahal S-06 mewajibkan data milik spec. Reader milik spec tidak dapat ditambahkan karena kuota `Long Range` Client A sudah terpakai 5 dari 6; spec memulihkan Seed Reader A lewat fixture BE.
  - TC-GS-HHR-425 menyatakan "tidak ada script berjalan" tanpa cara pengamatan; spec memakai penangkap dialog JavaScript browser.
  - TC-GS-HHR-449 butir c ("alias yang ditolak tidak tampil") tidak menyebut kolom Event Log yang memuat alias; spec mengasersi alias tidak tampil pada baris `Failed` baru.
