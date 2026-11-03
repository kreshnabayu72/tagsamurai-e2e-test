---
id: TC-AC-DS-E2E-067-edit-sukses-range-type-port-user-tag-dan-tiga-field
title: "Edit SKU Berhasil: Range Type, Port pada Stok 0 dan Stok Berisi, serta User TAG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-196
  - TC-AC-DS-197
  - TC-AC-DS-198
  - TC-AC-DS-199
coverage:
  web: automated
---

# Edit SKU Berhasil: Range Type, Port pada Stok 0 dan Stok Berisi, serta User TAG

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` (Range Type `Short Range`), `SFR-ZERO-01` (Port `9090`), `SFR-VEL-4P` (Port `8080`, stok 36), dan `TAG-ARC-OBJ` (TAG Type `Object`) ke nilai Pre-setup #29; preferensi kolom List (Range Type dan TAG Type di-unhide) dihapus dari browser di hook `after` (kemampuan disediakan tim FE). Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-196: Range Type

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Ubah Range Type dari `Short Range` menjadi `Long Range`
3. Klik `[Save]`
4. Verifikasi muncul toast sukses "Success, device SKU has been updated."
5. Verifikasi popup Edit tertutup
6. Klik header kolom Actions `(⋯)`, lalu centang `Range Type` pada Column Visibility
7. Verifikasi baris `HHR-ARC-200` menampilkan badge `Long Range` pada kolom Range Type

### TC-AC-DS-197: Port pada Smart Fixed Reader stok 0

8. Ketik Search `SFR-ZERO-01`, tekan Enter
9. Klik `⋯` pada baris `SFR-ZERO-01`, lalu pilih `Edit`
10. Ubah Port dari `9090` menjadi `9100`
11. Klik `[Save]`
12. Verifikasi muncul toast sukses "Success, device SKU has been updated."
13. Verifikasi popup Edit tertutup
14. Klik `⋯` pada baris `SFR-ZERO-01`, lalu pilih `Edit`
15. Verifikasi field Port berisi `9100`
16. Klik `✕` pada header popup Edit SKU

### TC-AC-DS-198: Port pada Smart Fixed Reader berstok

17. Ganti isi kotak search dengan `SFR-VEL-4P`, tekan Enter
18. Klik `⋯` pada baris `SFR-VEL-4P`, lalu pilih `Edit`
19. Ubah Port dari `8080` menjadi `8081`
20. Klik `[Save]`
21. Verifikasi muncul toast sukses "Success, device SKU has been updated."
22. Verifikasi popup Edit tertutup
23. Klik `⋯` pada baris `SFR-VEL-4P`, lalu pilih `Edit`
24. Verifikasi field Port berisi `8081`
25. Klik `✕` pada header popup Edit SKU

### TC-AC-DS-199: This is User TAG

26. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
27. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Edit`
28. Centang checkbox `This is User TAG`
29. Klik `[Save]`
30. Verifikasi muncul toast sukses "Success, device SKU has been updated."
31. Verifikasi popup Edit tertutup
32. Klik header kolom Actions `(⋯)`, lalu centang `TAG Type` pada Column Visibility
33. Verifikasi baris `TAG-ARC-OBJ` menampilkan badge `User` pada kolom TAG Type

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: Search pada langkah 8, 17, dan 26 menemukan baris target di luar halaman 1 (default sort SKU A-Z, Pre-setup #29 dan #30); "Klik `✕`" setelah verifikasi Port menutup popup bersih. Langkah membuka Column Visibility mengikuti Expected TC-196 dan TC-199 (kolom Hidden secara default).
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface.
- Temuan untuk QA: TC-196 dan TC-199 mensyaratkan kolom di-unhide tetapi tidak menyatakan pemulihan preferensi kolom; spec memulihkannya di hook `after` (bagian 4).
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
