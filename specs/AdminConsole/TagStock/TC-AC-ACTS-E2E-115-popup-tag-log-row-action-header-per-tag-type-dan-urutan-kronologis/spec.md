---
id: TC-AC-ACTS-E2E-115-popup-tag-log-row-action-header-per-tag-type-dan-urutan-kronologis
title: "Popup TAG Log: Row Action di Tab Available dan In Use, Header Per TAG Type, dan Urutan Kronologis dengan Judul Kalimat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-952
  - TC-AC-ACTS-953
  - TC-AC-ACTS-954
  - TC-AC-ACTS-955
coverage:
  web: automated
---

# Popup TAG Log: Row Action di Tab Available dan In Use, Header Per TAG Type, dan Urutan Kronologis dengan Judul Kalimat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: Detail SKU `RFID-ASSET-CORE-R5` > Tab Available (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data milik spec disiapkan seeding fixture BE (disediakan tim FE/BE): SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12) dengan unit Available `TAG-4F7K2XQ9` (EPC `E280...01`, UID `A1B2C3D4E5F6`; Data Dinamis #5), unit In Use, dan satu unit dengan sedikitnya tiga entri TAG Log pada waktu berbeda yang pelakunya mencakup user (mis. `Budi Santoso`, Data Dinamis #3) dan `System`; SKU `NFC-CARD-BETA-N2` (#13), `BLE-BEACON-ALPHA-B1` (#14), dan `GPS-TRACK-CORE-G3` (#15) masing-masing dengan satu unit Available. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Spec ini hanya membaca data; tidak ada perubahan state.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-952: Row action TAG Log tampil di Tab Available dan Tab In Use dan membuka Popup TAG Log

1. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
2. Klik (⋯) pada baris Available
3. Verifikasi menu memuat `TAG Log` (icon FileHistoryLine, dark) dan `Delete`
4. Klik `TAG Log`
5. Verifikasi klik `TAG Log` membuka Popup TAG Log unit pada baris itu
6. Tutup popup lewat (X)
7. Buka Tab In Use, klik (⋯) pada baris In Use
8. Verifikasi menu hanya memuat `TAG Log`
9. Klik `TAG Log`
10. Verifikasi klik `TAG Log` membuka Popup TAG Log unit pada baris itu
11. Tutup popup lewat (X)

### TC-AC-ACTS-953: Header Popup TAG Log RFID memuat TAG Code, Status, TAG Type, Identifier, dan atribut katalog

12. Buka Tab Available, klik (⋯) > `TAG Log` pada baris unit `TAG-4F7K2XQ9`
13. Verifikasi judul `TAG Log`
14. Verifikasi grid label:value memuat TAG Code `TAG-4F7K2XQ9`, TAG Type `RFID – Object TAG`, Identifier `E280...01 / A1B2C3D4E5F6`, Device Name, SKU, Brand, dan Model/Type
15. Verifikasi badge Status `Available`
16. Tutup popup lewat (X)

### TC-AC-ACTS-954: Header Popup TAG Log untuk NFC, BLE, dan GPS memakai identifier masing-masing

17. Buka Detail SKU `NFC-CARD-BETA-N2` > Tab Available, klik (⋯) > `TAG Log` pada unit NFC
18. Verifikasi TAG Type `NFC` dan Identifier berupa UID
19. Tutup popup lewat (X)
20. Buka Detail SKU `BLE-BEACON-ALPHA-B1` > Tab Available, klik (⋯) > `TAG Log` pada unit BLE
21. Verifikasi TAG Type `BLE` dan Identifier berupa MAC Address
22. Tutup popup lewat (X)
23. Buka Detail SKU `GPS-TRACK-CORE-G3` > Tab Available, klik (⋯) > `TAG Log` pada unit GPS
24. Verifikasi TAG Type `GPS` dan Identifier berupa IMEI
25. Tutup popup lewat (X)

### TC-AC-ACTS-955: Daftar log berurutan kronologis terbaru di atas dengan judul kalimat, Date & Time, dan Description

26. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) > `TAG Log` pada unit dengan tiga entri
27. Verifikasi entri terbaru berada paling atas
28. Verifikasi tiap entri memuat judul kalimat (mis. `TAG Registered by 👤 Budi S`) dan Date & Time pada satu baris serta Description (bila ada)
29. Hover nama pelaku user pada satu entri
30. Verifikasi pelaku tampil sebagai ikon user dan `[First Name] [Last Initial]` dengan tooltip nama lengkap saat hover
31. Verifikasi pelaku `System` tampil tanpa ikon dan tanpa tooltip
32. Verifikasi tidak ada badge Event maupun baris PIC terpisah
33. Verifikasi tidak ada toolbar, Search, Filter, paginasi, maupun footer
34. Tutup popup lewat (X)

## Notes

- Mode: FE+BE.
- Langkah penghubung tanpa Verifikasi (S-03): menutup popup lewat (X) sebelum TC berikutnya (S-09) dan membuka Detail SKU tiap TAG Type.
- Pelaku `System` pada TC-AC-ACTS-955 dibuktikan lewat entri yang diseeding dengan pelaku System (precondition; S-11).
- Temuan untuk QA:
  - TC-AC-ACTS-954 menyebut "Unit NFC, BLE, dan GPS Available ada di SKU masing-masing" tanpa data; spec memakai Pre-setup #13 sampai #15.
  - TC-AC-ACTS-955 menyebut "unit dengan minimal tiga entri pada waktu berbeda" tanpa data; disediakan seeding.
