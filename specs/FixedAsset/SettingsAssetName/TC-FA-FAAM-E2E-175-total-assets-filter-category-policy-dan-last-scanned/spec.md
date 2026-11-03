---
id: TC-FA-FAAM-E2E-175-total-assets-filter-category-policy-dan-last-scanned
title: "Tab Total Assets Filter: Category Tree Picker, Transactional Policy, dan Last Scanned"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-762
  - TC-FA-FAAM-764
  - TC-FA-FAAM-769
coverage:
  web: automated
---

# Tab Total Assets Filter: Category Tree Picker, Transactional Policy, dan Last Scanned

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Category client memuat `Electronics` dengan turunan `Laptop` dan `Phone`; Category aset `Laptop`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-762: Filter Category memakai Modal Tree Picker multi-select dengan cascade ke turunan

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik Filter, klik field Category (`All categories`)
3. Verifikasi field Category berupa tombol `All categories` yang membuka Modal Tree Picker multi-select
4. Verifikasi tree memuat Category penuh client dengan checkbox per node
5. Verifikasi footer `[Cancel]` dan `[Select]`
6. Centang `Phone`, klik `[Select]`
7. Verifikasi nilai terpilih `Phone` tampil sebagai chip pada field
8. Klik `[Apply]`
9. Verifikasi Title `No results found`
10. Verifikasi Description `Try adjusting your search or filter.`
11. Klik Filter, klik field Category, hapus `Phone`, centang `Electronics`
12. Verifikasi mencentang `Electronics` mencentang turunannya (`Laptop`, `Phone`)
13. Klik `[Select]`, klik `[Apply]`
14. Verifikasi keenam baris tampil karena Category aset adalah turunan node terpilih

### TC-FA-FAAM-764: Filter Transactional Policy dengan empat opsi tetap, OR

15. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (membersihkan filter Category)
16. Klik Filter, amati field Transactional Policy
17. Verifikasi field `Transactional Policy` bertipe multi-select searchable dengan placeholder `All transactions`
18. Buka dropdown Transactional Policy
19. Verifikasi opsi empat transaksi tetap: `Borrow`, `Self Service Borrow`, `Assign`, `Transfer`
20. Pilih `Borrow`, klik `[Apply]`
21. Verifikasi `Borrow` (policy On): keenam baris tampil
22. Klik Filter, klik `[Clear Field]` pada field itu, pilih `Transfer`, klik `[Apply]`
23. Verifikasi `Transfer` (policy Off): Title `No results found`
24. Verifikasi `Transfer` (policy Off): Description `Try adjusting your search or filter.`
25. Klik Filter, pilih `Borrow` dan `Transfer`, klik `[Apply]`
26. Verifikasi `Borrow` dan `Transfer`: keenam baris tampil (OR: salah satu transaksi terpilih On)

### TC-FA-FAAM-769: Filter Last Scanned date range tidak mencocokkan aset yang belum pernah dipindai

27. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (membersihkan filter Transactional Policy)
28. Klik Filter, amati field Last Scanned
29. Verifikasi field `Last Scanned` bertipe date range picker dengan placeholder `Select date`
30. Pilih rentang 01 Oct 2026 sampai 31 Oct 2026, klik `[Apply]`
31. Verifikasi hanya `AST-2001` dan `AST-2003` tampil
32. Verifikasi `AST-2005` (12 Sep 2026) tidak tampil
33. Verifikasi baris `—` (belum pernah dipindai) tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- NC-25 (TC-FA-FAAM-764 mengenai opsi transaksi): spec tidak mengasersi bentuk ikon.
- Langkah penghubung: `[Clear Field]` dan `[Apply]` untuk membersihkan filter antar blok TC (S-09).
- Asersi absence `AST-2005` dan baris `—` didahului anchor positif: `AST-2001` dan `AST-2003` tampil pada tabel hasil yang sama.
- Temuan untuk QA:
  - TC-FA-FAAM-762: LK langkah 5 ("hapus Phone") tidak menyebut cara menghapus pilihan lama; spec membukanya lewat Modal Tree Picker (uncheck `Phone`).
