---
id: TC-AC-DN-E2E-184-konkurensi-bulk-delete-bagian-1
title: "Konkurensi Bulk Delete: Item Menjadi Berelasi atau Dihapus Admin Lain saat Dialog Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-231
  - TC-AC-DN-232
  - TC-AC-DN-233
  - TC-AC-DN-234
coverage:
  web: automated
---

# Konkurensi Bulk Delete: Item Menjadi Berelasi atau Dihapus Admin Lain saat Dialog Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Brand `Brand C`, Model/Type `Model X`. Nama dinamis dibentuk `<nama dasar> {runId}-184` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Antenna`); #16 pola Device Name inti (tidak menjadi target aksi, S-06).
- Kemampuan teknis (disediakan tim FE/BE): sesi API Maya Putri untuk membuat SKU dan menghapus Device Name; membaca jumlah entri Changelog Device Name (baseline N0, S-12); seeding Device Name.
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk SKU). Seed tidak menulis entri Changelog. Semua record: Measurement `Unit`, Category `Antenna`, tanpa SKU dan tanpa unit BYO. Setiap blok memakai sepasang record sendiri dan dipilih lewat Search `{runId}-184`.

  | Blok | Record 1 | Record 2 | Aksi pelaku kedua | TC |
  |---|---|---|---|---|
  | B1 | `Bulk Kabel A {runId}-184` | `Bulk Pintu A {runId}-184` | membuat SKU `BP-A-{runId}-184` (Brand C/Model X) untuk Record 2 | TC-AC-DN-231 |
  | B2 | `Bulk Kabel B {runId}-184` | `Bulk Pintu B {runId}-184` | membuat SKU `BK-B-{runId}-184` untuk Record 1 dan SKU `BP-B-{runId}-184` untuk Record 2 | TC-AC-DN-232 |
  | B3 | `Bulk Kabel C {runId}-184` | `Bulk Pintu C {runId}-184` | menghapus Record 2 | TC-AC-DN-233 |
  | B4 | `Bulk Kabel D {runId}-184` | `Bulk Pintu D {runId}-184` | menghapus Record 1 dan Record 2 | TC-AC-DN-234 |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

1. Ketik Search `{runId}-184`, tekan Enter

### TC-AC-DN-231: Item menjadi berelasi SKU, item lain tetap terhapus

2. Catat jumlah entri Changelog Device Name sebagai N0 lewat kemampuan baca Changelog
3. Centang baris `Bulk Kabel A {runId}-184` dan `Bulk Pintu A {runId}-184`, klik `Bulk Action` lalu `Delete`
4. Maya Putri (sesi API) membuat SKU `BP-A-{runId}-184` untuk `Bulk Pintu A {runId}-184` hingga tersimpan
5. Klik `[Delete]` pada dialog `Delete Device Names`
6. Verifikasi toast sukses "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
7. Verifikasi baris `Bulk Kabel A {runId}-184` tidak lagi ada pada List
8. Verifikasi baris `Bulk Pintu A {runId}-184` tetap ada pada List
9. Verifikasi Bulk Action Bar hilang dan seleksi kembali ke 0
10. Klik ikon Changelog, klik header kolom Date dua kali
11. Verifikasi modal Changelog memuat jumlah entri N0 ditambah satu
12. Verifikasi entri teratas (Newest First) adalah entri Delete dengan Field `Device Name`, Old Value `Bulk Kabel A {runId}-184`, New Value `—`, Modified By `Budi S`
13. Klik icon `(✕)` pada modal

### TC-AC-DN-232: Seluruh item menjadi berelasi SKU

14. Centang baris `Bulk Kabel B {runId}-184` dan `Bulk Pintu B {runId}-184`, klik `Bulk Action` lalu `Delete`
15. Maya Putri (sesi API) membuat SKU `BK-B-{runId}-184` untuk `Bulk Kabel B {runId}-184` dan SKU `BP-B-{runId}-184` untuk `Bulk Pintu B {runId}-184` hingga kedua SKU tersimpan
16. Klik `[Delete]` pada dialog `Delete Device Names`
17. Verifikasi dialog blok bulk `D-05` berjudul "Cannot Delete Device Names" memuat `Bulk Kabel B {runId}-184` (anotasi "1 SKU") dan `Bulk Pintu B {runId}-184` (anotasi "1 SKU") serta satu tombol `[OK]`
18. Verifikasi tidak ada toast tampil
19. Klik `[OK]`
20. Verifikasi dialog blok tertutup
21. Verifikasi Bulk Action Bar tetap tampil dengan counter `2 Device Names selected`
22. Verifikasi baris `Bulk Kabel B {runId}-184` dan `Bulk Pintu B {runId}-184` tetap tercentang
23. Verifikasi baris `Bulk Kabel B {runId}-184` dan `Bulk Pintu B {runId}-184` tetap ada pada List
24. Klik `Unselect All` pada Bulk Action Bar

