---
id: TC-GS-BRAND-E2E-016-create-sukses-batas-trim-karakter-dan-submit
title: "Create Brand Berhasil: Batas Karakter, Trim, Karakter Khusus, dan Perilaku Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-44
  - TC-GS-BRAND-46
  - TC-GS-BRAND-47
  - TC-GS-BRAND-50
  - TC-GS-BRAND-56
  - TC-GS-BRAND-64
  - TC-GS-BRAND-65
  - TC-GS-BRAND-151
coverage:
  web: automated
---

# Create Brand Berhasil: Batas Karakter, Trim, Karakter Khusus, dan Perilaku Submit

## Prerequisites

- Mode: FE+BE (backend nyata). Kasus saving state (TC-GS-BRAND-64) memakai intercept parsial di atas backend nyata.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data pre-setup: 12 brand Client A (Acme Corp sampai Zenith Corp) sebagai latar tabel; tidak diubah spec ini.
- Data dinamis (dibuat lewat UI oleh spec ini; nama memakai suffix per run `{runId}`, dan `{runId}-016` untuk nama yang juga dipakai spec lain):
  - D-03: Brand Name 120 karakter huruf `B` yang diakhiri ` {runId}`; panjang total sudah termasuk suffix (tepat 120).
  - D-06: input = 2 spasi + `é` (U+00E9) diulang lalu ` {runId}` + 2 spasi; jumlah `é` disesuaikan sehingga panjang setelah trim tepat 120 termasuk suffix.
  - D-07: input `  Rook  Labs {runId}  ` (2 spasi depan, 2 spasi internal, 2 spasi belakang); tersimpan `Rook  Labs {runId}`.
  - D-08: `Café O’Neil – Ünïcode™ ® © 東京 {runId}`.
  - D-12: `Vesper Co {runId}-016`; D-13: `Wren Co {runId}-016`; D-11: `Tidal Co {runId}-016`; D-27: `Omega Works {runId}`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua brand D-03, D-06, D-07, D-08, D-11, D-12, D-13, dan D-27 yang bernama memuat `{runId}` bila masih ada.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons Create Brand 3 detik dan melepas intercept sesudahnya (TC-GS-BRAND-64); klik ganda cepat pada [Submit] (TC-GS-BRAND-65); hover pada tombol; pembacaan teks sel tabel termasuk spasi internal; Search pada tabel.
- State global: tidak ada yang diubah (intercept dilepas di langkah 30 dan di hook `after`).

## Test Steps

### TC-GS-BRAND-44: Create Brand Name tepat 120 karakter berhasil

1. Buka Global Settings > Master Reference > Brand
2. Klik [+ Brand]
3. Centang checkbox `Stay on this form after submitting` agar form tetap terbuka untuk Create berikutnya
4. Ketik Brand Name 120 karakter (D-03, total termasuk suffix ` {runId}`)
5. Verifikasi tidak ada error inline
6. Klik [Submit]
7. Verifikasi toast sukses: "Success, brand has been created."

### TC-GS-BRAND-46: Batas 120 dihitung setelah trim: nama 120 karakter beraksen diterima, spasi tepi tidak dihitung

8. Ketik 2 spasi, lalu 120 karakter `é` (termasuk suffix ` {runId}`), lalu 2 spasi pada field Brand Name (D-06)
9. Verifikasi tidak ada error `Max. 120 characters`
10. Klik [Submit]
11. Verifikasi toast sukses: "Success, brand has been created."

### TC-GS-BRAND-47: Create memangkas spasi depan dan belakang Brand Name, spasi ganda internal dipertahankan

12. Ketik `  Rook  Labs {runId}  ` pada field Brand Name (D-07)
13. Klik [Submit]
14. Verifikasi toast sukses: "Success, brand has been created."

### TC-GS-BRAND-50: Create Brand Name dengan tanda baca non-ASCII ’ – — ™ ® © dan huruf non-Latin diterima

15. Ketik `Café O’Neil – Ünïcode™ ® © 東京 {runId}` pada field Brand Name (D-08)
16. Verifikasi tidak ada error karakter
17. Klik [Submit]
18. Verifikasi toast sukses: "Success, brand has been created."

### TC-GS-BRAND-64: Saving state tombol Submit pada Create

19. Pasang intercept yang menahan respons Create Brand selama 3 detik
20. Ketik `Vesper Co {runId}-016` pada field Brand Name (D-12)
21. Hover [Submit]
22. Verifikasi hover [Submit] menampilkan background success hover
23. Klik [Submit]
24. Verifikasi [Submit] menampilkan spinner
25. Verifikasi [Submit] disabled
26. Verifikasi field Brand Name ikut disabled
27. Verifikasi checkbox `Stay on this form after submitting` ikut disabled
28. Verifikasi [Clear Field] ikut disabled
29. Verifikasi setelah respons kembali, toast sukses: "Success, brand has been created."
30. Lepas intercept penahan respons

