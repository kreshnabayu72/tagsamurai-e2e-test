---
id: TC-FA-LBL-E2E-071-setup-column-labels-list-drag-reorder-dan-pin
title: "Setup Column Labels List: Drag Reorder dan Pin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-258
  - TC-FA-LBL-259
  - TC-FA-LBL-260
coverage:
  web: automated
---

# Setup Column Labels List: Drag Reorder dan Pin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Color Hex | Total Asset | Modified By |
  |---|---|---|---|
  | `High Priority` | `#EF4444` | 3 | `Sarah J` |
  | `Finance Department` | `#3B82F6` | 5 | `David K` |
  | `Audit Ready` | `#10B981` | 2 | `Sarah J` |
  | `Executive Asset` | `#8B5CF6` | 1 | `Michael W` |
  | `Maintenance Due` | `#F59E0B` | 4 | `David K` |
  | `Seasonal Event` | `#EC4899` | 0 | `Michael W` |
  | `Night Shift` | `#1E3A8A` | 0 | `Sarah J` |
  | `Warehouse Priority` | `#0EA5E9` | 0 | `Sarah J` |
  | `Field Kit` | `#84CC16` | 2 | `David K` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Labels List (diubah dan dipulihkan oleh langkah spec); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).
- State global lain: lebar viewport dipersempit pada langkah 15 dan dipulihkan pada langkah 30; hook `after` suite memulihkan viewport sebagai cadangan.
- Kemampuan teknis: mempersempit lebar viewport sampai tabel Labels List dapat di-scroll horizontal dan mengamati kolom membeku (sticky) saat scroll; lebar dan mekanisme observasi ditetapkan tim FE saat script.
- Data uji drag (TC-FA-LBL-258, lima seretan berurutan; tiap baris menyeret kolom ke posisi paling atas):

  | Kolom yang diseret | Urutan Live Preview sesudahnya |
  |---|---|
  | `Color Hex` | `Color Hex`, `Label`, `Total Asset`, `Modified By`, `Last Updated` |
  | `Total Asset` | `Total Asset`, `Color Hex`, `Label`, `Modified By`, `Last Updated` |
  | `Modified By` | `Modified By`, `Total Asset`, `Color Hex`, `Label`, `Last Updated` |
  | `Last Updated` | `Last Updated`, `Modified By`, `Total Asset`, `Color Hex`, `Label` |
  | `Label` | `Label`, `Last Updated`, `Modified By`, `Total Asset`, `Color Hex` |

- Data uji fase pin (TC-FA-LBL-259, fase keempat sampai keenam, sesudah ketiga kolom pertama dibekukan):

  | Aksi pada icon Pin | Kondisi saat scroll horizontal |
  |---|---|
  | lepas pin `Label`, `Color Hex`, dan `Total Asset` satu per satu | ketiga kolom itu ikut bergeser |
  | pasang pin `Modified By` lalu `Last Updated` | `Modified By` dan `Last Updated` membeku di kiri |
  | lepas pin `Modified By` dan `Last Updated` | tidak ada kolom yang membeku |


## Test Steps

### TC-FA-LBL-258: Setup Column: drag reorder kolom

1. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
2. Untuk setiap baris tabel Data uji drag (langkah 2 sampai 3): seret kolom pada baris itu ke posisi paling atas daftar Setup Column
3. Verifikasi urutan Live Preview sesuai kolom "Urutan Live Preview sesudahnya" pada baris tabel
4. Klik `[Save]`
5. Verifikasi urutan header tabel `Label`, `Last Updated`, `Modified By`, `Total Asset`, `Color Hex`
6. Tekan F5
7. Verifikasi urutan header tabel bertahan setelah F5 (sama dengan urutan sebelum F5)
8. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
9. Klik `[Reset to Default]`
10. Klik `[Save]`

### TC-FA-LBL-259: Setup Column: pin dan unpin kolom

11. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
12. Klik icon Pin `Label`, `Color Hex`, dan `Total Asset` satu per satu
13. Verifikasi icon Pin ketiga kolom itu berstatus aktif
14. Klik `[Save]`
15. Persempit lebar viewport sampai tabel Labels List dapat di-scroll horizontal
16. Scroll tabel horizontal
17. Verifikasi `Label`, `Color Hex`, dan `Total Asset` membeku di kiri saat scroll
18. Tekan F5
19. Scroll tabel horizontal
20. Verifikasi `Label`, `Color Hex`, dan `Total Asset` tetap membeku setelah F5
21. Untuk setiap baris tabel Data uji fase pin (langkah 21 sampai 24): buka Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`) dan klik icon Pin sesuai kolom "Aksi pada icon Pin" pada baris tabel
22. Klik `[Save]`
23. Scroll tabel horizontal
24. Verifikasi kondisi kolom saat scroll sesuai kolom "Kondisi saat scroll horizontal" pada baris tabel

### TC-FA-LBL-260: Pin keempat dinonaktifkan setelah tiga kolom dibekukan

25. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
26. Klik icon Pin `Label`, `Color Hex`, dan `Total Asset` satu per satu
27. Hover icon Pin `Modified By`
28. Verifikasi icon Pin `Modified By` dan `Last Updated` berstatus disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
29. Klik icon `[✕]` pada popup Setup Column (menutup tanpa menyimpan)
30. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Spec ini 30 langkah nominal dan 46 langkah setelah ekspansi (di atas smell 35 langkah; langkah 2 sampai 3 diulang untuk lima baris Data uji drag dan langkah 21 sampai 24 untuk tiga baris Data uji fase pin, bagian 8b butir 7). Alasan: seluruh blok adalah Setup Column drag dan pin pada popup dan dataset Pre-setup #12 yang sama dengan kelas fungsional yang sama; ekspansi berasal dari iterasi prosedur identik per kolom atau fase, dan tiap TC dimulai dari konfigurasi default (langkah 10 memulihkan) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 sampai 10 mengembalikan urutan kolom ke default sebelum TC-FA-LBL-259 (S-09); langkah 15 mempersempit viewport agar tabel dapat di-scroll horizontal; langkah 29 dan 30 menutup popup tanpa menyimpan dan memulihkan viewport.
- Fase keempat sampai keenam TC-FA-LBL-259 ditulis sebagai tiga baris tabel Data uji fase pin dengan prosedur identik (buka popup, atur icon Pin, Save, scroll, amati); tiga butir pertama TC-FA-LBL-259 (pasang pin ketiga kolom pertama, simpan, dan muat ulang) ditulis eksplisit karena memuat asersi tersendiri (status icon Pin dan bertahan setelah F5).
- Temuan untuk QA:
  - TC-FA-LBL-259 dan TC-FA-LBL-260 tidak menyebut lebar viewport "sempit" secara numerik dan cara mengamati kolom membeku saat scroll; lebar dan mekanisme observasi (posisi sticky) ditetapkan tim FE saat script.
