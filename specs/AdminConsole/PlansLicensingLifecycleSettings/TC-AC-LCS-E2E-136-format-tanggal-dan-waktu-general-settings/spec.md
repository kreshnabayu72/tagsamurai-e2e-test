---
id: TC-AC-LCS-E2E-136-format-tanggal-dan-waktu-general-settings
title: "Format Tanggal dan Waktu General Settings pada Kolom Date Modal Changelog, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-492
  - TC-AC-LCS-493
  - TC-AC-LCS-494
  - TC-AC-LCS-495
  - TC-AC-LCS-496
  - TC-AC-LCS-497
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings pada Kolom Date Modal Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Dataset L (27 entri Changelog tab `Client Lifecycle`, entri ke-n pada n May 26 pukul 10:00 UTC) diseed lewat Fixture BE di hook `before` spec ini, termasuk entri 10 May 26 pukul 10:00 UTC; satu entri tambahan pada 10 May 26 pukul 23:30 UTC diseed lewat Fixture BE sebelum TC-AC-LCS-497. Spec ini tidak membuat atau mengubah Dataset L.
- General Settings yang diubah spec ini lewat Fixture BE: Date Format (`dd MMM yy`, `dd/MM/yy`), Time Format (24 jam, 12 jam), Time Zone (UTC, Asia/Jakarta); nilai awal Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC.
- State global dan pemulihan: General Settings dipulihkan ke Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC, jam server dan jam browser dipulihkan, dan dataset Changelog dikembalikan ke keadaan awal oleh hook `after` suite; jam dipulihkan segera setelah Save TC-AC-LCS-496 sebelum akun aktor membuka System Log dan Activity Log (S-09). Free Plan Duration `366` dipulihkan ke `365` oleh hook `beforeEach` dan `after` suite.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk mengatur General Settings, mengatur jam server dan jam browser, menyeed entri Changelog, dan memulihkan tab; kemampuan membaca jumlah entri System Log aktor dan Activity Log Admin Console sebelum aksi.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-492: Kolom Date modal Changelog memakai Date Format dd MMM yy dan Time Format 24 jam

1. Klik tab `Client Lifecycle`
2. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
3. Verifikasi kolom Date entri yang dicatat pada 10 May 26 pukul 10:00 UTC menampilkan tanggal `10 May 26` dan jam `10:00`
4. Atur General Settings lewat Fixture BE: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone UTC, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-493: Kolom Date modal Changelog memakai Date Format dd/MM/yy

5. Klik tab `Client Lifecycle`
6. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
7. Verifikasi kolom Date entri yang dicatat pada 10 May 26 pukul 10:00 UTC menampilkan tanggal `10/05/26` dan jam `10:00`
8. Atur General Settings lewat Fixture BE: Date Format `dd MMM yy`, Time Format 12 jam, Time Zone UTC, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-494: Kolom Date modal Changelog memakai Time Format 12 jam

9. Klik tab `Client Lifecycle`
10. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
11. Verifikasi kolom Date entri yang dicatat pada 10 May 26 pukul 10:00 UTC menampilkan tanggal `10 May 26` dan jam dalam format 12 jam dengan penanda `AM`
12. Atur General Settings lewat Fixture BE: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone Asia/Jakarta, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-495: Kolom Date modal Changelog mengikuti Time Zone General Settings

13. Klik tab `Client Lifecycle`
14. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
15. Verifikasi kolom Date entri yang dicatat pada 10 May 26 pukul 10:00 UTC menampilkan tanggal `10 May 26` dan jam `17:00` (UTC+7)

### TC-AC-LCS-496: System Log dan Activity Log menampilkan Date sesuai General Settings

16. Atur General Settings lewat Fixture BE: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone UTC, lalu muat ulang halaman Lifecycle Settings
17. Klik tab `Free Plan Settings`
18. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
19. Atur jam server dan jam browser ke 10 May 26 pukul 10:00 UTC lewat Fixture BE
20. Ubah Free Plan Duration dari `365` menjadi `366`
21. Klik `[Save]` dan tunggu toast sukses
22. Pulihkan jam server dan jam browser lewat Fixture BE
23. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
24. Verifikasi kolom Date entri baru System Log (jumlah entri bertambah satu dari baseline; Field `Free Plan Duration`, Old Value `365`, New Value `366`) menampilkan tanggal `10/05/26` dan jam `10:00`
25. Buka Activity Log (Admin Console)
26. Verifikasi kolom Date entri baru Activity Log (jumlah entri bertambah satu dari baseline; Field `Free Plan Duration`, Old Value `365`, New Value `366`) menampilkan tanggal `10/05/26` dan jam `10:00`
27. Atur General Settings lewat Fixture BE: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone Asia/Jakarta, dan tambah satu entri Changelog tab `Client Lifecycle` yang dicatat pada 10 May 26 pukul 23:30 UTC, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-497: Filter Date modal Changelog memakai batas hari menurut Time Zone General Settings

28. Klik tab `Client Lifecycle`
29. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
30. Klik Filter
31. Pilih rentang `11 May 26` sampai `11 May 26` pada `Date`
32. Klik `[Apply]`
33. Verifikasi entri yang dicatat pada 10 May 26 pukul 23:30 UTC tampil pada hasil filter dengan Date `11 May 26` dan jam `06:30` (hari mengikuti Time Zone Asia/Jakarta)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur General Settings ... lalu muat ulang" (precondition tiap TC), "Klik tab", "Klik Filter", "Catat jumlah entri ... sebagai baseline", dan pengaturan serta pemulihan jam (S-03, S-09, S-12).
- TC-AC-LCS-496 menyimpan Free Plan Duration saat jam server dan jam browser berada pada 10 May 26 pukul 10:00 UTC, lalu jam dipulihkan sebelum System Log dan Activity Log dibuka. Entri baru dikenali lewat kenaikan satu dari baseline serta Field, Old Value, dan New Value, bukan posisi "teratas", karena entri bercap waktu lampau tidak berada di posisi teratas setelah jam dipulihkan (S-12, S-14).
- Temuan untuk QA: TC-AC-LCS-496 tidak menyebut cara membuat Save pada 10 May 26 pukul 10:00 UTC; spec memakai Fixture BE pengatur jam yang disediakan tim FE/BE (S-13). Spec tidak menambahkan asersi kolom Modified By pada TC ini karena Expected TC hanya memuat kolom Date.
- Temuan untuk QA: precondition TC-AC-LCS-497 menyebut dataset memuat entri pada 10 May 26 pukul 23:30 UTC, sedangkan Dataset L (Pre-setup 8) hanya memuat entri 10 May 26 pukul 10:00 UTC; spec menyeed satu entri tambahan. Entri Dataset L ke-11 (11 May 26 pukul 10:00 UTC, 17:00 Asia/Jakarta) juga jatuh pada rentang filter, sedangkan Expected TC hanya menyebut entri 06:30; spec mengasersi hanya entri yang disebut TC.
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
