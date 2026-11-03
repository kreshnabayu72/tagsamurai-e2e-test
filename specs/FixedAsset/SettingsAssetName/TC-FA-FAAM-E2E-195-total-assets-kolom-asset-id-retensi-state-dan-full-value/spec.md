---
id: TC-FA-FAAM-E2E-195-total-assets-kolom-asset-id-retensi-state-dan-full-value
title: "Tab Total Assets: Asset ID Tidak Filterable, Pindah Tab Memulihkan State Kolom Curated, dan Aktor Full Value Access"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-788
  - TC-FA-FAAM-796
  - TC-FA-FAAM-808
coverage:
  web: automated
---

# Tab Total Assets: Asset ID Tidak Filterable, Pindah Tab Memulihkan State Kolom Curated, dan Aktor Full Value Access

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field (Pre-setup #33e): `Serial Notes` (Text, General), `Purchase Price` (Number, Purchasing; `AST-2001` 2500, `AST-2003` 0, `AST-2004` 1800, `AST-2005` 3200), `Accounting Code` (Text, Accounting; `ACC-1` `AST-2001`, `ACC-4` `AST-2004`), lisensi `FA-7` aktif pada client utama.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-788: Aktor berhak atas seluruh baris menampilkan nilai atau strip tanpa No access

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`
3. Verifikasi Setup Column memuat `Asset Value`, `Warranty Expiry`, `Purchase Price`, dan `Accounting Code`
4. Centang Asset Value, Warranty Expiry, `Purchase Price`, `Accounting Code`, klik `[Save]`
5. Verifikasi Asset Value: 15000000, currency nol (mis. `Rp 0,00`), `—`, 5000000, 20000000, `—` berurutan `AST-2001` sampai `AST-2006`
6. Verifikasi Warranty Expiry: 31 Mar 2027, `—`, 15 Jan 2026, 30 Jun 2028, 01 Feb 2025, `—` berurutan `AST-2001` sampai `AST-2006`
7. Verifikasi Purchase Price: 2500, `—`, `0`, 1800, 3200, `—` berurutan `AST-2001` sampai `AST-2006`
8. Verifikasi Accounting Code: `ACC-1`, `—`, `—`, `ACC-4`, `—`, `—` berurutan `AST-2001` sampai `AST-2006`
9. Verifikasi tidak ada sel `No access` pada keempat kolom
10. Verifikasi sel kolom Name, Asset ID, Brand, Group, Status tetap tampil normal pada keenam baris
11. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Asset Value, Warranty Expiry, `Purchase Price`, `Accounting Code`, klik `[Save]`

### TC-FA-FAAM-796: Pindah tab memulihkan state Tab Total Assets termasuk kolom curated dan filter pada kolom baru

12. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value dan `Serial Notes`, klik `[Save]`
13. Ketik Search `Column Matrix`, tekan Enter
14. Klik Filter, isi Asset Value Min `1000000`, klik `[Apply]`
15. Klik header Asset Value 1 kali
16. Klik tab Models per Brand, lalu klik kembali tab Total Assets
17. Verifikasi Search tetap berisi `Column Matrix`
18. Verifikasi Filter Asset Value Min 1000000 tetap ter-Apply
19. Verifikasi Sort Asset Value ascending tetap aktif dan baris berurutan `AST-2004`, `AST-2001`, `AST-2005`
20. Verifikasi kolom Asset Value dan `Serial Notes` tetap tampil
21. Klik `(←)` pada kotak Search, klik Filter, klik `[Clear Field]`, klik `[Apply]`
22. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-808: Kolom Asset ID tidak Filterable; pencarian lewat Search

23. Login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`)
24. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
25. Klik Filter, amati daftar field
26. Verifikasi Filter Panel memuat field lain (mis. `Brand`) dan tidak memuat field `Asset ID`
27. Tutup Filter Panel, ketik Search `AST-2005`, tekan Enter
28. Verifikasi Search `AST-2005` hanya menampilkan baris dengan Asset ID `AST-2005`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 788 dan 796 (Full Value Access, Pre-setup #32e), lalu ganti akun ke Total Control untuk 808 (ACC TC-FA-FAAM-808 menyebut Role Total Control; S-07: Logout dan Login ulang adalah langkah ganti akun eksplisit).
- Langkah penghubung: mencentang kolom, `(←)` pada Search, `[Clear Field]` dan `[Apply]` untuk membersihkan filter, serta menutup popup Detail dan Logout.
- Konfigurasi kolom empat kolom dikembalikan ke default di akhir blok TC-FA-FAAM-788 (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-808: precondition memuat Pre-setup #33g tetapi tidak ada langkah yang memakai field di dalamnya; spec tidak menambah asersi.
  - TC-FA-FAAM-796 sebagai TC retensi state tab: tab Models per Brand tidak punya `Verifikasi` tersendiri karena Expected hanya menyebut state Tab Total Assets setelah kembali.
