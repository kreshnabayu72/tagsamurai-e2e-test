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

  | No | Sub-Tab | Baris | Field | Nilai | Pesan (sel dan Callout) |
  |---|---|---|---|---|---|
  | 1 | Brand | #1 | Brand Name | `Acme 😀` | Brand name contains invalid characters |
  | 2 | Measurement | #1 | Unit Name | `Kilo 😀` | Unit name contains invalid characters |
  | 3 | Measurement | #1 | Symbol | `k😀` | Symbol contains invalid characters |
  | 4 | Position | #1 | Position Name | `Manager 😀` | Position name contains invalid characters |
  | 5 | Division | #2 | Division Name | `Ops 😀` | Division name contains invalid characters |
  | 6 | Division | #2 | Code | `FIN@1` (diketik biasa) | Code contains invalid characters |

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
4. Verifikasi sel field menampilkan Nilai
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
14. Verifikasi sel Code berborder `danger` dengan pesan "Code contains invalid characters" saat itu juga
15. Klik `[Save]`
16. Verifikasi `[Save]` diblokir: sel Code berborder `danger` dengan pesan "Code contains invalid characters"
17. Verifikasi Error Summary Callout memuat baris pesan "Code contains invalid characters" dengan badge "1 row"
18. Verifikasi footer tetap `[Cancel]` dan `[Save]`
19. Klik `[Cancel]`
20. Klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-675: Format Email, Overtime Hours, Emergency Phone

Untuk setiap baris tabel "Format tidak valid" (langkah 21 sampai 29 diulang tiga kali):

21. Buka Sub-Tab User Login
22. Klik `⋯` pada baris #1, pilih `Edit`
23. Ganti isi sel field sesuai kolom Field dengan Nilai
24. Klik `[Save]`
25. Verifikasi `[Save]` diblokir tanpa toast sukses
26. Verifikasi sel field berborder `danger` dengan Pesan sel
27. Verifikasi Error Summary Callout memuat Baris Callout dengan badge "1 row"
28. Verifikasi footer tetap `[Cancel]` dan `[Save]`
29. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (injeksi DOM hanya cara memasukkan nilai ke input, bukan tampering ke server).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 sampai 10 diulang lima kali, langkah 21 sampai 29 diulang tiga kali (parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat). Dengan ekspansi spec berisi sekitar 87 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Save diblokir), tiap blok membuka dan menutup sesi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): `[Cancel]` lalu `[Discard]` (langkah 9, 10, 19, 20, 29) membuang perubahan karena sesi berisi perubahan sehingga dialog Discard Changes pasti tampil.
- Pembagian TC lintas spec: TC-GS-IMPORT-212 sampai 214, 671, 673, 674, dan 842 (Save diblokir) ada di spec 094.
- Temuan untuk QA:
  - TC-GS-IMPORT-672 Expected a membedakan varian 1 sampai 5 (hanya nilai tampil) dan varian 6 (pesan live); spec mengikuti pembagian itu dan tidak mengasersi pesan sebelum `[Save]` pada varian 1 sampai 5.
  - TC-GS-IMPORT-672 Expected b menyebut baris Callout "yang sama" dengan pesan sel, sedangkan pada TC-GS-IMPORT-671 baris Callout memakai awalan nama field; spec menulis pesan persis seperti TC.
  - Injeksi value langsung ke DOM bergantung pada kemampuan runner; disediakan tim FE.
  - Post Condition kedua TC kosong; tidak ada yang diasersi.
