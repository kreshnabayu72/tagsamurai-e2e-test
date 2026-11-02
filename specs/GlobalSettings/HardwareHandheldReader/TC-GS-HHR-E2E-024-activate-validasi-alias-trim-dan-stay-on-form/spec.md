---
id: TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form
title: "Activate Reader: Validasi Alias Name (Batas 120, Emoji), Trim Alias, Brand, dan Model/Type, serta Checkbox Stay on this form"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-99
  - TC-GS-HHR-100
  - TC-GS-HHR-101
  - TC-GS-HHR-446
  - TC-GS-HHR-447
  - TC-GS-HHR-467
  - TC-GS-HHR-468
coverage:
  web: automated
---

# Activate Reader: Validasi Alias Name (Batas 120, Emoji), Trim Alias, Brand, dan Model/Type, serta Checkbox Stay on this form

## Prerequisites

- Mode: FE+BE. Backend nyata dengan fixture backend; reader hasil aktivasi dipulihkan oleh spec sendiri (lihat langkah penghubung) dan hook `after`.
- Suite serial (`parallel: false`). State global yang diubah spec ini: (a) tiga aktivasi sukses (reader `Zebra RFID Reader - 2` dari unit `SN-HHR-00201` pada langkah 32 dan 51, dan reader `Chainway C72 - 2` dari `SN-HHR-00302` pada langkah 71), (b) kolom `Brand` dan `Model/Type` pada tabel daftar diaktifkan lewat Overlay Column Visibility (langkah 73). Dua reader pertama dihapus oleh spec lewat `Delete` agar kuota `Long Range` pulih (NC-06: Delete reader Jalur A mengembalikan unit ke `Available` di Hardware Stock). Hook `after` memulihkan seluruhnya (hapus reader sisa, nonaktifkan kembali kolom `Brand` dan `Model/Type`, pulihkan Seed Reader A lewat fixture backend).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, `Long Range` terpakai 5 dari 6, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. Katalog Device Name DN-01 sampai DN-07 (Admin Console, dibaca read-only oleh Client A); `Chainway C72` (DN-01) sudah dipakai DD-05 dengan `N` terpakai 1. HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm, nomor urut 2) tersedia di stok Principal; `SN-HHR-00302` di luar stok.
- Data Dinamis: nilai uji Alias Name literal dari TC: 120 dan 121 karakter `A`, emoji `😊`, `  Reader Dock 01-{runId}-024  ` (spasi di awal dan akhir, suffix per run mengikuti S-12), Brand `  Chainway  ` dan Model/Type `  C72  `. Nama baris hasil aktivasi (`Zebra RFID Reader - 2`, `Chainway C72 - 2`) mengikuti penomoran HHR-LOGIC-02g dan dipakai apa adanya karena Expected TC menyebutnya. Fixture baru `Fixture.hardwareHandheldReader.aliasTrimStay024`.
- Kemampuan teknis: simulator reader USB (sambung dan cabut reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); menempel (paste) teks ke field; menyuntikkan nilai langsung ke DOM field `Alias Name` (melewati filter keystroke FE, TC-GS-HHR-101); membaca total reader pada daftar.

## Test Steps

### TC-GS-HHR-99: Alias Name 121 karakter menonaktifkan Submit dengan pesan inline

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
4. Klik `[Sync]`
5. Isi `Alias Name` dengan 121 karakter `A`
6. Verifikasi pesan inline `Max. 120 characters` tampil
7. Verifikasi `[Submit]` disabled
8. Hapus satu karakter sehingga `Alias Name` berisi 120 karakter `A`
9. Verifikasi pesan inline `Max. 120 characters` tidak tampil
10. Verifikasi `[Submit]` enabled
11. Klik `[Clear Field]`

### TC-GS-HHR-100: Emoji pada Alias Name saat aktivasi diblok di input

12. Ketik emoji `😊` pada `Alias Name`
13. Tempel emoji `😊` pada `Alias Name`
14. Verifikasi `Alias Name` tetap kosong (emoji tidak pernah masuk ke field)
15. Verifikasi tidak ada pesan error pada `Alias Name`

### TC-GS-HHR-101: Emoji pada Alias Name yang lolos filter FE ditolak server saat aktivasi

