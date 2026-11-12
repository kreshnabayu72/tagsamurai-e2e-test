---
id: TC-FA-FAAM-E2E-209-total-assets-hak-tier-role-matrix-global-dan-group-manager
title: "Tab Total Assets Gerbang Akses: Hak Tier Total Control, Default User, Read Only, dan Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-804
  - TC-FA-FAAM-805
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Hak Tier Total Control, Default User, Read Only, dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya pada TC-FA-FAAM-804 (ganti akun eksplisit; langkah 10 sampai 19); tabel "Role yang diuji":

| Role | Pre-setup | Email | Password |
|---|---|---|---|
| Default User | #32f | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| Read Only | #2 | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Akun TC-FA-FAAM-805: Group Manager (Pre-setup #32g) `groupManagerAssetName_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD` (di-assign pada `Head Office` beserta `Finance`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Nilai: Warranty `AST-2001` 31 Mar 2027, `AST-2003` 15 Jan 2026, `AST-2004` 30 Jun 2028, `AST-2005` 01 Feb 2025; `Purchase Price` 2500 `AST-2001`, 0 `AST-2003`, 1800 `AST-2004`, 3200 `AST-2005`; `Accounting Code` `ACC-1` `AST-2001`, `ACC-4` `AST-2004`; lisensi `FA-7` aktif (Pre-setup #33e).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-804: Hak tier menurut role_matrix(): Total Control, Default User, dan Read Only

Total Control (akun hook `before`):

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
3. Verifikasi Setup Column memuat `Asset Value`, `Warranty Expiry`, `Purchase Price`, dan `Accounting Code`
4. Centang Asset Value, Warranty Expiry, `Purchase Price`, `Accounting Code`, klik `[Save]`
5. Verifikasi Asset Value: 15000000, currency nol (mis. `Rp 0,00`), `Pending`, 5000000, 20000000, `Pending` berurutan `AST-2001` sampai `AST-2006`
6. Verifikasi Warranty Expiry: 31 Mar 2027, `—`, 15 Jan 2026, 30 Jun 2028, 01 Feb 2025, `—` berurutan
7. Verifikasi Purchase Price: 2500, `—`, `0`, 1800, 3200, `—` berurutan
8. Verifikasi Accounting Code: `ACC-1`, `—`, `—`, `ACC-4`, `—`, `—` berurutan
9. Verifikasi tidak ada sel `No access` (termasuk baris Warehouse)

Untuk setiap baris tabel "Role yang diuji" pada Prerequisites (langkah 10 sampai 19):

10. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang keempat kolom, klik `[Save]`, tutup popup Detail, klik tombol akun, pilih Logout
11. Login sebagai role baris tabel (email dan password dari tabel), buka Fixed Asset > Settings > Asset Master > Asset Name
12. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`
13. Verifikasi Setup Column memuat `Asset Value`, `Warranty Expiry`, `Purchase Price`, dan `Accounting Code`
14. Centang Asset Value, Warranty Expiry, `Purchase Price`, `Accounting Code`, klik `[Save]`
15. Verifikasi Asset Value: 15000000, currency nol (mis. `Rp 0,00`), `Pending`, 5000000, 20000000, `Pending` berurutan `AST-2001` sampai `AST-2006`
16. Verifikasi Warranty Expiry: 31 Mar 2027, `—`, 15 Jan 2026, 30 Jun 2028, 01 Feb 2025, `—` berurutan
17. Verifikasi Purchase Price: 2500, `—`, `0`, 1800, 3200, `—` berurutan
18. Verifikasi Accounting Code: `ACC-1`, `—`, `—`, `ACC-4`, `—`, `—` berurutan
19. Verifikasi tidak ada sel `No access` (termasuk baris Warehouse)

### TC-FA-FAAM-805: Hak tier Group Manager menurut role_matrix()

20. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang keempat kolom, klik `[Save]`, tutup popup Detail, klik tombol akun, pilih Logout
21. Login sebagai Group Manager (`groupManagerAssetName_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_GM_PASSWORD`), buka Fixed Asset > Settings > Asset Master > Asset Name
22. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
23. Verifikasi Setup Column memuat `Asset Value`, `Warranty Expiry`, dan `Purchase Price`
24. Verifikasi Setup Column tidak memuat `Accounting Code`
25. Centang Asset Value, Warranty Expiry, dan `Purchase Price`, klik `[Save]`
26. Verifikasi Asset Value: `AST-2001` 15000000, `AST-2002` currency nol (mis. `Rp 0,00`), `AST-2003` `Pending`; `AST-2004`, `AST-2005`, `AST-2006` `No access`
27. Verifikasi Warranty Expiry: `AST-2001` 31 Mar 2027, `AST-2002` `—`, `AST-2003` 15 Jan 2026; `AST-2004`, `AST-2005`, `AST-2006` `No access`
28. Verifikasi Purchase Price: `AST-2001` 2500, `AST-2002` `—`, `AST-2003` `0`; `AST-2004`, `AST-2005`, `AST-2006` `No access`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix (bagian 3a): TC-FA-FAAM-804 memakai perulangan atas tabel "Role yang diuji" (langkah 10 sampai 19, ekspansi 22 langkah, total ekspansi spec sekitar 39 langkah) karena langkah tiga tier (Total Control, Default User, Read Only) identik dan hanya akun login yang berbeda; Total Control login di hook `before` dan dikerjakan langkah demi langkah di atas perulangan, karena ganti akun menuntut Step eksplisit. TC-FA-FAAM-805 ditulis terpisah karena hasilnya berbeda (hak terbatas group, tanpa Accounting).
- Langkah penghubung: menghapus centang kolom, menutup popup Detail, dan Logout sebelum ganti akun (S-09, S-07).
- Aktor ACC TC-FA-FAAM-804: Total Control (#1), Default User (#32f), Read Only (#2).
- Temuan untuk QA:
  - TC-FA-FAAM-804 LK langkah 6 dan 7 ("ulangi langkah 1 sampai 5") ditulis sebagai isi perulangan.
  - TC-FA-FAAM-805 Expected b memakai Asset Value `AST-2003` `Pending` untuk aktor Group Manager pada group `Finance` (descendant `Head Office`), selaras Pre-setup #32g.
