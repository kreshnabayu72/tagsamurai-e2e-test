---
id: TC-FA-LBL-E2E-182-isi-berkas-unduh-drawer-tagged-asset-csv-xlsx-nama-berkas-kolom-dan-ikut-search-filter
title: "Isi Berkas Unduh Drawer Tagged Asset: CSV dan XLSX, Nama Berkas, Kolom Visible, serta Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-594
  - TC-FA-LBL-595
coverage:
  web: automated
---

# Isi Berkas Unduh Drawer Tagged Asset: CSV dan XLSX, Nama Berkas, Kolom Visible, serta Search dan Filter

## Prerequisites

- Mode: FE+BE. Backend nyata; berkas diunduh dan dibaca.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 dan #13 (Company Alpha; hanya dibaca, tidak diubah). Label `Finance Department` (Total Asset 5) memiliki lima aset aktif berikut; `Scanner Zebra - 6` (Deleted) terpasang label yang sama dan tidak dihitung:

  | Aset | Status |
  |---|---|
  | `Laptop Dell - 1` | `Available` |
  | `Laptop Dell - 2` | `Borrowed` |
  | `Printer HP - 3` | `Draft` |
  | `Monitor LG - 4` | `Waiting for Approval` |
  | `Projector Epson - 5` | `Disposed` |

- Kolom tabel Drawer yang tampil pada keadaan awal (delapan kolom Hideable Setup Column Drawer): `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`.
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Brand` disembunyikan pada langkah 16 dan dipulihkan pada langkah 31 sampai 32); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).
- Kemampuan teknis (disediakan tim FE): direktori unduhan uji untuk menangkap berkas; pembaca CSV dan XLSX (nama berkas, header, dan baris).

## Test Steps

### TC-FA-LBL-594: Download Drawer menghasilkan file CSV dan XLSX berisi aset berlabel

1. Klik chip `Finance Department` di kolom Label
2. Klik icon Download di toolbar Drawer
3. Klik `Download as CSV`
4. Verifikasi berkas CSV terunduh dengan nama `Tagged-Assets-Finance Department.csv`
5. Verifikasi berkas CSV memuat kelima aset berlabel `Finance Department`: `Laptop Dell - 1`, `Laptop Dell - 2`, `Printer HP - 3`, `Monitor LG - 4`, `Projector Epson - 5`
6. Verifikasi berkas CSV memuat 5 baris data, sama dengan Total Asset `5`
7. Verifikasi header berkas CSV memuat kolom yang visible di tabel Drawer: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
8. Klik icon Download di toolbar Drawer
9. Klik `Download as XLSX`
10. Verifikasi berkas XLSX terunduh dengan nama `Tagged-Assets-Finance Department.xlsx`
11. Verifikasi berkas XLSX memuat kelima aset berlabel `Finance Department`: `Laptop Dell - 1`, `Laptop Dell - 2`, `Printer HP - 3`, `Monitor LG - 4`, `Projector Epson - 5`
12. Verifikasi berkas XLSX memuat 5 baris data, sama dengan Total Asset `5`
13. Verifikasi header berkas XLSX memuat kolom yang visible di tabel Drawer: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`

### TC-FA-LBL-595: Isi file Download Drawer mengikuti Search, Filter, dan kolom visible

14. Ketik Search `Laptop Dell - 1` di toolbar Drawer, tekan Enter
15. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
16. Hapus centang `Brand`, lalu klik `[Save]`
17. Klik icon Download di toolbar Drawer
18. Klik `Download as CSV`
19. Verifikasi berkas CSV memuat baris aset `Laptop Dell - 1`
20. Verifikasi berkas CSV tidak memuat baris aset `Laptop Dell - 2`, `Printer HP - 3`, `Monitor LG - 4`, dan `Projector Epson - 5`
21. Verifikasi header berkas CSV memuat tujuh kolom lain: `Name`, `Asset ID`, `TAG`, `Model/Type`, `Group`, `Status`, `Last Updated`
22. Verifikasi header berkas CSV tidak memuat kolom `Brand`
23. Klik `(←)` pada kotak Search Drawer
24. Klik icon Filter di toolbar Drawer
25. Pilih `Status` = `Draft`, lalu klik `[Apply]`
26. Klik icon Download di toolbar Drawer
27. Klik `Download as CSV`
28. Verifikasi berkas CSV memuat baris aset `Printer HP - 3`
29. Verifikasi berkas CSV tidak memuat baris aset berstatus lain: `Laptop Dell - 1`, `Laptop Dell - 2`, `Monitor LG - 4`, dan `Projector Epson - 5`
30. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup panel Filter dengan klik icon Filter di toolbar Drawer
31. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
32. Centang `Brand`, lalu klik `[Save]`
33. Tutup Drawer dengan `[✕]`

## Notes

- Mode: FE+BE (backend nyata; berkas diunduh dan dibaca). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Kelas harness binary buffer (bagian 3 prinsip 13f): spec ini hanya memuat asersi isi berkas hasil unduh Drawer; kegagalan ekspor tidak termasuk.
- Urutan `Verifikasi` pada TC-FA-LBL-594 mengikuti berkas: Expected a, c untuk berkas CSV (langkah 4 sampai 7) lalu Expected b, c untuk berkas XLSX (langkah 10 sampai 13), supaya tiap berkas dibaca tepat setelah diunduh (urutan state, bagian 8b butir 5).
- Langkah penghubung (S-03): langkah 30 mengosongkan Filter dan menutup panel Filter (panel tetap terbuka sesudah `[Apply]`, bagian 8b butir 9, S-09); langkah 31 sampai 32 memulihkan kolom `Brand` (Pemulihan Setup Column, bagian 8b butir 14); langkah 33 menutup Drawer.
- Langkah 23 menyalin langkah TC "Klik `[Clear Field]` pada Search" sebagai `(←)` pada kotak Search, cara mengosongkan Search yang menutup input dan mereset tabel (bagian 8b butir 9).
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` header berkas CSV memuat tujuh kolom lain (langkah 21) dan berkas memuat baris `Laptop Dell - 1` serta `Printer HP - 3` (langkah 19 dan 28) berfungsi sebagai anchor positif sebelum asersi absence kolom dan baris (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-LBL-594 menyebut "kolom Tabel 2 yang sedang visible" tanpa daftar kolom; spec memakai delapan kolom Hideable Drawer pada keadaan awal (Prerequisites).
  - TC-FA-LBL-594 menyebut "jumlah baris sama dengan Total Asset" tanpa menyebut apakah header dihitung; spec menghitung baris data tanpa header.
  - TC-FA-LBL-595 tidak menyebut aset untuk Search, kolom yang dicentang, dan Status untuk Filter; spec memilih `Laptop Dell - 1`, `Brand`, dan `Draft` dari data Pre-setup #12 dan #13.
  - TC-FA-LBL-595 Expected b hanya menyebut isi file langkah 6; kolom `Brand` tetap disembunyikan saat unduhan itu tetapi tidak diasersi.
