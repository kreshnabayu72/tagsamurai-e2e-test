---
id: TC-FA-LBL-E2E-067-isi-berkas-unduhan-csv-xlsx-labels-list-drawer-dan-changelog
title: "Isi berkas unduhan CSV dan XLSX Labels List, Drawer Tagged Asset, dan Changelog (nilai sel, BOM, sheet)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:global-table-rules/download
  - FALB:obl/T-ALB-01/download
  - FALB:obl/T-ALB-02/download
  - FALB:obl/T-ALB-03/download
coverage:
  web: automated
---

# Isi berkas unduhan CSV dan XLSX Labels List, Drawer Tagged Asset, dan Changelog (nilai sel, BOM, sheet)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Pelaku kedua seeding lewat sesi API: `DU-31`, env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`. Tidak ada ganti akun.
- Data uji, dibuat lewat sesi API di hook `before` dan dihapus di hook `after` (aset lalu label):
  - `DU-56` (Dataset Labels List: 12 label bersuffix), pola `Lst-{runId}-067-nn`, Total Asset 0 sampai 3, Modified By dari `DU-01` dan `DU-31`; M = jumlah label yang dimodifikasi `DU-31`, dicatat dari seeding.
  - `DU-59` (Dataset Drawer Tagged Asset), label `Tagged-{runId}-067` dengan 12 aset Active bersuffix (lebih dari satu halaman), minimal dua Group bertingkat, sebagian aset ber-TAG (RFID, QR, NFC, lebih dari satu tipe) dan sebagian tanpa tag.
  - `DU-62` (Dataset Changelog: Labels), label `Log-{runId}-067-nn` dengan 12 entri Create, Edit Label Name, Edit Color, dan Delete oleh `DU-01` dan `DU-31`.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding; kemampuan membaca berkas unduhan (encoding, BOM, pemisah, nama sheet, tipe sel, dan nilai sel CSV dan XLSX); disediakan tim FE/BE. Format tanggal mengikuti Global Settings > General Settings akun `DU-01`.
- State global: konfigurasi kolom Setup Column Labels List diubah dan dipulihkan lewat langkah eksplisit (langkah 23); hook `after` menghapus preferensi kolom akun `DU-01` sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:global-table-rules/download: Download Labels List: format CSV dan XLSX, filename, mengikuti Search dan Filter, dan Modified By nama lengkap

1. Ketik Search `DU-56`, tekan Enter
2. Verifikasi dua belas baris label milik `DU-56` tampil pada Labels List
3. Buka Filter Panel, pilih nama lengkap akun `DU-31` pada dropdown Modified By, klik `[Apply]`
4. Verifikasi hanya baris label milik `DU-56` yang dimodifikasi `DU-31` tampil sebanyak M baris
5. Klik Download pada toolbar tabel, pilih `Download as CSV`
6. Baca berkas CSV yang terunduh
7. Verifikasi nama berkas `Labels.csv`
8. Verifikasi berkas CSV berenkoding UTF-8 dengan BOM dan berpemisah koma
9. Verifikasi berkas memuat M baris data, hanya label hasil Search dan Filter
10. Verifikasi sel Modified By berisi nama lengkap akun `DU-31`, bukan format `[First Name] [Last Initial]`
11. Klik Download pada toolbar tabel, pilih `Download as XLSX`
12. Baca berkas XLSX yang terunduh
13. Verifikasi nama berkas `Labels.xlsx`
14. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1` dengan M baris data dan sel Modified By berisi nama lengkap akun `DU-31`

### FALB:obl/T-ALB-01/download: Download Labels List mengikuti kolom tampil dan nilai sel

15. Sembunyikan kolom Last Updated lewat Setup Column Labels List dan klik `[Save]`
16. Klik Download pada toolbar tabel, pilih `Download as CSV`
17. Baca berkas CSV yang terunduh
18. Verifikasi baris header berkas memuat Label, Color Hex, Total Asset, dan Modified By tanpa Last Updated
19. Verifikasi sel Total Asset berisi angka asli tanpa format tampilan dan sel Color Hex berformat `#RRGGBB` kapital
20. Klik Download pada toolbar tabel, pilih `Download as XLSX`
21. Baca berkas XLSX yang terunduh
22. Verifikasi header sheet `Sheet1` tanpa Last Updated dan sel Total Asset bertipe angka (number)
23. Tampilkan kembali kolom Last Updated lewat Setup Column Labels List dan klik `[Save]`
24. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/download: Download Tagged Asset List: seluruh baris, nilai sel, nama berkas

