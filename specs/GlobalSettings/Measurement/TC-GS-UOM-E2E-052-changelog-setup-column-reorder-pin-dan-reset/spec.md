---
id: TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset
title: "Changelog Measurement: Setup Column Reorder (Modal dan Panel), Pin Maksimal 3, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-308
  - TC-GS-UOM-309
  - TC-GS-UOM-310
  - TC-GS-UOM-350
coverage:
  web: automated
---

# Changelog Measurement: Setup Column Reorder (Modal dan Panel), Pin Maksimal 3, dan Reset to Default

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip halaman Measurement: disetel true (flag `seen`) oleh kemampuan yang disediakan tim FE untuk integration test; rujukan pernyataan hook suite di `suite.md` (bagian "Hook suite").
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Kebutuhan mock (endpoint dan respons yang dipaksa):
  - Daftar Changelog Measurement mengembalikan sedikitnya satu entri dengan nilai Old Value/New Value cukup panjang sehingga ketujuh kolom melebihi lebar viewport yang diperkecil (TC-GS-UOM-309 hanya bermakna bila scroll horizontal teramati).
  - Daftar Measurement (tabel utama) mengembalikan sedikitnya tiga unit supaya layar Measurement termuat.
  - API pendukung di luar modul (identitas pengguna Total Control Client A, menu, flag Guided Tooltip): disediakan tim FE.
  - Path daftar Measurement: `POST /v2/enterprise-management/measurements/list` (`tc-measurement-backend.md`). Endpoint daftar Changelog: disediakan tim FE sesuai kontrak modul activity-log. Rujukan `openapi.yaml` dan `low-level-design.md`: disediakan tim FE.
