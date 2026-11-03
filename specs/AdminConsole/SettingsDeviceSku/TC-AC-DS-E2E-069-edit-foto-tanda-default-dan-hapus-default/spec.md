---
id: TC-AC-DS-E2E-069-edit-foto-tanda-default-dan-hapus-default
title: "Edit SKU Berhasil: Hapus Foto Bukan Default, Ganti Tanda Default, dan Hapus Foto Default Menaikkan Foto Tersisa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-203
  - TC-AC-DS-204
  - TC-AC-DS-205
coverage:
  web: automated
---

# Edit SKU Berhasil: Hapus Foto Bukan Default, Ganti Tanda Default, dan Hapus Foto Default Menaikkan Foto Tersisa

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti #29 (`HHR-ARC-100`).
- Jam server dan jam browser sinkron; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35, tidak diubah). Asersi Last Modified membandingkan dengan waktu yang dicatat sesudah aksi Save, toleransi satu menit.
- Pemulihan (pengecualian S-12 A-11; fixture BE pemulih dinyatakan di `suite.md`): hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-100` ke 2 foto dengan foto kedua default dan Last Modified `01/10/26 09:15` (Pre-setup #29); fixture yang sama dijalankan sebagai langkah penghubung antar blok (langkah 11 dan 20) dan menghapus entri Changelog buatan test bila memungkinkan. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bila fixture tidak dapat menghapusnya.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (pengecualian S-12 A-11, lihat Notes).
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 (ditandai di Notes).

## Test Steps


### TC-AC-DS-203: hapus foto bukan default

1. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`
2. Hapus foto pertama (bukan default)
3. Klik `[Save]`
4. Catat waktu saat ini sebagai T1
5. Verifikasi muncul toast sukses "Success, device SKU has been updated."
6. Verifikasi popup Edit tertutup
7. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`
8. Verifikasi popup Edit menampilkan satu foto (default)
9. Klik `✕` pada header popup Edit SKU
10. Verifikasi Last Modified baris `HHR-ARC-100` berubah dari `01/10/26 09:15` ke T1 (toleransi satu menit)

### TC-AC-DS-204: ganti tanda default

11. Pulihkan baris `HHR-ARC-100` ke nilai Pre-setup #29 lewat fixture BE
12. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`
13. Tandai foto pertama sebagai default
14. Klik `[Save]`
15. Catat waktu saat ini sebagai T2
16. Verifikasi muncul toast sukses "Success, device SKU has been updated."
17. Verifikasi popup Edit tertutup
18. Verifikasi thumbnail baris `HHR-ARC-100` pada List menjadi foto pertama
19. Verifikasi Last Modified baris `HHR-ARC-100` berubah dari `01/10/26 09:15` ke T2 (toleransi satu menit)

### TC-AC-DS-205: hapus foto default

20. Pulihkan baris `HHR-ARC-100` ke nilai Pre-setup #29 lewat fixture BE
21. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`
22. Hapus foto default (foto kedua)
23. Klik `[Save]`
24. Catat waktu saat ini sebagai T3
25. Verifikasi muncul toast sukses "Success, device SKU has been updated."
26. Verifikasi popup Edit tertutup
27. Verifikasi thumbnail baris `HHR-ARC-100` pada List adalah foto yang tersisa
28. Verifikasi Last Modified baris `HHR-ARC-100` berubah dari `01/10/26 09:15` ke T3 (toleransi satu menit)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 11 dan 20 memulihkan `HHR-ARC-100` karena tiap blok membutuhkan dua foto dan Last Modified awal (S-09; pemulihan Pre-setup oleh fixture BE, S-06). "Klik `✕`" menutup popup bersih.
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface. Khusus TC-205: foto tersisa menjadi default otomatis tanpa entri log Photo "Set as default" (Post Condition a) tidak diasersi.
- Temuan untuk QA: berkas foto `HHR-ARC-100` tidak diberi nama di Pre-setup #29, sehingga asersi "thumbnail menjadi foto pertama" dan "foto yang tersisa" membandingkan dengan foto yang dibaca dari popup Edit sebelum aksi; cara membandingkannya disediakan tim FE.
- Temuan untuk QA (S-12/S-06): baris Pre-setup #29 (`HHR-ARC-100`) dipakai sebagai target `[Save]` sesuai pengecualian S-12 A-11; fixture BE pemulih dinyatakan di `suite.md` dan memulihkan Last Modified serta nilai awal (idempotent, suite serial).
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
