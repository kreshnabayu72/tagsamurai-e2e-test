---
id: TC-GS-BRAND-E2E-017-create-population-12-brand-stay-checked
title: "Create 12 Brand Berurutan dengan Stay on this form Dicentang (Population)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-1
coverage:
  web: automated
---

# Create 12 Brand Berurutan dengan Stay on this form Dicentang (Population)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data pre-setup: 12 brand Client A (Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp). Tabel harus berisi tepat 12 brand ini sebelum spec dimulai; suite berjalan serial (`parallel: false`) sehingga tidak ada spec lain yang menambah brand Client A selama spec ini berjalan.
- Data dinamis D-01 (Population, 12 brand): Apex Tools, Bolt Systems, Cedar Supply, Delta Instruments, Echo Devices, Falcon Gear, Granite Works, Harbor Tech, Iris Optics, Juniper Labs, Keystone Mfg, Linear Dynamics. Dibuat lewat UI oleh spec ini. Nama literal tanpa suffix `{runId}` karena asersi urutan A-Z dan jumlah 24 baris bergantung pada nama ini.
- Hook `before`: hapus lewat API sisa brand D-01 dari run sebelumnya (bila ada) sehingga tabel awal tepat 12 brand.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API seluruh 12 brand D-01 bila masih ada.
- Kemampuan teknis: pembacaan fokus keyboard pada field Brand Name; pembacaan pagination (jumlah halaman dan baris per halaman).
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-BRAND-1: Create 12 Brand berurutan dengan Stay on this form dicentang (Population)

1. Buka Global Settings > Master Reference > Brand
2. Klik [+ Brand]
3. Centang checkbox `Stay on this form after submitting`
4. Isi Brand Name `Apex Tools`, klik [Submit]
5. Verifikasi toast sukses: "Success, brand has been created."
6. Verifikasi form tetap terbuka
7. Verifikasi field Brand Name kosong
8. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
9. Verifikasi fokus keyboard kembali ke field Brand Name
10. Isi Brand Name `Bolt Systems`, klik [Submit]
11. Verifikasi toast sukses: "Success, brand has been created."
12. Verifikasi form tetap terbuka
13. Verifikasi field Brand Name kosong
14. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
15. Verifikasi fokus keyboard kembali ke field Brand Name
16. Isi Brand Name `Cedar Supply`, klik [Submit]
17. Verifikasi toast sukses: "Success, brand has been created."
18. Verifikasi form tetap terbuka
19. Verifikasi field Brand Name kosong
20. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
21. Verifikasi fokus keyboard kembali ke field Brand Name
22. Isi Brand Name `Delta Instruments`, klik [Submit]
23. Verifikasi toast sukses: "Success, brand has been created."
24. Verifikasi form tetap terbuka
25. Verifikasi field Brand Name kosong
26. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
27. Verifikasi fokus keyboard kembali ke field Brand Name
28. Isi Brand Name `Echo Devices`, klik [Submit]
29. Verifikasi toast sukses: "Success, brand has been created."
30. Verifikasi form tetap terbuka
31. Verifikasi field Brand Name kosong
32. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
33. Verifikasi fokus keyboard kembali ke field Brand Name
34. Isi Brand Name `Falcon Gear`, klik [Submit]
35. Verifikasi toast sukses: "Success, brand has been created."
36. Verifikasi form tetap terbuka
37. Verifikasi field Brand Name kosong
38. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
39. Verifikasi fokus keyboard kembali ke field Brand Name
40. Isi Brand Name `Granite Works`, klik [Submit]
41. Verifikasi toast sukses: "Success, brand has been created."
42. Verifikasi form tetap terbuka
43. Verifikasi field Brand Name kosong
44. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
45. Verifikasi fokus keyboard kembali ke field Brand Name
46. Isi Brand Name `Harbor Tech`, klik [Submit]
47. Verifikasi toast sukses: "Success, brand has been created."
48. Verifikasi form tetap terbuka
49. Verifikasi field Brand Name kosong
50. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
51. Verifikasi fokus keyboard kembali ke field Brand Name
52. Isi Brand Name `Iris Optics`, klik [Submit]
53. Verifikasi toast sukses: "Success, brand has been created."
54. Verifikasi form tetap terbuka
55. Verifikasi field Brand Name kosong
56. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
57. Verifikasi fokus keyboard kembali ke field Brand Name
58. Isi Brand Name `Juniper Labs`, klik [Submit]
59. Verifikasi toast sukses: "Success, brand has been created."
60. Verifikasi form tetap terbuka
61. Verifikasi field Brand Name kosong
62. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
63. Verifikasi fokus keyboard kembali ke field Brand Name
64. Isi Brand Name `Keystone Mfg`, klik [Submit]
65. Verifikasi toast sukses: "Success, brand has been created."
66. Verifikasi form tetap terbuka
67. Verifikasi field Brand Name kosong
68. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
69. Verifikasi fokus keyboard kembali ke field Brand Name
70. Isi Brand Name `Linear Dynamics`, klik [Submit]
71. Verifikasi toast sukses: "Success, brand has been created."
72. Verifikasi form tetap terbuka
73. Verifikasi field Brand Name kosong
74. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
75. Verifikasi fokus keyboard kembali ke field Brand Name
76. Tutup form lewat icon `[✕]`
77. Verifikasi tabel berisi 24 baris: 12 brand Pre-setup ditambah 12 brand Population
78. Verifikasi tabel terbagi dalam 3 halaman (10 per halaman)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Spec ini sengaja satu TC (TC-GS-BRAND-1) karena menjadi sumber Population D-01 yang dibutuhkan spec lain; spec lain menyiapkan Population-nya sendiri lewat API di hook `before` dan tidak bergantung pada spec ini.
- Langkah 4 sampai 75 adalah pengulangan "Isi Brand Name, klik [Submit]" untuk data ke-1 sampai ke-12 sesuai Langkah Uji 3 dan 4 TC sumber; tiap pengulangan ditutup asersi toast dan empat asersi state form (Expected Result a dan b).
- Karena 12 pengulangan, spec melewati sekitar 35 langkah; tetap satu topik aksi, satu akun, satu kelas.
- Asersi 24 baris dan 3 halaman pada langkah 77 dan 78 bergantung pada tabel awal tepat 12 brand dan nama Population literal (spec lain mengasersi urutan A-Z dari nama ini); run paralel dengan spec lain yang menambah brand ke Client A tidak diizinkan (suite `parallel: false`).
