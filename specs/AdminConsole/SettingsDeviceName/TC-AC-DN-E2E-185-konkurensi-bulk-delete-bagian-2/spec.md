---
id: TC-AC-DN-E2E-185-konkurensi-bulk-delete-bagian-2
title: "Konkurensi Bulk Delete: Seleksi Campuran SKU dan Hapus dari Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-579
  - TC-AC-DN-580
  - TC-AC-DN-581
  - TC-AC-DN-625
coverage:
  web: automated
---

# Konkurensi Bulk Delete: Seleksi Campuran SKU dan Hapus dari Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2, Modified By `Maya P`) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Brand `Brand C`, Model/Type `Model X`. Nama dinamis dibentuk `<nama dasar> {runId}-185` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Antenna`); #16 dan #17 pola Device Name inti dan seed (tidak menjadi target aksi, S-06).
- Kemampuan teknis (disediakan tim FE/BE): sesi API Maya Putri untuk membuat SKU dan menghapus Device Name; membaca jumlah entri Changelog Device Name (baseline N0, S-12); seeding Device Name.
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk SKU). Seed tidak menulis entri Changelog. Semua record: Measurement `Unit`, Category `Antenna`, tanpa SKU dan tanpa unit BYO. Setiap blok memakai record sendiri dan dipilih lewat Search `{runId}-185`.

  | Blok | Record | Aksi pelaku kedua | TC |
  |---|---|---|---|
  | B1 | `Bulk Pintu A {runId}-185` (X), `Bulk Seed A {runId}-185` (Y) | menghapus Y | TC-AC-DN-579 |
  | B2 | `Bulk Pintu B {runId}-185` (X), `Bulk Seed B {runId}-185` (Y) | membuat SKU `BP-B-{runId}-185` (Brand C/Model X) untuk X | TC-AC-DN-580 |
  | B3 | `Bulk Pintu C {runId}-185` (X), `Bulk Kabel C {runId}-185` (Y) | membuat SKU `BP-C-{runId}-185` untuk X dan `BK-C-{runId}-185` untuk Y | TC-AC-DN-581 |
  | B4 | `Bulk Pintu D {runId}-185` (X), `Bulk Kabel D {runId}-185` (Y), `Bulk Seed D {runId}-185` (Z) | membuat SKU `BP-D-{runId}-185` untuk X dan `BK-D-{runId}-185` untuk Y, lalu menghapus Z | TC-AC-DN-625 |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

1. Ketik Search `{runId}-185`, tekan Enter

### TC-AC-DN-579: Salah satu item dihapus sesi lain

2. Catat jumlah entri Changelog Device Name sebagai N0 lewat kemampuan baca Changelog
3. Centang baris `Bulk Pintu A {runId}-185` dan `Bulk Seed A {runId}-185`, klik `Bulk Action` lalu `Delete`
4. Verifikasi dialog konfirmasi berjudul "Delete Device Names" memuat bullet `Bulk Pintu A {runId}-185` dan `Bulk Seed A {runId}-185`
5. Maya Putri (sesi API) menghapus Device Name `Bulk Seed A {runId}-185` hingga terhapus
6. Klik `[Delete]` pada dialog
7. Verifikasi dialog ditutup
8. Verifikasi toast sukses "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
9. Verifikasi baris `Bulk Pintu A {runId}-185` dan `Bulk Seed A {runId}-185` tidak ada lagi di List
10. Klik ikon Changelog, klik header kolom Date dua kali
11. Verifikasi modal "Changelog: Device Name" memuat jumlah entri N0 ditambah dua
12. Verifikasi dua entri teratas (Newest First) adalah entri Delete dengan Field `Device Name`: Old Value `Bulk Pintu A {runId}-185` New Value `—` Modified By `Budi S`, dan Old Value `Bulk Seed A {runId}-185` New Value `—` Modified By `Maya P`
13. Klik icon `(✕)` pada modal

### TC-AC-DN-580: Salah satu item mendapat SKU dari sesi lain

14. Centang baris `Bulk Pintu B {runId}-185` dan `Bulk Seed B {runId}-185`, klik `Bulk Action` lalu `Delete`
15. Maya Putri (sesi API) membuat SKU `BP-B-{runId}-185` untuk `Bulk Pintu B {runId}-185` hingga tersimpan
16. Klik `[Delete]` pada dialog
17. Verifikasi toast sukses "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
18. Verifikasi baris `Bulk Seed B {runId}-185` tidak ada lagi di List
19. Verifikasi baris `Bulk Pintu B {runId}-185` tetap ada di List

### TC-AC-DN-581: Seluruh item terpilih mendapat SKU dari sesi lain

