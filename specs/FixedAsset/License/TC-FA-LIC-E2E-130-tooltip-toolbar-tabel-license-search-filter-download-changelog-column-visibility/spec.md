---
id: TC-FA-LIC-E2E-130-tooltip-toolbar-tabel-license-search-filter-download-changelog-column-visibility
title: "Tooltip Toolbar Tabel License: Search, Filter, Download, Changelog, dan Column Visibility"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-10
  - TC-FA-LIC-11
coverage:
  web: automated
---

# Tooltip Toolbar Tabel License: Search, Filter, Download, Changelog, dan Column Visibility

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: kuota dan hierarki #12, riwayat #13, sesi aktif #14; hanya dibaca, tidak diubah. Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Kemampuan teknis: hover kursor dan fokus keyboard (tombol Tab) pada ikon toolbar.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

Tabel "Ikon toolbar tabel riwayat" (urutan baris = urutan verifikasi; sama untuk sub-tab `Subscription History` dan `Allocation History`):

| Elemen | Tooltip |
|---|---|
| ikon Search | `Search` |
| ikon Filter | `Filter` |
| ikon Download | `Download` |
| header kolom Actions `⋯` | `Column Visibility` |

Tabel "Ikon toolbar Tab Concurrent User":

| Elemen | Tooltip |
|---|---|
| ikon Search | `Search` |
| ikon Filter | `Filter` |
| ikon Changelog | `Changelog` |
| header kolom Actions `⋯` | `Column Visibility` |

Tabel "Ikon toolbar Section 2 Tab Allocation Quota":

| Elemen | Tooltip |
|---|---|
| ikon Search | `Search` |
| ikon Filter | `Filter` |
| ikon Download | `Download` |
| ikon Changelog | `Changelog` |

## Test Steps

### TC-FA-LIC-10: Tooltip toolbar tabel riwayat

1. Untuk setiap baris tabel "Ikon toolbar tabel riwayat" pada sub-tab `Subscription History`, ulangi langkah 2 sampai 5
2. Arahkan kursor ke elemen pada baris tabel
3. Verifikasi tooltip sesuai kolom Tooltip baris tabel tampil
4. Pindahkan fokus keyboard ke elemen yang sama (tekan Tab hingga fokus mencapai elemen itu)
5. Verifikasi tooltip sesuai kolom Tooltip baris tabel tampil saat elemen difokus
6. Klik sub-tab `Allocation History`
7. Ulangi langkah 1 sampai 5 pada sub-tab `Allocation History`

### TC-FA-LIC-11: Tooltip toolbar Tab Concurrent User dan Tab Allocation Quota

8. Klik Tab `Concurrent User`
9. Untuk setiap baris tabel "Ikon toolbar Tab Concurrent User", ulangi langkah 10 sampai 11
10. Arahkan kursor ke elemen pada baris tabel
11. Verifikasi tooltip sesuai kolom Tooltip baris tabel tampil
12. Verifikasi tidak ada ikon Download pada toolbar Tab `Concurrent User`
13. Klik Tab `Allocation Quota`
14. Untuk setiap baris tabel "Ikon toolbar Section 2 Tab Allocation Quota", ulangi langkah 15 sampai 16
15. Arahkan kursor ke ikon pada baris tabel di toolbar Section 2
16. Verifikasi tooltip sesuai kolom Tooltip baris tabel tampil

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-10, 11). Tidak ada TC hanya-BE di spec ini.
- Langkah di atas sekitar 35: langkah nominal berjumlah 16, tetapi dengan ekspansi blok ulang (langkah 1 sampai 5 dua kali dengan 4 elemen, langkah 9 sampai 11 dan 14 sampai 16 dengan 4 elemen) berjumlah sekitar 52 langkah. Alasan dipertahankan: seluruh blok satu topik (tooltip ikon toolbar tabel License), parameter tiap iterasi ada di tabel `## Prerequisites`, tanpa langkah bersyarat, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah yang diulang: langkah 2 sampai 5 (tiap baris tabel "Ikon toolbar tabel riwayat", pada dua sub-tab), langkah 10 sampai 11, dan langkah 15 sampai 16.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): klik sub-tab dan tab (langkah 6, 8, 13). Langkah 4 (fokus keyboard) menjadi langkah aksi untuk TC-10 butir b.
- Langkah 12 (absence ikon Download) berposisi sesudah langkah 11 yang memverifikasi tooltip ikon lain pada toolbar yang sama (anchor positif).
- Temuan untuk QA:
  - TC-10 butir b ("Tooltip juga tampil saat elemen difokus dengan keyboard") tidak punya langkah uji; spec menambah langkah 4 (fokus keyboard) sebagai aksi pemicu butir b.
