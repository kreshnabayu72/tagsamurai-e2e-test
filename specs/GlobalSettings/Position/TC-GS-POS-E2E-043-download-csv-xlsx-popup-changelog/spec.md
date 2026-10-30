---
id: TC-GS-POS-E2E-043-download-csv-xlsx-popup-changelog
title: "Download CSV dan XLSX Popup Changelog: Isi Berkas, Sel Kosong, serta Kepatuhan pada Filter dan Kolom Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-237
  - TC-GS-POS-238
  - TC-GS-POS-239
coverage:
  web: automated
---

# Download CSV dan XLSX Popup Changelog: Isi Berkas, Sel Kosong, serta Kepatuhan pada Filter dan Kolom Tampil

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
  - Manage user and role Create-Only (Sari Dewi) `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), hanya untuk seeding lewat API di hook `before` (Create `Procurement Analyst`), dengan `Spectra.env.GS_CREATE_PASSWORD`. Tidak dipakai login UI.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup: tidak ada yang dipakai.
- Data Dinamis (di-seed lewat API di hook `before` pada entitas Total Control; nama bersuffix per run; fixture baru `Fixture.position.changelogSeed043`). Totalnya 15 entri Changelog seed (13 Create, 1 Edit, 1 Delete) sehingga berkas lintas halaman (10 entri per halaman default):
  - Oleh Budi Santoso: Create 10 Position populasi `iOS Developer {runId}-043`, `Legal Counsel {runId}-043`, `Marketing Executive {runId}-043`, `Quality Assurance Analyst {runId}-043`, `Data Engineer {runId}-043`, `Office Administrator {runId}-043`, `Logistics Coordinator {runId}-043`, `Payroll Specialist {runId}-043`, `Security Officer {runId}-043`, dan `Training Coordinator {runId}-043`.
  - Oleh Budi Santoso: Create `IT Support Specialist {runId}-043`, Edit menjadi `IT Operations Lead {runId}-043`, Create `Temporary Staff {runId}-043`, Delete `Temporary Staff {runId}-043`.
  - Oleh Sari Dewi: Create `Procurement Analyst {runId}-043`.
  - Entri Changelog bersifat audit trail permanen dan tidak dibersihkan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-043` yang masih ada; hapus berkas unduhan yang dibuat spec; kembalikan preferensi Setup Column Changelog ke default (browser) bila masih diubah.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding lewat API dengan sesi Budi dan Sari; penangkapan berkas unduhan browser beserta nama berkasnya; pembacaan isi berkas CSV (baris, header, sel) dan pembacaan berkas XLSX hanya sebatas nama berkas; pembacaan toast yang tampil.
- State global: preferensi Setup Column Changelog (kolom `Modified By` disembunyikan di TC-GS-POS-239) dan Filter Popup Changelog dipulihkan di langkah penghubung; flag Guided Tooltip dipulihkan di `after`.

## Test Steps

### TC-GS-POS-237: Download CSV Popup Changelog

1. Klik ikon Changelog
2. Verifikasi User > Position > Popup Changelog: Position terbuka
3. Klik ikon Download
4. Klik opsi `Download as CSV`
5. Verifikasi tidak ada toast sukses yang tampil
6. Verifikasi berkas `Changelog-Position.csv` terunduh
7. Verifikasi berkas memuat seluruh entri lintas halaman, termasuk ke-15 entri seed `{runId}-043` (13 Create, 1 Edit, 1 Delete) yang melampaui 10 entri halaman 1
8. Verifikasi sel kosong (`—`) ditulis `-` di berkas

### TC-GS-POS-238: Download XLSX Popup Changelog

9. Klik ikon Download
10. Klik opsi `Download as XLSX`
11. Verifikasi tidak ada toast sukses yang tampil
12. Verifikasi berkas `Changelog-Position.xlsx` terunduh

### TC-GS-POS-239: Download mengikuti filter dan kolom tampil

