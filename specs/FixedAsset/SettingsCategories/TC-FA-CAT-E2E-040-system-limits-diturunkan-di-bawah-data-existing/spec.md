---
id: TC-FA-CAT-E2E-040-system-limits-diturunkan-di-bawah-data-existing
title: "System Limits Diturunkan di Bawah Data Existing: Non-retroaktif, Tanpa Excess, Hanya Add yang Diblok"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-582
coverage:
  web: automated
---

# System Limits Diturunkan di Bawah Data Existing: Non-retroaktif, Tanpa Excess, Hanya Add yang Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20 dengan seed tambahan Pre-setup #42), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) mengubah System Limits di Admin Console > Plans & Licensing > Lifecycle Settings.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #42 (seed tambahan lewat skrip/API, disediakan tim FE/BE): 1.100 kategori L1 `Mass 0001` sampai `Mass 1100` dan rantai `Deep 1` > `Deep 2` > `Deep 3` > `Deep 4` > `Deep 5` > `Deep 6` (depth 6). Principal menurunkan limit setelah data terisi.
- Data milik spec: kategori L1 leaf `Edit Target {runId}-040` (seed lewat API di hook `before`) sebagai target Edit varian A. Target Edit varian B adalah Pre-setup #42 `Deep 6`; hook `after` memulihkan Description `Deep 6` ke nilai awal (efek: Last Updated dan baris Changelog Edit `Deep 6`).
- State global yang diubah: Master Data Count Limit dan Hierarchy Depth Limit CatMain. Hook `after` mengembalikan keduanya ke default (Master Data Count Limit default, Hierarchy Depth Limit default) walau spec gagal di tengah. Suite berjalan serial.
- Kemampuan teknis: membaca jumlah kategori client lewat seed API (disediakan tim FE/BE; TC tidak menyebut cara membaca jumlah).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### Varian A: Master Data Count Limit 1.000 dengan data lebih dari 1.000

1. Principal Automation menurunkan Master Data Count Limit CatMain menjadi 1.000 di System Limits hingga tersimpan (data tetap lebih dari 1.000 kategori)
2. Tunggu aksi selesai
3. Klik menu Fixed Asset > Settings > Categories untuk membuka ulang halaman
4. Ketik Search `Mass 1100`, tekan Enter
5. Verifikasi baris `Mass 1100` tampil (seluruh kategori seed tetap tampil)
6. Klik `(←)` pada kotak Search
7. Verifikasi tidak ada node Excess pada sidebar dan tabel (tidak redup, tanpa tooltip Excess)
8. Verifikasi Alert Category Consolidation tidak tampil
9. Catat jumlah kategori client (baseline)
10. Klik elipsis (⋯) pada baris `Edit Target {runId}-040` > `Edit`
11. Ubah Description menjadi `Still editable`
12. Klik `[Save]`
13. Verifikasi toast `Success, category has been updated.` tampil
14. Klik `[+] Category` pada sidebar
15. Verifikasi dialog 🔒 `Cannot Add Category` · `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.` · `[OK]` tampil
16. Klik `[OK]`
17. Verifikasi jumlah kategori tidak bertambah dari baseline

### Varian B: Hierarchy Depth Limit 5 dengan data depth 6

18. Principal Automation mengembalikan Master Data Count Limit CatMain ke default lalu menurunkan Hierarchy Depth Limit menjadi 5 hingga tersimpan
19. Tunggu aksi selesai
20. Muat ulang halaman Categories dan expand rantai `Deep 1` sampai `Deep 6` di sidebar
21. Verifikasi `Deep 6` pada depth 6 tetap ada tanpa status Excess
22. Klik elipsis (⋯) pada node `Deep 6` > `Edit`
23. Ubah Description menjadi `Still editable`
24. Klik `[Save]`
25. Verifikasi toast `Success, category has been updated.` tampil
26. Klik elipsis (⋯) pada node `Deep 5` (depth 5) > `+ Add Subcategory`
27. Verifikasi dialog 🔒 `Cannot Add Category` · `You've reached the platform limit of 5 levels. Contact support if you need a higher limit.` · `[OK]` tampil
28. Klik `[OK]`
29. Klik elipsis (⋯) pada node `Deep 4` (depth 4) > `+ Add Subcategory`
30. Verifikasi popup New Subcategory terbuka tanpa dialog blok
31. Klik `✕` pada popup
32. Buka Modal Changelog
33. Verifikasi Modal Changelog memuat baris Edit Description untuk `Edit Target {runId}-040` (anchor)
34. Verifikasi Modal Changelog tidak memuat baris `Marked as Excess (Category Consolidation)` akibat penurunan limit
35. Tutup Modal Changelog

## Notes

- Alasan di atas sekitar 35 langkah / `P-1` (state berat): konteks varian A dan B bergantung pada state berat Pre-setup #42 (1.100 kategori dan rantai depth 6) dan penurunan limit berurutan; asersi absence Changelog (langkah 34) milik TC yang sama dan bergantung pada state itu, dengan baris Edit di langkah 33 sebagai anchor positif.
- Langkah penghubung (S-03): langkah 2, 19 (menunggu aksi API), 3, 6, 20 (navigasi/membersihkan Search), 16, 28 (menutup dialog), 31, 35 (menutup popup/modal).
- Pelaku kedua lewat sesi API bukan konteks kedua (tanpa `P-2`); langkah 1 dan 18 ditulis "... hingga ... tersimpan" (R-20).
- Target Edit varian A memakai `Edit Target {runId}-040` milik spec menggantikan `Furniture` pada TC agar Pre-setup #20 tidak berubah (S-06).
- Post Condition TC ("limit dikembalikan ke default") dijalankan hook `after` dan tidak diasersi (S-01).
- Temuan untuk QA:
  - TC-582 tidak menyebut cara membaca jumlah kategori untuk "jumlah kategori tidak bertambah"; spec memakai pembacaan lewat seed API yang disediakan tim FE/BE.
  - TC-582 "seluruh kategori seed tetap tampil" tidak dapat diverifikasi per baris di UI; spec memakai Search atas baris seed terakhir (`Mass 1100`).
  - TC-582 mengubah dua limit berurutan; Principal mengembalikan Master Data Count Limit ke default pada langkah 18 sesuai TC.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
