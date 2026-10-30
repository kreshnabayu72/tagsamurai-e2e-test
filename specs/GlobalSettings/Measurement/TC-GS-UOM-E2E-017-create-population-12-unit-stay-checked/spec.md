---
id: TC-GS-UOM-E2E-017-create-population-12-unit-stay-checked
title: "Create 12 Unit Berurutan dengan Stay on this form Dicentang (Population)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-36
coverage:
  web: automated
---

# Create 12 Unit Berurutan dengan Stay on this form Dicentang (Population)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Hook suite (login akun default Total Control Client A, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`. Password dari `Spectra.env.GS_TC_PASSWORD`; tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (8 unit, data baca): Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces. Tabel harus berisi tepat 8 unit ini sebelum langkah pertama; suite berjalan serial (`parallel: false`) sehingga tidak ada spec lain yang menambah unit Client A selama spec ini berjalan.
- Data dinamis D-01 (Population, 12 unit; nama literal tanpa suffix `{runId}` karena asersi jumlah 20 baris dan urutan A-Z oleh spec lain bergantung pada nama ini, pengecualian S-12). Dibuat lewat UI oleh spec ini:

| No | Unit Name | Symbol |
|---|---|---|
| 1 | Centimeter | cm |
| 2 | Millimeter | mm |
| 3 | Inch | in |
| 4 | Foot | ft |
| 5 | Milliliter | mL |
| 6 | Gallon | gal |
| 7 | Ounce | oz |
| 8 | Pound | lb |
| 9 | Ton | t |
| 10 | Roll | roll |
| 11 | Set | set |
| 12 | Sheet | sht |

- Hook `before`: hapus lewat API sisa unit non-Pre-setup dari run sebelumnya (unit D-01 maupun unit lain seperti carat, Hectare, Kilogram Force, Barrel) sehingga tabel awal tepat 8 unit Pre-setup. Unit Pre-setup tidak dihapus.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API ke-12 unit D-01 yang dibuat spec ini bila masih ada; spec lain menyiapkan Population-nya sendiri secara idempotent.
- Kemampuan teknis: pembacaan pagination (jumlah baris dan jumlah halaman).
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-UOM-36: Create 12 Measurement berurutan dengan Stay on this form dicentang

1. Klik [+ Unit]
2. Centang checkbox `Stay on this form after submitting`

Untuk setiap baris tabel Data Population D-01 (12 baris, langkah 3 sampai 8):

3. Isi Unit Name dan Symbol baris itu, klik [Submit]
4. Verifikasi toast sukses: "Success, unit has been created."
5. Verifikasi form tetap terbuka
6. Verifikasi field Unit Name kosong
7. Verifikasi field Symbol kosong
8. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang

Sesudah baris ke-12:

9. Tutup form lewat icon `[✕]`
10. Verifikasi halaman 1 menampilkan 10 baris
11. Pindah ke halaman 2 pada Pagination
12. Verifikasi halaman 2 menampilkan 10 baris
13. Verifikasi tabel terbagi dalam 2 halaman (10 per halaman)

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Spec ini sengaja satu TC (TC-GS-UOM-36) karena menjadi sumber Population D-01 yang dibutuhkan spec lain; spec lain menyiapkan Population-nya sendiri lewat API di hook `before` dan tidak bergantung pada spec ini (suite.md).
- Langkah 3 sampai 8 adalah blok perulangan atas 12 baris tabel Prerequisites (butir 7 bagian 8b). Dengan ekspansi spec memuat 2 + (12 x 6) + 5 = 79 langkah, melewati batas 35 langkah; tetap satu topik aksi, satu akun, satu kelas harness, dan satu TC. Tiap pengulangan ditutup asersi toast dan keadaan form (Expected Result a dan b).
- Pada Expected Result b TC ("field Unit Name dan Symbol kosong") spec memecahnya per field (S-01).
- Total 20 baris diturunkan dari dua halaman (10 + 10, langkah 10 sampai 12) dan seeding (8 unit Pre-setup + 12 unit D-01 pada Prerequisites), bukan dibaca dari tabel satu halaman (butir 10 bagian 8b). Asersi 20 baris dan 2 halaman (langkah 10 sampai 13) bergantung pada tabel awal tepat 8 unit Pre-setup dan nama Population literal; run paralel dengan spec lain yang menambah unit ke Client A tidak diizinkan (suite `parallel: false`).
- Langkah penghubung: hook `before` membersihkan sisa unit non-Pre-setup (lihat Prerequisites); langkah 11 (pindah ke halaman 2 pada Pagination, aksi tanpa `Verifikasi`).
- Temuan untuk QA: Post Condition TC-GS-UOM-36 ("12 Measurement baru tersimpan") tidak punya langkah observasi terpisah; ditangani oleh Expected Result c (20 baris) dan tidak diasersi tambahan.
