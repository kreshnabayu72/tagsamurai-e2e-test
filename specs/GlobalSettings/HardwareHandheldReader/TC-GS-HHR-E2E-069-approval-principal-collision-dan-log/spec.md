---
id: TC-GS-HHR-E2E-069-approval-principal-collision-dan-log
title: "Keputusan Approval Principal atas Collision: Approve, Reject, Cancel Request, Pencatatan Log, dan Isolasi Tenant Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-371
  - TC-GS-HHR-372
  - TC-GS-HHR-385
  - TC-GS-HHR-386
  - TC-GS-HHR-387
  - TC-GS-HHR-388
  - TC-GS-HHR-389
coverage:
  web: automated
---

# Keputusan Approval Principal atas Collision: Approve, Reject, Cancel Request, Pencatatan Log, dan Isolasi Tenant Lain

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, Principal memutuskan approval saat sesi Client terbuka; dua tenant pada TC-GS-HHR-386). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| P | Principal (Admin Console) | Bambang Hartono | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |
| C | Total Control (Client C) | - (tidak tertulis di Pre-setup TC) | `totalControl_automated_qaTeam3@qwertysystem.net` | `Spectra.env.GS_CLIENTC_TC_PASSWORD` |

- Password tidak ditulis di spec atau fixture.
- Login Sesi A dilakukan di hook `before`; Sesi P dan Sesi C dibuka dengan langkah ganti akun eksplisit (langkah 1 dan 2) karena hasilnya diasersi. Hook `after` menutup Sesi P dan Sesi C, lalu mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE): DD-05 (`Chainway C72 - 1`, Long Range, Source Self-Purchased, `Waiting for Approval`, permintaan collision di Admin Console > Approvals untuk `SN-HHR-00105`); kartu `Long Range` `5 of 6`, `1 remaining` pada keadaan awal. Client C: reader `SN-HHR-00301` aktif dan dipakai (Self-Purchased, tenant lain).
- Kemampuan teknis (disediakan tim FE/BE):
  - Konteks browser kedua dan ketiga (Sesi P dan Sesi C).
  - Pemulihan Seed Reader A dan permintaan Approvals DD-05 ke keadaan Tabel Data Uji TC antar blok (fixture BE; DD-05 menjadi Available, terhapus, atau permintaannya dibatalkan oleh tiap blok).
- Baseline: jumlah entri Changelog Handheld Reader Client A, Global Settings > Activity Log > tab `User Action` Client A dan Detail User Sari Dewi > Tab System Log (TC-GS-HHR-371 dan TC-GS-HHR-372), Changelog dan Activity Log (tab `User Action`) Client C, serta Activity Log dan System Log akun Principal di Admin Console dicatat sebelum keputusan Principal tiap blok; jumlah baris Tab History Approvals > Hardware Stock dan jumlah entri Changelog Hardware Stock dicatat sebelum Cancel Request Client (blok 3, TC-GS-HHR-388) (S-12).
- Jendela amat push realtime (TC-GS-HHR-389): TC tidak menyatakan durasi; 5 detik tanpa memuat ulang halaman (langkah 13) adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (konvensi bagian 6, jendela amat SSE).
- State global yang diubah: DD-05 dan stok `SN-HHR-00105` di Admin Console. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Persiapan sesi

1. Ganti akun: buka konteks browser kedua (Sesi P) dan login sebagai Principal Bambang Hartono
2. Ganti akun: buka konteks browser ketiga (Sesi C) dan login sebagai Total Control Client C

### Blok 1 - Approve collision DD-05: TC-GS-HHR-389, TC-GS-HHR-385, TC-GS-HHR-371, TC-GS-HHR-386

