---
id: TC-AC-DN-E2E-183-konkurensi-delete
title: "Konkurensi Delete: SKU atau Unit BYO Ditambah, Dihapus Admin Lain, dan Konfirmasi setelah Perubahan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-193
  - TC-AC-DN-194
  - TC-AC-DN-195
  - TC-AC-DN-574
  - TC-AC-DN-575
coverage:
  web: automated
---

# Konkurensi Delete: SKU atau Unit BYO Ditambah, Dihapus Admin Lain, dan Konfirmasi setelah Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Brand `Brand C`, Model/Type `Model X`. Nama dinamis dibentuk `<nama dasar> {runId}-183` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Antenna`); #16 pola Device Name inti; #22 unit BYO lewat fixture BE. Record Pre-setup #16 tidak menjadi target aksi (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk SKU dan unit BYO; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog. Semua record: Measurement `Unit`, Category `Antenna`, tanpa SKU dan tanpa unit BYO.

  | Kode | Nama | Aksi pelaku kedua | Dipakai oleh |
  |---|---|---|---|
  | R1 | `Delete SKU Race {runId}-183` | membuat SKU `DA-CX-A-{runId}-183` (Brand C/Model X) | TC-AC-DN-193 |
  | R2 | `Delete BYO Race {runId}-183` | menambah satu unit BYO tanpa SKU lewat fixture BE (Jalur B di Global Settings > Hardware) | TC-AC-DN-194 |
  | R3 | `Delete Hilang A {runId}-183` | menghapus R3 | TC-AC-DN-195 |
  | R4 | `Delete Hilang B {runId}-183` | menghapus R4 | TC-AC-DN-574 |
  | R5 | `Delete SKU Baru {runId}-183` | membuat SKU `DA-CX-B-{runId}-183` (Brand C/Model X) | TC-AC-DN-575 |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

### TC-AC-DN-193: Delete dibatalkan saat admin lain menambah SKU

1. Ketik Search `Delete SKU Race {runId}-183`, tekan Enter
2. Buka menu aksi pada baris `Delete SKU Race {runId}-183`, klik `Delete`
3. Maya Putri (sesi API) membuat SKU `DA-CX-A-{runId}-183` untuk Device Name `Delete SKU Race {runId}-183` hingga tersimpan
4. Klik `[Delete]` pada dialog konfirmasi
5. Verifikasi dialog blok berjudul "Cannot Delete Device Name" dengan bullet `Delete SKU Race {runId}-183`, pesan "This device name still has SKUs.", dan satu tombol `[OK]` menggantikan dialog konfirmasi
6. Verifikasi tidak ada toast tambahan
7. Klik `[OK]`
8. Verifikasi baris `Delete SKU Race {runId}-183` tetap ada pada List

### TC-AC-DN-194: Delete dibatalkan saat unit BYO ditambahkan

9. Ketik Search `Delete BYO Race {runId}-183`, tekan Enter
10. Buka menu aksi pada baris `Delete BYO Race {runId}-183`, klik `Delete`
11. Maya Putri (sesi API) menambahkan satu unit BYO tanpa SKU untuk `Delete BYO Race {runId}-183` lewat fixture BE hingga unit tersimpan
12. Klik `[Delete]` pada dialog konfirmasi
13. Verifikasi dialog blok berjudul "Cannot Delete Device Name" dengan bullet `Delete BYO Race {runId}-183`, pesan "This device name still has registered devices.", dan satu tombol `[OK]` menggantikan dialog konfirmasi
14. Verifikasi tidak ada toast tambahan
15. Klik `[OK]`
16. Verifikasi baris `Delete BYO Race {runId}-183` tetap ada pada List

### TC-AC-DN-195: Delete Device Name yang sudah dihapus admin lain

