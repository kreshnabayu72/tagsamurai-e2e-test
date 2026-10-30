---
id: TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup
title: "Changelog Measurement: Setup Column Screening, Hide/Unhide, Guard Kolom Terakhir, Tutup Modal, dan Preferensi Terpisah dari Tabel Utama"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-187
  - TC-GS-UOM-297
  - TC-GS-UOM-306
  - TC-GS-UOM-307
  - TC-GS-UOM-311
  - TC-GS-UOM-312
coverage:
  web: automated
---

# Changelog Measurement: Setup Column Screening, Hide/Unhide, Guard Kolom Terakhir, Tutup Modal, dan Preferensi Terpisah dari Tabel Utama

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip halaman Measurement: disetel true (flag `seen`) oleh kemampuan yang disediakan tim FE untuk integration test; rujukan pernyataan hook suite di `suite.md` (bagian "Hook suite").
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Kebutuhan mock (endpoint dan respons yang dipaksa):
  - Daftar Measurement (tabel utama) mengembalikan sedikitnya tiga unit (mis. `Box`, `Dozen`, `Gram`) beserta Used By (Items) dan Last Updated, supaya kolom tabel utama `Unit Name`, `Symbol`, dan `Last Updated` terbaca (TC-GS-UOM-297).
  - Daftar Changelog Measurement mengembalikan sedikitnya satu entri, supaya ketujuh kolom Changelog terisi.
  - API pendukung di luar modul (identitas pengguna Total Control Client A, menu, flag Guided Tooltip): disediakan tim FE.
  - Path daftar Measurement: `POST /v2/enterprise-management/measurements/list` (`tc-measurement-backend.md`). Endpoint daftar Changelog: disediakan tim FE sesuai kontrak modul activity-log. Rujukan `openapi.yaml` dan `low-level-design.md`: disediakan tim FE.