16. Suntikkan nilai `😊` langsung ke DOM field `Alias Name` (melewati filter keystroke FE)
17. Klik `[Submit]`
18. Verifikasi pesan inline `Alias name contains invalid characters` tampil (penolakan server 422)
19. Verifikasi Popup Activate tetap terbuka
20. Verifikasi input dipertahankan: `Serial Number` tetap `SN-HHR-00201`
21. Klik `[✕]`
22. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
23. Klik `[Cancel Activation]`
24. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
25. Verifikasi empty state "No results found" tampil (tidak ada reader baru)
26. Klik `(←)` pada kotak Search

### TC-GS-HHR-446: Spasi awal dan akhir Alias Name dibuang saat Submit aktivasi

27. Klik `[+ Activate Reader]`
28. Klik `Long Range` pada Overlay `Select Range Type`
29. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
30. Klik `[Sync]`
31. Isi `Alias Name` dengan `  Reader Dock 01-{runId}-024  ` (spasi di awal dan akhir)
32. Klik `[Submit]`
33. Verifikasi toast sukses "Success, Reader Dock 01-{runId}-024 has been activated."
34. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
35. Verifikasi kolom `Alias Name` baris `Zebra RFID Reader - 2` menampilkan `Reader Dock 01-{runId}-024` tanpa spasi tepi
36. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
37. Klik `[Delete]` pada dialog
38. Tunggu aksi selesai
39. Klik `(←)` pada kotak Search

### TC-GS-HHR-468 dan TC-GS-HHR-467: Checkbox Stay on this form default tidak tercentang, tidak ikut di-reset Clear Field, dan popup kembali ke state Menunggu Sync setelah Submit berhasil

40. Klik `[+ Activate Reader]`
41. Klik `Long Range` pada Overlay `Select Range Type`
42. Verifikasi checkbox `Stay on this form after submitting` tampil tepat di atas `[Submit]`
43. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang
44. Centang checkbox `Stay on this form after submitting`
45. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
46. Klik `[Sync]`
47. Isi `Alias Name` dengan `Reader Dock 01-{runId}-024`
48. Klik `[Clear Field]`
49. Verifikasi `Alias Name` kosong
50. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
51. Klik `[Submit]`
52. Verifikasi toast sukses "Success, Zebra RFID Reader - 2 has been activated."
53. Verifikasi Popup Activate tetap terbuka pada state Menunggu Sync dengan Range Type `Long Range`
54. Verifikasi `Serial Number`, label jalur, slider `Reader Power`, dan `Alias Name` tidak tampil
55. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
56. Klik `[✕]`
57. Verifikasi Popup Activate tertutup langsung tanpa dialog `Cancel Activation`
58. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
59. Verifikasi baris `Zebra RFID Reader - 2` tampil di daftar
60. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
61. Klik `[Delete]` pada dialog
62. Tunggu aksi selesai
63. Klik `(←)` pada kotak Search

### TC-GS-HHR-447: Spasi awal dan akhir Brand dan Model/Type Jalur B dibuang saat Submit aktivasi

