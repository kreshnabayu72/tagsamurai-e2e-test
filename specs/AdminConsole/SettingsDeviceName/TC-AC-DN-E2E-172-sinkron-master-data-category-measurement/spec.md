---
id: TC-AC-DN-E2E-172-sinkron-master-data-category-measurement
title: "Sinkronisasi Master Data: Unit BYO Hardware, Node Category, dan Measurement Baru/Dihapus pada Dropdown Create"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-527
  - TC-AC-DN-528
  - TC-AC-DN-529
  - TC-AC-DN-530
  - TC-AC-DN-531
coverage:
  web: automated
---

# Sinkronisasi Master Data: Unit BYO Hardware, Node Category, dan Measurement Baru/Dihapus pada Dropdown Create

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, node pohon Category. Nama dinamis dibentuk `<nama dasar> {runId}-172` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja kecuali dinyatakan): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Handheld Reader` > `UHF Handheld`; `Hardware` > `Smart Fixed Reader` > `Antenna`); #18 dan #22 pola Usage by Company dan unit BYO Company E.
- Data Dinamis (milik spec; dibuat lewat API atau fixture BE di hook `before`, dihapus di hook `after`; kemampuan seeding Device Name dan unit BYO disediakan tim FE/BE). Seed lewat API tidak menulis entri Changelog.

  | Kode | Data | Detail | Dipakai oleh |
  |---|---|---|---|
  | R1 | Device Name `Radio Lapangan {runId}-172` | Measurement `Box`, Category `Accessory`, tanpa SKU; 5 unit BYO Hardware di Company E (menyimpan ID Device Name); Total Stock awal 5 berasal dari seeding ini | TC-AC-DN-527 |
  | N1 | Node Category `Barcode Handheld {runId}-172` | dibuat langkah UI sebagai anak `Handheld Reader`, dihapus langkah UI pada TC-AC-DN-529 | TC-AC-DN-528, TC-AC-DN-529 |
  | M1 | Measurement `Roll {runId}-172` | Symbol `rl`, dibuat langkah UI, dihapus langkah UI pada TC-AC-DN-531 | TC-AC-DN-530, TC-AC-DN-531 |

- Kemampuan teknis (disediakan tim FE/BE): fixture backend menambah unit BYO Hardware ke R1 di Company E (aktivasi Jalur B oleh Client, bukan Hardware Stock).
- State global (S-06, pengecualian 2026-10-30): pohon Category Pre-setup #14 (node N1) dan master Measurement Pre-setup #13 (M1) berubah sementara; fixture backend yang disediakan tim FE/BE menghapus N1 dan M1 bila masih ada di hook `before` dan `after`. Efeknya (Last Modified dan audit trail modul Category dan Measurement) dicatat di sini. Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DN-527: Unit BYO Jalur B memperbarui Total Stock Company pada dialog Detail

1. Ketik Search `Radio Lapangan {runId}-172`, tekan Enter
2. Klik nama `Radio Lapangan {runId}-172`
3. Verifikasi dialog "Device Name Detail" menampilkan baris Company E dengan badge `Client`, Total SKU `0`, dan Total Stock `5`
4. Klik icon `(✕)` pada dialog
5. Tambahkan 2 unit BYO untuk `Radio Lapangan {runId}-172` pada Company E lewat fixture BE hingga unit tersimpan
6. Klik nama `Radio Lapangan {runId}-172`
7. Verifikasi baris Company E menampilkan Total Stock `7`
8. Verifikasi baris Company E menampilkan Total SKU `0`
9. Klik icon `(✕)` pada dialog

### TC-AC-DN-528: Node Category baru dapat dipilih pada dropdown Category form Create

10. Pada Category Sidebar, hover node `Handheld Reader`, klik aksi `+ Subcategory`
11. Ketik "Barcode Handheld {runId}-172", klik `[Submit]`
12. Klik `+ Device Name`
13. Klik field Category, expand `Hardware` dan `Handheld Reader`
14. Verifikasi pohon Category memuat "Barcode Handheld {runId}-172" di bawah "Handheld Reader" dan dapat dipilih
15. Verifikasi node "Handheld Reader" dapat dipilih
16. Verifikasi node "Hardware" tampil untuk konteks dan tidak dapat dipilih
17. Klik icon `(✕)` pada form Create Device Name

### TC-AC-DN-529: Node Category yang dihapus hilang dari opsi Category

18. Pada Category Sidebar, hover node "Barcode Handheld {runId}-172", klik aksi `Delete`, klik `[Delete]` pada dialog
19. Klik `+ Device Name`
20. Klik field Category, expand `Hardware` dan `Handheld Reader`
21. Verifikasi node "UHF Handheld" tetap tampil dan dapat dipilih
22. Verifikasi pohon Category tidak memuat "Barcode Handheld {runId}-172"
23. Klik icon `(✕)` pada form Create Device Name

### TC-AC-DN-530: Measurement baru muncul pada dropdown Measurement form Create

24. Buka halaman `Master Reference > Measurement`
25. Klik `[+ Unit]`
26. Ketik "Roll {runId}-172" pada Unit Name dan "rl" pada Symbol, klik `[Submit]`
27. Tunggu aksi selesai (Unit "Roll {runId}-172" tersimpan)
28. Buka halaman `Settings > Device > Device Name`, klik `+ Device Name`
29. Klik field Measurement
30. Verifikasi dropdown Measurement memuat opsi "Roll {runId}-172"
31. Verifikasi dropdown Measurement tetap memuat "Unit", "Meter", dan "Box"
32. Klik icon `(✕)` pada form Create Device Name

### TC-AC-DN-531: Measurement yang dihapus hilang dari dropdown Measurement

33. Buka halaman `Master Reference > Measurement`
34. Buka menu aksi pada baris "Roll {runId}-172", klik `Delete`, klik `[Delete]` pada dialog
35. Tunggu aksi selesai (Unit "Roll {runId}-172" terhapus)
36. Buka halaman `Settings > Device > Device Name`, klik `+ Device Name`
37. Klik field Measurement
38. Verifikasi dropdown Measurement memuat "Unit", "Meter", dan "Box"
39. Verifikasi dropdown Measurement tidak memuat opsi "Roll {runId}-172"
40. Klik icon `(✕)` pada form Create Device Name

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search) menemukan baris `Radio Lapangan {runId}-172`; langkah 4, 9, 17, 23, 32, 40 menutup dialog atau form yang bersih; langkah 24, 28, 33, 36 berpindah halaman; langkah 27 dan 35 (`Tunggu aksi selesai`) menunggu `[Submit]` dan `[Delete]` Measurement selesai sebelum halaman berpindah, tanpa `Verifikasi` karena hasilnya diverifikasi di dropdown Measurement.
- Record milik spec (S-06, S-12): `Radio Lapangan {runId}-172` menggantikan `Field Radio` Pre-setup #16 dan #18; Total Stock 5 dan 7 diturunkan dari seeding (8b butir 10). Node `Barcode Handheld {runId}-172` dan Measurement `Roll {runId}-172` dibuat dan dihapus oleh langkah spec; node `Barcode Handheld` dan Measurement `Roll` TC sumber diberi suffix.
- Urutan: mengikuti sourceTc; langkah 21 (anchor) ditulis sebelum langkah 22 (absence) dan langkah 38 sebelum 39 (8b butir 2), berbeda dari urutan butir a dan b TC-AC-DN-529 dan TC-AC-DN-531.
- TC-AC-DN-527 butir c (Total Stock menghitung seluruh unit BYO Company E untuk Device Name tersebut) adalah kesimpulan dari nilai `7` pada langkah 7 (5 unit seeding ditambah 2 unit); tidak ada pengamatan terpisah (S-03). Klausa "dihitung tanpa cache" teramati dari pembukaan ulang dialog (langkah 6 dan 7).
- Ukuran spec (40 langkah, di atas smell 35 langkah): satu topik (master data konsumen mengalir ke Device Name), satu dataset, satu kelas harness; tiap blok memakai data sendiri (`Radio Lapangan`, `Barcode Handheld`, `Roll`) dan bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-527 hingga TC-AC-DN-531.
  - TC-AC-DN-529 dan TC-AC-DN-531 membutuhkan node `Barcode Handheld {runId}-172` dan Measurement `Roll {runId}-172` dari TC sebelumnya (TC-AC-DN-528, TC-AC-DN-530); urutan spec memenuhinya dan fixture BE menyediakan cadangan bila blok sebelumnya gagal.
  - TC-AC-DN-528 hingga TC-AC-DN-531: TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-172` (S-12).
