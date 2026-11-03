---
id: TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom
title: "Search Labels List: Modified By, Guard Kolom, Trim, dan Visibilitas Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-213
  - TC-FA-LBL-214
  - TC-FA-LBL-215
  - TC-FA-LBL-216
  - TC-FA-LBL-217
  - TC-FA-LBL-218
  - TC-FA-LBL-219
  - TC-FA-LBL-507
coverage:
  web: automated
---

# Search Labels List: Modified By, Guard Kolom, Trim, dan Visibilitas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
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
- State global yang diubah: konfigurasi kolom Setup Column Labels List (kolom `Color Hex` disembunyikan lalu ditampilkan kembali oleh langkah spec; hook `after` suite menghapus preferensi kolom di browser sebagai cadangan).

## Test Steps

### TC-FA-LBL-213: Search kolom Modified By: pencocokan substring

1. Ketik Search `Sara`, tekan Enter
2. Verifikasi tabel memuat empat baris dengan Modified By `Sarah J`: `Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority`

### TC-FA-LBL-214: Search kolom Modified By: tidak membedakan huruf besar-kecil

3. Ganti isi kotak search dengan `MICHAEL`, tekan Enter
4. Verifikasi tabel memuat dua baris dengan Modified By `Michael W`: `Executive Asset` dan `Seasonal Event`

### TC-FA-LBL-215: Search kolom Modified By: kata kunci tidak ditemukan

5. Ganti isi kotak search dengan `Zulkifli`, tekan Enter
6. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-FA-LBL-507: Search kolom Modified By mencocokkan nama lengkap user, bukan format tampil

7. Ganti isi kotak search dengan `Johnson`, tekan Enter
8. Verifikasi tabel memuat empat baris dengan Modified By `Sarah J`: `Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority` (nama belakang tidak tampil di kolom tetapi tetap dicocokkan)
9. Ganti isi kotak search dengan `sarah johnson`, tekan Enter
10. Verifikasi tabel memuat empat baris dengan Modified By `Sarah J`: `Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority` (huruf besar-kecil tidak dibedakan)

### TC-FA-LBL-216: Guard: kolom Total Asset dan Last Updated tidak ikut dicari

11. Ganti isi kotak search dengan `4`, tekan Enter
12. Verifikasi tabel memuat baris yang Color Hex-nya memuat angka 4: `High Priority`, `Field Kit`, `Seasonal Event`
13. Verifikasi baris `Maintenance Due` (Total Asset 4) tidak muncul
14. Ganti isi kotak search dengan `15 Sep 2026`, tekan Enter
15. Verifikasi empty state `No results found`

### TC-FA-LBL-217: Query Search di-trim saat Enter tanpa mengubah isi input

16. Ganti isi kotak search dengan dua spasi + `High` + dua spasi, tekan Enter
17. Verifikasi tabel hanya memuat `High Priority`
18. Verifikasi isi input tetap menampilkan spasi yang diketik

### TC-FA-LBL-218: Search tidak mencari kolom yang sedang disembunyikan

19. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
20. Hapus centang kolom `Color Hex`
21. Klik `[Save]`
22. Ganti isi kotak search dengan `EF4444`, tekan Enter
23. Verifikasi empty state `No results found` karena kolom Color Hex yang disembunyikan tidak dapat dicari
24. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
25. Centang kolom `Color Hex`
26. Klik `[Save]`
27. Klik `(←)` pada kotak Search

### TC-FA-LBL-219: Search kembali mencari kolom yang ditampilkan lagi

28. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
29. Hapus centang kolom `Color Hex`
30. Klik `[Save]`
31. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
32. Centang kolom `Color Hex`
33. Klik `[Save]`
34. Ketik Search `EF4444`, tekan Enter
35. Verifikasi baris `High Priority` ditemukan (Color Hex `#EF4444`)

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 24 sampai 27 memulihkan kolom `Color Hex` dan mereset Search sebelum TC-FA-LBL-219 membangun state-nya sendiri dari awal (S-04 dan S-09); langkah 27 memakai `(←)` sesuai bagian 8b butir 9.
- Klausa "penyaringan tanggal hanya lewat Filter Panel" pada Expected b TC-FA-LBL-216 adalah penjelasan, bukan keadaan yang teramati pada Search; spec mengasersi empty state di langkah 15. Penyaringan lewat Filter Last Updated diasersi di TC-FA-LBL-230 dan TC-FA-LBL-231.
- Urutan blok TC-FA-LBL-507 sebelum TC-FA-LBL-216 mengelompokkan seluruh Search kolom Modified By; urutan ini tidak mengubah langkah TC.
- Temuan untuk QA:
  - TC-FA-LBL-217 memakai satu spasi di Langkah (` High `) tetapi dua spasi di Data Uji ("dua spasi + `High` + dua spasi"); spec mengikuti Data Uji.
