---
id: TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save
title: "Edit Reader Power Sukses: Nilai Baru, Batas 5 dan 30 dBm, Reader Damaged, Saving State, dan Klik Ganda Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-126
  - TC-GS-HHR-127
  - TC-GS-HHR-128
  - TC-GS-HHR-133
  - TC-GS-HHR-451
  - TC-GS-HHR-457
coverage:
  web: automated
---

# Edit Reader Power Sukses: Nilai Baru, Batas 5 dan 30 dBm, Reader Damaged, Saving State, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah Reader Power empat reader pada Seed Reader A dan menambah entri Changelog Client A, sehingga tidak berjalan bersamaan dengan spec lain pada Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Reader Long Range yang diedit, masing-masing milik satu blok TC: DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, `30 dBm`, TC-GS-HHR-126 dan 127), DD-03 (`Zebra Mobile Reader - 1`, Serial Number `SN-HHR-00103`, `25 dBm`, Damaged, TC-GS-HHR-128 dan 133), DD-09 (Serial Number `SN-HHR-00110`, `30 dBm`, TC-GS-HHR-451), dan DD-07 (`Honeywell CK65 - 1`, Serial Number `SN-HHR-00108`, `30 dBm`, TC-GS-HHR-457). Seed Reader A bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number.
- Baseline: jumlah entri total Changelog Handheld Reader dicatat sebelum aksi pemicu TC-GS-HHR-457 (langkah 37).
- Cleanup: Seed Reader A dipulihkan ke kondisi awal oleh fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme pemulihan disediakan tim FE/BE (lihat Temuan untuk QA). Entri Changelog yang bertambah tidak dihapus (audit trail permanen).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: input keyboard (`←`, `→`) dan penggeseran slider ke nilai tertentu; intercept jaringan untuk menahan respons request edit (hanya untuk mengamati saving state, dilepas segera sesudahnya); klik ganda cepat; membaca jumlah entri total Changelog Handheld Reader.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite), Reader Power Seed Reader A (dipulihkan), dan intercept penahanan respons (dilepas pada langkah 36).

## Test Steps

### TC-GS-HHR-126: Edit Reader Power berhasil menyimpan nilai baru

1. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
2. Geser slider ke 25 dBm
3. Verifikasi preview menampilkan `25 dBm` secara real-time
4. Klik `[Save]`
5. Verifikasi dialog tertutup
6. Verifikasi toast sukses "Success, Zebra RFID Reader - 1 has been updated."
7. Verifikasi kolom `Reader Power` baris DD-01 menampilkan `25 dBm`

### TC-GS-HHR-127: Reader Power batas bawah 5 dBm dapat disimpan

8. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
9. Geser slider ke nilai minimum
10. Verifikasi slider berhenti di `5 dBm`
11. Tekan `←` satu kali
12. Verifikasi slider tetap di `5 dBm` (tidak dapat digeser lebih rendah)
13. Klik `[Save]`
14. Verifikasi kolom `Reader Power` baris DD-01 menampilkan `5 dBm`

### TC-GS-HHR-128: Reader Power batas atas 30 dBm dapat disimpan

15. Klik `⋯` pada baris DD-03 (Serial Number `SN-HHR-00103`), pilih `Edit Reader Power`
16. Geser slider ke nilai maksimum
17. Verifikasi slider berhenti di `30 dBm`
18. Tekan `→` satu kali
19. Verifikasi slider tetap di `30 dBm` (tidak dapat digeser lebih tinggi)
20. Klik `[Save]`
21. Verifikasi kolom `Reader Power` baris DD-03 menampilkan `30 dBm`

### TC-GS-HHR-133: Edit Reader Power pada reader Damaged Long Range diperbolehkan

22. Klik `⋯` pada baris DD-03 (Serial Number `SN-HHR-00103`, Damaged), pilih `Edit Reader Power`
23. Geser slider ke 20 dBm
24. Klik `[Save]`
25. Verifikasi kolom `Reader Power` baris DD-03 menampilkan `20 dBm`
26. Verifikasi kolom `Status` baris DD-03 tetap `Damaged`

### TC-GS-HHR-451: Save masuk saving state selama request

27. Aktifkan penahanan respons pada request edit
28. Klik `⋯` pada baris DD-09 (Serial Number `SN-HHR-00110`), pilih `Edit Reader Power`
29. Geser slider ke 25 dBm
30. Klik `[Save]`
31. Verifikasi `[Save]` menampilkan spinner
32. Verifikasi `[Save]` disabled
33. Verifikasi `[Clear Field]` dinonaktifkan
34. Verifikasi `[✕]` dinonaktifkan
35. Verifikasi slider dinonaktifkan
36. Lepas penahanan respons dan tunggu dialog tertutup

