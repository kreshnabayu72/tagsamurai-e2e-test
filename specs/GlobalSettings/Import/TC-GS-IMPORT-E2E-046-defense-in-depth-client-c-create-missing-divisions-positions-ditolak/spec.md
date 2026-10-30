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
  - D-14 (Client C): draft User Login 4 baris dari `user-login-cm.csv` (Ahmad Fauzi dan Citra Lestari valid, Dedi Prakoso dengan Division `Logistik` tidak ada, Eka Putri dengan Position `Store Supervisor` tidak ada), disiapkan lewat skrip fixture oleh langkah 1 untuk TC-GS-IMPORT-41 dan 605.
  - `brand-12.csv` (D-01; header `Brand Name`, 12 baris) dan `measurement-6.csv` (D-02, 6 baris) dipakai TC-GS-IMPORT-83 dan 84; Client C tanpa draft Tab Brand dan Tab Measurement oleh hook `beforeEach` suite (Kontrak Fixture R1).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Langkah "Buka menu Import dari sidebar" mengikuti TC dan memuat ulang halaman.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand 12 baris hasil TC-GS-IMPORT-83 dan draft User Login Client C direset lewat skrip fixture (R1/R2) setelah blok masing-masing.

## Test Steps

### TC-GS-IMPORT-41: Create Missing Divisions lewat permintaan langsung oleh Import data (Read Only)

1. Siapkan draft User Login D-14 pada Client C (`user-login-cm.csv`, 4 baris) lewat skrip fixture
2. Kirim permintaan Create Missing Divisions untuk nilai `Logistik` langsung ke server dengan token akun Import data (Read Only) Client C
3. Verifikasi server menolak permintaan dengan 403 Forbidden
4. Buka menu Import dari sidebar dengan akun yang sama
5. Klik Sub-Tab User Login
6. Verifikasi baris dengan Division `Logistik` tetap berstatus `error`
7. Verifikasi Staging Metric Cards Errors 2
8. Verifikasi Staging Metric Cards Ready to Import 2

### TC-GS-IMPORT-605: Create Missing Positions lewat permintaan langsung oleh Import data (Read Only)

9. Kirim permintaan Create Missing Positions untuk nilai `Store Supervisor` langsung ke server dengan token akun Import data (Read Only) Client C
10. Verifikasi server menolak permintaan dengan 403 Forbidden
11. Buka menu Import dari sidebar dengan akun yang sama
12. Klik Sub-Tab User Login
13. Verifikasi baris dengan Position `Store Supervisor` tetap berstatus `error`
14. Verifikasi Staging Metric Cards Errors 2
15. Verifikasi Staging Metric Cards Ready to Import 2

### TC-GS-IMPORT-83: Pengulangan Confirm Mapping setelah sukses ditolak 409

16. Ganti akun: login UI sebagai Total Control Client C (Client C tanpa draft Tab Brand)
17. Buka menu Import dari sidebar dan pilih Sub-Tab Brand
18. Klik [Upload File]
19. Pilih berkas `brand-12.csv` di file picker
20. Klik [Confirm Mapping]
21. Tunggu aksi selesai (modal tertutup)
22. Kirim ulang permintaan Confirm Mapping langsung ke server dengan token akun yang sama dan pengenal berkas sementara yang sama (dibaca dari permintaan Confirm Mapping pertama)
23. Verifikasi permintaan kedua ditolak 409
24. Muat ulang halaman Import
25. Verifikasi draft tetap 12 baris tanpa baris ganda (Total Rows 12)
26. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-84: Pemetaan satu kolom berkas ke dua atribut target

27. Klik Sub-Tab Measurement
28. Klik [Upload File]
29. Pilih berkas `measurement-6.csv` di file picker
30. Tunggu aksi selesai (permintaan mendapat respons)
31. Kirim permintaan Confirm Mapping langsung ke server dengan token akun yang sama, pengenal berkas sementara dibaca dari permintaan upload, dan kolom `Unit Name` dipetakan ke atribut Unit Name dan Symbol
32. Verifikasi server menolak permintaan dengan 422
33. Muat ulang halaman Import
34. Verifikasi halaman menampilkan Dropzone tanpa draft
35. Verifikasi tidak ada baris masuk Staging Table

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a). Status 409 dan 422 diamati sebagai respons API; layar sesudahnya dibaca ulang hanya untuk memeriksa state data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (seed draft D-14, K-7); langkah 4, 11 (muat ulang halaman Import); langkah 5 dan 12 (membuka Sub-Tab User Login agar baris draft terbaca); langkah 16 (ganti akun); langkah 17 dan 27 (membuka Sub-Tab yang diuji); langkah 24 dan 33 (muat ulang halaman); langkah 26 (reset Client C); langkah 21 (menunggu Confirm Mapping pertama selesai sebelum permintaan kedua dikirim); langkah 30 (menunggu pilih berkas mendapat respons sebelum permintaan langsung dikirim; penanda tidak ada di TC).
- Langkah 31 mengikuti TC-GS-IMPORT-84 langkah 3-4: Modal Column Mapping dibiarkan terbuka tanpa `Verifikasi` karena TC tidak memuat Expected untuknya.
- Langkah 34 (Dropzone tampil) menjadi anchor positif bagi langkah 35 (tidak ada baris Staging Table).
- Pembagian TC lintas spec: TC-GS-IMPORT-41 dan 605 memakai draft D-14 yang sama dengan spec Create Missing lain pada Client C; draft dibuat ulang sebelum blok.
- Temuan untuk QA:
  - TC-GS-IMPORT-605 tidak menyebut Sub-Tab User Login dibuka, padahal Expected b menyebut "Sub-Tab User Login"; spec menambahkan langkah penghubung 12.
  - Penanda "permintaan mendapat respons" pada langkah 30 tidak ditulis di TC-GS-IMPORT-84; spec menambahkannya supaya unggah berkas selesai sebelum permintaan langsung dikirim.
  - Mekanisme token sesi per akun dan pembacaan pengenal berkas sementara tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-41 dan 605 tidak merujuk TC dependensi untuk draft D-14; Precondition TC dipakai sebagai sumber.
