---
id: TC-FA-FAAM-E2E-178-total-assets-sort-kolom-seragam-last-scanned-warranty-dan-asset-value
title: "Tab Total Assets Sort: Last Scanned, Warranty Expiry, dan Asset Value (Commercial)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-768
  - TC-FA-FAAM-772
  - TC-FA-FAAM-776
coverage:
  web: automated
---

# Tab Total Assets Sort: Last Scanned, Warranty Expiry, dan Asset Value (Commercial)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-768: Sort kelas Last Scanned (Oldest First / Newest First, strip di ujung)

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Last Scanned, klik `[Save]`
3. Klik header Last Scanned 1 kali
4. Verifikasi klik 1 (`Oldest First`): `AST-2005`, `AST-2003`, `AST-2001`, lalu `AST-2002`, `AST-2004`, `AST-2006` (`—`) di akhir (urutan di antara baris `—` tidak diasersikan)
5. Klik header Last Scanned 1 kali lagi
6. Verifikasi klik 2 (`Newest First`): baris `—` di awal, lalu `AST-2001`, `AST-2003`, `AST-2005`
7. Klik header Last Scanned 1 kali lagi
8. Verifikasi klik 3: kembali ke default Last Updated Newest First
9. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-776: Sort kelas Warranty Expiry (Oldest First / Newest First, strip di ujung)

10. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`)
11. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
12. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry, klik `[Save]`
13. Klik header Warranty Expiry 1 kali
14. Verifikasi klik 1 (`Oldest First`): `AST-2005`, `AST-2003`, `AST-2001`, `AST-2004`, lalu `AST-2002` dan `AST-2006` (`—`) di akhir (urutan di antara baris `—` tidak diasersikan)
15. Klik header Warranty Expiry 1 kali lagi
16. Verifikasi klik 2 (`Newest First`): baris `—` di awal, lalu `AST-2004`, `AST-2001`, `AST-2003`, `AST-2005`
17. Klik header Warranty Expiry 1 kali lagi
18. Verifikasi klik 3: kembali ke default Last Updated Newest First

### TC-FA-FAAM-772: Sort kelas Asset Value (Commercial) (numerik, Pending di ujung)

19. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value (Commercial), klik `[Save]`
20. Klik header Asset Value (Commercial) 1 kali
21. Verifikasi klik 1 (ascending numerik): `AST-2002` (0), `AST-2004`, `AST-2001`, `AST-2005`, lalu `AST-2003` dan `AST-2006` (`Pending`) di akhir (urutan di antara baris `Pending` tidak diasersikan)
22. Klik header Asset Value (Commercial) 1 kali lagi
23. Verifikasi klik 2 (descending): `AST-2005`, `AST-2001`, `AST-2004`, `AST-2002`, lalu baris `Pending` tetap di akhir
24. Klik header Asset Value (Commercial) 1 kali lagi
25. Verifikasi klik 3: kembali ke default Last Updated Newest First

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 768 (Total Control), lalu ganti akun ke Full Value Access untuk 776 dan 772 (S-07: ganti akun punya langkah eksplisit; Logout dan Login ulang adalah langkah ganti akun). TC-FA-FAAM-776 dan 772 memakai aktor `#32e` menurut ACC.
- Langkah penghubung: centang kolom lewat Setup Column sebagai precondition, menutup popup Detail dan Logout sebelum ganti akun.
- Pembagian TC lintas spec: TC-FA-FAAM-765 (Sort Measurement, Category, Transactional Policy) ada di spec 211 (`TC-FA-FAAM-E2E-211-total-assets-sort-kolom-seragam-measurement-category-dan-policy`).
- Temuan untuk QA:
  - TC-FA-FAAM-768, 776, 772: tidak ada pembanding urutan di antara baris `—` (772: `Pending`); TC sendiri menyatakan tidak diasersikan.
