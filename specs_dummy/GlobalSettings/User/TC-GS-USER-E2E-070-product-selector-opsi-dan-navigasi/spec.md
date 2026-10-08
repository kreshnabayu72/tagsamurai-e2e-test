---
id: TC-GS-USER-E2E-070-product-selector-opsi-dan-navigasi
title: 'Product Selector di User Detail: opsi produk dan navigasi ke Detail User produk lain'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-117
  - TC-GS-USER-118
  - TC-GS-USER-485
  - TC-GS-USER-545
coverage:
  web: automated
---

# Product Selector di User Detail: opsi produk dan navigasi ke Detail User produk lain

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, memiliki izin Read Settings > User di FAMS
- User "Ahmad Fauzi" punya Access ke Global Settings dan FAMS, dan sudah ter-provision di FAMS
- User "Wira Sendirian" hanya punya Access ke Global Settings dan tidak pernah punya produk lain di riwayat Access-nya
- User "Eka Dicabut" punya Access ke Global Settings saja sekarang, tetapi riwayat Changelog Field `Access` menyebut FAMS sebelum dicabut
- User "Fajar Baru" punya Access ke FAMS yang baru ditambahkan dan belum ter-provision di FAMS (belum pernah login ke produk itu)
- Spec ini tidak mengubah data

## Test Steps

### Ganti produk

1. Buka User Detail "Ahmad Fauzi" dan verifikasi selector "Viewing: [Global Settings ▾]" tampil dengan nilai default Global Settings
2. Buka selector dan verifikasi opsinya adalah Global Settings dan FAMS
3. Pilih FAMS
4. Verifikasi halaman berpindah penuh (bukan modal atau inline) ke Detail User FAMS untuk user yang sama, tanpa dialog konfirmasi, dengan tampilan asli modul FAMS

### Hanya produk yang pernah di-Access

5. Buka User Detail "Wira Sendirian" lalu buka selector
6. Verifikasi opsinya hanya Global Settings

### Access sudah dicabut tetapi tercatat di riwayat

7. Buka User Detail "Eka Dicabut" lalu buka selector
8. Verifikasi opsinya Global Settings dan FAMS, walau FAMS tidak ada di Access saat ini
9. Pilih FAMS dan verifikasi halaman berpindah penuh ke Detail User FAMS untuk user yang sama

### Produk belum ter-provision

10. Buka User Detail "Fajar Baru" lalu buka selector
11. Verifikasi opsi FAMS tetap tampil
12. Pilih FAMS
13. Verifikasi halaman berpindah ke Detail User FAMS dan tidak ada toast error, halaman 404, atau halaman error dari sisi Global Settings

## Notes

- Sumber `user.md` bagian 4.1, 4.2, dan 9.2 ([F-USER-16]). Opsi selector adalah produk yang ada di `access` user sekarang atau pernah tercatat di Changelog `Access`, dan produk itu punya modul Detail User sendiri.
- `TC-GS-USER-117` awalnya mengharapkan data di halaman yang sama ter-update. PRD tegas bahwa klik opsi adalah navigasi penuh, sehingga TC-nya diperbaiki (Changelog `tc-user.md` 2026-09-30 (9)).
- Tampilan Detail User FAMS untuk record yang belum ter-provision atau aksesnya sudah dicabut ditentukan modul FAMS dan tidak diverifikasi di sini.
- Sisi negatif matriks aktor dicakup `TC-GS-USER-E2E-071-product-selector-guard-aktor`.
