---
id: TC-GS-HHR-E2E-064-pencatatan-log-aktivasi-jalur-a-dan-collision
title: "Pencatatan Log Aktivasi Jalur A pada Tiga Surface: Status Available dan Collision Waiting for Approval"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-343
  - TC-GS-HHR-344
coverage:
  web: automated
---

# Pencatatan Log Aktivasi Jalur A pada Tiga Surface: Status Available dan Collision Waiting for Approval

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec membuat reader di Client A, mengonsumsi kuota dan stok Principal, memakai simulator USB bersama, dan menambah entri log; tidak boleh paralel dengan spec lain yang memakai Client A, Seed Reader A, atau simulator USB.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar itu lagi hanya sebagai kembali dari surface log.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client A plan Growth, Seed Reader A (fixture baru `Fixture.hardwareHandheldReader.seedReaderA`; 10 reader DD-01 s.d. DD-10, `Short Range` `5 of 8`, `Long Range` `5 of 6`), format tanggal `dd/MM/yy` 24-hour. Hardware Stock Principal (status `Available`):

  | ID | Serial Number | SKU | Range Type | Brand / Model | Device Name bawaan | Dipakai di |
  |---|---|---|---|---|---|---|
  | HS-01 | `SN-HHR-00201` | SKU-HHR-01 (Zebra RFID Reader) | Long Range | Zebra / RFD40 | `Zebra RFID Reader - 2` | TC-GS-HHR-343 |
  | HS-04 | `SN-HHR-00204` | SKU-HHR-01 (Zebra RFID Reader) | Long Range | Zebra / RFD40 | `Zebra RFID Reader - 4` | TC-GS-HHR-344 (aktif di Client C, collision) |

- Pemulihan state di tengah spec: aktivasi TC-GS-HHR-343 menaikkan `Long Range` ke `6 of 6`, sehingga TC-GS-HHR-344 membutuhkan state awal. Langkah 23 memulihkan Seed Reader A, status unit HS-01, dan kuota `Long Range` `5 of 6` lewat reset fixture backend (Catatan TC: mutasi TC sebelumnya tidak dibawa ke TC berikutnya); mekanisme disediakan tim FE/BE. Reset hanya memulihkan data dan state reader; audit trail (Changelog, System Log, Activity Log) permanen dan tidak dipulihkan, sehingga tiap TC membaca log relatif terhadap baseline yang dicatat sebelum aksi pemicunya (S-12). Hook `before` dan `after` juga memulihkannya.
- Baseline log: jumlah entri total Changelog Handheld Reader, System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action) dicatat tiap TC sebelum aksi pemicu (S-12). Total entri tidak diasersi sebagai angka absolut. Kolom Date hanya diasersi formatnya; jam server dan jam browser disinkron.
- Kemampuan teknis: simulator reader USB dan driver lokal yang menyajikan reader tersambung dengan Serial Number tertentu (`SN-HHR-00201`, `SN-HHR-00204`) dan Current Power dari stok (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); TC-GS-HHR-343 dan 344 berlabel Manual Only (b) di TC sumber. Reset fixture backend (di atas). Pembacaan jumlah dan isi entri pada tiga surface log.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan Seed Reader A, stok HS-01 dan HS-04, kuota Client A, dan simulator; tutup popup yang masih terbuka.

## Test Steps

### TC-GS-HHR-343: Log aktivasi Jalur A berstatus Available

1. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
2. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
3. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
4. Buka Global Settings > Hardware > Handheld Reader
5. Klik `[+ Activate Reader]`
6. Klik `Long Range` pada Overlay `Select Range Type`
7. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
8. Klik `[Sync]`
9. Klik `[Submit]`
10. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
11. Buka ikon Changelog Handheld Reader
12. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
13. Verifikasi entri terbaru Changelog: Action `Activate`, Device Name `Zebra RFID Reader - 2 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Available`, Modified By `Sari D`
14. Tutup Modal Changelog dengan `✕`
15. Buka Global Settings > User > Detail akun aktor > tab System Log
16. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
17. Verifikasi entri terbaru System Log aktor: Action `Activate`, Object `Handheld Reader`, Name `Zebra RFID Reader - 2 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Available`
18. Buka Global Settings > Activity Log > tab User Action
19. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
20. Verifikasi entri terbaru Activity Log: Action `Activate Reader`, Object `Handheld Reader`, Name `Zebra RFID Reader - 2 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Available`, Modified By `Sari D`
21. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
22. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
23. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 `Available`, kuota `Long Range` `5 of 6`), lalu muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-344: Log aktivasi collision berstatus Waiting for Approval

24. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
25. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
26. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
27. Buka Global Settings > Hardware > Handheld Reader
28. Klik `[+ Activate Reader]`
29. Klik `Long Range` pada Overlay `Select Range Type`
30. Sambungkan reader dengan Serial Number `SN-HHR-00204` (HS-04, aktif di Client C) lewat simulator reader USB
31. Klik `[Sync]`
32. Klik `[Submit]`
33. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
34. Buka ikon Changelog Handheld Reader
35. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
36. Verifikasi entri terbaru Changelog: Action `Activate`, Device Name `Zebra RFID Reader - 4 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Sari D`
37. Tutup Modal Changelog dengan `✕`
38. Buka Global Settings > User > Detail akun aktor > tab System Log
39. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
40. Verifikasi entri terbaru System Log aktor: Action `Activate`, Object `Handheld Reader`, Name `Zebra RFID Reader - 4 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`
41. Buka Global Settings > Activity Log > tab User Action
42. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
43. Verifikasi entri terbaru Activity Log: Action `Activate Reader`, Object `Handheld Reader`, Name `Zebra RFID Reader - 4 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Sari D`
44. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
45. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 5a). Kelas harness: eksternal (d), simulator reader USB; kedua TC berlabel Manual Only (b). Satu topik (pencatatan log aktivasi Jalur A), satu akun, satu harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok mengikuti nomor TC. Langkah 23 memulihkan state awal di antara kedua TC karena kuota `Long Range` `5 of 6` hanya cukup untuk satu aktivasi sukses.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline dan kembali ke layar Handheld Reader; menyiapkan reader di simulator; "Tunggu aksi selesai" sebelum berpindah surface (8b butir 8); membuka dan menutup surface log; pemulihan dan muat ulang.
- Spec memuat 45 langkah, di atas sekitar 35 langkah. Alasan: dua blok TC satu kelas harness (simulator USB) dengan pola baca-log berpola (buka surface, `Verifikasi` jumlah dan isi entri) yang tidak dihitung ke batas ukuran; blok kedua dimulai dari state hasil reset (langkah 23) sehingga kegagalan blok pertama tidak menghilangkan makna blok kedua; 16 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01).
- Pembagian TC lintas spec: Event Log Activate untuk aktivasi yang sama (TC-GS-HHR-364 dan 365) di spec 067; log Edit, Mark as, Cancel Request, dan Delete (TC-GS-HHR-345 sampai 351 dan 353) di spec 063; pencatatan Approve atau Reject collision oleh Principal (TC-GS-HHR-371, 372, 385 sampai 389) di spec 069.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (Serial Number dan Current Power yang dikembalikan driver) tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-343 dan 344 tidak menyatakan pemulihan state antar TC di dalam satu spec; kuota `Long Range` `5 of 6` tidak cukup untuk dua aktivasi berturut-turut. Spec menulis pemulihan lewat reset fixture backend (langkah 23); mekanismenya tidak didefinisikan dan disediakan tim FE/BE.
  - TC-GS-HHR-343 dan 344 tidak menyebut toast hasil aktivasi; spec tidak mengasersinya dan memakai langkah "Tunggu aksi selesai (Popup tertutup)" sebelum berpindah surface.
  - TC-GS-HHR-344 tidak menyatakan apakah aktivasi collision memakai slot kuota `Long Range`; spec tidak mengasersi kartu kuota.
  - TC-GS-HHR-343 Expected d menyebut "kolom Date mengikuti format General Settings" tanpa nilai tanggal; spec mengasersi format `dd/MM/yy` 24-hour, bukan nilai.
