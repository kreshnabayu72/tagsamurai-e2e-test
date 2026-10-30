---
id: TC-GS-IMPORT-E2E-174-resilience-koneksi-terputus-saat-confirm-mapping-tab-ditutup-saat-modal
title: "Resilience: koneksi terputus saat Confirm Mapping, tab ditutup saat modal terbuka, gagal unduh Changelog, gagal memuat Changelog (Try Again)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-539
  - TC-GS-IMPORT-540
  - TC-GS-IMPORT-541
  - TC-GS-IMPORT-793
  - TC-GS-IMPORT-794
coverage:
  web: automated
---

# Resilience: koneksi terputus saat Confirm Mapping, tab ditutup saat modal terbuka, gagal unduh Changelog, gagal memuat Changelog (Try Again)

## Prerequisites

- Mode: FE+BE (backend nyata) dengan `Spectra.intercept` parsial di atas backend nyata. Bukan `Mode: mock`: asersi mengandalkan state server nyata (draft tidak tercipta, total draft tetap 12 baris, total entri Changelog sama dengan pembacaan sebelum aksi), sehingga pengecualian resilience `Mode: mock` (keputusan 2026-10-29) tidak dipakai.
- Suite serial (`parallel: false`): draft Import dibagikan ke seluruh admin satu client dan Changelog Import Client E dibagikan lintas spec (seed D-60); lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama:
  - Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTB_TC_PASSWORD`: aktor pertama (TC-539, 541).
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`: ganti akun eksplisit (TC-540).
  - Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`: ganti akun eksplisit (TC-793, 794).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk ketiga akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - `Spectra.intercept` di browser: memutus koneksi permintaan Confirm Mapping sebelum respons diterima (TC-539, 540), membalas status 500 pada permintaan Download Changelog (TC-793) dan pada permintaan data Changelog Import (TC-794). Intercept dilepas segera setelah pemicu (S-09).
  - Pengelolaan tab peramban: menutup tab dan membuka tab baru dalam sesi login yang sama (TC-541).
  - Skrip seed Changelog Import Client E 30 entri (D-60; entri ke-i bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Measurement, Position, Division, User Login, User Non Login) dan pembersihan entri hasil commit TC lain; General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC+7.
  - Kemampuan baca jumlah entri Changelog Import Client E (total entri, dibaca sebelum aksi sebagai N untuk `Verifikasi` selisih).
  - Skrip fixture reset Client B ke tanpa draft Tab Brand dan pemulihan draft dasar Client A (D-01, Kontrak Fixture R2).
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga isi berkas literal sesuai Data Uji TC): `brand-12.csv` (isi seperti D-01, 12 baris Brand); `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp); D-01 draft Brand 12 baris `pending` Client A (Population, seeding idempotent); D-60 Changelog Import Client E 30 entri seed.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lepas semua intercept, hapus draft Client B, pulihkan draft dasar Client A, bersihkan seed D-60 Client E, tutup tab tambahan, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-539: Koneksi terputus saat Confirm Mapping tidak menyisakan draft atau baris

1. Reset Client B ke tanpa draft Tab Brand (aksi fixture)
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Klik `[Upload File]`
4. Pilih berkas `brand-12.csv`
5. Pasang intercept jaringan yang memutus koneksi permintaan Confirm Mapping sebelum respons diterima
6. Klik `[Confirm Mapping]`
7. Lepas intercept jaringan
8. Verifikasi toast error persisten: "Connection problem. Please try again."
9. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
10. Klik `[Cancel]` pada Modal Column Mapping
11. Muat ulang halaman Import > Brand
12. Verifikasi Dropzone tampil
13. Verifikasi Unsaved Banner tidak tampil
14. Verifikasi kartu Total Rows 0

### TC-GS-IMPORT-541: Menutup tab saat Modal Column Mapping terbuka tidak membuat draft

15. Reset Client B ke tanpa draft Tab Brand (aksi fixture)
16. Muat ulang halaman Import > Brand
17. Klik `[Upload File]`
18. Pilih berkas `brand-12.csv`
19. Verifikasi Modal Column Mapping terbuka
20. Tutup tab peramban
21. Buka tab baru dan buka halaman Global Settings > Import, pilih Sub-Tab Brand
22. Verifikasi Dropzone tampil
23. Verifikasi Unsaved Banner tidak tampil
24. Verifikasi kartu Total Rows 0

### TC-GS-IMPORT-540: Koneksi terputus saat Confirm Mapping pada kasus Append

25. Ganti akun: logout, lalu login sebagai Total Control Client A (Sari Dewi)
26. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
27. Buka Global Settings > Import, pilih Sub-Tab Brand
28. Klik `[Upload File]`
29. Pilih berkas `brand-6.csv`
30. Klik `[Append Records]` pada Dialog Append to Draft
31. Pasang intercept jaringan yang memutus koneksi permintaan Confirm Mapping sebelum respons diterima
32. Klik `[Confirm Mapping]`
33. Lepas intercept jaringan
34. Verifikasi toast error persisten: "Connection problem. Please try again."
35. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
36. Klik `[Cancel]` pada Modal Column Mapping
37. Muat ulang halaman Import > Brand
38. Verifikasi Staging Metric Cards Total Rows 12
39. Verifikasi Staging Metric Cards Ready to Import 12 (tidak bertambah 6 baris)

