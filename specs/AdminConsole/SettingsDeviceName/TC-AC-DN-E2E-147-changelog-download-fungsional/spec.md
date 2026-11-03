---
id: TC-AC-DN-E2E-147-changelog-download-fungsional
title: "Modal Changelog Download: Overlay Format, CSV Tanpa Toast, Mengikuti Search dan Filter Aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-476
  - TC-AC-DN-477
  - TC-AC-DN-480
  - TC-AC-DN-481
coverage:
  web: automated
---

# Modal Changelog Download: Overlay Format, CSV Tanpa Toast, Mengikuti Search dan Filter Aktif

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

- Kemampuan baca jumlah entri (disediakan tim FE/BE, bagian 8b butir 10): jumlah seluruh entri Changelog Principal (N0) dibaca sebelum aksi pada TC-AC-DN-477 karena audit trail tumbuh dan tidak boleh diasersi sebagai angka absolut (S-12).
- Isolasi riwayat seed: TC-AC-DN-481 memakai Filter Date `01/09/26` sampai `15/09/26` bersama Action `Delete`; TC-AC-DN-480 memakai kata kunci `tester` yang hanya ada pada entri seed (S-14).
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker. Plus pembaca berkas CSV/XLSX hasil unduhan.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List

### TC-AC-DN-476: Overlay Download menawarkan dua format

2. Klik ikon Download di toolbar popup
3. Verifikasi overlay menampilkan opsi `Download as CSV` dan `Download as XLSX`

### TC-AC-DN-477: Download CSV tanpa Search dan Filter mengunduh seluruh entri tanpa toast sukses

4. Catat jumlah seluruh entri Changelog Principal (N0) lewat kemampuan baca
5. Klik `Download as CSV`
6. Verifikasi tidak ada toast sukses
7. Verifikasi file terunduh bernama `Changelog-Device-Name.csv`
8. Verifikasi file memuat satu baris header dan N0 baris data (seluruh entri, bukan hanya halaman 1)
9. Verifikasi header memuat tujuh kolom: Date, Action, Device Name, Field, Old Value, New Value, Modified By

### TC-AC-DN-480: Download mengikuti Search yang aktif

10. Klik ikon Search, ketik Search `tester`, tekan Enter
11. Klik ikon Download lalu klik `Download as CSV`
12. Verifikasi file terunduh memuat satu baris header dan 4 baris data `Cable Tester`
13. Klik ikon panah `(←)` di kiri toolbar

### TC-AC-DN-481: Download mengikuti Filter yang aktif

14. Klik ikon Filter di toolbar popup
15. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
16. Klik field `Action`, centang `Delete`, lalu tutup dropdown
17. Klik `[Apply]`
18. Klik ikon Download lalu klik `Download as CSV`
19. Verifikasi file terunduh memuat satu baris header dan 1 baris data Action `Delete`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Nama berkas, header, dan jumlah baris adalah asersi fungsional; isi sel dan BOM ada di spec 149. Asersi tidak ada toast sukses diletakkan segera setelah pemicu dan sebelum asersi berkas (bagian 8b butir 11). Langkah klik `(←)` memulihkan Search sebelum TC berikutnya (S-09).
- Temuan untuk QA:
  - TC-AC-DN-477 Expected b menyebut 11 baris data; spec memakai N0 hasil baca sebelum aksi karena audit trail tumbuh (S-12).
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
