---
id: TC-GS-IMPORT-E2E-088-duplicate-antara-draft-lama-dan-berkas-append-client-a-d-01
title: "Duplicate antara draft lama dan berkas Append (Client A, D-01)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-187
coverage:
  web: automated
---

# Duplicate antara draft lama dan berkas Append (Client A, D-01)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: draft dasar Client A D-01 (Draft Brand 12 baris `pending` dari `brand-12.csv`, baris #1 `Acme Corp`; dibuat ulang ke kondisi Population oleh hook `beforeEach` sesuai Kontrak Fixture R2; nama literal karena asersi bergantung pada isi D-01). Berkas `brand-mutual-append.csv`: header `Brand Name`; 1 baris data `Acme Corp`.
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip pemulihan draft D-01 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Brand Client A dipulihkan ke D-01 lewat skrip pemulihan.

## Test Steps

### TC-GS-IMPORT-187: Duplicate antara draft lama dan berkas Append

1. Klik `[Upload File]`
2. Pilih berkas `brand-mutual-append.csv` pada file picker
3. Klik `[Append Records]` pada dialog "Append to Draft"
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi badge Status baris #1 `Acme Corp` bertuliskan `duplicate`
6. Arahkan kursor ke badge Status baris #1
7. Verifikasi tooltip pada badge Status baris #1: "This row duplicates another row in this draft. It will be skipped automatically."
8. Klik halaman 2 pada Pagination Staging Table
9. Verifikasi badge Status baris #13 `Acme Corp` hasil Append bertuliskan `pending`
10. Verifikasi Staging Metric Cards: Total Rows 13 (Active), Ready to Import 12, Errors 0 (Disabled), Duplicates 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Spec satu TC dengan satu alur; tidak digabung dengan spec Append lain karena alur Append milik slice lain memakai data berbeda.
- Urutan Expected TC (a badge dan tooltip, b baris #13, c kartu) diikuti; asersi tooltip (langkah 7) diletakkan sebelum pindah halaman (butir 5 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-187 Dependensi mencantumkan `TC-GS-IMPORT-1` (draft D-01); spec menyiapkan D-01 sendiri lewat hook `beforeEach` dan tidak menumpang hasil TC lain.
  - Post Condition ("Draft Brand Client A dipulihkan ke D-01") adalah pemulihan oleh fixture, bukan observasi; dikerjakan hook `after` dan tidak diasersi (S-01).
  - Skrip pemulihan draft D-01 (Kontrak Fixture R2) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
