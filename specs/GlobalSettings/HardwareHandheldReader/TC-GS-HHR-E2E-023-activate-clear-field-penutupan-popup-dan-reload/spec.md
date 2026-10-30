---
id: TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload
title: "Activate Reader: Clear Field, Penutupan Popup (X, Esc, Backdrop, Dialog Cancel Activation), dan Reload Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-85
  - TC-GS-HHR-86
  - TC-GS-HHR-87
  - TC-GS-HHR-88
  - TC-GS-HHR-89
  - TC-GS-HHR-90
  - TC-GS-HHR-91
  - TC-GS-HHR-92
  - TC-GS-HHR-93
  - TC-GS-HHR-94
  - TC-GS-HHR-102
coverage:
  web: automated
---

# Activate Reader: Clear Field, Penutupan Popup (X, Esc, Backdrop, Dialog Cancel Activation), dan Reload Halaman

## Prerequisites

- Mode: FE+BE. Backend nyata dengan fixture backend. Tidak ada data yang dibuat atau diubah spec ini (tidak ada Submit sukses).
- Suite serial (`parallel: false`). State global yang diubah spec ini: sesi login berpindah ke Total Control Client B pada langkah 83; hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader pada akun aktor pertama (Client A); langkah buka halaman di `## Test Steps` hanya ada sesudah ganti akun (langkah 83).
- Akun aktor pertama (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Akun kedua (ganti akun eksplisit di langkah 83): Total Control Client B, email dari `Fixture.hardwareHandheldReader.clientBTotalControl` (pola `totalControl_automated_{namaClient}@qwertysystem.net`), password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Client B: plan Growth, toggle `Allow Self-Purchased Device Activation` nonaktif, alokasi `Short Range` 3 dan `Long Range` 3, belum ada reader.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, `Long Range` terpakai 5 dari 6, total reader N = 10 (dari seeding). Katalog Device Name DN-01 sampai DN-07 (Admin Console, dibaca read-only oleh Client A). HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm) tersedia di stok Principal; `SN-HHR-00302` di luar stok. SKU Jalur B `SKU-HHR-03` (Brand `Chainway`, Model/Type `C66`) tersedia di pemilih `SKU`. Fixture baru `Fixture.hardwareHandheldReader.penutupanPopup023`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: simulator reader USB (sambung dan cabut reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); klik di area backdrop di luar popup; menangani dialog konfirmasi bawaan browser (`beforeunload`) saat `F5`: mengamati bahwa dialog muncul lalu membatalkannya (S-08); ganti akun (logout lalu login).

## Test Steps

### TC-GS-HHR-94: Klik backdrop di luar Popup Activate diabaikan

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Klik area backdrop di luar popup
4. Verifikasi Popup Activate tetap terbuka
5. Verifikasi tidak ada dialog konfirmasi

### TC-GS-HHR-85: Clear Field Jalur B mengosongkan Alias, Device Name, SKU, Brand, dan Model/Type tanpa menyentuh hasil Sync

6. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` lewat simulator USB
7. Klik `[Sync]`
8. Pilih `Chainway C72` pada `Device Name`
9. Pilih `SKU-HHR-03` pada `SKU` (`Brand` dan `Model/Type` terisi otomatis)
10. Isi `Alias Name` dengan `Reader Dock 01`
11. Klik `[Clear Field]`
12. Verifikasi `Device Name` kembali ke placeholder
13. Verifikasi `SKU` kembali ke placeholder
14. Verifikasi `Alias Name` kosong
15. Verifikasi `Brand` kosong
16. Verifikasi `Model/Type` kosong
17. Verifikasi status validasi field pristine
18. Verifikasi `Serial Number` tetap `SN-HHR-00302`
19. Verifikasi Range Type tetap `Long Range`
20. Verifikasi slider `Reader Power` kembali `30 dBm`
21. Verifikasi Popup Activate tetap terbuka
22. Verifikasi tidak ada dialog konfirmasi

### TC-GS-HHR-86: Clear Field Jalur A mengosongkan Alias dan mengembalikan slider ke 30 dBm tanpa membuka kunci Brand dan Model

23. Cabut reader `SN-HHR-00302`, lalu sambungkan reader USB dengan Serial Number `SN-HHR-00201` (stok Principal) lewat simulator USB
24. Klik `[Sync]`
25. Isi `Alias Name` dengan `Reader Dock 01`
26. Geser slider `Reader Power` ke 15 dBm
27. Klik `[Clear Field]`
28. Verifikasi `Alias Name` kosong
29. Verifikasi slider `Reader Power` kembali `30 dBm`
30. Verifikasi label `Official` tidak berubah
31. Verifikasi `Brand` tetap `Zebra` dan terkunci
32. Verifikasi `Model/Type` tetap `RFD40` dan terkunci
33. Verifikasi `Serial Number` tetap `SN-HHR-00201`
34. Verifikasi Popup Activate tetap terbuka
35. Verifikasi tidak ada dialog konfirmasi

### TC-GS-HHR-90: Menutup popup lewat Esc setelah Sync berhasil memunculkan dialog Cancel Activation

36. Tekan `Esc`
37. Verifikasi dialog `Cancel Activation` tampil dengan tombol `[Go Back]` dan `[Cancel Activation]`
38. Klik `[Go Back]`

### TC-GS-HHR-89: Menutup popup lewat X setelah Sync berhasil memunculkan dialog Cancel Activation

39. Klik `[✕]`
40. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
41. Verifikasi Popup Activate masih terbuka di belakang dialog
42. Klik `[Go Back]`

### TC-GS-HHR-91: Go Back pada dialog Cancel Activation mempertahankan hasil Sync dan field yang terisi

43. Cabut reader `SN-HHR-00201`, lalu sambungkan reader USB dengan Serial Number `SN-HHR-00302` lewat simulator USB
44. Klik `[Sync]`
45. Pilih `Chainway C72` pada `Device Name`
46. Isi `Brand` dengan `Chainway`
47. Isi `Model/Type` dengan `C72`
48. Klik `[✕]`
49. Klik `[Go Back]`
50. Verifikasi dialog `Cancel Activation` tertutup
51. Verifikasi Popup Activate tetap terbuka
52. Verifikasi `Serial Number` tetap `SN-HHR-00302`
53. Verifikasi `Device Name` tetap `Chainway C72`
54. Verifikasi `Brand` tetap `Chainway`
55. Verifikasi `Model/Type` tetap `C72`

### TC-GS-HHR-92: Cancel Activation menutup popup dan membatalkan sesi

56. Klik `[✕]`
57. Klik `[Cancel Activation]`
58. Verifikasi Popup Activate tertutup
59. Verifikasi total reader pada daftar tetap 10
60. Verifikasi kartu `Long Range` tetap `5 of 6`

### TC-GS-HHR-87: Menutup popup lewat tombol X sebelum ada hasil Sync langsung tertutup

61. Klik `[+ Activate Reader]`
62. Klik `Long Range` pada Overlay `Select Range Type`
63. Klik `[✕]`
64. Verifikasi Popup Activate tertutup langsung ke daftar reader
65. Verifikasi tidak ada dialog konfirmasi
66. Verifikasi total reader pada daftar tetap 10
67. Verifikasi kartu `Long Range` tetap `5 of 6`

### TC-GS-HHR-88: Menutup popup lewat Esc sebelum ada hasil Sync langsung tertutup

68. Klik `[+ Activate Reader]`
69. Klik `Long Range` pada Overlay `Select Range Type`
70. Tekan `Esc`
71. Verifikasi Popup Activate tertutup langsung ke daftar reader
72. Verifikasi tidak ada dialog konfirmasi

### TC-GS-HHR-102: Reload halaman saat Popup Activate berisi hasil Sync

73. Klik `[+ Activate Reader]`
74. Klik `Long Range` pada Overlay `Select Range Type`
75. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
76. Klik `[Sync]`
77. Tekan `F5` untuk memuat ulang halaman
78. Verifikasi konfirmasi bawaan browser untuk meninggalkan halaman muncul
79. Batalkan konfirmasi bawaan browser
80. Verifikasi Popup Activate tetap terbuka
81. Verifikasi `Serial Number` tetap `SN-HHR-00201`
82. Klik `[✕]`, lalu klik `[Cancel Activation]`

### TC-GS-HHR-93: Menutup popup setelah penolakan V-10 langsung tertutup tanpa dialog Cancel Activation (Client B)

83. Ganti akun: logout, lalu login sebagai Total Control Client B
84. Buka Global Settings > Hardware > Handheld Reader
85. Klik `[+ Activate Reader]`
86. Klik `Long Range` pada Overlay `Select Range Type`
87. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` lewat simulator USB
88. Klik `[Sync]` (ditolak server)
89. Klik `[✕]`
90. Verifikasi Popup Activate tertutup langsung ke daftar reader
91. Verifikasi dialog `Cancel Activation` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Popup Activate pertama (Client A) dibangun sekali dan dipakai berurutan oleh TC-GS-HHR-94, 85, 86, 90, 89, 91, dan 92: TC-GS-HHR-94 sebelum Sync (backdrop), TC-GS-HHR-85 (Jalur B), reader diganti untuk TC-GS-HHR-86 (Jalur A), dialog `Cancel Activation` dibuka lewat `Esc` (TC-GS-HHR-90) dan `[✕]` (TC-GS-HHR-89) dan masing-masing ditutup lewat `[Go Back]`, reader diganti kembali untuk TC-GS-HHR-91 (Jalur B), dan popup ditutup lewat `[Cancel Activation]` (TC-GS-HHR-92). Urutan menyimpang dari urutan nomor TC karena kasus tanpa Sync ditaruh paling awal dan kasus yang menutup popup ditaruh paling akhir (konvensi bagian 3). Pengganti reader di antara TC (Cabut dan sambungkan, `[Sync]`) membangun state yang sama dengan precondition TC masing-masing, sebab Sync ulang dengan reader berbeda mereset input (TC-GS-HHR-83, spec 022).
- Penutupan popup TC-GS-HHR-87 dan 88 memakai popup baru tanpa Sync (kasus "bersih" memerlukan form baru, prinsip 6), TC-GS-HHR-102 popup baru dengan Sync, TC-GS-HHR-93 popup baru di Client B. Total popup dibuka 5 kali dan ditutup 5 kali.
- Langkah penghubung (aksi tanpa `Verifikasi`): penyambungan dan pencabutan reader di simulator USB, `[Sync]`, pengisian field, `[Go Back]` pada dialog `Cancel Activation` setelah diasersi (langkah penutup dialog TC-GS-HHR-90 dan 89), `[✕]` dan `[Cancel Activation]` di akhir TC-GS-HHR-102, serta ganti akun dan buka halaman di langkah 83 dan sesudahnya. `[Sync]` yang ditolak server pada TC-GS-HHR-93 tidak diasersi karena Expected TC hanya meminta penutupan popup; penolakan V-10 diasersi di spec 020.
- Spec melewati sekitar 35 langkah (91 langkah). Alasan: seluruhnya satu kelas harness (kelas d: simulator USB) dan seluruh aksi berada pada Popup Activate yang sama (Clear Field dan penutupan popup). Blok Client A berdiri sendiri; blok ganti akun (Client B, TC-GS-HHR-93) memakai langkah ganti akun eksplisit sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal keras (konvensi bagian 3, pengecualian ganti akun). Tidak ada data yang dibuat sehingga tidak ada cleanup.
- Pembagian TC lintas spec: TC-GS-HHR-75 dan 76 (penolakan V-10 pada Client B) ada di spec 020.
- Temuan untuk QA:
  - Delapan TC (85, 86, 89, 90, 91, 92, 93, 102) berlabel `Manual Only` (b) (reader USB fisik) tetapi tetap ditulis (konvensi bagian 2). TC-GS-HHR-87, 88, dan 94 berlabel `Automatable`. Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-93 menyebut `[Sync]` "ditolak" tanpa Expected penolakan; spec mengikuti langkah dan tidak mengasersi pesan penolakan.
  - Expected TC-GS-HHR-85 a menyebut "status validasi pristine" tanpa menyebut indikatornya (border, pesan, atau state tombol); spec mengasersinya sebagai satu `Verifikasi` dan indikator konkret ditentukan di tahap script.
  - TC-GS-HHR-86 menyebut `Brand` `Zebra` dan `Model/Type` `RFD40` terkunci pada Jalur A, sedangkan TC-GS-HHR-83 (spec 022) menyebut input Jalur B (termasuk `Brand` dan `Model/Type`) direset kosong pada perpindahan jalur.
  - TC-GS-HHR-91 menggunakan Jalur B (`SN-HHR-00302`) sedangkan TC-GS-HHR-89 dan 90 menggunakan Jalur A (`SN-HHR-00201`); spec mengganti reader di antaranya (lihat butir urutan di atas).
  - TC-GS-HHR-102 menyatakan konfirmasi bawaan browser muncul pada `F5`; cara mengamati dan membatalkannya ditulis di Prerequisites (kemampuan teknis) karena tidak diuraikan di TC.
