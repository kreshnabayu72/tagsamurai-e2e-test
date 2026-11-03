---
id: TC-AC-DS-E2E-084-bulk-delete-preview-berubah-sebelum-confirm
title: "Bulk Delete: Seluruh SKU Terpilih Menjadi Berstok sebelum Confirm Menampilkan Dialog Blok Tanpa Toast"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-292
coverage:
  web: automated
---

# Bulk Delete: Seluruh SKU Terpilih Menjadi Berstok sebelum Confirm Menampilkan Dialog Blok Tanpa Toast

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| Pelaku kedua lewat sesi API: Total Control Principal `Budi Kurniawan` (Pre-setup #2) | `totalControlSku2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC2_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- Modul stok Hardware Stock (Pre-setup #39) untuk Add Stock `SEED-006` dan `SEED-007`.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: stok `SEED-006` dan `SEED-007` dikembalikan ke 0. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (disediakan tim FE/BE; bagian 8b butir 10).
- Kemampuan teknis: Sesi API aktor kedua (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) untuk menghapus SKU atau menambah stok lewat Add Stock Hardware Stock; mekanisme API tidak disebut TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Catat baseline jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action lewat kemampuan baca (disediakan tim FE/BE)
2. Ketik Search `SEED`, tekan Enter
3. Centang checkbox baris `SEED-006` dan `SEED-007`
4. Klik `Bulk Action`, lalu pilih `Delete`
5. Melalui sesi API aktor kedua (`Budi Kurniawan`), tambahkan 1 unit untuk `SEED-006` dan `SEED-007` lewat Add Stock Hardware Stock hingga stok keduanya 1 tersimpan
6. Klik `[Delete]`
7. Verifikasi dialog "Cannot Delete SKUs" tampil lagi dengan bullet `SEED-006` dan `SEED-007` dan tombol `[OK]`
8. Verifikasi tidak ada toast
9. Klik `[OK]`
10. Verifikasi dialog tertutup
11. Verifikasi seleksi dan bar bulk dipertahankan
12. Verifikasi baris `SEED-006` dan `SEED-007` tetap ada pada List
13. Klik ikon Changelog
14. Verifikasi modal "Changelog: Device SKU" menampilkan sedikitnya satu entri
15. Verifikasi Changelog tidak memuat entri Delete untuk `SEED-006` dan `SEED-007` (jumlah entri sama dengan baseline langkah 1)
16. Tutup modal Changelog, lalu buka Settings > User, pilih user aktor `Jane Setiawan`, buka Detail, dan pilih tab System Log
17. Verifikasi tabel System Log menampilkan sedikitnya satu entri
18. Verifikasi System Log aktor `Jane Setiawan` tidak memuat entri Delete untuk `SEED-006` dan `SEED-007` (jumlah entri sama dengan baseline langkah 1)
19. Buka Activity Log, lalu pilih tab User Action
20. Verifikasi tabel Activity Log menampilkan sedikitnya satu entri
21. Verifikasi Activity Log tidak memuat entri Delete untuk `SEED-006` dan `SEED-007` (jumlah entri sama dengan baseline langkah 1)
22. Buka Settings > Device > Device SKU

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- P-1: asersi absence log (Expected TC) ditulis di spec ini dengan baseline jumlah entri (langkah 1) karena aksi yang diuji ada di spec yang sama dan tidak ada spec absence dengan aksi nyata untuk TC itu (S-05); surface dan anchor positif ditulis sebelum tiap asersi absence (bagian 8b butir 2). Membuka System Log dan Activity Log serta kembali ke Device SKU adalah langkah penghubung.
- Pelaku kedua memakai sesi API (bukan konteks kedua kelas c), sehingga tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20). Search `SEED` pada langkah 2 menampilkan `SEED-006` dan `SEED-007` di halaman 1.
- Temuan untuk QA: TC-292 diberi Automation Manual Only (dua sesi paralel) di TC; pelaku kedua dijalankan lewat sesi API di spec ini. Post Condition TC-292 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
