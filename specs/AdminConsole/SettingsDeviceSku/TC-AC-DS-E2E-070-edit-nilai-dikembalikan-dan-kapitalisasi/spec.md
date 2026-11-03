---
id: TC-AC-DS-E2E-070-edit-nilai-dikembalikan-dan-kapitalisasi
title: "Edit SKU: Mengubah Lalu Mengembalikan Nilai Dianggap Tanpa Perubahan dan Perubahan Kapitalisasi Dicatat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-207
  - TC-AC-DS-208
coverage:
  web: automated
---

# Edit SKU: Mengubah Lalu Mengembalikan Nilai Dianggap Tanpa Perubahan dan Perubahan Kapitalisasi Dicatat

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke nilai Pre-setup #29 (Device Name `UHF Handheld Reader`, SKU `HHR-ARC-200`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0, 1 foto, Last Modified `28/09/26 14:40`). Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (disediakan tim FE/BE; bagian 8b butir 10).
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Catat baseline jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action lewat kemampuan baca (disediakan tim FE/BE)

### TC-AC-DS-207: nilai dikembalikan

2. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
3. Ubah Model/Type dari `H200` menjadi `H999`
4. Ubah Model/Type kembali menjadi `H200`
5. Klik `[Save]`
6. Verifikasi muncul toast info "No changes to save."
7. Verifikasi popup Edit tertutup
8. Klik ikon Changelog
9. Verifikasi modal "Changelog: Device SKU" menampilkan sedikitnya satu entri
10. Verifikasi Changelog tidak memuat entri baru untuk `HHR-ARC-200` (jumlah entri sama dengan baseline langkah 1)
11. Tutup modal Changelog, lalu buka Settings > User, pilih user aktor `Jane Setiawan`, buka Detail, dan pilih tab System Log
12. Verifikasi tabel System Log menampilkan sedikitnya satu entri
13. Verifikasi System Log aktor `Jane Setiawan` tidak memuat entri baru untuk `HHR-ARC-200` (jumlah entri sama dengan baseline langkah 1)
14. Buka Activity Log, lalu pilih tab User Action
15. Verifikasi tabel Activity Log menampilkan sedikitnya satu entri
16. Verifikasi Activity Log tidak memuat entri baru untuk `HHR-ARC-200` (jumlah entri sama dengan baseline langkah 1)
17. Buka Settings > Device > Device SKU

### TC-AC-DS-208: perubahan kapitalisasi

18. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
19. Ubah Model/Type dari `H200` menjadi `h200` (hanya huruf kecil)
20. Klik `[Save]`
21. Verifikasi muncul toast sukses "Success, device SKU has been updated."
22. Verifikasi tidak muncul toast "No changes to save."
23. Verifikasi baris `HHR-ARC-200` menampilkan badge Model/Type `h200`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- P-1: asersi absence log TC-207 (Expected c) ditulis di spec ini dengan baseline jumlah entri (langkah 1) karena aksi yang diuji (Save tanpa perubahan) berada di spec yang sama dan tidak ada spec absence dengan aksi nyata untuk TC-207 (S-05). Toast info sesudah Save menjadi anchor hasil server dan anchor surface ditulis sebelum tiap asersi absence (bagian 8b butir 2).
- Langkah penghubung: menutup modal Changelog, berpindah ke System Log dan Activity Log, lalu kembali ke Settings > Device > Device SKU.
- Post Condition TC-208 (Model/Type tersimpan `h200`, satu entri Edit Model/Type, entri log tiga surface) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
- Temuan untuk QA: TC-207 menyebut System Log aktor tanpa menyatakan filter; jumlah entri dibaca lewat kemampuan baca. Nama aktor `Jane Setiawan` dari Pre-setup #1.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
