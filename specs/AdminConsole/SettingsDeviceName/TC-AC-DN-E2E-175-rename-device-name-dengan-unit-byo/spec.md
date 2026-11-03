---
id: TC-AC-DN-E2E-175-rename-device-name-dengan-unit-byo
title: "Rename Device Name yang Memiliki Unit BYO Hardware atau TAG Tidak Memutus Relasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-650
  - TC-AC-DN-651
coverage:
  web: automated
---

# Rename Device Name yang Memiliki Unit BYO Hardware atau TAG Tidak Memutus Relasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1. Nama dinamis dibentuk `<nama dasar> {runId}-175` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Box`, `Meter`; #14 Pohon Category (`Accessory`, `Tag`); #16 pola `Field Radio` dan `Tag Reel`; #18 pola Company E; #22 unit BYO lewat fixture BE. Record Pre-setup #16 tidak menjadi target aksi (S-06).
- Data Dinamis (milik spec; dibuat lewat API atau fixture BE di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Nama awal | Measurement | Category | Relasi | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Radio Rename {runId}-175` | `Box` | `Accessory` | tanpa SKU; 5 unit BYO Hardware di Company E (menyimpan ID Device Name) | TC-AC-DN-650 |
  | R2 | `Reel Rename {runId}-175` | `Meter` | `Tag` (TAG > NFC > Tag) | tanpa SKU; 3 unit BYO TAG di Company E (menyimpan ID Device Name) | TC-AC-DN-651 |

  Total Stock 5 dan 3 berasal dari seeding (8b butir 10).

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DN-650: Rename Device Name dengan unit BYO Hardware

1. Ketik Search `Radio Rename {runId}-175`, tekan Enter
2. Buka menu aksi pada baris `Radio Rename {runId}-175`, klik `Edit`
3. Kosongkan field Device Name lalu ketik "Radio Rename Pro {runId}-175"
4. Klik `[Save]`
5. Verifikasi toast sukses "Success, device name has been updated."
6. Ketik Search `Radio Rename Pro {runId}-175`, tekan Enter
7. Klik nama `Radio Rename Pro {runId}-175`
8. Verifikasi dialog Detail memuat satu baris `Company E` dengan badge `Client`, Total SKU `0`, dan Total Stock `5`
9. Klik icon `(✕)` pada dialog
10. Buka menu aksi pada baris `Radio Rename Pro {runId}-175`, klik `Delete`
11. Verifikasi dialog blok berjudul "Cannot Delete Device Name" tampil langsung dengan bullet `Radio Rename Pro {runId}-175` dan pesan "This device name still has registered devices.", hanya tombol `[OK]`
12. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil
13. Verifikasi tidak ada toast
14. Klik `[OK]`
15. Verifikasi baris `Radio Rename Pro {runId}-175` tetap ada pada List

### TC-AC-DN-651: Rename Device Name dengan unit BYO TAG

16. Ketik Search `Reel Rename {runId}-175`, tekan Enter
17. Buka menu aksi pada baris `Reel Rename {runId}-175`, klik `Edit`
18. Kosongkan field Device Name lalu ketik "Reel Rename Pro {runId}-175"
19. Klik `[Save]`
20. Verifikasi toast sukses "Success, device name has been updated."
21. Ketik Search `Reel Rename Pro {runId}-175`, tekan Enter
22. Klik nama `Reel Rename Pro {runId}-175`
23. Verifikasi dialog Detail memuat satu baris `Company E` dengan badge `Client`, Total SKU `0`, dan Total Stock `3`
24. Klik icon `(✕)` pada dialog
25. Buka menu aksi pada baris `Reel Rename Pro {runId}-175`, klik `Delete`
26. Verifikasi dialog blok berjudul "Cannot Delete Device Name" tampil langsung dengan bullet `Reel Rename Pro {runId}-175` dan pesan "This device name still has registered devices.", hanya tombol `[OK]`
27. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil
28. Verifikasi tidak ada toast
29. Klik `[OK]`
30. Verifikasi baris `Reel Rename Pro {runId}-175` tetap ada pada List

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 16, 21 (Search) menemukan baris target; langkah 9 dan 24 menutup dialog Detail.
- Record milik spec (S-06, S-12): R1 menggantikan `Field Radio` dan R2 menggantikan `Tag Reel` TC sumber; Pre-setup #16 tidak diubah, jadi pemulihan nama oleh baseline TC tidak diperlukan; R1 dan R2 dihapus fixture di hook `after`.
- Urutan: mengikuti sourceTc; tidak ada aksi menghapus data Device Name.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-650 dan TC-AC-DN-651 (nama dipulihkan, unit tetap tersimpan).
  - Expected "tidak ada toast" pada langkah 13 dan 28 berlaku sesudah dialog blok tampil; dialog blok menjadi anchor positif (8b butir 2).
