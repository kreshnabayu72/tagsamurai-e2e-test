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
- Klien HTTP: klien HTTP yang mengirim request langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi pada langkah request hanya respons server (status dan pesan) dan state data; toast dan perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1). Satu-satunya asersi UI adalah keadaan elemen Hidden sesudah halaman dimuat ulang (Expected b TC-GS-HHR-403 sampai TC-GS-HHR-408).
- Endpoint request (kontrak `global-settings/hardware-handheld-reader/API/openapi.yaml`): Activate `POST /v2/hardware-tagging/handheld-readers`; Edit Alias Name `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/alias-name`; Edit Reader Power `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/reader-power`; Mark as Damaged `PATCH /v2/hardware-tagging/handheld-readers/status`; Delete `DELETE /v2/hardware-tagging/handheld-readers`; Cancel Request `POST /v2/hardware-tagging/handheld-readers/{readerId}/cancel-request`; Popup Detail `GET /v2/hardware-tagging/handheld-readers/{readerId}`; daftar reader `POST /v2/hardware-tagging/handheld-readers/list`.
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar reader Client A beserta `Status`, `Alias Name`, `Reader Power` per reader dan jumlah reader. Kata "tidak berubah" membandingkan dengan keadaan Seed Reader A pada Tabel Data Uji Dinamis TC.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun UI pada tabel di bawah (lihat `suite.md`, Hook suite).
- Akun (Tabel Data Uji Pre-setup, Client A):

| Blok | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-412, TC-GS-HHR-413, TC-GS-HHR-414, TC-GS-HHR-415, TC-GS-HHR-416 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| 2 | TC-GS-HHR-403 sampai TC-GS-HHR-408 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| 3 | TC-GS-HHR-409 | Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_HW_UPDATE_PASSWORD` |
| 4 | TC-GS-HHR-410 | Manage hardware (Create) | Rina Lestari | `manageHardwareCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_HW_CREATE_PASSWORD` |
| 5 | TC-GS-HHR-411 | Tanpa Capability | Hendra Gunawan | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Login UI Total Control (blok 1) dilakukan di hook `before`; sesi klien HTTP blok 1 memakai akun yang sama. Blok 2 butuh sesi UI Maya Putri (memuat ulang halaman dan mengamati elemen Hidden) dan memakai langkah ganti akun eksplisit; blok 3 sampai 5 hanya mengganti sesi klien HTTP. Hook `after` mengembalikan sesi UI ke akun default suite (Total Control) dan memulihkan Seed Reader A ke Tabel Data Uji Dinamis TC sebagai cadangan bila request keliru diterima.
- Data: Client A (plan Growth) dengan Seed Reader A (DD-01 s.d. DD-10) dari fixture BE. Target request memakai Seed Reader A: DD-01 (Available, Long Range, 30 dBm, `Alias Name` `—`), DD-05 (Waiting for Approval). Semua request ditolak sehingga data hanya dibaca (lihat Temuan untuk QA tentang S-06). Reader `SN-HHR-00301` milik tenant Client C (Self-Purchased; akun Total Control Client C `totalControl_automated_qaTeam3@qwertysystem.net` hanya identitas tenant pemilik dan tidak login di spec ini; Tabel Data Uji Pre-setup TC) dibaca pada TC-GS-HHR-412 dengan sesi Client A. Stok `SN-HHR-00201` (Long Range, HS-01) dipakai sebagai Serial Number pada request Activate TC-GS-HHR-403.
- Pembacaan log (Changelog Handheld Reader, System Log aktor, Activity Log) atas request yang ditolak ada di spec `TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak`; spec ini tidak membaca log.
- State global yang diubah: tidak ada (seluruh request ditolak).

## Test Steps

### Blok 1 - Total Control: TC-GS-HHR-412 sampai TC-GS-HHR-416

1. Kirim request langsung untuk membaca Popup Detail reader `SN-HHR-00301` milik Client C dengan sesi Sari Dewi
2. Verifikasi respons berstatus 404 Not Found
3. Verifikasi respons tidak memuat data reader Client C (keberadaan record tidak dibocorkan)
4. Kirim request langsung Edit Alias Name pada reader DD-05 dengan sesi Sari Dewi, `Alias Name` `Reader Dock 05-{runId}-012`
5. Verifikasi respons berstatus 422
6. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
7. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
8. Kirim request langsung Edit Reader Power pada reader DD-05 dengan sesi Sari Dewi, nilai 25
9. Verifikasi respons berstatus 422
10. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
11. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
12. Kirim request langsung Mark as Damaged pada reader DD-05 dengan sesi Sari Dewi
13. Verifikasi respons berstatus 422
14. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
15. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
16. Kirim request langsung Delete pada reader DD-05 dengan sesi Sari Dewi
17. Verifikasi respons berstatus 422
18. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
19. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`

