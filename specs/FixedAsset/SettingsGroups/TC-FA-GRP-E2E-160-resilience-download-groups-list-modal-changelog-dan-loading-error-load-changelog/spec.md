---
id: TC-FA-GRP-E2E-160-resilience-download-groups-list-modal-changelog-dan-loading-error-load-changelog
title: "Resilience: Download Groups List Gagal, Download Modal Changelog Gagal, dan Loading/Error Load Modal Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-411
  - TC-FA-GRP-431
  - TC-FA-GRP-514
coverage:
  web: automated
---

# Resilience: Download Groups List Gagal, Download Modal Changelog Gagal, dan Loading/Error Load Modal Changelog

## Prerequisites

- Mode: FE+BE (intercept parsial respons HTTP 5xx di atas backend nyata, bagian 6 konvensi).
- Kelas harness: b (fault injection) untuk seluruh TC; tiga TC kegagalan server dalam satu spec resilience.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE): intercept respons 5xx untuk (a) endpoint unduhan Groups List, (b) endpoint unduhan Changelog-Group, dan (c) endpoint pemuatan data Modal Changelog. Nama endpoint tidak tertulis di TC/PRD/LLD (APISpec modul kosong); spec tidak menyebut endpoint karangan. Intercept dilepas segera setelah pemicu selesai (S-09). Penangkapan berkas unduhan browser.
- Data: memakai data Pre-setup yang tampil (Groups List dan Changelog client); spec tidak membuat atau mengubah data.
- Cleanup: tidak ada data milik spec; hook `after` melepas intercept bila masih terpasang.

## Test Steps

### TC-FA-GRP-411: Download Groups List gagal

1. Catat nama baris halaman 1 tabel Groups List
2. Pasang intercept respons 5xx pada endpoint unduhan Groups List
3. Klik icon Download
4. Klik `Download as CSV`
5. Verifikasi toast error `Error, failed to download Groups.` tampil
6. Verifikasi tidak ada berkas terunduh
7. Verifikasi tabel tetap seperti semula: nama baris halaman 1 sama dengan yang dicatat pada langkah 1
8. Lepas intercept pada endpoint unduhan Groups List

### TC-FA-GRP-431: Loading dan error load Modal Changelog

9. Pasang intercept respons 5xx pada endpoint pemuatan data Modal Changelog
10. Klik icon Changelog
11. Verifikasi area tabel modal menampilkan teks `Unable to load this data.` dan tombol [Try Again]
12. Lepas intercept pada endpoint pemuatan data Modal Changelog
13. Klik [Try Again]
14. Verifikasi sedikitnya satu baris data tampil pada tabel modal

### TC-FA-GRP-514: Download Modal Changelog gagal

15. Catat nama baris halaman 1 tabel Modal Changelog
16. Pasang intercept respons 5xx pada endpoint unduhan Changelog-Group
17. Klik icon Download
18. Klik `Download as CSV`
19. Verifikasi toast error `Error, failed to download Changelog-Group.` tampil
20. Verifikasi tidak ada berkas terunduh
21. Verifikasi tabel modal tetap seperti semula: nama baris halaman 1 sama dengan yang dicatat pada langkah 15
22. Lepas intercept pada endpoint unduhan Changelog-Group
23. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mencatat nama baris halaman 1 (langkah 1 dan 15), memasang dan melepas intercept, serta menutup Modal Changelog (S-03, S-09).
- Spec kelas b (fault injection). Pemicu intercept hanya membentuk kegagalan; asersi terbatas pada perilaku FE atas respons 5xx (toast, tidak ada berkas, tabel tetap) dan state tampilan.
- TC-FA-GRP-431 berjudul "loading & error load" tetapi Langkah dan Expected hanya memuat state error dan [Try Again]; state loading tidak punya langkah atau Expected sehingga tidak diasersi.
- Temuan untuk QA:
  - Nama endpoint unduhan Groups List, unduhan Changelog-Group, dan pemuatan data Modal Changelog tidak tertulis di TC, PRD, atau LLD (APISpec kosong); disediakan tim FE.
  - TC-FA-GRP-431 berjudul "loading & error load" tetapi tidak memuat langkah atau Expected untuk state loading.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD`; perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
