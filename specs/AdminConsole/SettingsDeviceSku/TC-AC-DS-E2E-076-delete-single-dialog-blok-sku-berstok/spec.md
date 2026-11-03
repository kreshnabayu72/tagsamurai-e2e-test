---
id: TC-AC-DS-E2E-076-delete-single-dialog-blok-sku-berstok
title: "Delete SKU Single pada SKU Berstok: Dialog Blok, OK, Esc, Backdrop, dan Stok Masuk setelah Dialog Tampil"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-260
  - TC-AC-DS-261
  - TC-AC-DS-262
  - TC-AC-DS-263
coverage:
  web: automated
---

# Delete SKU Single pada SKU Berstok: Dialog Blok, OK, Esc, Backdrop, dan Stok Masuk setelah Dialog Tampil

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| Pelaku kedua lewat sesi API: Total Control Principal `Budi Kurniawan` (Pre-setup #2) | `totalControlSku2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC2_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU `HHR-ARC-100` (stok 120) dan `HHR-ARC-200` (stok 0) dari #29; modul stok Hardware Stock (Pre-setup #39) untuk Add Stock `HHR-ARC-200`.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke stok 0 (stok 1 hasil Add Stock dikembalikan). Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (disediakan tim FE/BE; bagian 8b butir 10).
- Kemampuan teknis: Sesi API aktor kedua (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) untuk menambah stok lewat Add Stock Hardware Stock; mekanisme API tidak disebut TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Catat baseline jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action lewat kemampuan baca (disediakan tim FE/BE)

### TC-AC-DS-260: dialog blok

2. Klik `⋯` pada baris `HHR-ARC-100`
3. Verifikasi opsi `Delete` tampil dan enabled sebelum diklik
4. Pilih `Delete`
5. Verifikasi dialog blok tampil dengan judul "Cannot Delete SKU", bullet `HHR-ARC-100`, body "This SKU still has stock. Remove all stock before deleting.", dan satu tombol `[OK]`
6. Verifikasi tidak ada toast

### TC-AC-DS-262: klik backdrop pada dialog blok

7. Klik area backdrop di luar dialog
8. Verifikasi dialog blok tetap terbuka dan hanya tertutup lewat `[OK]` atau Esc

### TC-AC-DS-261: OK dan Esc

9. Klik `[OK]`
10. Verifikasi dialog blok tertutup
11. Verifikasi baris `HHR-ARC-100` tetap ada
12. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Delete`
13. Tekan Esc
14. Verifikasi dialog blok tertutup seperti `[OK]`
15. Verifikasi tidak ada toast

### TC-AC-DS-263: stok masuk setelah dialog konfirmasi tampil

16. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Delete`
17. Melalui sesi API aktor kedua (`Budi Kurniawan`), tambahkan 1 unit `HHR-ARC-200` lewat Add Stock Hardware Stock hingga Current Stock menjadi 1 tersimpan
18. Klik `[Delete]`
19. Verifikasi dialog konfirmasi digantikan dialog blok "Cannot Delete SKU" dengan bullet `HHR-ARC-200` dan tombol `[OK]`
20. Verifikasi tidak ada toast
21. Klik `[OK]`
22. Verifikasi baris `HHR-ARC-200` tetap ada pada List (SKU tidak terhapus)
23. Klik ikon Changelog
24. Verifikasi modal "Changelog: Device SKU" menampilkan sedikitnya satu entri
25. Verifikasi Changelog tidak memuat entri Delete untuk `HHR-ARC-200` (jumlah entri sama dengan baseline langkah 1)
26. Tutup modal Changelog, lalu buka Settings > User, pilih user aktor `Jane Setiawan`, buka Detail, dan pilih tab System Log
27. Verifikasi tabel System Log menampilkan sedikitnya satu entri
28. Verifikasi System Log aktor `Jane Setiawan` tidak memuat entri Delete untuk `HHR-ARC-200` (jumlah entri sama dengan baseline langkah 1)
29. Buka Activity Log, lalu pilih tab User Action
30. Verifikasi tabel Activity Log menampilkan sedikitnya satu entri
31. Verifikasi Activity Log tidak memuat entri Delete untuk `HHR-ARC-200` (jumlah entri sama dengan baseline langkah 1)
32. Buka Settings > Device > Device SKU

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- P-1: asersi absence log (Expected TC) ditulis di spec ini dengan baseline jumlah entri (langkah 1) karena aksi yang diuji ada di spec yang sama dan tidak ada spec absence dengan aksi nyata untuk TC itu (S-05); surface dan anchor positif ditulis sebelum tiap asersi absence (bagian 8b butir 2). Membuka System Log dan Activity Log serta kembali ke Device SKU adalah langkah penghubung.
- Penyimpangan urutan: TC-262 (klik backdrop) dijalankan sebelum TC-261 (OK dan Esc) supaya dialog yang sama dipakai tanpa dibuka ulang; Expected d TC-263 diasersi di akhir spec.
- Pelaku kedua memakai sesi API (bukan konteks kedua kelas c), sehingga tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Temuan untuk QA: TC-263 diberi Automation Manual Only (dua sesi paralel) di TC; pelaku kedua dijalankan lewat sesi API di spec ini. Post Condition TC-260 sampai TC-263 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
