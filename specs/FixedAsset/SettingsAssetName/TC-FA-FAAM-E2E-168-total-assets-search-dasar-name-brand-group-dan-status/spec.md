---
id: TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status
title: "Tab Total Assets Search: Tanpa Hasil, Name, Asset ID, Brand, Model/Type, Group, Status, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-506
  - TC-FA-FAAM-507
  - TC-FA-FAAM-508
  - TC-FA-FAAM-509
  - TC-FA-FAAM-510
coverage:
  web: automated
---

# Tab Total Assets Search: Tanpa Hasil, Name, Asset ID, Brand, Model/Type, Group, Status, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Status beragam termasuk `Missing`, `Permanently Missing`, `Borrowed`, `Active`, Pre-setup #26) dan `Service Vehicle` (Total Asset 8: `AST-1001` sampai `AST-1004` Brand `Isuzu` model `D-Max` Group `Head Office`, `AST-1005` sampai `AST-1008` Brand `Toyota` model `Hilux` Group `Warehouse`, Pre-setup #14, #26c).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-506: Search tanpa hasil di Tab Total Assets

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Verifikasi sedikitnya satu baris aset tampil
3. Ketik Search `zzzz`, tekan Enter
4. Verifikasi Title `No results found`
5. Verifikasi Description `Try adjusting your search or filter.`

### TC-FA-FAAM-507: Search kelas Name dan Asset ID

6. Klik `(←)` pada kotak Search
7. Ketik Search `Latitude - 4`, tekan Enter
8. Verifikasi keyword `Latitude - 4` dicocokkan atas teks lengkap `[Asset Name] - [Increment]` sehingga baris `Dell Latitude - 4`, `Dell Latitude - 40`, `Dell Latitude - 41`, dan `Dell Latitude - 42` tampil
9. Ganti isi kotak search dengan `AST-0042`, tekan Enter
10. Verifikasi keyword `AST-0042` dicocokkan substring sehingga baris `AST-0042` tampil

### TC-FA-FAAM-509: Search kolom Status mencocokkan substring

11. Ganti isi kotak search dengan `missing`, tekan Enter
12. Verifikasi baris berstatus `Missing` tampil
13. Verifikasi baris berstatus `Permanently Missing` tampil

### TC-FA-FAAM-510: Search tidak mencari Last Updated

14. Klik `(←)` pada kotak Search
15. Verifikasi sedikitnya satu baris aset tampil
16. Catat teks tanggal Last Updated sebuah aset sebagaimana tampil di sel
17. Ketik Search teks tanggal Last Updated yang dicatat, tekan Enter
18. Verifikasi tidak ada kecocokan (tidak ada baris yang tampil)

### TC-FA-FAAM-508: Search kelas Brand, Model/Type, Group

19. Klik `(←)` pada kotak Search, tutup popup Detail
20. Ketik Search `Service Vehicle`, tekan Enter
21. Klik nama `Service Vehicle`, klik tab `Total Assets (8)`
22. Ketik Search `isuzu`, tekan Enter
23. Verifikasi keyword `isuzu` menampilkan 4 aset ber-Brand `Isuzu`
24. Ganti isi kotak search dengan `hilux`, tekan Enter
25. Verifikasi keyword `hilux` menampilkan 4 aset ber-model `Hilux` (Brand `Toyota`)
26. Ganti isi kotak search dengan `head office`, tekan Enter
27. Verifikasi keyword `head office` menampilkan 4 aset di Group `Head Office`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 506, 507, 509, 510 pada `Dell Latitude`, lalu 508 pada `Service Vehicle` (berpindah fixture sekali).
- Langkah penghubung: `(←)` pada Search antar blok TC, mencatat teks Last Updated pada blok TC-FA-FAAM-510, dan menutup popup lalu membuka `Service Vehicle` pada blok TC-FA-FAAM-508, dengan Search `Service Vehicle` pada langkah 20 agar baris berada di halaman 1 daftar A-Z yang diawali 30 `Seed Item` (R-16).
- Temuan untuk QA:
  - TC-FA-FAAM-510 Expected hanya "Tidak ada kecocokan" tanpa copy empty state; spec mengasersi tidak ada baris yang tampil tanpa mengutip teks empty state.
  - TC-FA-FAAM-509 menyebut kolom Status mencocokkan substring; hitungan baris `Missing` dan `Permanently Missing` tidak diberikan TC sehingga hanya keberadaannya diasersi.