3. Pulihkan Seed Reader A dan permintaan Approvals DD-05
4. Sesi C: buka Global Settings > Hardware > Handheld Reader, catat jumlah entri Changelog dan jumlah entri Activity Log (Global Settings > Activity Log > tab `User Action`) Client C sebagai baseline
5. Sesi C: ketik Search `SN-HHR-00301`, tekan Enter, catat `Status` reader sebagai Status awal
6. Sesi A: muat ulang Handheld Reader, klik ikon Changelog, catat jumlah entri Changelog sebagai baseline, tutup Modal Changelog
7. Sesi A: buka Global Settings > Activity Log > tab `User Action`, catat jumlah entri; buka Global Settings > User > Detail akun Sari Dewi > Tab System Log, catat jumlah entri
8. Sesi P: buka Activity Log di Admin Console, catat jumlah entri Activity Log akun Principal sebagai baseline
9. Sesi P: buka System Log di Admin Console, catat jumlah entri System Log akun Principal sebagai baseline
10. Sesi A: buka Global Settings > Hardware > Handheld Reader dan biarkan daftar terbuka tanpa refresh
11. Sesi P: buka Admin Console > Approvals dan klik Approve pada permintaan DD-05 (`SN-HHR-00105`)
12. Tunggu aksi selesai
13. Tunggu 5 detik tanpa memuat ulang halaman
14. Sesi A: amati daftar yang sedang terbuka tanpa refresh
15. Verifikasi baris DD-05 tetap menampilkan `Status` `Waiting for Approval`
16. Verifikasi tidak ada push realtime ke daftar
17. Verifikasi tidak ada muat ulang otomatis
18. Sesi A: muat ulang halaman Handheld Reader
19. Verifikasi baris DD-05 `Status` `Available`
20. Verifikasi badge `Status` baris DD-05 bergaya `severity="success"` (identitas `Active` di Admin Console tampil sebagai `Available`)
21. Sesi A: buka Overlay row action DD-05
22. Verifikasi Overlay row action DD-05 memuat `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`, `Delete`
23. Tutup Overlay row action DD-05 dengan `Esc`
24. Verifikasi kartu `Long Range` tetap `5 of 6` dan `1 remaining`
25. Sesi A: klik ikon Changelog
26. Verifikasi jumlah entri Changelog bertambah satu dari baseline
27. Verifikasi entri teratas Changelog: `Edit` | `Chainway C72 - 1` | `Status` | `Waiting for Approval` | `Available` | `Principal`
28. Sesi A: tutup Modal Changelog
29. Sesi P: buka Activity Log di Admin Console
30. Verifikasi jumlah entri Activity Log akun Principal bertambah satu dari baseline
31. Verifikasi entri teratas Activity Log akun Principal: `Approve Request` | `Handheld Reader` | `Chainway C72 - 1` | `Status` | `Waiting for Approval` | `Available` | `Principal`
32. Sesi P: buka System Log di Admin Console
33. Verifikasi jumlah entri System Log akun Principal bertambah satu dari baseline
34. Verifikasi entri teratas System Log akun Principal di Admin Console memuat entri yang sama dengan Action `Edit`
35. Sesi A: buka kembali Global Settings > Activity Log > tab `User Action`
36. Verifikasi jumlah entri Activity Log Client A sama dengan baseline (tidak ada entri keputusan Principal di surface Global Settings)
37. Sesi A: buka kembali Global Settings > User > Detail akun Sari Dewi > Tab System Log
38. Verifikasi jumlah entri System Log Sari Dewi sama dengan baseline (tidak ada entri keputusan Principal di surface Global Settings)
39. Sesi C: muat ulang Handheld Reader, ketik Search `SN-HHR-00301`, tekan Enter
40. Verifikasi reader `SN-HHR-00301` `Status` tetap `Available` sama dengan Status awal (tidak berubah)
41. Sesi C: bersihkan Search dengan klik `(←)` pada kotak Search, klik ikon Changelog
42. Verifikasi sedikitnya satu entri Changelog Client C tampil
43. Verifikasi jumlah entri Changelog Client C sama dengan baseline (tidak ada entri baru dari keputusan ini)
44. Sesi C: tutup Modal Changelog, buka Global Settings > Activity Log > tab `User Action` Client C
45. Verifikasi jumlah entri Activity Log Client C sama dengan baseline (tidak ada entri baru dari keputusan ini)

### Blok 2 - Reject collision DD-05: TC-GS-HHR-387, TC-GS-HHR-372

