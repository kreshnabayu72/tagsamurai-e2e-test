---
id: TC-AC-DN-E2E-149-changelog-download-isi-berkas
title: "Modal Changelog Download: Isi Berkas (Sheet1 XLSX, BOM CSV, Hyphen, Format Date, Modified By Nama Lengkap)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-478
  - TC-AC-DN-479
  - TC-AC-DN-483
  - TC-AC-DN-484
  - TC-AC-DN-485
coverage:
  web: automated
---

# Modal Changelog Download: Isi Berkas (Sheet1 XLSX, BOM CSV, Hyphen, Format Date, Modified By Nama Lengkap)

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
- Pembaca berkas CSV dan XLSX hasil unduhan (byte awal, sheet, sel) disediakan tim FE; Filter Date seed membuat berkas berisi tepat 11 baris data. Spec kelas f (binary buffer): isi berkas dipisah dari asersi fungsional di spec 147.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker. Plus pembaca berkas CSV/XLSX hasil unduhan.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup
3. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
4. Klik `[Apply]`
5. Klik ikon Filter untuk menutup Filter Panel

### TC-AC-DN-478: Download XLSX menghasilkan satu sheet bernama Sheet1

6. Klik ikon Download lalu klik `Download as XLSX`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file terunduh bernama `Changelog-Device-Name.xlsx`
9. Verifikasi file memuat satu sheet bernama `Sheet1` dengan satu baris header dan 11 baris data

### TC-AC-DN-479: File CSV memakai pemisah koma dan UTF-8 dengan BOM

10. Klik ikon Download lalu klik `Download as CSV`
11. Verifikasi byte awal file adalah BOM UTF-8
12. Verifikasi kolom pada baris header dipisah koma

### TC-AC-DN-483: Nilai kosong Old Value dan New Value pada file ditulis sebagai tanda hubung

13. Klik ikon Download lalu klik `Download as CSV`
14. Verifikasi sel Old Value pada baris Create `Tag Reel` berisi `-` (satu tanda hubung)
15. Verifikasi sel New Value pada baris Delete `Retired Gateway` berisi `-` (satu tanda hubung)
16. Verifikasi sel tersebut tidak berisi `—`, teks `null`, atau string kosong

### TC-AC-DN-484: Kolom Date pada file mengikuti format General Settings

17. Klik ikon Download lalu klik `Download as CSV`
18. Verifikasi sel Date baris Create `Tag Reel` berisi `15/09/26 10:10` sesuai Date Format `dd/MM/yy` dan Time Format 24 jam

### TC-AC-DN-485: Kolom Modified By pada file berisi nama lengkap pelaku

19. Klik ikon Download lalu klik `Download as CSV`
20. Verifikasi sel Modified By baris Create `Tag Reel` berisi `Maya Putri`
21. Verifikasi sel Modified By baris Delete `Retired Gateway` berisi `Budi Santoso`
22. Verifikasi sel Modified By tidak berisi format singkat `Maya P` atau `Budi S`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Tiap TC mengunduh berkas sendiri karena aksinya berdiri sendiri; pembatas Filter Date tetap aktif sepanjang spec dan berlaku pada seluruh unduhan.
- TC-AC-DN-485 memuat Dependensi NC-29 pada kolom TC; spec mengikuti Expected TC apa adanya.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
