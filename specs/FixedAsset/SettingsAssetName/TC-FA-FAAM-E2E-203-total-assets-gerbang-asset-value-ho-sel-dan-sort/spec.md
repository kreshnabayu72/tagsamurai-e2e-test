---
id: TC-FA-FAAM-E2E-203-total-assets-gerbang-asset-value-ho-sel-dan-sort
title: "Tab Total Assets Gerbang Akses: Aktor Asset Value HO (Sel dan Sort No access Paling Akhir)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-784
  - TC-FA-FAAM-790
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Aktor Asset Value HO (Sel dan Sort No access Paling Akhir)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Asset Value HO (Pre-setup #32) `assetValueHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AVHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Purchase HO (Pre-setup #32c) `managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PHO_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Asset Value HO memegang `View asset value` pada `Head Office` beserta `Finance` (tanpa Manage purchase dan Manage accounting); Purchase HO memegang `Manage purchase` pada `Head Office` beserta `Finance` (tidak pada `Warehouse`). Custom field Purchasing `Purchase Price`: `AST-2001` 2500, `AST-2003` 0, `AST-2004` 1800, `AST-2005` 3200 (Pre-setup #33e).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-784: Gerbang akses sel: aktor View asset value pada Head Office (Asset Value berhak, Warranty No access)

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
3. Verifikasi Setup Column memuat `Asset Value` dan `Warranty Expiry`
4. Verifikasi Setup Column tidak memuat kolom `Purchase Price` dan `Accounting Code`
5. Centang Asset Value dan Warranty Expiry (kolom `Purchase Price` dan `Accounting Code` tidak tersedia pada daftar), klik `[Save]`
6. Verifikasi Asset Value: `AST-2001` 15000000, `AST-2002` currency nol (mis. `Rp 0,00`), `AST-2003` `Pending`
7. Verifikasi Asset Value: `AST-2004`, `AST-2005`, `AST-2006` `No access`
8. Verifikasi Warranty Expiry: keenam baris `No access` (aktor tidak memegang Manage purchase di group mana pun)
9. Verifikasi sel kolom Name, Asset ID, Brand, Group, Status tetap tampil normal pada keenam baris
10. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Asset Value dan Warranty Expiry, klik `[Save]`

### TC-FA-FAAM-790: Sort kolom bergerbang: baris No access selalu paling akhir dan baris Pending tepat sebelumnya pada ascending dan descending

11. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value, klik `[Save]`
12. Klik header Asset Value 1 kali
13. Verifikasi Asset Value (aktor `Asset Value HO`) klik 1 (ascending): `AST-2002` (0), `AST-2001`, `AST-2003` (`Pending`), lalu `AST-2004`, `AST-2005`, `AST-2006` (`No access`) di akhir
14. Klik header Asset Value 1 kali lagi
15. Verifikasi Asset Value klik 2 (descending): `AST-2001`, `AST-2002`, `AST-2003` (`Pending`) tepat sebelum ketiga baris `No access` yang tetap di akhir
16. Tutup popup Detail, klik tombol akun, pilih Logout
17. Login sebagai Purchase HO (`managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_PHO_PASSWORD`)
18. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
19. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry dan Purchase Price, klik `[Save]`
20. Klik header Warranty Expiry 1 kali
21. Verifikasi Warranty Expiry (aktor `Purchase HO`) klik 1 (`Oldest First`): `AST-2003`, `AST-2001`, `AST-2002` (`—`), lalu ketiga baris `No access` di akhir
22. Klik header Warranty Expiry 1 kali lagi
23. Verifikasi Warranty Expiry klik 2 (`Newest First`): `AST-2002` (`—`), `AST-2001`, `AST-2003`, lalu ketiga baris `No access` tetap di akhir
24. Klik header Purchase Price 1 kali
25. Verifikasi Purchase Price klik 1 (ascending): `AST-2003` (0), `AST-2001`, `AST-2002` (`—`), lalu ketiga baris `No access` di akhir
26. Klik header Purchase Price 1 kali lagi
27. Verifikasi Purchase Price klik 2 (descending): `AST-2002` (`—`), `AST-2001`, `AST-2003`, lalu ketiga baris `No access` tetap di akhir

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix per blok role (bagian 3a): TC-FA-FAAM-790 memakai dua aktor (Asset Value HO lalu Purchase HO) dengan Step ganti akun eksplisit; akun pertama login di hook `before` (bagian 3a, KEPUTUSAN 2026-10-30). Aktor kedua (Purchase HO, Pre-setup #32c) tertulis di ACC TC-FA-FAAM-790.
- Langkah penghubung: menghapus centang kolom di akhir blok TC-FA-FAAM-784 (S-09), menutup popup Detail, dan Logout sebelum ganti akun.
- Urutan di antara ketiga baris `No access` tidak diasersi (sesuai TC).
- Temuan untuk QA:
  - TC-FA-FAAM-784 LK langkah 4 ("kolom Purchase Price dan Accounting Code bila tersedia") bersyarat; spec menulis centang hanya pada kolom yang terbukti tersedia lewat Expected a.
