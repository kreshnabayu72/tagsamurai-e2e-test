---
id: TC-FA-LBL-E2E-098-sort-drawer-tagged-asset-status-last-updated-label-dan-tie-breaker
title: "Sort Drawer Tagged Asset: Status, Last Updated, Label, dan Tie-Breaker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-358
  - TC-FA-LBL-359
  - TC-FA-LBL-360
  - TC-FA-LBL-361
coverage:
  web: automated
---

# Sort Drawer Tagged Asset: Status, Last Updated, Label, dan Tie-Breaker

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 dan #13 (Company Alpha; hanya dibaca, tidak diubah). Label `Finance Department` (`#3B82F6`, Total Asset 5) memiliki lima aset aktif berikut; `Scanner Zebra - 6` (Deleted) terpasang label yang sama dan tidak dihitung:

  | Aset | Asset ID | Status | Brand | Model/Type | Group | Category | Label lain | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | `Laptop Dell - 1` | `AST-0001` | `Available` | `Dell` | `Latitude 5440` | `Head Office > Floor 1` | `IT Equipment > Laptop` | `High Priority` | 14 Sep 2026 09:00 |
  | `Laptop Dell - 2` | `AST-0002` | `Borrowed` | `Dell` | `Latitude 5440` | `Head Office > Floor 2` | `IT Equipment > Laptop` | - | 13 Sep 2026 09:00 |
  | `Printer HP - 3` | `AST-0003` | `Draft` | `HP` | `LaserJet Pro` | `Head Office` | `Printer` | `Audit Ready`, `Maintenance Due` | 12 Sep 2026 09:00 |
  | `Monitor LG - 4` | `AST-0004` | `Waiting for Approval` | `LG` | `UltraWide 34` | `Head Office` | `Monitor` | - | 11 Sep 2026 09:00 |
  | `Projector Epson - 5` | `AST-0005` | `Disposed` | `Epson` | `EB-X49` | `Warehouse` | `Projector` | - | 10 Sep 2026 09:00 |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Label` ditampilkan pada langkah 15 dan dipulihkan pada langkah 28); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.

## Test Steps

### TC-FA-LBL-358: Sort Drawer kolom Status: alfabetis berdasarkan label status

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom `Status` satu kali
3. Verifikasi Ascending: `Available`, `Borrowed`, `Disposed`, `Draft`, `Waiting for Approval`
4. Klik header kolom `Status` sekali lagi (klik kedua)
5. Verifikasi Descending: `Waiting for Approval`, `Draft`, `Disposed`, `Borrowed`, `Available`
6. Klik header kolom `Status` sekali lagi (klik ketiga)
7. Verifikasi Netral: kembali ke default Name A-Z

### TC-FA-LBL-359: Sort Drawer kolom Last Updated

8. Klik header kolom `Last Updated` satu kali
9. Verifikasi Ascending (Oldest First): `Projector Epson - 5` (10 Sep) sampai `Laptop Dell - 1` (14 Sep)
10. Klik header kolom `Last Updated` sekali lagi (klik kedua)
11. Verifikasi Descending (Newest First): `Laptop Dell - 1` (14 Sep) sampai `Projector Epson - 5` (10 Sep)
12. Klik header kolom `Last Updated` sekali lagi (klik ketiga)
13. Verifikasi Netral: kembali ke default Name A-Z

### TC-FA-LBL-360: Sort Drawer kolom Label (+N more): jumlah label lalu label pertama A-Z

14. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
15. Tampilkan kolom `Label`: centang `Label`, lalu klik `[Save]`
16. Klik header kolom `Label` satu kali
17. Verifikasi Ascending: aset dengan jumlah label terkecil dulu (`Laptop Dell - 2`, `Monitor LG - 4`, `Projector Epson - 5` masing-masing 1 label, urut label pertama A-Z lalu Name), kemudian `Laptop Dell - 1` (2 label), terakhir `Printer HP - 3` (3 label)
18. Verifikasi urutan badge di dalam satu sel tetap A-Z pada arah Ascending
19. Klik header kolom `Label` sekali lagi (klik kedua)
20. Verifikasi Descending: `Printer HP - 3` lebih dulu, lalu `Laptop Dell - 1`, lalu tiga aset 1 label
21. Verifikasi urutan badge di dalam satu sel tetap A-Z pada arah Descending
22. Klik header kolom `Label` sekali lagi (klik ketiga)

### TC-FA-LBL-361: Sort Drawer: nilai sort sama mengikuti default Name lalu identifier

23. Klik header kolom `Brand` satu kali
24. Verifikasi Ascending: pada Brand `Dell` baris `Laptop Dell - 1` mendahului `Laptop Dell - 2`
25. Klik header kolom `Brand` sekali lagi (klik kedua)
26. Verifikasi Descending: pada Brand `Dell` baris `Laptop Dell - 1` mendahului `Laptop Dell - 2` (urutan sama dengan Ascending)
27. Klik header kolom `Brand` sekali lagi (klik ketiga)
28. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik ketiga pada kolom `Label` dan `Brand` mengembalikan sort ke netral sebelum TC berikutnya (S-09); pemulihan konfigurasi kolom di langkah 28. `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Asersi urutan badge dalam satu sel (TC-FA-LBL-360 butir c) diasersi pada kedua arah, satu `Verifikasi` per arah, karena butir itu menyebut 'kedua arah'.
- Pembagian TC lintas spec: TC-FA-LBL-355 ada di spec 103; TC-FA-LBL-356 dan TC-FA-LBL-357 ada di spec 097.
- Temuan untuk QA:
  - TC-FA-LBL-361 tidak menyebut kolom `Brand` sebagai klik ketiga yang mengembalikan netral; spec menutup siklus dengan klik ketiga sebagai langkah penghubung.
