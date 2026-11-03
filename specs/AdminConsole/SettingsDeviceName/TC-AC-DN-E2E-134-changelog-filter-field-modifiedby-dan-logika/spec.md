---
id: TC-AC-DN-E2E-134-changelog-filter-field-modifiedby-dan-logika
title: "Modal Changelog Filter: Field, Modified By, dan Logika OR/AND"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-428
  - TC-AC-DN-429
  - TC-AC-DN-430
  - TC-AC-DN-431
  - TC-AC-DN-432
coverage:
  web: automated
---

# Modal Changelog Filter: Field, Modified By, dan Logika OR/AND

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

- Isolasi riwayat seed: Filter Date `01/09/26` sampai `15/09/26` dipasang sekali di awal sebagai pembatas dan tetap aktif sepanjang spec (S-12, S-14); jumlah total seluruh entri tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup
3. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir

### TC-AC-DN-428: Filter Field

4. Klik field `Field`, centang `Category`
5. Klik `[Apply]`
6. Verifikasi tabel menampilkan 2 baris Field `Category` (Edit `NFC Tag` 07/09/26 14:05 dan Edit `Cable Tester` 06/09/26 09:30)

### TC-AC-DN-429: Filter Modified By

7. Klik ikon `(X)` pada chip `Category`
8. Klik field `Modified By`, centang pelaku Maya Putri
9. Klik `[Apply]`
10. Verifikasi tabel menampilkan 5 baris dengan Modified By `Maya P`

### TC-AC-DN-430: Multi-select dalam satu field memakai logika OR

11. Klik ikon `(X)` pada chip pelaku Maya Putri
12. Klik field `Device Name`, centang `Cable Tester` dan `Tag Reel`
13. Klik `[Apply]`
14. Verifikasi tabel menampilkan 5 baris: 4 baris `Cable Tester` dan 1 baris `Tag Reel`

### TC-AC-DN-431: Dua field berbeda memakai logika AND

15. Klik ikon `(X)` pada chip `Cable Tester` dan chip `Tag Reel`
16. Klik field `Action`, centang `Edit`
17. Klik field `Modified By`, centang pelaku Budi Santoso
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan 3 baris Edit `Cable Tester` (06/09/26 09:30, 09/09/26 08:00, dan 10/09/26 12:25) milik `Budi S`

### TC-AC-DN-432: OR dalam satu field berbeda dari AND antar field

20. Klik ikon `(X)` pada chip `Edit` dan chip pelaku Budi Santoso
21. Klik field `Action`, centang `Create` dan `Delete`
22. Klik field `Modified By`, centang pelaku Maya Putri
23. Klik `[Apply]`
24. Verifikasi tabel menampilkan 2 baris Create milik `Maya P` (`Retired Gateway` dan `Tag Reel`)
25. Verifikasi tidak ada baris Delete karena pelaku Delete adalah `Budi S`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah memasang Filter Date `01/09/26` sampai `15/09/26` dan langkah klik `(X)` pada chip adalah langkah penghubung (S-03): pembatas membatasi tampilan pada 11 entri seed; chip dihapus agar tiap TC mulai dari satu kriteria field.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
