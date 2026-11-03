---
id: TC-AC-DS-E2E-075-delete-single-dialog-konfirmasi-cancel-esc-backdrop
title: "Delete SKU Single: Dialog Konfirmasi, Cancel, Esc, dan Klik Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-255
  - TC-AC-DS-257
  - TC-AC-DS-258
  - TC-AC-DS-259
coverage:
  web: automated
---

# Delete SKU Single: Dialog Konfirmasi, Cancel, Esc, dan Klik Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU `HHR-ARC-200` dan `TAG-ARC-OBJ` (stok 0) dari #29; spec hanya membuka dan membatalkan dialog Delete.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` dan `TAG-ARC-OBJ` ke keadaan Pre-setup #29. Spec ini tidak menyimpan perubahan data.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (disediakan tim FE/BE; bagian 8b butir 10).
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Catat baseline jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action lewat kemampuan baca (disediakan tim FE/BE)

### TC-AC-DS-255: dialog konfirmasi

2. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Delete`
3. Verifikasi dialog konfirmasi tampil dengan judul "Delete SKU", bullet `HHR-ARC-200` pada baris terisolasi, body "Are you sure you want to delete it? This action cannot be undone.", dan tombol `[Cancel]` serta `[Delete]`
4. Verifikasi tidak ada toast pada saat dialog tampil
5. Klik `[Cancel]`

### TC-AC-DS-257, TC-AC-DS-258, TC-AC-DS-259: Cancel, Esc, dan klik backdrop pada SKU `TAG-ARC-OBJ`

6. Ketik Search `TAG-ARC-OBJ`, tekan Enter
7. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
8. Klik `[Cancel]`
9. Verifikasi dialog tertutup
10. Verifikasi tidak ada toast
11. Verifikasi baris `TAG-ARC-OBJ` tetap ada pada List
12. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
13. Tekan Esc
14. Verifikasi dialog tertutup seperti `[Cancel]`
15. Verifikasi tidak ada toast
16. Verifikasi baris `TAG-ARC-OBJ` tetap ada (tidak ada SKU terhapus)
17. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
18. Klik area backdrop di luar dialog
19. Verifikasi dialog tetap terbuka
20. Klik `[Cancel]`
21. Verifikasi baris `TAG-ARC-OBJ` tetap ada (SKU tidak terhapus)

### Expected c TC-AC-DS-257: log tidak memuat entri Delete baru

22. Klik ikon Changelog
23. Verifikasi modal "Changelog: Device SKU" menampilkan sedikitnya satu entri
24. Verifikasi Changelog tidak memuat entri Delete baru untuk `TAG-ARC-OBJ` (jumlah entri sama dengan baseline langkah 1)
25. Tutup modal Changelog, lalu buka Settings > User, pilih user aktor `Jane Setiawan`, buka Detail, dan pilih tab System Log
26. Verifikasi tabel System Log menampilkan sedikitnya satu entri
27. Verifikasi System Log aktor `Jane Setiawan` tidak memuat entri Delete baru untuk `TAG-ARC-OBJ` (jumlah entri sama dengan baseline langkah 1)
28. Buka Activity Log, lalu pilih tab User Action
29. Verifikasi tabel Activity Log menampilkan sedikitnya satu entri
30. Verifikasi Activity Log tidak memuat entri Delete baru untuk `TAG-ARC-OBJ` (jumlah entri sama dengan baseline langkah 1)
31. Buka Settings > Device > Device SKU

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- P-1: asersi absence log (Expected TC) ditulis di spec ini dengan baseline jumlah entri (langkah 1) karena aksi yang diuji ada di spec yang sama dan tidak ada spec absence dengan aksi nyata untuk TC itu (S-05); surface dan anchor positif ditulis sebelum tiap asersi absence (bagian 8b butir 2). Membuka System Log dan Activity Log serta kembali ke Device SKU adalah langkah penghubung.
- Penyimpangan urutan: Expected c TC-257 (log tidak memuat entri Delete) diasersi sekali di akhir spec setelah TC-258 dan TC-259, yang juga tidak menulis log; Search pada langkah 6 menemukan baris `TAG-ARC-OBJ` di luar halaman 1 (default sort SKU A-Z) sebagai langkah penghubung.
- Temuan untuk QA: TC-259 tidak menyatakan cara menutup dialog sesudah klik backdrop; spec memakai `[Cancel]` sebagai langkah penghubung. Dialog D-01 TC-255 menyebut "tidak ada toast" tanpa batas waktu.
- Post Condition TC-255 sampai TC-259 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
