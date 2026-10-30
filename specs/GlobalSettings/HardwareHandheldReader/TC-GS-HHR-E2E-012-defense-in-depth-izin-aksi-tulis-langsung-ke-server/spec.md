---
id: TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server
title: "Defense-in-Depth: Aksi Tulis Handheld Reader Tanpa Izin atau pada Reader Waiting for Approval Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-403
  - TC-GS-HHR-404
  - TC-GS-HHR-405
  - TC-GS-HHR-406
  - TC-GS-HHR-407
  - TC-GS-HHR-408
  - TC-GS-HHR-409
  - TC-GS-HHR-410
  - TC-GS-HHR-411
  - TC-GS-HHR-412
  - TC-GS-HHR-413
  - TC-GS-HHR-414
  - TC-GS-HHR-415
  - TC-GS-HHR-416
coverage:
  web: automated
---

# Defense-in-Depth: Aksi Tulis Handheld Reader Tanpa Izin atau pada Reader Waiting for Approval Ditolak Server

## Prerequisites

- Mode: FE+BE. Kelas harness: defense-in-depth (kelas a, request langsung ke server tanpa melalui UI). Suite `parallel: false`.
- Klien HTTP: klien HTTP yang mengirim request langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi hanya respons server (status dan pesan) dan state data; perilaku FE untuk respons yang sama (toast, elemen Hidden) tidak diasersi di spec ini (bagian 8b butir 1). Endpoint request tidak didefinisikan di TC dan tidak ditulis di spec ini; kontrak operasi mengikuti dokumen API modul yang disediakan tim FE/BE.
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar reader Client A beserta `Status`, `Alias Name`, `Reader Power` per reader dan jumlah reader. Kata "tidak berubah" membandingkan dengan keadaan Seed Reader A pada Tabel Data Uji Dinamis TC.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun UI pada tabel di bawah (lihat `suite.md`, Hook suite).
- Akun (Tabel Data Uji Pre-setup, Client A):

