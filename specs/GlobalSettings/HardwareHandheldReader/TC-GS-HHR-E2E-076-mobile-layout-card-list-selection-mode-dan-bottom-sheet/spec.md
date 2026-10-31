---
id: TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet
title: "Mobile (Viewport di Bawah 768px): Layout Card List, Toolbar Ikon, Selection Mode, Bottom Sheet, dan Activate Reader Disembunyikan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-437
  - TC-GS-HHR-438
  - TC-GS-HHR-439
  - TC-GS-HHR-440
  - TC-GS-HHR-441
  - TC-GS-HHR-442
  - TC-GS-HHR-443
  - TC-GS-HHR-471
coverage:
  web: automated
---

# Mobile (Viewport di Bawah 768px): Layout Card List, Toolbar Ikon, Selection Mode, Bottom Sheet, dan Activate Reader Disembunyikan

## Prerequisites

- Mode: FE+BE (viewport Mobile, lebar kurang dari 768px, pada browser web). Kelas harness: Mobile. Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: hook suite menyetel flag `guided_tooltip_seen_<page_key>` menjadi true untuk akun aktor. Pengecualian: blok TC-GS-HHR-443 menguji flag itu sendiri, sehingga spec mengatur flag menjadi belum diset sesudah hook (langkah 2). Setelah `[Done]` pada langkah 7 flag menjadi seen kembali.
- Akun:

| Role | Nama user | Email | Env var password |
|---|---|---|---|
| Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Total Control (Client E) | Email mengikuti pola Pre-setup TC `totalControl_automated_{namaClient}@qwertysystem.net`; nilai `{namaClient}` tidak tertulis di Pre-setup TC | | `Spectra.env.GS_CLIENTE_TC_PASSWORD` |

- Nama env var Client E baru dan belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner (satu arti per nama). Password tidak ditulis di spec atau fixture. Login Client A dilakukan di hook `before`; ganti akun ke Client E dilakukan di langkah eksplisit (langkah 60); flag Guided Tooltip akun Client E disetel true oleh hook suite; hook `after` mengembalikan sesi ke akun default suite (Client A) dan viewport ke ukuran default.
- Data (Client A, plan Growth, Seed Reader A dari fixture BE, format tanggal default `dd/MM/yy` 24-hour): DD-01 (`Zebra RFID Reader - 1`, Available, Long Range, Last Scanned `21/06/26 10:15`), DD-03 (Damaged), DD-04 (`Gudang Reader - 2`, Missing, Short Range, Last Scanned `—`), DD-05 (Waiting for Approval), DD-07 (Available). Client E: belum memiliki reader.
- Kemampuan teknis (disediakan tim FE): kontrol ukuran viewport (Mobile < 768px dan pemulihan ke ukuran default); gestur tap dan tekan lama (long-press) pada card list; pengaturan flag Guided Tooltip `guided_tooltip_seen_<page_key>` menjadi belum diset (mekanisme tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA).
- State global yang diubah: ukuran viewport dan flag Guided Tooltip. Pemulihan: langkah pemulihan eksplisit di akhir spec dan hook `after` sebagai cadangan. Spec tidak mengubah data reader (tidak ada aksi Save atau konfirmasi).

## Test Steps

### Guided Tooltip pada Mobile: TC-GS-HHR-443

1. Atur viewport Mobile (lebar kurang dari 768px)
2. Atur flag Guided Tooltip halaman Handheld Reader menjadi belum diset
3. Buka Global Settings > Hardware > Handheld Reader (muat ulang)
4. Amati tombol pada Step 1
5. Verifikasi Step 1 menampilkan tombol `[Done]`
6. Verifikasi Step `Add Hardware` dan Step `Reader Detail` tidak tampil pada Mobile
7. Klik `[Done]`
8. Verifikasi walkthrough tertutup setelah Step 1

### Layout, toolbar, dan isi kartu: TC-GS-HHR-439, TC-GS-HHR-437, TC-GS-HHR-471

