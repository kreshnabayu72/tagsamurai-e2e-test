---
id: TC-FA-FAAM-E2E-041-create-sukses-dua-brand-dan-model
title: "Create Sukses: Default Label Terisi dan Dua Brand dengan Model Berbeda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-147
  - TC-FA-FAAM-149
coverage:
  web: automated
---

# Create Sukses: Default Label Terisi dan Dua Brand dengan Model Berbeda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): Label #25 `Fragile`, Brand #23 `Dell` dan `Lenovo`.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 147 {runId}-041` dan `Create Min Item 149 {runId}-041`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedua Asset Name milik spec ini bila masih ada.

## Test Steps

### TC-FA-FAAM-147: Create dengan Default Label terisi

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi field wajib: Asset Name `Create Min Item 147 {runId}-041`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Pilih Default Label `Fragile`
4. Klik `[Submit]`

### TC-FA-FAAM-149: Create dengan dua Brand dan model berbeda per Brand

5. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
6. Isi field wajib: Asset Name `Create Min Item 149 {runId}-041`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, UoM `Unit`
7. Pilih Brand `Dell` dan `Lenovo`
8. Tambahkan model `5420` pada Dell dan `X1` pada Lenovo
9. Klik `[Submit]`

### Verifikasi hasil kedua Create

10. Ketik Search `{runId}-041`, tekan Enter
11. Buka Popup Detail `Create Min Item 147 {runId}-041` dari tabel
12. Verifikasi Detail menampilkan Default Label `Fragile` sebagai badge berwarna
13. Tutup Popup Detail
14. Buka Popup Detail `Create Min Item 149 {runId}-041` dari tabel
15. Verifikasi Tab Models per Brand: baris `Dell` menampilkan model `5420`
16. Verifikasi Tab Models per Brand: baris `Lenovo` menampilkan model `X1`
17. Tutup Popup Detail
18. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Langkah penghubung (tanpa `Verifikasi`): Search `{runId}-041` mengumpulkan kedua baris milik spec ini (R-16), penutupan Popup Detail, dan penutupan Search.
- TC-FA-FAAM-149 mengisi Brand `Dell` dan `Lenovo` secara terpisah dari field wajib lain (Brand tidak dimasukkan ke baris "Isi field wajib") karena TC menyebut dua Brand.