46. Pulihkan Seed Reader A dan permintaan Approvals DD-05
47. Sesi A: muat ulang Handheld Reader, klik ikon Changelog, catat jumlah entri Changelog sebagai baseline, tutup Modal Changelog
48. Sesi A: buka Global Settings > Activity Log > tab `User Action`, catat jumlah entri; buka Global Settings > User > Detail akun Sari Dewi > Tab System Log, catat jumlah entri
49. Sesi P: buka Activity Log di Admin Console, catat jumlah entri Activity Log akun Principal sebagai baseline
50. Sesi P: buka System Log di Admin Console, catat jumlah entri System Log akun Principal sebagai baseline
51. Sesi P: catat `Status` stok `SN-HHR-00105` di Admin Console sebagai Status awal
52. Sesi A: buka Global Settings > Hardware > Handheld Reader
53. Sesi P: buka Admin Console > Approvals dan klik Reject pada permintaan DD-05 (`SN-HHR-00105`)
54. Tunggu aksi selesai
55. Sesi A: muat ulang halaman Handheld Reader
56. Verifikasi sedikitnya satu baris reader Seed Reader A tampil
57. Verifikasi baris DD-05 tidak ada di tabel
58. Verifikasi kartu `Long Range` menjadi `4 of 6` dan `2 remaining`
59. Sesi P: buka Hardware Stock, ketik Search `SN-HHR-00105`, tekan Enter
60. Verifikasi `Status` stok `SN-HHR-00105` di Admin Console sama dengan Status awal (tidak berubah)
61. Verifikasi identitas perangkat `SN-HHR-00105` berstatus `Rejected` dipertahankan di Admin Console untuk jejak audit
62. Verifikasi sedikitnya satu baris reader Seed Reader A tampil
63. Verifikasi tidak ada reader berstatus `Rejected` di daftar Handheld Reader Global Settings
64. Sesi A: klik ikon Changelog
65. Verifikasi jumlah entri Changelog bertambah satu dari baseline
66. Verifikasi entri teratas Changelog: `Delete` | `Chainway C72 - 1` | `Device Name` | `Chainway C72 - 1` | `—` | `Principal`
67. Sesi A: tutup Modal Changelog
68. Sesi P: buka Activity Log di Admin Console
69. Verifikasi jumlah entri Activity Log akun Principal bertambah satu dari baseline
70. Verifikasi entri teratas Activity Log akun Principal: `Reject Request` | `Handheld Reader` | `Chainway C72 - 1` | `Device Name` | `Chainway C72 - 1` | `—` | `Principal`
71. Sesi P: buka System Log di Admin Console
72. Verifikasi jumlah entri System Log akun Principal bertambah satu dari baseline
73. Verifikasi entri teratas System Log akun Principal di Admin Console memuat entri yang sama dengan Action `Delete`
74. Sesi A: buka kembali Global Settings > Activity Log > tab `User Action`
75. Verifikasi jumlah entri Activity Log Client A sama dengan baseline (tidak ada entri keputusan Principal di surface Global Settings)
76. Sesi A: buka kembali Global Settings > User > Detail akun Sari Dewi > Tab System Log
77. Verifikasi jumlah entri System Log Sari Dewi sama dengan baseline (tidak ada entri keputusan Principal di surface Global Settings)

### Blok 3 - Cancel Request DD-05 oleh Client: TC-GS-HHR-388

