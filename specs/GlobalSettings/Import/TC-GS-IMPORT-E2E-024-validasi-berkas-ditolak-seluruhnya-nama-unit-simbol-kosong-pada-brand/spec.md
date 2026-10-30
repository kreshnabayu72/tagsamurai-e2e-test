---
id: TC-GS-IMPORT-E2E-024-validasi-berkas-ditolak-seluruhnya-nama-unit-simbol-kosong-pada-brand
title: "Validasi Berkas Ditolak Seluruhnya: Nama, Unit, dan Simbol Kosong pada Brand, Measurement, Position, dan Division"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-98
  - TC-GS-IMPORT-99
  - TC-GS-IMPORT-100
  - TC-GS-IMPORT-101
  - TC-GS-IMPORT-102
  - TC-GS-IMPORT-103
coverage:
  web: automated
---

# Validasi Berkas Ditolak Seluruhnya: Nama, Unit, dan Simbol Kosong pada Brand, Measurement, Position, dan Division

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Brand, Measurement, Position, dan Division (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Tidak ada draft yang tercipta karena berkas ditolak seluruhnya. Berkas fixture D-07 (isi literal, satu nama berkas satu isi) mengikuti tabel "Parameter validasi".
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik, hanya parameter berbeda). Header Error Banner untuk blok 1 baris bermasalah: "1 row couldn't be imported. Fix the following and upload again:".

  | TC | Sub-Tab | Berkas dan isi | Header Error Banner | Baris pesan Error Banner (berurutan) |
  |---|---|---|---|---|
  | 98 | Brand | `brand-empty-name.csv`: header `Brand Name,Catatan`; 10 baris data; baris ke-4 Brand Name kosong dengan Catatan `x`; sembilan baris lain `Merek 01`, `Merek 02`, `Merek 03`, `Merek 05` sampai `Merek 10` dengan Catatan kosong | 1 row | `Brand name must not be empty. 4` |
  | 99 | Measurement | `measurement-empty-unit.csv`: header `Unit Name,Symbol`; baris `Meter,m` / `,s` / `Liter,L` | 1 row | `Unit name must not be empty. 2` |
  | 100 | Measurement | `measurement-empty-symbol.csv`: header `Unit Name,Symbol`; baris `Meter,m` / `Liter,L` / `Gram,` | 1 row | `Symbol must not be empty. 3` |
  | 101 | Measurement | `measurement-empty-both.csv`: header `Unit Name,Symbol`; baris `Meter,m` / `,s` / `Liter,L` / `Gram,g` / `Ton,` | "2 rows couldn't be imported. Fix the following and upload again:" | `Unit name must not be empty. 2`, lalu `Symbol must not be empty. 5` |
  | 102 | Position | `position-empty-name.csv`: header `Position Name,Catatan`; baris `,x` / `Teknisi Gudang,` / `Kepala Shift,` | 1 row | `Position name must not be empty. 1` |
  | 103 | Division | `division-empty-name.csv`: header `Division Name,Code`; baris `Logistik,LOG` / `Pemasaran,PMS` / `,X3` / `Keuangan,KEU` | 1 row | `Division name must not be empty. 3` |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-98, 99, 100, 101, 102, 103: berkas ditolak seluruhnya

Untuk setiap baris tabel "Parameter validasi" (langkah 1 sampai 11; diulang enam kali berurutan, TC 98 sampai 103):

1. Klik Sub-Tab sesuai kolom Sub-Tab
2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
6. Verifikasi Error Banner tampil di dalam modal dengan header sesuai kolom Header Error Banner
7. Verifikasi baris pesan Error Banner sesuai kolom Baris pesan Error Banner (berurutan bila lebih dari satu)
8. Verifikasi tidak ada toast
9. Klik `[Cancel]` pada Modal Column Mapping
10. Verifikasi modal tertutup
11. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 1 sampai 11 diulang enam kali (ekspansi 66 langkah); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 1 sampai 11 (konvensi 8b butir 7). Langkah 1 selalu memilih Sub-Tab sesuai tabel (aksi idempoten bila Sub-Tab sudah aktif).
- Alasan di atas sekitar 35 langkah: enam blok homogen satu pola (upload berkas bermasalah, Confirm Mapping ditolak seluruhnya, Cancel), tanpa data tercipta; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 8) didahului `Verifikasi` Error Banner tampil di modal (langkah 6 dan 7) sebagai anchor positif yang terhubung ke pemicu (Confirm Mapping); asersi "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Pada blok TC-GS-IMPORT-101 langkah 7 memverifikasi dua baris pesan secara berurutan.
- Temuan untuk QA:
  - Angka pada nama data (`Merek 01`, dan seterusnya) mengikuti nomor baris data; berkas disediakan tim FE/BE sesuai Data Uji TC. Nama literal tanpa suffix `{runId}`; keunikan dijaga karena tidak ada draft yang tercipta.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
