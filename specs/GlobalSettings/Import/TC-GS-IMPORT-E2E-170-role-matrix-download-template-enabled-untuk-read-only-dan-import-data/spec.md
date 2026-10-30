---
id: TC-GS-IMPORT-E2E-170-role-matrix-download-template-enabled-untuk-read-only-dan-import-data
title: "Role Matrix: Download Template Enabled untuk Read Only dan Import data (Read Only)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-454
  - TC-GS-IMPORT-761
coverage:
  web: automated
---

# Role Matrix: Download Template Enabled untuk Read Only dan Import data (Read Only)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): sesi login berganti per role dan suite mengubah state global; lihat `suite.md`. Spec ini hanya membaca (tidak membuat atau mengubah data).
- Tabel "Role yang diuji" (satu blok role per baris: Read Only langkah 1 sampai 5, Import data (Read Only) langkah 6 sampai 11):

  | Role | Akun | Env password | TC |
  |---|---|---|---|
  | Read Only | Read Only Client A (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net` (Pre-setup) | `Spectra.env.GS_RO_PASSWORD` | TC-454 |
  | Import data (Read Only) | Import data (Read Only) Client A (Tono Hartono) `importRead_automated_qaTeam1@qwertysystem.net` (Pre-setup) | `Spectra.env.GS_IMPORTRO_PASSWORD` | TC-761 |

- Akun aktor pertama (Read Only Client A) login di hook `before`; akun berikutnya masuk lewat Step ganti akun eksplisit (langkah 6). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): pembaca nama berkas unduhan di browser. Tanpa data dinamis (Sub-Tab Brand).
- Pemulihan (hook `after`): tidak ada data yang dibuat; kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-454: Download Template Enabled untuk Read Only

1. Buka Global Settings > Import, pilih Sub-Tab Brand
2. Verifikasi `[Download Template]` Enabled
3. Klik `[Download Template]`
4. Verifikasi berkas `Template-Import-Brand.xlsx` terunduh langsung
5. Verifikasi tidak ada toast yang tampil

### TC-GS-IMPORT-761: Download Template Enabled untuk Import data (Read Only)

6. Ganti akun: logout, lalu login sebagai Import data (Read Only) Client A (Tono Hartono) dengan `Spectra.env.GS_IMPORTRO_PASSWORD`
7. Buka Global Settings > Import, pilih Sub-Tab Brand
8. Verifikasi `[Download Template]` Enabled
9. Klik `[Download Template]`
10. Verifikasi berkas `Template-Import-Brand.xlsx` terunduh langsung
11. Verifikasi tidak ada toast yang tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix positif (konvensi bagian 3a): langkah tiap role identik dan hanya akun login yang berbeda; kasus ini bukan kelas harness. Ditulis per blok role (bukan perulangan "untuk setiap role") karena ganti akun menuntut Step eksplisit (langkah 6) dan akun pertama login di hook `before` (bagian 3a).
- Spec singkat (11 langkah, dua blok role) sehingga tidak melewati sekitar 35 langkah. Tidak ada langkah bersyarat.
- Langkah penghubung (tanpa `Verifikasi`): ganti akun (langkah 6) dan pemilihan Sub-Tab (langkah 1 dan 7). Langkah 5 dan 11 (tidak ada toast) didahului berkas terunduh (langkah 4 dan 10) sebagai anchor positif yang terhubung ke pemicu.
- Pembagian TC lintas spec: isi berkas Download Template ada di spec 166, 167, dan 168 (kelas binary buffer); spec ini hanya mengasersi bahwa tombol Enabled dan berkas terunduh, sesuai Expected TC-GS-IMPORT-454 dan 761.
- Temuan untuk QA:
  - TC-GS-IMPORT-454 dan TC-GS-IMPORT-761 memiliki langkah dan Expected identik dan hanya berbeda pada role; kombinasi role lain (Default User, Import data (Create)) tidak punya TC untuk Download Template sehingga dilaporkan sebagai usulan TC baru bila QA menghendaki.
  - Post Condition TC-GS-IMPORT-454 dan 761 "-" dan tidak ada keadaan yang perlu dipulihkan.
