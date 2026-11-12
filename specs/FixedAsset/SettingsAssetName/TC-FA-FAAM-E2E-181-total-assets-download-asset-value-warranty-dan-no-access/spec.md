---
id: TC-FA-FAAM-E2E-181-total-assets-download-asset-value-warranty-dan-no-access
title: "Tab Total Assets Download: Asset Value, Warranty Expiry, dan Teks No access"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-774
  - TC-FA-FAAM-778
  - TC-FA-FAAM-793
coverage:
  web: automated
---

# Tab Total Assets Download: Asset Value, Warranty Expiry, dan Teks No access

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Purchase HO (Pre-setup #32c) `managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PHO_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Purchase Price (custom field Purchasing, Pre-setup #33e): `AST-2001` 2500, `AST-2003` 0, `AST-2004` 1800, `AST-2005` 3200. Aktor pertama berhak atas seluruh baris (Pre-setup #32e: Manage accounting global dan Manage purchase pada `Head Office` beserta `Finance` dan `Warehouse`); Purchase HO memegang `Manage purchase` pada `Head Office` beserta `Finance`, tanpa `Warehouse`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Kemampuan teknis: pembacaan berkas CSV yang terunduh (nama berkas, header, dan isi sel) disediakan tim FE.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Preferensi Setup Column tersimpan per akun (keputusan pemilik 2026-11-02), jadi centang kolom akun sebelumnya tidak terbawa ke akun berikutnya.
- Kelas harness: binary buffer (isi berkas CSV, bagian 3 prinsip 13f).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-774: Export kolom Asset Value (Commercial) menulis nilai asli, nol, dan kosong untuk Pending

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value (Commercial), klik `[Save]`
3. Klik Download lalu `Download as CSV`
4. Verifikasi berkas CSV terunduh
5. Verifikasi `AST-2001` berisi nilai 15000000
6. Verifikasi `AST-2002` berisi angka nol asli (bukan `-`, bukan teks berformat currency)
7. Verifikasi `AST-2003` dan `AST-2006` (sel `Pending`) ditulis kosong (bukan hyphen `-`, bukan teks `Pending`)

### TC-FA-FAAM-778: Export kolom Warranty Expiry mengikuti General Settings, kosong ditulis strip

8. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry, klik `[Save]`
9. Klik Download lalu `Download as CSV`
10. Verifikasi berkas CSV terunduh
11. Verifikasi `AST-2001` berisi tanggal 31 Mar 2027 dalam format General Settings
12. Verifikasi `AST-2002` (belum ada tanggal garansi) ditulis hyphen tunggal `-`
13. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-793: Download menulis teks No access untuk sel bergerbang dan nilai asli untuk sel berhak

14. Login sebagai Purchase HO (`managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_PHO_PASSWORD`)
15. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
16. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value, Warranty Expiry, Purchase Price, klik `[Save]`
17. Klik Download lalu `Download as CSV`
18. Verifikasi berkas CSV terunduh
19. Verifikasi kolom Asset Value: keenam baris berisi teks `No access`
20. Verifikasi kolom Warranty Expiry: `AST-2001` 31 Mar 2027 (format General Settings), `AST-2002` hyphen tunggal `-`, `AST-2003` 15 Jan 2026
21. Verifikasi kolom Warranty Expiry: `AST-2004`, `AST-2005`, `AST-2006` teks `No access`
22. Verifikasi kolom Purchase Price: `AST-2001` 2500, `AST-2002` `-`, `AST-2003` 0
23. Verifikasi kolom Purchase Price: `AST-2004`, `AST-2005`, `AST-2006` teks `No access`
24. Verifikasi berkas tidak memuat nilai milik baris `No access` (5000000, 20000000, 1800, 3200)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 774 dan 778 (Full Value Access, Pre-setup #32e), lalu ganti akun ke Purchase HO (#32c) untuk 793 (S-07: Logout dan Login ulang adalah langkah ganti akun eksplisit).
- Langkah penghubung: centang kolom lewat Setup Column sebagai precondition, serta menutup popup Detail dan Logout sebelum ganti akun.
- Temuan untuk QA:
  - TC-FA-FAAM-793 Expected b memakai "hyphen tunggal" untuk `AST-2002` dan teks `No access` untuk baris di luar hak; sel `AST-2006` Warranty Expiry nilainya belum ada tetapi di luar hak sehingga ditulis `No access` (bukan `-`).
