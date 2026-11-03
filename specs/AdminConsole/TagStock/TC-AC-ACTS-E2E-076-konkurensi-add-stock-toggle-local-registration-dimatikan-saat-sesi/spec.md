---
id: TC-AC-ACTS-E2E-076-konkurensi-add-stock-toggle-local-registration-dimatikan-saat-sesi
title: "Konkurensi Add Stock: Toggle Local Registration Dimatikan saat Sesi RFID, NFC, BLE, dan GPS"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-175
  - TC-AC-ACTS-208
  - TC-AC-ACTS-237
  - TC-AC-ACTS-267
coverage:
  web: automated
---

# Konkurensi Add Stock: Toggle Local Registration Dimatikan saat Sesi RFID, NFC, BLE, dan GPS

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
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

- TAG uji NFC (TC-AC-ACTS-208) (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | UID |
|---|---|
| TAG A | `Fixture.tagStock.nfcA.uid` (`A1B2C3D4E5F7`) |
| TAG B | `Fixture.tagStock.nfcB.uid` |

- TAG uji BLE (TC-AC-ACTS-237) (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |
| TAG B | `Fixture.tagStock.bleB.mac` |

- IMEI uji GPS (Preview Manual Entry): `Fixture.tagStock.imeiA` dan `Fixture.tagStock.imeiB` (Data Uji Dinamis #2, `356938035643809` s/d `356938035643817`), belum terdaftar kecuali disebut lain.
- Principal pengubah toggle Local Registration Distributor: tidak ada di Pre-setup TC, disediakan tim FE; dipakai lewat sesi API aktor.
- State global: toggle Local Registration Distributor (diubah OFF lewat sesi API Principal pada tiap blok, dipulihkan ON sesudah tiap blok dan di hook `after`). Suite berjalan serial.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: Total Registered SKU `RFID-ASSET-CORE-R5`, `NFC-CARD-BETA-N2`, `BLE-BEACON-ALPHA-B1`, dan `GPS-TRACK-CORE-G3` (lewat kemampuan baca BE)
2. Ketik Search `GPS-TRACK-CORE-G3`, tekan Enter
3. Klik (⋯) baris SKU `GPS-TRACK-CORE-G3`, klik `Add Stock`

### TC-AC-ACTS-267: Toggle Local Registration dimatikan saat sesi GPS

4. Tambahkan dua IMEI baru lewat Manual Entry untuk membentuk Preview dua baris OK
5. Matikan toggle Local Registration Distributor lewat sesi API Principal hingga toggle OFF tersimpan
6. Tunggu aksi selesai
7. Klik `[Submit]`
8. Verifikasi toast error `Error, failed to register TAGs.`
9. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
10. Nyalakan kembali toggle Local Registration Distributor lewat sesi API Principal hingga toggle ON tersimpan
11. Klik Breadcrumb `Stock`
12. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Leave]`
14. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
15. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-175: Toggle Local Registration dimatikan saat sesi RFID

16. Klik `[Add by Scan]`
17. Scan TAG A
18. Scan TAG B
19. Klik `[Stop]`
20. Matikan toggle Local Registration Distributor lewat sesi API Principal hingga toggle OFF tersimpan
21. Tunggu aksi selesai
22. Klik `[Submit]`
23. Verifikasi toast error `Error, failed to register TAGs.`
24. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
25. Nyalakan kembali toggle Local Registration Distributor lewat sesi API Principal hingga toggle ON tersimpan
26. Klik Breadcrumb `Stock`
27. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Leave]`
29. Ganti isi kotak search dengan `NFC-CARD-BETA-N2`, tekan Enter
30. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-208: Toggle Local Registration dimatikan saat sesi NFC

31. Klik `[Add by Scan]`
32. Scan TAG A
33. Scan TAG B
34. Klik `[Stop]`
35. Matikan toggle Local Registration Distributor lewat sesi API Principal hingga toggle OFF tersimpan
36. Tunggu aksi selesai
37. Klik `[Submit]`
38. Verifikasi toast error `Error, failed to register TAGs.`
39. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
40. Nyalakan kembali toggle Local Registration Distributor lewat sesi API Principal hingga toggle ON tersimpan
41. Klik Breadcrumb `Stock`
42. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
43. Klik `[Leave]`
44. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
45. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-237: Toggle Local Registration dimatikan saat sesi BLE

46. Klik `[Add by Scan]`
47. Scan TAG A
48. Scan TAG B
49. Klik `[Stop]`
50. Matikan toggle Local Registration Distributor lewat sesi API Principal hingga toggle OFF tersimpan
51. Tunggu aksi selesai
52. Klik `[Submit]`
53. Verifikasi toast error `Error, failed to register TAGs.`
54. Verifikasi tidak ada unit tersimpan (Total Registered SKU sama dengan baseline)
55. Nyalakan kembali toggle Local Registration Distributor lewat sesi API Principal hingga toggle ON tersimpan
56. Klik Breadcrumb `Stock`
57. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
58. Klik `[Leave]`

## Notes

- Pelaku kedua (Principal pengubah toggle Local Registration) memakai sesi API aktor yang disediakan tim FE/BE; bukan konteks kedua, sehingga P-2 tidak dipakai. Akun Principal tidak ada di Pre-setup TC dan ditulis "disediakan tim FE".
- Toggle Local Registration Distributor adalah state global bersama; dipulihkan ke ON sesudah tiap blok dan di hook `after` (R-08). Suite berjalan serial.
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pencatatan baseline, pembentukan list atau Preview precondition (scan lalu `[Stop]`, Manual Entry), pemulihan toggle, dan perpindahan antar SKU lewat Breadcrumb `Stock` dengan Search dan row action `Add Stock` (precondition TC).
- TC-AC-ACTS-178, TC-AC-ACTS-715, dan TC-AC-ACTS-727 (dua sesi dan hasil commit berbeda dari badge) ada di spec 078.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (toggle Local Registration diubah pelaku kedua lewat sesi API) dengan pola identik per TAG Type; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-175, 208, 237, dan 267 tidak menyebut cara Principal mematikan toggle; mekanisme disediakan tim FE/BE.
  - TC-AC-ACTS-175, 208, 237, dan 267 Expected "tidak ada unit tersimpan" tidak memberi langkah observasi; spec memakai Total Registered terhadap baseline lewat kemampuan baca BE.
  - TC-AC-ACTS-267 tidak menjelaskan cara membentuk Preview dua baris OK; spec memakai Manual Entry dengan dua IMEI baru milik fixture.
- `P-9` (simulator scan sebagai pembentuk state): TC-AC-ACTS-175 (RFID), TC-AC-ACTS-208 (NFC), dan TC-AC-ACTS-237 (BLE) memakai simulator pemindai hanya untuk membentuk list Scanned TAG sebelum Submit; objek uji adalah toggle Local Registration yang dimatikan saat sesi, bukan perangkat scan. Blok GPS (TC-AC-ACTS-267) tidak membutuhkan hardware dan diletakkan lebih dulu; blok yang membutuhkan simulator berada sesudahnya, dan state antar blok dipulihkan lewat `[Leave]` pada dialog Unsaved Changes lalu Search dan row action `Add Stock`.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