### TC-GS-HHR-457: Klik ganda cepat pada Save hanya menyimpan satu perubahan

37. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog, tutup modal
38. Tunggu toast lama hilang otomatis
39. Klik `⋯` pada baris DD-07 (Serial Number `SN-HHR-00108`), pilih `Edit Reader Power`
40. Geser slider ke 25 dBm
41. Klik ganda cepat `[Save]`
42. Verifikasi hanya satu toast sukses "Success, Honeywell CK65 - 1 has been updated."
43. Buka ikon Changelog
44. Verifikasi jumlah entri total Changelog bertambah tepat satu dari baseline pada langkah 37
45. Verifikasi entri baru berjenis `Edit` pada `Reader Power` dengan nilai `30 dBm` ke `25 dBm` untuk reader DD-07 (Serial Number `SN-HHR-00108`)
46. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 126, 127, 128, 133, 451, 457. Urutan menyimpang dari urutan TC sumber: kasus yang mengubah nilai ke batas (127 dan 128) memakai baris yang sudah dipakai TC sebelumnya karena nilai awalnya tidak dipakai asersi; kasus penahanan respons (451) dan klik ganda (457) ditaruh terakhir karena memakai reader sendiri.
- Reader per blok dibedakan karena Seed Reader A hanya dipulihkan sekali sebelum spec, sedangkan tiap TC sumber mengandaikan data awal yang dipulihkan. Dibanding Data Uji TC: TC-GS-HHR-451 memakai DD-09 dan TC-GS-HHR-457 memakai DD-07 (TC menulis DD-01); keduanya Long Range 30 dBm seperti DD-01 sehingga objek uji tidak berubah. TC-GS-HHR-128 dan 133 berurutan pada DD-03: nilai awal TC-GS-HHR-133 menjadi `30 dBm` (TC menulis `25 dBm`) dan objek uji (reader Damaged boleh diedit) tidak berubah. Toast pada TC-GS-HHR-457 memakai Device Name DD-07 (`Honeywell CK65 - 1`) dan entri Changelog diasersi untuk DD-07.
- Asersi absence (tidak ada penurunan lebih rendah atau lebih tinggi) pada langkah 12 dan 19 memakai anchor pemicu `←` atau `→` (langkah 11 dan 18) dan `Verifikasi` batas yang mendahuluinya (langkah 10 dan 17).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 27 dan 36 (memasang dan melepas penahanan respons, S-09), langkah 37 (baseline Changelog), langkah 38 (menunggu toast lama hilang agar hitungan satu toast bermakna), dan langkah 46 (menutup modal).
- Jumlah pembukaan dialog Edit Reader Power: 6 (langkah 1, 8, 15, 22, 28, 39); jumlah penutupan: 6 (semua lewat Save atau penutupan otomatis sesudah Save).
- Spec melewati sekitar 35 langkah (46 langkah). Seluruhnya satu topik dan satu kelas (Edit Reader Power yang berhasil serta guard Save), satu akun, tanpa harness eksternal; penahanan respons pada langkah 27 hanya untuk mengamati saving state dan dilepas pada langkah 36. Tiap blok TC memakai reader atau nilai awal sendiri, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan dialog.
- Pembagian TC lintas spec: TC-GS-HHR-125 dan 129 sampai 132 ada di spec 032; TC-GS-HHR-134 sampai 136 dan 450 ada di spec 034; TC-GS-HHR-137 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-HHR-127 Expected a dan TC-GS-HHR-128 Expected a ("tidak dapat digeser lebih rendah/tinggi") tidak menyebut cara mencoba menggeser melewati batas; spec menekan `←` atau `→` satu kali sesudah slider berhenti di batas.
  - TC-GS-HHR-126 dan 127 memakai DD-01 secara berurutan dan TC-GS-HHR-128 dan 133 memakai DD-03 secara berurutan, sedangkan TC mengandaikan data awal terpulihkan di tiap TC (lihat Notes di atas).
  - TC-GS-HHR-457 Expected b menyebut "satu entri `Edit` `Reader Power` `30 dBm` ke `25 dBm` untuk DD-01" tanpa menyebut kolom Changelog yang membawa nilai lama dan baru; spec mengasersi entri baru berdasarkan jenis, field, dan nilai tanpa menyebut kolom.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.
