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
- Data Dinamis (Client A, disiapkan lewat skrip fixture, dipulihkan ke kondisi Population sebelum tiap TC):
  - D-01: draft Brand 12 baris `pending` dari `brand-12.csv` (nama literal Population: `Acme Corp` pada Row # 1).
  - D-76 varian 1: `created_at` draft dimundurkan 25 jam sehingga Unsaved Banner tampil (TC-GS-IMPORT-39; hanya seed backdate, bukan batas waktu yang diuji).
  - Berkas sementara hasil upload `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) oleh Total Control Client A, diunggah lewat fixture sebelum TC-GS-IMPORT-35; pengenal berkas sementara dibaca dari respons upload fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Langkah "Buka menu Import dari sidebar" mengikuti TC dan memuat ulang halaman setelah permintaan langsung.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: setiap permintaan ditolak sehingga draft tidak berubah; hook `beforeEach` suite memulihkan draft D-01 sesuai Kontrak Fixture R2.

## Test Steps

### TC-GS-IMPORT-35: Confirm Mapping lewat permintaan langsung oleh Import data (Read Only)

1. Kirim permintaan Confirm Mapping langsung ke server dengan token akun Import data (Read Only) Client A, memakai pengenal berkas sementara hasil upload `brand-6.csv` oleh Total Control Client A
2. Verifikasi server menolak permintaan dengan 403 Forbidden
3. Buka menu Import dari sidebar dengan akun yang sama
4. Verifikasi Staging Metric Cards tetap Total Rows 12
5. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
6. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-36: Save sesi edit lewat permintaan langsung oleh Import data (Read Only)

7. Ambil pengenal baris tetap `Row #` 1 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
8. Kirim permintaan Save baris #1 langsung ke server dengan token akun Import data (Read Only) Client A, mengubah Brand Name dari `Acme Corp` menjadi `Acme Corporation`
9. Verifikasi server menolak permintaan dengan 403 Forbidden
10. Buka menu Import dari sidebar dengan akun yang sama
11. Verifikasi Staging Metric Cards tetap Total Rows 12
12. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
13. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-37: Remove baris lewat permintaan langsung oleh Import data (Read Only)

14. Ambil pengenal baris tetap `Row #` 1 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
15. Kirim permintaan Remove baris #1 langsung ke server dengan token akun Import data (Read Only) Client A
16. Verifikasi server menolak permintaan dengan 403 Forbidden
17. Buka menu Import dari sidebar dengan akun yang sama
18. Verifikasi Staging Metric Cards tetap Total Rows 12
19. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
20. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-38: Bulk Delete lewat permintaan langsung oleh Import data (Read Only)

21. Ambil pengenal baris tetap `Row #` 1 dan `Row #` 2 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
22. Kirim permintaan Bulk Delete untuk baris #1 dan #2 langsung ke server dengan token akun Import data (Read Only) Client A
23. Verifikasi server menolak permintaan dengan 403 Forbidden
24. Buka menu Import dari sidebar dengan akun yang sama
25. Verifikasi Staging Metric Cards tetap Total Rows 12
26. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
27. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-39: Discard Draft lewat permintaan langsung oleh Import data (Read Only)

28. Kirim permintaan Discard Draft Brand langsung ke server dengan token akun Import data (Read Only) Client A
29. Verifikasi server menolak permintaan dengan 403 Forbidden
30. Buka menu Import dari sidebar dengan akun yang sama
31. Verifikasi Unsaved Banner tetap tampil
32. Verifikasi Staging Metric Cards tetap Total Rows 12
33. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
34. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`

### TC-GS-IMPORT-40: Import (commit) lewat permintaan langsung oleh Import data (Read Only)

35. Kirim permintaan Import (commit) langsung ke server dengan token akun Import data (Read Only) Client A
36. Verifikasi server menolak permintaan dengan 403 Forbidden
37. Buka menu Import dari sidebar dengan akun yang sama
38. Verifikasi Staging Metric Cards tetap Total Rows 12
39. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
40. Verifikasi baris `Row #` 1 berstatus `pending` berisi `Acme Corp`
41. Verifikasi `[Import (12)]` tetap tampil tanpa status committing

### TC-GS-IMPORT-601: Upload File lewat permintaan langsung oleh Import data (Read Only)

42. Kirim permintaan Upload File langsung ke server dengan token akun Import data (Read Only) Client A, melampirkan berkas `brand-6.csv`
43. Verifikasi server menolak permintaan dengan 403 Forbidden
44. Buka menu Import dari sidebar dengan akun yang sama
45. Verifikasi Staging Table tetap berisi 12 baris berstatus `pending` dengan `Row #` 1 berisi `Acme Corp`
46. Verifikasi Total Rows 12

### TC-GS-IMPORT-43: Pembacaan Staging Table, Changelog, dan Download Template untuk akun Tanpa Capability

47. Kirim permintaan baca Staging Table Brand langsung ke server dengan token akun Tanpa Capability Client A
48. Verifikasi server menolak permintaan dengan 403 Forbidden
49. Verifikasi respons tidak memuat baris draft
50. Kirim permintaan baca Changelog Import langsung ke server dengan token akun Tanpa Capability Client A
51. Verifikasi server menolak permintaan dengan 403 Forbidden
52. Verifikasi respons tidak memuat entri log
53. Kirim permintaan Download Template Brand langsung ke server dengan token akun Tanpa Capability Client A
54. Verifikasi server menolak permintaan dengan 403 Forbidden
55. Verifikasi respons tidak berisi berkas template

### TC-GS-IMPORT-606: Remove baris lewat permintaan langsung oleh Read Only

56. Ganti akun: login UI sebagai Read Only Client A
57. Kirim permintaan Remove baris #1 langsung ke server dengan token akun Read Only Client A
58. Verifikasi server menolak permintaan dengan 403 Forbidden
59. Buka menu Import dari sidebar dengan akun yang sama
60. Verifikasi Staging Table tetap berisi 12 baris berstatus `pending` dengan `Row #` 1 berisi `Acme Corp`
61. Verifikasi Total Rows 12

### TC-GS-IMPORT-604: Memulai sesi edit lewat permintaan langsung oleh Import data (Read Only) tidak mengambil kunci

62. Kirim permintaan memulai sesi edit baris #1 langsung ke server dengan token akun Import data (Read Only) Client A
63. Verifikasi server menolak permintaan dengan 403 Forbidden
64. Ganti akun: login UI sebagai Total Control Client A pada sesi browser terpisah
65. Buka menu Import dari sidebar
66. Klik `[⋯]` pada baris #1
67. Pilih Edit
68. Verifikasi baris #1 menjadi input
69. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
70. Verifikasi dialog "Draft Is Being Edited" tidak tampil
71. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a). Asersi pada langkah permintaan langsung hanya status respons dan state data; tidak ada perilaku FE yang diasersi dari permintaan itu.
- Spec memuat sekitar 71 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (permintaan langsung ke server oleh akun tanpa hak), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah muncul dari satu `Verifikasi` per klausa Expected dan pembacaan ulang state draft.
- Urutan TC-GS-IMPORT-604 dipertahankan di akhir karena membuka sesi edit Total Control; langkah 71 (`[Cancel]`) menutup sesi edit itu.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 10, 17, 24, 30, 37, 44, 59 (muat ulang halaman Import untuk membaca state draft terbaru); langkah 7, 14, 21 (mengambil pengenal baris dari respons baca); langkah 56 dan 64 (ganti akun); langkah 71.
- TC-GS-IMPORT-43 memakai token Tanpa Capability tanpa sesi UI; blok TC-GS-IMPORT-606 memakai sesi UI Read Only hanya untuk membaca state draft.
- Temuan untuk QA:
  - Mekanisme memperoleh token sesi per akun dan pengenal berkas sementara hasil upload fixture tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-604 tidak menyebut langkah membuka kembali halaman dengan akun Import data (Read Only) sebelum sesi Total Control; spec mengikuti langkah TC.
  - Post Condition "Draft Brand tetap berisi 12 baris pending tanpa perubahan" pada TC-GS-IMPORT-35 sampai 40 dan 601, 606 diasersi lewat Expected b/c masing-masing; Post Condition TC-GS-IMPORT-604 setara dengan Expected b.
