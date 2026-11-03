---
id: TC-FA-FAAM-E2E-201-total-assets-penanda-masa-garansi-batas-hari
title: "Tab Total Assets: Penanda Warranty Expiry (Lewat, Hari Ini, Hari ke-30, Hari ke-31)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-816
  - TC-FA-FAAM-817
  - TC-FA-FAAM-818
  - TC-FA-FAAM-819
coverage:
  web: automated
---

# Tab Total Assets: Penanda Warranty Expiry (Lewat, Hari Ini, Hari ke-30, Hari ke-31)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Warranty Date Item` (Total Asset 6; Pre-setup #36), tanggal disemai relatif terhadap tanggal hari berjalan menurut Time Zone General Settings client utama: `AST-3001` hari ini minus 1 hari (`Head Office`), `AST-3002` hari ini, `AST-3003` hari ini plus 30 hari, `AST-3004` hari ini plus 31 hari (semua `Head Office`), `AST-3005` tanpa tanggal garansi, `AST-3006` hari ini minus 5 hari (`Warehouse`). Seeding tanggal relatif dilakukan oleh tim BE/FE sebelum spec dijalankan; Time Zone General Settings tidak diubah.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-816: Warranty Expiry tanggal lewat tampil dengan penanda danger dan tooltip Warranty expired

1. Klik nama `Warranty Date Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry, klik `[Save]`
3. Amati sel Warranty Expiry baris `AST-3001` dan `AST-3006`
4. Verifikasi kedua sel menampilkan tanggal penuh dengan penanda kelas danger
5. Hover sel Warranty Expiry baris `AST-3001`
6. Verifikasi tooltip `Warranty expired`
7. Hover sel Warranty Expiry baris `AST-3006`
8. Verifikasi tooltip `Warranty expired`

### TC-FA-FAAM-817: Warranty Expiry hari ini masih berlaku dan tampil dengan penanda warning

9. Amati sel Warranty Expiry baris `AST-3002`
10. Verifikasi sel menampilkan tanggal penuh dengan penanda kelas warning
11. Verifikasi sel tidak menampilkan penanda kelas danger karena pada tanggal habis itu sendiri garansi masih berlaku
12. Hover sel Warranty Expiry baris `AST-3002`
13. Verifikasi tooltip `Warranty expires soon`

### TC-FA-FAAM-818: Warranty Expiry hari ke-30 ke depan masih tampil dengan penanda warning (batas inklusif)

14. Amati sel Warranty Expiry baris `AST-3003`
15. Verifikasi sel menampilkan tanggal penuh dengan penanda kelas warning
16. Hover sel Warranty Expiry baris `AST-3003`
17. Verifikasi tooltip `Warranty expires soon`

### TC-FA-FAAM-819: Warranty Expiry hari ke-31 ke depan tampil normal tanpa penanda

18. Amati sel Warranty Expiry baris `AST-3004`
19. Verifikasi sel menampilkan tanggal penuh tanpa penanda danger maupun warning (kelas normal)
20. Hover sel Warranty Expiry baris `AST-3004`
21. Verifikasi hover tidak menampilkan tooltip `Warranty expired`
22. Verifikasi hover tidak menampilkan tooltip `Warranty expires soon`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah amati sel (tanpa `Verifikasi`) sebelum asersi; Warranty Expiry dicentang sekali pada blok TC-FA-FAAM-816 dan tetap tampil pada blok berikutnya.
- Asersi absence tooltip (TC-FA-FAAM-819) didahului anchor positif: sel menampilkan tanggal penuh pada baris yang sama.
- Hover diasersi segera sesudah pemicu hover (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-FA-FAAM-816 menyebut tanggal "hari ini minus 1 hari" menurut Time Zone client; tanggal seed relatif harus dibuat tepat sebelum run agar tidak bergeser melewati tengah malam.
  - TC-FA-FAAM-817 butir a menyatakan "bukan danger"; spec mengasersinya sebagai `Verifikasi` terpisah.
