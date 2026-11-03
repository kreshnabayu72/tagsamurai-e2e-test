---
id: TC-FA-FAAM-E2E-197-total-assets-custom-field-numerik-teks-dan-formula
title: "Tab Total Assets Custom Field: Numeric, Currency, Percentage, Text, Text Area, Phone, Email, URL, dan Document"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-812
  - TC-FA-FAAM-813
coverage:
  web: automated
---

# Tab Total Assets Custom Field: Numeric, Currency, Percentage, Text, Text Area, Phone, Email, URL, dan Document

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field Active tambahan (General, Scope `Column Matrix Item`; Pre-setup #33g): `Qty Count` (Numeric; `AST-2001` 4711, `AST-2004` 4795), `Budget Cost` (Currency; `AST-2001` 1000000, `AST-2004` 3000000), `Completion Pct` (Percentage; `AST-2001` 25, `AST-2004` 75), `Serial Notes` (Text; `SN-1` `AST-2001`), `Notes Area` (Text Area; `AST-2001` `Lantai dua`), `Contact Phone` (Phone; `AST-2001` `081200001111`), `Contact Email` (Email; `AST-2001` `pic.cmx@example.com`), `Web Link` (URL; `AST-2001` `https://example.com/cmx`), `Spec Doc` (Document; `AST-2001` berkas `spec-cmx.pdf`).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Keyword Search TC-FA-FAAM-813 (langkah 22 sampai 23):

| Kolom | Keyword |
|---|---|
| `Serial Notes` (Text) | `SN-1` |
| `Notes Area` (Text Area) | `Lantai` |
| `Contact Phone` (Phone) | `081200001111` |
| `Contact Email` (Email) | `pic.cmx` |
| `Web Link` (URL) | `example.com/cmx` |
| `Spec Doc` (Document) | `spec-cmx` |

- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-812: Numeric, Currency, dan Percentage: Search, Filter range Min–Max, dan Sort numerik

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang `Qty Count`, `Budget Cost`, `Completion Pct`, klik `[Save]`
3. Ketik Search `4795`, tekan Enter
4. Verifikasi Search `4795` menampilkan hanya `AST-2004`
5. Ganti isi kotak search dengan `75`, tekan Enter
6. Verifikasi Search `75` menampilkan hanya `AST-2004`
7. Ganti isi kotak search dengan teks `Budget Cost` `AST-2004` sebagaimana tampil, tekan Enter
8. Verifikasi teks `Budget Cost` `AST-2004` menampilkan hanya `AST-2004`
9. Klik `(←)` pada kotak Search, klik Filter, amati ketiga field
10. Verifikasi Filter Panel memuat field `Qty Count`, `Budget Cost`, `Completion Pct` bertipe range dengan placeholder `Min` dan `Max`
11. Isi `Qty Count` Min `4700` Max `4750`, klik `[Apply]`
12. Verifikasi `Qty Count` 4700 sampai 4750: hanya `AST-2001` tampil
13. Klik Filter, klik `[Clear Field]`, isi `Budget Cost` Min `2000000` Max `4000000`, klik `[Apply]`
14. Verifikasi `Budget Cost` 2000000 sampai 4000000: hanya `AST-2004` tampil
15. Klik Filter, klik `[Clear Field]`, isi `Completion Pct` Min `50` Max `100`, klik `[Apply]`
16. Verifikasi `Completion Pct` 50 sampai 100: hanya `AST-2004` tampil
17. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
18. Klik header `Qty Count` 1 kali
19. Verifikasi sort `Qty Count` klik 1 (ascending numerik): `AST-2001` (4711), `AST-2004` (4795), lalu baris `—` di akhir
20. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Qty Count`, `Budget Cost`, `Completion Pct`, klik `[Save]`

### TC-FA-FAAM-813: Text, Text Area, Phone, Email, URL, dan Document: Search tanpa field Filter

21. Klik header Actions (⋯), pilih `Setup Column...`, centang `Serial Notes`, `Notes Area`, `Contact Phone`, `Contact Email`, `Web Link`, `Spec Doc`, klik `[Save]`

Untuk setiap baris tabel "Keyword Search TC-FA-FAAM-813" pada Prerequisites (langkah 22 sampai 23):

22. Ganti isi kotak search dengan keyword kolom, tekan Enter
23. Verifikasi keyword kolom menampilkan hanya `AST-2001`

24. Klik `(←)` pada kotak Search, klik Filter, amati daftar field
25. Verifikasi Filter Panel tidak memuat field untuk `Serial Notes`, `Notes Area`, `Contact Phone`, `Contact Email`, `Web Link`, dan `Spec Doc`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 22 sampai 23 diulang untuk enam keyword (ekspansi 12 langkah); parameter tiap iterasi ada di tabel "Keyword Search TC-FA-FAAM-813" (bagian 8b butir 7). Total ekspansi spec sekitar 35 langkah; seluruh TC satu kelas harness (fungsional Search, Filter, Sort kolom custom field per Data Type) dan satu dataset.
- Langkah penghubung: `(←)` pada Search, `[Clear Field]` dan `[Apply]` untuk menghapus filter (S-09), serta menghapus centang kolom di akhir blok TC-FA-FAAM-812.
- Asersi absence field Filter (TC-FA-FAAM-813) didahului anchor positif: hasil Search keenam keyword tampil dan Filter Panel terbuka.
- Temuan untuk QA:
  - TC-FA-FAAM-812 Expected a: teks `Budget Cost` `AST-2004` dibaca dari sel sesuai format currency; nilai asli 3000000.