25. Ganti isi kotak search dengan `DU-59`, tekan Enter
26. Klik chip badge label milik `DU-59` pada Labels List
27. Verifikasi Drawer Tagged Asset tampil dengan baris aset milik `DU-59`
28. Klik Download pada toolbar Drawer Tagged Asset, pilih `Download as CSV`
29. Baca berkas CSV yang terunduh
30. Verifikasi nama berkas `Tagged-Assets-` diikuti nama label `DU-59` dengan ekstensi `.csv`
31. Verifikasi berkas memuat 12 baris data, bukan hanya 10 baris halaman pertama
32. Verifikasi baris header berkas memuat Name, Asset ID, TAG, Brand, Model/Type, Group, Status, dan Last Updated
33. Verifikasi sel TAG berisi label tipe tag aktif dipisah `, ` (mis. `RFID, QR`) dan `-` untuk aset tanpa tag aktif
34. Verifikasi sel Group berisi hierarki penuh `[Parent] > [Child]` dan sel Status berisi teks label badge tanpa warna
35. Klik Download pada toolbar Drawer Tagged Asset, pilih `Download as XLSX`
36. Baca berkas XLSX yang terunduh
37. Verifikasi nama berkas `Tagged-Assets-` diikuti nama label `DU-59` dengan ekstensi `.xlsx`, satu sheet `Sheet1`, dan 12 baris data
38. Klik `[✕]` pada header Drawer Tagged Asset

### FALB:obl/T-ALB-03/download: Download Changelog: nilai sel, nama berkas, dan sheet

39. Klik ikon Changelog pada toolbar tabel
40. Ketik Search `DU-62`, tekan Enter
41. Klik Download pada toolbar Modal Changelog, pilih `Download as CSV`
42. Baca berkas CSV yang terunduh
43. Verifikasi nama berkas `Changelog-Labels.csv`
44. Verifikasi baris header berkas memuat Date, Action, Label Name, Field, Old Value, New Value, dan Modified By dengan 12 baris data
45. Verifikasi sel Modified By berisi nama lengkap akun `DU-01` atau `DU-31`, bukan format `[First Name] [Last Initial]`
46. Verifikasi sel Old Value baris Create dan sel New Value baris Delete berisi `-` (tanda hubung tunggal), bukan `—` dan bukan kosong
47. Verifikasi sel Date mengikuti Date Format dan Time Format General Settings akun `DU-01`
48. Klik Download pada toolbar Modal Changelog, pilih `Download as XLSX`
49. Baca berkas XLSX yang terunduh
50. Verifikasi nama berkas `Changelog-Labels.xlsx`, satu sheet `Sheet1`, header tujuh kolom, dan 12 baris data
51. Klik `[✕]` pada header Modal Changelog

## Notes

- Langkah penghubung (S-03): langkah 1, 25, dan 40 mempersempit tabel ke data milik spec (R-16); langkah 6, 12, 17, 21, 29, 36, 42, dan 49 membaca berkas lewat kemampuan baca berkas; langkah 15 dan 23 menyembunyikan dan menampilkan kembali kolom Last Updated (pemulihan eksplisit, bagian 8b butir 14); langkah 24 mengosongkan Filter; langkah 26, 38, 39, dan 51 membuka dan menutup Drawer dan Modal.
- Anchor positif: langkah 2 dan 4 membuktikan Labels List termuat dan terfilter sebelum asersi berkas; langkah 27 membuktikan Drawer termuat sebelum unduh.
- Ruang lingkup (kelas f, bagian 3 prinsip 13): spec ini hanya mengasersi isi berkas (nilai sel, BOM, pemisah, nama sheet, tipe sel). Nama berkas, header, dan jumlah baris di Modal Changelog juga diasersi sebagai klausa fungsional di spec 054; UI unduh Labels List dan Drawer Tagged Asset diasersi di spec 035 dan 050.
- Pembagian klausa lintas spec: `FALB:global-table-rules/download` dikutip spec 035 dan spec ini; `FALB:obl/T-ALB-01/download` dikutip spec 035 dan spec ini; `FALB:obl/T-ALB-02/download` dikutip spec 050 dan spec ini; `FALB:obl/T-ALB-03/download` dikutip spec 054 dan spec ini.
- Pengaruh kolom tersembunyi atas Drawer dan Changelog serta Filter atas Drawer dan Changelog tidak diasersi di spec ini; keduanya memakai aturan §9.9 yang sama dengan Labels List yang diasersi di langkah 3, 15 sampai 22.
- Alasan spec melewati 35 langkah: seluruh blok satu kelas harness (binary buffer, kelas f) dengan tiga surface yang berdiri sendiri (Labels List, Drawer Tagged Asset, Changelog) dan data seed `DU-56`, `DU-59`, dan `DU-62` yang disiapkan hook; kegagalan satu surface tidak membuat surface lain kehilangan makna. Perubahan state hanya kolom Last Updated dan Filter yang dipulihkan di langkah 23 dan 24.
