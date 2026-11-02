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
- Akun kedua (TC-GS-HHR-367, langkah 48): Total Control Client B, `totalControl_automated_qaTeam2@qwertysystem.net`, password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Client B: plan Growth, toggle `Allow Self-Purchased Device Activation` nonaktif, alokasi `Short Range` 3 dan `Long Range` 3, belum ada reader. Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup Client A: plan Growth, Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru; 10 reader DD-01 s.d. DD-10, `Short Range` `5 of 8`, `Long Range` `5 of 6`, pagination `Showing 1 - 10 of 10 readers`), format tanggal `dd/MM/yy` 24-hour. Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) dibuat fixture backend dengan `Date` Juni 2026 dan tidak dipulihkan (audit trail permanen). Hardware Stock Principal (status `Available`):

  | ID | Serial Number | SKU | Range Type | Brand / Model | Device Name bawaan | Dipakai di |
  |---|---|---|---|---|---|---|
  | HS-01 | `SN-HHR-00201` | SKU-HHR-01 (Zebra RFID Reader) | Long Range | Zebra / RFD40 | `Zebra RFID Reader - 2` | TC-GS-HHR-364 |
  | HS-04 | `SN-HHR-00204` | SKU-HHR-01 (Zebra RFID Reader) | Long Range | Zebra / RFD40 | `Zebra RFID Reader - 4` | TC-GS-HHR-365 (aktif di Client C, collision) |

  Serial Jalur B: `SN-HHR-00302` (bebas; dibaca reader Client B pada TC-GS-HHR-367). Reader `SN-HHR-00101` aktif di Client A sebagai DD-01 (TC-GS-HHR-366, ditolak V-04).
- Data Dinamis: Alias Name `Alias Uji` (TC-GS-HHR-366, input uji yang submit-nya diblokir sehingga boleh literal; tidak disimpan).
- Baseline Event Log (S-12): jumlah baris Event Log Activate dicatat sebelum aksi pemicu tiap TC (Client B: nol bila empty state `No activation log yet`). Asersi memakai selisih terhadap baseline; jumlah total Event Log tidak diasersi sebagai angka absolut.
- Pemulihan state di tengah spec: aktivasi TC-GS-HHR-364 menaikkan `Long Range` ke `6 of 6`, sehingga TC-GS-HHR-365 membutuhkan state awal. Langkah 33 memulihkan Seed Reader A, status unit HS-01, dan kuota `Long Range` `5 of 6` lewat reset fixture backend (Catatan TC: mutasi TC sebelumnya tidak dibawa ke TC berikutnya); mekanisme disediakan tim FE/BE.
- Kemampuan teknis: simulator reader USB dan driver lokal yang menyajikan reader tersambung dengan Serial Number tertentu (`SN-HHR-00201`, `SN-HHR-00204`, `SN-HHR-00101`, `SN-HHR-00302`) dan Current Power dari stok (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); TC-GS-HHR-364 sampai 367 berlabel Manual Only (b) di TC sumber. Reset fixture backend (di atas). Pembacaan baris, badge, dan jumlah Event Log Activate.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client B) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan Seed Reader A, stok HS-01 dan HS-04, kuota Client A dan Client B, dan simulator; tutup popup yang masih terbuka; kembalikan sesi ke akun default.

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
12. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
13. Klik `[Cancel Activation]`
14. Klik ikon Event Log
15. Verifikasi jumlah baris Event Log bertambah tepat 1 dari baseline Event Log TC-GS-HHR-366
16. Verifikasi baris baru: Result `Failed`, Range Type `Long Range`, PIC `Sari D`
17. Verifikasi Device Name pada baris baru tidak memuat `Alias Uji`
18. Tutup Popup Event Log Activate dengan `✕`
19. Verifikasi teks pagination tabel utama sama dengan baseline daftar reader TC-GS-HHR-366 (tidak ada reader baru)

### TC-GS-HHR-364: Aktivasi berhasil menambah satu baris Activated

20. Klik ikon Event Log
21. Catat jumlah baris Event Log sebagai baseline N0 Event Log TC-GS-HHR-364
22. Tutup Popup Event Log Activate dengan `✕`
23. Klik `[+ Activate Reader]`
24. Klik `Long Range` pada Overlay `Select Range Type`
25. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
26. Klik `[Sync]`
27. Klik `[Submit]`
28. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
29. Klik ikon Event Log
30. Verifikasi baris baru teratas: Range Type `Long Range`, Device Name `Zebra RFID Reader - 2 (SKU-HHR-01)`, Result `Activated`, PIC `Sari D`
31. Verifikasi jumlah baris Event Log bertambah tepat 1 dari baseline N0 Event Log TC-GS-HHR-364
32. Tutup Popup Event Log Activate dengan `✕`
33. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 `Available`, kuota `Long Range` `5 of 6`), lalu muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-365: Aktivasi collision menambah satu baris Waiting for Approval

34. Klik ikon Event Log
35. Catat jumlah baris Event Log sebagai baseline Event Log TC-GS-HHR-365
36. Tutup Popup Event Log Activate dengan `✕`
37. Klik `[+ Activate Reader]`
38. Klik `Long Range` pada Overlay `Select Range Type`
39. Sambungkan reader dengan Serial Number `SN-HHR-00204` (HS-04, aktif di Client C) lewat simulator reader USB
40. Klik `[Sync]`
41. Klik `[Submit]`
42. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
43. Klik ikon Event Log
44. Verifikasi jumlah baris Event Log bertambah tepat 1 dari baseline Event Log TC-GS-HHR-365
45. Verifikasi baris baru teratas: Device Name `Zebra RFID Reader - 4 (SKU-HHR-01)`, Result `Waiting for Approval`, PIC `Sari D`
46. Tutup Popup Event Log Activate dengan `✕`

