---
id: TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan
title: "Popup Handheld Reader Detail: Pembukaan, Screening, Nilai Kosong, Penutupan, Reader Waiting for Approval dan Jalur B, serta State Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-163
  - TC-GS-HHR-164
  - TC-GS-HHR-165
  - TC-GS-HHR-166
  - TC-GS-HHR-167
  - TC-GS-HHR-168
  - TC-GS-HHR-472
  - TC-GS-HHR-489
coverage:
  web: automated
---

# Popup Handheld Reader Detail: Pembukaan, Screening, Nilai Kosong, Penutupan, Reader Waiting for Approval dan Jalur B, serta State Tab

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec hanya membaca dan tidak mengubah data Seed Reader A.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Reader yang dibuka: DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`), DD-02 (`Gudang Reader - 1`, Short Range), DD-03 (`Zebra Mobile Reader - 1`, Damaged), DD-04 (`Gudang Reader - 2`, Missing, belum pernah dipindai), DD-05 (`Chainway C72 - 1`, Waiting for Approval, tanpa SKU), dan DD-08 (`Unitech EA520 - 1`, Jalur B, tanpa SKU dan Model/Type). Seed Changelog Client A dipakai TC-GS-HHR-472: baris seed DD-03 CL-06 (`18/06/26`), CL-07 (`17/06/26`), dan CL-08 (`16/06/26`), dikenali lewat `Date` (rentang `16/06/26` sampai `18/06/26`). Audit trail permanen: entri DD-03 lain bertanggal waktu aksi dapat ada di luar rentang itu, sehingga jumlah baris tab tidak diasersi sebagai angka absolut dan dibaca sebagai baseline N0 sebelum Search. Seed Reader A bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number.
- Cleanup: Seed Reader A tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme pemulihan disediakan tim FE/BE (lihat Temuan untuk QA). Audit trail (Changelog) tidak dipulihkan dan spec ini tidak menulis entri; asersi Changelog memakai baseline N0 dan baris seed bertanggal Juni 2026.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: input keyboard (`Esc`); klik pada area backdrop di luar popup; membaca nilai field info grid; pemilih rentang tanggal pada Filter Panel (nilai `Date` pada langkah ditulis dalam format tampil `dd/MM/yy`; input date picker memakai format `MM/dd/yyyy`, mis. `06/16/2026`, dan dipilih lewat date picker; perilaku date picker belum diverifikasi di UI).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-163 dan TC-GS-HHR-165: Pembukaan lewat Device Name dan screening Popup Detail

1. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
2. Verifikasi Popup `Handheld Reader Detail` terbuka untuk `Zebra RFID Reader - 1`
3. Verifikasi judul Header `Handheld Reader Detail` (flat, tanpa nama reader)
4. Verifikasi ikon `[✕]` tampil pada Header
5. Verifikasi tidak ada tombol teks `Close` pada Header
6. Verifikasi info grid label : value berisi field `Device Name`, `Alias Name`, `Serial Number`, `SKU`, `Range Type`, `Reader Power`, `Brand`, `Model/Type`, `Source`, `Last Scanned`, `Last Scanned In`, `Last User`, `Activated At`, `Status`
7. Catat nilai tiap field info grid sebagai pembanding TC-GS-HHR-164
8. Verifikasi tab `Usage` dan `Changelog` tampil
9. Verifikasi tab `Usage` aktif dan terbuka pertama
10. Verifikasi tidak ada footer aksi

### TC-GS-HHR-167: Popup Detail ditutup lewat X dan Esc, tidak lewat klik backdrop

11. Klik area backdrop
12. Verifikasi popup tetap terbuka
13. Klik `[✕]`
14. Verifikasi popup tertutup
15. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
16. Tekan `Esc`
17. Verifikasi popup tertutup

### TC-GS-HHR-164: Row action Detail membuka Popup Detail yang sama

18. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Detail`
19. Verifikasi Popup `Handheld Reader Detail` terbuka untuk `Zebra RFID Reader - 1`
20. Verifikasi nilai tiap field info grid sama dengan nilai yang dicatat pada langkah 7
21. Klik `[✕]`

### TC-GS-HHR-166: Info grid menampilkan strip untuk nilai kosong

22. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
23. Verifikasi `Last Scanned` menampilkan `—`
24. Verifikasi `Last Scanned In` menampilkan `—`
25. Verifikasi `Last User` menampilkan `—`
26. Klik `[✕]`
27. Klik `Device Name` baris DD-05 (`Chainway C72 - 1`)
28. Verifikasi `SKU` menampilkan `—`

### TC-GS-HHR-168: Popup Detail reader Waiting for Approval

29. Verifikasi Popup `Handheld Reader Detail` terbuka untuk `Chainway C72 - 1`
30. Verifikasi `Status` menampilkan `Waiting for Approval`
31. Verifikasi `Source` menampilkan `Self-Purchased`
32. Verifikasi tidak ada kontrol tulis pada popup
33. Klik `[✕]`

### TC-GS-HHR-166 (lanjutan): reader Short Range

34. Klik `Device Name` baris DD-02 (`Gudang Reader - 1`)
35. Verifikasi `Reader Power` menampilkan `—`
36. Klik `[✕]`

### TC-GS-HHR-489: Popup Detail reader Jalur B tanpa SKU dan tanpa Model/Type