### Blok 2 - Read Only: TC-GS-HHR-403 sampai TC-GS-HHR-408

20. Logout, lalu login sebagai Maya Putri (Read Only) pada sesi UI, dan ganti sesi klien HTTP ke Maya Putri
21. Buka Global Settings > Hardware > Handheld Reader
22. Kirim request langsung Activate untuk `SN-HHR-00201` Long Range atas reader Client A dengan sesi Maya Putri
23. Verifikasi respons berstatus 403 Forbidden
24. Verifikasi (lewat fixture BE) jumlah reader Client A tetap 10 dan tidak ada reader baru untuk `SN-HHR-00201`
25. Kirim request langsung Edit Alias Name DD-01 dengan sesi Maya Putri, `Alias Name` `Reader Dock 01-{runId}-012`
26. Verifikasi respons berstatus 403 Forbidden
27. Verifikasi (lewat fixture BE) `Alias Name` DD-01 tetap `—`
28. Kirim request langsung Edit Reader Power DD-01 dengan sesi Maya Putri, nilai 25
29. Verifikasi respons berstatus 403 Forbidden
30. Verifikasi (lewat fixture BE) `Reader Power` DD-01 tetap `30 dBm`
31. Kirim request langsung Mark as Damaged DD-01 dengan sesi Maya Putri
32. Verifikasi respons berstatus 403 Forbidden
33. Verifikasi (lewat fixture BE) `Status` DD-01 tetap `Available`
34. Kirim request langsung Delete DD-01 dengan sesi Maya Putri
35. Verifikasi respons berstatus 403 Forbidden
36. Verifikasi (lewat fixture BE) reader DD-01 tetap ada
37. Kirim request langsung Cancel Request DD-05 dengan sesi Maya Putri
38. Verifikasi respons berstatus 403 Forbidden
39. Verifikasi (lewat fixture BE) `Status` DD-05 tetap `Waiting for Approval`
40. Muat ulang halaman Handheld Reader
41. Verifikasi toolbar menampilkan `Search` dan `Filter` (halaman termuat)
42. Verifikasi tombol `[+ Activate Reader]` Hidden
43. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
44. Verifikasi Overlay row action DD-01 menampilkan `Detail`
45. Verifikasi `Edit Alias Name` tidak ada pada Overlay row action DD-01
46. Verifikasi `Edit Reader Power` tidak ada pada Overlay row action DD-01
47. Verifikasi `Mark as Damaged` tidak ada pada Overlay row action DD-01
48. Verifikasi `Delete` tidak ada pada Overlay row action DD-01
49. Tutup Overlay row action dengan Esc
50. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
51. Verifikasi Overlay row action DD-05 menampilkan `Detail`
52. Verifikasi `Cancel Request` tidak ada pada Overlay row action DD-05
53. Tutup Overlay row action dengan Esc

### Blok 3 - Manage hardware (Update): TC-GS-HHR-409

54. Ganti sesi klien HTTP ke Agus Wijaya (Manage hardware level Update)
55. Kirim request langsung Delete DD-01 dengan sesi Agus Wijaya
56. Verifikasi server menolak request (status penolakan, bukan 2xx)
57. Verifikasi (lewat fixture BE) reader DD-01 tetap ada

### Blok 4 - Manage hardware (Create): TC-GS-HHR-410

58. Ganti sesi klien HTTP ke Rina Lestari (Manage hardware level Create)
59. Kirim request langsung Edit Alias Name DD-01 dengan sesi Rina Lestari, `Alias Name` `Reader Dock 01-{runId}-012`
60. Verifikasi server menolak request (status penolakan, bukan 2xx)
61. Verifikasi (lewat fixture BE) `Alias Name` DD-01 tetap `—`

### Blok 5 - Tanpa Capability: TC-GS-HHR-411

