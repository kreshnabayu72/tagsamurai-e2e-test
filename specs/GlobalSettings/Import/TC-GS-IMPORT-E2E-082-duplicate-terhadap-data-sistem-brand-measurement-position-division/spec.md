---
id: TC-GS-IMPORT-E2E-082-duplicate-terhadap-data-sistem-brand-measurement-position-division
title: "Duplicate terhadap data sistem: Brand, Measurement, Position, Division (tooltip, status, kartu Duplicates) dan nama sistem yang muncul dua kali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-173
  - TC-GS-IMPORT-174
  - TC-GS-IMPORT-175
  - TC-GS-IMPORT-176
  - TC-GS-IMPORT-177
  - TC-GS-IMPORT-178
  - TC-GS-IMPORT-828
coverage:
  web: automated
---

# Duplicate terhadap data sistem: Brand, Measurement, Position, Division (tooltip, status, kartu Duplicates) dan nama sistem yang muncul dua kali

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini): Brand `Samsung`; Measurement `Kilogram` (Symbol `kg`); Position `Store Manager`; Division `Engineering` (Code `ENG`). Client C tanpa draft pada tiap Sub-Tab sebelum tiap TC (Kontrak Fixture R1; dipenuhi hook `beforeEach` dan langkah reset di spec ini, mekanisme skrip reset disediakan tim FE/BE).
- Data Dinamis (berkas fixture uji, D-07; isi mengikuti Data Uji TC). Nilai baris literal karena draft tidak di-commit, dibuang oleh reset, dan asersi bergantung pada kecocokan nama dengan data Pre-setup:

  Tabel "Berkas duplikat terhadap sistem":

  | TC | Sub-Tab | Berkas | Header | Baris 1 / Baris 2 / Baris 3 | Tooltip badge Status baris 2 |
  |---|---|---|---|---|---|
  | 173 | Brand | `brand-dup-sys.csv` | `Brand Name` | `Pioneer Electronics` / `Samsung` / `Nexus Tech` | "Brand name already exists. This row will be skipped automatically." |
  | 174 | Brand | `brand-dup-case.csv` | `Brand Name` | `Pioneer Electronics` / `SAMSUNG` / `Nexus Tech` | "Brand name already exists. This row will be skipped automatically." |
  | 175 | Brand | `brand-dup-trim.csv` | `Brand Name` | `Pioneer Electronics` / `  Samsung  ` (dua spasi di kiri dan di kanan) / `Nexus Tech` | "Brand name already exists. This row will be skipped automatically." |
  | 176 | Measurement | `measurement-dup-sys.csv` | `Unit Name,Symbol` | `Meter,m` / `Kilogram,kg` / `Liter,L` | "Unit name already exists. This row will be skipped automatically." |
  | 177 | Position | `position-dup-sys.csv` | `Position Name` | `Teknisi Gudang` / `Store Manager` / `Kepala Shift` | "Position name already exists. This row will be skipped automatically." |
  | 178 | Division | `division-dup-sys.csv` | `Division Name,Code` | `Logistik,LOG` / `Engineering,` (Code kosong) / `Keuangan,KEU` | "Division name already exists. This row will be skipped automatically." |

  Berkas TC-828 `brand-dup-sys-mutual.csv`: header `Brand Name`; 4 baris data: `Pioneer Electronics` / `Samsung` / `Nexus Tech` / `Samsung`.
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip reset draft per Sub-Tab (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Sub-Tab Brand, Measurement, Position, dan Division Client C dibuang lewat skrip reset.

## Test Steps

### TC-GS-IMPORT-173 sampai TC-GS-IMPORT-178: Duplicate terhadap data sistem

Untuk setiap baris tabel "Berkas duplikat terhadap sistem" (langkah 1 sampai 12 diulang enam kali, urutan 173 sampai 178):

1. Tunggu toast lama hilang otomatis; pilih Sub-Tab sesuai kolom Sub-Tab; reset draft Sub-Tab itu di Client C lewat skrip reset, lalu muat ulang halaman
2. Klik `[Upload File]`
3. Pilih berkas sesuai kolom Berkas pada file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal Column Mapping tertutup
6. Verifikasi muncul toast: "Success, row has been added."
7. Verifikasi Staging Table menampilkan 3 baris
8. Verifikasi badge Status baris 2 bertuliskan `duplicate`
9. Verifikasi badge Status baris 1 dan baris 3 bertuliskan `pending`
10. Arahkan kursor ke badge Status baris 2
11. Verifikasi tooltip pada badge Status baris 2 sesuai kolom Tooltip tabel
12. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-828: Nama sistem muncul dua kali dalam berkas

13. Tunggu toast lama hilang otomatis; pilih Sub-Tab Brand; reset draft Brand Client C lewat skrip reset, lalu muat ulang halaman
14. Klik `[Upload File]`
15. Pilih berkas `brand-dup-sys-mutual.csv` pada file picker
16. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
17. Verifikasi modal Column Mapping tertutup
18. Verifikasi muncul toast: "Success, row has been added."
19. Verifikasi Staging Table menampilkan 4 baris
20. Verifikasi badge Status baris 2 dan baris 4 bertuliskan `duplicate`
21. Verifikasi badge Status baris 1 dan baris 3 bertuliskan `pending`
22. Arahkan kursor ke badge Status baris 2
23. Verifikasi tooltip pada badge Status baris 2: "Brand name already exists. This row will be skipped automatically."
24. Arahkan kursor ke badge Status baris 4
25. Verifikasi tooltip pada badge Status baris 4: "Brand name already exists. This row will be skipped automatically."
26. Verifikasi Staging Metric Cards: Total Rows 4 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 2

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (tanpa harness khusus).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1-12 diulang enam kali (satu putaran per baris tabel Prerequisites, tanpa langkah bersyarat); nomor langkah TC-828 (13 sampai 26) dihitung setelah satu putaran. Bila dihitung dengan ekspansi, spec berisi sekitar 86 langkah (12 langkah kali 6 putaran ditambah 14 langkah TC-828). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional), tiap blok berdiri sendiri dengan reset draft dan unggah sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan langkah 13 (menunggu toast lama hilang, pemilihan Sub-Tab, reset draft, muat ulang) menjalankan Precondition "Client C tanpa draft Tab X (fixture direset sebelum TC, Kontrak Fixture R1)".
- Verifikasi per klausa Expected: a (langkah 5, 6), b (langkah 7, 8, 9), c (langkah 10, 11), d (langkah 12); TC-828 a (17, 18), b (19, 20, 21), c (22, 23), d (24, 25), e (26). Klausa hover diasersi sebelum langkah berikutnya yang mengubah state tooltip (butir 5 bagian 8b).
- Pembagian TC lintas spec: TC-GS-IMPORT-179 sampai 181 (Email) ada di spec 083, TC-GS-IMPORT-182 sampai 184 (Employee ID) di spec 084.
- Temuan untuk QA:
  - Post Condition tiap TC ("Draft ... berisi 3 baris (2 `pending`, 1 `duplicate`), direset sebelum TC berikutnya") tidak punya langkah observasi di TC dan padanan Expected-nya sudah diasersi pada Expected d; tidak diasersi terpisah (S-01). Pembersihan draft dikerjakan langkah 1 dan 13 serta hook `after`.
  - Mekanisme skrip reset draft per Sub-Tab (Kontrak Fixture R1) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - Nama env `GS_CLIENTC_TC_PASSWORD` sudah terdaftar di `.env.example` untuk akun `totalControl_automated_qaTeam3@qwertysystem.net`.
