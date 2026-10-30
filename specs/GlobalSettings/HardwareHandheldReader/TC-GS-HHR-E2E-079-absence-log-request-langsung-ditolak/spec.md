---
id: TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak
title: "Absence Log: Request Langsung ke Server yang Ditolak Tidak Menambah Entri Changelog Handheld Reader, System Log Aktor, Activity Log, dan Event Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-229
  - TC-GS-HHR-403
  - TC-GS-HHR-404
  - TC-GS-HHR-405
  - TC-GS-HHR-406
  - TC-GS-HHR-407
  - TC-GS-HHR-408
  - TC-GS-HHR-413
  - TC-GS-HHR-414
  - TC-GS-HHR-415
  - TC-GS-HHR-416
  - TC-GS-HHR-420
  - TC-GS-HHR-474
coverage:
  web: automated
---

# Absence Log: Request Langsung ke Server yang Ditolak Tidak Menambah Entri Changelog Handheld Reader, System Log Aktor, Activity Log, dan Event Log

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas harness: absence log (kelas g). Pemicu berupa request langsung ke server (kelas a) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5` butir a). Suite `parallel: false`.
- Klien HTTP: klien HTTP yang mengirim request langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi pada langkah request hanya status respons dan pesan (sebagai anchor positif); toast dan perilaku FE tidak diasersi (bagian 8b butir 1). Endpoint request (kontrak `global-settings/hardware-handheld-reader/API/openapi.yaml`): Activate `POST /v2/hardware-tagging/handheld-readers`; Edit Alias Name `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/alias-name`; Edit Reader Power `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/reader-power`; Mark as Damaged `PATCH /v2/hardware-tagging/handheld-readers/status`; Delete `DELETE /v2/hardware-tagging/handheld-readers`; Cancel Request `POST /v2/hardware-tagging/handheld-readers/{readerId}/cancel-request`.
- Kemampuan membaca jumlah entri tiga surface log (disediakan tim FE/BE): audit trail permanen tumbuh dan tiap spec menambah entri, sehingga jumlah entri dibaca sebelum aksi dan asersi memakai perbandingan dengan jumlah itu, bukan angka absolut (bagian 8b butir 10, S-12). Tiga surface: Changelog Handheld Reader (ikon Changelog di halaman Handheld Reader), System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action). TC-GS-HHR-420 membaca Event Log (ikon Event Log), sesuai TC.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun UI pada tabel di bawah (lihat `suite.md`, Hook suite).
- Akun (Tabel Data Uji Pre-setup, Client A):

| Blok | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-413, TC-GS-HHR-414, TC-GS-HHR-415, TC-GS-HHR-416, TC-GS-HHR-474, TC-GS-HHR-420 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| 2 | TC-GS-HHR-403 sampai TC-GS-HHR-408, TC-GS-HHR-229 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |

- Login UI Total Control (blok 1) dilakukan di hook `before`; sesi klien HTTP blok 1 memakai akun yang sama. Blok 2 memakai langkah ganti akun eksplisit (sesi UI dan sesi klien HTTP Maya Putri). Hook `after` mengembalikan sesi UI ke akun default suite (Total Control).
- Data: Client A (plan Growth) dengan Seed Reader A (DD-01 s.d. DD-10, Tabel Data Uji Dinamis TC) dari fixture BE. Target request: DD-01 (Available), DD-03 (Damaged), DD-05 (Waiting for Approval), DD-07 (Available; Bulk Delete TC-GS-HHR-229), stok `SN-HHR-00201` (Long Range, HS-01) untuk Activate TC-GS-HHR-403. Semua request ditolak sehingga data hanya dibaca dan tidak ada yang dipulihkan; hook `after` memulihkan Seed Reader A sebagai cadangan bila request keliru diterima. Baseline jumlah entri dicatat per TC sebelum request (tiap TC punya baseline sendiri, S-12).
- Parameter iterasi blok 1 (langkah 1 sampai 13). Status respons `422`, pesan `This device is waiting for approval and cannot be changed.`:

| TC | Aksi pada reader DD-05 | Nilai request |
|---|---|---|
| TC-GS-HHR-413 | Edit Alias Name | `Alias Name` `Reader Dock 05-{runId}-079` |
| TC-GS-HHR-414 | Edit Reader Power | nilai 25 |
| TC-GS-HHR-415 | Mark as Damaged | tanpa nilai |
| TC-GS-HHR-416 | Delete | tanpa nilai |

- Parameter iterasi blok 2 (langkah 35 sampai 47). Status respons `403 Forbidden`:

| TC | Aksi | Target dan nilai request |
|---|---|---|
| TC-GS-HHR-403 | Activate | `SN-HHR-00201` Long Range atas reader Client A |
| TC-GS-HHR-404 | Edit Alias Name | DD-01, `Alias Name` `Reader Dock 01-{runId}-079` |
| TC-GS-HHR-405 | Edit Reader Power | DD-01, nilai 25 |
| TC-GS-HHR-406 | Mark as Damaged | DD-01 |
| TC-GS-HHR-407 | Delete | DD-01 |
| TC-GS-HHR-408 | Cancel Request | DD-05 |
| TC-GS-HHR-229 | Bulk Delete | DD-01 dan DD-07 dalam satu request bulk, tanpa melalui UI |

- State global yang diubah: tidak ada (seluruh request ditolak).

## Test Steps

### Blok 1 - Total Control: TC-GS-HHR-413 sampai TC-GS-HHR-416

Untuk setiap baris tabel "Parameter iterasi blok 1", lakukan langkah 1 sampai 13.

1. Buka Global Settings > Hardware > Handheld Reader
2. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri Changelog Handheld Reader, tutup dengan `✕`
3. Catat baseline System Log aktor: buka Global Settings > User > Detail akun Sari Dewi > tab System Log, catat jumlah entri
4. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
5. Kirim request langsung sesuai kolom Aksi dan Nilai request pada reader DD-05 dengan sesi Sari Dewi
6. Verifikasi respons berstatus 422
7. Verifikasi pesan respons `This device is waiting for approval and cannot be changed.`
8. Buka Global Settings > Hardware > Handheld Reader, lalu buka ikon Changelog
9. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline langkah 2 (tidak bertambah)
10. Tutup Modal Changelog dengan `✕`, lalu buka Global Settings > User > Detail akun Sari Dewi > tab System Log
11. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 3 (tidak bertambah)
12. Buka Global Settings > Activity Log > tab User Action
13. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 4 (tidak bertambah)
### TC-GS-HHR-474: Request bulk seluruhnya dilewati dengan alasan campuran dijawab 409

14. Buka Global Settings > Hardware > Handheld Reader
15. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri Changelog Handheld Reader, tutup dengan `✕`
16. Catat baseline System Log aktor: buka Global Settings > User > Detail akun Sari Dewi > tab System Log, catat jumlah entri
17. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
18. Kirim request bulk Mark as Damaged langsung berisi DD-03 (Damaged) dan DD-05 (Waiting for Approval) dengan sesi Sari Dewi
19. Verifikasi respons berstatus 409 Conflict
20. Buka Global Settings > Hardware > Handheld Reader, lalu buka ikon Changelog
21. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline langkah 15 (tidak bertambah)
22. Tutup Modal Changelog dengan `✕`, lalu buka Global Settings > User > Detail akun Sari Dewi > tab System Log
23. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 16 (tidak bertambah)
24. Buka Global Settings > Activity Log > tab User Action
25. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 17 (tidak bertambah)

### TC-GS-HHR-420: Aktivasi langsung tanpa Serial Number ditolak

26. Buka Global Settings > Hardware > Handheld Reader
27. Catat baseline Event Log: klik ikon Event Log, catat jumlah baris, tutup popup
28. Kirim request aktivasi langsung tanpa Serial Number untuk Long Range dengan sesi Sari Dewi
29. Verifikasi respons berstatus 422
30. Verifikasi pesan respons `Serial number must not be empty`
31. Klik ikon Event Log
32. Verifikasi jumlah baris Event Log sama dengan baseline langkah 27 (tidak ada baris baru)
33. Tutup popup Event Log

### Blok 2 - Read Only: TC-GS-HHR-403 sampai TC-GS-HHR-408 dan TC-GS-HHR-229

34. Logout, lalu login sebagai Maya Putri (Read Only) pada sesi UI, dan ganti sesi klien HTTP ke Maya Putri

Untuk setiap baris tabel "Parameter iterasi blok 2", lakukan langkah 35 sampai 47.

35. Buka Global Settings > Hardware > Handheld Reader
36. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri Changelog Handheld Reader, tutup dengan `✕`
37. Catat baseline System Log aktor: buka Global Settings > User > Detail akun Maya Putri > tab System Log, catat jumlah entri
38. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
39. Kirim request langsung sesuai kolom Aksi dan Target dan nilai request dengan sesi Maya Putri
40. Verifikasi respons berstatus 403 Forbidden
41. Muat ulang halaman Handheld Reader
42. Buka ikon Changelog
43. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline langkah 36 (tidak bertambah)
44. Tutup Modal Changelog dengan `✕`, lalu buka Global Settings > User > Detail akun Maya Putri > tab System Log
45. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 37 (tidak bertambah)
46. Buka Global Settings > Activity Log > tab User Action
47. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 38 (tidak bertambah)

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 8 Security & Defense-in-Depth dan section 3k Bulk). Kelas harness: absence log (g), prinsip 13g konvensi bagian 3. Pemicu request langsung ke server adalah kelas a yang hanya membentuk kondisi yang diasersi tidak tercatat (`P-5` butir a); tiap TC punya sesi, baseline, dan request sendiri.
- Pembagian TC lintas spec (S-05): setiap TC di spec ini terbelah antara presence dan absence dan juga ada di `sourceTc` spec asalnya. TC-GS-HHR-403 sampai TC-GS-HHR-408 dan TC-GS-HHR-413 sampai TC-GS-HHR-416 ada di `TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server` (status respons, pesan, state data, elemen Hidden sesudah muat ulang); TC-GS-HHR-420 ada di `TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power` (status 422, pesan, tidak ada reader baru); TC-GS-HHR-474 ada di `TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server` (respons 409 dan Status `Damaged` serta `Waiting for Approval` tetap); TC-GS-HHR-229 ada di `TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server` (respons 403 Forbidden dan kedua reader tetap ada). Rujukan sebaliknya ada di Notes spec 049. Spec ini hanya mengasersi jumlah entri log tidak bertambah, dengan status respons dan pesan sebagai anchor positif.
- Anchor absence (bagian 8b butir 2): pemicu yang terhubung ke surface log adalah request yang ditolak; `Verifikasi` status respons (langkah 6, 7, 19, 29, 30, 40) membuktikan server sudah memproses request sebelum jumlah entri dibandingkan, dan baseline jumlah entri dicatat sebelum pemicu. Perbandingan sama-dengan-baseline adalah asersi jumlah (bukan kelas g murni) dan memakai baseline dari langkah sebelum request (S-12).
- Ukuran: 47 langkah nominal; dengan ekspansi iterasi (blok 1: 13 langkah dikali 4 baris, blok 2: 13 langkah dikali 7 baris) sekitar 165 langkah. Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (absence log dengan pemicu request langsung), tiap TC memakai pola baca-log berpola yang sama (catat baseline tiga surface, kirim request, buka ulang tiga surface) dan berdiri sendiri; kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna. Langkah yang diulang: langkah 1 sampai 13 (blok 1) dan langkah 35 sampai 47 (blok 2), parameter tiap iterasi ada di tabel `## Prerequisites`.
- Urutan: blok Total Control lebih dulu (akun hook `before`), lalu Read Only sesudah ganti akun eksplisit (langkah 34), supaya sesi UI diganti sekali. Urutan TC mengikuti pengelompokan akun, bukan nomor TC sumber (413 sampai 416, 474, 420, lalu 403 sampai 408 dan 229). TC-GS-HHR-229 diletakkan sesudah 403 sampai 408 sebagai iterasi ketujuh blok 2 karena aktornya sama (Maya Putri, Read Only); tiap iterasi punya baseline tiga surface, request langsung, dan perbandingan sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka halaman Handheld Reader dan menutup Modal Changelog serta popup Event Log (langkah 1, 8, 10, 14, 20, 22, 26, 33, 35, 44), mencatat baseline (langkah 2 sampai 4, 15 sampai 17, 27, 36 sampai 38), membuka surface log untuk dibaca (langkah 12, 24, 31, 42, 46), logout lalu login Maya Putri (langkah 34), dan muat ulang halaman (langkah 41).
- Pembacaan log memakai halaman Handheld Reader dan surface yang sama sebelum dan sesudah request; jumlah entri dibandingkan dengan baseline per surface, tanpa mengandalkan posisi "teratas" (S-12, S-14).
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai nama literal tanpa suffix reader Pre-setup DD-01, DD-03, DD-05, dan DD-07 Client A sebagai target request yang ditolak; data hanya dibaca, pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE (hook `after` sebagai cadangan), dinyatakan di `suite.md` dan Prerequisites; suite serial.
- Temuan untuk QA:
  - TC-GS-HHR-420 hanya menyebut Event Log sebagai surface pembacaan (bukan tiga surface log) dan tanpa langkah baseline; spec membaca Event Log saja dan menambah baseline jumlah baris (S-12). Pembacaan tiga surface log tidak ditambahkan karena tidak ada di TC (S-02).
  - TC-GS-HHR-229 dan TC-GS-HHR-403 sampai TC-GS-HHR-408 membuka Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai Read Only tanpa menyebut path surface itu dan tanpa menyebut apakah Read Only boleh membukanya; spec memakai path System Log aktor dan Activity Log seperti pada spec 049 dan mengikuti TC. Bila Read Only tidak dapat membuka salah satu surface, pembacaan jumlah entri dilakukan lewat kemampuan baca log yang disediakan tim FE/BE.
  - TC-GS-HHR-403 tidak merinci payload Activate (Range Type dan Serial Number); spec memakai `SN-HHR-00201` Long Range supaya penolakan berasal dari izin. TC-GS-HHR-413 sampai TC-GS-HHR-416 tidak merinci nilai request: spec memakai `Alias Name` bersuffix `Reader Dock 05-{runId}-079` dan Reader Power 25.
  - TC-GS-HHR-474 Expected b menulis jumlah entri tiga surface tidak bertambah dalam butir yang sama dengan Status `Damaged` dan `Waiting for Approval` tetap; asersi Status ada di spec 049 dan asersi jumlah entri di spec ini.
  - TC-GS-HHR-229 dan TC-GS-HHR-403 sampai TC-GS-HHR-416 menyasar Seed Reader A bersama (DD-01, DD-03, DD-05, DD-07) padahal S-06 mewajibkan data milik spec; reader milik spec tidak dapat ditambahkan karena kuota `Long Range` Client A sudah terpakai 5 dari 6. Seluruh request ditolak sehingga data hanya dibaca.
  - TC-GS-HHR-229, TC-GS-HHR-403 sampai TC-GS-HHR-408, 413 sampai 416, 420, dan 474 tidak mencantumkan Post Condition.
