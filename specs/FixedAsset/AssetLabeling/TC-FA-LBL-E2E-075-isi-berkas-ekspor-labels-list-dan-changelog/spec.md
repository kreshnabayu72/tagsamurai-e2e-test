---
id: TC-FA-LBL-E2E-075-isi-berkas-ekspor-labels-list-dan-changelog
title: "Isi Berkas Ekspor Labels List dan Changelog: Nilai Sel, Escaping CSV, dan BOM"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-273
  - TC-FA-LBL-275
  - TC-FA-LBL-323
coverage:
  web: automated
---

# Isi Berkas Ekspor Labels List dan Changelog: Nilai Sel, Escaping CSV, dan BOM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Color Hex | Total Asset | Modified By |
  |---|---|---|---|
  | `High Priority` | `#EF4444` | 3 | `Sarah J` |
  | `Finance Department` | `#3B82F6` | 5 | `David K` |
  | `Audit Ready` | `#10B981` | 2 | `Sarah J` |
  | `Executive Asset` | `#8B5CF6` | 1 | `Michael W` |
  | `Maintenance Due` | `#F59E0B` | 4 | `David K` |
  | `Seasonal Event` | `#EC4899` | 0 | `Michael W` |
  | `Night Shift` | `#1E3A8A` | 0 | `Sarah J` |
  | `Warehouse Priority` | `#0EA5E9` | 0 | `Sarah J` |
  | `Field Kit` | `#84CC16` | 2 | `David K` |

- Akun ganti 1: Total Control Company Extra (Pre-setup #56: salinan label Pre-setup #12 plus seed tambahan), `Fixture.assetLabeling.akun.totalControlExtra`. Nama company, email akun (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), dan nama env password belum ada, disediakan tim FE; tidak diisi di spec. Dipakai pada langkah 9 sampai 11 (ganti akun, S-07).
- Akun ganti 2: Total Control Company Changelog (Pre-setup #17), `Fixture.assetLabeling.akun.totalControlChangelog` (email mengikuti pola Pre-setup #1 untuk Company Changelog; ditetapkan tim FE), password `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; dipakai pada langkah 17 sampai 19. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` suite mengembalikan sesi ke akun default suite.
- Data Pre-setup #17: log Changelog Company Changelog berisi entri Create `Audit Ready` dan Delete `Old Tag` (hanya dibaca).
- Data Pre-setup #29 (hanya dibaca, di Company Extra): label `R&D, "Core" Lab` (`#0EA5E9`, tanpa aset), `Fixture.assetLabeling.labelRdCoreLab` (nama berisi koma dan kutip ganda; tanpa sufiks `{runId}`).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- Kemampuan teknis (disediakan tim FE/BE): direktori unduhan uji; pembaca CSV (nilai sel) dan penampil byte (BOM, escaping kutip).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-273: Isi sel ekspor per tipe kolom

1. Klik icon Download
2. Klik `Download as CSV`
3. Buka berkas CSV terunduh dan cari baris `High Priority` dan `Seasonal Event`
4. Verifikasi kolom Label ditulis teks `High Priority` (warna chip tidak ikut)
5. Verifikasi kolom Color Hex ditulis `#EF4444`
6. Verifikasi kolom Total Asset ditulis angka `3` (`High Priority`) dan `0` (`Seasonal Event`) tanpa pemisah ribuan
7. Verifikasi kolom Modified By ditulis nama lengkap `Sarah Johnson` (bukan `Sarah J`)
8. Verifikasi kolom Last Updated ditulis dalam format General Settings

### TC-FA-LBL-275: CSV: pembungkus kutip ganda, koma, dan encoding UTF-8 dengan BOM

9. Ganti akun: logout dari Total Control Company Alpha
10. Login sebagai Total Control Company Extra (`Fixture.assetLabeling.akun.totalControlExtra`)
11. Buka Fixed Asset > Settings > Asset Master > tab Labels
12. Klik icon Download
13. Klik `Download as CSV`
14. Buka berkas CSV terunduh dengan penampil byte
15. Verifikasi berkas berencoding UTF-8 dengan BOM
16. Verifikasi nilai label `Fixture.assetLabeling.labelRdCoreLab` dibungkus tanda kutip ganda dengan kutip di dalamnya digandakan: `"R&D, ""Core"" Lab"`

### TC-FA-LBL-323: Isi sel ekspor Changelog: nilai kosong dan tanggal

17. Ganti akun: logout dari Total Control Company Extra
18. Login sebagai Total Control Company Changelog (`Fixture.assetLabeling.akun.totalControlChangelog`, password `Spectra.env.FA_TC_CHANGELOG_PASSWORD`)
19. Buka Fixed Asset > Settings > Asset Master > tab Labels
20. Klik icon Changelog di Table Tools
21. Klik icon Download di toolbar modal
22. Klik `Download as CSV`
23. Buka berkas CSV terunduh dan cari baris `Create Audit Ready` dan `Delete Old Tag`
24. Verifikasi baris Create: Old Value ditulis `-`
25. Verifikasi baris Delete: New Value ditulis `-`
26. Verifikasi kolom Date mengikuti format General Settings
27. Verifikasi kolom Modified By ditulis nama lengkap

## Notes

- Mode: FE+BE (backend nyata; berkas diunduh dan dibaca). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a dan 4b.
- Kelas harness binary buffer (bagian 3 prinsip 13 f): spec ini hanya memuat asersi isi berkas.
- TC-FA-LBL-275 berjalan di Company Extra (login berbeda dari TC-FA-LBL-273 di Company Alpha), sehingga mengunduh CSV sendiri; label `R&D, "Core" Lab` adalah data Pre-setup #29 tanpa sufiks `{runId}`, sehingga Expected memakai literal `"R&D, ""Core"" Lab"` sesuai TC. Urutan TC-FA-LBL-273, 275, 323 mengikuti TC; ketiganya di company berbeda sehingga dua kali ganti akun tidak dapat dikurangi.
- Langkah 9 sampai 11 dan 17 sampai 19 adalah Ganti akun eksplisit (S-07); hook `after` suite mengembalikan sesi ke akun default suite.
- Temuan untuk QA:
  - TC-FA-LBL-273 dan TC-FA-LBL-323 menulis "format General Settings" tanpa nilai literal format; spec mengasersi mengikuti format General Settings Company yang dipakai (nilai ditetapkan tim FE saat script).
  - TC-FA-LBL-323 tidak menyebut nama pengguna pada kolom Modified By Company Changelog; spec mengasersi nama lengkap (bukan format `[First Name] [Last Initial]`).
