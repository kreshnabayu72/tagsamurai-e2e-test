---
id: TC-GS-BRAND-E2E-050-changelog-screening-hover-dan-search
title: "Changelog Brand: Screening, Hover Modified By, dan Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-168
  - TC-GS-BRAND-169
  - TC-GS-BRAND-173
  - TC-GS-BRAND-174
coverage:
  web: automated
---

# Changelog Brand: Screening, Hover Modified By, dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`, setara TC-GS-BRAND-1):
  - Population D-01: 12 brand dengan nama literal `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics`, menghasilkan entri Changelog Action Create oleh `Sari D` (Old Value `—`).
  - Brand pembantu `Log Del Co {runId}-050` dibuat lalu langsung dihapus (Action Delete, New Value `—`), dilakukan sesudah Population supaya entri Delete menjadi entri terbaru.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus 12 brand Population lewat API. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: hover (tooltip); membaca tanggal hari uji dari baris Changelog (format tampilan kolom Date).
- Precondition TC-GS-BRAND-168, 169, 173, 174: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand. TC-GS-BRAND-168, 173 bergantung pada Population (TC-GS-BRAND-1) yang di-seed di `before`.
- State global yang dipulihkan: tidak ada (spec hanya membaca).

## Test Steps

### TC-GS-BRAND-168: Screening Modal Changelog: Brand

1. Klik icon Changelog di halaman Global Settings > Master Reference > Brand → modal Changelog tampil
2. Verifikasi bagian Header: Title `Changelog: Brand`
3. Verifikasi bagian Header: tombol `[✕]`
4. Verifikasi bagian Header: Table Tools `Search | Filter | Download`
5. Verifikasi bagian Body: kolom `Date (sortable) | Action (sortable) | Brand Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`
6. Verifikasi bagian Body: baris terurut Date terbaru di atas
7. Verifikasi bagian Body: kolom Action berupa plain text (bukan badge)
8. Verifikasi bagian Body: Old Value pada baris Action Create tampil `—`
9. Verifikasi bagian Body: New Value pada baris Action Delete tampil `—`
10. Verifikasi bagian Footer: Pagination dengan opsi ukuran halaman 10/25/50/100
11. Verifikasi bagian Footer: ukuran halaman default 10

### TC-GS-BRAND-169: Hover Modified By menampilkan nama lengkap

12. Hover `Sari D` pada kolom Modified By di modal Changelog yang sama
13. Verifikasi Tooltip `Sari Dewi`

### TC-GS-BRAND-173: Search Changelog kelas kolom teks

14. Klik icon Search pada Table Tools Changelog
15. Verifikasi placeholder `Search action, brand, or user...`
16. Search `create`, tekan Enter
17. Verifikasi hasil memuat baris Action Create
18. Search `Apex`, tekan Enter
19. Verifikasi hasil memuat baris yang Brand Name / New Value-nya memuat Apex Tools
20. Search `sari`, tekan Enter
21. Verifikasi hasil memuat baris Modified By `Sari D`

### TC-GS-BRAND-174: Search nilai Date Changelog tidak mencocokkan baris

22. Salin teks tanggal hari uji dari kolom Date salah satu baris yang tampil (format yang tampil di kolom itu)
23. Search teks tanggal yang disalin, tekan Enter
24. Verifikasi pesan `No results found`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Changelog dibuka sekali di langkah 1 dan dipakai berurutan untuk TC-GS-BRAND-169, 173, 174 (precondition keempat TC sama: Total Control di halaman Brand; langkah "Buka Changelog" TC-169, 173, 174 sudah terpenuhi oleh langkah 1). Urutan TC sumber dipertahankan.
- Langkah 9 (New Value `—` pada baris Delete) bergantung pada brand pembantu yang dihapus di `before`; kebutuhan ini tercatat di Prerequisites (seeding `Log Del Co {runId}-050`).
- Langkah penghubung: langkah 22 (menyalin teks tanggal hari uji dari kolom Date sebagai nilai ketik langkah 23).
- Population D-01 di-seed ulang di tiap spec Changelog dengan nama literal sehingga Changelog Client A akan memuat banyak entri Create/Delete bernama sama dari run dan spec lain. Asersi pada spec ini tidak menghitung jumlah baris sehingga tidak terpengaruh.
