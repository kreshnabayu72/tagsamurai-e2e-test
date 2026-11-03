---
id: TC-FA-FAAM-E2E-200-total-assets-asset-value-fiscal-gerbang-dan-sort-filter
title: "Tab Total Assets: Gerbang No access pada Dua Kolom Asset Value serta Sort-Filter-Search Fiscal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-826
  - TC-FA-FAAM-827
coverage:
  web: automated
---

# Tab Total Assets: Gerbang No access pada Dua Kolom Asset Value serta Sort-Filter-Search Fiscal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Asset Value HO (Pre-setup #32) `assetValueHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AVHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`.
- Client `AutoDepreciation` (Pre-setup #37): salinan `Column Matrix Item` dengan `Asset Value (Commercial)` (`AST-2001` 15000000, `AST-2002` 0, `AST-2004` 5000000, `AST-2005` 20000000) dan `Asset Value (Fiscal)` (`AST-2001` 9000000, `AST-2002` 0, `AST-2004` 4000000, `AST-2005` 25000000; `AST-2003` dan `AST-2006` tanpa harga perolehan); `AST-2001`, `AST-2002` Group `Head Office`, `AST-2004`, `AST-2005` Group `Warehouse` (di luar hak Asset Value HO). Akun Asset Value HO dan Full Value Access pada client ini disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Preferensi Setup Column tersimpan per akun (keputusan pemilik 2026-11-02), jadi centang kolom akun sebelumnya tidak terbawa ke akun berikutnya.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-826: Gerbang No access berlaku pada kedua kolom Asset Value

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik `[Save]`
3. Verifikasi `Asset Value (Commercial)`: `AST-2001` 15000000, `AST-2002` currency nol, `AST-2004` dan `AST-2005` `No access`
4. Verifikasi `Asset Value (Fiscal)`: `AST-2001` 9000000, `AST-2002` currency nol, `AST-2004` dan `AST-2005` `No access`
5. Verifikasi harga perolehan `AST-2005` tidak tampil bagi aktor tanpa hak
6. Hover sel `AST-2004` pada kolom `Asset Value (Commercial)`
7. Verifikasi tooltip `Requires View asset value access in this group.`
8. Hover sel `AST-2004` pada kolom `Asset Value (Fiscal)`
9. Verifikasi tooltip `Requires View asset value access in this group.`
10. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-827: Sort, Filter, dan Search bekerja pada kolom Asset Value (Fiscal)

11. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`)
12. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
13. Klik header Actions (⋯), pilih `Setup Column...`, centang kedua kolom Asset Value, klik `[Save]`
14. Klik header `Asset Value (Fiscal)` 1 kali
15. Verifikasi klik 1 (ascending numerik): `AST-2002` (0), `AST-2004`, `AST-2001`, `AST-2005`, lalu baris `—` di akhir
16. Klik header `Asset Value (Fiscal)` 1 kali lagi
17. Verifikasi klik 2 (descending): baris `—` di awal, lalu `AST-2005`, `AST-2001`, `AST-2004`, `AST-2002`
18. Klik header `Asset Value (Fiscal)` 1 kali lagi
19. Verifikasi klik 3: kembali ke default Last Updated Newest First
20. Klik Filter, amati field Asset Value
21. Verifikasi Filter Panel memuat satu field range `Min` dan `Max` untuk `Asset Value (Commercial)` dan satu untuk `Asset Value (Fiscal)`
22. Isi `Asset Value (Fiscal)` Min `5000000`, klik `[Apply]`
23. Verifikasi `Fiscal` Min 5000000: hanya `AST-2001` dan `AST-2005` tampil
24. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
25. Ketik Search teks nilai `Asset Value (Fiscal)` `AST-2001` sebagaimana tampil, tekan Enter
26. Verifikasi Search teks nilai Fiscal `AST-2001` menampilkan `AST-2001`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 826 (Asset Value HO), lalu ganti akun ke Full Value Access untuk 827 (ACC TC-FA-FAAM-827 menyebut Role Full Value Access; S-07).
- Langkah penghubung: `[Clear Field]` dan `[Apply]` untuk menghapus filter; menutup popup Detail dan Logout sebelum ganti akun.
- Temuan untuk QA:
  - Pre-setup #37 tidak memberi email akun Asset Value HO dan Full Value Access pada client `AutoDepreciation`; spec memakai akun yang disediakan tim FE.
  - TC-FA-FAAM-827 memuat Pre-setup #37 pada ACC; hanya Pre-setup #32e yang tertulis sebagai aktor, sedangkan TC-FA-FAAM-826 menyebut Pre-setup #32.
