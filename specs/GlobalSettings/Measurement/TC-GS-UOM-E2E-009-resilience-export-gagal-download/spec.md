---
id: TC-GS-UOM-E2E-009-resilience-export-gagal-download
title: "Resilience Export: Kegagalan Download Tabel, Changelog, dan Item Types"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-169
  - TC-GS-UOM-189
  - TC-GS-UOM-196
coverage:
  web: automated
---

# Resilience Export: Kegagalan Download Tabel, Changelog, dan Item Types

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan penyuntikan kegagalan pembuatan file di browser).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data (hanya dibaca, spec tidak membuat atau mengubah data backend): Pre-setup Client A. Population D-01 di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md` dan dipakai sebagai precondition TC, tidak diasersi. Unit Pieces (dengan accordion Item Type List) dipakai untuk TC-GS-UOM-196 dan dicari lewat Search karena berada di halaman 2.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script dari kontrak modul:
  - Respons export daftar Measurement (`Download CSV`): jawab 500 (TC-GS-UOM-169).
  - Respons export Changelog Measurement (`Download CSV`): jawab 500 (TC-GS-UOM-189).
- Kemampuan teknis yang diminta ke tim FE: menyuntikkan kegagalan pembuatan file di sisi browser (mis. membuat penulis CSV/Blob/`URL.createObjectURL` melempar error pada `Download CSV` di accordion Item Type List) untuk TC-GS-UOM-196. TC-GS-UOM-196 tidak menyebut cara memaksa kegagalan ("Paksa kegagalan pembuatan file"); kebutuhan ini dicatat di sini sebagai sumber resmi.
- Guided Tooltip: flag halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite.
- Pemulihan di hook `after`: semua intercept dan penyuntikan kegagalan pembuatan file dilepas walau spec gagal di tengah. Spec tidak mengubah data backend.

## Test Steps

### TC-GS-UOM-169: Download gagal menampilkan toast error

1. Pasang intercept pada respons export daftar Measurement: jawab 500
2. Klik icon Download
3. Pilih Download CSV
4. Verifikasi toast error: `Error, failed to download Measurement.`
5. Tutup toast error
6. Lepas intercept respons export daftar Measurement

### TC-GS-UOM-189: Download Changelog gagal

7. Klik icon Changelog untuk membuka Modal Changelog
8. Pasang intercept pada respons export Changelog Measurement: jawab 500
9. Klik icon Download pada Modal Changelog
10. Pilih Download CSV pada Modal Changelog
11. Verifikasi toast error: `Error, failed to download Changelog-Measurement.`
12. Tutup toast error
13. Lepas intercept respons export Changelog Measurement
14. Tutup Modal Changelog lewat `✕` di header

### TC-GS-UOM-196: Download Item Type List gagal

15. Ketik Search `Pieces`, tekan Enter
16. Klik `⋯` baris Pieces > Detail
17. Aktifkan penyuntikan kegagalan pembuatan file di browser
18. Klik icon Download pada accordion Item Type List
19. Pilih Download CSV pada accordion Item Type List
20. Verifikasi toast error: `Error, failed to download Item Types - Pieces.` dengan `[Unit Name]` = `Pieces`
21. Matikan penyuntikan kegagalan pembuatan file
22. Tutup Modal Unit Detail lewat `[✕]`
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (intercept parsial dan penyuntikan kegagalan di browser; kelas harness fault injection, bagian 3 prinsip 13b). Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-UOM-169 dan TC-GS-UOM-189 sama-sama kegagalan respons export (500) yang bisa dipicu lewat intercept HTTP; TC-GS-UOM-196 kegagalan pembuatan file di sisi klien sehingga butuh penyuntikan di browser (bukan intercept respons).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 5 dan 12 (menutup toast error sebelum toast berikutnya diasersi, S-09), 6 dan 13 dan 21 (melepas intercept atau mematikan penyuntikan), 7 dan 14 (membuka dan menutup Modal Changelog sebagai konteks Download CSV TC-GS-UOM-189), 15 dan 23 (Search `Pieces` untuk menemukan baris di halaman 2 dan mengosongkannya), 16 dan 22 (membuka dan menutup Modal Unit Detail Pieces), serta 9 dan 18 (klik icon Download pada Modal Changelog dan pada accordion Item Type List untuk membuka menu Download).
- TC-GS-UOM-196 pada TC sumber menyebut "Download CSV" setelah membuka Detail Pieces tanpa menyebut accordion; judul TC dan toast (`Item Types - Pieces`) menunjukkan Download pada toolbar accordion Item Type List (PRD: toolbar Item Type List memiliki Download; accordion Device Name List tidak), sehingga langkah 19 memakai accordion itu. Accordion Item Type List terbuka secara default (Expanded) sehingga tidak ada langkah expand.
- Spec ini tidak mengasersi "tidak ada file terunduh" karena Expected TC hanya menyebut toast.
- Spec ini berdiri terpisah dari `TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again` karena gabungan keduanya 64 langkah (41 + 23), jauh melewati batas 35 langkah; spec ini memakai intercept respons export dan penyuntikan kegagalan pembuatan file di browser (kemampuan teknis yang tidak dibutuhkan 008), sedangkan 008 hanya memakai intercept respons baca. Tiap spec membuka layar dan modalnya sendiri, sehingga kegagalan satu spec tidak membuat spec lain kehilangan makna.
- Temuan untuk QA: TC-GS-UOM-196 bertanda Automatable dengan precondition "paksa kegagalan pembuatan file" tanpa menyebut mekanismenya; spec menulisnya sebagai kemampuan teknis yang disediakan tim FE (Prerequisites).
