---
id: TC-GS-IMPORT-E2E-046-defense-in-depth-client-c-create-missing-divisions-positions-ditolak
title: "Defense-in-depth Client C: Create Missing Divisions/Positions Ditolak 403, Confirm Mapping Ulang 409, dan Pemetaan Satu Kolom ke Dua Atribut 422"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-41
  - TC-GS-IMPORT-83
  - TC-GS-IMPORT-84
  - TC-GS-IMPORT-605
coverage:
  web: automated
---

# Defense-in-depth Client C: Create Missing Divisions/Positions Ditolak 403, Confirm Mapping Ulang 409, dan Pemetaan Satu Kolom ke Dua Atribut 422

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Klien HTTP: spec mengirim permintaan langsung ke server dengan token sesi akun yang diuji. Token diperoleh lewat login API yang disediakan tim FE/BE (mekanisme tidak tertulis di TC, PRD, atau LLD).
- Kemampuan membaca pengenal berkas sementara dari permintaan upload dan Confirm Mapping (pengamatan jaringan tanpa mock, disediakan tim FE/BE) untuk TC-GS-IMPORT-83 dan 84.
- Akun (Client C), password lewat env:
  - Import data (Read Only) Client C (Hari Wibowo) `importRead_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_IMPORTRO_PASSWORD` (TC-GS-IMPORT-41 dan 605; login UI di hook `before`).
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD` (TC-GS-IMPORT-83 dan 84; login UI lewat langkah ganti akun). Hook `after` mengembalikan sesi ke akun default suite.
  - Password tidak ditulis di spec atau fixture.
- Data Dinamis:
  - D-14 (Client C): draft User Login 4 baris dari `user-login-cm.csv` (Ahmad Fauzi dan Citra Lestari valid, Dedi Prakoso dengan Division `Logistik` tidak ada, Eka Putri dengan Position `Store Supervisor` tidak ada), disiapkan lewat skrip fixture untuk TC-GS-IMPORT-41 dan 605, dibuat ulang bila perlu.
  - `brand-12.csv` (D-01; header `Brand Name`, 12 baris) dan `measurement-6.csv` (D-02, 6 baris) dipakai TC-GS-IMPORT-83 dan 84; Client C tanpa draft Tab Brand dan Tab Measurement sebelum tiap TC (Kontrak Fixture R1).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Langkah "Buka menu Import dari sidebar" mengikuti TC dan memuat ulang halaman.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand 12 baris hasil TC-GS-IMPORT-83 dan draft User Login Client C direset lewat skrip fixture (R1/R2) setelah blok masing-masing.

## Test Steps

### TC-GS-IMPORT-41: Create Missing Divisions lewat permintaan langsung oleh Import data (Read Only)

1. Kirim permintaan Create Missing Divisions untuk nilai `Logistik` langsung ke server dengan token akun Import data (Read Only) Client C
2. Verifikasi server menolak permintaan dengan 403 Forbidden
3. Buka menu Import dari sidebar dengan akun yang sama
4. Klik Sub-Tab User Login
5. Verifikasi baris dengan Division `Logistik` tetap berstatus `error`
6. Verifikasi Staging Metric Cards Errors 2
7. Verifikasi Staging Metric Cards Ready to Import 2

### TC-GS-IMPORT-605: Create Missing Positions lewat permintaan langsung oleh Import data (Read Only)

8. Kirim permintaan Create Missing Positions untuk nilai `Store Supervisor` langsung ke server dengan token akun Import data (Read Only) Client C
9. Verifikasi server menolak permintaan dengan 403 Forbidden
10. Buka menu Import dari sidebar dengan akun yang sama
11. Klik Sub-Tab User Login
12. Verifikasi baris dengan Position `Store Supervisor` tetap berstatus `error`
13. Verifikasi Staging Metric Cards Errors 2
14. Verifikasi Staging Metric Cards Ready to Import 2

### TC-GS-IMPORT-83: Pengulangan Confirm Mapping setelah sukses ditolak 409

15. Ganti akun: login UI sebagai Total Control Client C (Client C tanpa draft Tab Brand)
16. Buka menu Import dari sidebar dan pilih Sub-Tab Brand
17. Klik [Upload File]
18. Pilih berkas `brand-12.csv` di file picker
19. Klik [Confirm Mapping]
20. Tunggu aksi selesai (modal tertutup)
21. Kirim ulang permintaan Confirm Mapping langsung ke server dengan token akun yang sama dan pengenal berkas sementara yang sama (dibaca dari permintaan Confirm Mapping pertama)
22. Verifikasi permintaan kedua ditolak 409
23. Muat ulang halaman Import
24. Verifikasi draft tetap 12 baris tanpa baris ganda (Total Rows 12)
25. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-84: Pemetaan satu kolom berkas ke dua atribut target

26. Klik Sub-Tab Measurement
27. Klik [Upload File]
28. Pilih berkas `measurement-6.csv` di file picker
29. Kirim permintaan Confirm Mapping langsung ke server dengan token akun yang sama, pengenal berkas sementara dibaca dari permintaan upload, dan kolom `Unit Name` dipetakan ke atribut Unit Name dan Symbol
30. Verifikasi server menolak permintaan dengan 422
31. Muat ulang halaman Import
32. Verifikasi halaman menampilkan Dropzone tanpa draft
33. Verifikasi tidak ada baris masuk Staging Table

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a). Status 409 dan 422 diamati sebagai respons API; layar sesudahnya dibaca ulang hanya untuk memeriksa state data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 10 (muat ulang halaman Import); langkah 4 dan 11 (membuka Sub-Tab User Login agar baris draft terbaca); langkah 15 (ganti akun); langkah 16 dan 26 (membuka Sub-Tab yang diuji); langkah 23 dan 31 (muat ulang halaman); langkah 25 (reset Client C); langkah 20 (menunggu Confirm Mapping pertama selesai sebelum permintaan kedua dikirim).
- Langkah 29 mengikuti TC-GS-IMPORT-84 langkah 3-4: Modal Column Mapping dibiarkan terbuka tanpa `Verifikasi` karena TC tidak memuat Expected untuknya.
- Langkah 32 (Dropzone tampil) menjadi anchor positif bagi langkah 33 (tidak ada baris Staging Table).
- Pembagian TC lintas spec: TC-GS-IMPORT-41 dan 605 memakai draft D-14 yang sama dengan spec Create Missing lain pada Client C; draft dibuat ulang sebelum blok.
- Temuan untuk QA:
  - TC-GS-IMPORT-605 tidak menyebut Sub-Tab User Login dibuka, padahal Expected b menyebut "Sub-Tab User Login"; spec menambahkan langkah penghubung 11.
  - Mekanisme token sesi per akun dan pembacaan pengenal berkas sementara tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-41 dan 605 tidak merujuk TC dependensi untuk draft D-14; Precondition TC dipakai sebagai sumber.
