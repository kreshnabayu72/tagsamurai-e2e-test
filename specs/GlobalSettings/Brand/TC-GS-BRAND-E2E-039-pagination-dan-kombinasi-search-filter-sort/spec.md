---
id: TC-GS-BRAND-E2E-039-pagination-dan-kombinasi-search-filter-sort
title: "Pagination Tabel Brand dan Kombinasi Search, Filter, Sort, serta Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-149
  - TC-GS-BRAND-152
coverage:
  web: automated
---

# Pagination Tabel Brand dan Kombinasi Search, Filter, Sort, serta Page Size

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment): 12 brand Client A dengan Last Updated sebelum hari uji.
- Data Dinamis: Population D-01 (12 brand: `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics`) di-seed lewat API di hook `before` (setara TC-GS-BRAND-1) dengan nama literal; total tabel 24 brand, 10 per halaman secara default. Dihapus lewat API di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh. Nama literal disengaja (asersi Search dan urutan bergantung pada nama Population; pengecualian S-12): seed idempotent (dilewati bila sudah ada), cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial.
- State global: tidak ada yang diubah. Page size dikembalikan ke 10 dan filter/search dikosongkan di hook `after` (preferensi UI).
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: tidak ada yang khusus.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-152: Pagination: page size, next/prev, dan kembali ke halaman 1 saat kriteria berubah

2. Klik Next
3. Verifikasi tabel berpindah ke halaman 2
4. Ubah page size 25
5. Verifikasi 24 baris tampil dalam 1 halaman
6. Ubah page size 10
7. Pindah ke halaman 2
8. Search `a`, tekan Enter
9. Verifikasi tabel kembali ke halaman 1
10. Hapus keyword Search, tekan Enter

### TC-GS-BRAND-149: Kombinasi Search, Filter, Sort, dan page size

11. Search `e`, tekan Enter
12. Buka Filter, isi Last Updated hari uji, lalu klik [Apply]
13. Sort Brand Name descending (klik header Brand Name dua kali)
14. Verifikasi keyword `e` dan filter Last Updated hari uji tetap aktif setelah sort
15. Ubah page size 25
16. Verifikasi hasil = Population yang namanya memuat `e`, urut Z-A, dalam satu halaman
17. Verifikasi keyword `e` dan filter Last Updated hari uji tetap aktif setelah ganti page size

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec: 152 lalu 149 (TC-GS-BRAND-152 memulai dari state tanpa search/filter; TC-GS-BRAND-149 mengakhiri dengan page size 25). Dependensi TC-GS-BRAND-1 dipenuhi lewat seeding Population di hook `before`.
- Langkah penghubung: langkah 10 (menghapus keyword Search dari TC-GS-BRAND-152 sebelum TC-GS-BRAND-149 mengandalkan state tanpa search).
