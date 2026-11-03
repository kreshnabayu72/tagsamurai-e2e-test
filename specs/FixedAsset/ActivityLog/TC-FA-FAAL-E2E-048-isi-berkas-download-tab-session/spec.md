---
id: TC-FA-FAAL-E2E-048-isi-berkas-download-tab-session
title: "Isi Berkas Download Tab Session: Sel Date, User, Teks, Status, dan Device/Browser"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-173
  - TC-FA-FAAL-174
  - TC-FA-FAAL-175
  - TC-FA-FAAL-176
  - TC-FA-FAAL-177
coverage:
  web: automated
---

# Isi Berkas Download Tab Session: Sel Date, User, Teks, Status, dan Device/Browser

## Prerequisites

- Mode: FE+BE (backend nyata; unduhan nyata tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka).
- General Settings staf akun aktor: Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (nilai default Pre-setup #1; TC-FA-FAAL-173 butir d).
- Data Pre-setup: Data Log Tab Session SS-01 sampai SS-11 (#11), disediakan lewat seed suite. Nilai sel yang diasersi (Date, User, Employee ID, Position, Division, Activity, Note, Status, IP Address, Device/Browser) berasal dari tabel Pre-setup #11 TC sumber. Baris dikenali di berkas lewat kombinasi nilai kolom Date dan User seed. Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE). Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE): penangkap unduhan browser dan parser CSV yang membaca nilai sel per baris dan kolom.
- Spec ini tidak mengubah state global dan tidak menyimpan konfigurasi kolom.
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### Satu unduhan CSV Tab Session dibaca untuk TC-FA-FAAL-173 sampai 177

1. Klik icon Download di Tab Session, pilih `Download as CSV`, lalu buka berkas dengan parser CSV

### TC-FA-FAAL-173: Sel Date

2. Verifikasi sel Date baris SS-01 bernilai `14/07/26, 08:05`
3. Verifikasi sel Date baris SS-11 bernilai `16/07/26, 09:00`

### TC-FA-FAAL-174: Sel User

4. Verifikasi sel User baris SS-03 bernilai `Siti Nurbaya` (bukan `Siti N`)
5. Verifikasi sel User baris SS-06 bernilai `Budi Santoso` (bukan `Budi S`)

### TC-FA-FAAL-175: Sel teks dengan nilai kosong

6. Verifikasi baris SS-05: Employee ID `-`, Position `-`, IP Address `-`
7. Verifikasi baris SS-05: Division `Finance`
8. Verifikasi baris SS-05: Activity `Session`
9. Verifikasi baris SS-01: Activity `Session`
10. Verifikasi baris SS-01: Note `Session started`

### TC-FA-FAAL-176: Sel Status

11. Verifikasi sel Status baris SS-01 sampai SS-04 semuanya bernilai `-` (bukan Success maupun Failed)

### TC-FA-FAAL-177: Sel Device/Browser

12. Verifikasi sel Device/Browser baris SS-01 bernilai `Chrome on Windows`
13. Verifikasi sel Device/Browser baris SS-05 bernilai `TAG Samurai App on Android`
14. Verifikasi sel Device/Browser baris SS-06 dan SS-07 bernilai `-`

## Notes

- Mode: FE+BE, kelas f (binary buffer): spec ini khusus isi sel berkas; nama berkas, header, dan jumlah baris ada di spec 046 dan 047.
- Satu unduhan CSV (langkah 1) dipakai bersama untuk TC-FA-FAAL-173 sampai 177 karena data (#11), format (CSV), dan General Settings staf identik pada kelima TC; tiap TC punya `Verifikasi` sendiri atas berkas yang sama.
- Pengelompokan `Verifikasi` (S-01): kolom yang bernilai sama pada satu baris (Employee ID, Position, IP Address bernilai `-`) ditulis satu `Verifikasi` (langkah 6); selebihnya satu `Verifikasi` per klausa Expected dan per baris (langkah 2 dan 3, 4 dan 5, 12 dan 13).
- Temuan untuk QA:
  - TC-FA-FAAL-173 sampai 177 tidak menyebut cara mengenali baris SS-xx di berkas; spec mengenalinya dari nilai Date dan User seed.
  - TC-FA-FAAL-174 menulis pembanding negatif "(bukan `Siti N` dan `Budi S`)" dalam Expected; spec mengasersi nilai nama lengkap, dan pembanding negatif dicantumkan sebagai keterangan pada nilai yang sama.
