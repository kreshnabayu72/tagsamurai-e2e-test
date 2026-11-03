---
id: TC-AC-ACTS-E2E-077-absence-add-stock-bypass-seluruh-batch-preview-read-only-dan-remove-tanpa-tulis
title: "Absence Add Stock: Batch Seluruhnya Bypass Tanpa Entri Add Stock, Batch Seluruhnya Bypass Tanpa Baris Event Log, Cek Match Preview GPS Read-Only, dan Remove Tanpa Request atau Log"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-773
  - TC-AC-ACTS-779
  - TC-AC-ACTS-878
  - TC-AC-ACTS-946
coverage:
  web: automated
---

# Absence Add Stock: Batch Seluruhnya Bypass Tanpa Entri Add Stock, Batch Seluruhnya Bypass Tanpa Baris Event Log, Cek Match Preview GPS Read-Only, dan Remove Tanpa Request atau Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- SKU Pre-setup #15 `GPS-TRACK-CORE-G3` (TAG Type GPS, halaman Add Stock Import atau Manual Entry IMEI).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |
| TAG C | `Fixture.tagStock.rfidC.epc` | `Fixture.tagStock.rfidC.uid` |
| TAG D | `Fixture.tagStock.rfidD.epc` | `Fixture.tagStock.rfidD.uid` |

