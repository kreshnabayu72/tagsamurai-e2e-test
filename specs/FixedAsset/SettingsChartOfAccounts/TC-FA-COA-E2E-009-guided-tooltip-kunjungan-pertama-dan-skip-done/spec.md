---
id: TC-FA-COA-E2E-009-guided-tooltip-kunjungan-pertama-dan-skip-done
title: "Guided Tooltip: Kunjungan Pertama dan Skip Done"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-105
  - TC-FA-COA-337
  - TC-FA-COA-340
  - TC-FA-COA-341
coverage:
  web: automated
---

# Guided Tooltip: Kunjungan Pertama dan Skip Done

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control desktop `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; dipakai sebagai user yang belum pernah membuka halaman (asumsi pre-setup, bukan data PRD). Login di hook `before` spec ini.
- Env var `FA_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Pengecualian atas butir Flag Guided Tooltip di `suite.md`: spec ini mengatur flag `guided_tooltip_seen_fa-settings-chart-of-accounts` sendiri sesudah hook (menghapus flag dengan langkah eksplisit sebelum tiap blok yang membutuhkan kunjungan pertama); kemampuan menghapus flag disediakan tim FE/BE. Hook suite `after` memulihkan flag ke true. Spec membuka layar sendiri sesudah flag dihapus (pengecualian atas hook `beforeEach` suite).
- Kemampuan teknis: viewport desktop; tombol `[Skip]`, `[Next]`, `[Done]`, dan `[?]`. Flag tidak dibaca langsung; persistensi diamati lewat muat ulang halaman.
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-337: Guided Tooltip berjalan otomatis pada kunjungan pertama dan tidak berjalan pada kunjungan berikutnya

1. Hapus flag `guided_tooltip_seen_fa-settings-chart-of-accounts`
2. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
3. Verifikasi tur mulai otomatis dari step 1
4. Klik `[Skip]`
5. Muat ulang halaman
6. Verifikasi Breadcrumb `Settings > Accounting > Chart of Accounts` tampil
7. Verifikasi tur tidak mulai otomatis

### TC-FA-COA-105: Guided Tooltip berjalan di desktop dengan enam step berurutan pada target yang benar

8. Klik `[?]` di kanan Breadcrumb
9. Verifikasi Step 1 menyorot header kolom Account Code dengan Title `Account Code` dan Description `Use the same code as in your accounting application so exported journals can be imported directly.`
10. Klik `[Next]`
11. Verifikasi Step 2 menyorot header kolom Function dengan Title `Account Function` dan Description `Each account has one function that decides which journal line it is used for.`
12. Klik `[Next]`
13. Verifikasi Step 3 menyorot header kolom Used By dengan Title `Where an Account Is Used` dan Description `Shows how many Asset Classes use the account. Accounts that are still in use cannot be deactivated or deleted.`
14. Klik `[Next]`
15. Verifikasi Step 4 menyorot header kolom Last Used in Journal dengan Title `Last Used in Journal` dan Description `Shows the latest journal period in which the account was exported. Exported accounts cannot be deleted.`
16. Klik `[Next]`
17. Verifikasi Step 5 menyorot ikon Filter di toolbar dengan Title `Filter Accounts` dan Description `Narrow down the list. Filters combine with your search.`
18. Klik `[Next]`
19. Verifikasi Step 6 menyorot ikon Changelog di toolbar dengan Title `Changelog` dan Description `See the history of changes made to accounts.`
20. Klik `[Done]`

### TC-FA-COA-340: Skip dan Done menutup tur serta menyetel flag kunjungan

21. Hapus flag `guided_tooltip_seen_fa-settings-chart-of-accounts`
22. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
23. Klik `[Skip]` pada step 1
24. Verifikasi tur tertutup
25. Muat ulang halaman
26. Verifikasi Breadcrumb `Settings > Accounting > Chart of Accounts` tampil
27. Verifikasi tur tidak mulai otomatis

### TC-FA-COA-341: Pindah halaman di tengah tur menutup tur tanpa menyetel flag

28. Hapus flag `guided_tooltip_seen_fa-settings-chart-of-accounts`
29. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
30. Klik `[Next]` dua kali sehingga tur berada di step 3
31. Klik menu sidebar di luar halaman ini
32. Verifikasi tur tertutup saat berpindah halaman
33. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
34. Verifikasi tur mulai otomatis dari step 1
35. Klik `[Skip]`

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Pengecualian atas hook suite: spec ini membuka halaman sendiri sesudah mengatur flag (langkah 1, 21, dan 28 menghapus flag; langkah "Buka Fixed Asset > Settings > Accounting > Chart of Accounts" sesudahnya).
- Urutan (S-10): TC-FA-COA-337 lebih dulu karena `[Skip]` menyetel flag true sehingga TC-FA-COA-105 berjalan lewat `[?]` tanpa tur otomatis; TC-FA-COA-340 dan TC-FA-COA-341 masing-masing diawali penghapusan flag. TC-FA-COA-337 memilih "melewati tur" (`[Skip]`); "menyelesaikan tur" diuji di langkah 8 sampai 20.
- Langkah penghubung (S-03): langkah 35 (menutup tur dengan `[Skip]` sehingga flag kembali true); langkah 5, 25 (muat ulang adalah langkah observasi flag; flag tidak dibaca langsung, S-13).
- Asersi tambahan di luar Expected TC (S-03): langkah 6 dan 26 menjadi anchor positif untuk absence tur (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-COA-341 langkah 2 menyebut "menu sidebar di luar halaman ini" tanpa menyebut menu; spec memakai menu sidebar lain mana pun, pilihan konkret perlu ditetapkan tim FE.
  - TC-FA-COA-337 menyebut "selesaikan atau lewati tur" tanpa memilih; spec memakai `[Skip]`.
  - User P87 ("belum pernah membuka halaman") adalah asumsi pre-setup; spec memakai akun Total Control default dengan flag dihapus lewat langkah eksplisit.
  - TC-FA-COA-105 langkah 2 menyebut "Klik `[Next]` pada tiap step sampai step 6" tanpa menyebut penutupan tur; spec menutup dengan `[Done]` (langkah 20).
