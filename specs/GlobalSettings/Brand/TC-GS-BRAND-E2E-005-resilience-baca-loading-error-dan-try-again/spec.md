---
id: TC-GS-BRAND-E2E-005-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca Tab Brand: Loading, Error Load, dan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-13
  - TC-GS-BRAND-17
  - TC-GS-BRAND-18
  - TC-GS-BRAND-172
  - TC-GS-BRAND-185
coverage:
  web: automated
---

# Resilience Baca Tab Brand: Loading, Error Load, dan Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client A (12 brand, data environment tetap), termasuk Vertex Labs (Used By (Items) = 5) untuk Modal Brand Detail. Spec tidak membuat data.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script:
  - Respons daftar Brand: tahan 3 detik lalu jawab normal (langkah 1 sampai 7, TC-GS-BRAND-13); jawab 500 (langkah 8 sampai 12, TC-GS-BRAND-17). Intercept 500 yang sama dilepas di langkah 13 sebelum [Try Again] (TC-GS-BRAND-18); tidak dibutuhkan intercept "500 sekali" terpisah.
  - Respons Changelog Brand: jawab 500 (TC-GS-BRAND-172).
  - Respons Detail Brand: dipasang di langkah 24 (tahan 3 detik lalu jawab 500) dan dilepas di langkah 29 sebelum [Try Again] (TC-GS-BRAND-185); tidak dibutuhkan intercept "500 sekali" terpisah.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` lalu menyetelnya ke true lewat API; hook `after` memulihkan nilai awal.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah, dan flag Guided Tooltip dipulihkan. Spec tidak mengubah data backend.

## Test Steps

### TC-GS-BRAND-13: Tampilan Loading saat data tabel diambil

1. Pasang intercept pada respons daftar Brand: tahan 3 detik
2. Buka Global Settings > Master Reference dari sidebar → tab Brand mulai dimuat
3. Verifikasi Skeleton loader tampil di area tabel
4. Tunggu respons diterima
5. Verifikasi data tabel tampil
6. Verifikasi Skeleton loader hilang
7. Lepas intercept respons daftar Brand

### TC-GS-BRAND-17: Error Load tabel saat pengambilan data gagal

8. Pasang intercept pada respons daftar Brand: jawab 500
9. Buka Tab Brand (muat ulang Global Settings > Master Reference)
10. Verifikasi area tabel menampilkan `"Unable to load this data."`
11. Verifikasi area tabel menampilkan `[Try Again]`
12. Verifikasi tidak ada baris parsial di tabel

### TC-GS-BRAND-18: Klik Try Again memuat ulang data setelah Error Load

13. Pulihkan respons normal pada respons daftar Brand (lepas intercept 500 dari TC-GS-BRAND-17)
14. Klik [Try Again]
15. Verifikasi Loading tampil
16. Verifikasi 10 baris termuat
17. Verifikasi pesan error `"Unable to load this data."` hilang

### TC-GS-BRAND-172: Error load Modal Changelog

18. Pasang intercept pada respons Changelog Brand: jawab 500
19. Klik icon Changelog
20. Verifikasi Modal Changelog menampilkan `"Unable to load this data."`
21. Verifikasi Modal Changelog menampilkan `[Try Again]`
22. Tutup Modal Changelog dengan `✕` di header
23. Lepas intercept respons Changelog Brand

### TC-GS-BRAND-185: Modal Brand Detail menampilkan Loading lalu Error load saat request gagal

24. Pasang intercept pada respons Detail Brand: tahan 3 detik lalu jawab 500 pada permintaan pertama
25. Pindah ke halaman 2 pada Pagination, lalu pilih row action `Detail` pada baris Vertex Labs
26. Verifikasi Skeleton loader tampil di Modal Brand Detail
27. Verifikasi Modal Brand Detail menampilkan `"Unable to load this data."`
28. Verifikasi Modal Brand Detail menampilkan `[Try Again]`
29. Pulihkan respons normal pada respons Detail Brand
30. Klik [Try Again]
31. Verifikasi retry memuat isi Detail Vertex Labs
32. Tutup Modal Brand Detail dengan `✕` di header

## Notes

- Mode: FE+BE (intercept parsial, kelas harness fault injection; bagian 6 konvensi). Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-BRAND-18 berdependensi TC-GS-BRAND-17, dan langkah 1 sampai 2 TC-GS-BRAND-18 (paksa 500, buka Tab Brand) identik dengan langkah 8 sampai 9 spec ini; spec melanjutkan state Error Load dari TC-GS-BRAND-17 tanpa membuka ulang tab, lalu memulihkan respons di langkah 13 sebelum [Try Again].
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 (menunggu respons), 7 dan 23 (lepas intercept), 22 dan 32 (tutup modal), 25 (pindah ke halaman 2 tempat baris Vertex Labs berada; 12 brand urut A-Z dengan 10 per halaman).
- Nama endpoint tidak disebut di TC sumber; kebutuhan ini sudah dicatat di Prerequisites.
