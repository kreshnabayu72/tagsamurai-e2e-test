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

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Amati header kolom (default)
4. Verifikasi header tabel memuat kolom `Name`
5. Verifikasi kolom Measurement tidak tampil pada kondisi default
6. Buka Popup Setup Column
7. Verifikasi kolom Measurement berstatus curated (unchecked, enabled)
8. Centang Measurement
9. Klik [Save]
10. Amati kolom Measurement
11. Verifikasi G1, G2, G3, dan G6 = `pcs`, G4 = `unit`, G5 = `m`
12. Verifikasi Unit Name (`Piece`, `Meter`) tidak ditampilkan
13. Verifikasi sel Measurement tidak pernah kosong

### TC-FA-GRP-1198: Search by kolom Measurement, substring Symbol, case-insensitive

14. Ketik Search `pcs`, tekan Enter
15. Verifikasi G1, G2, G3, dan G6 tampil
16. Verifikasi G4 dan G5 tidak tampil
17. Ganti isi kotak search dengan `PCS`, tekan Enter
18. Verifikasi hasil identik dengan `pcs`: G1, G2, G3, dan G6 tampil
19. Ganti isi kotak search dengan `unit`, tekan Enter
20. Verifikasi G4 tampil
21. Verifikasi baris lain (G1, G2, G3, G5, G6) tidak tampil
22. Ganti isi kotak search dengan `kg`, tekan Enter
23. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
24. Klik `(←)` pada kotak Search

### TC-FA-GRP-1199: Isi opsi dropdown Filter Measurement (populate dari data tabel)

25. Klik icon Filter
26. Buka dropdown field Measurement
27. Verifikasi field Measurement berupa dropdown multi-select searchable dengan placeholder `All units`
28. Verifikasi opsi = Symbol distinct yang ada di baris tabel (`m`, `pcs`, `unit`)
29. Verifikasi Unit Name (`Piece`, `Meter`) bukan opsi
30. Verifikasi kotak search internal tampil
31. Centang opsi `m` dan `unit`
32. Verifikasi opsi `m` dan `unit` tercentang bersamaan (dapat dicentang lebih dari satu)
33. Uncheck opsi `m` dan `unit`, tutup dropdown

### TC-FA-GRP-1200: Filter by Measurement, satu opsi dan dua opsi (OR)

34. Buka dropdown field Measurement, centang opsi `pcs`, tutup dropdown
35. Klik [Apply]
36. Verifikasi G1, G2, G3, dan G6 tampil
37. Verifikasi G4 dan G5 tidak tampil
38. Verifikasi indikator filter aktif tampil pada icon Filter
39. Klik icon Filter
40. Klik [Clear Field]
41. Buka dropdown field Measurement, centang opsi `m` dan `unit`, tutup dropdown
42. Klik [Apply]
43. Verifikasi G4 dan G5 tampil (OR di dalam field)
44. Verifikasi baris lain (G1, G2, G3, G6) tidak tampil
45. Buka Popup Setup Column
46. Uncheck Measurement
47. Klik [Save]
48. Verifikasi kolom Measurement tidak tampil di tabel
49. Verifikasi filter tetap berlaku: G4 dan G5 tampil
50. Verifikasi baris lain (G1, G2, G3, G6) tetap tidak tampil

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): Klik `(←)` pada kotak Search sebelum Filter; membuka Filter Panel dengan klik icon Filter; centang lalu uncheck dua opsi; [Clear Field] sebelum filter dua opsi; langkah hide Measurement (Uncheck, [Save]) untuk butir c TC-1200 yang tidak punya langkah di TC. Kolom Measurement dicentang sekali di blok TC-1197 dan tetap tercentang untuk TC-1198 sampai TC-1200.
- Spec ini 50 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom Measurement), satu dataset (Value Gate Node A), empat blok TC yang berdiri sendiri dengan state pembersih di antaranya; langkah dominan berupa Verifikasi per klausa.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA (S-15): (1) Expected TC-1200 butir c "Filter tetap berlaku walau kolom Measurement di-hide" tidak punya langkah hide di TC; spec menambah Uncheck Measurement dan [Save]. (2) TC-1198 langkah 3 dan TC-1197 langkah 4 sama-sama mencentang Measurement; spec mencentang sekali di TC-1197 karena state kolom tersimpan. (3) TC tidak menyatakan apakah Filter Panel tertutup sesudah [Apply].
