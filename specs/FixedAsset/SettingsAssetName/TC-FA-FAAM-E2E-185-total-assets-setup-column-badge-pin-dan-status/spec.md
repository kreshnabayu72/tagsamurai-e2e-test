---
id: TC-FA-FAAM-E2E-185-total-assets-setup-column-badge-pin-dan-status
title: "Tab Total Assets Setup Column: Badge Pin dan Kelas Status (Ceklis, Geser)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-533
  - TC-FA-FAAM-534
  - TC-FA-FAAM-535
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Badge Pin dan Kelas Status (Ceklis, Geser)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kolom yang diuji: `Brand`, `Model/Type`, `Group` (pin, TC-FA-FAAM-533) dan `Status` (ceklis dan geser, TC-FA-FAAM-534 dan 535).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-533: Pin dan unpin kelas Brand, Model/Type, Group (badge)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, klik icon Pin pada `Brand`, `Model/Type`, dan `Group`
3. Verifikasi Brand: perubahan pin tampil di Live Preview
4. Verifikasi Model/Type: perubahan pin tampil di Live Preview
5. Verifikasi Group: perubahan pin tampil di Live Preview
6. Klik `[Save]`
7. Verifikasi Brand: kolom ter-pin pada tabel
8. Verifikasi Model/Type: kolom ter-pin pada tabel
9. Verifikasi Group: kolom ter-pin pada tabel
10. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
11. Verifikasi Brand: pin tersimpan dan tetap setelah popup dibuka kembali
12. Verifikasi Model/Type: pin tersimpan dan tetap setelah popup dibuka kembali
13. Verifikasi Group: pin tersimpan dan tetap setelah popup dibuka kembali
14. Klik header Actions (⋯), pilih `Setup Column...`, unpin `Brand`, `Model/Type`, dan `Group`, klik `[Save]`
15. Verifikasi kolom Brand, Model/Type, dan Group tidak lagi ter-pin pada tabel

### TC-FA-FAAM-534: Ceklis dan unceklis kelas Status (badge status)

16. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Status`
17. Verifikasi perubahan tampil di Live Preview (kolom Status tidak ada)
18. Klik `[Save]`
19. Verifikasi perubahan tampil di tabel (kolom Status tidak tampil)
20. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
21. Verifikasi perubahan tersimpan dan tetap setelah popup dibuka kembali (kolom Status tetap tidak tampil)
22. Klik header Actions (⋯), pilih `Setup Column...`, centang kembali `Status`, klik `[Save]`
23. Verifikasi kolom Status tampil kembali pada tabel

### TC-FA-FAAM-535: Geser urutan kelas Status (badge status)

24. Klik header Actions (⋯), pilih `Setup Column...`, geser (drag) `Status` ke posisi lain
25. Verifikasi perubahan urutan tampil di Live Preview
26. Klik `[Save]`
27. Verifikasi perubahan urutan tampil di tabel
28. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
29. Verifikasi urutan tersimpan dan tetap setelah popup dibuka kembali

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kolom Brand, Model/Type, dan Group dikerjakan bersamaan dalam satu penyimpanan pada TC-FA-FAAM-533; Expected per kolom punya `Verifikasi` masing-masing.
- Langkah penghubung: unpin dan mencentang kembali kolom sebagai pemulihan (S-09); `Verifikasi` kolom tidak lagi ter-pin dan tampil kembali mengacu pada Expected "Perubahan tampil di tabel". Urutan geser dipulihkan oleh hook `after`.
- "tersimpan per tabel di `localStorage`" hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali (S-13); "pin maksimal tiga kolom" tidak diasersi karena TC tidak memberi langkah memin kolom keempat.
