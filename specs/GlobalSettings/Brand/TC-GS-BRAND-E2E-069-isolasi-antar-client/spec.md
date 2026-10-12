---
id: TC-GS-BRAND-E2E-069-isolasi-antar-client
title: "Isolasi Data Brand antar Client dan Nama Sama di Client Berbeda"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-228
  - TC-GS-BRAND-229
coverage:
  web: automated
---

# Isolasi Data Brand antar Client dan Nama Sama di Client Berbeda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client B, Lina Kusuma, `totalControl_automated_qaTeam2@qwertysystem.net` (Tabel Data Uji Pre-setup baris 9). Login di hook `before` spec ini; kredensial `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_CLIENTB_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya sebagai pembanding, tidak diakses langsung, tanpa suffix `{runId}`): brand `Vertex Labs`, `Acme Corp`, `Duo Brand`, `Kestrel`, `Northwind Co`, `Zenith Corp` yang memiliki item (Used By (Items) minimal 1).
- Prasyarat Client B: tidak memiliki brand bernama `Acme Corp` sebelum spec berjalan; hook `before` menghapus `Acme Corp` milik Client B sisa run lain lewat API bila ada.
- Data dinamis: brand `Acme Corp` di Client B dibuat spec lewat UI pada TC-GS-BRAND-229. Nama sengaja dipakai literal tanpa suffix `{runId}`, karena yang diuji adalah nama yang sama persis dengan brand Client A.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API `Acme Corp` milik Client B.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-228: login sebagai Total Control Client B. TC-GS-BRAND-229: login sebagai Total Control Client B dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-228: Isolasi data antar client

1. Buka Tab Brand
2. Search `Vertex`
3. Verifikasi brand Client A tidak tampil
4. Kosongkan Search
5. Klik Filter, isi Used By (Items) Min `1`, klik [Apply]
6. Verifikasi brand Client A yang punya item (Acme Corp, Duo Brand, Kestrel, Northwind Co, Vertex Labs, Zenith Corp) tidak tampil
7. Hapus filter Used By (Items) sehingga tabel kembali tanpa filter

### TC-GS-BRAND-229: Nama sama boleh dipakai di client berbeda

8. Klik [+ Brand], isi Brand Name `Acme Corp`, klik [Submit]
9. Verifikasi toast sukses: "Success, brand has been created."

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber: 228 (tanpa aksi) lebih dulu, lalu 229 yang membuat data (prinsip 2 dan 3 konvensi).
- Langkah penghubung: langkah 7 (menghapus filter Used By (Items) sebelum TC berikutnya) tidak tertulis di Langkah Uji TC sumber.
- Nama brand Client A dibaca dari Pre-setup untuk asersi absence; spec tidak menyentuh data Client A, sehingga tidak ada risiko cleanup lintas client.
