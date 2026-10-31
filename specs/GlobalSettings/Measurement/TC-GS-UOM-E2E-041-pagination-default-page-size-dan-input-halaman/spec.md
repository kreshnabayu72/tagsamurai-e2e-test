---
id: TC-GS-UOM-E2E-041-pagination-default-page-size-dan-input-halaman
title: "Pagination: Default 10 per Halaman, Ubah Page Size, dan Input Nomor Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-153
  - TC-GS-UOM-154
  - TC-GS-UOM-339
coverage:
  web: automated
---

# Pagination: Default 10 per Halaman, Ubah Page Size, dan Input Nomor Halaman

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box (Used By (Items) 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Liter / L (0), Meter / m (0), Pack / pk (0), Pieces / pc (3).
- Data Dinamis: Population D-01 (12 unit, nama literal, Used By (Items) 0): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada); total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding. Nama literal disengaja (asersi hasil bergantung pada nama; pengecualian S-12); cleanup hanya menghapus unit yang dibuat spec ini.
- Spec tidak mengubah data unit.
- State global yang dipulihkan: page size tabel dikembalikan ke 10 di langkah spec dan di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: membuka Overlay Page Size pada pagination; mengetik di input nomor halaman; klien HTTP/API untuk seeding Population (disediakan tim FE).

## Test Steps

### TC-GS-UOM-153: Pagination default 10 per halaman dengan 2 halaman untuk 20 baris

1. Verifikasi tabel menampilkan 10 baris di halaman 1
2. Verifikasi pagination menampilkan 2 halaman

### TC-GS-UOM-154: Ubah page size dan navigasi halaman

3. Pilih page size 25
4. Verifikasi tabel menampilkan 20 baris dalam 1 halaman
5. Pilih page size 10
6. Klik Next
7. Verifikasi tabel menampilkan halaman 2
8. Klik Previous
9. Verifikasi tabel menampilkan halaman 1

### TC-GS-UOM-339: Opsi page size 10, 25, 50, 100 tanpa opsi All dan input nomor halaman langsung

10. Klik Overlay Page Size pada pagination
11. Verifikasi Overlay Page Size memuat opsi `10`, `25`, `50`, dan `100`
12. Verifikasi Overlay Page Size tidak memuat opsi `All`
13. Pilih page size 50
14. Verifikasi tabel menampilkan 20 baris dalam 1 halaman
15. Klik Overlay Page Size pada pagination, pilih page size 100
16. Verifikasi tabel menampilkan 20 baris dalam 1 halaman
17. Klik Overlay Page Size pada pagination, pilih page size 10
18. Ketik nomor halaman `2` pada input nomor halaman, tekan Enter
19. Verifikasi tabel langsung menampilkan halaman 2

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 mengembalikan page size ke 10 (TC-GS-UOM-154 langkah 2); TC-GS-UOM-339 diakhiri page size 10 (Post Condition TC), dan hook `after` menjadi cadangan.
- Layar awal Tab Measurement dibuka di hook `beforeEach` (TC-GS-UOM-153 langkah 1 "Buka Tab Measurement" tidak diulang di Test Steps). Total N = 20 unit diturunkan dari seeding, bukan dibaca dari tabel yang hanya menampilkan satu halaman.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-154 dan TC-GS-UOM-339 sama-sama menguji ubah page size (25 dan 50/100); keduanya dipertahankan sesuai TC.
