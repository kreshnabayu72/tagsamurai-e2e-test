---
id: TC-AC-DN-E2E-174-guard-delete-setelah-penghapusan-relasi
title: "Guard Delete: Lolos setelah Unit BYO atau SKU Terakhir Dihapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-640
  - TC-AC-DN-641
coverage:
  web: automated
---

# Guard Delete: Lolos setelah Unit BYO atau SKU Terakhir Dihapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1, Brand `Brand C`, Model/Type `Model X`. Nama dinamis dibentuk `<nama dasar> {runId}-174` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement; #14 Pohon Category; #16 pola `Field Radio` dan `Door Antenna`; #18 pola Usage by Company Company E; #22 unit BYO dan SKU lewat fixture BE. Record Pre-setup #16 tidak menjadi target aksi (S-06).
- Data Dinamis (milik spec; dibuat lewat API atau fixture BE di hook `before`, dihapus di hook `after`; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Nama | Measurement | Category | Relasi | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Radio Guard {runId}-174` | `Box` | `Accessory` | tanpa SKU; 5 unit BYO Hardware di Company E (menyimpan ID Device Name); Total Stock 5 dari seeding | TC-AC-DN-640 |
  | R2 | `Antenna Guard {runId}-174` | `Unit` | `Antenna` | satu-satunya SKU `DA-CX-8-{runId}-174` (Brand C/Model X), tanpa unit BYO | TC-AC-DN-641 |

- Kemampuan teknis (disediakan tim FE/BE): fixture backend menghapus unit BYO R1 di Company E (dihapus Client di Global Settings > Hardware pada alur nyata).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DN-640: Unit BYO dihapus menurunkan Total Stock dan Delete lolos guard

1. Ketik Search `Radio Guard {runId}-174`, tekan Enter
2. Klik nama `Radio Guard {runId}-174`
3. Verifikasi baris Company E menampilkan badge `Client`, Total SKU `0`, dan Total Stock `5`
4. Klik icon `(✕)` pada dialog
5. Hapus kelima unit BYO `Radio Guard {runId}-174` di Company E lewat fixture BE hingga unit terhapus
6. Klik nama `Radio Guard {runId}-174`
7. Verifikasi tabel Usage menampilkan empty state "No usage data yet"
8. Klik icon `(✕)` pada dialog
9. Buka menu aksi pada baris `Radio Guard {runId}-174`, klik `Delete`
10. Verifikasi dialog konfirmasi `Delete Device Name` tampil dengan bullet `Radio Guard {runId}-174`
11. Verifikasi dialog blok `Cannot Delete Device Name` tidak tampil
12. Klik `[Cancel]` pada dialog
13. Verifikasi dialog tertutup
14. Verifikasi baris `Radio Guard {runId}-174` tetap ada pada List
15. Verifikasi tidak ada toast

### TC-AC-DN-641: Delete Device Name lolos guard setelah SKU terakhir dihapus

16. Ketik Search `Antenna Guard {runId}-174`, tekan Enter
17. Buka menu aksi pada baris `Antenna Guard {runId}-174`, klik `Delete`
18. Verifikasi dialog blok `Cannot Delete Device Name` tampil dengan bullet `Antenna Guard {runId}-174` dan pesan "This device name still has SKUs."
19. Klik `[OK]`
20. Klik sub-tab `Device SKU`
21. Ketik Search `DA-CX-8-{runId}-174`, tekan Enter
22. Buka menu aksi pada baris SKU, klik `Delete`, klik `[Delete]` pada dialog
23. Tunggu aksi selesai (SKU terhapus)
24. Klik sub-tab `Device Name`
25. Ketik Search `Antenna Guard {runId}-174`, tekan Enter
26. Buka menu aksi pada baris `Antenna Guard {runId}-174`, klik `Delete`
27. Verifikasi dialog konfirmasi `Delete Device Name` tampil dengan bullet `Antenna Guard {runId}-174`
28. Verifikasi dialog blok tidak tampil
29. Klik `[Cancel]` pada dialog
30. Verifikasi dialog tertutup
31. Verifikasi baris `Antenna Guard {runId}-174` tetap ada pada List dengan Brand `—`
32. Verifikasi baris `Antenna Guard {runId}-174` menampilkan Model/Type `—`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 16, 21, 25 (Search) menemukan baris target; langkah 4 dan 8 menutup dialog Detail; langkah 20 dan 24 memindah sub-tab; langkah 23 menunggu penghapusan SKU yang hasilnya tidak diasersi (8b butir 8).
- Record milik spec (S-06, S-12): R1 menggantikan `Field Radio` dan R2 menggantikan `Door Antenna` TC sumber; unit BYO dan SKU dihapus pada record milik spec, sehingga Pre-setup #16, #18, dan #22 tidak berubah.
- Urutan: mengikuti sourceTc. Dialog `Cancel` tidak menghapus apa pun sehingga tidak ada aksi menghapus data Device Name; R1 dan R2 dihapus fixture di hook `after`.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-640 (unit BYO terhapus, Device Name tetap tersimpan) dan TC-AC-DN-641 (SKU terhapus).
  - TC-AC-DN-640 butir b: empty state Usage "No usage data yet" diasersi sesuai TC; baris pembanding untuk R1 tidak tersedia pada dialog yang sama karena Company E satu-satunya baris.
