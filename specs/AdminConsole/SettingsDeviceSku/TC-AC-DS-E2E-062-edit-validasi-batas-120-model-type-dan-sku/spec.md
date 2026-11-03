---
id: TC-AC-DS-E2E-062-edit-validasi-batas-120-model-type-dan-sku
title: "Edit SKU: Model/Type dan SKU Batas 120 dan 121 Karakter"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-213
  - TC-AC-DS-214
  - TC-AC-DS-215
  - TC-AC-DS-216
coverage:
  web: automated
---

# Edit SKU: Model/Type dan SKU Batas 120 dan 121 Karakter

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (dibaca untuk atribut seed, tidak diubah): pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Data milik spec (S-06, S-12), di-seed idempotent di hook `before` lewat sesi API aktor dan fixture BE yang disediakan tim FE/BE, dihapus di hook `after` (termasuk bila kodenya sudah berubah oleh Save): SKU `EDT-{runId}-062` (Device Name `UHF Handheld Reader`, Category `UHF Handheld`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0, 1 foto). Atribut menyamai SKU Pre-setup `HHR-ARC-200` yang digantikannya, sehingga SKU Pre-setup tidak berubah. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`.
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE; memuat nilai Pre-setup #25, #26, #27, dan #37 yang dirujuk di atas.

## Test Steps

1. Ketik Search `EDT-{runId}-062`, tekan Enter
2. Klik `⋯` pada baris `EDT-{runId}-062`, lalu pilih `Edit`

### TC-AC-DS-214: Model/Type 121 karakter

3. Ganti Model/Type dengan 121 karakter `M`
4. Verifikasi pesan inline "Max. 120 characters" tampil langsung pada Model/Type
5. Klik `[Save]`
6. Verifikasi Save diblok: popup Edit tetap terbuka
7. Ganti Model/Type dengan `H200`

### TC-AC-DS-216: SKU 121 karakter

8. Ganti SKU dengan 121 karakter `A`
9. Verifikasi pesan inline "Max. 120 characters" tampil langsung pada SKU
10. Klik `[Save]`
11. Verifikasi Save diblok: popup Edit tetap terbuka
12. Klik `✕` pada header popup Edit SKU
13. Verifikasi dialog Unsaved Changes tampil
14. Klik `[Leave]`
15. Verifikasi baris `EDT-{runId}-062` menampilkan Model/Type `H200` (nilai tersimpan TC-214 tidak berubah)
16. Verifikasi baris dengan SKU `EDT-{runId}-062` masih tampil (nilai tersimpan TC-216 tidak berubah)

### TC-AC-DS-213: Model/Type 120 karakter

17. Klik `⋯` pada baris `EDT-{runId}-062`, lalu pilih `Edit`
18. Ganti Model/Type dengan 120 karakter `M`
19. Verifikasi tidak ada pesan error pada Model/Type
20. Klik `[Save]`
21. Verifikasi muncul toast sukses "Success, device SKU has been updated."

### TC-AC-DS-215: SKU 120 karakter

22. Klik `⋯` pada baris `EDT-{runId}-062`, lalu pilih `Edit`
23. Ganti SKU dengan 120 karakter `A`
24. Verifikasi tidak ada pesan error pada SKU
25. Klik `[Save]`
26. Verifikasi muncul toast sukses "Success, device SKU has been updated."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: blok validasi yang diblokir (TC-214, TC-216) dijalankan sebelum blok yang menyimpan (TC-213, TC-215), mengikuti S-10; nilai tersimpan TC-214 dan TC-216 diasersi sesudah popup ditutup (langkah 14 dan sesudahnya).
- Langkah penghubung: langkah 1 (Search untuk menemukan baris milik spec, R-16), langkah 7 (mengembalikan Model/Type sebelum menutup form), dan langkah 12 sampai 14 (menutup form dirty, S-08).
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface. Nilai 120 karakter hasil Save TC-213 dan TC-215 ikut terhapus bersama SKU milik spec oleh hook `after`.
- Temuan untuk QA: TC-214 dan TC-216 tidak menyebut cara membuktikan "Save diblok"; spec mengasersi popup tetap terbuka.
- Temuan untuk QA (S-06/S-12): TC-213 sampai TC-216 menulis ke SKU Pre-setup `HHR-ARC-200`; spec memakai SKU milik spec `EDT-{runId}-062` berkonfigurasi sama (pengecualian S-12 A-11: spec 062, 063, dan 064 memakai SKU milik spec bersuffix untuk `[Save]`), sehingga SKU Pre-setup dan Last Modified-nya tidak berubah.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
