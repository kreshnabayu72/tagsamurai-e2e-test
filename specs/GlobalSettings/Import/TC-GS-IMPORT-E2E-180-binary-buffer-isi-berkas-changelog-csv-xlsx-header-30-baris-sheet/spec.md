---
id: TC-GS-IMPORT-E2E-180-binary-buffer-isi-berkas-changelog-csv-xlsx-header-30-baris-sheet
title: "Binary buffer: isi berkas Changelog CSV/XLSX (header, 30 baris, sheet, mengikuti Search dan kolom) dan isi Download Template tanpa Custom Field Deactivated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-498
  - TC-GS-IMPORT-791
  - TC-GS-IMPORT-792
  - TC-GS-IMPORT-959
coverage:
  web: automated
---

# Binary buffer: isi berkas Changelog CSV/XLSX (header, 30 baris, sheet, mengikuti Search dan kolom) dan isi Download Template tanpa Custom Field Deactivated

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai seed Changelog Import Client E (D-60) yang tidak boleh berbagi run dengan spec commit Client E tanpa pembersihan, dan menonaktifkan Custom Field Client A; lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama:
  - Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`: aktor pertama (TC-498, 791, 792).
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`: ganti akun eksplisit (TC-959).
  - Pelaku kedua (pemicu): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`, memakai sesi API untuk menonaktifkan Custom Field `Shift` (TC-959); tidak ada sesi UI kedua karena hasil di sesi itu tidak diasersi (P-2).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun UI spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Pembaca berkas CSV (BOM, header, jumlah baris, isi sel) dan XLSX (nama sheet, jumlah sheet, isi sel) pada buffer unduhan.
  - Skrip seed Changelog Import Client E 30 entri (D-60): entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login; Data `[Imported] records imported, 0 duplicates ignored, 0 errors remaining` dengan [Imported] = i; Modified By `Yoga P` untuk i ganjil dan `Dimas A` untuk i genap; entri hasil commit TC lain dibersihkan. General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC+7.
  - Kemampuan baca jumlah entri Changelog Import Client E (total entri, dibaca sebelum aksi sebagai N untuk `Verifikasi` selisih).
  - Pemulihan konfigurasi kolom: hapus preferensi kolom Changelog Import di browser akun Total Control Client E (kemampuan disediakan tim FE; didaftarkan di `suite.md`).
  - Sesi API Admin kedua Client A untuk menonaktifkan dan mengaktifkan kembali Custom Field; skrip fixture pemulihan draft dasar (D-05 Client A, Kontrak Fixture R2).
- Data Dinamis (milik spec ini): D-60 Changelog Import Client E 30 entri seed; D-05 draft User Login 8 baris `pending` Client A dari `user-login-8.csv` (Population; seeding idempotent; Shift `Siang` Row # 1 dan 2, `Pagi` Row # 3, Overtime Hours `1.25` Row # 4; Custom Field Active lain `Shift Notes` Text Area, `Emergency Phone` Phone, `Join Date` Date); `shift-append.csv`: header First Name; Last Name; Email; Division; Access; Shift; 1 baris Oka, Wibowo, `oka.wibowo@example.com`, Engineering, Global Settings, Malam.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): aktifkan kembali Custom Field `Shift` Client A, hapus preferensi kolom Changelog Import di browser akun Total Control Client E, bersihkan seed D-60 Client E, pulihkan draft dasar Client A, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-498, TC-GS-IMPORT-791, TC-GS-IMPORT-792: Berkas Changelog Import Client E

1. Seed Changelog Import Client E 30 entri (D-60) lewat skrip seed
2. Baca jumlah entri Changelog Import Client E sebagai N lewat kemampuan baca jumlah entri
3. Buka Global Settings > Import, pilih Sub-Tab Brand
4. Klik `[Changelog]`

#### TC-GS-IMPORT-498: Download as CSV

5. Klik icon Download
6. Pilih "Download as CSV"
7. Verifikasi berkas `Changelog-Import.csv` terunduh
8. Verifikasi tidak ada toast sukses yang tampil
9. Buka berkas CSV yang terunduh pada pembaca buffer
10. Verifikasi baris header berisi kolom Date, Action, Data, dan Modified By
11. Verifikasi berkas memuat N baris data, selisih terhadap N yang dibaca pada langkah 2 adalah 0 (seluruh entri, bukan hanya 10 baris halaman pertama)
12. Verifikasi entri `Import User Non Login` tanggal 30 Sep 26 memuat Date `30 Sep 26`
13. Verifikasi entri `Import User Non Login` tanggal 30 Sep 26 memuat jam `10:00` sesuai Date Format dan Time Format General Settings

#### TC-GS-IMPORT-791: Download as XLSX

14. Klik icon Download
15. Pilih "Download as XLSX"
16. Verifikasi berkas `Changelog-Import.xlsx` terunduh
17. Verifikasi tidak ada toast sukses yang tampil
18. Buka berkas XLSX yang terunduh pada pembaca buffer
19. Verifikasi berkas memuat satu sheet bernama `Sheet1`
20. Verifikasi sheet memuat baris header Date, Action, Data, dan Modified By
21. Verifikasi sheet memuat N baris data, selisih terhadap N yang dibaca pada langkah 2 adalah 0

#### TC-GS-IMPORT-792: Download mengikuti Search dan kolom yang tampil

22. Ketik Search `import brand`, tekan Enter
23. Klik header kolom Actions (kosong) untuk membuka Column Visibility
24. Hilangkan centang kolom `Data`
25. Klik icon Download
26. Pilih "Download as CSV"
27. Verifikasi berkas `Changelog-Import.csv` terunduh
28. Buka berkas CSV yang terunduh pada pembaca buffer
29. Verifikasi baris header hanya memuat kolom Date, Action, dan Modified By
30. Verifikasi berkas memuat 5 baris data
31. Verifikasi seluruh baris data memiliki Action `Import Brand`
32. Kembalikan centang kolom `Data` agar tampil kembali dan klik `(←)` pada kotak Search, lalu tutup modal Changelog

### TC-GS-IMPORT-959: Download Template dan Modal Column Mapping hanya menawarkan Custom Field Active

33. Ganti akun: logout, lalu login sebagai Total Control Client A (Sari Dewi)
34. Pulihkan draft dasar Client A D-05 (User Login 8 baris `pending`) dan pastikan Custom Field `Shift` Active lewat skrip fixture
35. Buka Global Settings > Import, pilih Sub-Tab User Login
36. Nonaktifkan Custom Field `Shift` Client A atas nama Admin kedua Client A lewat sesi API
37. Tekan F5 pada halaman Import
38. Verifikasi header Staging Table tetap memuat kolom Shift tanpa lencana
39. Klik `[Download Template]` di Tab User Login
40. Buka berkas XLSX yang terunduh pada pembaca buffer dan baca header Sheet 1
41. Verifikasi header Sheet 1 memuat Emergency Phone, Join Date, Overtime Hours, dan Shift Notes
42. Verifikasi header Sheet 1 tidak memuat kolom Shift
43. Buka Sheet 2 `Field Limit`
44. Verifikasi tabel Sheet 2 memuat baris Emergency Phone, Join Date, Overtime Hours, dan Shift Notes
45. Verifikasi tabel Sheet 2 tidak memuat baris Shift
46. Klik `[Upload File]` di toolbar dan pilih berkas `shift-append.csv`
47. Klik `[Append Records]` pada Dialog Append to Draft
48. Verifikasi daftar Target Attribute di Modal Column Mapping memuat Custom Field Active Emergency Phone, Join Date, Overtime Hours, dan Shift Notes
49. Verifikasi daftar Target Attribute tidak memuat Shift
50. Klik `[Cancel]` pada Modal Column Mapping
51. Verifikasi draft tidak berubah: Staging Metric Cards Total Rows 8
52. Aktifkan kembali Custom Field `Shift` Client A atas nama Admin kedua Client A lewat sesi API (pemulihan)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: binary buffer (f); objek uji adalah isi berkas CSV/XLSX hasil unduhan Changelog dan template. Admin kedua hanya memicu penonaktifan Custom Field lewat sesi API (P-2).
- Alasan melewati sekitar 35 langkah (52 langkah nominal): empat blok homogen yang berbagi surface (satu unduhan atau lebih per blok), semua satu kelas binary buffer dan berdiri sendiri. Blok Changelog Client E (TC-498, 791, 792) berbagi satu modal Changelog dan satu seed D-60; blok TC-959 memakai ganti akun eksplisit ke Client A (langkah 33), sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` dan `####` memetakan langkah ke id TC granular. Pembagian TC lintas spec: Custom Field Deactivated pada Staging Table (presence) ada di spec lain (S6); spec ini hanya memuat sisi isi template dan Target Attribute.
- Langkah penghubung (tanpa `Verifikasi`): seeding (langkah 1, 34), pembacaan N (langkah 2), pembukaan halaman dan Sub-Tab, membuka Changelog (langkah 4), membuka berkas pada pembaca buffer, Search atomik (langkah 22), pengaturan kolom (langkah 23, 24), pemulihan kolom Data dan Search (langkah 32), ganti akun (langkah 33), penonaktifan dan pengaktifan Custom Field (langkah 36 dan 52). Asersi absence (langkah 8, 17, 42, 45, 49) didahului Verifikasi unsur lain pada surface yang sama sebagai pembanding (berkas terunduh; header atau baris Custom Field lain; daftar Target Attribute lain).
- Temuan untuk QA:
  - Jumlah 30 baris adalah keadaan seed D-60 yang dijamin skrip seed (langkah 1), bukan total audit trail yang tumbuh; TC-GS-IMPORT-498 Expected menulis 30 baris absolut, sedangkan spec mengasersi selisih 0 terhadap N yang dibaca sebelum aksi (langkah 2, 11, 21; S-12).
  - TC-GS-IMPORT-498 Expected d menyebut "entri Import User Non Login tanggal 30 Sep 26" sebagai satu baris; spec membaca baris itu menurut Action dan Date pada berkas CSV.
  - TC-GS-IMPORT-792 langkah 5 "Klik header kolom Actions (kosong)" membuka Column Visibility (NC-03); spec menuliskan maksudnya. Post Condition TC menyatakan kolom Data pada cache browser dikembalikan tampil; spec mengembalikannya pada langkah 32 sebagai pemulihan antar blok lewat UI dan pada hook `after` lewat penghapusan preferensi kolom, tanpa asersi (S-01).
  - TC-GS-IMPORT-959 Expected a mengasersi kolom Shift pada header Staging Table "tanpa lencana"; arti lencana (badge deactivated) tidak dirinci di TC.
  - TC-GS-IMPORT-959 menyebut Admin kedua menonaktifkan Custom Field `Shift` lewat UI; spec memakai sesi API (P-2).
  - Post Condition TC-GS-IMPORT-498, 791 "-"; TC-GS-IMPORT-959 (Custom Field dipulihkan) dikerjakan langkah 52 dan hook `after`.
