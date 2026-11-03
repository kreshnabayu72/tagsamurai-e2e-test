---
id: TC-AC-DC-E2E-016-role-matrix-negatif-entity-distributor
title: "Role Matrix Negatif: Akses Entity Distributor ke Category"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-44
  - TC-AC-DC-45
  - TC-AC-DC-280
coverage:
  web: automated
---
# Role Matrix Negatif: Akses Entity Distributor ke Category

## Prerequisites

- Mode: FE+BE.
- Aktor: satu akun, Distributor (Pre-setup #10). Login di hook `before` spec ini; halaman awal yang dibuka hook `beforeEach` suite tidak dipakai; tiap TC membuka halamannya sendiri.

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control entitas Distributor `Distributor Jaringan` | #10 `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_DISTRIBUTOR_PASSWORD` |

- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca), #16 (Device SKU `SKU-FN-1`, `SKU-FN-2`, `SKU-FN-3`, hanya dibaca). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Spec ini tidak membuat data; tidak ada seeding dan tidak ada cleanup selain hook `after` yang mengembalikan sesi ke akun default suite.
- Env var `AC_DC_DISTRIBUTOR_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-44: Distributor melihat tree Category read-only hanya pada sub-tab Device SKU

1. Buka halaman `Settings > Device > Device SKU`
2. Verifikasi tabel Device SKU menampilkan sedikitnya satu baris
3. Expand `Hardware` lalu `Handheld Reader`
4. Verifikasi tree Category tampil seluruhnya dalam mode read-only
5. Hover node `Rugged Scanner`
6. Verifikasi aksi `+ Subcategory`, Edit, dan Delete tidak ada (Hidden) pada `Rugged Scanner`
7. Hover node hardcoded `Handheld Reader`
8. Verifikasi aksi `+ Subcategory`, Edit, dan Delete tidak ada (Hidden) pada `Handheld Reader`
9. Centang kotak `Filter Induk`
10. Verifikasi kotak `Filter Induk` tercentang
11. Verifikasi tabel Device SKU tersaring dan menampilkan `SKU-FN-1`, `SKU-FN-2`, `SKU-FN-3`
12. Hapus centang kotak `Filter Induk`
13. Verifikasi ikon Changelog tidak tampil pada header sidebar sehingga modal Changelog tidak dapat dibuka

### TC-AC-DC-45: Distributor tidak dapat membuka sub-tab Device Name lewat URL langsung

14. Ketik URL `Settings > Device > Device Name` langsung di address bar
15. Verifikasi toast error "You don't have permission to do this." tampil
16. Verifikasi halaman di-refresh sehingga elemen yang tidak berhak tersembunyi
17. Verifikasi tidak ada redirect ke halaman unauthorized

### TC-AC-DC-280: Distributor tidak melihat sub-tab Device Name pada Settings > Device

18. Buka halaman `Settings > Device`
19. Verifikasi sub-tab Device SKU tampil
20. Verifikasi sub-tab Device Name tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix negatif dengan satu role (Distributor); tiga kasus dikelompokkan per topik entity gate (bagian 3a).
- Langkah penghubung: langkah 1 dan 18 (membuka halaman akun Distributor, karena halaman awal hook suite tidak berlaku untuk entity ini), langkah 2 (pembanding data: baris Device SKU pada surface yang sama sebelum asersi tersaring, 8b butir 2), langkah 3 (expand tree agar node `Rugged Scanner` dan `Handheld Reader` terlihat), langkah 12 (membersihkan seleksi filter sebelum TC berikutnya, S-09).
- Temuan untuk QA:
  - Hook `beforeEach` suite membuka Settings > Device > Device Name; untuk akun yang ditolak di halaman itu (Distributor, Partner, Client, tanpa capability) pembukaan itu memicu penolakan akses. Perlu pengecualian di hook suite; langkah pertama tiap TC spec ini membuka halaman sendiri.
  - TC-AC-DC-45 menulis "elemen yang tidak berhak tersembunyi" tanpa menyebut elemen mana; asersi mengikuti kalimat TC apa adanya.
  - TC-AC-DC-44 tidak menyebut jumlah baris tabel Device SKU sebelum filter; kata "tersaring" diasersi dengan pembanding generik (sedikitnya satu baris) dan tiga SKU hasil filter.
  - TC-AC-DC-44 langkah 1 menyebut "halaman tampil dengan Sidebar Category" dan langkah 4 hanya "perhatikan header sidebar"; keduanya tidak punya Expected sendiri dan tidak diasersi di luar butir Expected.
  - Post Condition TC-AC-DC-44, 45, dan 280 ('-') tidak punya langkah observasi dan tidak diasersi.
