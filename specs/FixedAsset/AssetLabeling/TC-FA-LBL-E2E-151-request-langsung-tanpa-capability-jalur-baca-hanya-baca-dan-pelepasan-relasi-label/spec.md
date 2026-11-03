---
id: TC-FA-LBL-E2E-151-request-langsung-tanpa-capability-jalur-baca-hanya-baca-dan-pelepasan-relasi-label
title: "Request Langsung: Tanpa Capability, Jalur Baca Hanya-Baca, dan Pelepasan Relasi Label"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-451
  - TC-FA-LBL-452
  - TC-FA-LBL-460
  - TC-FA-LBL-481
coverage:
  web: automated
---

# Request Langsung: Tanpa Capability, Jalur Baca Hanya-Baca, dan Pelepasan Relasi Label

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Seluruh langkah berupa request langsung ke server lewat klien HTTP (bagian 8b butir 1): asersi hanya status respons dan state data yang dibaca lewat fixture BE; perilaku FE untuk respons yang sama diasersi di spec jalur form.
- Role yang diuji (sesi API; akun aktor hook `before` adalah Tanpa Role Ini, ganti sesi lewat langkah eksplisit; tidak ada login UI):

  | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|
  | Tanpa Role Ini | #8 | `Fixture.assetLabeling.akun.noRole` | `Spectra.env.FA_NOROLE_PASSWORD` |
  | Policy-Read | #25 | `Fixture.assetLabeling.akun.policyRead` | `Spectra.env.FA_POLICYREAD_PASSWORD` |
  | Asset-Tag-Update | #26 | `Fixture.assetLabeling.akun.assetTagUpdate` | `Spectra.env.FA_ASSETTAGUPDATE_PASSWORD` |
  | Total Control Company Alpha (juga Update pada Manage Asset & TAG; TC-FA-LBL-481) | #1 | `Fixture.assetLabeling.akun.totalControl` | `Spectra.env.FA_LBL_TC_PASSWORD` |
  | Total Control Company Extra (juga Update pada Manage Asset & TAG; TC-FA-LBL-460) | #56 | `Fixture.assetLabeling.akun.totalControlExtra` | belum ada, disediakan tim FE |

