---
id: TC-FA-FAAM-E2E-200-total-assets-asset-value-fiscal-gerbang-dan-sort-filter
title: "Tab Total Assets: Gerbang No access, Pending, serta Sort-Filter-Search-Download Kolom Asset Value Fiscal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-826
  - TC-FA-FAAM-848
  - TC-FA-FAAM-827
  - TC-FA-FAAM-847
coverage:
  web: automated
---

# Tab Total Assets: Gerbang No access, Pending, serta Sort-Filter-Search-Download Kolom Asset Value Fiscal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Asset Value HO (Pre-setup #32) `assetValueHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AVHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`.
- Client `AutoDepreciation` (Pre-setup #37): salinan `Column Matrix Item` dengan `Asset Value (Commercial)` (`AST-2001` 15000000, `AST-2002` 0, `AST-2004` 5000000, `AST-2005` 20000000) dan `Asset Value (Fiscal)` (`AST-2001` 9000000, `AST-2002` 0, `AST-2004` 4000000, `AST-2005` 25000000; `AST-2003` dan `AST-2006` tanpa harga perolehan sehingga sel `Pending` bagi aktor berhak); `AST-2001`, `AST-2002` Group `Head Office`, `AST-2004`, `AST-2005` Group `Warehouse` (di luar hak Asset Value HO). Akun Asset Value HO dan Full Value Access pada client ini disediakan tim FE (lihat Temuan untuk QA).
- Data TC-FA-FAAM-848: `AST-2003` Group `Finance` (anak `Head Office`) sel `Pending` bagi Asset Value HO; `AST-2004`, `AST-2005`, `AST-2006` Group `Warehouse` sel `No access` bagi Asset Value HO.
- Data TC-FA-FAAM-847 (Pre-setup #37b, client `AutoDepreciation`): Asset Name `Pending Reason Item` tanpa Asset Class, Total Asset 3: `AST-4001` Group `Head Office` dengan Purchase Cost 8000000; `AST-4002` Group `Head Office` tanpa Purchase Cost; `AST-4003` Group `Warehouse` tanpa Purchase Cost. Fixture disediakan tim FE/BE (kunci fixture usulan `pendingReasonItem`).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Preferensi Setup Column tersimpan per akun (keputusan pemilik 2026-11-02), jadi centang kolom akun sebelumnya tidak terbawa ke akun berikutnya.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-826: Gerbang No access berlaku pada kedua kolom Asset Value

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik `[Save]`
3. Verifikasi `Asset Value (Commercial)`: `AST-2001` 15000000, `AST-2002` currency nol, `AST-2004` dan `AST-2005` `No access`
4. Verifikasi `Asset Value (Fiscal)`: `AST-2001` 9000000, `AST-2002` currency nol, `AST-2004` dan `AST-2005` `No access`
5. Verifikasi harga perolehan `AST-2005` tidak tampil bagi aktor tanpa hak
6. Hover sel `AST-2004` pada kolom `Asset Value (Commercial)`
7. Verifikasi tooltip `Requires View asset value access in this group.`
8. Hover sel `AST-2004` pada kolom `Asset Value (Fiscal)`
9. Verifikasi tooltip `Requires View asset value access in this group.`

### TC-FA-FAAM-848: Kolom Asset Value Pending pada Sort, Filter, Search, dan Download: Pending tepat sebelum No access, tidak cocok Filter dan Search, ditulis kosong

10. Klik header `Asset Value (Fiscal)` 1 kali
11. Verifikasi klik 1 (ascending): `AST-2002` (0), `AST-2001` (9000000), `AST-2003` (`Pending`), lalu `AST-2004`, `AST-2005`, `AST-2006` (`No access`) paling akhir
12. Klik header `Asset Value (Fiscal)` 1 kali lagi
13. Verifikasi klik 2 (descending): `AST-2001`, `AST-2002`, `AST-2003` (`Pending`) tepat sebelum ketiga baris `No access` yang tetap paling akhir
14. Klik Filter, isi `Asset Value (Fiscal)` Min `0` dan Max `99999999`, klik `[Apply]`
15. Verifikasi hanya `AST-2001` dan `AST-2002` tampil; `AST-2003` (`Pending`) dan baris `No access` tidak tampil
16. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
17. Klik Search, ketik `Pending`, tekan Enter
18. Verifikasi Title `No results found`
19. Verifikasi Description `Try adjusting your search or filter.`
20. Klik `(←)` pada kotak Search
21. Klik Download lalu `Download as CSV` dan buka berkas
22. Verifikasi berkas CSV kolom `Asset Value (Fiscal)`: `AST-2001` 9000000, `AST-2002` 0, `AST-2003` kosong, `AST-2004`, `AST-2005`, `AST-2006` teks `No access`
23. Verifikasi berkas CSV kolom `Asset Value (Commercial)`: `AST-2001` 15000000, `AST-2002` 0, `AST-2003` kosong, `AST-2004`, `AST-2005`, `AST-2006` teks `No access`; sel `Pending` tidak ditulis `Pending` maupun `-`
24. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-827: Sort, Filter, dan Search bekerja pada kolom Asset Value (Fiscal)

25. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`)
26. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
27. Klik header Actions (⋯), pilih `Setup Column...`, centang kedua kolom Asset Value, klik `[Save]`
28. Klik header `Asset Value (Fiscal)` 1 kali
29. Verifikasi klik 1 (ascending numerik): `AST-2002` (0), `AST-2004`, `AST-2001`, `AST-2005`, lalu baris `Pending` (`AST-2003`, `AST-2006`) di akhir
30. Klik header `Asset Value (Fiscal)` 1 kali lagi
31. Verifikasi klik 2 (descending): `AST-2005`, `AST-2001`, `AST-2004`, `AST-2002`, lalu baris `Pending` tetap di akhir
32. Klik header `Asset Value (Fiscal)` 1 kali lagi
33. Verifikasi klik 3: kembali ke default Last Updated Newest First
34. Klik Filter, amati field Asset Value
35. Verifikasi Filter Panel memuat satu field range `Min` dan `Max` untuk `Asset Value (Commercial)` dan satu untuk `Asset Value (Fiscal)`
36. Isi `Asset Value (Fiscal)` Min `5000000`, klik `[Apply]`
37. Verifikasi `Fiscal` Min 5000000: hanya `AST-2001` dan `AST-2005` tampil
38. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
39. Ketik Search teks nilai `Asset Value (Fiscal)` `AST-2001` sebagaimana tampil, tekan Enter
40. Verifikasi Search teks nilai Fiscal `AST-2001` menampilkan `AST-2001`
41. Klik `(←)` pada kotak Search, tutup popup Detail

### TC-FA-FAAM-847: Sel Asset Value Pending: tooltip alasan Purchase cost belum diisi atau Asset class belum diisi, prioritas alasan, dan No access mengalahkan Pending

42. Klik nama `Pending Reason Item`
43. Klik tab `Total Assets (3)`
44. Klik header Actions (⋯), pilih `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik `[Save]`
45. Hover sel `Pending` `AST-4001` pada kolom `Asset Value (Commercial)`
46. Verifikasi `AST-4001`, `AST-4002`, `AST-4003` menampilkan teks `Pending` (bukan `—`, bukan currency nol) pada `Asset Value (Commercial)` dan `Asset Value (Fiscal)`
47. Verifikasi tooltip `AST-4001` pada kolom `Asset Value (Commercial)`: `Asset class has not been set.` (Purchase Cost sudah ada)
48. Hover sel `Pending` `AST-4001` pada kolom `Asset Value (Fiscal)`
49. Verifikasi tooltip `AST-4001` pada kolom `Asset Value (Fiscal)`: `Asset class has not been set.`
50. Hover sel `Pending` `AST-4002` pada kolom `Asset Value (Commercial)`
51. Verifikasi tooltip `AST-4002` pada kolom `Asset Value (Commercial)`: `Purchase cost has not been set.` (prioritas alasan Purchase mengalahkan Asset Class)
52. Hover sel `Pending` `AST-4002` pada kolom `Asset Value (Fiscal)`
53. Verifikasi tooltip `AST-4002` pada kolom `Asset Value (Fiscal)`: `Purchase cost has not been set.`
54. Hover sel `Pending` `AST-4003` pada kolom `Asset Value (Commercial)`
55. Verifikasi tooltip `AST-4003` pada kolom `Asset Value (Commercial)`: `Purchase cost has not been set.`
56. Hover sel `Pending` `AST-4003` pada kolom `Asset Value (Fiscal)`
57. Verifikasi tooltip `AST-4003` pada kolom `Asset Value (Fiscal)`: `Purchase cost has not been set.`
58. Verifikasi tooltip sel `Pending` tidak memuat metode atau masa manfaat
59. Tutup popup Detail, klik tombol akun, pilih Logout
60. Login sebagai Asset Value HO (`assetValueHO_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_AVHO_PASSWORD`)
61. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Pending Reason Item`, klik tab `Total Assets (3)`
62. Klik header Actions (⋯), pilih `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik `[Save]`
63. Amati sel `AST-4001`, `AST-4002`, `AST-4003`
64. Verifikasi aktor `Asset Value HO`: `AST-4001` dan `AST-4002` (Head Office) tetap `Pending` dengan tooltip yang sama
65. Hover sel `AST-4003`
66. Verifikasi `AST-4003` (Warehouse) `No access`, bukan `Pending`
67. Verifikasi tooltip `Requires View asset value access in this group.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 826 dan 848 (Asset Value HO), lalu ganti akun ke Full Value Access untuk 827, lalu 847 (Full Value Access, kemudian ganti akun ke Asset Value HO untuk Expected e dan f) (S-07: ganti akun punya langkah eksplisit).
- Langkah penghubung: `[Clear Field]` dan `[Apply]` untuk menghapus filter; `(←)` pada Search; menutup popup Detail dan Logout sebelum ganti akun.
- TC-FA-FAAM-848 langkah 3 (mencentang kedua kolom) tidak diulang karena kolom sudah tercentang dari TC-FA-FAAM-826 dalam spec ini; popup Detail yang sama dipakai berulang (langkah 1 dan 2 TC tidak diulang).
- Hover `Pending` pada TC-FA-FAAM-847 langkah 4 dipecah per sel dan per kolom (langkah 45, 48, 50, 52, 54, 56) agar tooltip tiap sel diverifikasi.
- Temuan untuk QA:
  - Pre-setup #37 tidak memberi email akun Asset Value HO dan Full Value Access pada client `AutoDepreciation`; spec memakai akun yang disediakan tim FE.
  - TC-FA-FAAM-827 memuat Pre-setup #37 pada ACC; hanya Pre-setup #32e yang tertulis sebagai aktor, sedangkan TC-FA-FAAM-826 menyebut Pre-setup #32.
  - TC-FA-FAAM-848 menyebut `AST-2003` (Finance) `Pending` bagi Asset Value HO; spec menandai bahwa `AST-2003` tanpa Purchase Cost berada di Group `Finance` (anak `Head Office`) sebagai kebutuhan fixture.
  - Pre-setup #37b (Asset Name `Pending Reason Item`) baru muncul pada TC-FA-FAAM-847; kunci fixture belum ada dan disediakan tim FE/BE.
