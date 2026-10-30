---
id: TC-GS-HHR-E2E-067-event-log-activate-pencatatan-hasil-aktivasi
title: "Event Log Activate: Pencatatan Baris Activated, Waiting for Approval, dan Failed (V-04 dan V-10)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-364
  - TC-GS-HHR-365
  - TC-GS-HHR-366
  - TC-GS-HHR-367
coverage:
  web: automated
---

# Event Log Activate: Pencatatan Baris Activated, Waiting for Approval, dan Failed (V-04 dan V-10)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec membuat reader dan baris Event Log di Client A dan Client B, mengonsumsi kuota dan stok Principal, dan memakai simulator USB bersama; tidak boleh paralel dengan spec lain yang memakai Client A, Client B, Seed Reader A, atau simulator USB.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar itu lagi hanya sesudah ganti akun.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (TC-GS-HHR-367, langkah 46): Total Control Client B, email `totalControl_automated_{namaClient}@qwertysystem.net` dengan nilai `{namaClient}` dari fixture `Fixture.hardwareHandheldReader` (nilai tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Client B: plan Growth, toggle `Allow Self-Purchased Device Activation` nonaktif, alokasi `Short Range` 3 dan `Long Range` 3, belum ada reader. Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup Client A: plan Growth, Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`; 10 reader DD-01 s.d. DD-10, `Short Range` `5 of 8`, `Long Range` `5 of 6`, pagination `Showing 1 - 10 of 10 readers`), format tanggal `dd/MM/yy` 24-hour. Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) berisi 5 baris dan dipulihkan lewat fixture backend di hook `before` dan `after`. Hardware Stock Principal (status `Available`):

  | ID | Serial Number | SKU | Range Type | Brand / Model | Device Name bawaan | Dipakai di |
  |---|---|---|---|---|---|---|
  | HS-01 | `SN-HHR-00201` | SKU-HHR-01 (Zebra RFID Reader) | Long Range | Zebra / RFD40 | `Zebra RFID Reader - 2` | TC-GS-HHR-364 |
  | HS-04 | `SN-HHR-00204` | SKU-HHR-01 (Zebra RFID Reader) | Long Range | Zebra / RFD40 | `Zebra RFID Reader - 4` | TC-GS-HHR-365 (aktif di Client C, collision) |

  Serial Jalur B: `SN-HHR-00302` (bebas; dibaca reader Client B pada TC-GS-HHR-367). Reader `SN-HHR-00101` aktif di Client A sebagai DD-01 (TC-GS-HHR-366, ditolak V-04).
- Data Dinamis: Alias Name `Alias Uji` (TC-GS-HHR-366, input uji yang submit-nya diblokir sehingga boleh literal; tidak disimpan).
- Baseline Event Log (S-12): jumlah baris Event Log Activate dicatat sebelum aksi pemicu tiap TC (Client B: nol bila empty state `No activation log yet`). Asersi memakai selisih terhadap baseline; angka 6 pada TC-GS-HHR-364 adalah baseline seed 5 ditambah 1.
- Pemulihan state di tengah spec: aktivasi TC-GS-HHR-364 menaikkan `Long Range` ke `6 of 6`, sehingga TC-GS-HHR-365 membutuhkan state awal. Langkah 31 memulihkan Seed Reader A, status unit HS-01, kuota `Long Range` `5 of 6`, dan Seed Event Log lewat reset fixture backend (Catatan TC: mutasi TC sebelumnya tidak dibawa ke TC berikutnya); mekanisme disediakan tim FE/BE.
- Kemampuan teknis: simulator reader USB dan driver lokal yang menyajikan reader tersambung dengan Serial Number tertentu (`SN-HHR-00201`, `SN-HHR-00204`, `SN-HHR-00101`, `SN-HHR-00302`) dan Current Power dari stok (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); TC-GS-HHR-364 sampai 367 berlabel Manual Only (b) di TC sumber. Reset fixture backend (di atas). Pembacaan baris, badge, dan jumlah Event Log Activate.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client B) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan Seed Reader A, stok HS-01 dan HS-04, Seed Event Log, kuota Client A dan Client B, dan simulator; tutup popup yang masih terbuka; kembalikan sesi ke akun default.

## Test Steps

