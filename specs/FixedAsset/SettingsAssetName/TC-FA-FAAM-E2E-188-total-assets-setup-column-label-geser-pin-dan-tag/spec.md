---
id: TC-FA-FAAM-E2E-188-total-assets-setup-column-label-geser-pin-dan-tag
title: "Tab Total Assets Setup Column: Label Geser dan Pin serta Kelas TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-715
  - TC-FA-FAAM-716
  - TC-FA-FAAM-755
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Label Geser dan Pin serta Kelas TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26). Setiap aset berlabel `Finance` dan `High Priority`, aset `Dell Latitude - 42` berlabel tambahan `Fragile`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kolom yang diuji: `Label` (curated; geser dan pin, TC-FA-FAAM-715 dan 716) dan `TAG` (default Visible; unceklis, geser, pin, TC-FA-FAAM-755).
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-715: Geser urutan kelas Label (curated)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Label
3. Geser (drag) Label ke posisi lain
4. Verifikasi urutan Live Preview mengikuti posisi baru
5. Klik `[Save]`
6. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
7. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
8. Verifikasi urutan tersimpan dan tetap setelah popup dibuka kembali

### TC-FA-FAAM-716: Pin dan unpin kelas Label (curated)

9. Klik header Actions (⋯), pilih `Setup Column...`, klik icon Pin pada Label, klik `[Save]`
10. Scroll tabel horizontal
11. Verifikasi kolom yang di-pin membeku (sticky) saat scroll horizontal
12. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
13. Verifikasi pin bertahan setelah popup dibuka kembali
14. Klik header Actions (⋯), pilih `Setup Column...`, unpin Label, klik `[Save]`
15. Scroll tabel horizontal
16. Verifikasi kolom Label kembali ikut scroll

### TC-FA-FAAM-755: Kelas TAG (default Visible): unceklis, geser urutan, pin

17. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
18. Klik header Actions (⋯), pilih `Setup Column...`
19. Verifikasi di Popup Setup Column TAG `☑ Hideable` (checked, enabled)
20. Hapus centang TAG lalu centang kembali
21. Geser (drag) TAG ke posisi lain
22. Klik icon Pin pada TAG
23. Verifikasi perubahan ceklis, urutan, dan pin tampil di Live Preview
24. Klik `[Save]`
25. Verifikasi perubahan ceklis, urutan, dan pin tampil di tabel
26. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
27. Verifikasi perubahan tersimpan dan tetap setelah popup dibuka kembali

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- NC-25 (TAG pada TC-FA-FAAM-755): bentuk ikon tipe tag tidak diasersi.
- Urutan TC: 715 sebelum 716 (715 menyimpan Label sebagai kolom tampil sehingga 716 tidak perlu mencentangnya); 755 memakai fixture `Column Matrix Item`.
- Langkah penghubung: unpin sebagai pemulihan sebelum 755 (S-09; `Verifikasi` kolom Label kembali ikut scroll mengacu pada Expected b TC-FA-FAAM-716) dan menutup popup Detail sebelum berpindah fixture. Urutan geser dan kolom curated dipulihkan oleh hook `after`.
- "tersimpan per tabel di `localStorage`" hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali (S-13); "pin maksimal tiga kolom" tidak diasersi karena TC tidak memberi langkah memin kolom keempat.
- Temuan untuk QA:
  - TC-FA-FAAM-715 dan 716 memerlukan kolom Label tampil (Setup Column) tanpa precondition tertulis di LK TC-716; spec mengikuti dengan Label tersimpan dari TC-715.
