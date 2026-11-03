---
id: TC-AC-DS-E2E-078-delete-single-berhasil-klik-ganda-dan-riwayat-transaksi
title: "Delete SKU Single Berhasil: Klik Ganda Satu Penghapusan dan Riwayat Transaksi Tetap Terbaca"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-256
  - TC-AC-DS-270
  - TC-AC-DS-271
coverage:
  web: automated
---

# Delete SKU Single Berhasil: Klik Ganda Satu Penghapusan dan Riwayat Transaksi Tetap Terbaca

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU `TAG-ARC-OBJ` (Device Name `Asset TAG`, stok 0) dan `HHR-ARC-100` dari #29; modul TAG Stock (Add Stock dan Stock List) pada Principal PT Arunika Prima (Pre-setup #39); riwayat Changelog (Pre-setup #33).
- General Settings entitas uji: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: SKU `TAG-ARC-OBJ` dibuat ulang (stok 0) setelah tiap blok yang menghapusnya dan setelah spec selesai. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-256: Delete berhasil

1. Ketik Search `TAG-ARC-OBJ`, tekan Enter
2. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
3. Klik `[Delete]`
4. Verifikasi muncul toast sukses "Success, device SKU has been deleted."
5. Verifikasi dialog tertutup
6. Verifikasi baris `TAG-ARC-OBJ` hilang dari List
7. Tekan Enter pada kotak Search yang sama
8. Verifikasi hasil Search `TAG-ARC-OBJ` menampilkan "No results found"
9. Buat ulang SKU `TAG-ARC-OBJ` (stok 0) lewat fixture BE, lalu muat ulang halaman dengan F5

### TC-AC-DS-270: klik ganda Delete

10. Ketik Search `TAG-ARC-OBJ`, tekan Enter
11. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
12. Tunggu toast lama hilang otomatis
13. Klik `[Delete]` dua kali dengan cepat
14. Verifikasi tombol `[Delete]` disabled setelah klik pertama
15. Verifikasi muncul toast sukses "Success, device SKU has been deleted."
16. Verifikasi hanya satu toast sukses yang tampil
17. Buat ulang SKU `TAG-ARC-OBJ` (stok 0) lewat fixture BE, lalu muat ulang halaman dengan F5

### TC-AC-DS-271: riwayat transaksi tetap terbaca

18. Ketik Search `TAG-ARC-OBJ`, tekan Enter
19. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
20. Klik `[Delete]`
21. Tekan Enter pada kotak Search yang sama
22. Verifikasi hasil Search `TAG-ARC-OBJ` pada List menampilkan "No results found"
23. Klik ikon Changelog
24. Ketik Search Changelog `TAG-ARC-OBJ`, tekan Enter
25. Verifikasi hasil Search Changelog memuat entri Delete dengan SKU `Asset TAG (TAG-ARC-OBJ)`, Old Value `Asset TAG (TAG-ARC-OBJ)`, dan New Value `—`
26. Ganti isi kotak Search Changelog dengan `H10`, tekan Enter
27. Verifikasi entri lama Edit `UHF Handheld Reader (HHR-ARC-100)` Model/Type `H10` > `H100` tetap tampil tanpa perubahan
28. Tutup modal Changelog, lalu buka TAG Stock > Stock List, klik Add Stock, dan buka daftar SKU
29. Verifikasi daftar SKU pada pilihan Add Stock memuat sedikitnya satu opsi SKU lain
30. Verifikasi `TAG-ARC-OBJ` tidak tersedia sebagai pilihan Add Stock
31. Tutup Add Stock

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: Search pada langkah 1 menemukan baris di luar halaman 1 (default sort SKU A-Z); langkah 9 dan 17 membuat ulang `TAG-ARC-OBJ` (S-09, S-06; fixture BE disediakan tim FE/BE) karena tiap blok menghapus SKU itu; Search `H10` di modal Changelog menemukan entri seed lama (Pre-setup #33) tanpa bergantung posisi halaman (S-14).
- Pemisahan: asersi Search `TAG-ARC-OBJ` "No results found" TC-256 diasersi setelah Enter ulang pada kotak Search yang sama (bagian 8b butir 9).
- Temuan untuk QA: TC-271 mengharapkan entri Delete `Asset TAG (TAG-ARC-OBJ)` dengan Old Value `Asset TAG (TAG-ARC-OBJ)`; karena SKU ini dibuat ulang dan dihapus tiga kali dalam spec, Changelog memuat beberapa entri serupa dan spec mengasersi keberadaan, bukan jumlah. Post Condition TC-256 (SKU terhapus permanen, riwayat transaksi lama terbaca dari snapshot; entri log tiga surface) tidak diasersi karena TC tidak memberi langkah observasinya, kecuali bagian yang menjadi Expected TC-271; Post Condition TC-270 (satu penghapusan, satu entri Delete tiap surface log) tidak diasersi.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