78. Pulihkan Seed Reader A dan permintaan Approvals DD-05
79. Sesi P: buka Admin Console > Approvals > Hardware Stock, klik Tab History, catat jumlah baris Tab History sebagai baseline Tab History
80. Sesi P: buka Changelog Hardware Stock, catat jumlah entri sebagai baseline Changelog Hardware Stock, tutup Changelog Hardware Stock
81. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request`
82. Sesi A: klik `[Cancel Request]` pada dialog
83. Tunggu aksi selesai
84. Sesi P: buka Admin Console > Approvals > Hardware Stock, klik Tab History
85. Verifikasi jumlah baris Tab History bertambah satu dari baseline Tab History
86. Sesi P: buka Tab Active, ketik Search `SN-HHR-00105`, tekan Enter
87. Verifikasi permintaan collision untuk `SN-HHR-00105` tidak muncul di Tab Active pada Approvals > Hardware Stock (empty state `No results found`)
88. Sesi P: klik Tab History pada Approvals > Hardware Stock, ketik Search `SN-HHR-00105`, tekan Enter
89. Verifikasi baris teratas Tab History memuat permintaan `SN-HHR-00105` dengan `Decision` `Canceled`
90. Verifikasi `Decided By` permintaan tersebut `—`
91. Sesi P: buka Changelog Hardware Stock
92. Verifikasi jumlah entri Changelog Hardware Stock bertambah satu dari baseline Changelog Hardware Stock
93. Verifikasi entri teratas Changelog Hardware Stock memuat entri `Device Activation Canceled` dengan Old Value `Waiting for Approval` dan New Value `Canceled`

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 5c dan 7b). TC-GS-HHR-371, 372, 385 sampai 389 berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhannya ditulis di Prerequisites.
- Urutan blok: keputusan yang mempertahankan DD-05 (Approve) lebih dulu, lalu yang menghapus DD-05 (Reject, Cancel Request) (prinsip 3 butir 5). TC-GS-HHR-389 diletakkan di awal Blok 1 karena asersinya harus terjadi sebelum refresh; langkah Approve yang sama dipakai bersama TC-GS-HHR-385, TC-GS-HHR-371, dan TC-GS-HHR-386 (satu keputusan, banyak surface), dan ini dicatat di sini sebagai penggabungan.
- Cara baca entri baru (S-12, S-14): entri baru pada audit trail (Changelog, Activity Log dan System Log akun Principal, Tab History, Changelog Hardware Stock) dibaca pada baris teratas urutan default `Date` terbaru sesudah `Verifikasi` selisih satu dari baseline (langkah 26, 30, 33, 65, 69, 72, 85, 92); satu keputusan menghasilkan satu entri per surface sehingga tidak ada himpunan baris dalam menit yang sama.
- Spec melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (multi-konteks dengan Principal sebagai pemutus approval) dan topik yang sama; tiap blok berdiri sendiri karena Seed Reader A dan permintaan Approvals dipulihkan di awal blok (langkah 3, 46, 78), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Bagian pencatatan log di blok 1 dan 2 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom).
- Jumlah entri Global Settings > Activity Log Client A dan Detail User Sari Dewi > Tab System Log yang sama dengan baseline (TC-GS-HHR-371 butir d dan TC-GS-HHR-372 butir d) dan "tidak ada entri baru Client C" (TC-GS-HHR-386) ditulis di spec ini dengan baseline jumlah entri (S-12) dan butir P-1 konvensi bagian 3: kondisi berat (keputusan Principal baru saja dibangun di spec yang sama) membuat memindahkannya ke spec absence kehilangan konteks. Penggabungan dengan spec absence (spec 065) tidak dilakukan karena spec itu tidak memuat keputusan Principal.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan, mencatat baseline (membuka surface log, mencatat jumlah entri; pola S-14), menunggu 5 detik tanpa memuat ulang halaman (langkah 13), muat ulang, menutup Overlay dan Modal Changelog, bersihkan Search, berpindah tab. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi.
- Anchor absence (8b butir 2): `Verifikasi` sedikitnya satu baris reader Seed Reader A tampil (langkah 56 dan 62) ditulis sebelum asersi absence baris DD-05 dan absence reader berstatus `Rejected`; pada langkah 62 daftar yang diamati adalah daftar Sesi A hasil muat ulang langkah 55. `Verifikasi` anchor itu tidak ada di Expected TC dan dicatat di sini (S-03).
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai nama literal tanpa suffix Seed Reader A Client A (DD-05, `Chainway C72 - 1`) beserta permintaan collision DD-05 di Admin Console; pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE di hook `after` dan sebagai langkah pemulihan antar blok (langkah 3, 46, 78), dinyatakan di `suite.md` dan Prerequisites; suite serial.
- Temuan untuk QA:
  - TC-GS-HHR-389 Expected a tidak menyebut durasi pengamatan tanpa push realtime; spec memakai jendela 5 detik (langkah 13), lihat Prerequisites.
  - Nama user Total Control Client C tidak tertulis di Pre-setup TC (kolom nama `-`); spec menyebutnya "Total Control Client C".
  - TC-GS-HHR-387 butir c ("Status stok Admin Console tidak berubah") tidak menyebut nilai awal; spec mencatat Status stok sebelum keputusan sebagai baseline.
  - TC-GS-HHR-387 butir d ("identitas perangkat berstatus `Rejected` dipertahankan di Admin Console") tidak menyebut lokasi tampilannya; spec membukanya di Hardware Stock.
  - TC-GS-HHR-385 butir a menyebut badge `severity="success"` tanpa menyebut cara membacanya di UI; spec mengasersi gaya badge hijau/sukses sesuai TC.
  - TC-GS-HHR-386 precondition d hanya menyebut `SN-HHR-00301` aktif tanpa Device Name; spec mencarinya lewat Search `SN-HHR-00301` (asumsi Search mencakup `Serial Number`, tidak dinyatakan di bagian ini).
