---
id: TC-AC-DS-E2E-086-bulk-delete-seluruh-terpilih-dihapus-pelaku-lain
title: "Bulk Delete: Seluruh SKU Terpilih Dihapus Pelaku Lain dan Satu Terhapus Sisanya Berstok"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-547
  - TC-AC-DS-574
coverage:
  web: automated
---

# Bulk Delete: Seluruh SKU Terpilih Dihapus Pelaku Lain dan Satu Terhapus Sisanya Berstok

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| Pelaku kedua lewat sesi API: Total Control Principal `Budi Kurniawan` (Pre-setup #2) | `totalControlSku2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC2_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- Modul stok (Pre-setup #39); SKU berstok `HHR-ARC-100` (120) dan `SFR-VEL-4P` (36).
- General Settings entitas uji: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35, tidak diubah).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: `SEED-001` dan `SEED-002` dibuat ulang setelah dihapus pelaku kedua (TC-547 dan TC-574). Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (disediakan tim FE/BE; bagian 8b butir 10).
- Kemampuan teknis: Sesi API aktor kedua (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) untuk menghapus SKU atau menambah stok lewat Add Stock Hardware Stock; mekanisme API tidak disebut TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Catat baseline jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action lewat kemampuan baca (disediakan tim FE/BE)

### TC-AC-DS-547: seluruh SKU terpilih dihapus pelaku lain

2. Ketik Search `SEED`, tekan Enter
3. Centang checkbox baris `SEED-001` dan `SEED-002`
4. Klik `Bulk Action`, lalu pilih `Delete`
5. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus `SEED-001` dan `SEED-002` hingga penghapusan tersimpan
6. Klik `[Delete]`
7. Verifikasi muncul toast info "This device SKU is no longer available."
8. Verifikasi dialog tertutup
9. Verifikasi List di-refresh tanpa `SEED-001` dan `SEED-002`
10. Verifikasi seleksi dibersihkan (bar bulk hilang)
11. Buat ulang `SEED-001` dan `SEED-002` lewat fixture BE, lalu muat ulang halaman dengan F5

### TC-AC-DS-574: satu terpilih dihapus pelaku lain, sisanya berstok

12. Centang checkbox baris `SEED-002` dan `HHR-ARC-100`
13. Atur jumlah data per halaman menjadi 100
14. Pindah ke halaman 2
15. Centang checkbox baris `SFR-VEL-4P`
16. Klik `Bulk Action`, lalu pilih `Delete`
17. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus `SEED-002` hingga penghapusan tersimpan
18. Klik `[Continue]`
19. Verifikasi dialog "Cannot Delete SKUs" tampil lagi dengan bullet `HHR-ARC-100` dan `SFR-VEL-4P` dan tombol `[OK]`
20. Verifikasi `SEED-002` tidak ada di bullet dialog
21. Verifikasi tidak ada toast, termasuk toast "This device SKU is no longer available."
22. Klik `[OK]`
23. Verifikasi dialog tertutup
24. Verifikasi seleksi dan bar bulk dipertahankan
25. Verifikasi baris `SFR-VEL-4P` tetap ada pada halaman 2
26. Pindah ke halaman 1
27. Verifikasi baris `HHR-ARC-100` tetap ada pada halaman 1

### Expected log TC-AC-DS-547 dan TC-AC-DS-574: tidak ada entri Delete oleh Jane S

28. Klik ikon Changelog
29. Verifikasi modal "Changelog: Device SKU" menampilkan sedikitnya satu entri
30. Verifikasi Changelog tidak memuat entri Delete baru oleh `Jane S` (jumlah entri oleh `Jane S` sama dengan baseline langkah 1); entri Delete `SEED-001` dan `SEED-002` yang baru berasal dari `Budi K`
31. Tutup modal Changelog, lalu buka Settings > User, pilih user aktor `Jane Setiawan`, buka Detail, dan pilih tab System Log
32. Verifikasi tabel System Log menampilkan sedikitnya satu entri
33. Verifikasi System Log aktor `Jane Setiawan` tidak memuat entri Delete baru oleh `Jane S` (jumlah entri oleh `Jane S` sama dengan baseline langkah 1); entri Delete `SEED-001` dan `SEED-002` yang baru berasal dari `Budi K`
34. Buka Activity Log, lalu pilih tab User Action
35. Verifikasi tabel Activity Log menampilkan sedikitnya satu entri
36. Verifikasi Activity Log tidak memuat entri Delete baru oleh `Jane S` (jumlah entri oleh `Jane S` sama dengan baseline langkah 1); entri Delete `SEED-001` dan `SEED-002` yang baru berasal dari `Budi K`
37. Buka Settings > Device > Device SKU
38. Ubah jumlah data per halaman menjadi 10

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- P-1: asersi absence log (Expected TC) ditulis di spec ini dengan baseline jumlah entri (langkah 1) karena aksi yang diuji ada di spec yang sama dan tidak ada spec absence dengan aksi nyata untuk TC itu (S-05); surface dan anchor positif ditulis sebelum tiap asersi absence (bagian 8b butir 2). Membuka System Log dan Activity Log serta kembali ke Device SKU adalah langkah penghubung. Expected log TC-547 dan TC-574 diasersi sekali di akhir spec karena tidak ada aksi sesi pertama di kedua blok yang menulis log.
- Alasan di atas sekitar 35 langkah (bagian 3, prinsip 13): semua blok memakai satu kelas harness (dialog Bulk Delete pada data seed yang sama), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihannya berasal dari pemecahan Expected per klausa (S-01) dan pembersihan seleksi antar blok (S-09). Langkah: 38.
- Pelaku kedua memakai sesi API (bukan konteks kedua kelas c), sehingga tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20). Search pada langkah 2 menemukan `SEED-001` dan `SEED-002` di halaman 1; langkah 11 membuat ulang keduanya (S-09, S-06). Atur 100 baris per halaman dan pindah ke halaman 2 menjadikan `SFR-VEL-4P` dapat dicentang tanpa Search.
- Langkah penghubung akhir: langkah 38 memulihkan jumlah data per halaman ke 10 setelah diubah menjadi 100 (S-09).
- Temuan untuk QA: TC-547 dan TC-574 diberi Automation Manual Only (dua sesi paralel) di TC; pelaku kedua dijalankan lewat sesi API di spec ini. Post Condition TC-547 dan TC-574 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
