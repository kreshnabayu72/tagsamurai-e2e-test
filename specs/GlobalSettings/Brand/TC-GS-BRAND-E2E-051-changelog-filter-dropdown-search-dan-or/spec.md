---
id: TC-GS-BRAND-E2E-051-changelog-filter-dropdown-search-dan-or
title: "Changelog Brand: Filter per Field, Pencarian di Dropdown, dan Logika AND/OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-175
  - TC-GS-BRAND-176
  - TC-GS-BRAND-177
  - TC-GS-BRAND-178
  - TC-GS-BRAND-284
coverage:
  web: automated
---

# Changelog Brand: Filter per Field, Pencarian di Dropdown, dan Logika AND/OR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Akun seeding tambahan (hanya untuk seeding API di hook `before`, bukan login UI):
  - Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_CREATE_PASSWORD`.
  - Update+Read, Agus Wijaya (`Agus W`), `updateOnly_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_UPDATE_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API di hook `before`, urutan sebagai berikut):
  - Population D-01 oleh Sari Dewi: 12 brand dengan nama literal `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics` (setara TC-GS-BRAND-1). Seed idempotent: nama yang sudah ada dilewati. Menghasilkan entri Create oleh `Sari D`. Dipakai TC-GS-BRAND-176 (`Apex Tools`) dan sebagai sumber entri Create oleh `Sari D` untuk TC-GS-BRAND-175.
  - Brand `Apex Tools {runId}-051` dibuat oleh Sari Dewi (entri Create oleh `Sari D` yang unik per run; dipakai TC-GS-BRAND-178, 284).
  - Brand `Log Edit Co {runId}-051` dibuat oleh Rina Marlina (entri Create oleh `Rina M`), lalu diubah namanya oleh Agus Wijaya menjadi `Log Edit Co Renamed {runId}-051` (entri Action Edit oleh `Agus W`).
  - Brand `Log Del Co {runId}-051` dibuat oleh Sari Dewi lalu dihapus oleh Sari Dewi (entri Action Delete, setara TC-GS-BRAND-95; brand sudah terhapus tetapi punya log).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus oleh Sari Dewi lewat API brand Population yang dibuat oleh spec ini (yang sudah ada sebelum spec dilewati), `Apex Tools {runId}-051`, dan `Log Edit Co Renamed {runId}-051`. Entri Changelog tidak bisa dihapus.
- Data tidak dibuat atau diubah oleh langkah spec ini; semua perubahan ada di `before`/`after`.
- Kemampuan teknis: kontrol date range picker (memilih hari uji); mengetik di kotak search di dalam dropdown filter.
- State global yang disyaratkan: log Client A hanya berisi Action Create, Delete, Edit (langkah 8), dan `Maya Putri` serta `Fajar Nugroho` tidak pernah memutasi brand Client A (langkah 13 dan 14).
- Nama yang tidak boleh muncul di opsi Modified By (hanya dirujuk sebagai nama, tidak ada login): `Maya Putri` (Read Only, `readOnly_automated_qaTeam1@qwertysystem.net`) dan `Fajar Nugroho` (Tanpa Capability, `noCapability_automated_qaTeam1@qwertysystem.net`).
- Precondition TC-GS-BRAND-175, 176, 177, 178, 284: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand. TC-GS-BRAND-284 tambahan: entri Create oleh Sari D (Population) dan entri Delete tersedia (TC-GS-BRAND-95).
- State global yang dipulihkan: tidak ada.

## Test Steps

### TC-GS-BRAND-175: Screening Filter Panel Changelog dan isi opsi

1. Klik icon Changelog di halaman Global Settings > Master Reference > Brand → modal Changelog tampil
2. Klik Filter → Filter Panel Changelog tampil
3. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
4. Verifikasi field `Action` dengan placeholder `All actions`
5. Verifikasi field `Brand Name` dengan placeholder `All brands`
6. Verifikasi field `Modified By` dengan placeholder `All users`
7. Buka dropdown Action
8. Verifikasi opsi Action hanya nilai yang ada di log: Create, Delete, Edit
9. Buka dropdown Brand Name
10. Verifikasi opsi Brand Name memuat `Log Del Co {runId}-051` (brand yang sudah dihapus tetapi punya log)
11. Buka dropdown Modified By
12. Verifikasi opsi Modified By memuat `Sari D`, `Rina M`, dan `Agus W` (user yang pernah mengubah brand)
13. Verifikasi opsi Modified By tidak memuat `Maya Putri`
14. Verifikasi opsi Modified By tidak memuat `Fajar Nugroho`

