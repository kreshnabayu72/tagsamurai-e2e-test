---
id: TC-AC-DN-E2E-130-changelog-search-bagian-2
title: "Modal Changelog Search: Old/New Value, Modified By, Huruf Besar-Kecil, dan Trim"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-411
  - TC-AC-DN-412
  - TC-AC-DN-413
  - TC-AC-DN-414
  - TC-AC-DN-415
coverage:
  web: automated
---

# Modal Changelog Search: Old/New Value, Modified By, Huruf Besar-Kecil, dan Trim

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

- Isolasi riwayat seed (S-12, S-14): Changelog adalah audit trail permanen yang tumbuh karena spec lain menulis entri bertanggal waktu nyata (lebih baru dari 15/09/26). Asersi isi, jumlah, dan urutan atas riwayat seed dibatasi dengan Filter Date `01/09/26` sampai `15/09/26` sehingga hanya 11 entri seed yang terlihat; jumlah total seluruh entri tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup
3. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
4. Klik `[Apply]`
5. Klik ikon Filter untuk menutup Filter Panel

### TC-AC-DN-411: Search kolom Old Value dan New Value

6. Klik ikon Search, ketik Search `Meter`, tekan Enter
7. Verifikasi kolom Old Value: baris Edit `Cable Tester` 10/09/26 12:25 (Old Value `Meter`) tampil
8. Verifikasi kolom New Value: baris Edit `Cable Tester` 09/09/26 08:00 (New Value `Meter`) tampil
9. Verifikasi total hasil 2 baris

### TC-AC-DN-412: Search kolom Old Value

10. Ganti isi kotak search dengan `Gate Antena`, tekan Enter
11. Verifikasi tabel menampilkan 1 baris Edit `Gate Antenna` dengan Old Value `Gate Antena`

### TC-AC-DN-413: Search kolom Modified By

12. Ganti isi kotak search dengan `maya`, tekan Enter
13. Verifikasi tabel menampilkan 5 baris dengan Modified By `Maya P` pada halaman 1
14. Verifikasi tidak ada baris Modified By `Budi S` pada hasil

### TC-AC-DN-414: Tidak membedakan huruf besar kecil dan mencocokkan sebagian kata

15. Ganti isi kotak search dengan `CABLE`, tekan Enter
16. Verifikasi kata kunci `CABLE` menampilkan 4 baris `Cable Tester`
17. Ganti isi kotak search dengan `ester`, tekan Enter
18. Verifikasi kata kunci `ester` menampilkan 4 baris `Cable Tester`

### TC-AC-DN-415: Search memangkas spasi di awal dan akhir

19. Ganti isi kotak search dengan `  tester  ` (spasi di awal dan akhir), tekan Enter
20. Verifikasi tabel menampilkan 4 baris `Cable Tester`, sama dengan kata kunci `tester`
21. Verifikasi isi kolom pencarian di layar tetap `  tester  `
22. Klik ikon panah `(←)` di kiri toolbar

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
