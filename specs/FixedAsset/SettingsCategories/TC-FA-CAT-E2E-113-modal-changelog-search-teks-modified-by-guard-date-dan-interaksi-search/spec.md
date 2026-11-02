---
id: TC-FA-CAT-E2E-113-modal-changelog-search-teks-modified-by-guard-date-dan-interaksi-search
title: "Modal Changelog: Search Kolom Teks dan Modified By, Guard Kolom Date, dan Interaksi Kotak Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-394
  - TC-FA-CAT-395
  - TC-FA-CAT-396
  - TC-FA-CAT-584
coverage:
  web: automated
---

# Modal Changelog: Search Kolom Teks dan Modified By, Guard Kolom Date, dan Interaksi Kotak Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain) dan #23 (Changelog CatMain), hanya dibaca dan tidak diubah: 12 baris riwayat sesuai Example Data PRD §4.1, termasuk baris Marked dan Restored as Excess, Create `Electronics` dan `Electronics › Laptop`, Edit Description `Furniture` (Old Value `Office furniture`), rename `Laptop` ke `Notebook`, dan baris Modified By `Sarah T` (nama lengkap `Sarah Taylor`). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-394: Search pada kolom teks log

1. Klik icon Changelog di Table Tools
2. Ketik Search `excess`, tekan Enter
3. Verifikasi pencarian `excess` menemukan baris `Marked as Excess (Category Consolidation)` dan `Restored from Excess (Category Consolidation)` (substring case-insensitive)
4. Ganti isi kotak search dengan `Electronics`, tekan Enter
5. Verifikasi pencarian `Electronics` menemukan baris dengan path `Electronics` dan `Electronics › Laptop`
6. Ganti isi kotak search dengan `Description`, tekan Enter
7. Verifikasi pencarian `Description` menemukan baris Field `Description`
8. Ganti isi kotak search dengan `Office furniture`, tekan Enter
9. Verifikasi pencarian `Office furniture` menemukan baris Edit Description `Furniture`
10. Ganti isi kotak search dengan `Notebook`, tekan Enter
11. Verifikasi pencarian `Notebook` menemukan baris rename `Laptop` ke `Notebook`

### TC-FA-CAT-395: Search pada Modified By

12. Ganti isi kotak search dengan `sarah`, tekan Enter
13. Verifikasi baris dengan Modified By `Sarah T` (nama lengkap `Sarah Taylor`) ditemukan

### TC-FA-CAT-396: Guard kolom Date

14. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search dan memuat seluruh baris
15. Catat nilai Date baris pertama
16. Ketik Search dengan nilai Date baris pertama, tekan Enter
17. Verifikasi Title `No results found` tampil (kolom Date tidak dapat dicari lewat Search; penyaringan tanggal hanya lewat Filter Panel)

### TC-FA-CAT-584: Interaksi kotak Search

18. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search
19. Catat jumlah baris yang tampil pada halaman pertama (baseline)
20. Hover icon Search di toolbar modal
21. Verifikasi tooltip icon `Search`
22. Klik icon Search
23. Verifikasi input melebar (reveal)
24. Verifikasi kursor langsung fokus pada input
25. Verifikasi placeholder `Search action, category name, field...`
26. Ketik `Electronics` tanpa menekan `Enter`
27. Verifikasi icon (✕) muncul pada input
28. Verifikasi tabel belum tersaring (jumlah baris sama dengan baseline langkah 19)
29. Tekan `Enter`
30. Verifikasi tabel hanya memuat baris yang cocok dengan `Electronics`
31. Klik icon (✕) pada input
32. Verifikasi input kosong dan hasil terakhir (baris `Electronics`) dipertahankan
33. Tekan `Enter` pada input kosong
34. Verifikasi tabel kembali memuat semua baris (jumlah baris sama dengan baseline langkah 19)
35. Ketik `Vehicle`, tekan `Enter`
36. Klik icon panah (←) di kiri toolbar
37. Verifikasi kotak pencarian menutup menjadi icon Search biasa
38. Verifikasi keyword kosong
39. Verifikasi tabel langsung memuat seluruh baris tanpa menekan `Enter`

## Notes

- Langkah penghubung (S-03): langkah 14 dan 18 (menutup kotak Search untuk mengembalikan tabel penuh sebelum TC berikutnya, S-09), 15 dan 19 (mencatat baseline).
- Ambang sekitar 35 langkah terlampaui (39 langkah). Alasan: seluruh TC satu surface (Modal Changelog), satu dataset (Pre-setup #20 dan #23), dan satu kelas harness (fungsional Search); tiap TC berdiri sendiri dan kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-396 tidak menyebut format nilai Date yang diketik; spec memakai nilai teks Date baris pertama sebagaimana tampil di tabel (langkah 15 dan 16).
  - TC-584 butir d menyebut "tabel kembali memuat semua baris baru saat `Enter` pada input kosong"; spec membandingkan jumlah baris dengan baseline halaman pertama.
  - TC-395 menyebut Pre-setup #23 memuat baris `Sarah T` tetapi Data Uji #23 tidak menyebutnya secara eksplisit; spec mengandalkan baris itu ada pada Pre-setup #23.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
