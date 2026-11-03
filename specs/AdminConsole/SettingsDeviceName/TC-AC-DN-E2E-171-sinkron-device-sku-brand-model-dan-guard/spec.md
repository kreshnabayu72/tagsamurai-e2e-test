---
id: TC-AC-DN-E2E-171-sinkron-device-sku-brand-model-dan-guard
title: "Sinkronisasi dari Device SKU: Brand/Model Terisi, Kembali ke Em Dash, Changelog Tidak Bertambah, dan Delete Diblok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-522
  - TC-AC-DN-523
  - TC-AC-DN-524
  - TC-AC-DN-525
coverage:
  web: automated
---

# Sinkronisasi dari Device SKU: Brand/Model Terisi, Kembali ke Em Dash, Changelog Tidak Bertambah, dan Delete Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1, Brand `Brand C`, Model/Type `Model X`, dan nilai valid field wajib lain form Create Device SKU (`skuFieldWajib`, disediakan tim FE). Nama record dinamis dibentuk `<nama dasar> {runId}-171` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Antenna`); #15 Brand `Brand C`; #19 riwayat Changelog (dipakai hanya lewat baseline jumlah entri). Record inti Pre-setup #16 tidak menjadi target aksi (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk SKU; kemampuan seeding disediakan tim FE/BE). Seed lewat API tidak menulis entri Changelog.

  | Kode | Nama | Measurement | Category | SKU awal | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-171` | `Unit` | `Antenna` | tanpa SKU; SKU `DA-CX-1-{runId}-171` (Brand C/Model X) dibuat langkah UI | TC-AC-DN-522, TC-AC-DN-523 |
  | R2 | `Antena Changelog {runId}-171` | `Unit` | `Antenna` | tanpa SKU; SKU `DA-CX-2-{runId}-171` dibuat langkah UI | TC-AC-DN-524 |
  | R3 | `Antena Guard {runId}-171` | `Unit` | `Antenna` | `DA-CX-1G-{runId}-171` (Brand C/Model X), tanpa unit BYO | TC-AC-DN-525 |

- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog Device Name sebelum dan sesudah aksi (baseline, S-12; 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DN-522: SKU baru mengisi kolom Brand dan Model/Type

1. Klik sub-tab `Device SKU`
2. Klik `[+ SKU]`
3. Pilih Device Name `Door Antenna {runId}-171`, Brand `Brand C`, Model/Type `Model X`, isi SKU code `DA-CX-1-{runId}-171` dan field wajib lain dengan nilai valid
4. Klik `[Submit]`
5. Tunggu aksi selesai (form tertutup)
6. Klik sub-tab `Device Name`
7. Ketik Search `Door Antenna {runId}-171`, tekan Enter
8. Verifikasi baris `Door Antenna {runId}-171` menampilkan Brand `Brand C` sebagai satu chip tanpa `+N more`
9. Verifikasi baris `Door Antenna {runId}-171` menampilkan Model/Type `Model X` sebagai satu chip tanpa `+N more`

### TC-AC-DN-523: SKU dihapus mengembalikan Brand dan Model/Type menjadi em dash

10. Klik sub-tab `Device SKU`
11. Ketik Search `DA-CX-1-{runId}-171`, tekan Enter
12. Buka menu aksi pada baris SKU, klik `Delete`, klik `[Delete]` pada dialog
13. Tunggu aksi selesai (SKU terhapus)
14. Klik sub-tab `Device Name`
15. Ketik Search `Door Antenna {runId}-171`, tekan Enter
16. Verifikasi baris `Door Antenna {runId}-171` menampilkan Brand `—`
17. Verifikasi baris `Door Antenna {runId}-171` menampilkan Model/Type `—`

### TC-AC-DN-524: Pembuatan SKU tidak menambah entri Changelog Device Name

18. Catat jumlah entri Changelog Device Name sebagai N0 lewat kemampuan baca Changelog
19. Klik ikon Changelog
20. Klik icon `(✕)` pada modal
21. Klik sub-tab `Device SKU`, klik `[+ SKU]`
22. Pilih Device Name `Antena Changelog {runId}-171`, Brand `Brand C`, Model/Type `Model X`, isi SKU code `DA-CX-2-{runId}-171` dan field wajib lain dengan nilai valid, klik `[Submit]`
23. Tunggu aksi selesai (form tertutup)
24. Klik sub-tab `Device Name`, klik ikon Changelog
25. Verifikasi modal "Changelog: Device Name" memuat jumlah entri sama dengan N0
26. Klik ikon Search
27. Verifikasi input Search pada modal memakai placeholder "Search by field or modified by"
28. Ketik `Antena Changelog {runId}-171` pada Search modal, tekan Enter
29. Verifikasi empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."
30. Klik icon `(✕)` pada modal

### TC-AC-DN-525: Device Name yang memiliki SKU diblok dari Delete

31. Ketik Search `Antena Guard {runId}-171`, tekan Enter
32. Buka menu aksi pada baris `Antena Guard {runId}-171`, klik `Delete`
33. Verifikasi dialog blok berjudul "Cannot Delete Device Name" langsung tampil memuat bullet "Antena Guard {runId}-171" dan teks "This device name still has SKUs."
34. Verifikasi dialog konfirmasi berjudul "Delete Device Name" tidak tampil
35. Verifikasi dialog hanya memuat tombol `[OK]`
36. Verifikasi dialog tidak memuat teks alasan unit terdaftar
37. Verifikasi tidak ada toast tampil
38. Klik `[OK]` pada dialog
39. Verifikasi dialog tertutup
40. Verifikasi baris `Antena Guard {runId}-171` tetap ada di List

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 7, 11, 15, 31 (Search) menemukan baris target; langkah 1, 6, 10, 14, 21, 24 memindah sub-tab; langkah 5, 13, 23 menunggu aksi yang hasilnya tidak diasersi (8b butir 8); langkah 18 mencatat baseline; langkah 19 dan 20 membuka lalu menutup modal Changelog sesuai langkah TC; langkah 26 membuka input Search modal.
- Record milik spec (S-06, S-12): R1 sampai R3 menggantikan `Door Antenna` Pre-setup #16 yang di TC dipakai ber-SKU dan tanpa SKU; Pre-setup #16 tidak diubah. TC-AC-DN-525 memakai R3 yang di-seed ber-SKU, bukan SKU hasil TC-AC-DN-523.
- Urutan: mengikuti sourceTc; Delete yang diblok (TC-AC-DN-525) di akhir. Asersi absence langkah 29 didahului langkah 25 pada surface yang sama (8b butir 2).
- Baseline Changelog (S-12): TC sumber menyebut "11 entri pada dua halaman"; spec membandingkan jumlah sesudah aksi dengan N0 dan tidak memakai angka absolut. Klausa "tidak memuat entri dengan Device Name" diasersi lewat Search (langkah 28 dan 29).
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R1): empat blok satu kelas harness pada dua halaman yang sama (List Device Name dan Device SKU); tiap blok memakai record sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-522, TC-AC-DN-523, TC-AC-DN-524 (tidak ada entri Changelog baru selain yang dibandingkan dengan N0), TC-AC-DN-525.
  - TC-AC-DN-522 hingga TC-AC-DN-525: nilai "field wajib lain" form Create Device SKU tidak dirinci TC; diisi nilai valid yang disediakan tim FE. TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-171`.
  - TC-AC-DN-524: placeholder "Search by field or modified by" hanya menyebut dua kolom representatif (cakupan Search modal: semua kolom kecuali Date, prd-conventions §9.1a, NC-11); empty state langkah 29 diasersi sesuai Expected TC karena SKU baru tidak menambah entri Changelog Device Name.
