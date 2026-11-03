---
id: TC-FA-FAAM-E2E-177-total-assets-sort-status-last-updated-label-dan-tag
title: "Tab Total Assets Sort: Status, Last Updated, Label, dan TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-520
  - TC-FA-FAAM-521
  - TC-FA-FAAM-713
  - TC-FA-FAAM-752
coverage:
  web: automated
---

# Tab Total Assets Sort: Status, Last Updated, Label, dan TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26). Setiap aset berlabel `Finance` dan `High Priority` (41 aset memiliki 2 label), aset `Dell Latitude - 42` berlabel tambahan `Fragile` (3 label).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-520: Sort kelas Status

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Status 1 kali
3. Verifikasi klik 1: A-Z menurut gabungan label badge sesuai urutan tampil
4. Klik header Status 1 kali lagi
5. Verifikasi klik 2: Z-A
6. Klik header Status 1 kali lagi
7. Verifikasi klik 3: kembali ke default Last Updated Newest First

### TC-FA-FAAM-521: Sort kelas Last Updated (default Newest First)

8. Klik header Last Updated 1 kali
9. Verifikasi klik 1: `Oldest First`
10. Klik header Last Updated 1 kali lagi
11. Verifikasi klik 2: `Newest First`
12. Klik header Last Updated 1 kali lagi
13. Verifikasi klik 3: kembali ke default Last Updated Newest First

### TC-FA-FAAM-713: Sort kelas Label (jumlah label, tiebreaker label pertama)

14. Klik header Actions (⋯), pilih `Setup Column...`, centang Label, klik `[Save]` (precondition TC: kolom curated Label sudah ditampilkan; dipakai sebagai precondition, tidak diasersi)
15. Klik header Label 1 kali
16. Verifikasi klik 1: ascending, jumlah label paling sedikit dulu
17. Pindah ke halaman terakhir pada pagination
18. Verifikasi klik 1: `Dell Latitude - 42` (3 label) di urutan terakhir (halaman terakhir, langkah 17)
19. Kembali ke halaman 1 pada pagination
20. Klik header Label 1 kali lagi
21. Verifikasi klik 2: descending, jumlah label paling banyak dulu
22. Verifikasi klik 2: `Dell Latitude - 42` di baris pertama halaman 1
23. Verifikasi klik 2: badge di dalam sel tetap urut A–Z
24. Klik header Label 1 kali lagi
25. Verifikasi klik 3: urutan kembali ke default tabel (Last Updated Newest First)

### TC-FA-FAAM-752: Sort kelas TAG (alfabetis atas urutan label ikon, awalan lebih pendek lebih dulu, sel kosong di ujung)

26. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
27. Klik header TAG 1 kali
28. Verifikasi klik 1 (ascending): `AST-2006` (`NFC`), `AST-2005` (`NFC, QR`), `AST-2002` (`QR`), `AST-2001` (`QR, RFID`), `AST-2004` (`RFID`), lalu `AST-2003` (`—`) di akhir
29. Klik header TAG 1 kali lagi
30. Verifikasi klik 2 (descending): `AST-2003` (`—`) di awal, lalu `AST-2004`, `AST-2001`, `AST-2002`, `AST-2005`, `AST-2006`
31. Klik header TAG 1 kali lagi
32. Verifikasi klik 3: kembali ke default Last Updated Newest First

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- NC-25 (TC-FA-FAAM-752): label tipe tag tiap baris diasersi lewat label aksesibilitas ikon; bentuk ikon tidak diasersi.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): centang Label (precondition TC-FA-FAAM-713), pindah ke halaman terakhir (langkah 17) sebelum asersi `Dell Latitude - 42` di urutan terakhir, kembali ke halaman 1 (langkah 19) sebelum klik kedua, dan menutup popup Detail sebelum berpindah fixture.
- Temuan untuk QA:
  - TC-FA-FAAM-713 memerlukan kolom Label tampil (precondition) tanpa langkah memunculkannya di LK; spec menambah langkah centang Label.
  - TC-FA-FAAM-520: contoh baris urutan Status tidak diberikan TC; spec mengasersi urutan umum A-Z dan Z-A menurut gabungan label badge.