37. Klik `Device Name` baris DD-08 (`Unitech EA520 - 1`)
38. Verifikasi Popup `Handheld Reader Detail` terbuka
39. Verifikasi `SKU` menampilkan `—`
40. Verifikasi `Model/Type` menampilkan `—`
41. Verifikasi `Brand` menampilkan `Unitech`
42. Verifikasi `Source` menampilkan `Self-Purchased`
43. Klik `[✕]`

### TC-GS-HHR-472: Popup Detail selalu terbuka di tab Usage dan state tab tidak dipertahankan

44. Klik `Device Name` baris DD-03 (`Zebra Mobile Reader - 1`)
45. Klik tab `Changelog`
46. Catat jumlah baris tab `Changelog` sebagai baseline N0
47. Klik ikon Filter di tab, isi `Date` rentang `16/06/26` sampai `17/06/26`, klik `[Apply]`
48. Ketik Search `Damaged`, tekan Enter
49. Verifikasi tabel Changelog menampilkan 2 baris seed Status `Damaged`: CL-07 (`17/06/26`) dan CL-08 (`16/06/26`), dibaca pada tab yang dibatasi Filter `Date` seed (langkah 47) sehingga kedua baris seed berada pada satu halaman hasil (baris non-seed tidak diasersi jumlahnya)
50. Verifikasi setiap baris yang tampil memuat `Damaged`
51. Klik tab `Usage`
52. Klik tab `Changelog`
53. Verifikasi kotak Search kosong
54. Verifikasi jumlah baris tab `Changelog` sama dengan N0 (langkah 46)
55. Klik `[✕]`
56. Klik `Device Name` baris DD-03 (`Zebra Mobile Reader - 1`)
57. Verifikasi popup terbuka pada tab `Usage`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 163 dan 165, 167, 164, 166 dan 168, 489, 472. Urutan menyimpang dari urutan TC sumber: screening di awal; TC-GS-HHR-166 (langkah 27 dan 28, DD-05) dan TC-GS-HHR-168 (langkah 29 sampai 33) memakai satu pembukaan Popup Detail DD-05 karena Data Uji dan popup-nya sama (TC-GS-HHR-166 langkah 3 membuka DD-05; TC-GS-HHR-168 membuka DD-05 lewat `Device Name`). `Verifikasi` `SKU` `—` pada langkah 28 sekaligus memenuhi Expected b TC-GS-HHR-168 (`SKU` `—`); TC-GS-HHR-166 untuk DD-02 dilanjutkan pada langkah 34 sampai 36 sesudah TC-GS-HHR-168.
- Langkah 7 mencatat nilai grid sebagai pembanding "identik" pada TC-GS-HHR-164 (langkah 20); TC-GS-HHR-164 tidak merinci field yang dibandingkan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (mencatat nilai), langkah 13, 21, 26, 33, 36, 43, 55 (menutup popup), langkah 15 dan 16 (membuka kembali popup lalu menutupnya dengan `Esc`, langkah TC-GS-HHR-167), dan langkah 45 sampai 48 dan 51 sampai 52 (berpindah tab, mencatat baseline N0, mengisi Filter `Date` seed sebagai pembatas baca, dan mencari, langkah TC-GS-HHR-472). Keterangan "termasuk 3 baris seed CL-06, CL-07, CL-08" pada Expected b TC-GS-HHR-472 menjelaskan isi N0 dan tidak diasersi terpisah.
- Spec melewati sekitar 35 langkah (57 langkah). Seluruhnya satu topik dan satu kelas (Popup Detail, hanya baca, satu akun, tanpa harness eksternal). Tiap blok membuka popup reader sendiri dan menutupnya, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan popup.
- Pembagian TC lintas spec: TC-GS-HHR-169 sampai 178 dan 183 ada di spec 036; TC-GS-HHR-179 sampai 182 ada di spec 037; isi tab Changelog Popup Detail ada di spec 062.
- Temuan untuk QA:
  - TC-GS-HHR-163 dan 164 menyebut "terbuka untuk `Zebra RFID Reader - 1`" padahal DD-01 dan DD-06 sama-sama bernama itu; spec membuka DD-01 lewat Serial Number `SN-HHR-00101` dan mengasersi `Device Name` pada popup.
  - TC-GS-HHR-164 Expected a ("identik dengan yang dibuka dari klik Device Name") tidak merinci bagian yang dibandingkan; spec membandingkan nilai tiap field info grid.
  - TC-GS-HHR-472 Expected c ("state tab tidak dipertahankan") mencakup Search kosong sesudah berpindah tab; spec mengasersi kotak Search kosong pada tab `Changelog` (langkah 53).
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-HHR-472 langkah 2 hanya menyebut Search `Damaged` pada Changelog DD-03 yang tumbuh (audit trail permanen). Spec memasang Filter `Date` `16/06/26` sampai `17/06/26` (langkah 47) sebagai pembatas baca baris seed CL-07 dan CL-08 sebelum Search (S-14), sehingga tanpa langkah pindah halaman. Filter itu tidak disebut di TC; spec menganggap state tab (Search dan Filter) tidak dipertahankan sesudah berpindah tab, sehingga jumlah baris pada langkah 54 dibandingkan dengan N0 tanpa pembatas.
  - Tidak ada Post Condition pada TC sumber spec ini.