9. Amati halaman
10. Verifikasi kartu `Short Range` dan `Long Range` bertumpuk vertikal
11. Verifikasi tabel menjadi card list vertikal
12. Verifikasi toolbar berisi `[⋯]` dan `[🔍]`
13. Verifikasi ikon Changelog berada di header halaman
14. Verifikasi tombol `[+ Activate Reader]` tidak tampil di toolbar
15. Amati kartu DD-01
16. Verifikasi kartu DD-01 menampilkan `Zebra RFID Reader - 1` (tebal)
17. Verifikasi kartu DD-01 menampilkan badge `Available`
18. Verifikasi kartu DD-01 menampilkan `Long Range`
19. Verifikasi kartu DD-01 menampilkan `21/06/26 10:15`
20. Verifikasi kartu DD-01 menampilkan ikon `[⋯]` di pojok kanan
21. Amati kartu DD-04
22. Verifikasi kartu DD-04 menampilkan `Gudang Reader - 2` (tebal)
23. Verifikasi kartu DD-04 menampilkan badge `Missing`
24. Verifikasi kartu DD-04 menampilkan `Short Range`
25. Verifikasi kartu DD-04 menampilkan `Last Scanned` `—`
26. Verifikasi kartu DD-04 menampilkan ikon `[⋯]` di pojok kanan
27. Klik `[⋯]` pada toolbar
28. Verifikasi bottom sheet `[⋯]` memuat Filter, Download, dan Event Log
29. Verifikasi tombol `[+ Activate Reader]` tidak tampil di bottom sheet
30. Tutup bottom sheet `[⋯]`
31. Klik `[🔍]`
32. Verifikasi `[🔍]` membuka inline search

### Row action dan tap kartu: TC-GS-HHR-440

33. Tutup inline search dengan klik `(←)`, klik `[⋯]` pada kartu DD-01
34. Verifikasi menu kartu DD-01 memuat `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`, `Delete`
35. Tutup menu lalu tap kartu DD-03
36. Verifikasi tap kartu membuka Popup `Handheld Reader Detail` DD-03

### Bottom sheet popup dan dialog: TC-GS-HHR-442

37. Tutup Popup Detail, klik `[⋯]` kartu DD-01, klik `Edit Alias Name`
38. Verifikasi dialog Edit Alias Name tampil sebagai bottom sheet dengan konten dan tombol yang sama seperti web
39. Klik `✕` untuk menutup dialog, klik `[⋯]` kartu DD-01, klik `Delete`
40. Verifikasi dialog Delete Reader tampil sebagai bottom sheet dengan konten dan tombol yang sama seperti web
41. Klik `[Cancel]` pada dialog Delete Reader

### Selection mode: TC-GS-HHR-441

42. Tap kartu DD-03 saat belum dalam selection mode
43. Verifikasi tap saat belum dalam selection mode membuka Popup Detail DD-03
44. Tutup Popup Detail, tekan lama kartu DD-01
45. Amati kartu dan bar
46. Verifikasi long-press masuk selection mode: checkbox tampil di kiri tiap kartu
47. Verifikasi kartu DD-01 tercentang
48. Verifikasi Floating Bottom Bulk Bar tampil dengan `[✕]`, counter `1 Selected`, `[Select All]`, dan `Bulk Action`
49. Tap kartu DD-07
50. Verifikasi tap kartu DD-07 menambah centang (counter `2 Selected`)
51. Verifikasi tap kartu DD-07 tidak membuka Popup Detail
52. Tap kartu DD-05
53. Verifikasi kartu DD-05 (Waiting for Approval) tidak dapat dipilih: checkbox disabled
54. Verifikasi tap kartu DD-05 tidak mengubah counter (tetap `2 Selected`)
55. Tap `Bulk Action` pada bar
56. Verifikasi opsi `Bulk Action` untuk seleksi DD-01 dan DD-07: `Mark as Damaged`, `Mark as Missing`, `Delete`
57. Tutup opsi `Bulk Action`, tap `[✕]` pada bar
58. Verifikasi selection mode keluar: checkbox kartu hilang
59. Verifikasi seleksi dibersihkan