64. Klik `[+ Activate Reader]`
65. Klik `Long Range` pada Overlay `Select Range Type`
66. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` lewat simulator USB
67. Klik `[Sync]`
68. Pilih `Chainway C72` pada `Device Name`
69. Isi `Brand` dengan `  Chainway  ` (spasi di awal dan akhir)
70. Isi `Model/Type` dengan `  C72  ` (spasi di awal dan akhir)
71. Klik `[Submit]`
72. Verifikasi toast sukses "Success, Chainway C72 - 2 has been activated."
73. Aktifkan kolom `Brand` dan `Model/Type` lewat Overlay Column Visibility
74. Ketik Search `Chainway C72 - 2`, tekan Enter
75. Verifikasi baris baru dengan `Device Name` `Chainway C72 - 2`
76. Verifikasi kolom `Brand` baris `Chainway C72 - 2` menampilkan `Chainway` tanpa spasi tepi
77. Verifikasi kolom `Model/Type` baris `Chainway C72 - 2` menampilkan `C72` tanpa spasi tepi
78. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok mengikuti konvensi bagian 3: validasi yang diblokir (TC-GS-HHR-99, 100, 101) memakai satu Popup Activate dan tidak membuat data; sesudahnya aksi sukses (TC-GS-HHR-446, TC-GS-HHR-468 dan 467, TC-GS-HHR-447). Urutan menyimpang dari nomor TC karena TC-GS-HHR-468 (Clear Field dan checkbox) dan TC-GS-HHR-467 (Submit dengan Stay) digabung dalam satu popup: checkbox yang sudah tercentang oleh TC-GS-HHR-468 dipakai oleh Submit TC-GS-HHR-467 (langkah centang TC-GS-HHR-467 sudah terpenuhi oleh langkah centang TC-GS-HHR-468).
- Popup Activate dibuka 4 kali (validasi, TC-GS-HHR-446, TC-GS-HHR-468 dan 467, TC-GS-HHR-447) dan ditutup 4 kali: popup validasi lewat `[✕]` dan `[Cancel Activation]`, tiga popup lainnya lewat Submit sukses atau `[✕]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): penyambungan reader di simulator USB, `[Sync]`, `[Clear Field]` setelah TC-GS-HHR-99 (agar TC-GS-HHR-100 memulai dari field kosong, S-09), Search untuk menemukan baris target dan `(←)` untuk mengosongkan Search, pengaktifan kolom `Brand` dan `Model/Type` (langkah 73), serta `Delete` reader hasil TC-GS-HHR-446 dan TC-GS-HHR-467 sesudah diasersi, masing-masing diikuti "Tunggu aksi selesai" (langkah 38 dan 62; hasil `Delete` tidak diasersi dan aktivasi berikutnya bergantung pada kuota dan stok, bagian 8b butir 8). `Delete` ini mengembalikan kuota `Long Range` ke `5 of 6` sehingga `Long Range` tidak diblok gate kuota pada popup berikutnya, dan mengembalikan unit `SN-HHR-00201` ke `Available` di Hardware Stock (NC-06) agar serial itu dapat dipakai TC berikutnya. Karena Delete adalah pemulihan, bukan objek uji, tidak ada `Verifikasi` atasnya.
- Pengecualian P-5: TC-GS-HHR-101 (menyuntikkan emoji langsung ke DOM, ditolak server) adalah satu TC objek-uji ringan kelas a (defense-in-depth) yang berbagi permukaan Popup Activate dan field `Alias Name` dengan TC-GS-HHR-99 dan 100 tanpa harness eksternal dan tanpa state berat sendiri.
- Spec melewati sekitar 35 langkah (78 langkah). Alasan: seluruhnya satu kelas harness (kelas d: simulator USB) dan satu topik (validasi dan normalisasi input pada Popup Activate) dengan dataset yang sama. Blok validasi (tanpa data) dan blok aksi sukses berdiri sendiri; setiap blok sukses membuka popup baru dan memulihkan state sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Alias Name TC-GS-HHR-446 dan 468 (`Reader Dock 01`) ditulis bersuffix per run (`Reader Dock 01-{runId}-024`) mengikuti S-12; asersi memakai nilai bersuffix yang sama.
- Pembagian TC lintas spec: TC-GS-HHR-95 dan 98 (saving state dan klik ganda Submit) ada di spec 025; TC-GS-HHR-96 dan 97 (kegagalan 5xx dan timeout saat Submit) ada di spec 026.
- Temuan untuk QA:
  - Ketujuh TC berlabel `Manual Only` (b) di TC sumber (reader USB fisik) tetapi tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-99 menulis "Dengan 120 karakter pesan hilang dan `[Submit]` enabled" tanpa langkah; spec menambah langkah menghapus satu karakter dari 121 karakter sebagai penghubung.
  - Expected TC-GS-HHR-100 "tidak ada pesan error" adalah absence tanpa anchor di TC; spec memakai field `Alias Name` yang tetap kosong sebagai anchor positif.
  - Pemulihan antar-aktivasi (`Delete` reader hasil aktivasi) bergantung pada asumsi bahwa Delete reader Jalur A mengembalikan unit ke `Available` (NC-06) dan menghasilkan nama bawaan yang sama (`Zebra RFID Reader - 2`, nomor urut unit HS-01) pada aktivasi berikutnya. TC tidak menyatakan nama pada aktivasi ulang unit yang sama; bila nama berbeda, Expected TC-GS-HHR-467 a perlu disesuaikan.
  - TC-GS-HHR-446 dan 447 tidak menyebut Post Condition; tidak ada yang diasersi.
  - Kolom `Brand` dan `Model/Type` berstatus Hidden secara default (PRD §4.1); TC-GS-HHR-447 langkah 7 mengaktifkannya lewat Overlay Column Visibility dan spec mengikutinya.
