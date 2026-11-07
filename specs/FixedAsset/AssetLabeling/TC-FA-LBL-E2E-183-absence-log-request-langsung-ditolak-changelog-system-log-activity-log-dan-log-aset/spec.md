---
id: TC-FA-LBL-E2E-183-absence-log-request-langsung-ditolak-changelog-system-log-activity-log-dan-log-aset
title: "Absence Log: Request Langsung Ditolak Tidak Menambah Entri Changelog Labels, System Log, Activity Log, dan Log Aset"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-441
  - TC-FA-LBL-442
  - TC-FA-LBL-443
  - TC-FA-LBL-444
  - TC-FA-LBL-445
  - TC-FA-LBL-446
  - TC-FA-LBL-447
  - TC-FA-LBL-448
  - TC-FA-LBL-449
  - TC-FA-LBL-450
  - TC-FA-LBL-453
  - TC-FA-LBL-457
  - TC-FA-LBL-481
coverage:
  web: automated
---

# Absence Log: Request Langsung Ditolak Tidak Menambah Entri Changelog Labels, System Log, Activity Log, dan Log Aset

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Seluruh langkah berupa request langsung ke server lewat klien HTTP (bagian 8b butir 1) sebagai pemicu kondisi yang diasersi tidak tercatat (P-5 butir a); entri log dibaca lewat fixture BE sebagai jumlah entri per surface dan dibandingkan dengan baseline TC itu sendiri (S-12). Tidak ada login UI.
- Role yang diuji (sesi API; akun aktor hook `before` adalah Read Only, ganti sesi lewat langkah eksplisit):

  | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|
  | Read Only | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` |
  | Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` |
  | Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` |
  | Delete-Only | #5 | `Fixture.assetLabeling.akun.deleteOnly` | `Spectra.env.FA_DELETEONLY_PASSWORD` |
  | Read-Capability | #6 | `Fixture.assetLabeling.akun.readCapability` | `Spectra.env.FA_READCAP_PASSWORD` |
  | Total Control Company Alpha (juga Update pada Manage Asset & TAG; TC-FA-LBL-481) | #1 | `Fixture.assetLabeling.akun.totalControl` | `Spectra.env.FA_LBL_TC_PASSWORD` |

- Seeding: label, aset, dan Asset Name seed dibuat oleh Total Control (Pre-setup #1) lewat fixture BE di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `FA_RO_PASSWORD`, `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_DELETEONLY_PASSWORD`, `FA_READCAP_PASSWORD`, dan `FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Request Ditolak (parameter langkah 1 sampai 7, TC-FA-LBL-441 sampai 449):

  | TC | Sesi API | Request |
  |---|---|---|
  | TC-FA-LBL-441 | Read Only | membuat label `Direct Create 441 {runId}-183` |
  | TC-FA-LBL-442 | Read Only | mengubah nama `Direct Edit 442 {runId}-183` menjadi `Direct Edit 442 X {runId}-183` |
  | TC-FA-LBL-443 | Read Only | menghapus label bersih `Direct Delete 443 {runId}-183` |
  | TC-FA-LBL-444 | Create-Only | mengubah nama `Direct Edit 444 {runId}-183` menjadi `Direct Edit 444 X {runId}-183` |
  | TC-FA-LBL-445 | Create-Only | menghapus label bersih `Direct Delete 445 {runId}-183` |
  | TC-FA-LBL-446 | Update-Only | membuat label `Direct Create 446 {runId}-183` |
  | TC-FA-LBL-447 | Update-Only | menghapus label bersih `Direct Delete 447 {runId}-183` |
  | TC-FA-LBL-448 | Delete-Only | membuat label `Direct Create 448 {runId}-183` |
  | TC-FA-LBL-449 | Delete-Only | mengubah nama `Direct Edit 449 {runId}-183` menjadi `Direct Edit 449 X {runId}-183` |

- Warna Tidak Valid (dipakai langkah 21 dan 22, TC-FA-LBL-453):

  | Warna |
  |---|
  | `#GGGGGG` |
  | `#12345` |
  | `#FFF` |
  | `3B82F6` (tanpa `#`) |
  | `#1234567` |

