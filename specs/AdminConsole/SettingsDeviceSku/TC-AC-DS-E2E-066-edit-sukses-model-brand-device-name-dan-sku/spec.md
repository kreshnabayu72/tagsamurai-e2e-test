---
id: TC-AC-DS-E2E-066-edit-sukses-model-brand-device-name-dan-sku
title: "Edit SKU Berhasil: Model/Type, Brand, Device Name, dan Kode SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-192
  - TC-AC-DS-193
  - TC-AC-DS-194
  - TC-AC-DS-195
coverage:
  web: automated
---

# Edit SKU Berhasil: Model/Type, Brand, Device Name, dan Kode SKU

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti #29 (`HHR-ARC-200`), Device Name (#26), Brand (#27).
- Jam server dan jam browser sinkron; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35, tidak diubah). Asersi Last Modified membandingkan dengan waktu yang dicatat sesudah aksi Save, toleransi satu menit.
- Pemulihan (pengecualian S-12 A-11; fixture BE pemulih dinyatakan di `suite.md`): hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke nilai Pre-setup #29 (Device Name `UHF Handheld Reader`, SKU `HHR-ARC-200`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0, 1 foto, Last Modified `28/09/26 14:40`) dan menghapus entri Changelog buatan test bila memungkinkan. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bila fixture tidak dapat menghapusnya.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (pengecualian S-12 A-11, lihat Notes).
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 (ditandai di Notes).

## Test Steps


### TC-AC-DS-192: Model/Type

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Ubah Model/Type dari `H200` menjadi `H201`
3. Klik `[Save]`
4. Catat waktu saat ini sebagai T1
5. Verifikasi muncul toast sukses "Success, device SKU has been updated."
6. Verifikasi popup Edit tertutup
7. Verifikasi baris `HHR-ARC-200` menampilkan badge Model/Type `H201`
8. Verifikasi Last Modified baris `HHR-ARC-200` sama dengan T1 (toleransi satu menit)

### TC-AC-DS-193: Brand

9. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
10. Ubah Brand dari `Arcturus` menjadi `Veltrix`
11. Klik `[Save]`
12. Verifikasi muncul toast sukses "Success, device SKU has been updated."
13. Verifikasi popup Edit tertutup
14. Verifikasi baris `HHR-ARC-200` menampilkan badge Brand `Veltrix`

### TC-AC-DS-194: Device Name

15. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
16. Ubah Device Name dari `UHF Handheld Reader` menjadi `UHF Handheld Reader Pro`
17. Klik `[Save]`
18. Verifikasi muncul toast sukses "Success, device SKU has been updated."
19. Verifikasi popup Edit tertutup
20. Verifikasi baris `HHR-ARC-200` menampilkan Device Name `UHF Handheld Reader Pro`

### TC-AC-DS-195: kode SKU

21. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
22. Ubah SKU dari `HHR-ARC-200` menjadi `HHR-ARC-201`
23. Klik `[Save]`
24. Verifikasi muncul toast sukses "Success, device SKU has been updated."
25. Verifikasi popup Edit tertutup
26. Verifikasi baris dengan SKU `HHR-ARC-201` tampil
27. Verifikasi baris `HHR-ARC-200` tidak ada lagi

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Perubahan pada baris yang sama berlangsung berurutan; kode SKU diubah terakhir supaya baris tetap dikenali sebagai `HHR-ARC-200` pada blok sebelumnya, dan nilai awal field yang diubah tiap blok tetap sama dengan Pre-setup (Brand `Arcturus` pada TC-193, Device Name `UHF Handheld Reader` pada TC-194).
- Asersi absence baris `HHR-ARC-200` (langkah terakhir) memakai toast sukses sebagai anchor (bagian 8b butir 2).
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface.
- Temuan untuk QA (S-12/S-06): baris Pre-setup #29 (`HHR-ARC-200`) dipakai sebagai target `[Save]` sesuai pengecualian S-12 A-11; fixture BE pemulih dinyatakan di `suite.md` dan memulihkan Last Modified serta nilai awal (idempotent, suite serial).
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
