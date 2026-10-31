---
id: TC-GS-UOM-E2E-030-delete-single-sukses-dan-urutan-default
title: "Delete Unit Tunggal Berhasil dan Urutan Default Tabel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-5
  - TC-GS-UOM-96
coverage:
  web: automated
---

# Delete Unit Tunggal Berhasil dan Urutan Default Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca, urutan A-Z diasersi): 8 unit `Box`, `Dozen`, `Gram`, `Kilogram`, `Liter`, `Meter`, `Pack`, `Pieces`. Fixture belum ada; tim FE menyiapkan `fixtures/measurement.json` dengan kunci `preSetupClientA` (8 nama) dan `populationD01` (12 nama).
- Data dinamis (seeding lewat API di hook `before`; tidak menumpang spec lain):
  - Population D-01 (setara TC-GS-UOM-36; nama literal tanpa suffix karena urutan A-Z dan jumlah diasersi; pengecualian S-12), 12 unit: `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Seeding idempotent: tiap nama yang sudah ada di Client A dilewati, dan hanya nama yang dibuat hook `before` spec ini dicatat sebagai milik spec ini. Suite berjalan serial pada Client A.
  - `carat` / `ct` (D-09, huruf kecil di awal nama; nama literal tanpa suffix karena menentukan hasil urutan tanpa membedakan huruf besar kecil; pengecualian S-12 dengan syarat yang sama: seeding idempotent, kode literal dibersihkan di hook `before`, cleanup hanya menghapus yang dibuat spec ini, suite serial), bebas relasi. Total tabel Client A 21 unit (8 Pre-setup + 12 Population + `carat`), N diturunkan dari seeding (butir 10 bagian 8b); hook suite membersihkan sisa unit non-Population hasil run sebelumnya.
  - `Barrel {runId}-030` / `bbl` (D-08, bebas relasi), dibuat lewat API di langkah penghubung sesudah TC-GS-UOM-5 supaya tabel TC-5 tepat 21 unit.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API `carat` dan `Barrel {runId}-030` bila masih ada, lalu hanya unit Population D-01 yang dibuat oleh hook `before` spec ini (D-01 yang sudah ada sebelum spec berjalan tidak dihapus).
- Kemampuan teknis: API seeding Measurement (create dan delete) di hook dan di satu langkah penghubung; pembacaan jumlah halaman pagination.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-UOM-5: Urutan default tabel Measurement adalah Unit Name A-Z tanpa membedakan huruf besar kecil

1. Perhatikan urutan baris halaman 1 dan indikator sort seluruh kolom tanpa mengklik apa pun
2. Verifikasi halaman 1 berurutan: `Box`, `carat`, `Centimeter`, `Dozen`, `Foot`, `Gallon`, `Gram`, `Inch`, `Kilogram`, `Liter`
3. Verifikasi `carat` tidak berada di akhir daftar halaman 1
4. Pindah ke halaman 2
5. Verifikasi halaman 2 berurutan: `Meter`, `Milliliter`, `Millimeter`, `Ounce`, `Pack`, `Pieces`, `Pound`, `Roll`, `Set`, `Sheet`
6. Pindah ke halaman 3
7. Verifikasi halaman 3 berisi `Ton`
8. Verifikasi tidak ada kolom yang menampilkan panah sort aktif, termasuk Unit Name
9. Verifikasi tidak ada filter aktif
10. Pindah ke halaman 1
11. Klik `⋯` baris `carat` > Delete
12. Klik [Delete]
13. Verifikasi jumlah halaman kembali 2
14. Verifikasi `carat` hilang dari tabel

### TC-GS-UOM-96: Delete unit bebas relasi berhasil

15. Buat unit `Barrel {runId}-030` / `bbl` lewat API (langkah penghubung)
16. Ketik Search `Barrel {runId}-030`, tekan Enter
17. Verifikasi baris `Barrel {runId}-030` tampil di tabel
18. Klik `⋯` baris `Barrel {runId}-030` > Delete
19. Klik [Delete]
20. Verifikasi toast `Success, unit has been deleted.`
21. Verifikasi `Barrel {runId}-030` hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 21.
- Aksi menghapus data ada di akhir tiap blok (prinsip 5): `carat` dihapus pada ujung TC-GS-UOM-5 setelah seluruh asersi urutan, lalu `Barrel` pada TC-GS-UOM-96. Dependensi `TC-GS-UOM-36` (Population) dan `TC-GS-UOM-55` (Barrel) dipenuhi oleh seeding spec sendiri (S-04, S-06).
- Langkah penghubung: langkah 4, 6, dan 10 (navigasi halaman untuk membaca urutan, bagian dari langkah 2 TC-5 "perhatikan halaman 1, 2, dan 3"), langkah 15 (seeding `Barrel` lewat API sesudah TC-5; ditunda supaya hitungan 21 unit TC-5 tidak terganggu), dan langkah 16 (Search untuk menemukan baris target; hasil kosong sesudah Delete didahului toast sukses langkah 20 sebagai anchor, butir 2 bagian 8b).
- TC-GS-UOM-5 Expected butir e dipecah menjadi langkah 13 (jumlah halaman kembali 2) dan 14 (`carat` hilang); urutan ini sengaja dibalik dari urutan penulisan di TC supaya jumlah halaman yang berkurang menjadi anchor positif sebelum asersi absence (butir 2 bagian 8b); TC-5 tidak menyebut toast sukses pada penghapusan `carat`, sehingga tidak diasersi di blok itu.
- TC-GS-UOM-96 memakai `Barrel {runId}-030` (D-08 pada TC sumber memakai nama `Barrel`) sebagai nama bersuffix (S-12).
- Temuan untuk QA: TC-GS-UOM-5 mengasumsikan 21 unit tepat pada baseline; jika environment Client A masih memuat sisa unit dari spec lain (mis. `Kilogram Force`, `Hectare`, `Square Meter`), Expected urutan halaman 1 dan 2 gagal. Bergantung pada pembersihan hook suite.