| Blok | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-412, TC-GS-HHR-413, TC-GS-HHR-414, TC-GS-HHR-415, TC-GS-HHR-416 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| 2 | TC-GS-HHR-403 sampai TC-GS-HHR-408 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| 3 | TC-GS-HHR-409 | Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| 4 | TC-GS-HHR-410 | Manage hardware (Create) | Rina Lestari | `manageHardwareCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| 5 | TC-GS-HHR-411 | Tanpa Capability | Hendra Gunawan | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Login UI Total Control (blok 1) dilakukan di hook `before`; sesi klien HTTP blok 1 memakai akun yang sama. Blok 2 butuh sesi UI Maya Putri (membaca log) dan memakai langkah ganti akun eksplisit; blok 3 sampai 5 hanya mengganti sesi klien HTTP. Hook `after` mengembalikan sesi UI ke akun default suite (Total Control) dan memulihkan Seed Reader A ke Tabel Data Uji Dinamis TC sebagai cadangan bila request keliru diterima.
- Data: Client A (plan Growth) dengan Seed Reader A (DD-01 s.d. DD-10) dari fixture BE. Target request memakai Seed Reader A: DD-01 (Available, Long Range, 30 dBm, `Alias Name` `—`), DD-05 (Waiting for Approval). Semua request ditolak sehingga data hanya dibaca (lihat Temuan untuk QA tentang S-06). Reader `SN-HHR-00301` milik Client C (Self-Purchased, tenant lain, Tabel Data Uji Pre-setup TC) dibaca pada TC-GS-HHR-412 dengan sesi Client A. Stok `SN-HHR-00201` (Long Range, HS-01) dipakai sebagai Serial Number pada request Activate TC-GS-HHR-403.
- Surface log (blok 1 dan blok 2): Changelog Handheld Reader, System Log aktor, dan Activity Log. Baseline berupa jumlah entri tiap surface dicatat sebelum request pertama blok dan dibandingkan sesudah request terakhir blok (S-12).
- State global yang diubah: tidak ada (seluruh request ditolak).

## Test Steps

### Blok 1 - Total Control: TC-GS-HHR-412 sampai TC-GS-HHR-416

1. Kirim request langsung untuk membaca Popup Detail reader `SN-HHR-00301` milik Client C dengan sesi Sari Dewi
2. Verifikasi respons berstatus 404 Not Found
3. Verifikasi respons tidak memuat data reader Client C (keberadaan record tidak dibocorkan)
4. Catat jumlah entri Changelog Handheld Reader sebagai baseline
5. Catat jumlah entri System Log aktor sebagai baseline
6. Catat jumlah entri Activity Log sebagai baseline
7. Kirim request langsung Edit Alias Name pada reader DD-05 dengan sesi Sari Dewi, `Alias Name` `Reader Dock 05-{runId}-012`
8. Verifikasi respons berstatus 422
9. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
10. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
11. Kirim request langsung Edit Reader Power pada reader DD-05 dengan sesi Sari Dewi, nilai 25
12. Verifikasi respons berstatus 422
13. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
14. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
15. Kirim request langsung Mark as Damaged pada reader DD-05 dengan sesi Sari Dewi
16. Verifikasi respons berstatus 422
17. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
18. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
19. Kirim request langsung Delete pada reader DD-05 dengan sesi Sari Dewi
20. Verifikasi respons berstatus 422
21. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
22. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
23. Buka kembali Changelog Handheld Reader
24. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah)
25. Tutup Modal Changelog
26. Buka kembali System Log aktor
27. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah)
28. Tutup System Log aktor
29. Buka kembali Activity Log
30. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak bertambah)
31. Tutup Activity Log

### Blok 2 - Read Only: TC-GS-HHR-403 sampai TC-GS-HHR-408

32. Logout, lalu login sebagai Maya Putri (Read Only) pada sesi UI, dan ganti sesi klien HTTP ke Maya Putri
33. Buka Global Settings > Hardware > Handheld Reader
34. Catat jumlah entri Changelog Handheld Reader sebagai baseline
35. Catat jumlah entri System Log aktor sebagai baseline
36. Catat jumlah entri Activity Log sebagai baseline
37. Kirim request langsung Activate untuk `SN-HHR-00201` Long Range atas reader Client A dengan sesi Maya Putri
38. Verifikasi server menolak request (status penolakan, bukan 2xx)
39. Verifikasi (lewat fixture BE) jumlah reader Client A tetap 10 dan tidak ada reader baru untuk `SN-HHR-00201`
40. Kirim request langsung Edit Alias Name DD-01 dengan sesi Maya Putri, `Alias Name` `Reader Dock 01-{runId}-012`
41. Verifikasi server menolak request (status penolakan, bukan 2xx)
42. Verifikasi (lewat fixture BE) `Alias Name` DD-01 tetap `—`
43. Kirim request langsung Edit Reader Power DD-01 dengan sesi Maya Putri, nilai 25
44. Verifikasi server menolak request (status penolakan, bukan 2xx)
45. Verifikasi (lewat fixture BE) `Reader Power` DD-01 tetap `30 dBm`
46. Kirim request langsung Mark as Damaged DD-01 dengan sesi Maya Putri
47. Verifikasi server menolak request (status penolakan, bukan 2xx)
48. Verifikasi (lewat fixture BE) `Status` DD-01 tetap `Available`
49. Kirim request langsung Delete DD-01 dengan sesi Maya Putri
50. Verifikasi server menolak request (status penolakan, bukan 2xx)
51. Verifikasi (lewat fixture BE) reader DD-01 tetap ada
52. Kirim request langsung Cancel Request DD-05 dengan sesi Maya Putri
53. Verifikasi server menolak request (status penolakan, bukan 2xx)
54. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
55. Muat ulang halaman Handheld Reader
56. Buka kembali Changelog Handheld Reader
57. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah)
58. Tutup Modal Changelog
59. Buka kembali System Log aktor
60. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah)
61. Tutup System Log aktor
62. Buka kembali Activity Log
63. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak bertambah)
64. Tutup Activity Log

### Blok 3 - Manage hardware (Update): TC-GS-HHR-409

65. Ganti sesi klien HTTP ke Agus Wijaya (Manage hardware level Update)
66. Kirim request langsung Delete DD-01 dengan sesi Agus Wijaya
67. Verifikasi server menolak request (status penolakan, bukan 2xx)
68. Verifikasi (lewat fixture BE) reader DD-01 tetap ada

### Blok 4 - Manage hardware (Create): TC-GS-HHR-410

69. Ganti sesi klien HTTP ke Rina Lestari (Manage hardware level Create)
70. Kirim request langsung Edit Alias Name DD-01 dengan sesi Rina Lestari, `Alias Name` `Reader Dock 01-{runId}-012`
71. Verifikasi server menolak request (status penolakan, bukan 2xx)
72. Verifikasi (lewat fixture BE) `Alias Name` DD-01 tetap `—`

### Blok 5 - Tanpa Capability: TC-GS-HHR-411

73. Ganti sesi klien HTTP ke Hendra Gunawan (Tanpa Capability)
74. Kirim request langsung untuk membaca daftar reader Client A dengan sesi Hendra Gunawan
75. Verifikasi server menolak request (status penolakan, bukan 2xx)
76. Verifikasi respons tidak memuat data reader Client A

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 8 Security & Defense-in-Depth). Kelas harness: defense-in-depth (a), prinsip 13a konvensi bagian 3; keempat belas TC memakai pola yang sama (request langsung, asersi status respons dan state data). Keputusan P-4 user: TC defense-in-depth yang Expected-nya berupa respons API tetap dimasukkan sebagai spec FE+BE. TC defense-in-depth lain ada di `TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power` dan `TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server`.
- Spec melewati sekitar 35 langkah (76 langkah nominal). Alasan: seluruh blok satu kelas harness (defense-in-depth tanpa harness eksternal) dan tiap blok berdiri sendiri (akun dan sesi klien HTTP sendiri); kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembacaan log tiga surface hanya di blok 1 dan blok 2.
- Urutan TC sumber diubah: blok Total Control (TC-GS-HHR-412 sampai TC-GS-HHR-416) berada di awal karena akun hook `before`, lalu Read Only, Update, Create, dan Tanpa Capability, supaya sesi diganti sekali per akun. Pada blok 1 dan blok 2 jumlah entri tiga surface log dibandingkan sekali sesudah semua request blok (TC-GS-HHR-413 sampai TC-GS-HHR-416 dan TC-GS-HHR-403 sampai TC-GS-HHR-408), karena tiap request ditolak dan tidak menambah entri; baseline dicatat sekali sebelum request pertama pemicu (S-12).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): logout lalu login sesi UI Maya Putri (langkah 32), ganti sesi klien HTTP (langkah 65, 69, 73), menutup Modal Changelog, System Log aktor, dan Activity Log (langkah 25, 28, 31, 58, 61, 64), serta mencatat baseline (langkah 4 sampai 6 dan 34 sampai 36).
- Asersi tidak bertambahnya entri log dibandingkan dengan baseline jumlah entri (bagian 8b butir 2, S-12); surface yang sama diukur sebelum dan sesudah, jadi baseline adalah jumlah awal yang dicatat. Spec absence kelas g untuk TC ini tidak ada, sehingga asersi ditulis di spec ini (S-05).
- Temuan untuk QA:
  - TC-GS-HHR-403 sampai TC-GS-HHR-408 Expected b (toast "You don't have permission to do this." dan elemen Hidden "pada jalur UI yang memicunya") adalah perilaku FE dan tidak diasersi pada request langsung (bagian 8b butir 1); perilaku FE untuk respons izin diasersi di spec jalur UI (`TC-GS-HHR-E2E-011-capability-dicabut-saat-aksi-berjalan`). TC-GS-HHR-412 butir a menyebut toast netral `This device is no longer available.` dan tidak diasersi karena alasan yang sama.
  - TC-GS-HHR-403 sampai TC-GS-HHR-411 menyatakan server "menolak" tanpa menyebut kode status; spec memakai asersi "status penolakan, bukan 2xx" dan tidak menebak kode. TC-GS-HHR-403 tidak merinci payload Activate (Range Type dan Serial Number); spec memakai `SN-HHR-00201` Long Range supaya penolakan berasal dari izin, bukan validasi payload.
  - TC-GS-HHR-403 sampai TC-GS-HHR-408 tidak menyebut halaman tempat Overlay atau path System Log aktor dan Activity Log dibuka, dan tidak menyebut apakah akun Read Only boleh membuka System Log aktor dan Activity Log; spec mengikuti TC.
  - TC-GS-HHR-413 sampai TC-GS-HHR-416 tidak merinci nilai request: spec memakai `Alias Name` bersuffix `Reader Dock 05-{runId}-012` dan Reader Power 25 pada request yang ditolak.
  - TC-GS-HHR-403 sampai TC-GS-HHR-416 menyasar Seed Reader A bersama (DD-01 dan DD-05) padahal S-06 mewajibkan data milik spec; reader milik spec tidak dapat ditambahkan karena kuota `Long Range` Client A sudah terpakai 5 dari 6 (DD-05 adalah Long Range Waiting for Approval). Seluruh request ditolak sehingga data hanya dibaca, dan Seed Reader A dipulihkan di hook `after` sebagai cadangan.
