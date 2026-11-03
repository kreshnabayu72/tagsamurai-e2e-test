---
id: TC-AC-DS-E2E-026-local-registration-nonaktif-edit-dan-delete-sku-lokal
title: "Local Registration Nonaktif: Edit, Delete, dan Bulk Delete SKU Lokal Tetap Berjalan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-85
  - TC-AC-DS-596
coverage:
  web: automated
---

# Local Registration Nonaktif: Edit, Delete, dan Bulk Delete SKU Lokal Tetap Berjalan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Mandala Niaga, Local Registration nonaktif `totalControlDistOff_automated_{namaCompany}@qwertysystem.net` (Pre-setup #17), password `Spectra.env.AC_DS_DISTOFF_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30, SKU Distributor #31 (`MAN-LOC-01`). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data milik spec (hook `before`, lewat fixture BE yang disediakan tim BE/FE karena Distributor ini tidak dapat membuat SKU lewat UI saat Local Registration nonaktif; menggantikan `MAN-LOC-01` agar data Pre-setup tidak berubah, S-06): SKU lokal Distributor PT Mandala Niaga `OFF-A-{runId}-026` (Device Name `Asset TAG`, Category `Asset TAG`, Brand Distributor, Model/Type `MA-{runId}`, stok 0, 1 foto) untuk Edit lalu Delete, dan `OFF-B-{runId}-026` (atribut yang sama, Model/Type `MB-{runId}`) untuk Bulk Delete. Hook `after` menghapus keduanya bila masih ada lewat fixture BE.
- Env var `AC_DS_DISTOFF_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Status Local Registration nonaktif adalah konfigurasi tetap entitas uji dan tidak diubah spec.

## Test Steps

### TC-AC-DS-85: Edit dan Delete SKU lokal

1. Ketik Search `OFF-A-{runId}-026`, tekan Enter
2. Klik ⋯ baris `OFF-A-{runId}-026` lalu pilih `Edit`
3. Ubah Model/Type menjadi `MAN-X-{runId}`
4. Klik `[Save]`
5. Verifikasi toast sukses: "Success, device SKU has been updated."
6. Klik ⋯ baris `OFF-A-{runId}-026` lalu pilih `Delete`
7. Klik `[Delete]` pada dialog konfirmasi
8. Verifikasi toast sukses: "Success, device SKU has been deleted."
9. Verifikasi baris `OFF-A-{runId}-026` hilang dari List

### TC-AC-DS-596: Bulk Delete SKU lokal

10. Ganti isi kotak search dengan `OFF-B-{runId}-026`, tekan Enter
11. Centang checkbox baris `OFF-B-{runId}-026`
12. Klik `Bulk Action`
13. Pilih `Delete` pada overlay aksi
14. Verifikasi dialog berjudul "Delete SKU" dengan bullet `OFF-B-{runId}-026`, teks "Are you sure you want to delete it? This action cannot be undone.", serta tombol `[Cancel]` dan `[Delete]`
15. Klik `[Delete]`
16. Verifikasi toast sukses: "Success, device SKU has been deleted."
17. Verifikasi dialog tertutup
18. Verifikasi baris `OFF-B-{runId}-026` hilang dari List
19. Verifikasi bar bulk hilang
20. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-85, TC-596. Aksi menghapus data berada di akhir tiap TC (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 10 (Search untuk menemukan baris target, R-16), 2 sampai 4, 6 dan 7 (Edit dan Delete yang hasilnya diasersi pada langkah berikutnya), 11 sampai 13 dan 15 (Bulk Delete), 20 (mengosongkan Search, S-09).
- Asersi absence langkah 9 dan 18 memakai toast sukses langkah 8 dan 16 sebagai anchor (8b butir 2).
- Temuan untuk QA:
  - S-12/S-06: TC mengedit dan menghapus `MAN-LOC-01` pada data Pre-setup; spec memakai SKU milik spec bersuffix dengan atribut setara (stok 0). TC-85 mengubah Model/Type menjadi `MAN-X`; spec memakai `MAN-X-{runId}`.
  - Fixture rancangan: ketersediaan Pre-setup #17 dan #31 (`MAN-LOC-01`) di environment belum diverifikasi; seeding SKU lokal untuk Distributor dengan Local Registration nonaktif bergantung pada fixture BE tim BE/FE.
  - TC-85 dan TC-596 tidak menyebut Brand Distributor Mandala; Brand untuk seeding disediakan tim BE/FE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
