---
id: TC-GS-UOM-E2E-057-detail-setup-column-device-name-list
title: "Unit Detail Principal: Setup Column Device Name List"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-320
  - TC-GS-UOM-321
  - TC-GS-UOM-322
coverage:
  web: automated
tags: [principal]
---

# Unit Detail Principal: Setup Column Device Name List

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip halaman Measurement: disetel true (flag `seen`) oleh kemampuan yang disediakan tim FE untuk integration test; rujukan pernyataan hook suite di `suite.md` (bagian "Hook suite").
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Kebutuhan mock (endpoint dan respons yang dipaksa):
  - Daftar Measurement (tabel utama) instance Principal mengembalikan unit `Watt` (Symbol `W`) beserta Used By (Items) `2` dan Last Updated, supaya baris `Watt` dapat dibuka lewat `⋯` > Detail.
  - Detail Measurement `Watt` mengembalikan Device Name `BLE Gateway` dan `Handheld Reader` tanpa Item Type. Detail diambil lewat request terpisah dari List (NC-18).
  - Identitas pengguna instance Principal (Total Control), menu, dan flag Guided Tooltip: disediakan tim FE.
  - Path daftar Measurement: `POST /v2/enterprise-management/measurements/list`; path Detail Measurement: `GET /v2/enterprise-management/measurements/{measurement_id}` (`tc-measurement-backend.md`). Rujukan `openapi.yaml` dan `low-level-design.md`: disediakan tim FE.
- Preferensi kolom tabel (visibilitas, urutan, pin) disimpan di `localStorage` browser dengan key unik per tabel (PRD measurement.md §4.2i; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Device Name List dikembalikan ke default (kolom `Device Name` tampil, tanpa pin) lewat penghapusan preferensi kolom tabel Device Name List di browser (key `localStorage` tabel Device Name List; kemampuan disediakan tim FE, lihat Kemampuan teknis); viewport dikembalikan ke ukuran awal.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Measurement.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar dan Detail Measurement; mengatur dan mengembalikan ukuran viewport; scroll horizontal tabel; hover (tooltip); membaca dan menghapus key `localStorage` browser (disediakan tim FE).
- Precondition TC-GS-UOM-320, 321, 322: login sebagai Total Control (Principal) dan berada di Global Settings > Master Reference > Measurement; Watt dipakai BLE Gateway dan Handheld Reader. TC-GS-UOM-322: viewport diperkecil hingga tabel Device Name List dapat di-scroll horizontal.

## Test Steps

1. Klik `⋯` pada baris Watt
2. Klik Detail

### TC-GS-UOM-320: Screening Popup Setup Column dari tabel Device Name List

3. Klik header Actions (⋯) pada tabel Device Name List
4. Klik `Setup Column...`
5. Verifikasi Header: Title `Setup Column`
6. Verifikasi Header: subtitle `Manage column visibility, reorder, and freeze columns.`
7. Verifikasi Header: icon close `[✕]`
8. Verifikasi Body: kolom search `Search column name...`
9. Verifikasi Body: satu kolom `Device Name` dengan checkbox tercentang dan enabled (Hideable)
10. Verifikasi Body: drag handle pada baris kolom `Device Name`
11. Verifikasi Body: icon Pin pada baris kolom `Device Name`
12. Verifikasi Footer rata kanan: `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
13. Verifikasi Footer tidak memuat tombol `[Cancel]`
14. Klik `[✕]`

### TC-GS-UOM-321: Kolom Device Name sebagai satu-satunya kolom tidak dapat di-uncheck

15. Klik header Actions (⋯) pada tabel Device Name List
16. Coba uncheck `Device Name` di panel Column Visibility
17. Hover checkbox `Device Name` pada panel Column Visibility
18. Verifikasi checkbox `Device Name` pada panel Column Visibility disabled
19. Verifikasi tooltip `At least one column must remain visible.` pada panel Column Visibility
20. Klik `Setup Column...`
21. Coba uncheck `Device Name` di modal Setup Column
22. Hover checkbox `Device Name` pada modal Setup Column
23. Verifikasi checkbox `Device Name` pada modal Setup Column disabled
24. Verifikasi tooltip `At least one column must remain visible.` pada modal Setup Column
25. Klik `[✕]`

### TC-GS-UOM-322: Pin dan unpin kolom Device Name

26. Perkecil viewport hingga tabel Device Name List dapat di-scroll horizontal
27. Klik header Actions (⋯) pada tabel Device Name List, lalu klik `Setup Column...`
28. Klik icon Pin `Device Name`
29. Klik [Save]
30. Scroll tabel Device Name List secara horizontal
31. Verifikasi kolom `Device Name` tetap di posisinya saat tabel di-scroll horizontal
32. Klik header Actions (⋯) > `Setup Column...`
33. Klik icon Pin `Device Name` untuk unpin
34. Klik [Save]
35. Scroll tabel Device Name List secara horizontal
36. Verifikasi kolom `Device Name` kembali ikut bergeser saat di-scroll
37. Kembalikan viewport ke ukuran awal

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan (320 screening, 321 guard, 322 pin). TC-GS-UOM-322 di akhir karena membutuhkan viewport diperkecil dan menyimpan pin, yang dipulihkan di langkah 32 sampai 34 (unpin) dan hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (membuka Detail Watt), langkah 14 dan 25 (menutup popup Setup Column), langkah 26 dan 37 (memperkecil dan mengembalikan viewport).
- Spec ini sekitar 35 langkah (37 langkah). Alasan: ketiga TC adalah perilaku satu tabel Device Name List pada satu pembukaan Detail dengan satu dataset mock dan satu kelas harness (mock UI).
- Pembagian TC lintas spec: Setup Column Item Type List ada di `TC-GS-UOM-E2E-056-detail-setup-column-item-type-list`; isi dan Search/Sort Device Name List di `TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor`.
- Temuan untuk QA:
  - TC-GS-UOM-322 menyebut viewport diperkecil tanpa ukuran; lebar yang membuat tabel satu kolom dapat di-scroll horizontal bergantung pada lebar kolom, sehingga ukuran viewport ditentukan tim FE.
