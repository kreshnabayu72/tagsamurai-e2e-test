---
id: TC-GS-HHR-E2E-048-bulk-status-berubah-sebelum-konfirmasi
title: "Multi-Konteks: Bulk Mark as Damaged saat Sebagian atau Seluruh Reader Terpilih Sudah Diubah Admin Lain Sebelum Konfirmasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-223
  - TC-GS-HHR-224
coverage:
  web: automated
---

# Multi-Konteks: Bulk Mark as Damaged saat Sebagian atau Seluruh Reader Terpilih Sudah Diubah Admin Lain Sebelum Konfirmasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini mengubah status reader Seed Reader A dan memulihkannya (lihat butir pemulihan).
- Layar awal Sesi A: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman) atau pembacaan log (kembali ke halaman).
- Akun Sesi A (UI): Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua (Sesi B, kelas multi-konteks): Admin B Total Control Client A yang memicu perubahan status hanya lewat sesi API; hasil di sesi itu tidak diasersi sehingga tidak butuh sesi UI kedua (P-2). Akun dan kredensial Admin B tidak ada di Tabel Pre-setup TC (TC hanya menyebut "dua sesi Total Control Client A"); disediakan tim FE. Kemampuan "Sesi B memanggil Mark as Damaged atas reader tertentu hingga tersimpan" disediakan tim FE/BE tanpa endpoint yang dikarang.
- Data Pre-setup: Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SKU-HHR-01, Available) dan DD-07 (`Honeywell CK65 - 1`, Available). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya. Spec memulihkannya di awal tiap TC (kemampuan "pulihkan Seed Reader A lewat fixture backend" disediakan tim FE/BE tanpa endpoint yang dikarang), lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Tiga surface log: Changelog Handheld Reader (ikon Changelog di halaman), System Log aktor Sesi A (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action). Baseline jumlah entri dicatat per surface sebelum aksi pemicu pertama.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: dua pelaku (Sesi A UI dan Sesi B API) berjalan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`; pembacaan dialog, Badge `Status`, dan tiga surface log (jumlah dan isi entri); pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain status Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-223: Sebagian reader berubah status sebelum konfirmasi, dilewati dan sisanya diproses

1. [Sesi A] Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
2. [Sesi A] Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
3. [Sesi A] Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
4. [Sesi A] Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
5. [Sesi A] Buka Global Settings > Hardware > Handheld Reader
6. [Sesi A] Centang checkbox baris DD-01
7. [Sesi A] Centang checkbox baris DD-07
8. [Sesi A] Klik tombol `Bulk Action`, pilih `Mark as Damaged`
9. [Sesi A] Verifikasi dialog `Mark as Damaged` tampil
10. [Sesi B] Mark as Damaged pada DD-07 lewat sesi API hingga tersimpan
11. [Sesi A] Klik `[Mark as Damaged]` pada dialog
12. [Sesi A] Verifikasi muncul toast sukses: "Success, reader has been marked as damaged. Some items were skipped."
13. [Sesi A] Verifikasi Badge `Status` baris DD-01 menjadi `Damaged`
14. [Sesi A] Verifikasi Badge `Status` baris DD-07 tetap `Damaged` hasil Sesi B
15. [Sesi A] Verifikasi Bulk Action Bar hilang
16. [Sesi A] Verifikasi seleksi di-reset (tidak ada checkbox tercentang)
17. [Sesi A] Buka ikon Changelog
18. [Sesi A] Verifikasi jumlah entri Changelog bertambah tepat 2 dibanding baseline langkah 2 (satu entri aksi Sesi B untuk DD-07 dan satu entri aksi Sesi A untuk DD-01)
19. [Sesi A] Verifikasi tepat satu dari entri baru ber-Modified By `Sari D`, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
20. [Sesi A] Tutup Modal Changelog dengan `✕`
21. [Sesi A] Buka Global Settings > User > Detail akun aktor > tab System Log
22. [Sesi A] Verifikasi jumlah entri System Log aktor bertambah tepat 1 dibanding baseline langkah 3
23. [Sesi A] Verifikasi entri baru adalah untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
24. [Sesi A] Buka Global Settings > Activity Log > tab User Action
25. [Sesi A] Verifikasi jumlah entri Activity Log bertambah tepat 2 dibanding baseline langkah 4
26. [Sesi A] Verifikasi tepat satu dari entri baru ber-Action `Mark as Damaged` dan ber-Modified By `Sari D`, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`

### TC-GS-HHR-224: Seluruh reader terpilih sudah berubah status, ditolak 409 dan seleksi dipertahankan

