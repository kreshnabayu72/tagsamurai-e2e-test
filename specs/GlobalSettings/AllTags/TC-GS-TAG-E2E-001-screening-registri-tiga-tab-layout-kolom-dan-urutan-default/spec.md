---
id: TC-GS-TAG-E2E-001-screening-registri-tiga-tab-layout-kolom-dan-urutan-default
title: "Screening Registri TAG: Tab All, Paired, Not Paired (Header, Toolbar, Kolom, Footer) dan Urutan Default Code A-Z"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-1
  - TC-GS-TAG-2
  - TC-GS-TAG-3
  - TC-GS-TAG-4
coverage:
  web: automated
---

# Screening Registri TAG: Tab All, Paired, Not Paired (Header, Toolbar, Kolom, Footer) dan Urutan Default Code A-Z

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca): Seed Registri A (DD-01 s.d. DD-30; 30 baris, Paired 4, Not Paired 26), plan Growth, format tanggal default General Settings Client A (`dd/MM/yy`, 24-hour). Seed Registri A di-seed ulang idempotent oleh hook `before` sebelum aksi pertama (mekanisme reset disediakan tim FE/BE; identifier tetap, Q-4). Hitungan 30/4/26 valid hanya pada Seed Registri A utuh.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Spec tidak membuat, mengubah, atau menghapus data. Suite berjalan serial (`parallel: false`).
- Selektor: PRD hanya menetapkan target Guided Tooltip (`#license-counter-cards`, `#tag-tabs`, `#tag-table-toolbar`); selektor elemen lain (ikon `[?]`, header kolom, footer pagination) belum ada di sumber dan diselesaikan tim FE di tahap script (tidak dikarang di spec).

## Test Steps

### TC-GS-TAG-1: Screening halaman registri Tab All

1. Amati header, kartu counter, toolbar, tabel, dan pagination dari atas ke bawah
2. Verifikasi Breadcrumb `TAG` tampil sebagai satu segmen
3. Verifikasi tidak ada Page Title terpisah
4. Verifikasi ikon `[?]` tampil tepat di kanan Breadcrumb
5. Verifikasi Tab `All` (aktif), `Paired`, `Not Paired`
6. Verifikasi kartu counter `RFID – Object TAG`, `RFID – User TAG`, `NFC`, `BLE`, `GPS` tampil
7. Verifikasi tidak ada kartu QR
8. Verifikasi Table Tools `Search by Scan`, `Search`, `Filter`, `Download`, `Event Log`, `Audit TAG`, `Delete by Scan`, `+ Activate TAG` tampil
9. Verifikasi kolom tampil default `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, `Last Scanned` sortable dan `Column Visibility (⋯)` unsortable
10. Verifikasi kolom `Last Scanned In`, `Activated At`, `Last User` tidak tampil
11. Verifikasi tidak ada kolom checkbox
12. Verifikasi baris diurutkan Code A-Z
13. Verifikasi footer pagination `Showing 1 - 10 of 30 TAGs`
14. Verifikasi footer `Rows per page: 10`

### TC-GS-TAG-4: Urutan default Code A-Z dan isi tiap halaman pagination Tab All

15. Amati urutan baris halaman 1
16. Verifikasi halaman 1 (10 baris) berurutan: `04A224B2C15E80`, `04A224B2C15E82`, `04A224B2C15E83`, `356938035643501`, `AABBCCDDEE80`, `E2801160600002054D8A0001`, `E2801160600002054D8A0002`, `E2801160600002054D8A0006`, `E2801160600002054D8A0007`, `E2801160600002054D8A0008`
17. Verifikasi header kolom `Code` menampilkan indikator sort Ascending
18. Pindah ke halaman 2
19. Verifikasi halaman 2 (10 baris) berurutan: `E2801160600002054D8A0011`, `E2801160600002054D8A0012`, `E28011606000020F00000001`, `E28011606000020F00000002`, `E28011606000020F00000003`, `E28011606000020F00000004`, `E28011606000020F00000005`, `E28011606000020F00000006`, `E28011606000020F00000007`, `E28011606000020F00000008`
20. Pindah ke halaman 3
21. Verifikasi halaman 3 (10 baris) berurutan: `E28011606000020F00000009`, `E28011606000020F00000010`, `E28011606000020F00000011`, `E28011606000020F00000012`, `E28011606000020F00000013`, `E28011606000020F00000014`, `E28011606000020F00000015`, `E28011606000020F00000016`, `TAG-QR-00512`, `TAG-QR-00611`

### TC-GS-TAG-2: Screening halaman registri Tab Paired

22. Klik Tab Paired
23. Verifikasi Tab `All`, `Paired` (aktif), `Not Paired`
24. Verifikasi kartu counter tidak tampil
25. Verifikasi Table Tools `Search by Scan`, `Search`, `Filter`, `Download` tampil
26. Verifikasi `Event Log`, `Audit TAG`, `Delete by Scan`, `+ Activate TAG` Hidden
27. Verifikasi kolom `Status` tidak tampil
28. Verifikasi tidak ada kolom checkbox
29. Verifikasi 4 baris tampil berurutan Code A-Z: `04A224B2C15E82`, `E2801160600002054D8A0001`, `TAG-QR-00512`, `TAG-QR-00611`
30. Verifikasi footer `Showing 1 - 4 of 4 TAGs`

### TC-GS-TAG-3: Screening halaman registri Tab Not Paired

31. Klik Tab Not Paired
32. Verifikasi Tab `All`, `Paired`, `Not Paired` (aktif)
33. Verifikasi Health Counter Card `RFID – Object TAG`, `RFID – User TAG`, `NFC`, `BLE`, `GPS` tampil
34. Verifikasi Table Tools `Search by Scan`, `Search`, `Filter`, `Download`, `Event Log`, `Audit TAG`, `Delete by Scan`, `+ Activate TAG` tampil
35. Verifikasi kolom checkbox seleksi tampil sebagai kolom pertama
36. Verifikasi kolom `Status` tampil
37. Verifikasi footer `Showing 1 - 10 of 26 TAGs`
38. Verifikasi baris `Reserved` (`E2801160600002054D8A0006`) tidak punya checkbox (Hidden)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 1a). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-4 ditaruh sebelum TC-2 dan TC-3 karena TC-1 dan TC-4 memakai Tab All dengan sort default dan halaman 1; pindah tab Paired lalu Not Paired mereset kondisi Tab All (S-10). Urutan sumber TC-1, TC-2, TC-3, TC-4.
- Langkah 1, 15, 18, 20 (amati dan pindah halaman) adalah langkah penghubung tanpa `Verifikasi` (S-03).
- Alasan spec melewati sekitar 35 langkah (38): empat blok screening baca-saja pada satu dataset (Seed Registri A), satu kelas harness (tanpa kelas khusus), tiap blok berdiri sendiri (pindah tab mereset tampilan) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; urutan halaman TC-4 memuat 30 identifier yang diasersi per halaman sebagai satu klausa urutan.
- Temuan untuk QA:
  - TC-1 butir b.i memakai notasi `Column Visibility (⋯) (unsortable)` untuk kolom Actions; label kolom di aplikasi tidak ditetapkan di TC. Spec mengikuti teks TC.
  - TC-3 butir a menyebut "Health Counter Card" tanpa nilai kartu pada langkah ini (nilai ada di TC-14, spec 003); spec hanya mengasersi keberadaan kelima kartu.
  - Post Condition semua TC bernilai `-`; tidak ada yang diasersi.