- Preferensi kolom tabel (visibilitas, urutan, pin) disimpan di `localStorage` browser dengan key unik per tabel (PRD measurement.md §4.2i; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya. "Muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Changelog dikembalikan ke default (urutan `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`, semua tampil, tanpa pin) lewat penghapusan preferensi kolom tabel Changelog di browser (key `localStorage` tabel Changelog; kemampuan disediakan tim FE, lihat Kemampuan teknis); viewport dikembalikan ke ukuran awal.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Measurement.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar Changelog dan daftar Measurement; drag and drop elemen (baris kolom pada modal dan panel); mengatur dan mengembalikan ukuran viewport; scroll horizontal tabel; hover (tooltip); membaca dan menghapus key `localStorage` browser (disediakan tim FE).
- Precondition TC-GS-UOM-308, 309, 310, 350: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement. TC-GS-UOM-309: viewport diperkecil hingga tabel Changelog dapat di-scroll horizontal.

## Test Steps

### TC-GS-UOM-308: Reorder kolom tabel Changelog lewat drag dan persist setelah F5

1. Klik icon Changelog
2. Klik header Actions (⋯) pada tabel Changelog, lalu klik `Setup Column...`
3. Geser `Modified By` ke posisi paling atas
4. Verifikasi preview mengurutkan `Modified By`, `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`
5. Geser `Date` ke posisi paling bawah
6. Verifikasi preview mengurutkan `Modified By`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Date`
7. Klik [Save]
8. Verifikasi header kolom Changelog mengikuti urutan langkah 6
9. Muat ulang halaman (F5)
10. Klik icon Changelog
11. Verifikasi header kolom Changelog tetap mengikuti urutan langkah 6
12. Klik header Actions (⋯) > `Setup Column...`, klik [Reset to Default], klik [Save]
13. Verifikasi urutan kembali `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`

### TC-GS-UOM-350: Reorder kolom tabel Changelog lewat drag di panel Column Visibility ter-apply langsung dan tersimpan

14. Klik header Actions (⋯) pada tabel Changelog sehingga panel Column Visibility terbuka
15. Geser `Modified By` ke atas `Date` di panel
16. Verifikasi urutan header Changelog langsung `Modified By`, `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value` tanpa menekan tombol apa pun
17. Muat ulang halaman (F5)
18. Klik icon Changelog
19. Verifikasi urutan header Changelog tetap `Modified By`, `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`
20. Klik header Actions (⋯) > `Setup Column...`, klik [Reset to Default], klik [Save]
21. Verifikasi urutan header Changelog kembali `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`

### TC-GS-UOM-309: Pin dan unpin kolom Changelog serta batas 3 kolom ter-pin

22. Perkecil viewport hingga tabel Changelog dapat di-scroll horizontal
23. Klik header Actions (⋯) pada tabel Changelog, lalu klik `Setup Column...`
24. Klik icon Pin `Date`
25. Klik [Save]
26. Scroll tabel Changelog secara horizontal
27. Verifikasi kolom `Date` tetap di posisinya saat tabel di-scroll horizontal
28. Klik header Actions (⋯) > `Setup Column...`
29. Klik icon Pin `Date` untuk unpin
30. Klik [Save]
31. Scroll tabel Changelog secara horizontal
32. Verifikasi kolom `Date` ikut bergeser saat di-scroll
33. Klik header Actions (⋯) > `Setup Column...`
34. Klik icon Pin `Date`, `Action`, dan `Unit Name`
35. Arahkan kursor ke icon Pin `Field`
36. Verifikasi icon Pin `Field` disabled
37. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
38. Coba klik icon Pin `Field`
39. Verifikasi kolom `Field` tidak menjadi beku (icon Pin `Field` tidak ter-pin)
40. Klik `[✕]` untuk menutup tanpa Save
41. Scroll tabel Changelog secara horizontal
42. Verifikasi kolom `Date`, `Action`, dan `Unit Name` ikut bergeser saat di-scroll (perubahan pin dibuang)
43. Kembalikan viewport ke ukuran awal

### TC-GS-UOM-310: Reset to Default modal Setup Column Changelog mengembalikan susunan default

44. Klik header Actions (⋯) > `Setup Column...`
45. Uncheck `Field` dan geser `Modified By` ke posisi paling atas
46. Klik [Save]
47. Klik header Actions (⋯) > `Setup Column...`
48. Klik [Reset to Default]
49. Verifikasi preview menampilkan 7 kolom dengan urutan `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`
50. Klik [Save]
51. Verifikasi tabel Changelog memakai susunan default
52. Muat ulang halaman (F5)
53. Klik icon Changelog
54. Verifikasi tabel Changelog tetap memakai susunan default

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-308, 350, 309, 310. Alasan: TC-GS-UOM-308 dan 350 berakhir dengan reset ke default sehingga TC berikutnya mulai dari state bersih; TC-GS-UOM-309 butuh viewport diperkecil dan dipulihkan sebelum TC-GS-UOM-310; TC-GS-UOM-310 di akhir karena reset mengembalikan konfigurasi sekaligus menjadi pemulihan state.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 22 dan 43 (memperkecil dan mengembalikan viewport), langkah 10 dan 18 dan 53 (membuka ulang Modal Changelog sesudah F5), langkah 28 dan 33 dan 44 dan 47 (membuka ulang popup Setup Column).
- Langkah 12 dan 20 adalah langkah ketiga TC sumber (Reset to Default sebagai pemulihan) yang ekspektasinya diasersi di langkah 13 dan 21.
- Spec ini melewati sekitar 35 langkah (54 langkah).
- Dipisah dari `TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup`: topik Setup Column Modal Changelog dengan dataset mock dan akun yang sama, tetapi gabungan kedua spec 110 langkah nominal (56 + 54), jauh melewati batas ukuran sekitar 35 langkah. Spec ini memuat reorder, pin, dan reset; spec 051 memuat screening, hide/unhide, dan tutup modal. Kebutuhan data mock berbeda: spec ini membutuhkan nilai Old Value/New Value panjang agar kolom melebihi viewport (TC-GS-UOM-309). Alasan: keempat TC adalah perilaku satu Modal Setup Column Changelog pada satu dataset mock dan satu kelas harness (mock UI); gagalnya membuka Modal Changelog di langkah 1 membuat seluruh blok kehilangan makna, sehingga pemisahan hanya menambah pembukaan modal.
- Temuan untuk QA:
  - TC-GS-UOM-309 Expected c menyebut kolom `Field` "tidak menjadi beku" tanpa menyebut cara mengamatinya; spec mengasersi icon Pin `Field` tidak ter-pin sesudah percobaan klik.
  - TC-GS-UOM-309 menyebut viewport diperkecil tanpa ukuran; lebar yang membuat tabel Changelog dapat di-scroll horizontal bergantung pada isi kolom Old Value/New Value, sehingga ukuran viewport ditentukan tim FE.
