---
id: TC-GS-UOM-E2E-049-changelog-filter-chip-x-uncheck-dan-overflow
title: "Changelog Measurement: Chip Filter (X), Uncheck Opsi, dan Overflow +N more"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-302
  - TC-GS-UOM-303
  - TC-GS-UOM-304
coverage:
  web: automated
---

# Changelog Measurement: Chip Filter (X), Uncheck Opsi, dan Overflow +N more

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` suite (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Layar awal Global Settings > Master Reference > Measurement dibuka di hook `beforeEach` suite.
- Akun seeding tambahan (hanya untuk seeding API di hook `before`, bukan login UI): Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_CREATE_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite (lihat bagian "Hook suite" di `suite.md`).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Suite berjalan serial (`parallel: false`).
- Seeding (lewat API di hook `before`, urutan sebagai berikut):
  - Population D-01 oleh Sari Dewi (setara TC-GS-UOM-36), idempotent (nama yang sudah ada dilewati): `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Menghasilkan entri Create oleh `Sari D` untuk 10 nama pada TC-GS-UOM-304 dan untuk `Centimeter` pada TC-GS-UOM-302 dan 303.
  - Unit milik spec `Kilometer {runId}-049` (Symbol `km`) dibuat oleh Rina Marlina (entri Create oleh `Rina M`, setara TC-GS-UOM-32), lalu Symbol-nya diubah menjadi `kms` oleh Sari Dewi (entri Edit, Field `Symbol`, oleh `Sari D`). Nama bersuffix menggantikan `Kilometer` pada Data Uji TC-GS-UOM-302 dan 303.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Kilometer {runId}-049` dan unit Population yang dibuat spec ini (yang sudah ada sebelum spec dilewati); ukuran viewport dikembalikan ke bawaan. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: viewport desktop lebar 1280 px (diatur di hook `before`, TC-GS-UOM-304); klik `(X)` pada chip filter; membaca jumlah chip yang tampil pada field.
- Precondition TC-GS-UOM-302, 303: login sebagai Total Control; entri Changelog Population dan Create/Edit Kilometer tersedia (Create Centimeter oleh `Sari D`; Create Kilometer oleh `Rina M`). TC-GS-UOM-304: entri Create untuk 10 nama Population tersedia; viewport desktop lebar 1280 px.
- State global yang dipulihkan: ukuran viewport (hook `after`).

## Test Steps

### TC-GS-UOM-304: Overflow chip pada field Unit Name filter Changelog diringkas menjadi +N more

1. Klik icon Changelog di halaman Global Settings > Master Reference > Measurement
2. Klik Filter
3. Pilih 10 opsi Unit Name: `Centimeter`, `Millimeter`, `Inch`, `Foot`, `Milliliter`, `Ounce`, `Ton`, `Roll`, `Set`, `Sheet`
4. Amati field Unit Name
5. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field
6. Verifikasi sisanya diringkas dalam satu chip `+N more`
7. Verifikasi jumlah chip tampil ditambah N sama dengan 10
8. Verifikasi field tidak melebar keluar panel
9. Verifikasi field tidak digulir horizontal

### TC-GS-UOM-302: Menghapus chip filter Changelog lewat (X) pada field Action, Unit Name, Field, dan Modified By

10. Kosongkan seluruh pilihan Unit Name (sisa TC-GS-UOM-304)
11. Pilih Action `Create` dan `Edit`
12. Pilih Unit Name `Centimeter` dan `Kilometer {runId}-049`
13. Pilih Field `Unit Name` dan `Symbol`
14. Pilih Modified By `Sari D` dan `Rina M`
15. Klik `(X)` pada chip `Edit` (field Action)
16. Klik `(X)` pada chip `Kilometer {runId}-049` (field Unit Name)
17. Klik `(X)` pada chip `Symbol` (field Field)
18. Klik `(X)` pada chip `Rina M` (field Modified By)
19. Verifikasi field Action: chip `Edit` hilang
20. Verifikasi field Action: chip `Create` tetap
21. Verifikasi field Unit Name: chip `Kilometer {runId}-049` hilang
22. Verifikasi field Unit Name: chip `Centimeter` tetap
23. Verifikasi field Field: chip `Symbol` hilang
24. Verifikasi field Field: chip `Unit Name` tetap
25. Verifikasi field Modified By: chip `Rina M` hilang
26. Verifikasi field Modified By: chip `Sari D` tetap
27. Buka dropdown Action, amati checkbox
28. Verifikasi checkbox `Edit` ter-uncheck
29. Buka dropdown Unit Name, amati checkbox
30. Verifikasi checkbox `Kilometer {runId}-049` ter-uncheck
31. Buka dropdown Field, amati checkbox
32. Verifikasi checkbox `Symbol` ter-uncheck
33. Buka dropdown Modified By, amati checkbox
34. Verifikasi checkbox `Rina M` ter-uncheck
35. Klik [Apply]
36. Verifikasi hasil memuat baris Action `Create`, Unit Name `Centimeter`, Field `Unit Name`, Modified By `Sari D`
37. Verifikasi setiap baris yang tampil memiliki Action `Create`, Unit Name `Centimeter`, Field `Unit Name`, dan Modified By `Sari D`

### TC-GS-UOM-303: Meng-uncheck opsi di dalam dropdown filter Changelog menghapus chip pada field Action, Unit Name, Field, dan Modified By

38. Klik Filter, kosongkan seluruh pilihan field Action, Unit Name, Field, dan Modified By (sisa TC-GS-UOM-302)
39. Pilih Action `Create` dan `Edit`
40. Pilih Unit Name `Centimeter` dan `Kilometer {runId}-049`
41. Pilih Field `Unit Name` dan `Symbol`
42. Pilih Modified By `Sari D` dan `Rina M`
43. Buka dropdown Action dan uncheck `Edit`
44. Buka dropdown Unit Name dan uncheck `Kilometer {runId}-049`
45. Buka dropdown Field dan uncheck `Symbol`
46. Buka dropdown Modified By dan uncheck `Rina M`
47. Verifikasi field Action: chip `Edit` hilang
48. Verifikasi field Action: chip `Create` tetap
49. Verifikasi field Unit Name: chip `Kilometer {runId}-049` hilang
50. Verifikasi field Unit Name: chip `Centimeter` tetap
51. Verifikasi field Field: chip `Symbol` hilang
52. Verifikasi field Field: chip `Unit Name` tetap
53. Verifikasi field Modified By: chip `Rina M` hilang
54. Verifikasi field Modified By: chip `Sari D` tetap
55. Klik [Apply]
56. Verifikasi hasil memuat baris Action `Create`, Unit Name `Centimeter`, Field `Unit Name`, Modified By `Sari D`
57. Verifikasi setiap baris yang tampil memiliki Action `Create`, Unit Name `Centimeter`, Field `Unit Name`, dan Modified By `Sari D`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-304, 302, 303. Alasan: TC-GS-UOM-304 hanya mengamati field tanpa [Apply] (screening lebih dulu, prinsip 2 konvensi 3), sedangkan 302 dan 303 meng-Apply filter; Modal Changelog dibuka sekali untuk ketiganya.
- Langkah penghubung (aksi tanpa `Verifikasi`, membersihkan state filter dari TC sebelumnya): langkah 10 dan 38.
- Langkah 36 dan 56 adalah pembanding positif bagi langkah 37 dan 57 (asersi universal). Unit Name `Kilometer {runId}-049` bersuffix menggantikan `Kilometer` di Data Uji agar tidak bentrok dengan spec lain; `Centimeter` memakai nama Population literal.
- Spec ini melewati sekitar 35 langkah (57 langkah). Alasan: ketiga TC menguji satu perilaku (sinkronisasi chip dan checkbox pada Filter Panel Changelog) pada satu dataset dan satu modal; satu kelas harness (fungsional). Langkah TC-GS-UOM-302 dan 303 sengaja diulang untuk empat field sesuai Expected a sampai d. Memecah spec menambah seeding dan pembukaan modal tanpa memperkecil risiko.
- Temuan untuk QA: Expected TC-GS-UOM-302 butir a sampai d menyebut chip pasangan "tetap" dan checkbox "ter-uncheck"; kondisi checkbox pasangan yang tetap tercentang tidak disebut TC dan tidak diasersi.
