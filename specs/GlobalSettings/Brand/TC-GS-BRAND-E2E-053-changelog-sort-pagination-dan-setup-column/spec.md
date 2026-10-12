---
id: TC-GS-BRAND-E2E-053-changelog-sort-pagination-dan-setup-column
title: "Changelog Brand: Sort, Pagination, dan Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-179
  - TC-GS-BRAND-180
  - TC-GS-BRAND-181
coverage:
  web: automated
---

# Changelog Brand: Sort, Pagination, dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`, urutan sebagai berikut):
  - Population D-01: 12 brand dengan nama literal `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics` (setara TC-GS-BRAND-1). Menghasilkan lebih dari 10 entri Create, cukup untuk Next, ukuran halaman 25, dan agar baris `—` pada sort Old Value dan New Value berada di halaman terakhir (Changelog append-only, jumlah entri Create tidak berkurang).
  - Brand `Log Edit Co {runId}-053` dibuat lalu diubah namanya menjadi `Log Edit Co Renamed {runId}-053` (entri Edit dengan Old Value dan New Value berisi nilai, bukan `—`).
  - Brand `Log Del Co {runId}-053` dibuat lalu dihapus (entri Delete dengan Old Value berisi nilai dan New Value `—`).
  - Dengan data ini kolom Old Value campuran (`—` pada Create, nilai pada Edit dan Delete) dan kolom New Value campuran (`—` pada Delete, nilai pada Create dan Edit), sehingga pada sort ascending baris bernilai ada di halaman pertama dan baris `—` ada di halaman terakhir.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus 12 brand Population dan brand `Log Edit Co Renamed {runId}-053` lewat API; pulihkan konfigurasi kolom Changelog ke default (kolom Field tampil) lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel Changelog bila langkah pemulihan di spec tidak sempat jalan. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: pindah ke halaman terakhir lewat Pagination (nomor halaman terakhir); membaca dan menghapus key `localStorage` browser.
- Precondition TC-GS-BRAND-179, 180, 181: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand. TC-GS-BRAND-180 bergantung pada Population (TC-GS-BRAND-1) yang di-seed di `before`.
- State global yang dipulihkan: konfigurasi Setup Column Changelog (kolom Field) disimpan di `localStorage` browser dengan key unik per tabel (PRD brand.md §4.2h; prd-conventions.md §9.3), bukan per user. Dipulihkan di langkah 29 dan di hook `after` sebagai cadangan lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel Changelog.

## Test Steps

### TC-GS-BRAND-179: Sort Changelog: Date, kolom teks, dan kolom Old/New Value campuran

1. Klik icon Changelog di halaman Global Settings > Master Reference > Brand → modal Changelog tampil
2. Klik header Date
3. Verifikasi Date ascending: tanggal tertua di atas
4. Klik header Brand Name
5. Verifikasi Brand Name ascending A-Z
6. Klik header Old Value
7. Verifikasi Old Value ascending: baris pertama pada halaman 1 bernilai (bukan `—`), yaitu baris bernilai lebih dulu
8. Pindah ke halaman terakhir pada Pagination
9. Verifikasi Old Value ascending: baris `—` (Create) berada di akhir pada halaman terakhir
10. Pindah ke halaman 1 pada Pagination
11. Klik header New Value
12. Verifikasi New Value ascending: baris pertama pada halaman 1 bernilai (bukan `—`), yaitu baris bernilai lebih dulu
13. Pindah ke halaman terakhir pada Pagination
14. Verifikasi New Value ascending: baris `—` (Delete) berada di akhir pada halaman terakhir

### TC-GS-BRAND-180: Pagination Modal Changelog

15. Pindah ke halaman 1 pada Pagination
16. Klik Next pada Pagination modal Changelog
17. Verifikasi navigasi berjalan ke halaman berikutnya
18. Ubah ukuran halaman menjadi 25
19. Verifikasi ukuran halaman 25 diterapkan

### TC-GS-BRAND-181: Setup Column Modal Changelog dua tingkat

20. Klik header Column Visibility (⋯) di Changelog
21. Klik `Setup Column...`
22. Verifikasi overlay Setup Column berisi 7 kolom Changelog (Date, Action, Brand Name, Field, Old Value, New Value, Modified By)
23. Verifikasi footer modal Setup Column memuat `[Reset to Default]` dan `[Save]`
24. Uncheck kolom Field
25. Klik [Save]
26. Verifikasi kolom Field hilang dari tabel Changelog
27. Tutup modal Changelog lewat `[✕]`, lalu buka kembali lewat icon Changelog
28. Verifikasi kolom Field tetap hilang (bertahan setelah ditutup-buka)
29. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik [Save]

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. Modal Changelog dibuka sekali untuk TC-GS-BRAND-179 dan 180 (precondition sama); TC-GS-BRAND-181 dijalankan terakhir karena mengubah konfigurasi kolom.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 dan 15 (kembali ke halaman 1 sebelum sort berikutnya dan sebelum Next, karena halaman terakhir dari langkah 8 dan 13 tidak punya Next), dan langkah 29 (pemulihan konfigurasi kolom; hook `after` sebagai cadangan). Langkah 27 (tutup-buka modal) bukan penghubung: dasarnya Expected c TC-GS-BRAND-181.
- Langkah 7 dan 12 mewujudkan frasa "baris bernilai lebih dulu" pada Expected c dan d TC-GS-BRAND-179 pada halaman 1; langkah 9 dan 14 mewujudkan "`—` di akhir pada halaman terakhir".
- TC-GS-BRAND-181 mengacu keputusan NC-01 (Setup Column dua tingkat: header Column Visibility lalu `Setup Column...`).
