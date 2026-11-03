---
id: TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps
title: "Resilience Add Stock: Submit Gagal (Toast T-03) pada RFID, NFC, BLE, dan GPS serta Submit RFID Tanpa Respons (Toast T-24)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-173
  - TC-AC-ACTS-206
  - TC-AC-ACTS-235
  - TC-AC-ACTS-265
  - TC-AC-ACTS-811
coverage:
  web: automated
---

# Resilience Add Stock: Submit Gagal (Toast T-03) pada RFID, NFC, BLE, dan GPS serta Submit RFID Tanpa Respons (Toast T-24)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- SKU Pre-setup #13 `NFC-CARD-BETA-N2` (Device Name `NFC Access Card`, Brand `Beta`, Model `N2`, TAG Type NFC).
- SKU Pre-setup #14 `BLE-BEACON-ALPHA-B1` (Device Name `BLE Beacon Alpha`, Brand `Alpha`, Model `B1`, TAG Type BLE).
- SKU Pre-setup #15 `GPS-TRACK-CORE-G3` (TAG Type GPS, halaman Add Stock Import atau Manual Entry IMEI).
- Kemampuan teknis: simulator pemindai RFID, NFC, BLE (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |

- TAG uji NFC (TC-AC-ACTS-206) (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | UID |
|---|---|
| TAG A | `Fixture.tagStock.nfcA.uid` (`A1B2C3D4E5F7`) |
| TAG B | `Fixture.tagStock.nfcB.uid` |

- TAG uji BLE (TC-AC-ACTS-235) (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |
| TAG B | `Fixture.tagStock.bleB.mac` |

- IMEI uji GPS (Preview Manual Entry): `Fixture.tagStock.imeiA` dan `Fixture.tagStock.imeiB` (Data Uji Dinamis #2, `356938035643809` s/d `356938035643817`), belum terdaftar kecuali disebut lain.
- Kemampuan teknis tambahan: `Spectra.intercept()` untuk memaksa respons 5xx atau menahan respons request Submit (di atas backend nyata); intercept dilepas segera sesudah asersi dan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: Total Registered SKU `RFID-ASSET-CORE-R5`, `NFC-CARD-BETA-N2`, `BLE-BEACON-ALPHA-B1`, dan `GPS-TRACK-CORE-G3` (lewat kemampuan baca BE)
2. Ketik Search `GPS-TRACK-CORE-G3`, tekan Enter
3. Klik (⋯) baris SKU `GPS-TRACK-CORE-G3`, klik `Add Stock`

### TC-AC-ACTS-265: Submit GPS gagal (5xx)

4. Tambahkan dua IMEI baru lewat Manual Entry untuk membentuk Preview dua baris OK
5. Intercept request Submit dengan respons 5xx
6. Klik `[Submit]`
7. Verifikasi toast error `Error, failed to register TAGs.`
8. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
9. Verifikasi Preview tetap berisi 2 baris OK
10. Verifikasi `[Submit]` aktif lagi
11. Lepas intercept
12. Klik Breadcrumb `Stock`
13. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
14. Klik `[Leave]`
15. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
16. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-173: Submit RFID gagal (5xx)

17. Klik `[Add by Scan]`
18. Scan TAG A
19. Scan TAG B
20. Klik `[Stop]`
21. Intercept request Submit dengan respons 5xx
22. Klik `[Submit]`
23. Verifikasi toast error `Error, failed to register TAGs.`
24. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
25. Verifikasi list tetap berisi 2 baris
26. Verifikasi `[Submit]` aktif lagi
27. Lepas intercept
28. Tunggu toast lama hilang otomatis

### TC-AC-ACTS-811: Submit RFID tanpa respons (timeout)

29. Tahan respons request Submit dengan intercept sampai timeout (tanpa respons)
30. Klik `[Submit]`
31. Verifikasi toast `Connection problem. Please try again.`
32. Verifikasi toast `Error, failed to register TAGs.` tidak tampil
33. Verifikasi halaman tetap di Add Stock
34. Verifikasi list tetap berisi 2 baris
35. Verifikasi `[Submit]` aktif lagi
36. Lepas intercept
37. Klik Breadcrumb `Stock`
38. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
39. Klik `[Leave]`
40. Ganti isi kotak search dengan `NFC-CARD-BETA-N2`, tekan Enter
41. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-206: Submit NFC gagal (5xx)

42. Klik `[Add by Scan]`
43. Scan TAG A
44. Scan TAG B
45. Klik `[Stop]`
46. Intercept request Submit dengan respons 5xx
47. Klik `[Submit]`
48. Verifikasi toast error `Error, failed to register TAGs.`
49. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
50. Verifikasi list tetap berisi 2 baris
51. Verifikasi `[Submit]` aktif lagi
52. Lepas intercept
53. Klik Breadcrumb `Stock`
54. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
55. Klik `[Leave]`
56. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
57. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-235: Submit BLE gagal (5xx)

58. Klik `[Add by Scan]`
59. Scan TAG A
60. Scan TAG B
61. Klik `[Stop]`
62. Intercept request Submit dengan respons 5xx
63. Klik `[Submit]`
64. Verifikasi toast error `Error, failed to register TAGs.`
65. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
66. Verifikasi list tetap berisi 2 baris
67. Verifikasi `[Submit]` aktif lagi
68. Lepas intercept
69. Klik Breadcrumb `Stock`
70. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
71. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pencatatan baseline, pemicu intercept dan pelepasannya, menunggu toast error TC-AC-ACTS-173 hilang agar toast identik tidak tertukar pada TC-AC-ACTS-811 (R-12), pembentukan list atau Preview precondition (scan lalu `[Stop]`, Manual Entry), dan perpindahan antar SKU lewat Breadcrumb `Stock` dengan Search dan row action `Add Stock` (precondition TC). Intercept dilepas segera sesudah asersi (S-09) dan di hook `after` bila spec gagal di tengah.
- Urutan TC dalam spec: 265 (GPS, tanpa hardware), 173, 811 (RFID), 206 (NFC), 235 (BLE) (P-9).
- Kegagalan dipicu lewat `Spectra.intercept()` di atas backend nyata (5xx dan penahanan respons sampai timeout), sehingga `Mode: FE+BE`.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (fault injection pada Submit) dengan pola identik per TAG Type; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-173 dan lainnya menyebut "Intercept ... respons 5xx" tanpa kode status spesifik; spec memakai respons 5xx apa pun.
  - TC-AC-ACTS-265 tidak menjelaskan cara membentuk Preview dua baris OK; spec memakai Manual Entry dengan dua IMEI baru milik fixture.
  - TC-AC-ACTS-811 tidak menyebut durasi timeout; mekanisme penahanan sampai timeout disediakan tim FE.
- `P-9` (simulator scan sebagai pembentuk state): TC-AC-ACTS-173 dan TC-AC-ACTS-811 (RFID), TC-AC-ACTS-206 (NFC), dan TC-AC-ACTS-235 (BLE) memakai simulator pemindai hanya untuk membentuk list Scanned TAG sebelum Submit; objek uji adalah kegagalan Submit (5xx dan penahanan respons sampai timeout), bukan perangkat scan. Blok GPS (TC-AC-ACTS-265) tidak membutuhkan hardware dan diletakkan lebih dulu; blok yang membutuhkan simulator berada sesudahnya, dan state antar blok dipulihkan lewat `[Leave]` pada dialog Unsaved Changes lalu Search dan row action `Add Stock`.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