### TC-GS-BRAND-65: Klik ganda Submit Create hanya membuat satu record

31. Ketik `Wren Co {runId}-016` pada field Brand Name (D-13)
32. Klik [Submit] dua kali cepat
33. Verifikasi hanya satu toast sukses yang tampil: "Success, brand has been created."

### TC-GS-BRAND-56: Submit Create dengan Stay unchecked menutup form

34. Lepas centang checkbox `Stay on this form after submitting`
35. Ketik `Tidal Co {runId}-016` pada field Brand Name (D-11)
36. Klik [Submit]
37. Verifikasi toast sukses: "Success, brand has been created."
38. Verifikasi modal tertutup
39. Isi Search dengan `Tidal Co {runId}-016`
40. Verifikasi `Tidal Co {runId}-016` tampil di tabel
41. Verifikasi Used By (Items) baris `Tidal Co {runId}-016` bernilai `0`
42. Verifikasi Last Updated baris `Tidal Co {runId}-016` sesuai waktu Submit

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-BRAND-44, 46, 47, 50, 65)

43. Isi Search dengan nama Brand D-03 (120 karakter)
44. Verifikasi brand D-03 tampil di tabel (TC-GS-BRAND-44)
45. Isi Search dengan nama Brand D-06
46. Verifikasi brand D-06 tersimpan dan tampil di tabel (TC-GS-BRAND-46)
47. Isi Search dengan `Rook  Labs {runId}`
48. Verifikasi teks sel nama brand sama persis dengan `Rook  Labs {runId}` (tanpa spasi tepi, dua spasi internal tetap) (TC-GS-BRAND-47)
49. Isi Search dengan `Café O’Neil`
50. Verifikasi nama tampil persis `Café O’Neil – Ünïcode™ ® © 東京 {runId}` di tabel (TC-GS-BRAND-50)
51. Isi Search dengan `Wren Co {runId}-016`
52. Verifikasi tabel menampilkan 1 baris (TC-GS-BRAND-65)
53. Kosongkan Search

### TC-GS-BRAND-151: Brand baru yang tidak cocok search tidak muncul di tabel tersaring

54. Isi Search dengan `zeta`, tekan Enter
55. Klik [+ Brand]
56. Isi Brand Name `Omega Works {runId}` (D-27)
57. Klik [Submit]
58. Verifikasi toast sukses: "Success, brand has been created."
59. Verifikasi tabel tersaring tetap tidak menampilkan `Omega Works {runId}`
60. Kosongkan Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 44, 46, 47, 50, 64, 65 (satu sesi modal dengan Stay tercentang, prinsip 8 konvensi), lalu 56 (Stay dilepas sehingga Submit menutup form, sekaligus menjadi kejadian menutup form), lalu verifikasi tabel, lalu 151 (butuh pembukaan form kedua dari tabel yang sedang tersaring). Hanya dua kali [+ Brand] dibuka. Urutan ini menyimpang dari urutan TC sumber (44, 46, 47, 50, 56, 64, 65, 151) demi satu sesi modal.
- Asersi "Brand tampil di tabel" milik TC-GS-BRAND-44, 46, 47, 50, dan "Search menampilkan 1 baris" milik TC-GS-BRAND-65 ditaruh sesudah form ditutup (langkah 43 sampai 52) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung setelah Submit.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi) namun tetap satu kelas (Create sukses) dengan satu akun dan satu dataset; pemecahan hanya menambah login, hook, dan pembukaan form. Bagian sesudah TC-GS-BRAND-44 tetap bermakna bila satu Create gagal, karena tiap Create memakai nama sendiri.
- Panjang 120 karakter pada TC-GS-BRAND-44 dan TC-GS-BRAND-46 sudah termasuk suffix ` {runId}`; suffix tidak mengubah batas yang diuji.
- Nama D-11, D-12, dan D-13 bersuffix `{runId}-016` karena nama yang sama juga muncul di TC spec lain (Data Uji Dinamis D-11 sampai D-13 dipakai lebih dari satu TC).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 39, 43, 45, 47, 49, dan 51 (Search agar baris target tampil di halaman aktif pada tabel 10 per halaman), langkah 53 dan 60 (mengosongkan Search), serta langkah 19 dan 30 (memasang dan melepas intercept untuk TC-GS-BRAND-64).
- Langkah 3 (centang Stay) dan 34 (lepas centang Stay) mengatur mode sesi modal, bukan asersi TC.
