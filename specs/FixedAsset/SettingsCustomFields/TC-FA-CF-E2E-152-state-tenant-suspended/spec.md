---
id: TC-FA-CF-E2E-152-state-tenant-suspended
title: "State Tenant: Aksi Tulis Ditolak Saat Suspended"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-585
  - TC-FA-CF-586
  - TC-FA-CF-587
  - TC-FA-CF-588
  - TC-FA-CF-592
coverage:
  web: automated
---

# State Tenant: Aksi Tulis Ditolak Saat Suspended

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor blok pertama: Total Control Client Suspended (Pre-setup #22). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_SUSPENDED_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite.
- Akun aktor blok kedua (ganti akun eksplisit di langkah 37 dan 38): Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Client Suspended (Pre-setup #22): entitas Suspended dengan field baseline Pre-setup #12 (`Storage Capacity`, `Asset Serial Tag`, `Legacy Tag`, `Compliance File`). Company Alpha (Pre-setup #11 dan #12) berstatus Active saat awal blok kedua. Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE). Semua aksi tulis ditolak sehingga data Pre-setup tidak berubah (S-06).
- Data Dinamis: Field Name hasil Edit yang ditolak `Susp Edit {runId}-152`.
- Kemampuan teknis: seed status Client (ubah Company Alpha menjadi Suspended saat sesi berjalan, pemicu state; disediakan tim FE/BE); pengujian berkas unduhan CSV.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: status Company Alpha diubah menjadi Suspended pada langkah 41 (TC-FA-CF-592); hook `after` memulihkannya ke Active lewat seed reset Company Alpha. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-585: Edit saat Suspended

1. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
2. Ubah Field Name menjadi `Susp Edit {runId}-152`
3. Klik `[Save]`
4. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
5. Verifikasi tidak ada redirect (halaman Custom Fields tetap tampil)
6. Verifikasi modal Edit tertutup otomatis
7. Verifikasi tabel di-refresh
8. Verifikasi baris `Storage Capacity` tetap di tabel tanpa perubahan data
9. Tutup toast error

### TC-FA-CF-586: Deactivate saat Suspended

10. Geser switch Active baris `Asset Serial Tag` ke OFF
11. Klik `[Deactivate]`
12. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
13. Verifikasi dialog Deactivate tertutup
14. Verifikasi tabel di-refresh
15. Verifikasi switch Active baris `Asset Serial Tag` kembali ke posisi ON
16. Tutup toast error

### TC-FA-CF-587: Delete dan Bulk Delete saat Suspended

17. Klik row action `⋯` > `Delete` pada baris `Legacy Tag` sampai dialog Delete tampil
18. Klik `[Delete]` pada dialog
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
20. Verifikasi dialog Delete tertutup
21. Verifikasi tabel di-refresh
22. Verifikasi baris `Legacy Tag` tetap ada
23. Tutup toast error
24. Pilih dua field (`Legacy Tag` dan `Compliance File`) dan jalankan Bulk Delete sampai dialog Bulk Delete tampil
25. Klik `[Delete]` pada dialog Bulk Delete
26. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
27. Verifikasi dialog Bulk Delete tertutup
28. Verifikasi tabel di-refresh
29. Verifikasi kedua baris tetap ada
30. Tutup toast error

### TC-FA-CF-588: pembacaan tetap diizinkan saat Suspended

31. Verifikasi tabel tampil tanpa penolakan
32. Klik icon Download > `Download as CSV`
33. Verifikasi berkas terunduh
34. Buka Modal Changelog
35. Verifikasi Modal Changelog terbuka tanpa penolakan
36. Tutup Modal Changelog

### TC-FA-CF-592: entitas menjadi Suspended saat halaman terbuka

37. Ganti akun: `Logout` dari Total Control Client Suspended
38. Login sebagai Total Control Company Alpha dengan `Spectra.env.FA_TC_PASSWORD`
39. Buka tabel Settings > Custom Fields tab General
40. Verifikasi tabel tampil
41. Ubah status Company Alpha menjadi Suspended lewat Pre-setup
42. Klik row action `⋯` > `Delete` pada baris `Legacy Tag` sampai dialog Delete tampil
43. Klik `[Delete]` pada dialog
44. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
45. Verifikasi dialog Delete tertutup
46. Verifikasi tabel di-refresh
47. Verifikasi field `Legacy Tag` tidak terhapus

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 47 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas h, penolakan aksi tulis saat entitas Suspended), berdiri sendiri, dan tiap aksi ditolak sehingga data tidak berubah; satu blok tidak membuat blok lain kehilangan makna. Pemecahan per aksi hanya menambah login dan hook tanpa membedakan state.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 24 (memilih dua field dan membuka dialog Bulk Delete, mengikuti Langkah 3 TC-FA-CF-587), langkah 36 (menutup Modal Changelog), langkah 37 dan 38 (ganti akun eksplisit ke Company Alpha), langkah 39 (membuka tabel), langkah 9, 16, 23, dan 30 (menutup toast error sebelum aksi atau asersi berikutnya; toast error identik pada langkah 4, 12, 19, dan 26 tidak bertahan ke aksi berikutnya, R-12). Langkah 41 adalah pemicu state (ubah status Company Alpha) yang diperlukan Langkah 2 TC-FA-CF-592.
- TC-FA-CF-584 dan TC-FA-CF-659 (Suspended) tidak ada di spec ini; TC itu ada di spec absence karena tujuan utamanya tidak adanya entri log.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Client Suspended (Pre-setup #22 hanya mendeskripsikan Company); akun disediakan tim FE.
  - TC-FA-CF-587 menyebut "dua field" tanpa nama; spec memakai `Legacy Tag` dan `Compliance File`.
  - TC-FA-CF-588 menyebut "Buka tabel" sebagai langkah 1; tabel sudah dibuka hook `beforeEach` suite sehingga spec langsung memverifikasinya (langkah 31).
