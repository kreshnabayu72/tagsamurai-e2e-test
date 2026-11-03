---
id: TC-FA-FAAM-E2E-207-total-assets-gerbang-tanpa-hak-nilai-sensitif
title: "Tab Total Assets Gerbang Akses: Aktor Tanpa Hak Nilai Sensitif (Kolom, Ketersediaan, dan Respons Data)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-787
  - TC-FA-FAAM-794
  - TC-FA-FAAM-800
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Aktor Tanpa Hak Nilai Sensitif (Kolom, Ketersediaan, dan Respons Data)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: No Value Access (Pre-setup #32d) `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOVAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya pada TC-FA-FAAM-794 (ganti akun eksplisit; langkah 19 sampai 23 dan langkah 24); lisensi `FA-7` aktif pada client utama (Pre-setup #33e):

| Akun | Pre-setup | Email | Password | Kolom tersedia | Kolom tidak tersedia |
|---|---|---|---|---|---|
| Asset Value HO | #32 | `assetValueHO_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AVHO_PASSWORD` | `Asset Value`, `Warranty Expiry` | `Purchase Price`, `Accounting Code` |
| Accounting Global | #32b | `manageAccounting_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ACCG_PASSWORD` | `Asset Value`, `Warranty Expiry`, `Accounting Code` | `Purchase Price` |
| Purchase HO | #32c | `managePurchaseHO_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_PHO_PASSWORD` | `Asset Value`, `Warranty Expiry`, `Purchase Price` | `Accounting Code` |

- Akun terakhir TC-FA-FAAM-794: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; keempat kolom tersedia.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Nilai: `AST-2001` Warranty 31 Mar 2027, `AST-2004` 30 Jun 2028, `AST-2005` 01 Feb 2025, `AST-2003` 15 Jan 2026; `Accounting Code` `ACC-1` `AST-2001` dan `ACC-4` `AST-2004` (Pre-setup #33e). Aktor pertama (No Value Access) tanpa View asset value, Manage purchase, dan Manage accounting.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kemampuan teknis (TC-FA-FAAM-800): pengamatan respons jaringan data Tab Total Assets dari halaman dan klien HTTP bersesi aktor yang sama untuk request langsung ke endpoint data Tab Total Assets `Column Matrix Item`; endpoint tidak disebut TC, PRD, atau LLD dan disediakan tim BE/FE (S-13).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-787: Gerbang akses sel: aktor tanpa hak nilai sensitif

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
3. Verifikasi Setup Column memuat `Asset Value` dan `Warranty Expiry`
4. Verifikasi Setup Column tidak memuat `Purchase Price` dan `Accounting Code`
5. Centang Asset Value dan Warranty Expiry (kolom `Purchase Price` dan `Accounting Code` tidak tersedia pada daftar), klik `[Save]`
6. Verifikasi Asset Value: keenam baris `No access`, termasuk `AST-2003` dan `AST-2006` yang nilainya belum ada
7. Verifikasi Warranty Expiry: keenam baris `No access`
8. Verifikasi sel kolom Name, Asset ID, Brand, Group, Status tetap tampil normal pada keenam baris

### TC-FA-FAAM-800: Respons data Tab Total Assets tidak memuat nilai sel No access

9. Tutup popup Detail, klik nama `Column Matrix Item` dengan pemantauan respons jaringan, klik tab `Total Assets (6)`
10. Periksa payload respons data tab untuk keenam baris
11. Verifikasi payload tidak memuat nilai Asset Value (15000000, 5000000, 20000000)
12. Verifikasi payload tidak memuat nilai Warranty Expiry (31 Mar 2027, 30 Jun 2028, 01 Feb 2025, 15 Jan 2026)
13. Verifikasi sel Asset Value dan Warranty Expiry hanya ditandai sebagai `No access`
14. Kirim request langsung ke endpoint data Tab Total Assets `Column Matrix Item` memakai sesi aktor yang sama
15. Verifikasi respons request langsung memberi payload yang sama (tanpa nilai)

### TC-FA-FAAM-794: Ketersediaan kolom Purchasing dan Accounting per hak aktor

16. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`
17. Verifikasi `No Value Access`: `Asset Value` dan `Warranty Expiry` tersedia
18. Verifikasi `No Value Access`: `Purchase Price` dan `Accounting Code` tidak tersedia

Untuk setiap baris tabel "Akun" pada Prerequisites (langkah 19 sampai 23):

19. Tekan Esc, tutup popup Detail, klik tombol akun, pilih Logout
20. Login sebagai akun baris tabel (email dan password dari tabel), buka Fixed Asset > Settings > Asset Master > Asset Name
21. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`
22. Verifikasi kolom tersedia sesuai kolom "Kolom tersedia" pada baris tabel
23. Verifikasi kolom tidak tersedia sesuai kolom "Kolom tidak tersedia" pada baris tabel

24. Tekan Esc, tutup popup Detail, klik tombol akun, pilih Logout
25. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`), buka Fixed Asset > Settings > Asset Master > Asset Name
26. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`
27. Verifikasi `Full Value Access`: keempat kolom `Asset Value`, `Warranty Expiry`, `Purchase Price`, dan `Accounting Code` tersedia

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-FA-FAAM-800 adalah TC defense-in-depth dengan Expected respons API (payload respons data tab dan request langsung ke server) yang tetap masuk spec FE+BE; asersi request langsung hanya respons server (bagian 8b butir 1). Tidak ada asersi pengalihan halaman atau toast pada request langsung.
- Spec Role Matrix per blok role (bagian 3a): langkah 19 sampai 23 diulang untuk tiga akun (ekspansi 15 langkah, total ekspansi spec 37 langkah) karena langkah tiap akun identik dan hanya akun login yang berbeda (matriks ketersediaan kolom per role); ganti akun menuntut Step eksplisit sehingga akun pertama login di hook `before`. Akun terakhir (Full Value Access) ditulis terpisah (langkah 24) karena tidak punya kolom yang tidak tersedia.
- Langkah penghubung: menekan Esc untuk menutup popup Setup Column, menutup popup Detail, dan Logout sebelum ganti akun.
- Konfigurasi kolom Asset Value dan Warranty Expiry dari blok TC-FA-FAAM-787 masih tersimpan saat blok TC-FA-FAAM-800 dimulai; langkah mencentang kedua kolom pada LK TC-800 tidak diulang agar tidak membatalkan centang yang tersimpan.
- Temuan untuk QA:
  - TC-FA-FAAM-794 ACC menyebut Pre-setup #32 sampai #32e (lima akun); spec mengerjakan No Value Access (#32d) sebagai akun pertama, lalu #32, #32b, #32c, dan #32e.
  - TC-FA-FAAM-800: payload respons dan endpoint tidak disebut di TC; spec memakai kemampuan pengamatan respons/klien HTTP yang disediakan tim BE/FE tanpa endpoint karangan.
  - TC-FA-FAAM-787 LK langkah 4 bersyarat ("bila tersedia"); spec menulis centang hanya pada kolom yang terbukti tersedia lewat Expected a.
