---
id: TC-AC-DN-E2E-073-delete-blok-karena-unit-byo-bagian-2
title: "Delete Device Name Diblok: Unit BYO Lintas Company dan SKU Milik Distributor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-610
  - TC-AC-DN-611
coverage:
  web: automated
---

# Delete Device Name Diblok: Unit BYO Lintas Company dan SKU Milik Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Dinamis milik spec (di-seed di hook `before` lewat Fixture BE, #27; Category `Accessory`, Measurement `Unit`; dihapus di hook `after`): `Door Antenna BYO {runId}-073` tanpa SKU dengan satu unit BYO Hardware di Company C dan satu unit BYO TAG di Company E (TC-AC-DN-610); `Door Antenna Distributor {runId}-073` tanpa unit BYO dengan satu SKU lokal milik Distributor `Distributor Jaringan` (Pre-setup #9) tanpa SKU Principal (TC-AC-DN-611).
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE) untuk men-seed Device Name milik spec (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO; master Pre-setup #13 dan #14) dan menghapus sisanya di hook `after` bila spec berhenti di tengah.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-610: Delete Device Name tanpa SKU yang unit BYO-nya tersebar di dua Company Client ditolak dengan dialog blok

1. Ketik Search `Door Antenna BYO {runId}-073`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `Door Antenna BYO {runId}-073` lalu klik `Delete`
3. Verifikasi judul dialog blok "Cannot Delete Device Name"
4. Verifikasi body: daftar nama berisi bullet `Door Antenna BYO {runId}-073`
5. Verifikasi body: pesan alasan blok "This device name still has registered devices."
6. Verifikasi footer: hanya satu tombol `[OK]`
7. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
8. Verifikasi tidak ada toast
9. Klik `[OK]`
10. Verifikasi baris `Door Antenna BYO {runId}-073` tetap ada pada List
11. Klik nama `Door Antenna BYO {runId}-073`
12. Verifikasi dialog Detail: baris Company C menampilkan Total SKU `0` dan Total Stock `1`
13. Verifikasi dialog Detail: baris Company E menampilkan Total SKU `0` dan Total Stock `1`
14. Tutup dialog Detail lewat ikon `[X]`

### TC-AC-DN-611: Delete Device Name yang hanya memiliki satu SKU milik Distributor ditolak dengan dialog blok

15. Ganti isi kotak search dengan `Door Antenna Distributor {runId}-073`, tekan Enter
16. Klik ikon aksi pada kolom Actions baris `Door Antenna Distributor {runId}-073` lalu klik `Delete`
17. Verifikasi judul dialog blok "Cannot Delete Device Name"
18. Verifikasi body: daftar nama berisi bullet `Door Antenna Distributor {runId}-073`
19. Verifikasi body: pesan alasan blok "This device name still has SKUs."
20. Verifikasi footer: hanya satu tombol `[OK]`
21. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
22. Verifikasi tidak ada toast
23. Verifikasi baris `Door Antenna Distributor {runId}-073` tetap ada pada List
24. Klik `[OK]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 15 (Search target, R-16); langkah 14 dan 24 (menutup dialog Detail dan dialog blok).
- Record milik spec dipakai (bukan `Door Antenna` Pre-setup) supaya seed unit BYO dan SKU tidak mengubah data Pre-setup bersama (S-06); nama pada TC diganti nama bersuffix (S-12).
- Temuan untuk QA: Post Condition TC-AC-DN-610 dan 611 tidak punya langkah observasi di TC, sehingga tidak diasersi.
