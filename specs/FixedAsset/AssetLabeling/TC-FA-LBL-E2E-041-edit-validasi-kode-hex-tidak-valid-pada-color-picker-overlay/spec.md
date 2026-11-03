---
id: TC-FA-LBL-E2E-041-edit-validasi-kode-hex-tidak-valid-pada-color-picker-overlay
title: "Edit: Validasi Kode Hex Tidak Valid pada Color Picker Overlay"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-125
  - TC-FA-LBL-126
  - TC-FA-LBL-127
  - TC-FA-LBL-128
coverage:
  web: automated
---

# Edit: Validasi Kode Hex Tidak Valid pada Color Picker Overlay

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Tidak ada kasus di spec ini yang menyimpan perubahan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-041`):
  - `Edit Target 125 {runId}-041` (satu label seed untuk keempat TC; overlay dibuka sekali)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hex5Digit` | `#12345` |
  | `Fixture.assetLabeling.hex7Digit` | `#1234567` |
  | `Fixture.assetLabeling.hexNonHeks` | `#GGGGGG` |
  | `Fixture.assetLabeling.hexTanpaPagar` | `EF4444` |

- Kemampuan teknis: mengetik ke kolom Hex di dalam Color Picker Overlay dan menekan Esc.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 125 {runId}-041`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 125 {runId}-041`, lalu klik `Edit`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay

### TC-FA-LBL-125: Edit: kode hex kurang dari 6 digit ditolak real-time

4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hex5Digit`
5. Verifikasi inline error `Invalid color format` tampil di dalam overlay
6. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `Fixture.assetLabeling.warnaSeed` (warna valid terakhir)
7. Verifikasi `[Save]` berstatus disabled selama kode tidak valid

### TC-FA-LBL-126: Edit: kode hex lebih dari 6 digit ditolak real-time

8. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.warnaSeed` (kembalikan ke warna valid; menghapus error kasus sebelumnya)
9. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hex7Digit`
10. Verifikasi inline error `Invalid color format` tampil di dalam overlay
11. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `Fixture.assetLabeling.warnaSeed` (warna valid terakhir)
12. Verifikasi `[Save]` berstatus disabled selama kode tidak valid

### TC-FA-LBL-127: Edit: kode hex berisi karakter non-heksadesimal ditolak real-time

13. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.warnaSeed` (kembalikan ke warna valid; menghapus error kasus sebelumnya)
14. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexNonHeks`
15. Verifikasi inline error `Invalid color format` tampil di dalam overlay
16. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `Fixture.assetLabeling.warnaSeed` (warna valid terakhir)
17. Verifikasi `[Save]` berstatus disabled selama kode tidak valid

### TC-FA-LBL-128: Edit: kode hex 6 digit tanpa awalan # ditolak real-time

18. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.warnaSeed` (kembalikan ke warna valid; menghapus error kasus sebelumnya)
19. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexTanpaPagar`
20. Verifikasi inline error `Invalid color format` tampil di dalam overlay
21. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `Fixture.assetLabeling.warnaSeed` (warna valid terakhir)
22. Verifikasi `[Save]` berstatus disabled selama kode tidak valid
23. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.warnaSeed` (kembalikan ke nilai tersimpan)
24. Tekan Esc untuk menutup Color Picker Overlay
25. Klik icon `[✕]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03, R-12): langkah 8, 13, 18, 23, 24, 25 mengembalikan kolom Hex ke warna valid supaya error `Invalid color format` kasus sebelumnya hilang sebelum kasus berikutnya, lalu menutup overlay dan modal bersih pada akhir spec.
- Seeding minimal (S-11): keempat TC memakai satu label seed dan satu pembukaan overlay karena semuanya validasi tanpa Save (bagian 3, halaman yang sama dipakai berulang).
- Temuan untuk QA:
  - TC-FA-LBL-128 (hex 6 digit tanpa `#`) mengikuti NC-04: UI menampilkan `V-04` (`Invalid color format`); TC tidak menyebut apakah kolom Hex menambahkan `#` otomatis.
