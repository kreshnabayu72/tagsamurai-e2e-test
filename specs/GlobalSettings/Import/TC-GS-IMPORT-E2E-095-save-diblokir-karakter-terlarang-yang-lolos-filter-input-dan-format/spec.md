---
id: TC-GS-IMPORT-E2E-095-save-diblokir-karakter-terlarang-yang-lolos-filter-input-dan-format
title: "Save diblokir: karakter terlarang yang lolos filter input dan format Email, Overtime Hours, Emergency Phone"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-672
  - TC-GS-IMPORT-675
coverage:
  web: automated
---

# Save diblokir: karakter terlarang yang lolos filter input dan format Email, Overtime Hours, Emergency Phone

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum spec: D-01 (Draft Brand 12 baris), D-02 (Measurement 6 baris), D-03 (Position 6 baris), D-04 (Division 6 baris), D-05 (User Login 8 baris `pending`; Custom Field Active Overtime Hours (Numeric 2 desimal) dan Emergency Phone (Phone)).
- Tabel "Karakter terlarang" (TC-672; nilai dimasukkan lewat injeksi value langsung ke DOM sehingga melewati filter input FE, kecuali varian 6 yang diketik biasa):

  | No | Sub-Tab | Baris | Field | Nilai | Nilai tampil | Pesan (sel dan Callout) |
  |---|---|---|---|---|---|---|
  | 1 | Brand | #1 | Brand Name | `Acme 😀` | `Acme 😀` | Brand name contains invalid characters |
  | 2 | Measurement | #1 | Unit Name | `Kilo 😀` | `Kilo 😀` | Unit name contains invalid characters |
  | 3 | Measurement | #1 | Symbol | `k😀` | `k😀` | Symbol contains invalid characters |
  | 4 | Position | #1 | Position Name | `Manager 😀` | `Manager 😀` | Position name contains invalid characters |
  | 5 | Division | #2 | Division Name | `Ops 😀` | `Ops 😀` | Division name contains invalid characters |
  | 6 | Division | #2 | Code | `FIN@1` (diketik biasa) | `FIN@1` | Code contains invalid characters |

- Tabel "Format tidak valid" (TC-675; Sub-Tab User Login, baris #1):

  | No | Field | Nilai | Pesan sel | Baris Callout |
  |---|---|---|---|---|
  | 1 | Email | `ahmad.fauzi@` | Invalid email format | Invalid email format |
  | 2 | Custom Field Overtime Hours | `1.234` | Overtime hours must have at most 2 decimal places | Overtime hours must have at most 2 decimal places |
  | 3 | Custom Field Emergency Phone | Country Code `🇮🇩 +62`, Number `123` | Min. 4 characters | Emergency phone: Min. 4 characters |
- Kemampuan teknis: injeksi value langsung ke DOM pada input sel (melewati filter input FE; disediakan tim FE), pengamatan toast, skrip pemulihan draft (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01 sampai D-05 dan lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-672: Karakter terlarang yang melewati filter input (varian 1 sampai 5)

Untuk setiap baris No 1 sampai 5 tabel "Karakter terlarang" (langkah 1 sampai 10 diulang lima kali):

1. Buka Sub-Tab sesuai kolom Sub-Tab
2. Klik `⋯` pada baris sesuai kolom Baris, pilih `Edit`
3. Ganti isi sel field sesuai kolom Field dengan Nilai lewat injeksi value langsung ke DOM
4. Verifikasi sel field menampilkan nilai sesuai kolom Nilai tampil
5. Klik `[Save]`
6. Verifikasi `[Save]` diblokir: sel field berborder `danger` dengan Pesan
7. Verifikasi Error Summary Callout memuat baris pesan sesuai Pesan dengan badge "1 row"
8. Verifikasi footer tetap `[Cancel]` dan `[Save]`
9. Klik `[Cancel]`
10. Klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-672: Karakter terlarang diketik biasa (varian 6)

11. Buka Sub-Tab Division
12. Klik `⋯` pada baris #2, pilih `Edit`
13. Ganti isi sel Code baris #2 dengan `FIN@1` (diketik biasa)
14. Verifikasi sel Code baris #2 menampilkan `FIN@1`
15. Verifikasi sel Code berborder `danger` saat itu juga
16. Verifikasi sel Code menampilkan pesan "Code contains invalid characters" saat itu juga
17. Klik `[Save]`
18. Verifikasi `[Save]` diblokir: sel Code berborder `danger` dengan pesan "Code contains invalid characters"
19. Verifikasi Error Summary Callout memuat baris pesan "Code contains invalid characters" dengan badge "1 row"
20. Verifikasi footer tetap `[Cancel]` dan `[Save]`
21. Klik `[Cancel]`
22. Klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-675: Format Email, Overtime Hours, Emergency Phone

Untuk setiap baris tabel "Format tidak valid" (langkah 23 sampai 31 diulang tiga kali):

23. Buka Sub-Tab User Login
24. Klik `⋯` pada baris #1, pilih `Edit`
25. Ganti isi sel field sesuai kolom Field dengan Nilai
26. Klik `[Save]`
27. Verifikasi `[Save]` diblokir tanpa toast sukses
28. Verifikasi sel field berborder `danger` dengan Pesan sel
29. Verifikasi Error Summary Callout memuat Baris Callout dengan badge "1 row"
30. Verifikasi footer tetap `[Cancel]` dan `[Save]`
31. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (injeksi DOM hanya cara memasukkan nilai ke input, bukan tampering ke server).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 sampai 10 diulang lima kali, langkah 23 sampai 31 diulang tiga kali (parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat). Dengan ekspansi spec berisi 89 langkah (10 × 5 + 12 + 9 × 3). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Save diblokir), tiap blok membuka dan menutup sesi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): `[Cancel]` lalu `[Discard]` (langkah 9, 10, 21, 22, 31) membuang perubahan karena sesi berisi perubahan sehingga dialog Discard Changes pasti tampil.
- Pembagian TC lintas spec: TC-GS-IMPORT-212 sampai 214, 671, 673, 674, dan 842 (Save diblokir) ada di spec 094.
- Temuan untuk QA:
  - TC-GS-IMPORT-672 Expected a: setiap varian (1 sampai 6) menampilkan nilainya di sel sebelum `[Save]` (kolom Nilai tampil; langkah 4 untuk varian 1 sampai 5, langkah 14 untuk varian 6); hanya varian 6 menampilkan pesan live (langkah 15 dan 16). Pesan sebelum `[Save]` pada varian 1 sampai 5 tidak diasersi.
  - TC-GS-IMPORT-672 Expected b menyebut baris Callout "yang sama" dengan pesan sel, sedangkan pada TC-GS-IMPORT-671 baris Callout memakai awalan nama field; spec menulis pesan persis seperti TC.
  - Injeksi value langsung ke DOM bergantung pada kemampuan runner; disediakan tim FE.
  - Post Condition kedua TC kosong; tidak ada yang diasersi.
