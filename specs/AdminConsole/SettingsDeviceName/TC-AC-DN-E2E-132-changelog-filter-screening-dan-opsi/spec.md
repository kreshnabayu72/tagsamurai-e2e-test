---
id: TC-AC-DN-E2E-132-changelog-filter-screening-dan-opsi
title: "Modal Changelog Filter: Screening, Isi Opsi, Device Name Terhapus, dan Indikator Pemuatan Opsi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-420
  - TC-AC-DN-421
  - TC-AC-DN-422
  - TC-AC-DN-448
coverage:
  web: automated
---

# Modal Changelog Filter: Screening, Isi Opsi, Device Name Terhapus, dan Indikator Pemuatan Opsi

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
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

- Kemampuan intercept (disediakan tim FE/BE): `Spectra.intercept()` menunda respons opsi filter Changelog pada TC-AC-DN-448 (menahan respons hanya untuk mengamati state UI, bukan kelas b); intercept dilepas segera sesudah asersi (S-09).
- Data opsi dropdown berasal dari seluruh data log Principal, termasuk entri spec lain.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List

### TC-AC-DN-420: Screening Filter Panel

2. Arahkan kursor ke ikon Filter di toolbar popup
3. Verifikasi tooltip ikon Filter `Filter`
4. Klik ikon Filter di toolbar popup
5. Verifikasi ikon Filter berubah gelap saat panel terbuka
6. Verifikasi lima field berurutan: `Date`, `Action`, `Device Name`, `Field`, `Modified By`
7. Verifikasi field `Date` bertipe date range picker dengan placeholder `Select date`
8. Verifikasi field `Action` bertipe multi-select searchable dengan placeholder `All actions`
9. Verifikasi field `Device Name` bertipe multi-select searchable dengan placeholder `All device names`
10. Verifikasi field `Field` bertipe multi-select searchable dengan placeholder `All fields`
11. Verifikasi field `Modified By` bertipe multi-select searchable dengan placeholder `All users`
12. Verifikasi field `Old Value` dan `New Value` tidak ada di Filter Panel
13. Verifikasi footer Filter Panel: tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-DN-421: Isi opsi dropdown diambil dari data log

14. Klik field `Action`
15. Verifikasi dropdown Action berisi 3 opsi: `Create`, `Edit`, `Delete`
16. Tutup dropdown, klik field `Device Name`
17. Verifikasi dropdown Device Name memuat opsi seed `Cable Tester`, `NFC Tag`, `Retired Gateway`, `Gate Antenna`, dan `Tag Reel`
18. Tutup dropdown, klik field `Field`
19. Verifikasi dropdown Field berisi 3 opsi: `Device Name`, `Measurement`, `Category`
20. Tutup dropdown, klik field `Modified By`
21. Verifikasi dropdown Modified By memuat opsi pelaku Budi Santoso dan pelaku Maya Putri

### TC-AC-DN-422: Opsi Device Name memuat nama yang sudah dihapus

22. Tutup dropdown, klik field `Device Name`
23. Verifikasi opsi `Retired Gateway` tampil karena memiliki entri log walau Device Name sudah dihapus
24. Verifikasi tidak ada opsi dengan teks tepat `Door Antenna` karena tidak memiliki entri log

### TC-AC-DN-448: Indikator pemuatan saat opsi sedang diambil

25. Tutup dropdown
26. Aktifkan intercept yang menunda respons opsi filter
27. Klik field `Device Name`
28. Verifikasi dropdown menampilkan skeleton atau spinner mini saat opsi dimuat
29. Verifikasi dropdown tidak menampilkan daftar kosong tanpa indikator
30. Lepas intercept dan tahanan respons opsi filter

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini tidak memakai pembatas Filter Date karena yang diasersi adalah panel dan opsi dropdown, bukan baris tabel.
- Temuan untuk QA:
  - TC-AC-DN-421 Expected b dan d menyebut jumlah tepat 5 opsi Device Name dan 2 opsi Modified By; audit trail tumbuh oleh spec lain, sehingga spec mengasersi bahwa opsi seed tampil (jumlah tepat tidak diasersi, S-12). Opsi Action (3) dan Field (3) tepat karena himpunannya tetap.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
