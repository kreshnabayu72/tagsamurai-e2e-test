---
id: TC-AC-DN-E2E-139-changelog-filter-sinkron-dua-arah
title: "Modal Changelog Filter: Sinkron Dua Arah Chip dan Checkbox (Action, Field, Modified By)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-638
coverage:
  web: automated
---

# Modal Changelog Filter: Sinkron Dua Arah Chip dan Checkbox (Action, Field, Modified By)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal, rujukan `Fixture.settings-device-name.akunTotalControl`; fixture belum ada, disediakan tim FE), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data Pre-setup (dibaca saja, tidak diubah): #16 Device Name inti; #19 Riwayat Changelog Uji (11 entri, tabel di bawah, pelaku `Budi S` = Budi Santoso dan `Maya P` = Maya Putri, nama lengkap pelaku seed #2 `Maya Putri`); #20 General Settings entitas uji (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).

  | No | Date | Action | Device Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|---|
  | 1 | 01/09/26 08:30 | Create | Cable Tester | Device Name | — | Cable Tester | Budi S |
  | 2 | 02/09/26 09:10 | Create | NFC Tag | Device Name | — | NFC Tag | Budi S |
  | 3 | 03/09/26 10:00 | Create | Retired Gateway | Device Name | — | Retired Gateway | Maya P |
  | 4 | 05/09/26 13:15 | Edit | Gate Antenna | Device Name | Gate Antena | Gate Antenna | Maya P |
  | 5 | 06/09/26 09:30 | Edit | Cable Tester | Category | TAG > NFC > Tag | TAG > NFC > Accessory | Budi S |
  | 6 | 07/09/26 14:05 | Edit | NFC Tag | Category | TAG > NFC > Accessory | TAG > NFC > Tag | Maya P |
  | 7 | 08/09/26 15:40 | Edit | NFC Tag | Measurement | Box | Unit | Maya P |
  | 8 | 09/09/26 08:00 | Edit | Cable Tester | Measurement | Unit | Meter | Budi S |
  | 9 | 10/09/26 12:25 | Edit | Cable Tester | Measurement | Meter | Unit | Budi S |
  | 10 | 12/09/26 17:45 | Delete | Retired Gateway | Device Name | Retired Gateway | — | Budi S |
  | 11 | 15/09/26 10:10 | Create | Tag Reel | Device Name | — | Tag Reel | Maya P |

- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup

### TC-AC-DN-638: Sinkron dua arah chip dan checkbox pada field Action

3. Klik field `Action`, centang `Create` dan `Edit`, lalu tutup dropdown
4. Klik ikon `(✕)` pada chip `Create` tanpa membuka dropdown
5. Verifikasi chip `Create` hilang
6. Verifikasi chip `Edit` tetap ada
7. Klik field `Action`
8. Verifikasi checkbox `Create` tidak tercentang
9. Hilangkan centang `Edit` dari dalam dropdown yang terbuka
10. Verifikasi chip `Edit` hilang
11. Tutup dropdown

### TC-AC-DN-638: Sinkron dua arah chip dan checkbox pada field Field

12. Klik field `Field`, centang `Device Name` dan `Measurement`, lalu tutup dropdown
13. Klik ikon `(✕)` pada chip `Device Name` tanpa membuka dropdown
14. Verifikasi chip `Device Name` hilang
15. Verifikasi chip `Measurement` tetap ada
16. Klik field `Field`
17. Verifikasi checkbox `Device Name` tidak tercentang
18. Hilangkan centang `Measurement` dari dalam dropdown yang terbuka
19. Verifikasi chip `Measurement` hilang
20. Tutup dropdown

### TC-AC-DN-638: Sinkron dua arah chip dan checkbox pada field Modified By

21. Klik field `Modified By`, centang `Budi Santoso` dan `Maya Putri`, lalu tutup dropdown
22. Klik ikon `(✕)` pada chip `Budi Santoso` tanpa membuka dropdown
23. Verifikasi chip `Budi Santoso` hilang
24. Verifikasi chip `Maya Putri` tetap ada
25. Klik field `Modified By`
26. Verifikasi checkbox `Budi Santoso` tidak tercentang
27. Hilangkan centang `Maya Putri` dari dalam dropdown yang terbuka
28. Verifikasi chip `Maya Putri` hilang
29. Tutup dropdown

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Blok tiga field (Action, Field, Modified By) memakai pola langkah yang sama; opsi `Budi Santoso` dan `Maya Putri` pada Modified By adalah nama lengkap pelaku seed #19. Tabel tidak diasersi pada spec ini.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
