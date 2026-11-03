---
id: TC-AC-DS-E2E-001-screening-halaman-list-dasar
title: "Screening Halaman Device SKU List: Breadcrumb, Sub-tab, Hover SKU, dan Header Tabel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-1
  - TC-AC-DS-2
  - TC-AC-DS-4
  - TC-AC-DS-6
coverage:
  web: automated
---

# Screening Halaman Device SKU List: Breadcrumb, Sub-tab, Hover SKU, dan Header Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30 (129 SKU Principal), pohon Category #25. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Sesi API aktor dan seeding data tidak dipakai spec ini (read-only).

## Test Steps

### TC-AC-DS-1: Screening Header, Body, dan Footer

1. Amati area atas halaman, toolbar, tabel, pagination, dan sisi kanan halaman
2. Verifikasi Breadcrumb tampil `Settings > Device > Device SKU`
3. Verifikasi tidak ada Page Title terpisah di bawah Breadcrumb
4. Verifikasi tidak ada tombol Back
5. Verifikasi Sub-tab tampil `Device Name | Device SKU (aktif)`
6. Verifikasi Table Tools tampil `Search | Filter | Download | Changelog | [+ SKU]`
7. Verifikasi Sidebar Category tampil di sisi kanan halaman dengan judul `Category`
8. Verifikasi Sidebar Category memuat input pencarian pohon, tombol Expand/Collapse All, pohon Category, dan tab mengambang Collapse di tepi kiri panel
9. Verifikasi kolom tabel `Checkbox (unsortable) | Photo (unsortable) | Device Name (sortable) | SKU (sortable) | Category (sortable) | Brand (sortable) | Model/Type (sortable) | Current Stock (sortable) | Last Modified (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility, body per baris = row action menu)`
10. Verifikasi kolom Hardware Type, Range Type, dan TAG Type tidak tampil karena default Hidden
11. Verifikasi baris pertama halaman 1 adalah `BLE-KIN-GW1` (default sort SKU A-Z)
12. Verifikasi SKU berstok 0 (`HHR-ARC-200`) tetap tampil pada halaman 1
13. Verifikasi Pagination memuat selector jumlah data per halaman bernilai 10, navigasi halaman, dan input nomor halaman

### TC-AC-DS-4: Sub-tab Device Name dan Device SKU

14. Klik sub-tab `Device Name`
15. Verifikasi sub-tab `Device Name` ditandai aktif
16. Verifikasi tabel Device Name tampil
17. Klik sub-tab `Device SKU`
18. Verifikasi sub-tab `Device SKU` ditandai aktif
19. Verifikasi List Device SKU tampil dengan toolbar `Search | Filter | Download | Changelog | [+ SKU]`

### TC-AC-DS-6: Hover teks SKU

20. Amati warna teks SKU `HHR-ARC-100` dalam keadaan idle
21. Verifikasi teks SKU `HHR-ARC-100` berwarna netral sama dengan teks body tabel
22. Hover teks SKU `HHR-ARC-100`
23. Verifikasi warna teks SKU berubah ke warna primary Admin Console (merah)
24. Verifikasi tidak ada garis bawah pada teks SKU saat hover

### TC-AC-DS-2: Breadcrumb

25. Hover segmen `Settings` pada Breadcrumb, lalu klik segmen tersebut
26. Verifikasi segmen `Settings` berupa label statis dan halaman tidak berpindah (Breadcrumb `Settings > Device > Device SKU` dan List Device SKU tetap tampil)
27. Hover segmen `Device SKU` pada Breadcrumb, lalu klik segmen tersebut
28. Verifikasi segmen `Device SKU` berupa label statis dan halaman tidak berpindah (List Device SKU tetap tampil)
29. Hover segmen `Device`
30. Verifikasi segmen `Device` tampil sebagai elemen yang dapat diklik (kursor menunjukkan elemen dapat diklik)
31. Klik segmen `Device`
32. Verifikasi halaman Settings > Device terbuka dengan sub-tab `Device Name` aktif (default)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-1, TC-4, TC-6, TC-2. TC-2 diletakkan terakhir karena klik segmen `Device` meninggalkan halaman Device SKU (S-10); TC-4 dan TC-6 membutuhkan halaman Device SKU.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 20, 22 (mengamati), 25, 27, 29, 31 (hover dan klik yang hasilnya diasersi pada langkah berikutnya). Verifikasi langkah 12 memakai `HHR-ARC-100`/`HHR-ARC-200` hanya untuk menunjuk contoh SKU berstok 0 pada halaman 1; TC-1 hanya menyebut "SKU stok 0 tetap tampil" tanpa menyebut kode SKU.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#30 (`BLE-KIN-GW1`, `HHR-ARC-100`) karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 di environment belum diverifikasi.
  - TC-2 (langkah 5) tidak menyebut path atau cara kembali ke halaman Device SKU sesudah membuka Settings > Device; spec berakhir di halaman Settings > Device dan `beforeEach` suite membuka ulang halaman untuk spec berikutnya.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
