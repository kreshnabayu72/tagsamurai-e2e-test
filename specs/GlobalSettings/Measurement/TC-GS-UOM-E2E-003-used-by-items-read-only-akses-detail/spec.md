---
id: TC-GS-UOM-E2E-003-used-by-items-read-only-akses-detail
title: "Read Only Mengakses Unit Detail lewat Link Nama dan Angka Used By (Items)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-373
  - TC-GS-UOM-207
coverage:
  web: automated
---

# Read Only Mengakses Unit Detail lewat Link Nama dan Angka Used By (Items)

## Prerequisites

- Mode: FE+BE.
- Akun: Read Only Client A (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_RO_PASSWORD`. Login akun ini sebagai aktor pertama di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.GS_TC_PASSWORD`). Nama env didaftarkan di `executionConfig.environmentVariables`.
- Data (hanya dibaca, spec tidak membuat atau mengubah data): Pre-setup Client A dan Population D-01 (total N = 20 unit, di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md`). Unit yang dipakai: Box (Used By (Items) `4`) dan Liter (`0`) di halaman 1, serta Pieces di halaman 2 (dicari lewat Search).
- Guided Tooltip: flag halaman Measurement untuk akun Read Only mengikuti pernyataan hook suite di `suite.md` (suite menyetelnya untuk setiap akun aktor yang dipakai spec).
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-UOM-373: Read Only dapat mengklik angka Used By (Items) untuk membuka Detail

1. Klik angka Used By (Items) baris Box
2. Verifikasi Modal Unit Detail Box terbuka
3. Verifikasi Total Item `4`
4. Verifikasi tidak ada tombol kelola di Modal Unit Detail Box
5. Tutup Modal Unit Detail lewat `[✕]`
6. Klik angka Used By (Items) baris Liter (`0`)
7. Verifikasi Modal Unit Detail Liter terbuka
8. Verifikasi Total Item `0`
9. Verifikasi Accordion Item Type List menampilkan empty state `No item types linked`
10. Verifikasi tidak ada tombol kelola di Modal Unit Detail Liter
11. Tutup Modal Unit Detail lewat `[✕]`

### TC-GS-UOM-207: Read Only dapat membuka Unit Detail

12. Ketik Search `Pieces`, tekan Enter
13. Klik `⋯` baris Pieces > Detail
14. Verifikasi Modal Unit Detail Pieces terbuka
15. Verifikasi Modal Unit Detail Pieces read-only: tidak ada tombol kelola di modal
16. Tutup Modal Unit Detail lewat `[✕]`
17. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dibalik (TC-GS-UOM-373 lebih dulu) karena baris Box dan Liter berada di halaman 1 sehingga tidak butuh Search, sedangkan Pieces (TC-GS-UOM-207) di halaman 2 butuh Search yang harus dikosongkan lagi.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 5, 11, dan 16 (menutup Modal Unit Detail), 12 (Search `Pieces` untuk menemukan baris di halaman 2), dan 17 (mengosongkan Search).
- "Read-only" pada Expected TC-GS-UOM-207 diasersi lewat tidak adanya tombol kelola (langkah 15), mengikuti Expected c TC-GS-UOM-373; TC-GS-UOM-207 sendiri tidak merinci apa yang membuat modal read-only.
- Semua TC dalam spec ini memakai satu akun (Read Only); tidak ada penggantian akun. Klik angka Used By (Items) oleh Total Control ada di spec `TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover`.
- Temuan untuk QA: TC-GS-UOM-207 hanya menyebut "Modal Unit Detail terbuka read-only" tanpa Expected yang dapat diukur; spec menyamakannya dengan Expected c TC-GS-UOM-373 (tidak ada tombol kelola).
