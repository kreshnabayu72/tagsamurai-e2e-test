---
id: TC-GS-IMPORT-E2E-171-defense-in-depth-izin-dan-isolasi-plan-free-403-lock-409-isolasi-tenant
title: "Defense-in-depth: izin dan isolasi (plan Free 403, lock 409, isolasi tenant 404, Read Only 403, tanpa sesi 401, Create Missing Options 403)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-530
  - TC-GS-IMPORT-531
  - TC-GS-IMPORT-534
  - TC-GS-IMPORT-538
  - TC-GS-IMPORT-810
  - TC-GS-IMPORT-931
coverage:
  web: automated
---

# Defense-in-depth: izin dan isolasi (plan Free 403, lock 409, isolasi tenant 404, Read Only 403, tanpa sesi 401, Create Missing Options 403)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (plan Client Free) dan memakai draft Client A yang dibagikan ke seluruh admin; lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama:
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`: aktor pertama (TC-531, 534).
  - Import data (Read Only) Client A (Tono Hartono) `importRead_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_IMPORTRO_PASSWORD` (TC-538).
  - Import data (Read Only) Client C (Hari Wibowo) `importRead_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_IMPORTRO_PASSWORD` (TC-931).
  - Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTB_TC_PASSWORD` (TC-534 sebagai pemanggil lintas tenant, TC-810).
  - Total Control Client Free (Dewi Lestari) `totalControl_automated_qaTeam8@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTFREE_TC_PASSWORD` (TC-530).
  - Pelaku kedua (pemicu): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`, memakai sesi API untuk memulai sesi edit dan memegang kunci (TC-531; P-2). Draft Client C (TC-931) disiapkan oleh Total Control Client C lewat skrip fixture.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk setiap akun UI spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Klien HTTP yang mengirim request langsung ke server dengan token sesi akun aktor (Confirm Mapping, baca Staging Table, Remove, Create Missing Options), tanpa token, dan dengan token sesi kedaluwarsa; pengenal baris diambil dari respons pembacaan Staging Table. Asersi request langsung hanya respons server dan state data (butir 1 bagian 8b).
  - Fixture Admin Console untuk menaikkan plan Client Free ke Growth dan mengembalikannya ke Free.
  - Skrip fixture reset Client B dan Client Free ke tanpa draft, pemulihan draft dasar Client A (D-01, Kontrak Fixture R2), dan seeding draft Client C (D-79).
- Data Dinamis (milik spec ini): D-01 draft Brand 12 baris `pending` di Client A (Population: `Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`; nama literal karena asersi urutan baris; seeding idempotent, dipulihkan sebelum tiap TC); D-79 `user-login-shift-lembur.csv` (draft User Login Client C 3 baris: #1 dan #2 `error`, #3 `pending`).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): batalkan sesi edit Admin kedua Client A, kembalikan plan Client Free ke Free, pulihkan draft dasar Client A, hapus draft Client B dan Client C, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-531: Permintaan langsung saat kunci dipegang admin lain ditolak 409

1. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
2. Mulai sesi edit pada Row # 1 atas nama Admin kedua Client A lewat sesi API (kunci dipegang)
3. Ambil pengenal baris Row # 3 dari respons pembacaan Staging Table
4. Kirim permintaan Remove langsung ke server dengan token akun Total Control Client A untuk pengenal baris Row # 3
5. Verifikasi server menolak permintaan dengan 409 Conflict
6. Buka Global Settings > Import, pilih Sub-Tab Brand, lalu muat ulang halaman
7. Verifikasi Staging Metric Cards Total Rows 12
8. Verifikasi Row # 3 masih `Zebra Technologies`
9. Batalkan sesi edit Admin kedua Client A lewat sesi API (pemulihan)

### TC-GS-IMPORT-534: Isolasi tenant

10. Pulihkan draft dasar Client A D-01 dan reset Client B ke tanpa draft Tab Brand lewat skrip fixture
11. Kirim permintaan baca Staging Table Brand langsung ke server dengan token akun Total Control Client A dan ambil pengenal baris Row # 1
12. Kirim permintaan baca Staging Table Brand langsung ke server dengan token akun Total Control Client B
13. Verifikasi server menjawab permintaan baca Client B dengan status 200 OK
14. Verifikasi respons permintaan baca Client A (langkah 11) memuat 12 baris
15. Verifikasi respons permintaan baca Client B tidak memuat baris atau angka dari draft Client A
16. Kirim permintaan Remove langsung ke server dengan token akun Total Control Client B untuk pengenal baris Row # 1 milik draft Client A
17. Verifikasi server menolak permintaan dengan 404 Not Found
18. Muat ulang halaman Import > Brand pada sesi Total Control Client A
19. Verifikasi draft Client A masih 12 baris (kartu Total Rows 12)
20. Verifikasi Row # 1 `Acme Corp`

### TC-GS-IMPORT-538: Import data (Read Only) dapat membaca tetapi permintaan tulis ditolak 403

21. Pulihkan draft dasar Client A D-01 lewat skrip fixture
22. Ganti akun: logout, lalu login sebagai Import data (Read Only) Client A (Tono Hartono)
23. Buka Global Settings > Import, pilih Sub-Tab Brand
24. Verifikasi Staging Table menampilkan draft 12 baris
25. Verifikasi Staging Metric Cards Total Rows 12
26. Klik `[Changelog]`
27. Verifikasi modal `Changelog: Import` terbuka
28. Tutup modal Changelog
29. Ambil pengenal baris Row # 1 dari respons pembacaan Staging Table
30. Kirim permintaan Remove langsung ke server dengan token akun Import data (Read Only) untuk pengenal baris itu
31. Verifikasi server menolak permintaan dengan 403 Forbidden
32. Muat ulang halaman Import > Brand
33. Verifikasi draft masih 12 baris (kartu Total Rows 12)
34. Verifikasi Row # 1 `Acme Corp`

### TC-GS-IMPORT-931: Create Missing Options oleh Import data (Read Only) ditolak 403

35. Seed draft User Login Client C `user-login-shift-lembur.csv` (D-79) atas nama Total Control Client C lewat skrip fixture
36. Ganti akun: logout, lalu login sebagai Import data (Read Only) Client C (Hari Wibowo)
37. Kirim permintaan Create Missing Options untuk kategori "Shift: Invalid option" langsung ke server dengan token akun Import data (Read Only) Client C
38. Verifikasi server menolak permintaan dengan 403 Forbidden
39. Buka menu Import dari sidebar dengan akun yang sama
40. Klik Sub-Tab User Login
41. Verifikasi baris #1 dan #2 tetap berstatus `error`
42. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 1, Errors 2

### TC-GS-IMPORT-810: Permintaan tulis tanpa sesi yang valid ditolak 401

43. Ganti akun: logout, lalu login sebagai Total Control Client B (Bayu Santoso)
44. Reset Client B ke tanpa draft Tab Brand lewat skrip fixture
45. Buka Global Settings > Import, pilih Sub-Tab Brand
46. Kirim permintaan Confirm Mapping langsung ke server tanpa token sesi
47. Verifikasi server menolak permintaan dengan 401 Unauthorized
48. Kirim permintaan Confirm Mapping langsung ke server dengan token sesi yang sudah kedaluwarsa
49. Verifikasi server menolak permintaan dengan 401 Unauthorized
50. Muat ulang halaman Import > Brand
51. Verifikasi Dropzone tampil
52. Verifikasi Unsaved Banner tidak tampil

### TC-GS-IMPORT-530: Aksi tulis pada plan Free ditolak server

53. Ganti akun: logout, lalu login sebagai Total Control Client Free (Dewi Lestari)
54. Reset Client Free ke tanpa draft Tab Brand (plan Free) lewat skrip fixture
55. Kirim permintaan Confirm Mapping langsung ke server dengan token akun Total Control Client Free
56. Verifikasi server menolak permintaan dengan 403 Forbidden
57. Kirim permintaan baca Staging Table Brand langsung ke server dengan token akun Total Control Client Free
58. Verifikasi server menolak permintaan dengan 403 Forbidden
59. Naikkan plan Client Free ke Growth lewat fixture Admin Console
60. Buka Global Settings > Import, pilih Sub-Tab Brand
61. Verifikasi Dropzone tampil
62. Verifikasi Unsaved Banner tidak tampil
63. Kembalikan plan Client Free ke Free lewat fixture Admin Console

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (a) dengan request langsung ke server sebagai objek uji. Admin kedua hanya memicu kunci lewat sesi API (P-2); fixture Admin Console hanya memicu perubahan plan.
- Alasan melewati sekitar 35 langkah (63 langkah nominal): enam blok homogen (request langsung ke server dengan akun berbeda), semua satu kelas dan berdiri sendiri; urutan blok dikelompokkan per akun dengan langkah ganti akun eksplisit (langkah 22, 36, 43, 53) sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Blok plan Free (TC-530) diletakkan terakhir karena mengubah plan.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan draft dan reset (langkah 1, 10, 21, 35, 44, 54), pengambilan pengenal baris (langkah 3, 11, 29), pembukaan halaman dan Sub-Tab, pembatalan sesi edit (langkah 9), perubahan plan (langkah 59 dan 63), tutup modal (langkah 28), ganti akun. Asersi absence Unsaved Banner (langkah 52, 62) didahului Verifikasi Dropzone tampil sebagai anchor positif pada halaman yang sama; asersi absence isi respons Client B (langkah 15) didahului Verifikasi status 200 OK dan respons Client A memuat 12 baris (langkah 13 dan 14) sebagai pembuktian permintaan berhasil.
- Asersi pada request langsung hanya respons server dan state data (butir 1 bagian 8b); langkah muat ulang dan pembacaan UI sesudahnya mengamati state data (jumlah baris dan isi Row # 1), bukan perilaku FE atas respons.
- Temuan untuk QA:
  - TC-GS-IMPORT-531 langkah 1 memulai sesi edit lewat UI (`⋯` > Edit) atas nama Admin kedua Client A; spec memakai sesi API (P-2) karena hasil di sesi itu tidak diasersi.
  - TC-GS-IMPORT-530 dan TC-GS-IMPORT-810 tidak menyebut isi payload permintaan Confirm Mapping langsung (pengenal berkas sementara); payload disediakan klien HTTP tim FE.
  - TC-GS-IMPORT-538 Expected a dan b mengasersi UI (Staging Table, modal Changelog) di samping respons 403; kedua asersi presence dipertahankan karena merupakan Expected TC (bukan salinan perilaku FE atas request langsung).
  - TC-GS-IMPORT-931 menyebut draft disiapkan "oleh Total Control Client C" tanpa menyebut mekanismenya; spec men-seed lewat skrip fixture.
  - Post Condition TC-GS-IMPORT-530 (plan dikembalikan), TC-GS-IMPORT-531 (sesi edit dibatalkan), dan TC-GS-IMPORT-931 (tidak ada opsi dibuat; draft tidak berubah) dikerjakan langkah 63, 9, dan hook `after`; Post Condition TC-GS-IMPORT-931 dikonfirmasi oleh Expected b.