17. Ketik Search `Delete Hilang A {runId}-183`, tekan Enter
18. Buka menu aksi pada baris `Delete Hilang A {runId}-183`, klik `Delete`
19. Maya Putri (sesi API) menghapus Device Name `Delete Hilang A {runId}-183` hingga terhapus
20. Klik `[Delete]` pada dialog konfirmasi
21. Verifikasi toast netral "This device name is no longer available."
22. Verifikasi dialog tertutup
23. Verifikasi baris `Delete Hilang A {runId}-183` tidak ada pada List
24. Verifikasi tidak ada toast error "Error, failed to delete device name."

### TC-AC-DN-574: Konfirmasi Delete setelah Device Name dihapus sesi lain

25. Ketik Search `Delete Hilang B {runId}-183`, tekan Enter
26. Buka menu aksi pada baris `Delete Hilang B {runId}-183`, klik `Delete`
27. Maya Putri (sesi API) menghapus Device Name `Delete Hilang B {runId}-183` hingga terhapus
28. Klik `[Delete]` pada dialog konfirmasi
29. Verifikasi toast netral "This device name is no longer available."
30. Verifikasi dialog ditutup
31. Verifikasi List tidak memuat "Delete Hilang B {runId}-183"

### TC-AC-DN-575: Konfirmasi Delete setelah sesi lain membuat SKU

32. Ketik Search `Delete SKU Baru {runId}-183`, tekan Enter
33. Buka menu aksi pada baris `Delete SKU Baru {runId}-183`, klik `Delete`
34. Maya Putri (sesi API) membuat SKU `DA-CX-B-{runId}-183` untuk Device Name `Delete SKU Baru {runId}-183` hingga tersimpan
35. Klik `[Delete]` pada dialog konfirmasi
36. Verifikasi dialog blok berjudul "Cannot Delete Device Name" menggantikan dialog konfirmasi, memuat bullet `Delete SKU Baru {runId}-183` dan teks alasan SKU "This device name still has SKUs."
37. Verifikasi dialog memuat tombol `[OK]`
38. Verifikasi tidak ada toast tampil
39. Klik `[OK]`
40. Verifikasi baris `Delete SKU Baru {runId}-183` tetap ada di List

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah pemicu ditulis "... hingga ... tersimpan/terhapus" (R-20). Pembuatan SKU, penambahan unit BYO, dan penghapusan Device Name lewat sesi API adalah kemampuan yang disediakan tim FE/BE; TC menyebut jalur UI atau fixture BE.
- Langkah penghubung (S-03, R-16): langkah 1, 9, 17, 25, 32 (Search) menemukan baris record milik spec; langkah 7, 15, 39 menutup dialog blok sesuai TC.
- Anchor absence (8b butir 2): toast netral langkah 21 dan 29 menjadi anchor langkah 23 dan 31; langkah 24 (toast error) didahului toast netral langkah 21. Nama yang dicari absence bukan substring nama record lain (R-13).
- Record milik spec (S-06, S-12): R1 sampai R5 menggantikan `Door Antenna` dan `Cable Tester` Pre-setup #16 TC sumber. Tumpang tindih sumber: TC-AC-DN-193 dan TC-AC-DN-575 (SKU dibuat sesi lain sebelum konfirmasi), TC-AC-DN-195 dan TC-AC-DN-574 (record dihapus sesi lain sebelum konfirmasi) memiliki Expected hampir identik; tiap TC tetap satu spec ini dengan record sendiri.
- Urutan: mengikuti sourceTc; dialog blok (193, 194) sebelum penghapusan oleh sesi lain.
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R3): satu topik (konfirmasi Delete setelah state berubah), satu kelas harness, lima blok dengan record sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-193 dan TC-AC-DN-194 (tidak ada entri log Delete), TC-AC-DN-195 (tidak ada entri log Delete kedua), TC-AC-DN-574, TC-AC-DN-575 (tidak ada entri log Delete baru).
  - TC-AC-DN-194 langkah 3 mensyaratkan unit BYO "tanpa SKU" lewat fixture BE; sesi API Maya dipakai karena sumber memakai fixture BE, bukan UI.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-183` (S-12).
