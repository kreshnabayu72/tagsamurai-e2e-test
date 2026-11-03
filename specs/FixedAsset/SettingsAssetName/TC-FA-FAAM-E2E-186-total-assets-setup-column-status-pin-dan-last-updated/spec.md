---
id: TC-FA-FAAM-E2E-186-total-assets-setup-column-status-pin-dan-last-updated
title: "Tab Total Assets Setup Column: Status Pin dan Last Updated (Ceklis, Geser)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-536
  - TC-FA-FAAM-537
  - TC-FA-FAAM-538
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Status Pin dan Last Updated (Ceklis, Geser)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kolom yang diuji: `Status` (pin, TC-FA-FAAM-536) dan `Last Updated` (ceklis dan geser, TC-FA-FAAM-537 dan 538).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-536: Pin dan unpin kelas Status (badge status)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, klik icon Pin pada `Status`
3. Verifikasi perubahan pin tampil di Live Preview
4. Klik `[Save]`
5. Verifikasi kolom Status ter-pin pada tabel
6. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
7. Verifikasi pin tersimpan dan tetap setelah popup dibuka kembali
8. Klik header Actions (⋯), pilih `Setup Column...`, unpin `Status`, klik `[Save]`
9. Verifikasi kolom Status tidak lagi ter-pin pada tabel

### TC-FA-FAAM-537: Ceklis dan unceklis kelas Last Updated (tanggal)

10. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Last Updated`
11. Verifikasi perubahan tampil di Live Preview (kolom Last Updated tidak ada)
12. Klik `[Save]`
13. Verifikasi perubahan tampil di tabel (kolom Last Updated tidak tampil)
14. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
15. Verifikasi perubahan tersimpan dan tetap setelah popup dibuka kembali (kolom Last Updated tetap tidak tampil)
16. Klik header Actions (⋯), pilih `Setup Column...`, centang kembali `Last Updated`, klik `[Save]`
17. Verifikasi kolom Last Updated tampil kembali pada tabel

### TC-FA-FAAM-538: Geser urutan kelas Last Updated (tanggal)

18. Klik header Actions (⋯), pilih `Setup Column...`, geser (drag) `Last Updated` ke posisi lain
19. Verifikasi perubahan urutan tampil di Live Preview
20. Klik `[Save]`
21. Verifikasi perubahan urutan tampil di tabel
22. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
23. Verifikasi urutan tersimpan dan tetap setelah popup dibuka kembali

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: unpin dan mencentang kembali kolom sebagai pemulihan (S-09); `Verifikasi` kolom tidak lagi ter-pin dan tampil kembali mengacu pada Expected "Perubahan tampil di tabel". Urutan geser dipulihkan oleh hook `after`.
- "tersimpan per tabel di `localStorage`" hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali (S-13); "pin maksimal tiga kolom" tidak diasersi karena TC tidak memberi langkah memin kolom keempat.
