---
id: TC-AC-DN-E2E-143-changelog-setup-column-ceklis-urutan
title: "Modal Changelog Setup Column: Ceklis Old/New Value/Modified By dan Geser Urutan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-461
  - TC-AC-DN-462
coverage:
  web: automated
---

# Modal Changelog Setup Column: Ceklis Old/New Value/Modified By dan Geser Urutan

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
- State global yang diubah: konfigurasi kolom Changelog (dan kolom List bila disebut) tersimpan per user di browser. Hook `after` spec ini menghapus preferensi kolom di browser (bagian 4), bukan `[Reset to Default]`; kemampuan itu disediakan tim FE.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon `⋯` pada header kolom terakhir
3. Klik item `Setup Column...` di bagian bawah overlay

### TC-AC-DN-461: Ceklis dan unceklis kolom Old Value, New Value, dan Modified By

4. Hilangkan centang kolom Old Value
5. Hilangkan centang kolom New Value
6. Hilangkan centang kolom Modified By
7. Klik `[Save]`
8. Verifikasi kolom Old Value hilang dari tabel setelah Save
9. Verifikasi kolom New Value hilang dari tabel setelah Save
10. Verifikasi kolom Modified By hilang dari tabel setelah Save
11. Muat ulang halaman dengan F5
12. Klik ikon Changelog di toolbar List
13. Verifikasi kolom Date, Action, Device Name, dan Field tampil setelah F5
14. Verifikasi kolom Old Value tetap hilang setelah F5
15. Verifikasi kolom New Value tetap hilang setelah F5
16. Verifikasi kolom Modified By tetap hilang setelah F5

### TC-AC-DN-462: Geser urutan kolom

17. Klik ikon `⋯` pada header kolom terakhir
18. Klik item `Setup Column...` di bagian bawah overlay
19. Centang kolom Old Value, New Value, dan Modified By
20. Seret kolom Modified By ke posisi paling atas daftar
21. Seret kolom Date ke posisi paling bawah daftar
22. Verifikasi urutan header kolom pada preview: Modified By, Action, Device Name, Field, Old Value, New Value, Date
23. Klik `[Save]`
24. Verifikasi urutan header kolom pada tabel setelah Save: Modified By, Action, Device Name, Field, Old Value, New Value, Date
25. Muat ulang halaman dengan F5
26. Klik ikon Changelog di toolbar List
27. Verifikasi urutan header kolom yang sama bertahan setelah F5
28. Verifikasi tujuh kolom dapat dipindahkan tanpa kolom yang terkunci posisinya

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 13 memverifikasi kolom Date, Action, Device Name, dan Field masih tampil setelah F5 sebagai anchor positif sebelum asersi kolom Old Value, New Value, dan Modified By tetap hilang (langkah 14 sampai 16). Spec tidak membatasi tampilan dengan Filter Date dan tidak mengasersi jumlah entri.
- Pemulihan konfigurasi kolom dilakukan hook `after` dengan menghapus preferensi kolom di browser (bagian 4); `[Reset to Default]` hanya dipakai bila TC mengujinya.
- Langkah mencentang kembali Old Value, New Value, dan Modified By di awal TC-AC-DN-462 memulihkan hasil TC-AC-DN-461 (S-09) dan merupakan langkah penghubung (S-03); langkah itu dilakukan di popup Setup Column yang sama dengan penyeretan kolom.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
