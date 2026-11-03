---
id: TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif
title: "Download Labels List: CSV dan XLSX, Nama Berkas, Kolom, dan Filter Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-266
  - TC-FA-LBL-267
  - TC-FA-LBL-268
  - TC-FA-LBL-269
  - TC-FA-LBL-271
  - TC-FA-LBL-272
coverage:
  web: automated
---

# Download Labels List: CSV dan XLSX, Nama Berkas, Kolom, dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Total Asset | Modified By |
  |---|---|---|
  | `High Priority` | 3 | `Sarah J` |
  | `Finance Department` | 5 | `David K` |
  | `Audit Ready` | 2 | `Sarah J` |
  | `Executive Asset` | 1 | `Michael W` |
  | `Maintenance Due` | 4 | `David K` |
  | `Seasonal Event` | 0 | `Michael W` |
  | `Night Shift` | 0 | `Sarah J` |
  | `Warehouse Priority` | 0 | `Sarah J` |
  | `Field Kit` | 2 | `David K` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Labels List (diubah dan dipulihkan oleh langkah spec); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).
- Kemampuan teknis (disediakan tim FE): direktori unduhan uji untuk menangkap berkas, pembaca CSV dan XLSX (nama berkas, nama sheet, header, dan baris).

## Test Steps

### TC-FA-LBL-266 dan TC-FA-LBL-272: Download dengan Search dan Filter aktif; nama berkas dan sheet XLSX

1. Ketik Search `Sarah`, tekan Enter
2. Klik icon Filter di Table Tools
3. Isi `Total Asset` Min dengan 2
4. Klik `[Apply]`
5. Klik icon Download
6. Klik `Download as XLSX`
7. Verifikasi berkas terunduh bernama `Labels.xlsx`
8. Verifikasi berkas memuat satu sheet bernama `Sheet1`
9. Verifikasi berkas memuat dua baris `Audit Ready` dan `High Priority`
10. Pulihkan: klik `(←)` pada kotak Search, klik icon Filter, klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel

### TC-FA-LBL-269 dan TC-FA-LBL-271: Download berhasil tanpa toast; nama berkas CSV

11. Klik icon Download
12. Klik `Download as CSV`
13. Verifikasi tidak ada toast sukses
14. Verifikasi berkas terunduh
15. Verifikasi berkas bernama `Labels.csv`

### TC-FA-LBL-268: Kolom yang ditampilkan kembali ikut diekspor lagi

16. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
17. Hapus centang `Color Hex`
18. Klik `[Save]`
19. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
20. Centang `Color Hex`
21. Klik `[Save]`
22. Klik icon Download
23. Klik `Download as CSV`
24. Verifikasi berkas memuat kelima kolom `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated`

### TC-FA-LBL-267: Kolom yang disembunyikan tidak ikut diekspor

25. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
26. Hapus centang `Color Hex` dan `Last Updated`
27. Klik `[Save]`
28. Klik icon Download
29. Klik `Download as CSV`
30. Verifikasi tidak ada toast atau peringatan tambahan
31. Verifikasi berkas hanya memuat kolom `Label`, `Total Asset`, dan `Modified By`
32. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
33. Centang `Color Hex` dan `Last Updated`
34. Klik `[Save]`

## Notes

- Mode: FE+BE (backend nyata; berkas diunduh dan dibaca). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Urutan blok TC-FA-LBL-268 sebelum TC-FA-LBL-267 membuat blok terakhir berakhir dengan kolom tersembunyi lalu dipulihkan (langkah 32 sampai akhir), sehingga tiap blok mulai dari lima kolom; langkah TC tidak berubah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 memulihkan Search dan Filter sebelum unduhan tanpa saringan (S-09); langkah 32 sampai akhir memulihkan kolom.
- TC-FA-LBL-272 (Download as XLSX, nama berkas, dan sheet) diasersi pada unduhan XLSX TC-FA-LBL-266 dan TC-FA-LBL-271 (Download as CSV, nama berkas) pada unduhan TC-FA-LBL-269, karena langkah aksinya identik dan nama berkas serta sheet tidak bergantung pada saringan; Search dan Filter pada TC-FA-LBL-266 tidak memengaruhi Expected TC-FA-LBL-272.
- Asersi absence toast (langkah 13 dan 30) diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-FA-LBL-266 sampai TC-FA-LBL-272 tidak menyebut mekanisme membuka isi berkas; pembaca CSV/XLSX dan direktori unduhan uji disediakan tim FE (Prerequisites).
