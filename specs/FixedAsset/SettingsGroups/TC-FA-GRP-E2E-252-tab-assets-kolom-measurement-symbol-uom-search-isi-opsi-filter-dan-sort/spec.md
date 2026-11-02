---
id: TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort
title: "Tab Assets Kolom Measurement: Tersembunyi Default Menampilkan Symbol UoM, Search, Isi Opsi Filter, dan Filter Satu/Dua Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1197
  - TC-FA-GRP-1198
  - TC-FA-GRP-1199
  - TC-FA-GRP-1200
coverage:
  web: automated
---

# Tab Assets Kolom Measurement: Tersembunyi Default Menampilkan Symbol UoM, Search, Isi Opsi Filter, dan Filter Satu/Dua Opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Master Measurement (Tabel Dinamis No 14): Piece `pcs`, Unit `unit`, Meter `m`; Asset Name ke UoM: Laptop Dell (G1, G6), Printer HP (G2), dan Monitor LG (G3) = Piece `pcs`; Forklift Toyota (G4) = Unit `unit`; Kabel Roll (G5) = Meter `m`. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1197: Kolom curated Measurement tersembunyi default, menampilkan Symbol UoM saja

1. Buka Detail Value Gate Node A (Tab Assets)
2. Amati header kolom (default)
3. Verifikasi header tabel memuat kolom `Name`
4. Verifikasi kolom Measurement tidak tampil pada kondisi default
5. Buka Popup Setup Column
6. Verifikasi kolom Measurement berstatus curated (unchecked, enabled)
7. Centang Measurement
8. Klik [Save]
9. Amati kolom Measurement
10. Verifikasi G1, G2, G3, dan G6 = `pcs`, G4 = `unit`, G5 = `m`
11. Verifikasi Unit Name (`Piece`, `Meter`) tidak ditampilkan
12. Verifikasi sel Measurement tidak pernah kosong

### TC-FA-GRP-1198: Search by kolom Measurement, substring Symbol, case-insensitive

13. Ketik Search `pcs`, tekan Enter
14. Verifikasi G1, G2, G3, dan G6 tampil
15. Verifikasi G4 dan G5 tidak tampil
16. Ganti isi kotak search dengan `PCS`, tekan Enter
17. Verifikasi hasil identik dengan `pcs`: G1, G2, G3, dan G6 tampil
18. Ganti isi kotak search dengan `unit`, tekan Enter
19. Verifikasi G4 tampil
20. Verifikasi baris lain (G1, G2, G3, G5, G6) tidak tampil
21. Ganti isi kotak search dengan `kg`, tekan Enter
22. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
23. Klik `(←)` pada kotak Search

### TC-FA-GRP-1199: Isi opsi dropdown Filter Measurement (populate dari data tabel)

24. Klik icon Filter
25. Buka dropdown field Measurement
26. Verifikasi field Measurement berupa dropdown multi-select searchable dengan placeholder `All units`
27. Verifikasi opsi = Symbol distinct yang ada di baris tabel (`m`, `pcs`, `unit`)
28. Verifikasi Unit Name (`Piece`, `Meter`) bukan opsi
29. Verifikasi kotak search internal tampil
30. Centang opsi `m` dan `unit`
31. Verifikasi opsi `m` dan `unit` tercentang bersamaan (dapat dicentang lebih dari satu)
32. Uncheck opsi `m` dan `unit`, tutup dropdown

### TC-FA-GRP-1200: Filter by Measurement, satu opsi dan dua opsi (OR)

33. Buka dropdown field Measurement, centang opsi `pcs`, tutup dropdown
34. Klik [Apply]
35. Verifikasi G1, G2, G3, dan G6 tampil
36. Verifikasi G4 dan G5 tidak tampil
37. Verifikasi indikator filter aktif tampil pada icon Filter
38. Klik icon Filter
39. Klik [Clear Field]
40. Buka dropdown field Measurement, centang opsi `m` dan `unit`, tutup dropdown
41. Klik [Apply]
42. Verifikasi G4 dan G5 tampil (OR di dalam field)
43. Verifikasi baris lain (G1, G2, G3, G6) tidak tampil
44. Buka Popup Setup Column
45. Uncheck Measurement
46. Klik [Save]
47. Verifikasi kolom Measurement tidak tampil di tabel
48. Verifikasi filter tetap berlaku: G4 dan G5 tampil
49. Verifikasi baris lain (G1, G2, G3, G6) tetap tidak tampil

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): Klik `(←)` pada kotak Search sebelum Filter; membuka Filter Panel dengan klik icon Filter; centang lalu uncheck dua opsi; [Clear Field] sebelum filter dua opsi; langkah hide Measurement (Uncheck, [Save]) untuk butir c TC-1200 yang tidak punya langkah di TC. Kolom Measurement dicentang sekali di blok TC-1197 dan tetap tercentang untuk TC-1198 sampai TC-1200.
- Spec ini 49 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom Measurement), satu dataset (Value Gate Node A), empat blok TC yang berdiri sendiri dengan state pembersih di antaranya; langkah dominan berupa Verifikasi per klausa.
- Temuan untuk QA (S-15): (1) Expected TC-1200 butir c "Filter tetap berlaku walau kolom Measurement di-hide" tidak punya langkah hide di TC; spec menambah Uncheck Measurement dan [Save]. (2) TC-1198 langkah 3 dan TC-1197 langkah 4 sama-sama mencentang Measurement; spec mencentang sekali di TC-1197 karena state kolom tersimpan. (3) TC tidak menyatakan apakah Filter Panel tertutup sesudah [Apply].
