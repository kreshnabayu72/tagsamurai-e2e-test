---
id: TC-AC-DS-E2E-023-scope-baris-distributor-sku-principal-read-only
title: "Scope Baris Distributor: SKU Principal Read-only, Isolasi Antar Distributor, Detail, dan Pohon Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-34
  - TC-AC-DS-46
  - TC-AC-DS-78
  - TC-AC-DS-79
coverage:
  web: automated
---

# Scope Baris Distributor: SKU Principal Read-only, Isolasi Antar Distributor, Detail, dan Pohon Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi, Local Registration aktif `totalControlDist_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10, nama tampil `Dewi Lestari`), password `Spectra.env.AC_DS_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): jaringan entitas #24, pohon Category #25, SKU inti #29 (`HHR-ARC-100`) dan seed #30, SKU Distributor #31 (`LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03` milik PT Cakra Distribusi; `NUS-LOC-01` milik PT Nusantara Mitra; `MAN-LOC-01` milik PT Mandala Niaga), riwayat Changelog Distributor #34 (tiga entri Create oleh `Dewi L`). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_DIST_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-34: Distributor melihat SKU Principal read-only dan SKU miliknya

1. Ketik Search `R-`, tekan Enter
2. Verifikasi baris `HHR-ARC-100` (SKU Principal) dan `LOC-NOR-01` (SKU milik Distributor) tampil pada List yang sama
3. Klik ⋯ pada baris `HHR-ARC-100`
4. Verifikasi menu hanya memuat `Detail`; `Edit` dan `Delete` tidak ada
5. Tutup menu aksi
6. Klik ⋯ pada baris `LOC-NOR-01`
7. Verifikasi menu memuat `Detail`, `Edit`, dan `Delete`
8. Tutup menu aksi
9. Hover checkbox baris `HHR-ARC-100`
10. Verifikasi checkbox baris `HHR-ARC-100` tampil (visible) dan berstatus disabled
11. Verifikasi tooltip "You don't have permission to do this." tampil
12. Coba klik checkbox baris `HHR-ARC-100`
13. Verifikasi baris `HHR-ARC-100` tidak tercentang

### TC-AC-DS-79: Distributor membuka Detail SKU Principal

14. Klik SKU `HHR-ARC-100`
15. Verifikasi Popup `Device SKU Detail` terbuka dengan Info Grid SKU `HHR-ARC-100`, Device Name `UHF Handheld Reader`, Brand `Arcturus`, Model/Type `H100`
16. Verifikasi tidak ada tombol Edit atau Delete pada popup
17. Tutup popup dengan ikon close `[✕]`
18. Klik `(←)` pada kotak Search

### TC-AC-DS-46: Pohon Sidebar Category read-only

19. Klik tombol Expand/Collapse All pada Sidebar Category
20. Verifikasi pohon yang tampil sama dengan pohon Principal: `Hardware` dan `TAG` beserta seluruh node
21. Verifikasi tidak ada tombol atau menu untuk menambah, mengubah, atau menghapus Category
22. Klik node `Handheld Reader`
23. Verifikasi List tersaring ke SKU kategori itu, SKU Principal `HHR-ARC-100` dan SKU milik Distributor `LOC-NOR-01` tampil
24. Klik node `Handheld Reader` untuk membatalkan pilihan

### TC-AC-DS-78: Distributor tidak melihat SKU Distributor lain

25. Ketik Search `NUS-LOC-01`, tekan Enter
26. Verifikasi tabel menampilkan "No results found" dan SKU `NUS-LOC-01` tidak tampil
27. Ganti isi kotak search dengan `MAN-LOC-01`, tekan Enter
28. Verifikasi tabel menampilkan "No results found" dan SKU `MAN-LOC-01` tidak tampil
29. Ganti isi kotak search dengan `LOC-NOR-01`, tekan Enter
30. Verifikasi baris `LOC-NOR-01` milik Distributor tampil
31. Klik `(←)` pada kotak Search
32. Klik ikon Changelog
33. Ketik Search `LOC-` pada modal Changelog, tekan Enter
34. Verifikasi modal Changelog Distributor memuat tiga entri Create miliknya (`LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`)
35. Verifikasi modal Changelog tidak memuat entri `NUS-LOC-01` maupun `MAN-LOC-01`
36. Tutup modal Changelog

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-34, TC-79, TC-46, TC-78. TC-79 mengikuti TC-34 karena memakai List hasil Search yang sama; TC-78 diletakkan terakhir karena memakai Search dan modal Changelog.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 (Search `R-` agar baris `HHR-ARC-100` dan `LOC-NOR-01` berada pada satu halaman List, R-16), 3, 6, 9, 12, 14 (membuka menu, hover, klik yang hasilnya diasersi pada langkah berikutnya), 5, 8, 17, 36 (menutup menu, popup, atau modal), 18 dan 31 (mengosongkan Search, S-09), 19, 22 (membuka node), 24 (membatalkan pilihan node, S-09), 25, 27, 29 (Search), 32 dan 33 (membuka modal Changelog dan Search modal agar entri Create `LOC-*` teramati tanpa bergantung pada posisi halaman, S-14).
- Asersi absence langkah 26, 28 didahului hasil "No results found" sebagai anchor dan langkah 30 (pencarian berfungsi); langkah 35 didahului langkah 34 (entri Distributor tampil pada modal yang sama); langkah 21 didahului langkah 20 (pohon tampil).
- Spec melewati sekitar 35 langkah (36 langkah). Alasan pertahanan: seluruh blok memeriksa scope baris dan pohon Category pada halaman Device SKU untuk satu akun Distributor dalam satu kelas (scope entitas, read-only, tanpa seeding dan tanpa mengubah data); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#31/#34 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #10, #24, #29, #31, dan #34 (Activity Log dan Changelog Distributor sebagai data rancangan) di environment belum diverifikasi.
  - TC-34 Expected a ("kedua baris tampil pada List yang sama") tidak menyebut cara membuat kedua baris tampil bersama; spec memakai Search `R-` (kode `HHR-ARC-100` dan `LOC-NOR-01` sama-sama memuat `R-`); perilaku pencocokan substring Search belum diverifikasi.
  - TC-78 Expected c meminta modal Changelog tidak memuat entri Distributor lain tanpa merinci cara memeriksa seluruh halaman; spec memakai Search modal `LOC-` (perilaku Search modal atas kode SKU belum diverifikasi).
  - TC-46 Expected a menyebut "pohon sama dengan Principal"; spec mengasersi pohon Pre-setup #25.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
