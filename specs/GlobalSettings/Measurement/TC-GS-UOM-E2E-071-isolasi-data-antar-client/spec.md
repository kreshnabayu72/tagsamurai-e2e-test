---
id: TC-GS-UOM-E2E-071-isolasi-data-antar-client
title: "Isolasi Data Measurement antar Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-241
coverage:
  web: automated
---

# Isolasi Data Measurement antar Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client B, Lina Kusuma (`Lina K`), `totalControl_automated_qaTeam2@qwertysystem.net` (Tabel Data Uji Pre-setup), kredensial `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Master Reference > Measurement.
- Pelaku pemicu seeding (hanya lewat sesi API aktor, tanpa login UI; lihat `suite.md`, bagian Hook suite): Admin FAMS Client B, kredensial `Spectra.env.FA_ADMIN_CLIENTB_PASSWORD`. Akun ini tidak ada di Pre-setup TC; nama env var baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` bersama fixture akunnya (S-13).
- Environment variable: `GS_CLIENTB_TC_PASSWORD`, `GS_TC_PASSWORD`, `FA_ADMIN_CLIENTB_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite untuk akun aktor (lihat `suite.md`, bagian Hook suite).
- Data Pre-setup Client A (hanya sebagai pembanding, tidak diakses langsung, tanpa suffix `{runId}`): unit `Kilogram` (Used By (Items) 1, referensi Supply Chemical).
- Prasyarat Client B: tidak memiliki unit bernama `Kilogram` sebelum spec berjalan (environment Client B disiapkan tim FE tanpa unit itu); hook `before` hanya memverifikasi bahwa Client B tidak memiliki `Kilogram` dan menggagalkan prasyarat bila unit itu ada (tidak menghapus data Client B), serta memastikan tabel Client B memuat sedikitnya satu unit (lihat Temuan untuk QA).
- Data dinamis Client B (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before`: unit `Agregat {runId}-071` / `ag` dan Asset Name FAMS Client B `Agregat Item {runId}-071` yang memakai unit itu. Nilai field wajib lain Asset Name FAMS (Category, TAG Type) disediakan tim FE lewat fixture `fixtures/measurement.json` (belum ada): kunci `assetName.category` dan `assetName.tagType`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Agregat Item {runId}-071` lalu unit `Agregat {runId}-071` milik Client B.
- Tidak ada state global yang diubah.
- TC-GS-UOM-241: login sebagai Total Control Client B dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-241: Data Measurement client lain tidak terlihat

1. Buka Tab Measurement Client B
2. Verifikasi tabel Measurement Client B memuat sedikitnya satu baris
3. Ketik Search `Kilogram`, tekan Enter
4. Verifikasi unit `Kilogram` Client A tidak tampil (empty state `No results found`)
5. Klik `(←)` pada kotak Search
6. Ketik Search `Agregat {runId}-071`, tekan Enter
7. Verifikasi Used By (Items) baris `Agregat {runId}-071` bernilai `1`
8. Klik teks `Agregat {runId}-071`
9. Verifikasi Item Type List Detail memuat `Agregat Item {runId}-071`
10. Verifikasi Total Item `1` (agregasi Item Type hanya dari produk Client B)
11. Tutup Unit Detail

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: multi-konteks (dua tenant: Client B membaca, Client A hanya sebagai pembanding data).
- Langkah penghubung: langkah 1 (salinan Langkah Uji TC-GS-UOM-241 "Buka Tab Measurement Client B"; layar awal Client B dinyatakan di Prerequisites), langkah 5 (mengosongkan Search sebelum Search berikutnya), langkah 6 (Search unit milik spec `Agregat {runId}-071`) dan langkah 8 (klik teks unit untuk membuka Unit Detail), keduanya aksi tanpa `Verifikasi` yang bukan Langkah Uji TC-GS-UOM-241, langkah 11 (menutup Unit Detail).
- Langkah 2 menjadi anchor positif bagi absence pada langkah 4; empty state `No results found` juga menjadi anchor yang sah (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-UOM-241 tidak menyatakan isi Measurement Client B; Pre-setup TC hanya memuat data Client A (Client C: "tanpa Measurement"). Asersi "Kilogram Client A tidak tampil" mengandaikan Client B tidak punya unit `Kilogram` sendiri; spec menuliskannya sebagai prasyarat dan hook `before` memverifikasinya tanpa menghapus data Client B.
  - Expected b ("Agregasi Item Type hanya dari produk Client B") tidak menyebut data Client B yang diamati; spec men-seed satu unit dan satu Asset Name FAMS milik Client B untuk mengamati agregasinya. Akun Admin FAMS Client B tidak ada di Pre-setup TC (S-13).
  - TC-GS-UOM-241 tidak punya Post Condition.