### TC-GS-BRAND-176: Filter Changelog per field multi-select

15. Pilih Action `Delete`, klik [Apply]
16. Verifikasi tabel hanya memuat baris Action Delete
17. Klik Filter, uncheck Action `Delete`
18. Pilih Brand Name `Apex Tools`, klik [Apply]
19. Verifikasi tabel hanya memuat baris Brand Name `Apex Tools`
20. Klik Filter, uncheck Brand Name `Apex Tools`
21. Pilih Modified By `Sari D`, klik [Apply]
22. Verifikasi tabel hanya memuat baris Modified By `Sari D`

### TC-GS-BRAND-177: Filter Date Changelog

23. Klik Filter, uncheck Modified By `Sari D`
24. Pilih Date hari uji (rentang tanggal hari uji pada date range), klik [Apply]
25. Verifikasi tabel hanya memuat baris dengan tanggal hari uji

### TC-GS-BRAND-178: Kombinasi Filter Action dan Brand Name berlogika AND

26. Klik Filter, kosongkan Date
27. Pilih Action `Create` dan Brand Name `Apex Tools {runId}-051`, klik [Apply]
28. Verifikasi tabel memuat satu baris: Create `Apex Tools {runId}-051`

### TC-GS-BRAND-284: Search di dalam dropdown dan logika OR dalam satu field filter Changelog

29. Klik Filter, kosongkan seluruh pilihan field Date, Action, Brand Name, dan Modified By
30. Buka dropdown Brand Name, ketik `TOOLS {runId}-051` seluruhnya dalam huruf besar (potongan nama brand) pada kotak search di dalam dropdown
31. Verifikasi daftar opsi hanya memuat brand yang namanya memuat teks ketikan (`Apex Tools {runId}-051`; tidak membedakan huruf besar kecil)
32. Ketik `zzqx` pada kotak search yang sama
33. Verifikasi daftar opsi kosong, tanpa opsi cocok
34. Kosongkan kotak search, tutup dropdown
35. Pilih Action `Create` dan `Delete`, klik [Apply]
36. Verifikasi tabel memuat baris Action `Create`
37. Verifikasi tabel memuat baris Action `Delete` (gabungan OR dalam satu field)
38. Verifikasi tidak ada baris Action `Edit`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Changelog dibuka sekali (langkah 1) dan Filter Panel dibuka ulang lewat Filter setelah tiap [Apply]. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, membersihkan state filter dari TC sebelumnya): langkah 17, 20, 23, 26, 29.
- Langkah 28 (satu baris Create) memakai `Apex Tools {runId}-051` bersuffix per run, sehingga jumlah baris tidak bergantung pada entri Population dari run atau spec lain. Langkah 30 mengetik potongan nama di tengah (`TOOLS {runId}-051`) agar sifat substring dan tidak membedakan huruf besar kecil teruji dan hanya satu opsi cocok.
- Langkah 18-19 memakai `Apex Tools` literal sesuai Data Uji TC-GS-BRAND-176 (Population D-01); Expected b tidak menghitung jumlah baris, sehingga stabil. Langkah 28 dan 30 memakai brand bersuffix karena TC-GS-BRAND-178 dan 284 menulis `Apex Tools {runId}`.
- Langkah 8 mengasumsikan log Client A hanya berisi Action Create, Delete, Edit (Expected b TC-GS-BRAND-175); kebutuhan ini tercatat di Prerequisites.
- Temuan untuk QA: kata "hanya" pada Expected d TC-GS-BRAND-175 (Sari D, Rina M, Agus W) tidak stabil di environment bersama karena aktor lain dapat memutasi brand Client A; yang diasersikan adalah memuatnya tiga nama (langkah 12) dan tidak memuat Maya Putri serta Fajar Nugroho (langkah 13 dan 14), syarat keduanya ada di Prerequisites.
