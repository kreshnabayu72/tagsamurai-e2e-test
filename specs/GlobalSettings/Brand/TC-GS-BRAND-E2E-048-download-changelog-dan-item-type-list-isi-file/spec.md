---
id: TC-GS-BRAND-E2E-048-download-changelog-dan-item-type-list-isi-file
title: "Download Changelog dan Accordion Item Type List: Isi File"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-182
  - TC-GS-BRAND-194
coverage:
  web: automated
---

# Download Changelog dan Accordion Item Type List: Isi File

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment, spec ini tidak membuat atau mengubah data): 12 brand Client A; Vertex Labs memiliki 5 Item Type pada accordion Item Type List; Modal Changelog Brand memiliki entri.
- State global: tidak ada yang diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih; membaca isi berkas CSV dan XLSX (jumlah baris). Berkas unduhan dihapus di hook `after`.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-182: Download Changelog

2. Buka Changelog
3. Klik Download, lalu klik `Download as XLSX`
4. Verifikasi file `Changelog-Brand.xlsx` terunduh
5. Verifikasi tidak ada toast sukses
6. Tutup Modal Changelog

### TC-GS-BRAND-194: Download accordion Item Type List

7. Search `Vertex Labs`, tekan Enter
8. Buka Detail Vertex Labs (klik link nama)
9. Klik Download as CSV pada accordion Item Type List
10. Verifikasi file `Item Types - Vertex Labs.csv` terunduh dan berisi 5 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Isi berkas export dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f). Download tabel utama ada di spec `TC-GS-BRAND-E2E-047-download-tabel-utama-isi-file`; Device SKU List (Principal) di spec `TC-GS-BRAND-E2E-049-download-device-sku-list-principal-isi-file`.
- Langkah penghubung: langkah 6 (menutup Modal Changelog) dan langkah 7 (Search Vertex Labs untuk menemukan baris).
- TC-GS-BRAND-182 pada TC sumber hanya menyebut nama berkas dan tidak adanya toast sukses; isi berkas tidak diasersi lebih jauh dari Expected Result TC.
