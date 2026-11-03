---
id: TC-FA-LBL-E2E-093-search-drawer-tagged-asset-bagian-2-2
title: "Search Drawer Tagged Asset (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-344
  - TC-FA-LBL-345
  - TC-FA-LBL-493
coverage:
  web: automated
---

# Search Drawer Tagged Asset (bagian 2/2)

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
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Label` ditampilkan pada langkah 9 dan dipulihkan pada langkah 13); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.
- Search pada spec ini adalah Search toolbar Drawer Tagged Asset (menyaring saat Enter, bagian 8b butir 9).

## Test Steps

### TC-FA-LBL-344: Guard: kolom Last Updated tidak ikut dicari di Drawer

1. Klik chip `Finance Department` di kolom Label
2. Verifikasi sedikitnya satu baris tampil di Drawer (pembanding asersi hasil Search)
3. Ketik Search `14 Sep 2026`, tekan Enter
4. Verifikasi empty state `No results found` tampil
5. Klik `(←)` pada kotak Search

### TC-FA-LBL-345: Search Drawer tidak mencari kolom Category dan Label yang tersembunyi, dan mencarinya setelah ditampilkan

6. Ketik Search `Audit Ready`, tekan Enter
7. Verifikasi sebelum kolom Label ditampilkan: empty state `No results found` tampil
8. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
9. Tampilkan kolom `Label`: centang `Label`, lalu klik `[Save]`
10. Ganti isi kotak search dengan `Audit Ready`, tekan Enter (mengulang Search)
11. Verifikasi setelah kolom Label ditampilkan: hanya `Printer HP - 3` tampil (memiliki label `Audit Ready`)
12. Klik `(←)` pada kotak Search
13. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-LBL-493: Search toolbar Drawer: reveal, auto-focus, placeholder, tooltip, clear, submit lewat Enter, dan collapse

14. Hover icon Search di toolbar Drawer
15. Verifikasi tooltip `Search`
16. Klik icon Search di toolbar Drawer
17. Verifikasi search bar melebar
18. Verifikasi kursor fokus di input
19. Verifikasi placeholder `Search name, asset ID, brand...`
20. Ketik `Dell` di kotak Search tanpa menekan Enter
21. Verifikasi ikon `(✕)` muncul di dalam input
22. Verifikasi tabel belum tersaring (kelima aset masih tampil)
23. Tekan Enter
24. Verifikasi hanya `Laptop Dell - 1` dan `Laptop Dell - 2` tampil
25. Klik ikon `(✕)` di dalam input
26. Verifikasi input kosong
27. Verifikasi search bar tetap terbuka
28. Verifikasi tabel masih menampilkan hasil `Dell`
29. Tekan Enter pada input yang kosong
30. Verifikasi kelima aset tampil kembali
31. Klik ikon panah `(←)`
32. Verifikasi search bar menutup menjadi ikon Search
33. Verifikasi keyword kosong

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh TC memakai satu pembukaan Drawer `Finance Department` (TC tanpa perubahan state data); TC-FA-LBL-344 dan TC-FA-LBL-345 diakhiri `(←)` pada kotak Search agar tabel kembali ke lima baris (S-09).
- Asersi tambahan (S-03): `Verifikasi` sedikitnya satu baris tampil di Drawer sebelum Search pertama menjadi pembanding asersi universal 'hanya ...' (bagian 8b butir 2); tidak ada di TC sumber. Langkah 13 mengembalikan konfigurasi kolom ke default sebelum TC-FA-LBL-493.
- Spec ini berisi 33 langkah. TC-FA-LBL-493 memuat enam butir Expected yang masing-masing ditulis per klausa (S-01) sehingga langkah `Verifikasi` banyak, tanpa iterasi.
- Pembagian TC lintas spec: TC-FA-LBL-338 sampai TC-FA-LBL-343 ada di spec 092; TC-FA-LBL-575 ada di spec 095.
- Temuan untuk QA:
  - TC-FA-LBL-345 menulis 'Ulangi Search `Audit Ready`' tanpa menyatakan apakah kotak Search masih berisi `Audit Ready` setelah `[Save]` Setup Column; spec mengganti isi kotak dengan `Audit Ready` lalu menekan Enter.
  - TC-FA-LBL-345 tidak menyebut pemulihan kolom `Label`; spec memulihkannya pada langkah 13 supaya TC-FA-LBL-493 mulai dari konfigurasi default.
