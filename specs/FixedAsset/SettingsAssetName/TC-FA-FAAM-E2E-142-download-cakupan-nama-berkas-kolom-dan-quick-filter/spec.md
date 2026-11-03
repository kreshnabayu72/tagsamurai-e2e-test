---
id: TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter
title: "Download List: Cakupan Search-Filter, Kolom Hidden, Nama Berkas, Nol Baris, dan Quick Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-455
  - TC-FA-FAAM-456
  - TC-FA-FAAM-457
  - TC-FA-FAAM-459
  - TC-FA-FAAM-701
coverage:
  web: automated
---

# Download List: Cakupan Search-Filter, Kolom Hidden, Nama Berkas, Nol Baris, dan Quick Filter

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Total baris katalog (36) dan 30 baris `Seed Item` diturunkan dari seeding.
- Client `AutoLocked` (Pre-setup #12c) untuk TC-FA-FAAM-701: 30 `Seed Item`, 3 Asset Name Category Locked `Lock Alpha`, `Lock Beta`, `Lock Gamma` (tidak diubah spec ini); akun Total Control client ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), password `Spectra.env.FA_TC_LOCKED_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Kemampuan teknis: mengunduh berkas dari browser dan membaca isi berkas XLSX atau CSV (sel, encoding, nama sheet) lewat pembaca berkas; disediakan tim FE/BE.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-455: Cakupan baris export mengikuti Search dan Filter aktif seluruh halaman
1. Klik icon Download lalu `Download as CSV`
2. Verifikasi berkas pertama memuat seluruh baris katalog, bukan hanya satu halaman
3. Ketik Search `Seed`, tekan Enter
4. Klik icon Download lalu `Download as CSV`
5. Verifikasi berkas kedua hanya memuat baris yang cocok `Seed` (30 baris `Seed Item`)
6. Klik `(←)` pada kotak Search
### TC-FA-FAAM-457: Nama berkas dan extension mengikuti pilihan format
7. Klik icon Download lalu `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Asset-Names.csv` terunduh
10. Klik icon Download lalu `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Asset-Names.xlsx` terunduh
### TC-FA-FAAM-459: Download dengan nol baris menghasilkan berkas hanya header
13. Ketik Search `zzzz-none`, tekan Enter
14. Verifikasi tombol Download aktif
15. Klik icon Download lalu `Download as CSV`
16. Verifikasi tidak ada toast
17. Verifikasi berkas hanya berisi baris header kolom visible
18. Klik `(←)` pada kotak Search
### TC-FA-FAAM-456: Kolom di-hide tidak ikut export dan ikut kembali saat di-unhide
19. Klik header kolom Actions (⋯), lalu uncheck kolom `Code`
20. Tutup Column Visibility
21. Klik icon Download lalu `Download as CSV`
22. Verifikasi tidak ada toast peringatan
23. Verifikasi berkas pertama tanpa kolom `Code`
24. Klik header kolom Actions (⋯), lalu check kolom `Code`
25. Tutup Column Visibility
26. Klik icon Download lalu `Download as CSV`
27. Verifikasi berkas kedua memuat kolom `Code`
28. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### Ganti akun: client AutoLocked
29. Logout, lalu login sebagai Total Control client `AutoLocked` (Pre-setup #12c) dengan `Spectra.env.FA_TC_LOCKED_PASSWORD`
### TC-FA-FAAM-701: Download dengan quick filter aktif memuat hanya hasil quick filter
30. Klik `Show only these`
31. Klik icon Download lalu `Download as CSV`
32. Verifikasi tidak ada toast sukses
33. Verifikasi berkas `Asset-Names.csv` terunduh
34. Verifikasi berkas memuat tepat tiga baris data: `Lock Alpha`, `Lock Beta`, `Lock Gamma`
35. Klik `Clear filter`

## Notes

- Urutan di spec: TC-FA-FAAM-455, 457, 459 lebih dulu, TC-FA-FAAM-456 (mengubah konfigurasi kolom) kemudian, dan TC-FA-FAAM-701 terakhir karena memakai client lain (S-10). Hook `after` mengembalikan sesi ke akun default suite dan menghapus preferensi kolom di browser.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik `(←)` pada Search, membuka dan menutup Column Visibility, pemulihan konfigurasi kolom, dan `Clear filter`.
- Format unduhan CSV dipilih spec pada TC-FA-FAAM-455 karena TC hanya menyebut "Klik Download"; asersi absence toast pada TC-FA-FAAM-456, 457, 459, dan 701 diletakkan segera sesudah pemicu unduh dan sebelum asersi berkas (bagian 8b butir 11).
- Spec ini mengasersi nama berkas, kolom, dan jumlah baris (fungsional); isi sel berkas ada di spec 140 dan 141.
- Temuan untuk QA: TC-FA-FAAM-701 memakai Pre-setup #12c (client tanpa baris akun Total Control, email tidak tertulis); TC-FA-FAAM-456 menyebut dua kali Download CSV tanpa menyebut nama berkas yang dibandingkan.