### TC-GS-HHR-366: Penolakan V-04 menambah satu baris Failed dengan nama bawaan

1. Klik ikon Event Log
2. Catat jumlah baris Event Log sebagai baseline Event Log TC-GS-HHR-366
3. Tutup Popup Event Log Activate dengan `✕`
4. Catat teks pagination tabel utama sebagai baseline daftar reader TC-GS-HHR-366
5. Klik `[+ Activate Reader]`
6. Klik `Long Range` pada Overlay `Select Range Type`
7. Sambungkan reader dengan Serial Number `SN-HHR-00101` (sudah aktif di Client A) lewat simulator reader USB
8. Klik `[Sync]`
9. Isi `Alias Name` dengan `Alias Uji`
10. Klik `[Submit]`
11. Tutup Popup `Activate Handheld Reader` dengan `✕`
12. Klik ikon Event Log
13. Verifikasi jumlah baris Event Log bertambah tepat 1 dari baseline Event Log TC-GS-HHR-366
14. Verifikasi baris baru: Result `Failed`, Range Type `Long Range`, PIC `Sari D`
15. Verifikasi Device Name pada baris baru tidak memuat `Alias Uji`
16. Tutup Popup Event Log Activate dengan `✕`
17. Verifikasi teks pagination tabel utama sama dengan baseline daftar reader TC-GS-HHR-366 (tidak ada reader baru)

### TC-GS-HHR-364: Aktivasi berhasil menambah satu baris Activated

18. Klik ikon Event Log
19. Catat jumlah baris Event Log sebagai baseline Event Log TC-GS-HHR-364
20. Tutup Popup Event Log Activate dengan `✕`
21. Klik `[+ Activate Reader]`
22. Klik `Long Range` pada Overlay `Select Range Type`
23. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
24. Klik `[Sync]`
25. Klik `[Submit]`
26. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
27. Klik ikon Event Log
28. Verifikasi baris baru teratas: Range Type `Long Range`, Device Name `Zebra RFID Reader - 2 (SKU-HHR-01)`, Result `Activated`, PIC `Sari D`
29. Verifikasi jumlah baris Event Log bertambah tepat 1 dari baseline Event Log TC-GS-HHR-364 (menjadi 6)
30. Tutup Popup Event Log Activate dengan `✕`
31. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 `Available`, kuota `Long Range` `5 of 6`, Seed Event Log), lalu muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-365: Aktivasi collision menambah satu baris Waiting for Approval

32. Klik ikon Event Log
33. Catat jumlah baris Event Log sebagai baseline Event Log TC-GS-HHR-365
34. Tutup Popup Event Log Activate dengan `✕`
35. Klik `[+ Activate Reader]`
36. Klik `Long Range` pada Overlay `Select Range Type`
37. Sambungkan reader dengan Serial Number `SN-HHR-00204` (HS-04, aktif di Client C) lewat simulator reader USB
38. Klik `[Sync]`
39. Klik `[Submit]`
40. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
41. Klik ikon Event Log
42. Verifikasi jumlah baris Event Log bertambah tepat 1 dari baseline Event Log TC-GS-HHR-365
43. Verifikasi baris baru teratas: Device Name `Zebra RFID Reader - 4 (SKU-HHR-01)`, Result `Waiting for Approval`, PIC `Sari D`
44. Tutup Popup Event Log Activate dengan `✕`

### TC-GS-HHR-367: Penolakan V-10 menambah satu baris Failed per Sync yang ditolak (Client B)