### TC-GS-IMPORT-793 dan TC-GS-IMPORT-794: Changelog Import Client E

40. Ganti akun: logout, lalu login sebagai Total Control Client E (Yoga Permana)
41. Seed Changelog Import Client E 30 entri (D-60) lewat skrip seed
42. Baca jumlah entri Changelog Import Client E sebagai N lewat kemampuan baca jumlah entri
43. Buka Global Settings > Import, pilih Sub-Tab Brand

#### TC-GS-IMPORT-793: Download Changelog gagal server

44. Klik `[Changelog]`
45. Pasang intercept jaringan yang membalas permintaan Download Changelog dengan status 500
46. Klik icon Download
47. Pilih "Download as CSV"
48. Lepas intercept jaringan
49. Verifikasi toast error: "Error, failed to download Changelog-Import."
50. Verifikasi tidak ada berkas yang terunduh
51. Tutup toast error
52. Tutup modal Changelog (`✕`)

#### TC-GS-IMPORT-794: Gagal memuat Changelog dan Try Again

53. Pasang intercept jaringan yang membalas permintaan data Changelog Import dengan status 500
54. Klik `[Changelog]`
55. Lepas intercept jaringan
56. Verifikasi modal menampilkan "Unable to load this data."
57. Verifikasi tombol `[Try Again]` tampil
58. Klik `[Try Again]`
59. Verifikasi tabel Changelog menampilkan entri dengan "Showing 1 - 10 of N items" dan selisih total terhadap N yang dibaca pada langkah 42 adalah 0

## Notes

- Mode: FE+BE dengan intercept parsial. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection (b) (koneksi terputus, tab ditutup, kegagalan unduh dan baca server); kegagalan dipaksa lewat `Spectra.intercept` dan menjadi objek uji, sehingga spec ini kelas ringan b tunggal untuk Confirm Mapping dan Changelog.
- Alasan melewati sekitar 35 langkah (59 langkah nominal): lima blok homogen (kegagalan jaringan atau server pada alur impor atau Changelog), semua satu kelas dan berdiri sendiri dengan reset di awal tiap blok. Urutan blok dikelompokkan per akun (Client B, Client A, Client E) dengan langkah ganti akun eksplisit (langkah 25 dan 40) sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` dan `####` memetakan langkah ke id TC granular. TC-GS-IMPORT-541 (tanpa intercept) diletakkan di antara blok Client B sebelum ganti akun.
- Langkah penghubung (tanpa `Verifikasi`): reset, seeding, dan pemulihan draft (langkah 1, 15, 26, 41), pembacaan N (langkah 42), pembukaan halaman dan Sub-Tab, melepas intercept (langkah 7, 33, 48, 55), menutup toast dan modal (langkah 51, 52), dan ganti akun (langkah 25 dan 40). Langkah 19 adalah `Verifikasi` tambahan di luar Expected TC-GS-IMPORT-541 yang membuktikan prasyarat TC (Modal Column Mapping terbuka sebelum tab ditutup). Langkah 12, 22 (Dropzone tampil) menjadi anchor positif sebelum asersi absence Unsaved Banner.
- Langkah 50 (tidak ada berkas terunduh) didahului langkah 49 (toast tampil) sebagai anchor positif yang terhubung ke pemicu.
- Temuan untuk QA:
  - TC-GS-IMPORT-539 dan TC-GS-IMPORT-540 menulis `[Cancel]` pada Modal Column Mapping tanpa dialog Unsaved Changes; spec menganggap tidak ada dropdown yang diubah dari auto-match sehingga modal langsung tertutup (PRD §4.1 Dialog Unsaved Changes: 0 perubahan = langsung tertutup).
  - TC-GS-IMPORT-541 tidak menyebut apakah sesi login bertahan saat tab ditutup dan tab baru dibuka; spec mengasumsikan sesi login yang sama.
  - Jumlah 30 baris adalah keadaan seed D-60 yang dijamin skrip seed (langkah 41), bukan total audit trail yang tumbuh; TC-GS-IMPORT-794 Expected menulis total 30 absolut, sedangkan spec mengasersi selisih 0 terhadap N yang dibaca sebelum aksi (langkah 42, 59; S-12).
  - TC-GS-IMPORT-794 membaca daftar entri dari server (seed D-60), sehingga tidak dapat `Mode: mock`; TC-GS-IMPORT-793 dan 794 bergantung pada seed Changelog Import Client E yang tidak boleh berbagi run dengan spec commit Client E tanpa pembersihan.
  - TC-GS-IMPORT-539 Expected a menyebut "mapping yang sudah diisi" tanpa menyebut apa yang diisi; spec mengasersi modal tetap terbuka dengan mapping hasil auto-match.
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
