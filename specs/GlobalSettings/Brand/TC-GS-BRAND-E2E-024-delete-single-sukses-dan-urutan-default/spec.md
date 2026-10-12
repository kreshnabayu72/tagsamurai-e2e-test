---
id: TC-GS-BRAND-E2E-024-delete-single-sukses-dan-urutan-default
title: "Delete Brand Tunggal Berhasil dan Urutan Default Tabel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-7
  - TC-GS-BRAND-95
  - TC-GS-BRAND-106
coverage:
  web: automated
---

# Delete Brand Tunggal Berhasil dan Urutan Default Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data pre-setup (data environment tetap): 12 brand Client A (Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp). Fixture belum ada; tim FE menyiapkan `fixtures/brand.json` dengan kunci `preSetupClientA` (12 nama) dan `populationD01` (12 nama Population D-01 pada butir Data dinamis).
- Data dinamis (seeding lewat API di hook `before`; tidak menumpang spec lain):
  - Population D-01 (setara TC-GS-BRAND-1; nama literal tanpa suffix karena urutan A-Z diasersi; pengecualian S-12), 12 brand: `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics`.
  - Seeding Population D-01 idempotent: tiap nama D-01 yang sudah ada di Client A dilewati (tidak di-seed ulang), dan hanya nama yang benar-benar dibuat oleh hook `before` spec ini yang dicatat sebagai milik spec ini. Suite berjalan serial pada Client A, sehingga tidak ada spec lain yang mengubah Population D-01 selama spec ini berjalan.
  - `axiom labs {runId}-024` (D-02, huruf kecil di awal), `Xenon Bebas {runId}-024` (D-17), dan `Hazel Co {runId}-024` (D-20), semuanya bebas relasi.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga brand dinamis di atas bila masih ada, lalu hanya brand Population D-01 yang dibuat oleh hook `before` spec ini (D-01 yang sudah ada sebelum spec berjalan tidak dihapus). Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > Master Reference > Brand.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-BRAND-7: Urutan default tabel Brand adalah Brand Name A-Z tanpa membedakan huruf besar kecil

1. Buka Global Settings > Master Reference > Brand
2. Perhatikan urutan halaman 1 dan indikator sort tanpa mengklik apa pun
3. Verifikasi halaman 1 berurutan: `Acme Corp`, `Apex Tools`, `axiom labs {runId}-024`, `Bolt Systems`, `Brightway`, `Cedar Supply`, `Delta Instruments`, `Duo Brand`, `Echo Devices`, `Falcon Gear`
4. Verifikasi tidak ada kolom yang menampilkan panah sort aktif
5. Verifikasi tidak ada filter aktif
6. Klik `⋯` baris `axiom labs {runId}-024` > Delete
7. Klik [Delete]
8. Verifikasi `axiom labs {runId}-024` hilang dari tabel

### TC-GS-BRAND-95: Delete Brand bebas relasi berhasil

9. Cari baris `Xenon Bebas {runId}-024` (lewat pagination atau Search), lalu klik `⋯` > Delete
10. Klik [Delete]
11. Verifikasi toast sukses: "Success, brand has been deleted."
12. Verifikasi `Xenon Bebas {runId}-024` hilang dari tabel

### TC-GS-BRAND-106: Klik ganda Delete hanya memproses satu request

13. Cari baris `Hazel Co {runId}-024` (lewat pagination atau Search), lalu klik `⋯` > Delete
14. Klik [Delete] dua kali cepat
15. Verifikasi tepat satu toast sukses: "Success, brand has been deleted."
16. Verifikasi `Hazel Co {runId}-024` hilang dari tabel
17. Buka Changelog Brand
18. Verifikasi Changelog mencatat tepat satu entri Delete untuk `Hazel Co {runId}-024`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- TC-7 diletakkan pertama karena memuat screening (langkah 2 sampai 5) yang harus mendahului aksi hapus; penghapusan `axiom labs` (langkah 6 sampai 8) ikut di blok TC yang sama karena bagian dari Langkah Uji TC-7. Semua aksi sesudahnya juga penghapusan brand yang saling independen.
- Dependensi TC-7 (TC-GS-BRAND-1: Population D-01) disiapkan spec ini sendiri lewat API di hook `before`.
- Total brand pada Precondition TC-7 (24 brand, 25 dengan `axiom labs`) tidak diasersi, karena `Xenon Bebas` dan `Hazel Co` juga di-seed; keduanya terurut sesudah `Falcon Gear` (X dan H sesudah F), sehingga halaman 1 yang diasersi tidak terpengaruh.
- Suffix `{runId}-024` pada `axiom labs` tetap menjaga urutan A-Z (setelah `Apex Tools`, sebelum `Bolt Systems`).
- Asersi "Changelog mencatat satu entri" pada TC-106 adalah hitungan tepat satu entri (presence), bukan asersi absence.
