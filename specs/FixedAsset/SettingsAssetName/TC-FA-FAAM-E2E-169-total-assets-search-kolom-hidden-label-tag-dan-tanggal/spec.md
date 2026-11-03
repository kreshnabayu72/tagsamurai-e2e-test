---
id: TC-FA-FAAM-E2E-169-total-assets-search-kolom-hidden-label-tag-dan-tanggal
title: "Tab Total Assets Search: Kolom Hidden, Label, Tanggal Last Scanned-Warranty, dan Kelas Category"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-541
  - TC-FA-FAAM-711
  - TC-FA-FAAM-761
  - TC-FA-FAAM-754
coverage:
  web: automated
---

# Tab Total Assets Search: Kolom Hidden, Label, Tanggal Last Scanned-Warranty, dan Kelas Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`.
- Data: `Dell Latitude` (Total Asset 42, Pre-setup #26; setiap aset berlabel `Finance` dan `High Priority`, aset `Dell Latitude - 42` berlabel tambahan `Fragile`, Group `Head Office`, `Finance`, `Warehouse`) dan `Column Matrix Item` (Total Asset 6, `AST-2001` sampai `AST-2006`, Category `Laptop` anak `Electronics`, Pre-setup #33, #33b; nilai Last Scanned `AST-2001` 10 Oct 2026 09:00 dan Warranty Expiry `AST-2001` 31 Mar 2027, Pre-setup #33b); aktor kedua Pre-setup #32e.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-541: Search tidak mencari kolom yang di-hide

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Verifikasi sedikitnya satu baris aset tampil
3. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Group, klik `[Save]`
4. Ketik Search `Head Office`, tekan Enter
5. Verifikasi tidak ada kecocokan dari Group (tidak ada baris yang tampil)
6. Klik `(←)` pada kotak Search
7. Klik header Actions (⋯), pilih `Setup Column...`, centang Group, klik `[Save]`
8. Ketik Search `Head Office`, tekan Enter
9. Verifikasi baris yang cocok dengan Group `Head Office` tampil

### TC-FA-FAAM-711: Search kelas Label (termasuk label di balik +N more)

10. Klik `(←)` pada kotak Search
11. Klik header Actions (⋯), pilih `Setup Column...`, centang Label, klik `[Save]` (precondition TC; dipakai sebagai precondition, tidak diasersi)
12. Ketik Search `fragile`, tekan Enter
13. Verifikasi keyword `fragile` menampilkan 1 aset (`Dell Latitude - 42`)
14. Ganti isi kotak search dengan `high pri`, tekan Enter
15. Verifikasi keyword `high pri` menampilkan seluruh 42 aset (jumlah total pada footer pagination)
16. Telusuri halaman hasil (pagination) sampai baris `Dell Latitude - 42` ditemukan
17. Verifikasi `Dell Latitude - 42` termasuk hasil dengan label `High Priority` tersembunyi di balik `+1 more`

### TC-FA-FAAM-761: Search kelas Category

18. Klik `(←)` pada kotak Search, tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
19. Klik header Actions (⋯), pilih `Setup Column...`, centang Category, klik `[Save]`
20. Ketik Search `laptop`, tekan Enter
21. Verifikasi keyword `laptop` menampilkan keenam baris (tanpa membedakan huruf besar-kecil)
22. Ganti isi kotak search dengan `phone`, tekan Enter
23. Verifikasi Title `No results found`
24. Verifikasi Description `Try adjusting your search or filter.`

### TC-FA-FAAM-754: Search tidak mencari kolom Last Scanned dan Warranty Expiry

25. Klik `(←)` pada kotak Search, tutup popup Detail, klik tombol akun, pilih Logout
26. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`)
27. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
28. Klik header Actions (⋯), pilih `Setup Column...`, centang `Last Scanned` dan `Warranty Expiry`, klik `[Save]`
29. Verifikasi keenam baris aset tampil
30. Ketik Search teks tanggal Last Scanned `AST-2001` sebagaimana tampil di sel, tekan Enter
31. Verifikasi Title `No results found`
32. Verifikasi Description `Try adjusting your search or filter.`
33. Ganti isi kotak search dengan teks tanggal Warranty Expiry `AST-2001` sebagaimana tampil di sel, tekan Enter
34. Verifikasi Title `No results found`
35. Verifikasi Description `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 541, 711 (Dell Latitude, akun Total Control), 761 (Column Matrix Item), lalu ganti akun ke Full Value Access untuk 754 (S-07: ganti akun punya langkah eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal).
- Langkah penghubung: menelusuri halaman hasil sampai baris `Dell Latitude - 42` ditemukan (langkah 16, S-03; TC-FA-FAAM-711 Langkah 5), `(←)` pada Search, mengubah konfigurasi kolom (hide dan centang kolom) sebagai precondition, menutup popup lalu membuka fixture lain, dan Logout sebelum ganti akun.
- Temuan untuk QA:
  - TC-FA-FAAM-711 memerlukan kolom Label tampil (precondition) tetapi LK tidak menyebut langkahnya; spec menambah langkah centang Label.
  - TC-FA-FAAM-541 Expected a ("tidak ada kecocokan dari Group") tidak menyebut copy empty state; spec mengasersi tidak ada baris.
  - TC-FA-FAAM-754: format tanggal sel Last Scanned dan Warranty Expiry mengikuti General Settings; TC tidak menyebut tampilannya sehingga teks dibaca dari sel.
