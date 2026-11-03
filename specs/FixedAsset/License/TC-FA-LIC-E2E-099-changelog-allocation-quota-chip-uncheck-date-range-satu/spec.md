---
id: TC-FA-LIC-E2E-099-changelog-allocation-quota-chip-uncheck-date-range-satu
title: "Filter Modal Changelog Allocation Quota: Chip Uncheck di Dropdown, Date Range Inklusif, dan Satu Hari"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-345
  - TC-FA-LIC-346
  - TC-FA-LIC-347
coverage:
  web: automated
---

# Filter Modal Changelog Allocation Quota: Chip Uncheck di Dropdown, Date Range Inklusif, dan Satu Hari

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (General Settings `dd/MM/yy`, `HH:mm`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri) lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE).

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 10:05 | Edit | Divisi Logistik | Allocated Quota | 500 | 600 | Rudi H |
  | 28/09/26 15:30 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |
  | 27/09/26 09:00 | Remove Allocation | Gudang A | Allocated Quota | 100 | — | Rudi H |
  | 26/09/26 11:20 | Edit | Divisi Keuangan | Allocated Quota | — | 50 | Dewi L |
  | 25/09/26 08:45 | Remove Allocation | Divisi IT | Allocated Quota | 100 | — | Rudi H |

- Spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-FA-LIC-345: Uncheck di dalam dropdown menghapus chip yang bersangkutan

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Klik ikon Filter pada toolbar
3. Pada `Action` pilih `Edit` dan `Remove Allocation`
4. Buka dropdown `Action`, hapus centang `Edit`
5. Verifikasi chip `Edit` hilang dari field
6. Verifikasi chip `Remove Allocation` tetap
7. Verifikasi tabel belum berubah dan tetap menampilkan 6 baris sebelum `[Apply]` ditekan
8. Klik `[Apply]`
9. Verifikasi perubahan berlaku pada hasil setelah `[Apply]`: tabel menampilkan 27/09/26 09:00, 25/09/26 08:45
10. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-346: Filter date range picker (inklusif)

11. Verifikasi placeholder tiap field Date `Select date`
12. Pada `Date` pilih rentang 26/09/26–28/09/26
13. Verifikasi teks tanggal terpilih mengikuti Date Format General Settings (`dd/MM/yy`)
14. Klik `[Apply]`
15. Verifikasi Date 26/09/26–28/09/26 menampilkan: 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20
16. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-347: Pilih satu hari saja (Start = End) bersifat inklusif

17. Pada `Date` pilih tanggal 26/09/26 sebagai awal dan akhir, klik `[Apply]`
18. Verifikasi baris dengan Date tepat 26/09/26 tampil: 26/09/26 11:20
19. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 10, 16, dan 19 membersihkan filter antar kasus (S-09); langkah 19 juga menutup modal.
- Temuan untuk QA:
  - TC-FA-LIC-345 butir b ("perubahan berlaku pada hasil setelah `[Apply]` ditekan") tidak menyebut baris hasil; spec memakai dua entri `Remove Allocation` dari Pre-setup #27 (sama dengan hasil TC-FA-LIC-344) dan menambah `Verifikasi` tabel belum berubah sebelum `[Apply]` (langkah 7) untuk klausa "setelah".
  - TC-FA-LIC-346 butir a menyebut "placeholder tiap field `Select date`" dan teks tanggal terpilih tanpa langkah terpisah; spec mengasersi placeholder sebelum memilih rentang (langkah 11) dan teks tanggal sesudahnya (langkah 13).
