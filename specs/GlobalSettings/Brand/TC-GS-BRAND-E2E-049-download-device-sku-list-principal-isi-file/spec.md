---
id: TC-GS-BRAND-E2E-049-download-device-sku-list-principal-isi-file
title: "Download Accordion Device SKU List pada Instance Principal: Isi dan Nama File"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-197
  - TC-GS-BRAND-294
coverage:
  web: automated
---

# Download Accordion Device SKU List pada Instance Principal: Isi dan Nama File

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Hendra Wijaya); password dari `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login akun ini sebagai aktor pertama di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.GS_TC_PASSWORD`).
- Data Pre-setup (tetap di environment): Brand Principal `Signal One` dengan 3 Device SKU (SKU-HR-001 Handheld Reader A1 / Handheld Reader, SKU-TB-002 Tablet T10 / Tablet, SKU-GW-003 BLE Gateway G2 / BLE Gateway).
- Data Dinamis D-42: brand `Alpha/Beta: Co {runId}-049` pada instance Principal dengan 1 Device SKU. Di-seed lewat API di hook `before` (brand dan 1 Device SKU); fixture belum ada, tim FE menyiapkan. Pembersihan di hook `after`: hapus Device SKU, lalu brand; tidak berasumsi seeding berhasil penuh.
- Format `{runId}` hanya berisi karakter alfanumerik atau `-`, sehingga tidak ikut diganti pada nama berkas unduhan (hanya `/` dan `:` yang diganti `-`).
- State global: tidak ada yang diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih; membaca isi berkas CSV dan XLSX (jumlah baris) dan memeriksa nama berkas. Berkas unduhan dihapus di hook `after`.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand sebagai Total Control Principal

### TC-GS-BRAND-197: Download accordion Device SKU List

2. Search `Signal One`, tekan Enter
3. Buka Detail Signal One (klik link nama)
4. Expand accordion Device SKU
5. Klik Download as XLSX pada accordion Device SKU
6. Verifikasi file `Device SKUs - Signal One.xlsx` terunduh dan berisi 3 baris
7. Tutup Modal Brand Detail

### TC-GS-BRAND-294: Nama file unduhan accordion mengganti karakter tak sah pada Brand Name

8. Search `Alpha/Beta: Co {runId}-049`, tekan Enter
9. Buka Detail Alpha/Beta: Co {runId}-049 (klik link nama)
10. Expand accordion Device SKU List
11. Klik Download as CSV pada accordion Device SKU List
12. Verifikasi file terunduh bernama `Device SKUs - Alpha-Beta- Co {runId}-049.csv` (`/` dan `:` diganti `-`)
13. Verifikasi isi file memuat 1 baris Device SKU

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Nilai Brand Name dinamis D-42 diberi suffix ` {runId}-049` (unik per run dan per spec, sesuai S-12); nama berkas yang diharapkan memuat suffix yang sama, dengan karakter `/` dan `:` pada bagian `Alpha/Beta: Co` diganti `-` sesuai TC sumber. Syarat format `{runId}` tercatat di Prerequisites.
- Langkah penghubung: langkah 2 dan 8 (Search nama brand untuk menemukan baris) serta langkah 7 (menutup Modal Brand Detail).
- Isi berkas export dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f). Spec ini hanya untuk Principal; Device SKU tidak ada pada instance Client.
