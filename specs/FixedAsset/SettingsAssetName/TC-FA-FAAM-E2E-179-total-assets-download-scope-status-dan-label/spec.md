---
id: TC-FA-FAAM-E2E-179-total-assets-download-scope-status-dan-label
title: "Tab Total Assets Download: Cakupan Search-Filter, Kolom Status, dan Kolom Label"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-523
  - TC-FA-FAAM-525
  - TC-FA-FAAM-718
coverage:
  web: automated
---

# Tab Total Assets Download: Cakupan Search-Filter, Kolom Status, dan Kolom Label

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26). Setiap aset berlabel `Finance` dan `High Priority`, aset `Dell Latitude - 42` berlabel tambahan `Fragile`; `Unlabeled Asset Item` (Total Asset 1, aset `AST-1301` tanpa label; Pre-setup #26f).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Kemampuan teknis: pembacaan berkas CSV yang terunduh (nama berkas, header, dan isi sel) disediakan tim FE.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kelas harness: binary buffer (isi berkas CSV, bagian 3 prinsip 13f); nama berkas, header, dan jumlah baris adalah asersi fungsional.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-523: Download mencakup seluruh hasil sesuai Search dan Filter

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik Filter, pilih Status `Active`, klik `[Apply]`
3. Klik Download lalu `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas `Asset-Name-Assets.csv` terunduh
6. Verifikasi berkas memuat seluruh aset Active (bukan hanya halaman aktif) dengan 8 kolom tabel
7. Verifikasi kolom Name ada dan berformat `Dell Latitude - [Increment]`
8. Verifikasi kolom Asset ID ada dan berisi Asset ID tiap aset
9. Verifikasi kolom Brand ada dan berisi `Dell`
10. Verifikasi kolom Model/Type ada dan berisi model tiap aset
11. Verifikasi kolom Group ada dan berisi Group tiap aset
12. Verifikasi kolom TAG ada dan berisi label tipe tag aktif dipisah `, ` (aset tanpa tag aktif ditulis `-`)

### TC-FA-FAAM-525: Export kolom Status memakai label badge dipisah koma

13. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (membersihkan filter Status)
14. Klik Download lalu `Download as CSV`
15. Verifikasi berkas CSV terunduh
16. Verifikasi sel Status baris aset `Borrowed` dengan `Damaged` berisi label badge dipisah `, ` tanpa warna

### TC-FA-FAAM-718: Export kolom Label berisi seluruh label dipisah koma

17. Klik header Actions (⋯), pilih `Setup Column...`, centang Label, klik `[Save]` (precondition TC: kolom curated Label sudah ditampilkan; dipakai sebagai precondition, tidak diasersi)
18. Klik Download lalu `Download as CSV`
19. Verifikasi berkas CSV terunduh
20. Verifikasi sel Label baris `Dell Latitude - 42` berisi `Finance, Fragile, High Priority` (seluruh label urut A–Z, termasuk yang tersembunyi di balik `+1 more`, dipisah `, `)
21. Tutup popup Detail, klik nama `Unlabeled Asset Item`, klik tab `Total Assets (1)`
22. Klik Download lalu `Download as CSV`
23. Verifikasi berkas CSV kedua terunduh
24. Verifikasi sel Label aset `AST-1301` (tanpa label) ditulis hyphen tunggal `-`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: `[Clear Field]` dan `[Apply]` untuk membersihkan filter Status sebelum TC-FA-FAAM-525 (S-09), centang Label (precondition TC-FA-FAAM-718), serta menutup popup Detail sebelum berpindah fixture.
- Absence "tanpa toast sukses" (TC-FA-FAAM-523) diletakkan segera sesudah pemicu Download dan sebelum asersi berkas (bagian 8b butir 11); berkas terunduh menjadi anchor positif.
- Temuan untuk QA:
  - TC-FA-FAAM-523 menyebut "8 kolom tabel" pada berkas padahal kolom curated tersembunyi secara default; spec mengasersi 8 kolom default.
  - TC-FA-FAAM-718 memerlukan kolom Label tampil (precondition) tanpa langkah memunculkannya di LK; spec menambah langkah centang Label.
