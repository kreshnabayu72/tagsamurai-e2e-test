---
id: TC-FA-FAAM-E2E-184-total-assets-setup-column-badge-ceklis-dan-geser
title: "Tab Total Assets Setup Column: Kelas Brand, Model/Type, Group (Ceklis dan Geser)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-531
  - TC-FA-FAAM-532
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Kelas Brand, Model/Type, Group (Ceklis dan Geser)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kolom yang diuji pada kedua TC: `Brand`, `Model/Type`, `Group` (badge), dikerjakan bersamaan dalam satu penyimpanan per TC.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-531: Ceklis dan unceklis kelas Brand, Model/Type, Group (badge)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Brand`, `Model/Type`, dan `Group`
3. Verifikasi Brand: perubahan tampil di Live Preview (kolom tidak ada)
4. Verifikasi Model/Type: perubahan tampil di Live Preview (kolom tidak ada)
5. Verifikasi Group: perubahan tampil di Live Preview (kolom tidak ada)
6. Klik `[Save]`
7. Verifikasi Brand: perubahan tampil di tabel (kolom tidak tampil)
8. Verifikasi Model/Type: perubahan tampil di tabel (kolom tidak tampil)
9. Verifikasi Group: perubahan tampil di tabel (kolom tidak tampil)
10. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
11. Verifikasi Brand: perubahan tersimpan dan tetap setelah popup dibuka kembali
12. Verifikasi Model/Type: perubahan tersimpan dan tetap setelah popup dibuka kembali
13. Verifikasi Group: perubahan tersimpan dan tetap setelah popup dibuka kembali
14. Klik header Actions (⋯), pilih `Setup Column...`, centang kembali `Brand`, `Model/Type`, dan `Group`, klik `[Save]`
15. Verifikasi kolom Brand, Model/Type, dan Group tampil kembali pada tabel

### TC-FA-FAAM-532: Geser urutan kelas Brand, Model/Type, Group (badge)

16. Klik header Actions (⋯), pilih `Setup Column...`, geser (drag) `Brand`, `Model/Type`, dan `Group` ke posisi lain
17. Verifikasi Brand: perubahan urutan tampil di Live Preview
18. Verifikasi Model/Type: perubahan urutan tampil di Live Preview
19. Verifikasi Group: perubahan urutan tampil di Live Preview
20. Klik `[Save]`
21. Verifikasi Brand: perubahan urutan tampil di tabel
22. Verifikasi Model/Type: perubahan urutan tampil di tabel
23. Verifikasi Group: perubahan urutan tampil di tabel
24. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
25. Verifikasi Brand: urutan tersimpan dan tetap setelah popup dibuka kembali
26. Verifikasi Model/Type: urutan tersimpan dan tetap setelah popup dibuka kembali
27. Verifikasi Group: urutan tersimpan dan tetap setelah popup dibuka kembali

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Ketiga kolom dikerjakan bersamaan dalam satu penyimpanan per TC; Expected per kolom (butir a, b, c) masing-masing punya `Verifikasi`.
- Langkah penghubung: mencentang kembali kolom sebagai pemulihan sebelum TC berikutnya (S-09); `Verifikasi` kolom tampil kembali mengacu pada Expected "Perubahan tampil di tabel" untuk arah ceklis. Urutan geser dipulihkan oleh hook `after`.
- "tersimpan per tabel di `localStorage`" hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali (S-13); "pin maksimal tiga kolom" pada Expected tidak diasersi karena TC tidak memuat langkah pin untuk kelas ini.
- Spec ini sekitar 30 langkah; seluruh TC satu kelas harness dan satu dataset.