- Data Pre-setup (hanya dibaca; request yang diuji tidak mengubah data, S-06): #12 label `Seasonal Event` dan #13 aset `Laptop Dell - 3` tanpa label `Seasonal Event` (TC-FA-LBL-481).
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-183`, Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label kecuali dinyatakan lain): `Direct Edit 442`, `Direct Delete 443`, `Direct Edit 444`, `Direct Delete 445`, `Direct Delete 447`, `Direct Edit 449`, dan `Direct Edit 450` (masing-masing bersuffix `{runId}-183`). Label `Used Label 457 {runId}-183` tertempel pada tiga aset Active `Used Asset 1 {runId}-183`, `Used Asset 2 {runId}-183`, dan `Used Asset 3 {runId}-183`; label `Default Label 457 {runId}-183` menjadi Default Label satu Asset Name `Used Item {runId}-183` (jumlah Asset Name 1). Label `Direct Create 441`, `Direct Create 446`, `Direct Create 448`, `Direct Create 450`, dan `Hex Direct 453` tidak di-seed (hasil request yang ditolak tidak boleh ada).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.readOnly` | `readOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.createOnly` | `createOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.updateOnly` | `updateOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.deleteOnly` | `deleteOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.readCapability` | `readCapability_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.totalControl` | `totalControl_automated_{namaCompany}@qwertysystem.net` |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca jumlah entri Changelog Labels, System Log, Activity Log, dan log aset `Laptop Dell - 3`; endpoint tidak ditulis di TC (S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-441 sampai TC-FA-LBL-449: Read Only, Create-Only, Update-Only, dan Delete-Only (perulangan per baris tabel Request Ditolak)

1. Untuk setiap baris tabel Request Ditolak (langkah 1 sampai 7): gunakan sesi API pada kolom Sesi API
2. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE
3. Kirim request langsung ke server sebagai sesi pada kolom Sesi API: aksi pada kolom Request
4. Verifikasi server menolak dengan `403 Forbidden`
5. Verifikasi jumlah entri Changelog Labels sama dengan baseline, tidak ada entri baru
6. Verifikasi jumlah entri System Log sama dengan baseline, tidak ada entri baru
7. Verifikasi jumlah entri Activity Log sama dengan baseline, tidak ada entri baru

### TC-FA-LBL-450: Read-Capability

8. Ganti sesi API ke Read-Capability (Pre-setup #6)
9. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE
10. Kirim request langsung ke server sebagai Read-Capability: membuat label `Direct Create 450 {runId}-183`
11. Verifikasi server menolak pembuatan dengan `403 Forbidden`
12. Kirim request langsung ke server sebagai Read-Capability: mengubah nama label seed `Direct Edit 450 {runId}-183` menjadi `Direct Edit 450 X {runId}-183`
13. Verifikasi server menolak pengubahan dengan `403 Forbidden`
14. Kirim request langsung ke server sebagai Read-Capability: menghapus label seed `Direct Edit 450 {runId}-183`
15. Verifikasi server menolak penghapusan dengan `403 Forbidden`
16. Verifikasi jumlah entri Changelog Labels sama dengan baseline, tidak ada entri baru
17. Verifikasi jumlah entri System Log sama dengan baseline, tidak ada entri baru
18. Verifikasi jumlah entri Activity Log sama dengan baseline, tidak ada entri baru

### TC-FA-LBL-453: Warna tidak valid lewat permintaan langsung

19. Ganti sesi API ke Total Control Company Alpha (Pre-setup #1)
20. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE
21. Untuk setiap baris tabel Warna Tidak Valid (langkah 21 dan 22): kirim request langsung ke server sebagai Total Control: membuat label `Hex Direct 453 {runId}-183` dengan warna pada kolom Warna
22. Verifikasi request ditolak dengan pesan `Invalid color format`
23. Verifikasi jumlah entri Changelog Labels sama dengan baseline, tidak ada entri baru
24. Verifikasi jumlah entri System Log sama dengan baseline, tidak ada entri baru
25. Verifikasi jumlah entri Activity Log sama dengan baseline, tidak ada entri baru

### TC-FA-LBL-457: Delete label yang dipakai lewat permintaan langsung

26. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE
27. Kirim request langsung ke server sebagai Total Control: menghapus label `Used Label 457 {runId}-183`
28. Verifikasi request ditolak oleh guard in-use dengan jumlah aset `3`
29. Kirim request langsung ke server sebagai Total Control: menghapus label `Default Label 457 {runId}-183`
30. Verifikasi request ditolak oleh guard in-use dengan jumlah Asset Name `1`
31. Verifikasi jumlah entri Changelog Labels sama dengan baseline, tidak ada entri baru
32. Verifikasi jumlah entri System Log sama dengan baseline, tidak ada entri baru
33. Verifikasi jumlah entri Activity Log sama dengan baseline, tidak ada entri baru

### TC-FA-LBL-481: Pelepasan label yang tidak terpasang lewat permintaan langsung

34. Catat baseline jumlah entri log aset `Laptop Dell - 3` lewat fixture BE
35. Kirim request langsung ke server sebagai Total Control: melepas `Seasonal Event` dari aset `Laptop Dell - 3`
36. Verifikasi permintaan dijawab sukses tanpa galat
37. Verifikasi jumlah entri log aset `Laptop Dell - 3` sama dengan baseline, tidak ada entri baru

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth) dan section 9. Subjudul `###` memetakan langkah ke TC granular.
- Spec absence kelas g (bagian 3 prinsip 13g, S-05): asersi "tidak ada entri log baru" atas request langsung yang ditolak (kelas a) dengan request tersebut sebagai pemicu (P-5 butir a), bukan objek uji; setiap TC memakai baseline sendiri yang dicatat tepat sebelum pemicunya (S-12) dan satu `Verifikasi` per surface log (S-01). Anchor positif tiap absence (bagian 8b butir 2): `Verifikasi` penolakan server atau pesan penolakan atas pemicu yang sama (langkah 4, 11, 13, 15, 22, 28, 30) dan, untuk TC-FA-LBL-481, jawaban sukses tanpa galat (langkah 36); baseline yang dicatat sebelum pemicu menjadi pembanding jumlah.
- Pembagian TC lintas spec (S-05): TC-FA-LBL-441, TC-FA-LBL-442, TC-FA-LBL-443, TC-FA-LBL-444, TC-FA-LBL-445, TC-FA-LBL-446, dan TC-FA-LBL-447 ada di spec 149, TC-FA-LBL-448, TC-FA-LBL-449, dan TC-FA-LBL-450 di spec 150, TC-FA-LBL-481 di spec 151, dan TC-FA-LBL-453 dan TC-FA-LBL-457 di spec 152; spec itu mengasersi status respons dan state data katalog, spec ini mengasersi absence entri log. Id TC tetap di `sourceTc` kedua spec.
- Pemicu memakai role, request, dan data bernama yang sama dengan spec asal tetapi data milik spec ini (suffix `{runId}-183`, S-06).
- Langkah penghubung (S-03): langkah 8 dan 19 adalah pergantian sesi API tanpa `Verifikasi` (langkah 1 memilih sesi per baris tabel); langkah 2, 9, 20, 26, 34 mencatat baseline lewat fixture BE; bukan bagian Expected TC.
- Perulangan (bagian 8b butir 7): langkah 1 sampai 7 diulang untuk sembilan baris tabel Request Ditolak (baseline dicatat ulang di tiap putaran, langkah 2) dan langkah 21 dan 22 untuk lima warna; parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa. Pada TC-FA-LBL-453 baseline dicatat sekali sebelum seluruh baris tabel TC itu.
- Ukuran spec (37 langkah nominal, sekitar 101 langkah dengan ekspansi perulangan, di atas smell 35 langkah): seluruh blok satu kelas (absence log atas request langsung yang ditolak), satu klien HTTP dan sesi API tanpa UI, dan tiap blok berdiri sendiri dengan baseline dan data seed sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena S-12 mewajibkan baseline per TC (13 TC), S-01 mewajibkan satu `Verifikasi` per surface log, dan ekspansi perulangan.
- Temuan untuk QA:
  - Expected b TC-FA-LBL-441 sampai 450, 453, dan 457 "tidak ada entri log baru" tidak menyebut surface; spec memakai Changelog Labels, System Log, dan Activity Log (jumlah entri terhadap baseline). TC-FA-LBL-481 menyebut "entri log aset" tanpa surface; spec memakai jumlah entri log aset `Laptop Dell - 3`.
  - TC-FA-LBL-450 menyebut tiga request dalam satu langkah dengan Expected tunggal; spec memecahnya menjadi tiga request dengan `Verifikasi` `403 Forbidden` masing-masing (S-01) dan satu baseline untuk ketiganya (satu TC).
  - Nama baru pada TC-FA-LBL-442, 444, dan 449 ditulis `Direct Edit nnn X`; spec memakai nama bersuffix `{runId}` dan akhiran ` X` setelah suffix supaya unik per run.
  - TC-FA-LBL-457 menyebut jumlah aset 3 dan jumlah Asset Name 1 dari Pre-setup (`High Priority`, `Warehouse Priority`); spec men-seed label dengan jumlah yang sama.