- Preferensi kolom tabel (visibilitas, urutan, pin) disimpan di `localStorage` browser dengan key unik per tabel (PRD measurement.md §4.2i; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya. "Muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Tabel "Kolom Changelog" untuk TC-GS-UOM-307 (langkah 32 sampai 35 diulang per kolom): `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Changelog dikembalikan ke default (ketujuh kolom tampil dengan urutan `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`, tanpa pin) lewat penghapusan preferensi kolom tabel Changelog di browser (key `localStorage` tabel Changelog; kemampuan disediakan tim FE, lihat Kemampuan teknis); konfigurasi tabel utama tidak diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Measurement.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar Measurement dan daftar Changelog; hover (tooltip); muat ulang halaman; membaca dan menghapus key `localStorage` browser (disediakan tim FE).
- Precondition TC-GS-UOM-187, 297, 306, 307, 311, 312: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

1. Klik icon Changelog

### TC-GS-UOM-187: Setup Column Modal Changelog

2. Klik header Actions (⋯) pada tabel Changelog
3. Verifikasi Panel Column Visibility berisi 7 kolom Changelog: `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi Panel Column Visibility berisi item `Setup Column...`
5. Verifikasi ketujuh kolom tersebut Hideable (checkbox tercentang dan enabled)

### TC-GS-UOM-306: Screening Popup Setup Column dari Modal Changelog

6. Klik `Setup Column...`
7. Verifikasi Header: Title `Setup Column`
8. Verifikasi Header: subtitle `Manage column visibility, reorder, and freeze columns.`
9. Verifikasi Header: icon close `[✕]`
10. Verifikasi Body: kolom search `Search column name...`
11. Verifikasi Body: daftar kolom `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, `Modified By` masing-masing dengan checkbox tercentang dan enabled (Hideable)
12. Verifikasi Body: drag handle pada setiap baris kolom
13. Verifikasi Body: icon Pin pada setiap baris kolom
14. Verifikasi Footer rata kanan: `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
15. Verifikasi Footer tidak memuat tombol `[Cancel]`

### TC-GS-UOM-311: Menutup modal Setup Column Changelog lewat [✕] dan Esc membuang perubahan preview

16. Uncheck `Field` (tabel Changelog ter-preview tanpa Field)
17. Klik `[✕]`
18. Verifikasi kolom `Field` kembali tampil pada tabel Changelog
19. Klik header Actions (⋯) pada tabel Changelog, lalu klik `Setup Column...`
20. Uncheck `Field`
21. Tekan Esc
22. Verifikasi kolom `Field` kembali tampil pada tabel Changelog dengan hasil yang sama seperti `[✕]`

### TC-GS-UOM-312: Kolom Changelog terakhir yang tampil tidak dapat di-uncheck

23. Klik header Actions (⋯) pada tabel Changelog, lalu klik `Setup Column...`
24. Uncheck `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` sehingga hanya `Date` visible
25. Coba uncheck `Date`
26. Hover checkbox `Date`
27. Verifikasi checkbox `Date` disabled (tetap tampil)
28. Verifikasi tooltip `At least one column must remain visible.`
29. Klik `[✕]`
30. Verifikasi kolom `Date`, `Action`, `Unit Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` kembali tampil pada tabel Changelog

### TC-GS-UOM-307: Hide dan unhide tiap kolom tabel Changelog lewat modal Setup Column

31. Klik header Actions (⋯) pada tabel Changelog, lalu klik `Setup Column...`

Untuk setiap kolom pada tabel "Kolom Changelog" di Prerequisites (langkah 32 sampai 35):

32. Uncheck kolom, amati preview tabel Changelog
33. Verifikasi kolom hilang dari preview
34. Check kembali kolom
35. Verifikasi kolom kembali tampil pada preview

36. Uncheck `Old Value` dan `New Value`
37. Klik [Save]
38. Verifikasi kolom `Old Value` dan `New Value` tidak tampil pada tabel Changelog
39. Verifikasi modal Setup Column tertutup
40. Muat ulang halaman (F5)
41. Klik icon Changelog
42. Verifikasi kolom `Old Value` dan `New Value` tetap tidak tampil
43. Klik header Actions (⋯) pada tabel Changelog, lalu klik `Setup Column...`
44. Check `Old Value` dan `New Value`
45. Klik [Save]
46. Verifikasi kolom `Old Value` dan `New Value` tampil kembali

### TC-GS-UOM-297: Preferensi kolom Modal Changelog tidak memengaruhi tabel utama

47. Klik header Actions (⋯) pada tabel Changelog, lalu uncheck `Field`
48. Verifikasi kolom `Field` hilang dari Modal Changelog
49. Klik `[✕]` untuk menutup Modal Changelog
50. Verifikasi tabel utama tetap memuat kolom `Unit Name`, `Symbol`, dan `Last Updated`
51. Muat ulang halaman (F5)
52. Klik icon Changelog
53. Verifikasi Modal Changelog tetap tanpa kolom `Field`
54. Verifikasi tabel utama tetap memuat kolom `Unit Name`, `Symbol`, dan `Last Updated`
55. Klik header Actions (⋯) pada tabel Changelog, lalu check kembali `Field`
56. Verifikasi kolom `Field` tampil kembali

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Changelog dibuka sekali (langkah 1) dan dipakai berurutan; sesudah F5 dibuka ulang (langkah 41 dan 52). Urutan TC dalam spec: TC-GS-UOM-187, 306, 311, 312, 307, 297. Alasan: screening lebih dulu; tutup tanpa Save (311) dan guard kolom terakhir (312) dijalankan sebelum TC yang menyimpan konfigurasi (307, 297) supaya perubahan yang tidak disimpan tidak bercampur dengan konfigurasi tersimpan (prinsip 2 dan 3 konvensi 3).
- Langkah 32 sampai 35 diulang untuk 7 kolom (ekspansi 28 langkah); parameter ada di Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 19, 23, 31, 43 (membuka ulang popup Setup Column).
- TC-GS-UOM-187 butir b "dengan guard minimal satu kolom tetap visible": guard diasersi di TC-GS-UOM-312 (langkah 25 sampai 30); langkah 5 hanya mengasersi ketujuh kolom Hideable.
- Spec ini melewati sekitar 35 langkah (56 langkah nominal).
- Dipisah dari `TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset`: topik Setup Column Modal Changelog dengan dataset mock dan akun yang sama, tetapi gabungan kedua spec 110 langkah nominal (56 + 54), jauh melewati batas ukuran sekitar 35 langkah. Spec ini memuat screening, hide/unhide, dan tutup modal; spec 052 memuat reorder, pin, dan reset. Alasan: keenam TC berbagi satu Modal Changelog, satu dataset mock, dan satu kelas harness (mock UI); kegagalan keras membuka modal membuat seluruh blok kehilangan makna, dan pemisahan hanya menambah pembukaan modal tanpa mengurangi risiko.
- Temuan untuk QA:
  - TC-GS-UOM-297 Expected b menyebut tabel utama "tetap memuat `Unit Name`, `Symbol`, dan `Last Updated`" tanpa menyebut kolom `Used By (Items)`; spec mengasersi tiga kolom itu saja.