27. [Sesi A] Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
28. [Sesi A] Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
29. [Sesi A] Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
30. [Sesi A] Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
31. [Sesi A] Buka Global Settings > Hardware > Handheld Reader
32. [Sesi A] Centang checkbox baris DD-01
33. [Sesi A] Centang checkbox baris DD-07
34. [Sesi A] Klik tombol `Bulk Action`, pilih `Mark as Damaged`
35. [Sesi A] Verifikasi dialog `Mark as Damaged` tampil
36. [Sesi B] Mark as Damaged pada DD-01 dan DD-07 lewat sesi API hingga tersimpan
37. [Sesi A] Klik `[Mark as Damaged]` pada dialog
38. [Sesi A] Verifikasi dialog `Device Changed` tampil utuh: Body "This device was changed by someone else. Please review." dan tombol `[OK]`
39. [Sesi A] Klik `[OK]`
40. [Sesi A] Verifikasi dialog `Device Changed` tertutup
41. [Sesi A] Verifikasi daftar dimuat ulang: `Status` DD-01 dan DD-07 `Damaged` hasil Sesi B
42. [Sesi A] Verifikasi baris DD-01 dan DD-07 tetap tercentang
43. [Sesi A] Verifikasi Bulk Action Bar tetap tampil
44. [Sesi A] Buka ikon Changelog
45. [Sesi A] Verifikasi jumlah entri Changelog bertambah tepat 2 dibanding baseline langkah 28 (dua entri aksi Sesi B untuk DD-01 dan DD-07, tidak ada tambahan dari Sesi A)
46. [Sesi A] Tutup Modal Changelog dengan `✕`
47. [Sesi A] Buka Global Settings > User > Detail akun aktor > tab System Log
48. [Sesi A] Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 29
49. [Sesi A] Buka Global Settings > Activity Log > tab User Action
50. [Sesi A] Verifikasi jumlah entri Activity Log bertambah tepat 2 dibanding baseline langkah 30 (dua entri aksi Sesi B, tidak ada tambahan dari Sesi A)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k). Kelas harness: multi-konteks (dua pelaku pada entitas yang sama), prinsip 13c. Pelaku kedua hanya memicu perubahan state sehingga memakai sesi API (P-2): Sesi B tidak mempunyai asersi.
- Pengecualian P-2: Sesi B (API) memicu perubahan status reader yang ditonton Sesi A; hasil di Sesi B tidak diasersi, yang diasersi adalah perilaku Sesi A (dialog, toast, Badge, seleksi, log).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: 223, 224. Keduanya memakai DD-01 dan DD-07 yang berstatus Available pada precondition TC sehingga Seed Reader A dipulihkan sebelum tiap TC (langkah 1 dan 27).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 27 (pemulihan dan muat ulang), langkah 2 sampai 4 dan 28 sampai 30 (baseline jumlah entri sebelum aksi pemicu pertama; S-12), langkah 5 dan 31 (kembali ke halaman Handheld Reader), langkah 17, 21, 24, 44, 47, dan 49 (membuka surface log untuk dibaca), serta langkah 20 dan 46 (menutup Modal Changelog).
- Langkah 9 dan 35 (`Verifikasi` dialog tampil sebelum Sesi B bertindak) adalah asersi tambahan di luar Expected TC yang memastikan keadaan dialog terbuka sebelum Sesi B bertindak, mengikuti langkah "biarkan dialog terbuka" pada TC-GS-HHR-223 dan 224 (S-03).
- Asersi "tidak ada entri log dari Sesi A" TC-GS-HHR-223 d dan 224 b diasersi sebagai selisih jumlah entri terhadap baseline (bukan asersi absence kelas g): jumlah Changelog dan Activity Log bertambah tepat sebanyak aksi Sesi B dan Sesi A, jumlah System Log aktor Sesi A bertambah 1 pada TC-GS-HHR-223 dan sama dengan baseline pada TC-GS-HHR-224. Kenaikan jumlah entri Changelog dan Activity Log akibat aksi Sesi B menjadi anchor positif bahwa surface sudah termuat.
- Spec memuat 50 langkah (di atas sekitar 35 langkah). Alasan: seluruh blok satu kelas (konkurensi dua pelaku atas Bulk Mark as), tiap TC memakai pemulihan Seed Reader A sendiri sehingga kegagalan satu TC tidak menghilangkan makna TC lain, dan blok baca-log (langkah 2 sampai 4, 17 sampai 26, 28 sampai 30, 44 sampai 50) adalah blok baca-log berpola.
- Temuan untuk QA:
  - TC-GS-HHR-223 dan 224 tidak menyebut mekanisme Sesi B selain "lakukan Mark as Damaged"; spec memakai sesi API Admin B (P-2) dan menuliskan kemampuan itu sebagai disediakan tim FE/BE. Perlu konfirmasi QA bila Sesi B harus berupa sesi UI.
  - TC-GS-HHR-223 d dan 224 b tidak menyebut apakah Changelog dan Activity Log memuat entri aksi Sesi B (admin lain) pada surface yang sama; spec berasumsi Changelog entitas dan Activity Log entitas memuat entri semua pengguna Client A, sehingga kenaikan jumlah mencakup aksi Sesi B. Bila Activity Log dibatasi per pengguna, asersi jumlah pada langkah 25 dan 50 perlu disesuaikan.
  - TC-GS-HHR-223 d ("tepat satu entri untuk DD-01 dari sesi A") tidak menyebut identitas Sesi B; spec memakai Modified By `Sari D` untuk membedakan entri Sesi A.
  - TC-GS-HHR-224 Expected a menyebut dialog `Device Changed` dengan tombol `[OK]`; spec mengasersi judul, Body, dan tombol sebagai satu dialog utuh (S-01).
  - TC-GS-HHR-223 dan 224 tidak mencantumkan Post Condition.
  - Seed Reader A tidak diberi suffix per run (nama literal) dan mekanisme pemulihannya hanya disebut "fixture backend" di Catatan TC; pengecualian Population S-12 untuk HHR belum ada di konvensi.