62. Ganti sesi klien HTTP ke Hendra Gunawan (Tanpa Capability)
63. Kirim request langsung untuk membaca daftar reader Client A dengan sesi Hendra Gunawan
64. Verifikasi server menolak request (status penolakan, bukan 2xx)
65. Verifikasi respons tidak memuat data reader Client A

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 8 Security & Defense-in-Depth). Kelas harness: defense-in-depth (a), prinsip 13a konvensi bagian 3; keempat belas TC memakai pola yang sama (request langsung, asersi status respons dan state data). TC defense-in-depth lain ada di `TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power` dan `TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server`.
- K-1: TC kelas a ini memiliki Expected berupa respons API (status respons dan state data lewat fixture BE) yang tumpang tindih dengan `tc-hardware-handheld-reader-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec, sehingga spec FE+BE ini tetap memuatnya (konvensi bagian 2, K-1).
- Spec melewati sekitar 35 langkah (65 langkah nominal). Alasan: seluruh blok satu kelas harness (defense-in-depth tanpa harness eksternal) dan tiap blok berdiri sendiri (akun dan sesi klien HTTP sendiri); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: blok Total Control (TC-GS-HHR-412 sampai TC-GS-HHR-416) berada di awal karena akun hook `before`, lalu Read Only, Update, Create, dan Tanpa Capability, supaya sesi diganti sekali per akun. Pada blok 2 halaman dimuat ulang satu kali sesudah keenam request (TC sumber memuat ulang per TC) dan Expected b TC-GS-HHR-403 sampai TC-GS-HHR-408 diamati sesudah muat ulang itu; seluruh request ditolak sehingga keadaan halaman sama.
- Pembagian TC lintas spec: TC-GS-HHR-403 sampai TC-GS-HHR-408 dan TC-GS-HHR-413 sampai TC-GS-HHR-416 terbelah antara presence (status respons, pesan, state data di spec ini) dan absence (jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log tidak bertambah, S-05). Id TC tetap di `sourceTc` spec ini dan juga di `TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak`, yang mengirim request langsung nyata untuk tiap TC dengan user dan baseline sendiri. Spec ini tidak mengasersi log.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): logout lalu login sesi UI Maya Putri (langkah 20), membuka halaman Handheld Reader (langkah 21), muat ulang halaman (langkah 40), ganti sesi klien HTTP (langkah 54, 58, 62), serta membuka dan menutup Overlay row action (langkah 43, 49, 50, 53).
- Anchor absence untuk Expected b TC-GS-HHR-403 sampai TC-GS-HHR-408: langkah 41 (toolbar `Search` dan `Filter` tampil, halaman termuat) mendahului asersi `[+ Activate Reader]` Hidden; `Detail` tampil pada Overlay (langkah 44 dan 51) mendahului asersi opsi yang tidak ada (bagian 8b butir 2). Langkah 41 adalah asersi tambahan sebagai anchor, bukan Expected TC (S-03).
- Temuan untuk QA:
  - TC-GS-HHR-409 sampai TC-GS-HHR-411 menyatakan server "menolak" tanpa menyebut kode status; spec memakai asersi "status penolakan, bukan 2xx" dan tidak menebak kode. TC-GS-HHR-403 tidak merinci payload Activate (Range Type dan Serial Number); spec memakai `SN-HHR-00201` Long Range supaya penolakan berasal dari izin, bukan validasi payload.
  - TC-GS-HHR-403 sampai TC-GS-HHR-408 Expected b menyebut "elemen yang tidak berhak" tanpa menyebut elemennya; spec mengamati elemen yang bersesuaian dengan aksi tiap TC (`[+ Activate Reader]` untuk Activate, opsi Overlay row action `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Delete`, dan `Cancel Request` untuk TC lainnya).
  - TC-GS-HHR-413 sampai TC-GS-HHR-416 tidak merinci nilai request: spec memakai `Alias Name` bersuffix `Reader Dock 05-{runId}-012` dan Reader Power 25 pada request yang ditolak.
  - TC-GS-HHR-403 sampai TC-GS-HHR-416 menyasar Seed Reader A bersama (DD-01 dan DD-05) padahal S-06 mewajibkan data milik spec; reader milik spec tidak dapat ditambahkan karena kuota `Long Range` Client A sudah terpakai 5 dari 6 (DD-05 adalah Long Range Waiting for Approval). Seluruh request ditolak sehingga data hanya dibaca, dan Seed Reader A dipulihkan di hook `after` sebagai cadangan.
