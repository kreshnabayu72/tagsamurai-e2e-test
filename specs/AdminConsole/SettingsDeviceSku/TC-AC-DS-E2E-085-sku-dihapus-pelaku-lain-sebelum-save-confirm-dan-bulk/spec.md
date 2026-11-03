---
id: TC-AC-DS-E2E-085-sku-dihapus-pelaku-lain-sebelum-save-confirm-dan-bulk
title: "SKU Dihapus Pelaku Lain sebelum Save, Confirm Delete, dan Bulk Delete (Sebagian)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-544
  - TC-AC-DS-545
  - TC-AC-DS-546
coverage:
  web: automated
---

# SKU Dihapus Pelaku Lain sebelum Save, Confirm Delete, dan Bulk Delete (Sebagian)

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
- General Settings entitas uji: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35, tidak diubah).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: SKU `TAG-ARC-OBJ` dibuat ulang (stok 0) setelah dihapus pelaku kedua; `SEED-001`, `SEED-002`, dan `SEED-003` dibuat ulang. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog sebelum dan sesudah aksi (disediakan tim FE/BE; bagian 8b butir 10).
- Kemampuan teknis: Sesi API aktor kedua (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) untuk menghapus SKU atau menambah stok lewat Add Stock Hardware Stock; mekanisme API tidak disebut TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-544: SKU dihapus sebelum Save

1. Ketik Search `TAG-ARC-OBJ`, tekan Enter
2. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Edit`
3. Ubah Model/Type menjadi `T-GONE`
4. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus SKU `TAG-ARC-OBJ` hingga penghapusan tersimpan
5. Klik `[Save]`
6. Verifikasi muncul toast info "This device SKU is no longer available."
7. Verifikasi popup Edit tertutup
8. Verifikasi List di-refresh sehingga baris `TAG-ARC-OBJ` tidak ada
9. Buat ulang SKU `TAG-ARC-OBJ` (stok 0) lewat fixture BE, lalu muat ulang halaman dengan F5

### TC-AC-DS-545: SKU dihapus sebelum Confirm Delete

10. Ketik Search `TAG-ARC-OBJ`, tekan Enter
11. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Delete`
12. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus SKU `TAG-ARC-OBJ` hingga penghapusan tersimpan
13. Klik `[Delete]`
14. Verifikasi muncul toast info "This device SKU is no longer available."
15. Verifikasi dialog konfirmasi tertutup
16. Verifikasi List di-refresh sehingga baris `TAG-ARC-OBJ` tidak ada

### TC-AC-DS-546: Bulk Delete sebagian SKU sudah dihapus

17. Klik `(←)` pada kotak Search
18. Catat baseline jumlah entri Changelog lewat kemampuan baca (disediakan tim FE/BE)
19. Ketik Search `SEED`, tekan Enter
20. Centang checkbox baris `SEED-001`, `SEED-002`, dan `SEED-003`
21. Klik `Bulk Action`, lalu pilih `Delete`
22. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus SKU `SEED-002` hingga penghapusan tersimpan
23. Klik `[Delete]`
24. Verifikasi muncul toast info "This device SKU is no longer available."
25. Verifikasi tidak ada toast sukses
26. Verifikasi tidak ada toast partial "Some items were skipped"
27. Verifikasi `SEED-001` dan `SEED-003` terhapus; `SEED-002` tidak dihitung terhapus maupun dilewati
28. Verifikasi dialog tertutup
29. Verifikasi List di-refresh
30. Verifikasi seleksi direset
31. Klik ikon Changelog
32. Verifikasi modal "Changelog: Device SKU" menampilkan sedikitnya satu entri
33. Verifikasi Changelog memuat tepat dua entri Delete baru oleh `Jane S` (`SEED-001` dan `SEED-003`) tanpa entri Delete `SEED-002` oleh `Jane S`; entri Delete `SEED-002` baru berasal dari `Budi K` (tiga entri baru terhadap baseline langkah 18)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua memakai sesi API (bukan konteks kedua kelas c), sehingga tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20). Search pada langkah 1 dan Search berikutnya menemukan baris target di luar halaman 1 (default sort SKU A-Z, Pre-setup #29 dan #30) sebagai langkah penghubung; langkah 9 membuat ulang `TAG-ARC-OBJ` (S-09, S-06).
- Baseline Changelog (langkah 18) dicatat tepat sebelum TC-546 supaya entri Delete oleh pelaku kedua pada TC-544 dan TC-545 tidak mengubah selisih; tiga entri teratas yang urutannya dalam satu menit tidak diasersi.
- Temuan untuk QA: TC-544 sampai TC-546 diberi Automation Manual Only (dua sesi paralel) di TC; pelaku kedua dijalankan lewat sesi API di spec ini. TC-546 Expected e menyebut entri "dari sesi pertama" tanpa menyatakan surface; spec memakai Changelog. Post Condition TC-544 sampai TC-546 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
