---
id: TC-AC-DN-E2E-127-changelog-nilai-kosong-modified-by
title: "Modal Changelog: Old/New Value Edit, Nama Setelah Rename, Penanda Nilai Kosong, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-397
  - TC-AC-DN-398
  - TC-AC-DN-399
  - TC-AC-DN-400
  - TC-AC-DN-401
coverage:
  web: automated
---

# Modal Changelog: Old/New Value Edit, Nama Setelah Rename, Penanda Nilai Kosong, dan Modified By

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

### TC-AC-DN-397: Old Value dan New Value baris Edit

6. Verifikasi baris Edit `NFC Tag` Field `Measurement`: Old Value `Box` dan New Value `Unit`
7. Verifikasi baris Edit `Cable Tester` 09/09/26 08:00: Old Value `Unit` dan New Value `Meter`
8. Verifikasi baris Edit `Cable Tester` 10/09/26 12:25: Old Value `Meter` dan New Value `Unit`
9. Verifikasi baris Edit `NFC Tag` Field `Category` 07/09/26 14:05: Old Value `TAG > NFC > Accessory` dan New Value `TAG > NFC > Tag` (jalur penuh dari root)
10. Verifikasi seluruh nilai Old Value dan New Value ditulis sebagai teks biasa tanpa badge

### TC-AC-DN-398: Kolom Device Name baris Edit rename menampilkan nama sesudah perubahan

11. Verifikasi sel Device Name baris Edit `05/09/26 13:15` berisi `Gate Antenna` (nama sesudah perubahan)
12. Verifikasi sel Old Value baris itu berisi `Gate Antena`
13. Verifikasi sel New Value baris itu berisi `Gate Antenna`

### TC-AC-DN-399: Penanda nilai kosong pada Old Value baris Create

14. Verifikasi sel Old Value baris Create `Tag Reel` berisi penanda nilai kosong `—` (em dash)
15. Verifikasi sel New Value baris itu berisi `Tag Reel` untuk Field `Device Name`

### TC-AC-DN-400: Penanda nilai kosong pada New Value baris Delete

16. Verifikasi sel New Value baris Delete `Retired Gateway` berisi penanda nilai kosong `—` (em dash)
17. Verifikasi sel Old Value baris itu berisi `Retired Gateway` untuk Field `Device Name`

### TC-AC-DN-401: Kolom Modified By nama depan dan inisial nama belakang

18. Verifikasi sel Modified By baris Create `Tag Reel` `Maya P` sebagai teks biasa tanpa badge
19. Verifikasi sel Modified By baris Delete `Retired Gateway` `Budi S` sebagai teks biasa tanpa badge

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Temuan untuk QA:
  - TC-AC-DN-399 dan TC-AC-DN-400 memuat Dependensi NC-02 pada kolom TC; spec mengikuti Expected TC apa adanya.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