20. Centang baris `Bulk Pintu C {runId}-185` dan `Bulk Kabel C {runId}-185`, klik `Bulk Action` lalu `Delete`
21. Maya Putri (sesi API) membuat SKU `BP-C-{runId}-185` untuk `Bulk Pintu C {runId}-185` dan SKU `BK-C-{runId}-185` untuk `Bulk Kabel C {runId}-185` hingga kedua SKU tersimpan
22. Klik `[Delete]` pada dialog
23. Verifikasi dialog blok berjudul "Cannot Delete Device Names" menggantikan dialog konfirmasi, memuat `Bulk Pintu C {runId}-185` (anotasi "1 SKU") dan `Bulk Kabel C {runId}-185` (anotasi "1 SKU")
24. Verifikasi dialog hanya memuat tombol `[OK]`
25. Verifikasi tidak ada toast tampil (bukan toast sukses "Success, device name has been deleted." dan bukan toast netral "This device name is no longer available.")
26. Klik `[OK]`
27. Verifikasi dialog tertutup
28. Verifikasi baris `Bulk Pintu C {runId}-185` dan `Bulk Kabel C {runId}-185` tetap ada di List dan tetap tercentang
29. Verifikasi Bulk Action Bar tetap tampil menunjukkan "2 Device Names selected"
30. Klik `Unselect All` pada Bulk Action Bar

### TC-AC-DN-625: Sebagian item mendapat SKU dan sebagian dihapus sesi lain

31. Centang baris `Bulk Pintu D {runId}-185`, `Bulk Kabel D {runId}-185`, dan `Bulk Seed D {runId}-185`, klik `Bulk Action` lalu `Delete`
32. Maya Putri (sesi API) membuat SKU `BP-D-{runId}-185` untuk `Bulk Pintu D {runId}-185` dan SKU `BK-D-{runId}-185` untuk `Bulk Kabel D {runId}-185`, lalu menghapus `Bulk Seed D {runId}-185` hingga SKU tersimpan dan record terhapus
33. Klik `[Delete]` pada dialog
34. Verifikasi dialog blok berjudul "Cannot Delete Device Names" menggantikan dialog konfirmasi, memuat hanya item in-use: `Bulk Pintu D {runId}-185` (anotasi "1 SKU") dan `Bulk Kabel D {runId}-185` (anotasi "1 SKU")
35. Verifikasi `Bulk Seed D {runId}-185` tidak tampil pada dialog
36. Verifikasi dialog hanya memuat tombol `[OK]`
37. Verifikasi tidak ada toast tampil (bukan toast sukses, bukan toast `T-08`, dan bukan toast netral "This device name is no longer available.")
38. Klik `[OK]`
39. Verifikasi dialog tertutup
40. Verifikasi baris `Bulk Pintu D {runId}-185` dan `Bulk Kabel D {runId}-185` tetap ada di List dan tetap tercentang
41. Verifikasi Bulk Action Bar tetap tampil
42. Klik `Unselect All` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah pemicu ditulis "... hingga ... tersimpan/terhapus" (R-20). Pembuatan SKU dan penghapusan Device Name lewat sesi API adalah kemampuan yang disediakan tim FE/BE.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-185`) menemukan baris record milik spec dan diasumsikan tetap aktif sepanjang spec; langkah 2 mencatat baseline Changelog; langkah 13 menutup modal; langkah 26 dan 38 menutup dialog blok sesuai TC; langkah 30 dan 42 membersihkan seleksi (S-09).
- Anchor absence (8b butir 2): toast sukses langkah 8 dan 17 menjadi anchor absence baris (langkah 9 dan 18); langkah 34 menjadi anchor langkah 35 pada dialog yang sama; langkah 23, 24 dan 34 mendahului asersi tanpa toast. Nama yang dicari absence tidak saling mengandung (R-13).
- Changelog (S-12, S-14): TC-AC-DN-579 butir d diasersi dengan selisih dua entri terhadap N0 dan dua entri teratas Newest First sebagai himpunan (Date berketelitian menit sehingga urutan dua entri tidak diasersi); selisih dua membuktikan tidak ada entri Delete kedua untuk `Bulk Seed A`.
- Record milik spec (S-06, S-12): record bersuffix menggantikan `Door Antenna`, `Cable Tester`, `Seed Device 001`, dan `Seed Device 002` Pre-setup #16 dan #17 TC sumber, karena TC menghapus record.
- TC-AC-DN-581 butir e dan TC-AC-DN-625 butir f ("tidak ada Device Name terhapus") adalah kesimpulan dari langkah 28 dan 40 (baris tetap ada); tidak ada pengamatan terpisah (S-03).
- Urutan: mengikuti sourceTc dengan TC-AC-DN-625 setelah TC-AC-DN-581 karena memakai kembali kemampuan dialog blok bulk.
- Ukuran spec (42 langkah, di atas smell 35 langkah, kode R3): satu topik (Bulk Delete dengan seleksi campuran saat state berubah), satu kelas harness, empat blok dengan record sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-579 (Delete tercatat satu kali selain via Changelog di atas), TC-AC-DN-580, TC-AC-DN-581, TC-AC-DN-625 (tidak ada entri log Delete dari sesi pertama).
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-185` (S-12).
