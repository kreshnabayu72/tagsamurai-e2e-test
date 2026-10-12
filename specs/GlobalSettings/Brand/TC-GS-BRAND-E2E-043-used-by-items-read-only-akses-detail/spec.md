---
id: TC-GS-BRAND-E2E-043-used-by-items-read-only-akses-detail
title: "Read Only Mengakses Brand Detail lewat Link Nama dan Angka Used By (Items)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-270
  - TC-GS-BRAND-204
coverage:
  web: automated
---

# Read Only Mengakses Brand Detail lewat Link Nama dan Angka Used By (Items)

## Prerequisites

- Mode: FE+BE.
- Akun: Read Only Client A `readOnly_automated_qaTeam1@qwertysystem.net` (Maya Putri); password dari `Spectra.env.GS_RO_PASSWORD`. Login akun ini sebagai aktor pertama di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.GS_TC_PASSWORD`).
- Data Pre-setup (tetap di environment, spec ini tidak membuat atau mengubah data): 12 brand Client A. Yang dipakai: Acme Corp (Used By `1`) dan Vertex Labs (Used By `5`). Baris dicari lewat Search karena bisa berada di halaman selain halaman pertama.
- State global: tidak ada yang diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: tidak ada yang khusus.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-270: Read Only dapat klik angka Used By (Items)

2. Search `Acme Corp`, tekan Enter
3. Klik angka pada baris Acme Corp
4. Verifikasi Modal Brand Detail Acme Corp terbuka dengan `Total Item: 1`
5. Verifikasi tidak ada kontrol Create/Edit/Delete di Modal Brand Detail
6. Tutup Modal Brand Detail

### TC-GS-BRAND-204: Read Only dapat membuka Detail lewat link nama dan angka Used By (Items) tanpa kontrol ubah

7. Search `Vertex Labs`, tekan Enter
8. Klik link nama Vertex Labs
9. Verifikasi Modal Brand Detail tampil
10. Verifikasi tidak ada tombol Create/Edit/Delete untuk Item Type atau Model/Type
11. Tutup Modal Brand Detail
12. Klik angka `5` pada baris Vertex Labs
13. Verifikasi Modal Brand Detail tampil
14. Verifikasi tidak ada tombol Create/Edit/Delete untuk Item Type atau Model/Type

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Langkah penghubung: langkah 2 dan 7 (Search nama brand untuk menemukan baris) serta langkah 6 dan 11 (menutup Modal Brand Detail).
- Semua TC dalam spec ini dijalankan dengan satu akun (Read Only); tidak ada penggantian akun. Aksi klik angka Used By (Items) oleh Total Control ada di spec `TC-GS-BRAND-E2E-042-used-by-items-link-detail-dan-hover`.
