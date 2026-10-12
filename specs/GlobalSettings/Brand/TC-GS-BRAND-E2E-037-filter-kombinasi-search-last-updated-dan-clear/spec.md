---
id: TC-GS-BRAND-E2E-037-filter-kombinasi-search-last-updated-dan-clear
title: "Filter Last Updated, Kombinasi Search dan Filter, serta Clear Filter pada Tabel Brand"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-141
  - TC-GS-BRAND-142
  - TC-GS-BRAND-143
  - TC-GS-BRAND-144
  - TC-GS-BRAND-150
coverage:
  web: automated
---

# Filter Last Updated, Kombinasi Search dan Filter, serta Clear Filter pada Tabel Brand

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment): 12 brand Client A dengan Last Updated sebelum hari uji (Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp).
- Data Dinamis: Population D-01 (12 brand: `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics`) di-seed lewat API di hook `before` (setara TC-GS-BRAND-1) dengan nama literal sesuai TC-GS-BRAND-1, sehingga Last Updated Population = hari uji dan total tabel 24 brand. Population dihapus lewat API di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh. Nama literal disengaja (asersi Search dan urutan bergantung pada nama Population; pengecualian S-12): seed idempotent (dilewati bila sudah ada), cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial.
- Date Format General Settings memakai nilai default environment; spec ini tidak mengubah state global apa pun.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand, tab Brand.
- Kemampuan teknis: tidak ada yang khusus.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-141: Filter Last Updated rentang tanggal

2. Buka Filter, isi Last Updated dengan rentang hari uji – hari uji (hari ini – hari ini)
3. Verifikasi input Filter Last Updated menampilkan tanggal sesuai Date Format General Settings
4. Klik [Apply]
5. Verifikasi hanya brand yang dibuat atau diubah pada hari uji (Population dan data dinamis) yang tampil; brand Pre-setup tidak tampil

### TC-GS-BRAND-142: Kombinasi Filter Used By (Items) dan Last Updated berlogika AND

6. Buka Filter, isi Used By (Items) Min `2` Max `2`, pastikan Last Updated tetap hari uji – hari uji, lalu klik [Apply]
7. Verifikasi empty state `No results found` (Last Updated Duo Brand dan Kestrel sebelum hari uji)

### TC-GS-BRAND-143: Search lalu Filter menghasilkan irisan

8. Kosongkan seluruh filter (Used By (Items) dan Last Updated), lalu klik [Apply]
9. Search `co`, tekan Enter
10. Buka Filter, isi Used By (Items) Min `1` Max `1`, lalu klik [Apply]
11. Verifikasi tabel hanya berisi Acme Corp, Northwind Co, Zenith Corp (brand yang namanya memuat `co` dan berangka `1`)
12. Verifikasi keyword `co` tetap terisi di kolom Search

### TC-GS-BRAND-144: Filter lalu Search menghasilkan irisan

13. Hapus keyword Search dan kosongkan filter Used By (Items), lalu klik [Apply]
14. Buka Filter, isi Used By (Items) Min `5`, lalu klik [Apply]
15. Search `ver`, tekan Enter
16. Verifikasi tabel hanya berisi Vertex Labs
17. Verifikasi filter Used By (Items) Min `5` tetap aktif

### TC-GS-BRAND-150: Clear filter dan pemulihan empty state

18. Hapus keyword Search dan kosongkan filter Used By (Items), lalu klik [Apply]
19. Search `acme`, tekan Enter
20. Buka Filter, isi Used By (Items) Min `5` Max `5`, lalu klik [Apply]
21. Verifikasi empty state `No results found` (Acme Corp = 1, di luar rentang)
22. Kosongkan filter Used By (Items), lalu klik [Apply]
23. Verifikasi Acme Corp tampil di tabel
24. Verifikasi keyword Search `acme` tetap aktif

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung: langkah 8, 13, dan 18 mengosongkan filter dan keyword Search yang tersisa dari TC sebelumnya supaya TC berikutnya mulai dari state bersih (tanpa buka layar tambahan).
- Dependensi TC-GS-BRAND-1 pada TC-141 dan TC-142 dipenuhi spec ini sendiri lewat seeding Population di hook `before`, tidak menumpang spec lain.
