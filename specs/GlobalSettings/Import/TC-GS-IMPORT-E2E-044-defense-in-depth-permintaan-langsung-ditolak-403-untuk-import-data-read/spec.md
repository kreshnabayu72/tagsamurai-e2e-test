---
id: TC-GS-IMPORT-E2E-044-defense-in-depth-permintaan-langsung-ditolak-403-untuk-import-data-read
title: "Defense-in-depth: Permintaan Langsung Ditolak 403 untuk Import data (Read Only), Read Only, dan Tanpa Capability (Confirm Mapping, Save, Remove, Bulk Delete, Discard, Import, Upload, Edit Session, Baca)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-35
  - TC-GS-IMPORT-36
  - TC-GS-IMPORT-37
  - TC-GS-IMPORT-38
  - TC-GS-IMPORT-39
  - TC-GS-IMPORT-40
  - TC-GS-IMPORT-43
  - TC-GS-IMPORT-601
  - TC-GS-IMPORT-604
  - TC-GS-IMPORT-606
coverage:
  web: automated
---

# Defense-in-depth: Permintaan Langsung Ditolak 403 untuk Import data (Read Only), Read Only, dan Tanpa Capability (Confirm Mapping, Save, Remove, Bulk Delete, Discard, Import, Upload, Edit Session, Baca)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Klien HTTP: spec mengirim permintaan langsung ke server dengan token sesi akun yang diuji. Token tiap akun diperoleh lewat login API yang disediakan tim FE/BE (mekanisme tidak tertulis di TC, PRD, atau LLD).
- Akun (Client A), password lewat env:
  - Import data (Read Only) Client A (Tono Hartono) `importRead_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_IMPORTRO_PASSWORD`. Login UI di hook `before` (TC-GS-IMPORT-35 sampai 40, 601); token yang sama dipakai untuk permintaan langsung.
  - Tanpa Capability Client A (Fajar Nugroho) `noCapability_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_NOCAP_PASSWORD` (TC-GS-IMPORT-43, hanya permintaan langsung dengan token).
  - Read Only Client A (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_RO_PASSWORD` (TC-GS-IMPORT-606, login UI lewat langkah ganti akun).
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD` (TC-GS-IMPORT-604, login UI lewat langkah ganti akun; hook `after` mengembalikan sesi ke akun ini).
  - Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A): draft D-01 dipulihkan ke kondisi Population oleh hook `beforeEach` suite; D-76 varian 1 dan berkas sementara disiapkan lewat skrip fixture oleh langkah 1:
  - D-01: draft Brand 12 baris `pending` dari `brand-12.csv` (nama literal Population: `Acme Corp` pada Row # 1).
  - D-76 varian 1: `created_at` draft dimundurkan 25 jam sehingga Unsaved Banner tampil (TC-GS-IMPORT-39; hanya seed backdate, bukan batas waktu yang diuji).
  - Berkas sementara hasil upload `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) oleh Total Control Client A, diunggah lewat fixture oleh langkah 1; pengenal berkas sementara dibaca dari respons upload fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Langkah "Buka menu Import dari sidebar" mengikuti TC dan memuat ulang halaman setelah permintaan langsung.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: setiap permintaan ditolak sehingga draft tidak berubah; hook `beforeEach` suite memulihkan draft D-01 sesuai Kontrak Fixture R2.

## Test Steps

### TC-GS-IMPORT-35: Confirm Mapping lewat permintaan langsung oleh Import data (Read Only)

1. Siapkan lewat skrip fixture: mundurkan `created_at` draft Brand D-01 Client A 25 jam (D-76 varian 1) dan unggah `brand-6.csv` oleh Total Control Client A untuk memperoleh pengenal berkas sementara dari respons upload, lalu muat ulang halaman Import
2. Kirim permintaan Confirm Mapping langsung ke server dengan token akun Import data (Read Only) Client A, memakai pengenal berkas sementara hasil upload `brand-6.csv` oleh Total Control Client A
3. Verifikasi server menolak permintaan dengan 403 Forbidden
4. Buka menu Import dari sidebar dengan akun yang sama
5. Verifikasi Staging Metric Cards tetap Total Rows 12
6. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
7. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-36: Save sesi edit lewat permintaan langsung oleh Import data (Read Only)

8. Ambil pengenal baris tetap `Row #` 1 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
9. Kirim permintaan Save baris #1 langsung ke server dengan token akun Import data (Read Only) Client A, mengubah Brand Name dari `Acme Corp` menjadi `Acme Corporation`
10. Verifikasi server menolak permintaan dengan 403 Forbidden
11. Buka menu Import dari sidebar dengan akun yang sama
12. Verifikasi Staging Metric Cards tetap Total Rows 12
13. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
14. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-37: Remove baris lewat permintaan langsung oleh Import data (Read Only)

15. Ambil pengenal baris tetap `Row #` 1 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
16. Kirim permintaan Remove baris #1 langsung ke server dengan token akun Import data (Read Only) Client A
17. Verifikasi server menolak permintaan dengan 403 Forbidden
18. Buka menu Import dari sidebar dengan akun yang sama
19. Verifikasi Staging Metric Cards tetap Total Rows 12
20. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
21. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-38: Bulk Delete lewat permintaan langsung oleh Import data (Read Only)

22. Ambil pengenal baris tetap `Row #` 1 dan `Row #` 2 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
23. Kirim permintaan Bulk Delete untuk baris #1 dan #2 langsung ke server dengan token akun Import data (Read Only) Client A
24. Verifikasi server menolak permintaan dengan 403 Forbidden
25. Buka menu Import dari sidebar dengan akun yang sama
26. Verifikasi Staging Metric Cards tetap Total Rows 12
27. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
28. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-39: Discard Draft lewat permintaan langsung oleh Import data (Read Only)

29. Kirim permintaan Discard Draft Brand langsung ke server dengan token akun Import data (Read Only) Client A
30. Verifikasi server menolak permintaan dengan 403 Forbidden
31. Buka menu Import dari sidebar dengan akun yang sama
32. Verifikasi Unsaved Banner tetap tampil
33. Verifikasi Staging Metric Cards tetap Total Rows 12
34. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
35. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-40: Import (commit) lewat permintaan langsung oleh Import data (Read Only)

36. Kirim permintaan Import (commit) langsung ke server dengan token akun Import data (Read Only) Client A
37. Verifikasi server menolak permintaan dengan 403 Forbidden
38. Buka menu Import dari sidebar dengan akun yang sama
39. Verifikasi Staging Metric Cards tetap Total Rows 12
40. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
41. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`
42. Verifikasi `[Import (12)]` tetap tampil tanpa status committing

### TC-GS-IMPORT-601: Upload File lewat permintaan langsung oleh Import data (Read Only)

43. Kirim permintaan Upload File langsung ke server dengan token akun Import data (Read Only) Client A, melampirkan berkas `brand-6.csv`
44. Verifikasi server menolak permintaan dengan 403 Forbidden
45. Buka menu Import dari sidebar dengan akun yang sama
46. Verifikasi Staging Table tetap berisi 12 baris berstatus `pending` dengan `Row #` 1 berisi `Acme Corp`
47. Verifikasi Total Rows 12

### TC-GS-IMPORT-43: Pembacaan Staging Table, Changelog, dan Download Template untuk akun Tanpa Capability

48. Kirim permintaan baca Staging Table Brand langsung ke server dengan token akun Tanpa Capability Client A
49. Verifikasi server menolak permintaan dengan 403 Forbidden
50. Verifikasi respons tidak memuat baris draft
51. Kirim permintaan baca Changelog Import langsung ke server dengan token akun Tanpa Capability Client A
52. Verifikasi server menolak permintaan dengan 403 Forbidden
53. Verifikasi respons tidak memuat entri log
54. Kirim permintaan Download Template Brand langsung ke server dengan token akun Tanpa Capability Client A
55. Verifikasi server menolak permintaan dengan 403 Forbidden
56. Verifikasi respons tidak berisi berkas template

### TC-GS-IMPORT-606: Remove baris lewat permintaan langsung oleh Read Only

57. Ganti akun: login UI sebagai Read Only Client A
58. Kirim permintaan Remove baris #1 langsung ke server dengan token akun Read Only Client A
59. Verifikasi server menolak permintaan dengan 403 Forbidden
60. Buka menu Import dari sidebar dengan akun yang sama
61. Verifikasi Staging Table tetap berisi 12 baris berstatus `pending` dengan `Row #` 1 berisi `Acme Corp`
62. Verifikasi Total Rows 12

### TC-GS-IMPORT-604: Memulai sesi edit lewat permintaan langsung oleh Import data (Read Only) tidak mengambil kunci

63. Kirim permintaan memulai sesi edit baris #1 langsung ke server dengan token akun Import data (Read Only) Client A
64. Verifikasi server menolak permintaan dengan 403 Forbidden
65. Ganti akun: login UI sebagai Total Control Client A pada sesi browser terpisah
66. Buka menu Import dari sidebar
67. Klik `[⋯]` pada baris #1
68. Pilih Edit
69. Verifikasi baris #1 menjadi input
70. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
71. Verifikasi dialog "Draft Is Being Edited" tidak tampil
72. Klik `[Cancel]`
73. Tutup sesi browser terpisah Total Control Client A

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a). Asersi pada langkah permintaan langsung hanya status respons dan state data; tidak ada perilaku FE yang diasersi dari permintaan itu.
- Spec memuat sekitar 73 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (permintaan langsung ke server oleh akun tanpa hak), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah muncul dari satu `Verifikasi` per klausa Expected dan pembacaan ulang state draft.
- Urutan TC-GS-IMPORT-604 dipertahankan di akhir karena membuka sesi edit Total Control; langkah 72 (`[Cancel]`) menutup sesi edit itu dan langkah 73 menutup sesi browser Total Control terpisah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 11, 18, 25, 31, 38, 45, 60 (muat ulang halaman Import untuk membaca state draft terbaru); langkah 8, 15, 22 (mengambil pengenal baris dari respons baca); langkah 57 dan 65 (ganti akun); langkah 72 dan 73; langkah 1 (seed fixture D-76 varian 1 dan berkas sementara, K-7).
- TC-GS-IMPORT-43 memakai token Tanpa Capability tanpa sesi UI; blok TC-GS-IMPORT-606 memakai sesi UI Read Only hanya untuk membaca state draft.
- Kelas campur (D-11): blok TC-GS-IMPORT-604 menjalankan sesi browser Total Control kedua yang beraksi (Edit) dalam spec kelas a. Belum ada id pengecualian: konteks kedua beraksi di spec kelas a; usulan aturan baru menunggu batch konvensi. Spec tidak dipecah; sesi kedua ditutup pada langkah 73.
- Temuan untuk QA:
  - Mekanisme memperoleh token sesi per akun dan pengenal berkas sementara hasil upload fixture tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-604 tidak menyebut langkah membuka kembali halaman dengan akun Import data (Read Only) sebelum sesi Total Control; spec mengikuti langkah TC.
  - Post Condition "Draft Brand tetap berisi 12 baris pending tanpa perubahan" pada TC-GS-IMPORT-35 sampai 40 dan 601, 606 diasersi lewat Expected b/c masing-masing; Post Condition TC-GS-IMPORT-604 setara dengan Expected b.
