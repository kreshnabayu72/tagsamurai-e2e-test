---
id: TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state
title: "Search Labels List: Toolbar, Kelas Label dan Color Hex, serta Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-208
  - TC-FA-LBL-209
  - TC-FA-LBL-210
  - TC-FA-LBL-211
  - TC-FA-LBL-212
coverage:
  web: automated
---

# Search Labels List: Toolbar, Kelas Label dan Color Hex, serta Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah):

  | Label | Color Hex |
  |---|---|
  | `High Priority` | `#EF4444` |
  | `Finance Department` | `#3B82F6` |
  | `Audit Ready` | `#10B981` |
  | `Executive Asset` | `#8B5CF6` |
  | `Maintenance Due` | `#F59E0B` |
  | `Seasonal Event` | `#EC4899` |
  | `Night Shift` | `#1E3A8A` |
  | `Warehouse Priority` | `#0EA5E9` |
  | `Field Kit` | `#84CC16` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-208: Search toolbar: reveal, auto-focus, placeholder, tooltip, clear, dan submit lewat Enter

1. Hover icon Search di Table Tools sebelum diklik
2. Verifikasi tooltip icon `Search` tampil
3. Tekan F5, lalu hover icon Search di Table Tools (ulangi sesudah muat ulang)
4. Verifikasi tooltip icon `Search` tampil
5. Klik icon Search di Table Tools
6. Verifikasi Search bar melebar
7. Verifikasi kursor otomatis fokus di input
8. Verifikasi placeholder `Search label name, color hex...`
9. Ketik `Fin` di input Search tanpa menekan Enter
10. Verifikasi ikon `(✕)` muncul di dalam input
11. Verifikasi tabel belum tersaring (seluruh 9 label masih tampil; search bukan live-as-you-type)
12. Tekan Enter
13. Verifikasi tabel hanya memuat `Finance Department`
14. Klik ikon `(✕)` di dalam input
15. Verifikasi input kosong
16. Verifikasi search bar tetap terbuka
17. Verifikasi kursor fokus di input
18. Verifikasi tabel masih menampilkan hasil `Finance Department`
19. Tekan Enter pada input yang kosong
20. Verifikasi tabel kembali menampilkan 9 label
21. Klik ikon panah `(←)`
22. Verifikasi search bar menutup menjadi ikon Search
23. Verifikasi keyword kosong

### TC-FA-LBL-209: Klik panah (←) saat hasil search aktif langsung mereset tabel

24. Ketik Search `Fin`, tekan Enter
25. Klik ikon panah `(←)`
26. Verifikasi search bar menutup
27. Verifikasi keyword dikosongkan
28. Verifikasi tabel langsung menampilkan 9 label tanpa Enter tambahan

### TC-FA-LBL-210: Search kelas Label dan Color Hex: pencocokan substring

29. Ketik Search `Prior`, tekan Enter
30. Verifikasi tabel hanya memuat baris `High Priority` dan `Warehouse Priority` (kolom Label)
31. Ganti isi kotak search dengan `3B82`, tekan Enter
32. Verifikasi tabel hanya memuat baris `Finance Department` (kolom Color Hex `#3B82F6`)

### TC-FA-LBL-211: Search kelas Label dan Color Hex: tidak membedakan huruf besar-kecil

33. Ganti isi kotak search dengan `HIGH priority`, tekan Enter
34. Verifikasi tabel hanya memuat baris `High Priority`
35. Ganti isi kotak search dengan `ef4444`, tekan Enter
36. Verifikasi tabel hanya memuat baris `High Priority` (Color Hex `#EF4444`)

### TC-FA-LBL-212: Search kelas Label dan Color Hex: kata kunci tidak ditemukan menampilkan empty state

37. Ganti isi kotak search dengan `zzzz`, tekan Enter
38. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
39. Verifikasi tidak ada baris data

## Notes

- Mode: FE+BE (backend nyata; Search disaring server). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Spec ini 39 langkah (di atas smell 35 langkah). Alasan: seluruh blok adalah kasus Search Labels List pada dataset Pre-setup #12 yang sama dan satu kelas fungsional; tiap blok berdiri sendiri karena isi kotak search diganti di awal blok dan tidak mengandalkan hasil blok sebelumnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Memecahnya hanya menambah login dan hook tanpa mengubah dataset.
- Pembukaan Search bar di langkah 24 dan 29 memakai penulisan atomik "Ketik Search ..., tekan Enter" (bagian 8b butir 9); langkah 1 sampai 23 menulis siklus input eksplisit karena TC-FA-LBL-208 menguji siklus itu.
- Langkah 3 mengulang hover sesudah F5 sesuai langkah 2 TC-FA-LBL-208; Expected tooltip yang sama diasersi lagi di langkah 4.
- Temuan untuk QA:
  - TC-FA-LBL-208 langkah 2 "ulangi setelah reload" tidak punya Expected terpisah; spec mengasersi tooltip `Search` yang sama sesudah muat ulang.
