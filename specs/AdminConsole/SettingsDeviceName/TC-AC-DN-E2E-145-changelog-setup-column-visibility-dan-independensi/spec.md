---
id: TC-AC-DN-E2E-145-changelog-setup-column-visibility-dan-independensi
title: "Modal Changelog Setup Column: Kolom Terakhir, Column Visibility Tanpa Save, dan Independensi dari List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-468
  - TC-AC-DN-469
  - TC-AC-DN-470
  - TC-AC-DN-471
coverage:
  web: automated
---

# Modal Changelog Setup Column: Kolom Terakhir, Column Visibility Tanpa Save, dan Independensi dari List

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

- Konfigurasi kolom List (kolom Brand) dan Changelog tersimpan per user di browser; Brand dipulihkan dalam spec dan preferensi kolom List serta Changelog dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global yang diubah: konfigurasi kolom Changelog (dan kolom List bila disebut) tersimpan per user di browser. Hook `after` spec ini menghapus preferensi kolom di browser (bagian 4), bukan `[Reset to Default]`; kemampuan itu disediakan tim FE.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-471: Konfigurasi kolom List tidak memengaruhi kolom popup Changelog

1. Klik ikon `⋯` pada header kolom terakhir tabel List lalu hilangkan centang kolom Brand
2. Klik ikon Changelog di toolbar List
3. Verifikasi popup Changelog menampilkan tujuh kolom: Date, Action, Device Name, Field, Old Value, New Value, Modified By
4. Klik ikon close `(X)` pada popup
5. Klik ikon `⋯` pada header kolom terakhir tabel List lalu centang kembali kolom Brand

### TC-AC-DN-468: Kolom terakhir yang tersisa tidak dapat dihilangkan

6. Klik ikon Changelog di toolbar List
7. Klik ikon `⋯` pada header kolom terakhir
8. Klik item `Setup Column...` di bagian bawah overlay
9. Hilangkan centang enam kolom: Date, Action, Device Name, Field, Old Value, New Value
10. Arahkan kursor ke checkbox Modified By
11. Verifikasi checkbox Modified By tetap tampil tetapi nonaktif dan tidak dapat di-uncheck
12. Verifikasi tooltip `At least one column must remain visible.`
13. Klik ikon close `(X)` pada popup Setup Column

### TC-AC-DN-469: Perubahan di overlay Column Visibility langsung diterapkan tanpa Save

14. Klik ikon `⋯` pada header kolom terakhir
15. Hilangkan centang kolom Action
16. Verifikasi kolom Action langsung hilang dari tabel tanpa tombol Save
17. Klik ikon close `(X)` pada popup Changelog
18. Klik ikon Changelog di toolbar List
19. Verifikasi kolom Action tetap hilang saat popup dibuka kembali
20. Klik ikon `⋯` pada header kolom terakhir lalu centang kembali kolom Action

### TC-AC-DN-470: Konfigurasi kolom Changelog tidak memengaruhi kolom tabel List

21. Klik ikon `⋯` pada header kolom terakhir
22. Klik item `Setup Column...` di bagian bawah overlay
23. Hilangkan centang kolom Action, klik `[Save]`
24. Klik ikon close `(X)` pada popup Changelog
25. Verifikasi tabel List Device Name tetap menampilkan keenam kolom data: Device Name, Category, Brand, Model/Type, Measurement, Last Modified

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pemulihan konfigurasi kolom dilakukan hook `after` dengan menghapus preferensi kolom di browser (bagian 4); `[Reset to Default]` hanya dipakai bila TC mengujinya.
- Urutan: TC-AC-DN-471 lebih dulu karena memerlukan List tanpa popup dan karena TC-AC-DN-470 menyimpan konfigurasi Changelog yang menyembunyikan Action (S-10). Tidak ada asersi baris tabel sehingga pembatas Filter Date tidak dipakai.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
