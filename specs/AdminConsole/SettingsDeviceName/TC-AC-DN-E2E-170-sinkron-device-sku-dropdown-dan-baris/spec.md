---
id: TC-AC-DN-E2E-170-sinkron-device-sku-dropdown-dan-baris
title: "Sinkronisasi ke Device SKU: Create, Rename, dan Delete Device Name pada Dropdown dan Baris SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-518
  - TC-AC-DN-519
  - TC-AC-DN-520
  - TC-AC-DN-521
coverage:
  web: automated
---

# Sinkronisasi ke Device SKU: Create, Rename, dan Delete Device Name pada Dropdown dan Baris SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, node pohon Category, serta Brand `Brand A`, `Brand B` dan Model/Type `Model G1`, `Model G2`. Nama record dinamis dibentuk `<nama dasar> {runId}-170` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`); #15 Brand `Brand A`, `Brand B`; #22 sub-tab `Device SKU` sebagai konsumen dropdown Device Name. Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk SKU dan hasil rename; kemampuan seeding Device Name dan SKU disediakan tim FE/BE). Seed lewat API tidak menulis entri Changelog, sama seperti record Pre-setup #16.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Antena Gudang {runId}-170` | `Unit` | `Antenna` | tanpa SKU; dibuat langkah UI | TC-AC-DN-518 |
  | R2 | `Door Antenna {runId}-170` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-519 |
  | R3 | `Gate Antenna {runId}-170` | `Unit` | `Antenna` | `GA-G1-{runId}-170` (Brand A/Model G1) dan `GA-G2-{runId}-170` (Brand B/Model G2) | TC-AC-DN-520 |
  | R4 | `Hapus Antenna {runId}-170` | `Unit` | `Antenna` | tanpa SKU, tanpa unit BYO | TC-AC-DN-521 |

- Kemampuan teknis: mengetik, memilih opsi dropdown dan node pohon Category, membuka dropdown Device Name pada form Create Device SKU.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-518: Device Name baru muncul sebagai opsi dropdown Device Name form Create Device SKU

1. Klik `+ Device Name`
2. Ketik "Antena Gudang {runId}-170" pada field Device Name
3. Klik field Measurement lalu pilih `Unit`
4. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, device name has been created."
7. Klik sub-tab `Device SKU`
8. Klik `[+ SKU]`
9. Buka dropdown field Device Name
10. Verifikasi dropdown Device Name pada form Create Device SKU memuat opsi "Antena Gudang {runId}-170"
11. Klik icon `(✕)` pada form Create Device SKU
12. Klik sub-tab `Device Name`

### TC-AC-DN-519: Rename Device Name mengganti nama opsi dropdown

13. Ketik Search `Door Antenna {runId}-170`, tekan Enter
14. Buka menu aksi pada baris `Door Antenna {runId}-170`, klik `Edit`
15. Kosongkan field Device Name lalu ketik "Door Antenna Pro {runId}-170"
16. Klik `[Save]`
17. Verifikasi toast sukses "Success, device name has been updated."
18. Klik sub-tab `Device SKU`
19. Klik `[+ SKU]`
20. Buka dropdown field Device Name
21. Verifikasi dropdown Device Name memuat opsi "Door Antenna Pro {runId}-170"
22. Verifikasi dropdown Device Name tidak memuat opsi "Door Antenna {runId}-170"
23. Klik icon `(✕)` pada form Create Device SKU
24. Klik sub-tab `Device Name`

### TC-AC-DN-520: Rename Device Name memperbarui kolom Device Name pada baris SKU

25. Ketik Search `Gate Antenna {runId}-170`, tekan Enter
26. Buka menu aksi pada baris `Gate Antenna {runId}-170`, klik `Edit`
27. Kosongkan field Device Name lalu ketik "Gate Antenna Mk2 {runId}-170"
28. Klik `[Save]`
29. Tunggu aksi selesai (popup form tertutup)
30. Klik sub-tab `Device SKU`
31. Ketik Search `Gate Antenna Mk2 {runId}-170`, tekan Enter
32. Verifikasi baris SKU Brand A/Model G1 menampilkan Device Name "Gate Antenna Mk2 {runId}-170"
33. Verifikasi baris SKU Brand B/Model G2 menampilkan Device Name "Gate Antenna Mk2 {runId}-170"
34. Verifikasi tidak ada baris SKU milik Device Name tersebut yang masih menampilkan "Gate Antenna {runId}-170" sebagai nama Device Name
35. Klik sub-tab `Device Name`

### TC-AC-DN-521: Delete Device Name menghapus opsinya dari dropdown

36. Ketik Search `Hapus Antenna {runId}-170`, tekan Enter
37. Buka menu aksi pada baris `Hapus Antenna {runId}-170`, klik `Delete`
38. Verifikasi dialog konfirmasi berjudul "Delete Device Name" memuat bullet "Hapus Antenna {runId}-170"
39. Klik `[Delete]` pada dialog
40. Verifikasi toast sukses "Success, device name has been deleted."
41. Klik sub-tab `Device SKU`
42. Klik `[+ SKU]`
43. Buka dropdown field Device Name
44. Verifikasi dropdown Device Name memuat opsi "Antena Gudang {runId}-170"
45. Verifikasi dropdown Device Name tidak memuat opsi "Hapus Antenna {runId}-170"
46. Klik icon `(✕)` pada form Create Device SKU

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 13, 25, 31, 36 (Search) menemukan baris record milik spec; langkah 11, 23, 46 menutup form Create Device SKU yang bersih; langkah 12, 24, 35 mengembalikan sub-tab Device Name; langkah 29 menunggu penyimpanan Rename yang hasilnya tidak diasersi (8b butir 8). Kotak Search tidak dinyatakan TC setelah pindah sub-tab; langkah Search ditulis atomik.
- Record milik spec (S-06, S-12): R1 sampai R4 menggantikan `Antena Gudang` (dibuat TC), `Door Antenna`, `Gate Antenna`, dan `Door Antenna` TC sumber, yang menunjuk record Pre-setup #16; Pre-setup #16 tidak diubah. Nama dengan suffix diasersi dengan nilai bersuffix yang sama (R-06). Pada langkah 22 dan 34 nama yang dicari tidak menjadi substring dari nama hasil rename (R-13).
- Urutan: mengikuti sourceTc; Delete (TC-AC-DN-521) di akhir (S-10). Anchor absence langkah 22, 34, 45 adalah `Verifikasi` yang mendahuluinya pada surface yang sama (8b butir 2).
- Ukuran spec (46 langkah, di atas smell 35 langkah, kode R1): empat blok satu kelas harness memakai halaman yang sama (List Device Name dan form Create Device SKU); tiap blok memakai record sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; form Create Device SKU dibuka ulang per blok karena opsi dropdown dibaca setelah perubahan yang berbeda.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-518 (Category dan Measurement tersimpan), TC-AC-DN-519, TC-AC-DN-520 (relasi SKU tidak berubah), TC-AC-DN-521 (terhapus permanen).
  - TC-AC-DN-518 hingga TC-AC-DN-521: TC sumber memakai nama tanpa suffix dan menunjuk Pre-setup #16; spec memakai nama bersuffix `{runId}-170` (S-12).
  - TC-AC-DN-520: Expected tidak memuat Verifikasi toast Rename; toast pada langkah TC tidak diasersi.
