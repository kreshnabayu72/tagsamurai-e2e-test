---
id: TC-AC-DN-E2E-142-changelog-setup-column-screening-dan-ceklis
title: "Modal Changelog Setup Column: Screening Overlay/Popup dan Ceklis Kolom Date, Action, Device Name, Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-458
  - TC-AC-DN-459
  - TC-AC-DN-460
coverage:
  web: automated
---

# Modal Changelog Setup Column: Screening Overlay/Popup dan Ceklis Kolom Date, Action, Device Name, Field

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

### TC-AC-DN-458: Screening overlay Column Visibility

2. Klik ikon `⋯` pada header kolom terakhir
3. Verifikasi overlay muncul tanpa backdrop dan menempel pada header kolom `⋯`
4. Verifikasi daftar tujuh kolom berurutan: Date, Action, Device Name, Field, Old Value, New Value, Modified By
5. Verifikasi setiap kolom memiliki checkbox tercentang dan aktif (Hideable)
6. Verifikasi setiap kolom memiliki drag handle
7. Verifikasi footer overlay memuat item `Setup Column...` di bagian bawah

### TC-AC-DN-459: Screening popup Setup Column

8. Klik item `Setup Column...` di bagian bawah overlay
9. Verifikasi title popup `Setup Column`
10. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi tombol close `(X)` di kanan atas
12. Verifikasi daftar tujuh kolom berurutan: Date, Action, Device Name, Field, Old Value, New Value, Modified By
13. Verifikasi setiap kolom memiliki checkbox tercentang
14. Verifikasi setiap kolom memiliki drag handle
15. Verifikasi setiap kolom memiliki ikon Pin
16. Verifikasi Live Preview tabel menampilkan urutan header kolom yang sama
17. Verifikasi footer: tombol `[Reset to Default]` dan `[Save]` rata kanan
18. Verifikasi tidak ada tombol `[Cancel]`

### TC-AC-DN-460: Ceklis dan unceklis kolom Date, Action, Device Name, dan Field

19. Hilangkan centang kolom Date
20. Hilangkan centang kolom Action
21. Hilangkan centang kolom Device Name
22. Hilangkan centang kolom Field
23. Klik `[Save]`
24. Verifikasi kolom Date hilang dari tabel setelah Save
25. Verifikasi kolom Action hilang dari tabel setelah Save
26. Verifikasi kolom Device Name hilang dari tabel setelah Save
27. Verifikasi kolom Field hilang dari tabel setelah Save
28. Muat ulang halaman dengan F5
29. Klik ikon Changelog di toolbar List
30. Verifikasi kolom Old Value, New Value, dan Modified By tampil setelah F5
31. Verifikasi kolom Date tetap hilang setelah F5
32. Verifikasi kolom Action tetap hilang setelah F5
33. Verifikasi kolom Device Name tetap hilang setelah F5
34. Verifikasi kolom Field tetap hilang setelah F5
35. Klik ikon `⋯` pada header kolom terakhir
36. Klik item `Setup Column...` di bagian bawah overlay
37. Centang kolom Date, lalu klik `[Save]`
38. Verifikasi kolom Date tampil kembali setelah dicentang dan Save

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 30 memverifikasi kolom Old Value, New Value, dan Modified By masih tampil setelah F5 sebagai anchor positif sebelum asersi kolom Date, Action, Device Name, dan Field tetap hilang (langkah 31 sampai 34). Spec tidak membatasi tampilan dengan Filter Date dan tidak mengasersi jumlah entri.
- Pemulihan konfigurasi kolom dilakukan hook `after` dengan menghapus preferensi kolom di browser (bagian 4); `[Reset to Default]` hanya dipakai bila TC mengujinya.
- Ukuran spec (38 langkah, di atas smell 35 langkah): satu topik (Setup Column modal Changelog), satu kelas harness; tiap blok TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
