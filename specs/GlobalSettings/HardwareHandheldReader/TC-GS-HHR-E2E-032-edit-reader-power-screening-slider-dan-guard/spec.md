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
- Suite serial (`parallel: false`): spec dijalankan pada Client A yang datanya dipakai spec lain; spec tidak mengubah Reader Power tersimpan (Save pada langkah 22 adalah no-op).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); langkah 4 membuka layar lagi hanya sebagai kembali dari surface log.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, Long Range, `30 dBm`), DD-03 (`Zebra Mobile Reader - 1`, Serial Number `SN-HHR-00103`, Long Range, `25 dBm`, Damaged), DD-02 (`Gudang Reader - 1`, Short Range, Available), dan DD-04 (`Gudang Reader - 2`, Short Range, Missing). Seed Reader A bernama literal tanpa suffix (pengecualian S-12 Population Seed Reader A HHR) karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number.
- Baseline: jumlah entri total Changelog Handheld Reader, System Log aktor (Sari Dewi), dan Activity Log Global Settings (tab `User Action`; tab `Session` tidak dibaca) dicatat sebelum aksi pemicu pertama yang diasersi (langkah 1 sampai 3).
- Cleanup: Seed Reader A tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: input keyboard (`←`, `→`, `Esc`) untuk slider; membaca jumlah entri total pada Changelog Handheld Reader, System Log aktor, dan Activity Log tab `User Action`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Baseline log (TC-GS-HHR-130)

1. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog, tutup modal
2. Buka System Log aktor Sari Dewi, catat jumlah entri total sebagai baseline System Log
3. Buka Global Settings > Activity Log > tab `User Action`, catat jumlah entri total tab `User Action` sebagai baseline Activity Log
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
17. Klik `[✕]` pada header dialog
18. Verifikasi dialog Edit Reader Power tertutup langsung
19. Verifikasi dialog `Unsaved Changes` tidak muncul (slider kembali identik dengan nilai tersimpan `30 dBm`, form clean)
20. Verifikasi kolom `Reader Power` baris DD-01 tetap `30 dBm`

### TC-GS-HHR-130: Save tanpa perubahan

21. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
22. Klik `[Save]` tanpa menggeser slider
23. Verifikasi dialog tertutup
24. Verifikasi toast netral `No changes to save.`
25. Buka ikon Changelog
26. Verifikasi jumlah entri total Changelog sama dengan baseline Changelog
27. Tutup modal Changelog, buka System Log aktor Sari Dewi
28. Verifikasi jumlah entri total System Log sama dengan baseline System Log
29. Buka Global Settings > Activity Log > tab `User Action`
30. Verifikasi jumlah entri total tab `User Action` sama dengan baseline Activity Log
31. Buka Global Settings > Hardware > Handheld Reader
32. Verifikasi kolom `Reader Power` baris DD-01 tetap `30 dBm`

### TC-GS-HHR-132: Row action Edit Reader Power tidak ada untuk Short Range

33. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`, Short Range, Available)
34. Verifikasi Overlay row action berisi `Detail`, `Edit Alias Name`, `Mark as Damaged`, `Mark as Missing`, `Delete`
35. Verifikasi Overlay row action tidak berisi `Edit Reader Power`
36. Tutup Overlay row action
37. Klik `⋯` pada baris DD-04 (`Gudang Reader - 2`, Short Range, Missing)
38. Verifikasi Overlay row action berisi `Detail`, `Edit Alias Name`, `Mark as Available`, `Delete`
39. Verifikasi Overlay row action tidak berisi `Edit Reader Power`
40. Tutup Overlay row action

### TC-GS-HHR-131: Clear Field mengembalikan slider ke default 30 dBm tanpa mengubah nilai tersimpan

41. Klik `⋯` pada baris DD-03 (Serial Number `SN-HHR-00103`), pilih `Edit Reader Power`
42. Klik `[Clear Field]`
43. Verifikasi slider kembali ke `30 dBm`
44. Verifikasi dialog tetap terbuka
45. Verifikasi tidak ada dialog konfirmasi
46. Klik `[✕]`
47. Verifikasi dialog `Unsaved Changes` muncul dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]` (slider `30 dBm` berbeda dari nilai tersimpan `25 dBm`)
48. Klik `[Leave]`
49. Verifikasi dialog Edit Reader Power tertutup
50. Verifikasi kolom `Reader Power` baris DD-03 tetap `25 dBm`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 125, 129, 130, 132, 131. Urutan menyimpang dari urutan TC sumber: screening (125) pertama; TC-GS-HHR-131 ditaruh terakhir karena menutup form dirty (prinsip 6). Tiap TC Edit Reader Power membuka form baru.
- Asersi jumlah entri (langkah 26, 28, 30) memakai baseline jumlah entri (S-12), bukan asersi absence kelas g: TC-GS-HHR-130 memuat aksi Save nyata dan langkah catat-bandingkan di TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (baseline), langkah 11 (menutup form yang belum diubah), langkah 27, 31 (pindah surface log dan kembali), dan langkah 36 dan 40 (menutup overlay).
- Jumlah pembukaan dialog Edit Reader Power: 4 (langkah 5, 12, 21, 41); jumlah kejadian menutup: 4 (langkah 11, langkah 17, langkah 22, langkah 46 sampai 48).
- Spec melewati sekitar 35 langkah (50 langkah, di antaranya sekitar 12 langkah blok baca-log berpola yang tidak dihitung). Seluruhnya satu topik dan satu kelas (dialog Edit Reader Power dan row action-nya, satu akun, data Seed Reader A yang sama, tanpa harness eksternal). Tiap blok membuka form baru dan memulai dari nilai tersimpan, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan dialog.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Spec 032, 033, dan 034 menguji dialog Edit Reader Power pada dataset Seed Reader A yang sama dan sengaja dipisah: gabungannya 118 langkah (50, 46, dan 22), jauh di atas sekitar 35 langkah, dan tiap spec membuka dialog sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Pembagian TC lintas spec: TC-GS-HHR-126 sampai 128, 133, 451, dan 457 ada di spec 033; TC-GS-HHR-134 sampai 136 dan 450 ada di spec 034; TC-GS-HHR-137 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-HHR-130 menyebut System Log aktor dan Activity Log (tab `User Action`) tanpa menyebut jalur navigasi surface atau cara membaca jumlah entri; spec membaca jumlah entri total tiap surface dan jalur navigasinya mengikuti TC section 5.
  - TC-GS-HHR-131 Expected a menyebut "default 30 dBm" sedangkan nilai tersimpan DD-03 adalah 25 dBm; spec mengikuti TC (slider 30 dBm sesudah `[Clear Field]`, nilai tersimpan tetap 25 dBm).
  - Tidak ada Post Condition pada TC sumber spec ini.