- Hook `before` login API sebagai Tanpa Role Ini dan seeding oleh Total Control lewat fixture BE; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `FA_NOROLE_PASSWORD`, `FA_POLICYREAD_PASSWORD`, `FA_ASSETTAGUPDATE_PASSWORD`, dan `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture. Password akun Total Control Company Extra belum ada dan disediakan tim FE.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Pre-setup (hanya dibaca; request yang diuji ditolak atau tidak mengubah data, S-06): #12 label `Finance Department` (TC-FA-LBL-451), #12 label `Seasonal Event` dan #13 aset `Laptop Dell - 3` tanpa label `Seasonal Event` (TC-FA-LBL-481, pelepasan yang tidak terpasang tidak mengubah apa pun).
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-151`, Color `Fixture.assetLabeling.warnaSeed`): label `Tag Edit 452 {runId}-151` (bersih); label `Lock Default {runId}-151` sebagai Default Label Asset Name `Lock Item {runId}-151` dan tertempel ber-source default pada aset Active `Lock Asset {runId}-151` di Company Extra (Pre-setup #56; pola Pre-setup #27, TC-FA-LBL-460). Label `Policy Write 452` tidak di-seed (hasil request yang ditolak tidak boleh ada).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.noRole` | `noAssetMasterRole_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.policyRead` | `policyRead_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.assetTagUpdate` | `assetTagUpdate_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.totalControlExtra` | belum ada, disediakan tim FE (pola Pre-setup #56 `totalControl_automated_{namaCompany}@qwertysystem.net`; `{namaCompany}` Company Extra belum diketahui) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog serta jumlah entri Changelog Labels, System Log, dan Activity Log; endpoint tidak ditulis di TC (S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-451: Role tanpa capability tidak dapat membaca katalog atau View Tagged Assets

1. Gunakan sesi API Tanpa Role Ini (Pre-setup #8)
2. Kirim request langsung ke server: mengambil daftar label
3. Verifikasi server menolak dengan `403 Forbidden`
4. Kirim request langsung ke server: mengambil daftar aset ber-label `Finance Department`
5. Verifikasi server menolak dengan `403 Forbidden`
6. Kirim request langsung ke server: mengunduh ekspor katalog
7. Verifikasi server menolak dengan `403 Forbidden`
8. Verifikasi ketiga respons tidak memuat data label

### TC-FA-LBL-452: Jalur baca katalog Policy-Read dan Asset-Tag-Update bersifat hanya-baca

9. Ganti sesi API ke Policy-Read (Pre-setup #25)
10. Kirim request langsung ke server: mengambil nama dan warna label
11. Verifikasi permintaan baca nama dan warna label berhasil
12. Kirim request langsung ke server: membuat label `Policy Write 452 {runId}-151`
13. Verifikasi server menolak dengan `403 Forbidden`
14. Kirim request langsung ke server: mengambil aset ber-label
15. Verifikasi server menolak dengan `403 Forbidden`
16. Kirim request langsung ke server: mengunduh ekspor
17. Verifikasi server menolak dengan `403 Forbidden`
18. Ganti sesi API ke Asset-Tag-Update (Pre-setup #26)
19. Kirim request langsung ke server: mengambil nama dan warna label untuk dropdown penugasan
20. Verifikasi permintaan baca nama dan warna label berhasil
21. Kirim request langsung ke server: mengubah nama label seed `Tag Edit 452 {runId}-151`
22. Verifikasi server menolak dengan `403 Forbidden`
23. Kirim request langsung ke server: mengambil aset ber-label
24. Verifikasi server menolak dengan `403 Forbidden`

### TC-FA-LBL-460 dan TC-FA-LBL-481: Pelepasan relasi label lewat request langsung oleh Total Control

25. Ganti sesi API ke Total Control Company Extra (Pre-setup #56, juga memegang role Update pada Manage Asset & TAG)
26. Catat Total Asset label `Lock Default {runId}-151` sebagai baseline lewat fixture BE
27. Kirim request langsung ke server: melepas `Lock Default {runId}-151` dari aset `Lock Asset {runId}-151`
28. Verifikasi server menolak karena label terkunci oleh Default Label
29. Verifikasi relasi `Lock Default {runId}-151` pada aset `Lock Asset {runId}-151` tetap ada
30. Verifikasi Total Asset `Lock Default {runId}-151` sama dengan baseline
31. Ganti sesi API ke Total Control Company Alpha (Pre-setup #1, juga memegang role Update pada Manage Asset & TAG)
32. Catat baseline jumlah entri log aset `Laptop Dell - 3` lewat fixture BE
33. Kirim request langsung ke server: melepas `Seasonal Event` dari aset `Laptop Dell - 3`
34. Verifikasi permintaan dijawab sukses tanpa galat
35. Verifikasi aset `Laptop Dell - 3` tidak memiliki label `Seasonal Event` dan tidak ada perubahan data
36. Verifikasi jumlah entri log aset `Laptop Dell - 3` sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 1, 9, 18, 25, 26, 31, 32 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Penyimpangan urutan (S-05): TC-FA-LBL-451 dan 452 (role tanpa hak tulis) dikerjakan lebih dulu dan TC-FA-LBL-460 dan 481 (Total Control) di akhir, supaya sesi API berpindah dari role paling terbatas ke Total Control tanpa kembali.
- TC-FA-LBL-460 dan 481 memakai Total Control yang juga memegang role Update pada Manage Asset & TAG (precondition TC); keduanya ada di spec ini karena kelas harness sama (request langsung, defense-in-depth).
- Ukuran spec (36 langkah, di atas smell 35 langkah): keempat TC satu kelas (request langsung, defense-in-depth), satu sesi API yang berpindah role dari paling terbatas ke Total Control, seed milik spec, dan tiap blok berdiri sendiri; langkah bertambah satu karena TC-FA-LBL-460 (Company Extra) dan TC-FA-LBL-481 (Company Alpha) memakai akun Total Control berbeda (langkah 25 dan 31) dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - Akun dan `{namaCompany}` Company Extra (TC-FA-LBL-460, Pre-setup #56) belum ada dan menunggu konfirmasi tim FE; TC-FA-LBL-481 memakai Total Control Company Alpha (aset `Laptop Dell - 3`, Pre-setup #13) sehingga spec memakai dua akun sesuai TC (langkah 25 dan 31).
  - TC-FA-LBL-452 menyebut "mengubah label" untuk Asset-Tag-Update tanpa nama label; spec memakai label seed `Tag Edit 452`.
  - TC-FA-LBL-452 Expected b memuat ekspor hanya untuk Policy-Read (langkah ekspor Asset-Tag-Update tidak ada di TC); spec mengikuti TC.
  - TC-FA-LBL-481 Expected b "tidak ada entri log aset" tidak menyebut surface; spec memakai jumlah entri log aset `Laptop Dell - 3` terhadap baseline.
  - Post Condition TC-FA-LBL-460 dan 481 tidak ada langkah observasi tambahan di luar Expected sehingga tidak diasersi lagi.