- Unit existing Available U1 dan U2 (identifier TAG A dan TAG B) dan unit terdaftar untuk TAG C dan TAG D di-seed fixture BE milik spec (jalur bypass E2a, Total Control); unit existing Available dengan IMEI uji untuk TC-AC-ACTS-773 (Distributor Toggle ON, jalur approval normal); Handheld Reader `HR-RFID-01` (Pre-setup #25) terdaftar dan terdeteksi di Sync Panel, simulator reader USB disediakan tim FE.
- IMEI uji GPS (Preview Manual Entry): `Fixture.tagStock.imeiA` dan `Fixture.tagStock.imeiB` (Data Uji Dinamis #2, `356938035643809` s/d `356938035643817`), belum terdaftar kecuali disebut lain.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: jumlah entri `Add Stock` dan `Duplicate Approved` di Activity Log, jumlah baris Event Log Tab Add Stock SKU `RFID-ASSET-CORE-R5`, saldo Stock Ledger entitas registrant, jumlah entri Activity Log, System Log, dan Tab Usage `HR-RFID-01`, serta Total Registered SKU `RFID-ASSET-CORE-R5` (lewat kemampuan baca BE)
2. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
3. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-779: Batch seluruhnya bypass, tidak ada entri Add Stock

4. Klik `[Add by Scan]`
5. Scan TAG A dan TAG B yang cocok unit Available U1 dan U2
6. Klik `[Stop]`
7. Klik `[Submit]`
8. Verifikasi toast `Success, TAG has been registered.`
9. Verifikasi tidak ada dialog `Partial Register`
10. Verifikasi tidak ada toast T-04
11. Verifikasi dua unit baru Available dengan TAG Code baru di Tab Available
12. Buka Activity Log
13. Verifikasi dua entri `Duplicate Approved` baru tampil
14. Verifikasi tidak ada entri `Add Stock` baru (jumlah entri `Add Stock` sama dengan baseline)
15. Buka modal Event Log SKU (Tab Add Stock)
16. Verifikasi baris existing Event Log tampil
17. Verifikasi tidak ada entri `Add Stock` baru (jumlah baris sama dengan baseline)
18. Tutup modal Event Log
19. Buka Device Allocation > Stock Balance Summary Panel
20. Verifikasi saldo Stock Ledger entitas registrant bertambah 2 dari baseline
21. Klik Breadcrumb `Stock`
22. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
23. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-946: Batch seluruhnya bypass tidak menulis baris Event Log

24. Catat baseline sesudah TC-AC-ACTS-779: jumlah entri `Add Stock` dan `Duplicate Approved` di Activity Log dan jumlah baris Event Log Tab Add Stock SKU `RFID-ASSET-CORE-R5` (lewat kemampuan baca BE)
25. Klik `[Add by Scan]`
26. Scan TAG C dan TAG D yang cocok unit terdaftar (bypass E2a)
27. Klik `[Stop]`
28. Klik `[Submit]`
29. Verifikasi toast `Success, TAG has been registered.`
30. Buka Activity Log
31. Verifikasi entri `Duplicate Approved` baru tampil (dua entri bertambah dari baseline langkah 24)
32. Verifikasi tidak ada entri `Add Stock` baru (jumlah entri `Add Stock` sama dengan baseline langkah 24)
33. Buka modal Event Log SKU (Tab Add Stock)
34. Verifikasi baris existing Event Log tampil
35. Verifikasi tidak ada baris baru di Tab Add Stock (jumlah baris sama dengan baseline langkah 24)
36. Tutup modal Event Log
37. Klik Breadcrumb `Stock`
38. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
39. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-878: Remove dari Scanned TAG List tidak menulis data

40. Catat baseline sesudah TC-AC-ACTS-946: jumlah entri Activity Log, System Log, dan Tab Usage `HR-RFID-01`, serta Total Registered SKU `RFID-ASSET-CORE-R5` (lewat kemampuan baca BE)
41. Klik `[Add by Scan]`, scan TAG A, scan TAG B, scan TAG C, lalu klik `[Stop]`
42. Hapus satu baris lewat Bulk Action > `Remove`
43. Klik `[Remove by Scan]`, scan satu baris lain, lalu klik `[Stop]`
44. Klik Breadcrumb `Stock`
45. Klik `[Leave]` pada dialog Unsaved Changes
46. Buka Activity Log
47. Verifikasi baris existing Activity Log tampil
48. Verifikasi tidak ada entri Activity Log baru dari Remove (jumlah entri sama dengan baseline langkah 40)
49. Buka System Log
50. Verifikasi tidak ada entri System Log baru dari Remove (jumlah entri sama dengan baseline langkah 40)
51. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
52. Verifikasi baris existing Tab Usage tampil
53. Verifikasi tidak ada baris baru di Tab Usage (jumlah baris sama dengan baseline langkah 40)
54. Verifikasi tidak ada unit tersimpan dari list yang dikeluarkan (Total Registered SKU sama dengan baseline langkah 40)
55. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)

### TC-AC-ACTS-773: Cek match Preview GPS bersifat read-only

56. Ketik Search `GPS-TRACK-CORE-G3`, tekan Enter
57. Klik (⋯) baris SKU `GPS-TRACK-CORE-G3`, klik `Add Stock`
58. Tambahkan IMEI yang sudah terdaftar di unit existing Available lewat Manual Entry
59. Verifikasi baris Preview berstatus Waiting for Approval
60. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
61. Buka Approvals > TAG Stock > Tab Active
62. Verifikasi baris existing Approvals Tab Active tampil
63. Verifikasi tidak ada Subject baru sebelum `[Submit]` (jumlah Subject pending sama dengan baseline)
64. Buka Detail SKU `GPS-TRACK-CORE-G3` > Tab Available
65. Verifikasi tidak ada unit Waiting baru (jumlah unit Tab Available sama dengan baseline)
66. Buka Activity Log
67. Verifikasi tidak ada entri Activity Log baru (jumlah entri sama dengan baseline)

## Notes

- Spec kelas g (P-5 butir a): pemicu scan dan Manual Entry hanya membentuk kondisi yang diasersi tidak tercatat. Tiap TC punya baseline sendiri; baseline TC-AC-ACTS-946 (langkah 24) dan TC-AC-ACTS-878 (langkah 40) dicatat ulang di awal blok masing-masing, sesudah TC sebelumnya, karena audit trail dan Tab Usage bertambah oleh Submit TC sebelumnya (S-12).
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pencatatan baseline, `[Stop]`, penutupan modal Event Log, pembukaan ulang halaman Add Stock sesudah Submit, dan Search `GPS-TRACK-CORE-G3` untuk menemukan baris target (R-16). Hook `after` memulihkan sesi ke Total Control.
- Urutan TC dalam spec: 779, 946, 878, 773 (akun Total Control lebih dulu; Distributor terakhir, S-10).
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok kelas g dengan pemicu simulator reader dan Import atau Manual Entry; tiap blok punya baseline sendiri dan berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-878 Expected menulis "Activity Log, System Log, atau Activity Log" (Activity Log disebut dua kali); spec mengasersi Activity Log dan System Log.
  - TC-AC-ACTS-878 judul menyebut "tidak ada request" tetapi Expected hanya meminta tidak ada entri log, baris Usage, dan unit tersimpan; request jaringan tidak diasersi.
  - TC-AC-ACTS-946 menyebut requester Total Control entitas Principal tanpa SKU; spec memakai SKU RFID yang sama dengan TC-AC-ACTS-779.
  - TC-AC-ACTS-773 tidak menyebut hasil bila `[Submit]` dilakukan; hanya keadaan sebelum `[Submit]` yang diasersi.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