### Empty state Client E: TC-GS-HHR-438

60. Ganti akun: logout lalu login sebagai Total Control Client E (viewport tetap Mobile)
61. Buka Global Settings > Hardware > Handheld Reader
62. Verifikasi empty state tampil dengan judul `No handheld reader yet`
63. Verifikasi empty state menampilkan deskripsi `Get started by creating your first handheld reader.`
64. Verifikasi tidak ada tombol aksi pada empty state
65. Verifikasi tombol `[+ Activate Reader]` tidak tampil di Mobile

### Pemulihan

66. Pulihkan viewport ke ukuran default

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 10). Semua TC berlabel Automatable.
- Urutan: Guided Tooltip pertama karena menguji flag yang berubah menjadi seen setelah `[Done]` (prinsip 3 butir 2); layout dan isi kartu, row action, bottom sheet, lalu selection mode (berubah state tampilan), dan empty state Client E paling akhir karena ganti akun. Tidak ada aksi yang mengubah data.
- Spec memuat 66 langkah nominal (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (Mobile, viewport Android), satu akun Total Control Client A (ganti akun ke Client E hanya di akhir untuk empty state), satu dataset Seed Reader A, tanpa aksi yang mengubah data; delapan TC saling berurutan pada layar yang sama sehingga memecahnya hanya menambah login dan pembukaan halaman berulang.
- TC-GS-HHR-437 dan TC-GS-HHR-439 membuka bottom sheet `[⋯]` yang sama; satu pembukaan (langkah 27) dipakai untuk kedua TC (TC-GS-HHR-439 butir c: bottom sheet memuat Filter, Download, dan Event Log; TC-GS-HHR-437: `[+ Activate Reader]` tidak tampil di bottom sheet). TC-GS-HHR-440 butir b dan TC-GS-HHR-441 butir a mengamati tap kartu yang sama (membuka Popup Detail DD-03); TC-GS-HHR-440 diasersi pada langkah 36 dan TC-GS-HHR-441 pada langkah 43 (tap diulang karena Popup Detail ditutup di antaranya).
- Langkah penghubung tanpa `Verifikasi` (S-03): mengatur viewport dan flag, muat ulang, menutup bottom sheet, inline search, menu, popup, dan dialog, mengosongkan pilihan, ganti akun, pemulihan viewport. Dialog Edit Alias Name ditutup dengan `✕` tanpa perubahan (form bersih, tidak ada dialog `Unsaved Changes`) dan dialog Delete Reader ditutup dengan `[Cancel]` (tombol dialog konfirmasi) tanpa menghapus data.
- Bottom sheet dibuka dari menu kartu untuk dua dialog (Edit Alias Name dan Delete Reader) sehingga ada dua pembukaan sesuai dua kejadian TC-GS-HHR-442.
- Temuan untuk QA:
  - TC-GS-HHR-443 precondition e ("Flag guided tooltip belum diset") tidak menyebut mekanisme mengatur flag; spec mengaturnya lewat kemampuan yang disediakan tim FE tanpa mengarang endpoint.
  - TC-GS-HHR-443 tidak menyebut cara memeriksa bahwa Step `Add Hardware` dan Step `Reader Detail` tidak tampil selain tidak muncul setelah Step 1; spec mengasersi keduanya tidak tampil sebelum `[Done]` dan walkthrough tertutup sesudahnya.
  - TC-GS-HHR-441 langkah 6 dan expected e menyebut "opsi `Bulk Action` untuk seleksi DD-01 dan DD-07" tanpa menyebut cara menutup menu opsi; spec menutupnya dengan menutup menu lalu tap `[✕]`.
  - TC-GS-HHR-442 tidak menyebut cara menutup dialog Edit Alias Name dan Delete Reader pada Mobile; spec memakai `✕` dan `[Cancel]` sesuai konvensi bagian 9.
  - TC-GS-HHR-438 memakai Client E tanpa email di Pre-setup TC (hanya pola `{namaClient}`), dan password memakai env var baru yang belum terdaftar.
