---
id: TC-AC-DN-E2E-072-delete-blok-karena-unit-byo-bagian-1
title: "Delete Device Name Diblok karena Unit BYO: Hardware, TAG, dan Gabungan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-190
  - TC-AC-DN-191
  - TC-AC-DN-609
coverage:
  web: automated
---

# Delete Device Name Diblok karena Unit BYO: Hardware, TAG, dan Gabungan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja): #16 `Field Radio` (unit BYO Hardware di Company E) dan `Tag Reel` (unit BYO TAG di Company E); #22 unit BYO menyimpan ID Device Name (disediakan tim FE/BE lewat seed).
- Data Dinamis milik spec (di-seed di hook `before` lewat Fixture BE, #27): `Door Antenna {runId}-072` (Category `Accessory`, Measurement `Unit`, tanpa SKU) dengan satu unit BYO Hardware dan satu unit BYO TAG di Company E; dihapus di hook `after`.
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE) untuk men-seed Device Name milik spec (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO; master Pre-setup #13 dan #14) dan menghapus sisanya di hook `after` bila spec berhenti di tengah.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-190: Delete Device Name tanpa SKU yang masih punya unit BYO Hardware ditolak dengan dialog blok

1. Ketik Search `Field Radio`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `Field Radio` lalu klik `Delete`
3. Verifikasi judul dialog blok "Cannot Delete Device Name"
4. Verifikasi body: daftar nama berisi bullet `Field Radio`
5. Verifikasi body: pesan alasan blok unit BYO "This device name still has registered devices." (bukan pesan SKU)
6. Verifikasi footer: hanya satu tombol `[OK]`
7. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
8. Verifikasi tidak ada toast
9. Verifikasi baris `Field Radio` tetap ada pada List
10. Klik `[OK]`

### TC-AC-DN-191: Delete Device Name tanpa SKU yang masih punya unit BYO TAG ditolak dengan dialog blok

11. Ganti isi kotak search dengan `Tag Reel`, tekan Enter
12. Klik ikon aksi pada kolom Actions baris `Tag Reel` lalu klik `Delete`
13. Verifikasi judul dialog blok "Cannot Delete Device Name"
14. Verifikasi body: daftar nama berisi bullet `Tag Reel`
15. Verifikasi body: pesan alasan blok unit BYO "This device name still has registered devices." (bukan pesan SKU)
16. Verifikasi footer: hanya satu tombol `[OK]`
17. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
18. Verifikasi tidak ada toast
19. Verifikasi baris `Tag Reel` tetap ada pada List
20. Klik `[OK]`

### TC-AC-DN-609: Delete Device Name tanpa SKU yang memiliki unit BYO Hardware dan unit BYO TAG sekaligus ditolak dengan dialog blok

21. Ganti isi kotak search dengan `Door Antenna {runId}-072`, tekan Enter
22. Klik ikon aksi pada kolom Actions baris `Door Antenna {runId}-072` lalu klik `Delete`
23. Verifikasi judul dialog blok "Cannot Delete Device Name"
24. Verifikasi body: daftar nama berisi bullet `Door Antenna {runId}-072`
25. Verifikasi body: pesan alasan blok "This device name still has registered devices."
26. Verifikasi footer: hanya satu tombol `[OK]`
27. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
28. Verifikasi tidak ada toast
29. Verifikasi baris `Door Antenna {runId}-072` tetap ada pada List
30. Klik `[OK]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 11, 21 (Search target, R-16); langkah 10, 20, 30 (menutup dialog blok sebelum blok berikutnya).
- TC-AC-DN-609 memakai `Door Antenna {runId}-072` milik spec, bukan baris Pre-setup `Door Antenna`, supaya seed unit BYO tidak mengubah data Pre-setup bersama (S-06); nama pada TC diganti nama bersuffix (S-12).
- Temuan untuk QA: Post Condition ("record dan unit BYO tetap tersimpan", "tidak ada entri log baru") TC-AC-DN-190, 191, dan 609 tidak punya langkah observasi di TC, sehingga tidak diasersi.
