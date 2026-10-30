---
id: TC-GS-BRAND-E2E-044-used-by-items-principal-distributor
title: "Used By (Items) Sama dengan Total Item di Detail pada Instance Principal dan Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-272
coverage:
  web: automated
tags: [principal]
---

# Used By (Items) Sama dengan Total Item di Detail pada Instance Principal dan Distributor

## Prerequisites

- Mode: FE+BE.
- Akun (dua akun, ganti akun eksplisit di tengah spec; hook `after` mengembalikan sesi ke akun default suite, Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.GS_TC_PASSWORD`):
  - Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Hendra Wijaya); password dari `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login di hook `before` (seedSession).
  - Total Control Distributor `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (Bima Saputra); password dari `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`. Fixture baru: user ini beserta instance Distributor perlu disediakan QA/tim FE.
- Data Pre-setup (tetap di environment, spec ini tidak membuat atau mengubah data): Brand Principal `Signal One` (3 Device SKU: SKU-HR-001 Handheld Reader A1 / Handheld Reader, SKU-TB-002 Tablet T10 / Tablet, SKU-GW-003 BLE Gateway G2 / BLE Gateway); Brand Distributor `Aero Dist` (1 Device SKU SKU-DS-001 Distributor Reader A1 / Handheld Reader; fixture baru, perlu disediakan).
- State global: tidak ada yang diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: login dua akun berbeda secara berurutan dalam satu spec (logout lalu login ulang).

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand sebagai Total Control Principal

### TC-GS-BRAND-272: Angka Used By (Items) sama dengan Total Item di Detail pada instance Principal dan Distributor dengan Device SKU

2. Search `Signal One`, tekan Enter
3. Catat angka Used By (Items) baris Signal One
4. Buka Detail Signal One (klik link nama)
5. Verifikasi angka tabel `3` sama dengan `Total Item: 3` di Detail Signal One (menghitung Device SKU)
6. Tutup Modal Brand Detail
7. Logout dari akun Total Control Principal
8. Login sebagai Total Control Distributor `totalControlDistributor_automated_qaTeam1@qwertysystem.net`
9. Buka layar Global Settings > Master Reference > Brand
10. Search `Aero Dist`, tekan Enter
11. Catat angka Used By (Items) baris Aero Dist
12. Buka Detail Aero Dist (klik link nama)
13. Verifikasi angka tabel `1` sama dengan `Total Item: 1` di Detail Aero Dist

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Satu TC, dua akun: Principal lalu Distributor, dengan langkah ganti akun eksplisit (langkah 7 sampai 9).
- Langkah penghubung: langkah 2 dan 10 (Search nama brand untuk menemukan baris) serta langkah 6 (menutup Modal Brand Detail sebelum ganti akun).
- Kebutuhan fixture baru (user Total Control Distributor dan Brand `Aero Dist`) sudah dicatat sebagai kebutuhan di Prerequisites dan disiapkan tim FE.
