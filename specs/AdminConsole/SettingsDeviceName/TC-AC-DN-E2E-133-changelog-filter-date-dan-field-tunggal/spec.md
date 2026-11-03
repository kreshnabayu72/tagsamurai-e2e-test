---
id: TC-AC-DN-E2E-133-changelog-filter-date-dan-field-tunggal
title: "Modal Changelog Filter: Date Inklusif, Satu Hari, Format Tanggal, Action, dan Device Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-423
  - TC-AC-DN-424
  - TC-AC-DN-425
  - TC-AC-DN-426
  - TC-AC-DN-427
coverage:
  web: automated
---

# Modal Changelog Filter: Date Inklusif, Satu Hari, Format Tanggal, Action, dan Device Name

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

- Isolasi riwayat seed: TC-AC-DN-423 dan TC-AC-DN-424 dibatasi oleh rentang Date itu sendiri; TC-AC-DN-426 dan TC-AC-DN-427 memakai Filter Date `01/09/26` sampai `15/09/26` sebagai pembatas karena audit trail tumbuh (S-12, S-14).
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup

### TC-AC-DN-425 dan TC-AC-DN-423: Format teks tanggal dan rentang inklusif

3. Klik field `Date`
4. Pilih 05/09/26 sebagai tanggal awal dan 09/09/26 sebagai tanggal akhir
5. Verifikasi teks field Date memuat tanggal awal `05/09/26` dan tanggal akhir `09/09/26` dalam format `dd/MM/yy`
6. Klik `[Apply]`
7. Verifikasi tabel menampilkan 5 baris: Edit `Gate Antenna` 05/09/26 13:15, Edit `Cable Tester` Field `Category` 06/09/26 09:30, Edit `NFC Tag` Field `Category` 07/09/26 14:05, Edit `NFC Tag` Field `Measurement` 08/09/26 15:40, Edit `Cable Tester` Field `Measurement` 09/09/26 08:00
8. Verifikasi tanggal awal (baris 05/09/26 13:15) dan tanggal akhir (baris 09/09/26 08:00) ikut termasuk dalam hasil

### TC-AC-DN-424: Filter Date satu hari

9. Klik field `Date`
10. Pilih 12/09/26 sebagai tanggal awal dan tanggal akhir
11. Klik `[Apply]`
12. Verifikasi tabel menampilkan 1 baris Delete `Retired Gateway` 12/09/26 17:45 untuk Field `Device Name`

### TC-AC-DN-426: Filter Action tunggal

13. Klik field `Date`
14. Pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
15. Klik field `Action`, centang `Delete`
16. Klik `[Apply]`
17. Verifikasi tabel menampilkan 1 baris Action `Delete` (`Retired Gateway`, Field `Device Name`)

### TC-AC-DN-427: Filter Device Name

18. Klik ikon `(X)` pada chip `Delete`
19. Klik field `Device Name`, centang `Cable Tester`
20. Klik `[Apply]`
21. Verifikasi tabel menampilkan 4 baris dengan Device Name `Cable Tester`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Rentang Date `01/09/26` sampai `15/09/26` pada TC-AC-DN-426 dan TC-AC-DN-427 adalah pembatas riwayat seed (S-14): audit trail tumbuh sehingga Action `Delete` dan Device Name hanya bermakna dalam rentang seed. Langkah klik `(X)` pada chip `Delete` adalah langkah penghubung (S-03).
- Langkah memilih rentang 05/09/26 sampai 09/09/26 dipakai bersama TC-AC-DN-425 dan TC-AC-DN-423 karena aksinya identik (Filter Panel yang sama dipakai berulang); Verifikasi teks tanggal milik TC-AC-DN-425 ditaruh sebelum `[Apply]`.
- Temuan untuk QA:
  - TC-AC-DN-423 sampai TC-AC-DN-427 menyebut 'pelaku' dan Date tanpa pembatas; audit trail tumbuh sehingga rentang Date menjadi pembatas.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
