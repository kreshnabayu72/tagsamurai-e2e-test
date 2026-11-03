---
id: TC-AC-DS-E2E-063-edit-validasi-duplikat-format-sku-trim-dan-emoji
title: "Edit SKU: Duplikat SKU, SKU Sendiri, Format SKU, Trim Model/Type, dan Emoji"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-217
  - TC-AC-DS-218
  - TC-AC-DS-220
  - TC-AC-DS-221
  - TC-AC-DS-222
coverage:
  web: automated
---

# Edit SKU: Duplikat SKU, SKU Sendiri, Format SKU, Trim Model/Type, dan Emoji

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (dibaca saja, tidak diubah): SKU `HHR-ARC-100` (#29) sebagai kode yang sudah dipakai SKU lain pada TC-AC-DS-217 (hanya diketik, tidak pernah tersimpan); pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Data milik spec (S-06, S-12), di-seed idempotent di hook `before` lewat sesi API aktor dan fixture BE yang disediakan tim FE/BE, dihapus di hook `after`: SKU `EDT-{runId}-063` (Device Name `UHF Handheld Reader`, Category `UHF Handheld`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0, 1 foto). Atribut menyamai SKU Pre-setup `HHR-ARC-200` yang digantikannya, sehingga SKU Pre-setup tidak berubah. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`.
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE; memuat nilai Pre-setup #25, #26, #27, #29, dan #37 yang dirujuk di atas.

## Test Steps

1. Ketik Search `EDT-{runId}-063`, tekan Enter
2. Klik `⋯` pada baris `EDT-{runId}-063`, lalu pilih `Edit`

### TC-AC-DS-217: SKU duplikat

3. Ganti SKU dengan `HHR-ARC-100`, tunggu 1 detik tanpa pindah fokus
4. Verifikasi pesan inline "SKU already exists" tampil sekitar 500 ms setelah berhenti mengetik
5. Klik `[Save]`
6. Verifikasi Save diblok: popup Edit tetap terbuka

### TC-AC-DS-220: format SKU saat mengetik dan paste

7. Hapus teks SKU, lalu ketik `a_b c#d`
8. Verifikasi field SKU berisi `ABCD`
9. Verifikasi tidak ada pesan error pada SKU
10. Kosongkan field SKU, lalu tempel (paste) `ef_g h`
11. Verifikasi field SKU berisi `EFGH`

### TC-AC-DS-222: emoji pada Model/Type

12. Kosongkan Model/Type, lalu ketik `H😊2`
13. Verifikasi field Model/Type berisi `H2`
14. Verifikasi tidak ada pesan error pada Model/Type
15. Kosongkan Model/Type, lalu tempel (paste) `🔥Y`
16. Verifikasi field Model/Type berisi `Y`
17. Klik `✕` pada header popup Edit SKU
18. Verifikasi dialog Unsaved Changes tampil
19. Klik `[Leave]`
20. Verifikasi baris dengan SKU `EDT-{runId}-063` tampil dengan Model/Type `H200` (nilai tersimpan TC-217 tidak berubah)

### TC-AC-DS-218: SKU sama dengan nilai tersimpan

21. Klik `⋯` pada baris `EDT-{runId}-063`, lalu pilih `Edit`
22. Hapus teks SKU, lalu ketik ulang `EDT-{runId}-063`, tunggu 1 detik
23. Verifikasi field SKU berisi `EDT-{runId}-063`
24. Verifikasi tidak ada pesan "SKU already exists"
25. Klik `[Save]`
26. Verifikasi muncul toast info "No changes to save."

### TC-AC-DS-221: spasi tepi Model/Type dibuang

27. Klik `⋯` pada baris `EDT-{runId}-063`, lalu pilih `Edit`
28. Ganti Model/Type dengan `  H203  ` (dua spasi di awal dan akhir)
29. Klik `[Save]`
30. Verifikasi muncul toast sukses "Success, device SKU has been updated."
31. Verifikasi badge Model/Type baris `EDT-{runId}-063` menampilkan `H203` tanpa spasi tepi

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: validasi yang diblokir (TC-217, TC-220, TC-222) mendahului TC-218 dan TC-221 (S-10); nilai tersimpan TC-217 diasersi setelah popup ditutup. Format SKU (TC-220) dan Model/Type (TC-222) diketik pada form yang sama sebelum ditutup.
- Langkah penghubung: langkah 1 (Search untuk menemukan baris milik spec, R-16) dan langkah 17 sampai 19 (menutup form dirty, S-08). Anchor positif TC-218: langkah 23 memastikan field SKU berisi kode SKU milik spec sebelum asersi absence pesan "SKU already exists" (bagian 8b butir 2).
- Temuan untuk QA: TC-218 tidak menyatakan apakah popup menutup setelah toast "No changes to save."; spec mengasumsikan menutup seperti TC-207 sehingga langkah 27 membuka popup lagi. TC-217 menyebut "sekitar 500 ms" tanpa toleransi; spec menunggu 1 detik sesuai langkah TC.
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface.
- Temuan untuk QA (S-06/S-12): TC-217, TC-218, TC-220, TC-221, dan TC-222 menulis ke SKU Pre-setup `HHR-ARC-200`; spec memakai SKU milik spec `EDT-{runId}-063` berkonfigurasi sama (pengecualian S-12 A-11: spec 062, 063, dan 064 memakai SKU milik spec bersuffix untuk `[Save]`). Pada TC-218 kode yang diketik ulang adalah kode SKU milik spec, sehingga tidak dianggap duplikat terhadap dirinya sendiri. `HHR-ARC-100` pada TC-217 (nama literal Pre-setup, pengecualian S-12 A-11) hanya diketik dan tidak pernah tersimpan.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
