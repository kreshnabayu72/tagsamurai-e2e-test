---
id: TC-GS-BRAND-E2E-006-resilience-export-gagal-download
title: "Resilience Export: Kegagalan Download Brand, Changelog, dan Accordion Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-167
  - TC-GS-BRAND-183
  - TC-GS-BRAND-195
  - TC-GS-BRAND-249
coverage:
  web: automated
---

# Resilience Export: Kegagalan Download Brand, Changelog, dan Accordion Detail

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan penyuntikan kegagalan pembuatan file di browser).
- Akun aktor 1 (awal spec): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before`. Dipakai untuk TC-GS-BRAND-167, TC-GS-BRAND-183, dan TC-GS-BRAND-195.
- Akun aktor 2 (ganti akun di langkah 22 dan 23): Total Control Principal (Hendra Wijaya) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`). Dipakai untuk TC-GS-BRAND-249 pada Instance Principal. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`) karena spec berakhir di Principal. Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` dan `GS_PRINCIPAL_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup (data environment tetap, hanya dibaca): Client A memiliki Vertex Labs dengan Item Type List; Principal memiliki Signal One dengan Device SKU List (SKU-HR-001, SKU-TB-002, SKU-GW-003). Spec tidak membuat data.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script:
  - Respons export daftar Brand (Download as CSV): jawab 500 (TC-GS-BRAND-167).
  - Respons export Changelog Brand (Download as CSV): jawab 500 (TC-GS-BRAND-183).
- Kemampuan teknis yang diminta ke tim FE: menyuntikkan kegagalan pembuatan file di sisi browser (mis. membuat penulis CSV/Blob/`URL.createObjectURL` melempar error pada Download as CSV di accordion Item Type List dan Device SKU List), serta mengamati bahwa tidak ada file terunduh (event download browser). TC-GS-BRAND-195 dan TC-GS-BRAND-249 bertanda Manual Only di TC sumber, tetapi kebutuhan ini dicatat di sini sebagai sumber resmi (bagian 2 konvensi).
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` untuk kedua akun lalu menyetelnya ke true lewat API; hook `after` memulihkan nilai awal.
- Pemulihan di hook `after`: semua intercept dan penyuntikan kegagalan pembuatan file dilepas walau spec gagal di tengah; flag Guided Tooltip dipulihkan; sesi dikembalikan ke akun default suite. Spec tidak mengubah data backend.

## Test Steps

### TC-GS-BRAND-167: Download gagal menampilkan toast error

1. Buka Global Settings > Master Reference dari sidebar → tab Brand tampil
2. Pasang intercept pada respons export daftar Brand: jawab 500
3. Klik icon Download
4. Pilih Download as CSV
5. Verifikasi toast error: "Error, failed to download Brand-List."
6. Verifikasi tidak ada file terunduh
7. Verifikasi tabel tetap tampil
8. Lepas intercept respons export daftar Brand

### TC-GS-BRAND-183: Download Changelog gagal

9. Klik icon Changelog untuk membuka Modal Changelog
10. Pasang intercept pada respons export Changelog Brand: jawab 500
11. Pilih Download as CSV pada Modal Changelog
12. Verifikasi toast error: "Error, failed to download Changelog-Brand."
13. Lepas intercept respons export Changelog Brand
14. Tutup Modal Changelog dengan `✕` di header

### TC-GS-BRAND-195: Download accordion Item Type List gagal

15. Pindah ke halaman 2 pada Pagination, lalu buka Detail Vertex Labs lewat row action `Detail`
16. Expand accordion Item Type List
17. Aktifkan penyuntikan kegagalan pembuatan file di browser
18. Pilih Download as CSV pada accordion Item Type List
19. Verifikasi toast error: "Error, failed to download Item Types - Vertex Labs."
20. Matikan penyuntikan kegagalan pembuatan file
21. Tutup Modal Brand Detail dengan `✕` di header

### Ganti akun ke Principal

22. Logout dari Total Control Client A
23. Login sebagai Total Control Principal

### TC-GS-BRAND-249: Download accordion Device SKU List gagal

24. Buka Global Settings > Master Reference > Brand
25. Aktifkan penyuntikan kegagalan pembuatan file di browser
26. Buka Detail Signal One lewat row action `Detail`
27. Expand accordion Device SKU List
28. Pilih Download as CSV pada accordion Device SKU List
29. Verifikasi toast error: "Error, failed to download Device SKUs - Signal One."
30. Verifikasi tidak ada file terunduh
31. Matikan penyuntikan kegagalan pembuatan file

## Notes

- Mode: FE+BE (intercept parsial dan penyuntikan kegagalan di browser; kelas harness fault injection, bagian 3 prinsip 13b). Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-BRAND-167 dan TC-GS-BRAND-183 sama-sama kegagalan respons export (500) dan bisa dipicu lewat intercept HTTP; TC-GS-BRAND-195 dan TC-GS-BRAND-249 kegagalan pembuatan file di sisi klien sehingga butuh penyuntikan di browser (bukan intercept respons).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 13, 20, dan 31 (lepas intercept atau matikan penyuntikan), 9 dan 14 (buka dan tutup Modal Changelog sebagai konteks Download as CSV TC-GS-BRAND-183), 15 dan 21 (pindah ke halaman 2 tempat baris Vertex Labs berada, 12 brand urut A-Z dengan 10 per halaman, lalu buka dan tutup Modal Brand Detail Vertex Labs), 22 dan 23 (ganti akun ke Principal).
- TC-GS-BRAND-195 pada TC sumber menyebut "Download as CSV dari Detail Vertex Labs" tanpa menyebut accordion; judul TC dan toast ("Item Types - Vertex Labs") menunjukkan accordion Item Type List, sehingga spec meng-expand accordion tersebut (langkah 16). Hal ini sudah dicatat sebagai kebutuhan di Prerequisites (accordion dan penyuntikan di browser).
- Pada TC-GS-BRAND-249 pengecekan "tidak ada file terunduh" memakai event download browser.
- Spec memakai dua entity (Client A lalu Principal) dengan Step ganti akun eksplisit; bagian Principal tetap bermakna walau bagian Client A gagal.
