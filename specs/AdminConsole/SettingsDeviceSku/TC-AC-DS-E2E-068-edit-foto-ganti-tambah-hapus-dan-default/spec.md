---
id: TC-AC-DS-E2E-068-edit-foto-ganti-tambah-hapus-dan-default
title: "Edit SKU Berhasil: Tiga Field Sekaligus, Ganti Foto Default, dan Tambah Foto Kedua"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-200
  - TC-AC-DS-201
  - TC-AC-DS-202
coverage:
  web: automated
---

# Edit SKU Berhasil: Tiga Field Sekaligus, Ganti Foto Default, dan Tambah Foto Kedua

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti #29 (`HHR-ARC-100`, `HHR-ARC-200`), Brand (#27), file foto (#37).
- File foto: `foto-b.png` (300 KB) dan `foto-c.jpeg` (150 KB) dari Pre-setup #37.
- Jam server dan jam browser sinkron; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35, tidak diubah). Asersi Last Modified membandingkan dengan waktu yang dicatat sesudah aksi Save, toleransi satu menit.
- Pemulihan (pengecualian S-12 A-11; fixture BE pemulih dinyatakan di `suite.md`): hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` (nilai Pre-setup #29, Last Modified `28/09/26 14:40`) dan `HHR-ARC-100` (2 foto, foto kedua default, Last Modified `01/10/26 09:15`) ke nilai Pre-setup #29; fixture yang sama dijalankan sebagai langkah penghubung antar blok (langkah 20) dan menghapus entri Changelog buatan test bila memungkinkan. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bila fixture tidak dapat menghapusnya.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (pengecualian S-12 A-11, lihat Notes).
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 (ditandai di Notes).

## Test Steps


### TC-AC-DS-200: tiga field sekaligus

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Ubah Model/Type menjadi `H202`
3. Ubah Brand menjadi `Kinetia`
4. Ubah Range Type menjadi `Long Range`
5. Tunggu toast lama hilang otomatis
6. Klik `[Save]`
7. Verifikasi muncul toast sukses "Success, device SKU has been updated."
8. Verifikasi popup Edit tertutup
9. Verifikasi baris `HHR-ARC-200` menampilkan Model/Type `H202`
10. Verifikasi baris `HHR-ARC-200` menampilkan Brand `Kinetia`
11. Verifikasi hanya satu toast sukses yang tampil

### TC-AC-DS-201: ganti foto default

12. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`
13. Ganti foto kedua (default) dengan mengunggah `foto-c.jpeg` pada slot itu
14. Klik `[Save]`
15. Catat waktu saat ini sebagai T1
16. Verifikasi muncul toast sukses "Success, device SKU has been updated."
17. Verifikasi popup Edit tertutup
18. Verifikasi thumbnail baris `HHR-ARC-100` pada List menjadi `foto-c.jpeg`
19. Verifikasi Last Modified baris `HHR-ARC-100` berubah dari `01/10/26 09:15` ke T1 (toleransi satu menit)

### TC-AC-DS-202: tambah foto kedua

20. Pulihkan baris `HHR-ARC-200` ke nilai Pre-setup #29 lewat fixture BE (Last Modified `28/09/26 14:40`)
21. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
22. Unggah `foto-b.png` pada slot Photo kedua
23. Klik `[Save]`
24. Catat waktu saat ini sebagai T2
25. Verifikasi muncul toast sukses "Success, device SKU has been updated."
26. Verifikasi popup Edit tertutup
27. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
28. Verifikasi popup Edit menampilkan dua foto
29. Verifikasi foto pertama tetap default
30. Klik `✕` pada header popup Edit SKU
31. Verifikasi Last Modified baris `HHR-ARC-200` berubah dari `28/09/26 14:40` ke T2 (toleransi satu menit)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 20 memulihkan `HHR-ARC-200` karena TC-200 sudah mengubah Last Modified baris itu, sedangkan asersi "berubah dari `28/09/26 14:40`" TC-202 membutuhkan nilai awal (S-09; pemulihan Pre-setup oleh fixture BE, S-06). "Klik `✕`" menutup popup bersih.
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface.
- Temuan untuk QA: TC-201 dan TC-202 bergantung NC-02 (perubahan Photo termasuk perubahan nilai).
- Temuan untuk QA (S-12/S-06): baris Pre-setup #29 (`HHR-ARC-100`, `HHR-ARC-200`) dipakai sebagai target `[Save]` sesuai pengecualian S-12 A-11; fixture BE pemulih dinyatakan di `suite.md` dan memulihkan Last Modified serta nilai awal (idempotent, suite serial).
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
