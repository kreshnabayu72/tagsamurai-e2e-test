---
id: TC-GS-IMPORT-E2E-179-volume-batas-10000-baris-staging-ditegakkan-server-pada-permintaan
title: "Volume: batas 10000 baris Staging ditegakkan server pada permintaan langsung (draft 9995 baris, +10 ditolak 422 all-or-nothing)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-533
coverage:
  web: automated
---

# Volume: batas 10000 baris Staging ditegakkan server pada permintaan langsung (draft 9995 baris, +10 ditolak 422 all-or-nothing)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client C dibagikan ke seluruh admin dan draft 9995 baris memakai Sub-Tab Brand Client C yang dibagikan dengan spec volume lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client C dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan token sesi akun aktor (asersi hanya respons server dan state data, butir 1 bagian 8b); skrip seed draft Brand 9995 baris (D-16, `Brand 00001` sampai `Brand 09995`) pada Client C (volume >= 100 baris).
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris literal): D-16 draft Brand 9995 baris `pending` Client C; `brand-10.csv`: header `Brand Name`; 10 baris `Brand Baru 01` sampai `Brand Baru 10`.
- Pemulihan (hook `after`): hapus draft Brand Client C dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-533: Batas 10000 baris ditegakkan di server pada permintaan langsung

1. Reset Client C lewat skrip fixture dan seed draft Brand D-16 (9995 baris `pending`)
2. Muat ulang halaman Import > Brand
3. Kirim permintaan Confirm Mapping langsung ke server dengan token akun Total Control Client C dan berkas `brand-10.csv`
4. Verifikasi server menolak permintaan dengan 422 all-or-nothing
5. Muat ulang halaman Import > Brand
6. Verifikasi kartu Total Rows tetap 9995 (tidak ada dari 10 baris yang masuk)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data (e) (draft 9995 baris sebagai volume, di atas ambang 100 baris), dengan irisan defense-in-depth (a) karena permintaan langsung ke server; volume dominan sehingga tidak dipisah.
- Spec singkat (6 langkah) sehingga tidak melewati sekitar 35 langkah.
- Langkah penghubung (tanpa `Verifikasi`): seeding (langkah 1), muat ulang halaman Import > Brand (langkah 2 dan 5). Asersi pada request langsung hanya respons server dan state data (kartu Total Rows).
- Temuan untuk QA:
  - TC-GS-IMPORT-533 tidak menyebut isi payload permintaan Confirm Mapping langsung (pengenal berkas sementara dan mapping) selain berkas `brand-10.csv`; payload disediakan klien HTTP tim FE.
  - Post Condition TC-GS-IMPORT-533 "-" dan tidak ada keadaan yang perlu dipulihkan selain yang dikerjakan hook `after`.
