---
id: TC-GS-BRAND-E2E-067-brand-hasil-import-edit-dan-hapus
title: "Brand Hasil Import Dapat Diedit dan Dihapus seperti Brand Manual"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-225
coverage:
  web: automated
---

# Brand Hasil Import Dapat Diedit dan Dihapus seperti Brand Manual

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi): brand `Imported Co {runId}-067` (D-29), dibuat lewat job Import Type Brand yang dijalankan API di hook `before` dengan nilai sel diapit spasi (`  Imported Co {runId}-067  `) sehingga tersimpan ter-trim. Dihapus lewat UI pada spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Imported Co {runId}-067` dan `Imported Group {runId}-067` bila masih ada.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-225: login sebagai Total Control, berada di Global Settings > Master Reference > Brand, dan Brand hasil Import (D-29) sudah ada.

## Test Steps

### TC-GS-BRAND-225: Brand hasil Import dapat diedit dan dihapus seperti Brand manual

1. Search `Imported Co {runId}-067` pada tabel Brand
2. Verifikasi nama tampil `Imported Co {runId}-067` (ter-trim, tanpa spasi tepi)
3. Klik `⋯` pada baris `Imported Co {runId}-067` > Edit, ubah Brand Name menjadi `Imported Group {runId}-067`, klik [Save]
4. Verifikasi toast sukses: "Success, brand has been updated."
5. Search `Imported Group {runId}-067`, klik `⋯` pada baris `Imported Group {runId}-067` > Delete → dialog `Delete Brand` tampil, klik [Delete]
6. Verifikasi toast sukses: "Success, brand has been deleted."

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Tidak ada data lain yang dipengaruhi. Delete ditaruh paling akhir (prinsip 5); spec hanya memuat satu TC.
- Pembuatan brand lewat Import dilakukan di hook `before` karena Import bukan objek uji TC ini (modul Import: `global-settings/import/PRD/import.md`, IMP-LOGIC-01).
- Langkah penghubung: Search `Imported Group {runId}-067` pada langkah 5 sebelum Delete, tidak tertulis di Langkah Uji TC sumber.