### TC-AC-DN-233: Salah satu item sudah dihapus admin lain

25. Centang baris `Bulk Kabel C {runId}-184` dan `Bulk Pintu C {runId}-184`, klik `Bulk Action` lalu `Delete`
26. Maya Putri (sesi API) menghapus Device Name `Bulk Pintu C {runId}-184` hingga terhapus
27. Klik `[Delete]` pada dialog `Delete Device Names`
28. Verifikasi toast sukses "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
29. Verifikasi dialog tertutup
30. Verifikasi baris `Bulk Kabel C {runId}-184` dan `Bulk Pintu C {runId}-184` tidak ada pada List
31. Verifikasi Bulk Action Bar hilang dan seleksi kembali ke 0

### TC-AC-DN-234: Seluruh item sudah dihapus admin lain

32. Centang baris `Bulk Kabel D {runId}-184` dan `Bulk Pintu D {runId}-184`, klik `Bulk Action` lalu `Delete`
33. Maya Putri (sesi API) menghapus Device Name `Bulk Kabel D {runId}-184` dan `Bulk Pintu D {runId}-184` hingga keduanya terhapus
34. Klik `[Delete]` pada dialog `Delete Device Names`
35. Verifikasi toast netral "This device name is no longer available."
36. Verifikasi dialog blok tidak tampil
37. Verifikasi tidak ada toast sukses
38. Verifikasi dialog tertutup
39. Verifikasi kedua baris tidak ada pada List
40. Verifikasi Bulk Action Bar hilang dan seleksi kembali ke 0

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah pemicu ditulis "... hingga ... tersimpan/terhapus" (R-20). Pembuatan SKU dan penghapusan Device Name lewat sesi API adalah kemampuan yang disediakan tim FE/BE.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-184`) menemukan baris record milik spec dan diasumsikan tetap aktif sepanjang spec; langkah 2 mencatat baseline Changelog; langkah 13 menutup modal; langkah 19 menutup dialog blok sesuai TC; langkah 24 membersihkan seleksi sebelum blok berikutnya (S-09).
- Anchor absence (8b butir 2): toast sukses langkah 6 dan 28 menjadi anchor absence baris (langkah 7 dan 30); toast netral langkah 35 menjadi anchor langkah 37 sampai 39. Nama yang dicari absence tidak saling mengandung (R-13).
- Changelog (S-12, S-14): TC-AC-DN-231 Expected e ("memuat entri Delete untuk Cable Tester dan tidak memuat entri Delete untuk Door Antenna") diasersi dengan selisih satu entri terhadap N0 dan entri teratas Newest First; selisih satu terhadap N0 lebih deterministik daripada hasil Search kosong, dan selisih satu membuktikan tidak ada entri Delete untuk record yang dilewati.
- Record milik spec (S-06, S-12): empat pasang record menggantikan `Cable Tester` dan `Door Antenna` Pre-setup #16 TC sumber, karena TC menghapus record; tiap blok memakai pasangan sendiri.
- Urutan: mengikuti sourceTc.
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R3): satu topik (Bulk Delete saat state berubah di tengah dialog), satu kelas harness, empat blok dengan record sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-232 dan TC-AC-DN-234 (tidak ada entri log Delete), TC-AC-DN-233 (log tidak ganda), TC-AC-DN-231 butir c.
  - TC-AC-DN-233 dan TC-AC-DN-234: TC memakai istilah "seleksi kembali ke 0" tanpa nilai counter; spec mengasersi Bulk Action Bar hilang dan seleksi 0 sebagai satu klausa komposit.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-184` (S-12).
