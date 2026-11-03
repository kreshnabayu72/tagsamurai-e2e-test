---
id: TC-AC-DS-E2E-064-edit-validasi-port
title: "Edit SKU: Validasi Port Kosong, 0, 65536, 65535, dan Hanya Digit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-223
  - TC-AC-DS-224
  - TC-AC-DS-225
coverage:
  web: automated
---

# Edit SKU: Validasi Port Kosong, 0, 65536, 65535, dan Hanya Digit

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (dibaca untuk atribut seed, tidak diubah): pohon Category (#25), Device Name (#26), Brand (#27).
- Data milik spec (S-06, S-12), di-seed idempotent di hook `before` lewat sesi API aktor dan fixture BE yang disediakan tim FE/BE, dihapus di hook `after`: SKU `EDT-{runId}-064` (Device Name `Tunnel Scanner`, Category `Tunnel Reader`, Brand `Veltrix`, Model/Type `SF-0`, Hardware Type Smart Fixed Reader, Port `9090`, stok 0, 1 foto). Atribut menyamai SKU Pre-setup `SFR-ZERO-01` yang digantikannya, sehingga SKU Pre-setup tidak berubah. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`.
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE; memuat nilai Pre-setup #25, #26, dan #27 yang dirujuk di atas.

## Test Steps

1. Ketik Search `EDT-{runId}-064`, tekan Enter
2. Klik `⋯` pada baris `EDT-{runId}-064`, lalu pilih `Edit`

### TC-AC-DS-223: Port kosong dan 0

3. Hapus teks Port sampai kosong
4. Klik `[Save]`
5. Verifikasi pesan inline "Port must be at least 1" tampil pada Port kosong
6. Isi Port dengan `0`
7. Klik `[Save]`
8. Verifikasi pesan inline "Port must be at least 1" tampil pada Port `0`
9. Verifikasi popup Edit tetap terbuka
10. Klik `✕` pada header popup Edit SKU
11. Verifikasi dialog Unsaved Changes tampil
12. Klik `[Leave]`
13. Klik `⋯` pada baris `EDT-{runId}-064`, lalu pilih `Edit`
14. Verifikasi field Port berisi `9090` (Port tersimpan tidak berubah)

### TC-AC-DS-225: Port hanya menerima digit

15. Hapus Port, lalu ketik `7a-1.,2 ` karakter demi karakter
16. Verifikasi field Port berisi `712`
17. Verifikasi tidak ada pesan error pada Port
18. Kosongkan Port, lalu tempel (paste) `9x9`
19. Verifikasi field Port berisi `99`

### TC-AC-DS-224: Port 65536 dan 65535

20. Isi Port dengan `65536`
21. Klik `[Save]`
22. Verifikasi pesan inline "Port must be at most 65535" tampil
23. Verifikasi Save diblok: popup Edit tetap terbuka
24. Ubah Port menjadi `65535`
25. Klik `[Save]`
26. Verifikasi muncul toast sukses "Success, device SKU has been updated."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-225 dijalankan sebelum TC-224 supaya blok yang diblokir mendahului blok yang menyimpan (S-10); nilai Port tersimpan TC-223 diasersi setelah popup ditutup dan dibuka lagi (langkah 12 dan sesudahnya).
- Langkah penghubung: Search pada langkah 1 menemukan baris milik spec `EDT-{runId}-064` (R-16); langkah 10 sampai 12 menutup form dirty (S-08).
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface. Port `65535` hasil TC-224 ikut terhapus bersama SKU milik spec oleh hook `after`.
- Temuan untuk QA: TC-225 mengetik `7a-1.,2 ` (berakhir spasi) dan mengharapkan `712`; hasil bergantung penyaringan karakter non-digit saat mengetik.
- Temuan untuk QA (S-06/S-12): TC-223, TC-224, dan TC-225 menulis ke SKU Pre-setup `SFR-ZERO-01`; spec memakai SKU milik spec `EDT-{runId}-064` berkonfigurasi sama (pengecualian S-12 A-11: spec 062, 063, dan 064 memakai SKU milik spec bersuffix untuk `[Save]`), sehingga SKU Pre-setup dan Last Modified-nya tidak berubah.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
