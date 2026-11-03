---
id: TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet
title: "Screening Tab Asset Control: Station Quota, Station List, Tablet List, Aksi Row, dan Download"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-307
  - TC-AC-ACC-308
  - TC-AC-ACC-309
  - TC-AC-ACC-310
  - TC-AC-ACC-314
  - TC-AC-ACC-338
  - TC-AC-ACC-787
  - TC-AC-ACC-788
  - TC-AC-ACC-861
coverage:
  web: automated
---

# Screening Tab Asset Control: Station Quota, Station List, Tablet List, Aksi Row, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca, tidak diubah): Client C-01 "PT Sejahtera Abadi" (Tabel A2). Asset Control Total 3 / Used 2 / Available 1. Station List: "Gerbang Gudang A" (Active, Ports 4, Tablets 2, Reader Group (Fixed Asset) "Gudang Pusat", Reader Group (Supply) "—", Reader ID RDR-0001, Last Active 08 Jul 2026 09:30, berisi Tablet "Tablet Lobi 1" Active), "Gerbang Gudang B" (Inactive, Ports 4, Tablets 1, "Gudang Pusat", Supply "Supply Utama", RDR-0002, Last Active 08 Jul 2026 08:10), "Gerbang Lama" (Deactivated, Ports 2, Tablets 0, kedua group "—", RDR-0003, Last Active 01 Mar 2026, berisi Tablet "Tablet Lama" Revoked).
- Kemampuan teknis: penangkapan nama berkas unduhan di browser uji (disediakan tim FE).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite (dinyatakan di `suite.md`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, lalu klik Company Name "PT Sejahtera Abadi"

### TC-AC-ACC-307: Screening Tab Asset Control

2. Klik Tab Asset Control
3. Verifikasi Header: tab aktif `Asset Control`
4. Verifikasi Header: ikon Changelog tampil
5. Verifikasi Section Station Quota memuat kolom `Total`, `Used`, `Available`
6. Verifikasi tombol [Generate Enrollment QR] tampil di Section Station Quota
7. Verifikasi Section Station List: Search dengan placeholder "Search by reader name, reader ID, or model..."
8. Verifikasi Table Tools Station List: `Filter`, `Download`, `Changelog` tampil
9. Verifikasi kolom Station List: `Reader Name`, `Reader Group (Fixed Asset)`, `Reader Group (Supply)`, `Reader ID`, `Reader Model`, `Ports`, `Tablets`, `Last Active`, `Status`, `Column Visibility (⋯)`
10. Klik row "Gerbang Gudang A" untuk expand
11. Verifikasi Tablet List memuat kolom `Device Name`, `Brand`, `Device ID`, `App Version`, `Enrolled Date`, `Last Active`, `Status`, `⋯`
12. Verifikasi Footer: Pagination Station List tampil
13. Klik row "Gerbang Gudang A" untuk collapse

### TC-AC-ACC-308: Station Quota: Used dan Available

14. Verifikasi Station Quota: Total 3, Used 2, Available 1

### TC-AC-ACC-309: Badge Status Station List dan sel kosong

15. Verifikasi baris "Gerbang Gudang A": badge Status `Active` (success)
16. Verifikasi baris "Gerbang Gudang A": Reader Group (Fixed Asset) "Gudang Pusat" dan Reader Group (Supply) `—`
17. Verifikasi baris "Gerbang Gudang B": badge Status `Inactive` (secondary)
18. Verifikasi baris "Gerbang Gudang B": kedua Reader Group terisi
19. Verifikasi baris "Gerbang Lama": badge Status `Deactivated` (danger)
20. Verifikasi baris "Gerbang Lama": kedua Reader Group `—`, Tablets 0, dan Last Active terisi

### TC-AC-ACC-310: Kolom Tablets dan row expand

21. Klik row "Gerbang Gudang A"
22. Verifikasi row expand menampilkan Tablet List
23. Verifikasi kolom Tablets "Gerbang Gudang A" bernilai 2 (Revoked tidak dihitung)
24. Klik row "Gerbang Gudang A" untuk collapse
25. Klik row "Gerbang Lama" untuk expand Tablet List
26. Verifikasi Tablet "Tablet Lama" berbadge `Revoked` (danger)
27. Klik row "Gerbang Lama" untuk collapse

### TC-AC-ACC-314: Tablet List: kolom dan badge Status

28. Klik row "Gerbang Gudang A" untuk expand
29. Verifikasi kolom Tablet List sesuai: `Device Name`, `Brand`, `Device ID`, `App Version`, `Enrolled Date`, `Last Active`, `Status`
30. Verifikasi kolom App Version terurut semantic version
31. Verifikasi sel Last Active yang kosong tampil `—`
32. Klik row "Gerbang Gudang A" untuk collapse

### TC-AC-ACC-787: Ikon dan severity aksi Deactivate

33. Buka menu ⋯ pada Station "Gerbang Gudang A" (Active)
34. Verifikasi aksi Deactivate berikon CheckLine dengan severity dark
35. Tutup menu ⋯ dengan Esc

### TC-AC-ACC-788: Ikon dan severity aksi Revoke

36. Klik row "Gerbang Gudang A" untuk expand Tablet List
37. Buka menu ⋯ pada Tablet "Tablet Lobi 1" (Active)
38. Verifikasi aksi Revoke berikon DeleteBin6Line dengan severity danger
39. Tutup menu ⋯ dengan Esc

### TC-AC-ACC-861: Header kolom Station List satu baris

40. Verifikasi header "Reader Group (Fixed Asset)" dan "Reader Group (Supply)" tampil dalam satu baris tanpa wrap
41. Verifikasi sel Last Active pada ketiga baris Station List tampil dalam satu baris

### TC-AC-ACC-338: Download Station List: nama file

42. Klik Download pada toolbar Station List dan pilih satu format unduhan
43. Verifikasi nama berkas terunduh `Client-AssetControl-Stations-PT Sejahtera Abadi`

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 10 dan 13 (expand/collapse row agar kolom Tablet List yang diminta Expected 307 teramati), langkah 21, 24, 25, 27, 28, 32, 33, 35, 36, 37, 39 (expand/collapse dan membuka/menutup menu agar asersi berposisi sesuai S-14).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (baca-saja pada satu halaman Detail dan satu dataset Pre-setup, tanpa membuat data) dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-310 Expected b menyebut "Tablet Revoked tampil badge danger" pada row Gerbang Gudang A, tetapi Pre-setup C-01 hanya memuat Tablet Revoked ("Tablet Lama") di Gerbang Lama; langkah 25 sampai 27 menambahkan expand "Gerbang Lama" agar badge Revoked teramati (penyesuaian, bukan langkah TC).
  - TC-AC-ACC-314 Expected a tidak menyebut urutan semantic version yang dipakai (default sort Device Name A-Z atau sort App Version) dan Pre-setup tidak menyebut tablet berApp Version atau tablet ber-Last Active kosong pada Gerbang Gudang A; langkah 30 dan 31 mengikuti Expected apa adanya dan data tablet perlu dilengkapi di Tabel A.
  - TC-AC-ACC-338 tidak menyebut format berkas (CSV atau XLSX) dan ekstensi; nama berkas diasersi tanpa ekstensi.
  - TC-AC-ACC-309 tidak menyebut Reader Group baris B secara eksplisit; langkah 18 hanya mengasersi "terisi" sesuai Expected.