45. Logout dari akun Total Control Client A
46. Login sebagai Total Control Client B (`Spectra.env.GS_CLIENTB_TC_PASSWORD`)
47. Buka Global Settings > Hardware > Handheld Reader
48. Klik ikon Event Log
49. Catat jumlah baris Event Log Client B sebagai baseline Event Log TC-GS-HHR-367
50. Tutup Popup Event Log Activate dengan `✕`
51. Klik `[+ Activate Reader]`
52. Klik `Long Range` pada Overlay `Select Range Type`
53. Sambungkan reader dengan Serial Number `SN-HHR-00302` (Jalur B) lewat simulator reader USB
54. Klik `[Sync]` (ditolak V-10)
55. Klik `[Sync]` sekali lagi (ditolak lagi)
56. Verifikasi `[Submit]` disabled
57. Tutup Popup `Activate Handheld Reader` dengan `✕`
58. Klik ikon Event Log
59. Verifikasi jumlah baris Event Log bertambah tepat 2 dari baseline Event Log TC-GS-HHR-367
60. Verifikasi dua baris baru Result `Failed` (satu per `[Sync]` yang ditolak), masing-masing Device Name `—` dan Range Type `Long Range`
61. Tutup Popup Event Log Activate dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 5b). Kelas harness: eksternal (d), simulator reader USB; keempat TC berlabel Manual Only (b). Satu topik (pencatatan hasil aktivasi di Event Log), satu harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-366 (penolakan, tidak mengubah kuota) dahulu, lalu TC-GS-HHR-364 dan 365 yang mengonsumsi kuota `Long Range` dengan pemulihan di antaranya (langkah 31), dan TC-GS-HHR-367 paling akhir karena ganti akun ke Client B (langkah 45 dan 46); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline (buka Event Log, catat jumlah, tutup); menyiapkan reader di simulator; "Tunggu aksi selesai" sebelum membuka Event Log (8b butir 8); menutup popup; pemulihan, muat ulang, Logout, Login, dan membuka layar Handheld Reader sesudah ganti akun. `Verifikasi` `[Submit]` disabled (TC-GS-HHR-367) menjalankan klausa Expected b "karena `[Submit]` disabled" sebagai alasan tidak ada baris `Failed` dari `[Submit]`; jumlah +2 membuktikan tidak ada baris tambahan.
- Spec memuat 61 langkah, di atas sekitar 35 langkah. Alasan: empat blok TC satu kelas harness (simulator USB) dan satu topik; tiap blok mencatat baseline Event Log sendiri; blok aktivasi sukses dimulai dari state hasil reset (langkah 31) dan Client B memakai kuota dan Event Log sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; 11 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01).
- Pembagian TC lintas spec: Submit gagal 5xx lalu berhasil dengan satu baris Failed dan satu Activated (TC-GS-HHR-368) di spec 026; kegagalan driver dan penolakan Suspended tanpa baris Event Log (TC-GS-HHR-369 dan 370) di spec absence 065; screening, Search, Filter, Sort, dan Download Popup Event Log (TC-GS-HHR-356 sampai 363) di spec 066; log tiga surface untuk aktivasi yang sama (TC-GS-HHR-343 dan 344) di spec 064.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (Serial Number dan Current Power yang dikembalikan driver) tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-364 sampai 367 tidak menyatakan pemulihan state antar TC di dalam satu spec; kuota `Long Range` `5 of 6` tidak cukup untuk dua aktivasi berturut-turut. Spec menulis pemulihan lewat reset fixture backend (langkah 31); mekanismenya tidak didefinisikan dan disediakan tim FE/BE.
  - TC-GS-HHR-364 Expected b ("Jumlah baris menjadi 6") memakai angka absolut dari Seed Event Log; spec memakai baseline dan menyatakan 6 sebagai seed 5 ditambah 1.
  - TC-GS-HHR-366 dan 367 menyebut "tutup popup" tanpa menyatakan ada atau tidaknya dialog konfirmasi saat popup Activate ditutup; spec menutup dengan `✕` saja dan tidak menulis langkah bersyarat. Judul TC-GS-HHR-367 menyebut "SKU strip" padahal Event Log tidak punya kolom SKU; spec hanya mengasersi Device Name `—`.
  - TC-GS-HHR-366 Expected b ("selalu nama bawaan") tidak menyebut nilai Device Name pada baris Failed; spec hanya mengasersi bahwa Device Name tidak memuat `Alias Uji`. TC-GS-HHR-367 tidak menyebut PIC baris Failed Client B dan tidak menyebut isi Event Log Client B sebelum uji; spec tidak mengasersi PIC dan memakai baseline jumlah.
  - TC-GS-HHR-365 tidak menyebut toast atau dampak kuota aktivasi collision; spec tidak mengasersinya. Email akun Total Control Client B dan nilai `{namaClient}` tidak tertulis di Pre-setup TC; spec memakai pola fixture dan nama env `GS_CLIENTB_TC_PASSWORD`.