### TC-GS-HHR-367: Penolakan V-10 menambah satu baris Failed per Sync yang ditolak (Client B)

47. Logout dari akun Total Control Client A
48. Login sebagai Total Control Client B (`Spectra.env.GS_CLIENTB_TC_PASSWORD`)
49. Buka Global Settings > Hardware > Handheld Reader
50. Klik ikon Event Log
51. Catat jumlah baris Event Log Client B sebagai baseline Event Log TC-GS-HHR-367
52. Tutup Popup Event Log Activate dengan `✕`
53. Klik `[+ Activate Reader]`
54. Klik `Long Range` pada Overlay `Select Range Type`
55. Sambungkan reader dengan Serial Number `SN-HHR-00302` (Jalur B) lewat simulator reader USB
56. Klik `[Sync]`
57. Klik `[Sync]` sekali lagi
58. Verifikasi `[Submit]` disabled
59. Tutup Popup `Activate Handheld Reader` dengan `✕`
60. Klik ikon Event Log
61. Verifikasi jumlah baris Event Log bertambah tepat 2 dari baseline Event Log TC-GS-HHR-367
62. Verifikasi dua baris baru Result `Failed` (satu per `[Sync]` yang ditolak), masing-masing Device Name `—` dan Range Type `Long Range`
63. Tutup Popup Event Log Activate dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 5b). Kelas harness: eksternal (d), simulator reader USB; keempat TC berlabel Manual Only (b). Satu topik (pencatatan hasil aktivasi di Event Log), satu harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penutupan Popup `Activate Handheld Reader` pada TC-GS-HHR-366 (langkah 11 sampai 13): `[Submit]` yang ditolak V-04 meninggalkan hasil Sync pada popup, sehingga `✕` memunculkan dialog `Cancel Activation` (PRD §3.1 langkah 9 dan §4.2c, D-03; teks dialog dari TC-GS-HHR-89). Spec memverifikasi dialog itu, lalu klik `[Cancel Activation]` menurut A-1 (S-08); `Verifikasi` dialog bukan butir Expected TC-GS-HHR-366 dan dicatat di sini (S-03). Pada TC-GS-HHR-367, popup ditutup sesudah penolakan V-10 (langkah 59) dan langsung tertutup tanpa dialog (A-1).
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai Seed Reader A Client A (DD-01, `SN-HHR-00101`) bernama literal tanpa suffix; pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok (langkah 33), dinyatakan di `suite.md` dan Prerequisites; suite serial. Hasil aktivasi yang dibuat spec ini diasersi lewat baseline jumlah baris Event Log (S-12).
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-366 (penolakan, tidak mengubah kuota) dahulu, lalu TC-GS-HHR-364 dan 365 yang mengonsumsi kuota `Long Range` dengan pemulihan di antaranya (langkah 33), dan TC-GS-HHR-367 paling akhir karena ganti akun ke Client B (langkah 47 dan 48); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline (buka Event Log, catat jumlah, tutup); menyiapkan reader di simulator; "Tunggu aksi selesai" sebelum membuka Event Log (8b butir 8); menutup popup; klik `[Cancel Activation]` (langkah 13); pemulihan, muat ulang, Logout, Login, dan membuka layar Handheld Reader sesudah ganti akun. `Verifikasi` jumlah +1 pada TC-GS-HHR-365 (langkah 44) adalah baseline S-12 untuk klausa "baris baru" Expected a; angka +1 tidak tertulis sebagai butir Expected TC. `Verifikasi` `[Submit]` disabled (TC-GS-HHR-367) menjalankan klausa Expected b "karena `[Submit]` disabled" sebagai alasan tidak ada baris `Failed` dari `[Submit]`; jumlah +2 membuktikan tidak ada baris tambahan.
- Spec memuat 63 langkah, di atas sekitar 35 langkah. Alasan: empat blok TC satu kelas harness (simulator USB) dan satu topik; tiap blok mencatat baseline Event Log sendiri; blok aktivasi sukses dimulai dari state hasil reset (langkah 33) dan Client B memakai kuota dan Event Log sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; 12 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01).
- Pembagian TC lintas spec: Submit gagal 5xx lalu berhasil dengan satu baris Failed dan satu Activated (TC-GS-HHR-368) di spec 026; kegagalan driver dan penolakan Suspended tanpa baris Event Log (TC-GS-HHR-369 dan 370) di spec absence 065; screening, Search, Filter, Sort, dan Download Popup Event Log (TC-GS-HHR-356 sampai 363) di spec 066; log tiga surface untuk aktivasi yang sama (TC-GS-HHR-343 dan 344) di spec 064.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (Serial Number dan Current Power yang dikembalikan driver) tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-364 sampai 367 tidak menyatakan pemulihan state antar TC di dalam satu spec; kuota `Long Range` `5 of 6` tidak cukup untuk dua aktivasi berturut-turut. Spec menulis pemulihan lewat reset fixture backend (langkah 33); mekanismenya tidak didefinisikan dan disediakan tim FE/BE.
  - TC-GS-HHR-366 Expected b ("selalu nama bawaan") tidak menyebut nilai Device Name pada baris Failed; spec hanya mengasersi bahwa Device Name tidak memuat `Alias Uji`. TC-GS-HHR-367 tidak menyebut PIC baris Failed Client B dan tidak menyebut isi Event Log Client B sebelum uji; spec tidak mengasersi PIC dan memakai baseline jumlah.
  - TC-GS-HHR-365 tidak menyebut toast atau dampak kuota aktivasi collision; spec tidak mengasersinya.
