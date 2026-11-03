---
id: TC-FA-LBL-E2E-073-download-labels-list-nol-baris-dan-urutan-sort
title: "Download Labels List: Nol Baris Hasil dan Urutan Baris Mengikuti Sort"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-274
  - TC-FA-LBL-276
coverage:
  web: automated
---

# Download Labels List: Nol Baris Hasil dan Urutan Baris Mengikuti Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Total Asset |
  |---|---|
  | `High Priority` | 3 |
  | `Finance Department` | 5 |
  | `Audit Ready` | 2 |
  | `Executive Asset` | 1 |
  | `Maintenance Due` | 4 |
  | `Seasonal Event` | 0 |
  | `Night Shift` | 0 |
  | `Warehouse Priority` | 0 |
  | `Field Kit` | 2 |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.
- Kemampuan teknis (disediakan tim FE): direktori unduhan uji untuk menangkap berkas dan pembaca CSV (header dan baris).

## Test Steps

### TC-FA-LBL-274: Download dengan nol baris hasil tetap aktif dan hanya berisi header

1. Ketik Search `zzzz`, tekan Enter
2. Verifikasi icon Download tetap aktif
3. Klik icon Download
4. Klik `Download as CSV`
5. Verifikasi tidak ada toast
6. Verifikasi berkas terunduh hanya memuat baris header kolom yang visible: `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated`
7. Klik `(←)` pada kotak Search

### TC-FA-LBL-276: Urutan baris file mengikuti Sort aktif

8. Klik header `Total Asset` sekali
9. Klik icon Download
10. Klik `Download as CSV`
11. Verifikasi baris berkas berurutan Total Asset Ascending (0, 0, 0, 1, 2, 2, 3, 4, 5) sama dengan urutan baris tabel
12. Klik header `Total Asset` dua kali sampai indikator sort netral

## Notes

- Mode: FE+BE (backend nyata; berkas diunduh dan dibaca). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 mereset Search dengan `(←)` (bagian 8b butir 9) agar TC-FA-LBL-276 mengekspor seluruh baris; langkah 12 mengembalikan sort ke netral (S-09).
- Asersi absence toast pada langkah 5 diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada langkah 6 (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-FA-LBL-274 dan TC-FA-LBL-276 tidak menyebut mekanisme membuka isi berkas; pembaca CSV dan direktori unduhan uji disediakan tim FE (Prerequisites).