13. Klik ikon Filter
14. Pilih `Delete` pada dropdown `Action`
15. Klik `[Apply]`
16. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
17. Hilangkan centang `Modified By`
18. Klik `[Save]`
19. Klik ikon Download
20. Klik opsi `Download as CSV`
21. Verifikasi berkas CSV terunduh
22. Verifikasi berkas memuat entri Delete `Temporary Staff {runId}-043`
23. Verifikasi berkas hanya memuat entri Delete
24. Verifikasi kolom `Modified By` tidak ikut di berkas
25. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
26. Klik `[Reset to Default]`
27. Klik `[Save]`
28. Klik ikon Filter
29. Klik `[Clear Field]`
30. Klik `[Apply]`
31. Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 237, 238, 239 (urutan TC sumber). TC-GS-POS-239 mengubah Filter dan Setup Column sehingga ditaruh terakhir. Popup Changelog dibuka sekali dan ditutup sekali (langkah 1 dan 31); tidak ada form yang dibuka.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 25 sampai 30 (memulihkan Setup Column ke default, membersihkan Filter) dan penutupan Popup Changelog (langkah 31).
- Label opsi Download adalah `Download as CSV` dan `Download as XLSX` (PRD §4.1 #13, NC-17); TC menulis "opsi CSV" dan "opsi XLSX".
- Berkas CSV kedua (langkah 20) memakai nama dasar yang sama dengan berkas pertama; yang dibaca adalah berkas unduhan terbaru.
- Asersi absence toast sukses (langkah 5 dan 11) ditulis segera sesudah klik opsi format dan sebelum `Verifikasi` berkas terunduh (konvensi bagian 8b butir 11 dan butir 5); urutan ini menyimpang dari urutan Expected TC-GS-POS-237 dan 238 (berkas dulu, toast kemudian). Klik opsi format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 6 dan 12).
- Asersi tambahan di luar Expected TC-GS-POS-239 (langkah 21 dan 22). Langkah 21 (berkas CSV terunduh) adalah prasyarat membuka berkas sebelum Expected a dan b (langkah 23 dan 24) dapat dibaca; TC-GS-POS-239 tidak punya Expected "berkas terunduh". Langkah 22: berkas memuat entri Delete `Temporary Staff {runId}-043`, sebagai baris pembanding supaya "hanya memuat entri Delete" (langkah 23) tidak lulus pada berkas kosong (konvensi bagian 8b butir 2).
- Changelog satu dataset dipertahankan terpisah dari spec 038 sampai 042 (Popup, Filter, Search, Sort, Setup Column): gabungan keenam spec melewati batas ukuran jauh, dan tiap spec men-seed serta membersihkan datanya sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Isi berkas XLSX hanya diasersi sebatas nama berkas dan ketiadaan toast, sesuai Expected TC-GS-POS-238.
- Temuan untuk QA:
  - TC-GS-POS-237 Expected a menyebut "seluruh entri (lintas halaman)" tanpa cara menghitung total entri Changelog entitas (yang bersifat kumulatif dan memuat entri spec lain). Spec mengasersi bahwa ke-15 entri seed `{runId}-043` ada di berkas, termasuk yang melampaui halaman 1; jumlah total baris berkas tidak diasersi.
  - TC-GS-POS-237 dan 239 tidak menyebut header kolom, urutan kolom, atau format tanggal di berkas; spec tidak mengasersinya.
  - TC-GS-POS-239 langkah 2 ("sembunyikan kolom Modified By") tidak menyebut cara; spec memakai Popup Setup Column sesuai TC-GS-POS-231.
  - TC-GS-POS-239 tidak menyebut apakah Filter Panel Popup Changelog tertutup sesudah `[Apply]` (TC-GS-POS-160 sampai 170 untuk tabel utama menyatakan Filter Panel tetap terbuka; Popup Changelog tidak disebut); spec membuka Filter lagi dengan klik ikon Filter sebelum tiap pengisian (langkah 13 dan 28).
  - TC-GS-POS-238 hanya menetapkan nama berkas; TC tidak menyatakan isi XLSX sehingga tidak diasersi.
