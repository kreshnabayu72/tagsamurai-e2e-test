---
id: TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard
title: "Edit Reader Power: Screening Dialog, Step Slider 1 dBm, Save Tanpa Perubahan, Row Action Short Range, dan Clear Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-125
  - TC-GS-HHR-129
  - TC-GS-HHR-130
  - TC-GS-HHR-131
  - TC-GS-HHR-132
coverage:
  web: automated
---

# Edit Reader Power: Screening Dialog, Step Slider 1 dBm, Save Tanpa Perubahan, Row Action Short Range, dan Clear Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec dijalankan pada Client A yang datanya dipakai spec lain; spec tidak mengubah Reader Power tersimpan (Save pada langkah 17 dan 20 adalah no-op).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); langkah 4 membuka layar lagi hanya sebagai kembali dari surface log.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, Long Range, `30 dBm`), DD-03 (`Zebra Mobile Reader - 1`, Serial Number `SN-HHR-00103`, Long Range, `25 dBm`, Damaged), DD-02 (`Gudang Reader - 1`, Short Range, Available), dan DD-04 (`Gudang Reader - 2`, Short Range, Missing). Seed Reader A bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number.
- Baseline: jumlah entri total Changelog Handheld Reader, System Log aktor (Sari Dewi), dan Activity Log Global Settings dicatat sebelum aksi pemicu pertama yang diasersi (langkah 1 sampai 3).
- Cleanup: Seed Reader A tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme pemulihan disediakan tim FE/BE (lihat Temuan untuk QA).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: input keyboard (`←`, `→`, `Esc`) untuk slider; membaca jumlah entri total pada Changelog Handheld Reader, System Log aktor, dan Activity Log.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Baseline log (TC-GS-HHR-130)

1. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog, tutup modal
2. Buka System Log aktor Sari Dewi, catat jumlah entri total sebagai baseline System Log
3. Buka Activity Log Global Settings, catat jumlah entri total sebagai baseline Activity Log
4. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-125: Screening Dialog Edit Reader Power

5. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
6. Verifikasi judul Header dialog `Edit Reader Power`
7. Verifikasi ikon `[✕]` tampil pada Header
8. Verifikasi slider `Reader Power` terisi `30 dBm`
9. Verifikasi preview nilai bersatuan `30 dBm` tampil di samping slider
10. Verifikasi Footer berisi `[Clear Field]` dan `[Save]`
11. Klik `[✕]`

### TC-GS-HHR-129: Slider bergerak dengan step 1 dBm

12. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
13. Fokuskan slider, tekan `←` satu kali
14. Verifikasi preview `29 dBm`
15. Tekan `→` satu kali
16. Verifikasi preview `30 dBm`
17. Klik `[Save]`

### TC-GS-HHR-130: Save tanpa perubahan

18. Tunggu toast lama hilang otomatis
19. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
20. Klik `[Save]` tanpa menggeser slider
21. Verifikasi dialog tertutup
22. Verifikasi toast netral `No changes to save.`
23. Buka ikon Changelog
24. Verifikasi jumlah entri total Changelog sama dengan baseline Changelog
25. Tutup modal Changelog, buka System Log aktor Sari Dewi
26. Verifikasi jumlah entri total System Log sama dengan baseline System Log
27. Buka Activity Log Global Settings
28. Verifikasi jumlah entri total Activity Log sama dengan baseline Activity Log
29. Buka Global Settings > Hardware > Handheld Reader
30. Verifikasi kolom `Reader Power` baris DD-01 tetap `30 dBm`

### TC-GS-HHR-132: Row action Edit Reader Power tidak ada untuk Short Range

31. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`, Short Range, Available)
32. Verifikasi Overlay row action berisi `Detail`, `Edit Alias Name`, `Mark as Damaged`, `Mark as Missing`, `Delete`
33. Verifikasi Overlay row action tidak berisi `Edit Reader Power`
34. Tutup Overlay row action
35. Klik `⋯` pada baris DD-04 (`Gudang Reader - 2`, Short Range, Missing)
36. Verifikasi Overlay row action berisi `Detail`, `Edit Alias Name`, `Mark as Available`, `Delete`
37. Verifikasi Overlay row action tidak berisi `Edit Reader Power`
38. Tutup Overlay row action

### TC-GS-HHR-131: Clear Field mengembalikan slider ke default 30 dBm tanpa mengubah nilai tersimpan

39. Klik `⋯` pada baris DD-03 (Serial Number `SN-HHR-00103`), pilih `Edit Reader Power`
40. Klik `[Clear Field]`
41. Verifikasi slider kembali ke `30 dBm`
42. Verifikasi dialog tetap terbuka
43. Verifikasi tidak ada dialog konfirmasi
44. Klik `[✕]`
45. Verifikasi dialog `Unsaved Changes` muncul
46. Klik `[Leave]`
47. Verifikasi kolom `Reader Power` baris DD-03 tetap `25 dBm`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 125, 129, 130, 132, 131. Urutan menyimpang dari urutan TC sumber: screening (125) pertama; TC-GS-HHR-131 ditaruh terakhir karena menutup form dirty (prinsip 6). Tiap TC Edit Reader Power membuka form baru.
- Asersi jumlah entri (langkah 24, 26, 28) memakai baseline jumlah entri (S-12), bukan asersi absence kelas g: TC-GS-HHR-130 memuat aksi Save nyata dan langkah catat-bandingkan di TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (baseline), langkah 11 (menutup form yang belum diubah), langkah 17 (`[Save]` pada slider yang sudah kembali ke nilai tersimpan menutup form tanpa dialog `Unsaved Changes` dan tanpa perubahan data; toastnya tidak diasersi), langkah 18 (menunggu toast lama hilang agar toast TC-GS-HHR-130 dapat diasersi sendiri), langkah 25, 29 (pindah surface log dan kembali), dan langkah 34 dan 38 (menutup overlay).
- Jumlah pembukaan dialog Edit Reader Power: 4 (langkah 5, 12, 19, 39); jumlah kejadian menutup: 4 (langkah 11, langkah 17, langkah 20, langkah 44 sampai 46).
- Spec melewati sekitar 35 langkah (47 langkah, di antaranya sekitar 12 langkah blok baca-log berpola yang tidak dihitung). Seluruhnya satu topik dan satu kelas (dialog Edit Reader Power dan row action-nya, satu akun, data Seed Reader A yang sama, tanpa harness eksternal). Tiap blok membuka form baru dan memulai dari nilai tersimpan, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan dialog.
- Pembagian TC lintas spec: TC-GS-HHR-126 sampai 128, 133, 451, dan 457 ada di spec 033; TC-GS-HHR-134 sampai 136 dan 450 ada di spec 034; TC-GS-HHR-137 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-HHR-129 tidak menyebut cara menutup dialog sesudah slider kembali ke 30 dBm; spec menutupnya lewat `[Save]` yang no-op supaya tidak bergantung pada apakah slider yang dikembalikan dianggap dirty (S-08). Perlakuan dirty untuk slider yang dikembalikan tidak disebut TC maupun PRD yang dibaca penulis.
  - TC-GS-HHR-130 menyebut System Log aktor dan Activity Log tanpa menyebut jalur navigasi surface atau cara membaca jumlah entri; spec membaca jumlah entri total tiap surface dan jalur navigasinya mengikuti TC section 5.
  - TC-GS-HHR-131 Expected a menyebut "default 30 dBm" sedangkan nilai tersimpan DD-03 adalah 25 dBm; spec mengikuti TC (slider 30 dBm sesudah `[Clear Field]`, nilai tersimpan tetap 25 dBm).
  - TC-GS-HHR-131 langkah 4 memakai kata "bila dialog Unsaved Changes muncul" (bersyarat); spec menulis jalur deterministik `[✕]`, `Verifikasi` dialog, `[Leave]` (S-08) karena slider berubah dari 25 dBm ke 30 dBm sehingga form dirty.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.
