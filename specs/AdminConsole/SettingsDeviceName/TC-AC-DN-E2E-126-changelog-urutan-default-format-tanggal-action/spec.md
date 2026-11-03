---
id: TC-AC-DN-E2E-126-changelog-urutan-default-format-tanggal-action
title: "Modal Changelog: Urutan Default, Format Date, Kolom Action, dan Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-393
  - TC-AC-DN-394
  - TC-AC-DN-395
  - TC-AC-DN-396
coverage:
  web: automated
---

# Modal Changelog: Urutan Default, Format Date, Kolom Action, dan Field

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

### TC-AC-DN-393: Urutan default Date terbaru di atas pada halaman 1

6. Verifikasi baris 1: Date `15/09/26 10:10`, Action `Create`, Device Name `Tag Reel`, Field `Device Name`, Old Value `—`, New Value `Tag Reel`, Modified By `Maya P`
7. Verifikasi baris 2: Date `12/09/26 17:45`, Action `Delete`, Device Name `Retired Gateway`, Field `Device Name`, Old Value `Retired Gateway`, New Value `—`, Modified By `Budi S`
8. Verifikasi baris 3: Date `10/09/26 12:25`, Action `Edit`, Device Name `Cable Tester`, Field `Measurement`, Old Value `Meter`, New Value `Unit`, Modified By `Budi S`
9. Verifikasi baris 4: Date `09/09/26 08:00`, Action `Edit`, Device Name `Cable Tester`, Field `Measurement`, Old Value `Unit`, New Value `Meter`, Modified By `Budi S`
10. Verifikasi baris 5: Date `08/09/26 15:40`, Action `Edit`, Device Name `NFC Tag`, Field `Measurement`, Old Value `Box`, New Value `Unit`, Modified By `Maya P`
11. Verifikasi baris 6: Date `07/09/26 14:05`, Action `Edit`, Device Name `NFC Tag`, Field `Category`, Old Value `TAG > NFC > Accessory`, New Value `TAG > NFC > Tag`, Modified By `Maya P`
12. Verifikasi baris 7: Date `06/09/26 09:30`, Action `Edit`, Device Name `Cable Tester`, Field `Category`, Old Value `TAG > NFC > Tag`, New Value `TAG > NFC > Accessory`, Modified By `Budi S`
13. Verifikasi baris 8: Date `05/09/26 13:15`, Action `Edit`, Device Name `Gate Antenna`, Field `Device Name`, Old Value `Gate Antena`, New Value `Gate Antenna`, Modified By `Maya P`
14. Verifikasi baris 9: Date `03/09/26 10:00`, Action `Create`, Device Name `Retired Gateway`, Field `Device Name`, Old Value `—`, New Value `Retired Gateway`, Modified By `Maya P`
15. Verifikasi baris 10: Date `02/09/26 09:10`, Action `Create`, Device Name `NFC Tag`, Field `Device Name`, Old Value `—`, New Value `NFC Tag`, Modified By `Budi S`

### TC-AC-DN-394: Kolom Date mengikuti Date Format dan Time Format General Settings

16. Verifikasi sel Date baris Create `Tag Reel` `15/09/26 10:10`
17. Verifikasi sel Date baris Edit `Cable Tester` Meter ke Unit `10/09/26 12:25`
18. Klik tombol halaman 2 pada pagination
19. Verifikasi sel Date baris Create `Cable Tester` pada halaman 2 `01/09/26 08:30` (format `dd/MM/yy`, 24 jam, Asia/Jakarta)
20. Klik tombol halaman 1 pada pagination

### TC-AC-DN-395: Kolom Action menampilkan teks biasa tanpa badge

21. Verifikasi sel Action baris Create `Tag Reel` `Create` sebagai teks biasa tanpa badge berwarna
22. Verifikasi sel Action baris Delete `Retired Gateway` `Delete` sebagai teks biasa tanpa badge berwarna
23. Verifikasi sel Action baris Edit `Cable Tester` `Edit` sebagai teks biasa tanpa badge berwarna

### TC-AC-DN-396: Kolom Field menampilkan nama field yang terbaca manusia

24. Verifikasi sel Field baris Create `Tag Reel` berisi `Device Name` dalam Title Case tanpa nama teknis
25. Verifikasi sel Field baris Edit `NFC Tag` 08/09/26 15:40 berisi `Measurement` dalam Title Case tanpa nama teknis
26. Verifikasi sel Field baris Edit `NFC Tag` 07/09/26 14:05 berisi `Category` dalam Title Case tanpa nama teknis

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
