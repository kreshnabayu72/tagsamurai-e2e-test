---
id: TC-AC-DS-E2E-189-bulk-delete-hasil-aktual-menentukan-toast-preview-berubah
title: "Bulk Delete: Hasil Aktual Menentukan Toast saat Preview Campuran Menjadi Homogen dan Homogen Menjadi Campuran"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-293
  - TC-AC-DS-294
coverage:
  web: automated
---

# Bulk Delete: Hasil Aktual Menentukan Toast saat Preview Campuran Menjadi Homogen dan Homogen Menjadi Campuran

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| Pelaku kedua lewat sesi API: Total Control Principal `Budi Kurniawan` (Pre-setup #2) | `totalControlSku2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC2_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- Modul stok Hardware Stock (Pre-setup #39) untuk Add Stock `SEED-010` dan fixture BE yang mengosongkan unit `HHR-ARC-100`.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: `HHR-ARC-100` dikembalikan ke stok 120 dan `SEED-008`, `SEED-009`, `SEED-011` dibuat ulang; stok `SEED-010` dikembalikan ke 0. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Sesi API aktor kedua (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) untuk menghapus SKU atau menambah stok lewat Add Stock Hardware Stock; mekanisme API tidak disebut TC, PRD, atau LLD.
- Kemampuan teknis: Fixture BE yang mengosongkan seluruh unit `HHR-ARC-100` sehingga stoknya 0 (TC-293 langkah 4); mekanismenya tidak didefinisikan di TC.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-293: preview campuran menjadi homogen

1. Ketik Search `HHR-ARC-100`, tekan Enter
2. Centang checkbox baris `HHR-ARC-100`
3. Ganti isi kotak search dengan `SEED`, tekan Enter
4. Centang checkbox baris `SEED-008`
5. Klik `Bulk Action`, lalu pilih `Delete`
6. Kosongkan seluruh unit `HHR-ARC-100` lewat fixture BE hingga stoknya 0 tersimpan
7. Klik `[Continue]`
8. Verifikasi muncul toast sukses "Success, device SKU has been deleted." (bukan toast partial)
9. Verifikasi `HHR-ARC-100` dan `SEED-008` terhapus
10. Verifikasi bar bulk hilang
11. Verifikasi seleksi direset ke 0

### TC-AC-DS-294: preview homogen menjadi campuran

12. Pulihkan `HHR-ARC-100` (stok 120) dan `SEED-008` lewat fixture BE, lalu muat ulang halaman dengan F5
13. Ketik Search `SEED`, tekan Enter
14. Atur jumlah data per halaman menjadi 25
15. Centang checkbox baris `SEED-009`, `SEED-010`, dan `SEED-011`
16. Klik `Bulk Action`, lalu pilih `Delete`
17. Melalui sesi API aktor kedua (`Budi Kurniawan`), tambahkan 1 unit untuk `SEED-010` lewat Add Stock hingga stoknya 1 tersimpan
18. Klik `[Delete]`
19. Verifikasi muncul toast sukses "Success, device SKU has been deleted. Some items were skipped (still have stock)."
20. Verifikasi `SEED-009` dan `SEED-011` terhapus
21. Verifikasi `SEED-010` tetap ada karena berstok
22. Verifikasi bar bulk hilang
23. Verifikasi seleksi direset ke 0

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua memakai sesi API (bukan konteks kedua kelas c), sehingga tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20). Search pada langkah 1 dan Search `SEED` menemukan baris target di luar halaman 1 (default sort SKU A-Z, Pre-setup #29 dan #30); seleksi `HHR-ARC-100` dipertahankan saat Search diganti (TC-280).
- Temuan untuk QA: TC-293 dan TC-294 diberi Automation Manual Only (dua sesi paralel) di TC; pemicu dijalankan lewat fixture BE dan sesi API di spec ini. TC-293 tidak menyebut Selection Limit untuk seleksi lintas Search. Post Condition TC-293 dan TC-294 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
