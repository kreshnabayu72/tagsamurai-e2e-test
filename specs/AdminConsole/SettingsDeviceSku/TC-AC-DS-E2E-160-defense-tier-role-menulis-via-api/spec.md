---
id: TC-AC-DS-E2E-160-defense-tier-role-menulis-via-api
title: "Defense-in-Depth: Read Only, Create-Only, Update-Only, dan Delete-Only Menulis lewat API Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-515
  - TC-AC-DS-516
  - TC-AC-DS-517
  - TC-AC-DS-518
coverage:
  web: automated
---

# Defense-in-Depth: Read Only, Create-Only, Update-Only, dan Delete-Only Menulis lewat API Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Token API (sesi API aktor), tiap blok role memakai token sendiri: Read Only Principal (Rina Wijaya): `readOnlySku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_RO_PASSWORD` (Pre-setup #3); Create-Only Principal: `manageSkuC_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_C_PASSWORD` (Pre-setup #4); Update-Only Principal: `manageSkuU_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_U_PASSWORD` (Pre-setup #5); Delete-Only Principal: `manageSkuD_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_D_PASSWORD` (Pre-setup #6). Pengamat UI: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Data Pre-setup (hanya dibaca kecuali disebut lain): SKU inti dan seed (#29, #30), file foto (#37). Fixture kemampuan role Create-Only, Update-Only, dan Delete-Only (Global Role Manage device master data) sudah ada di Pre-setup #4 sampai #6.
- Data Dinamis: tidak ada; tidak ada SKU yang boleh tersimpan atau terhapus (target `TAG-ARC-OBJ`).
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server (multipart/form-data) dengan token sesi API aktor akun yang disebut; ID record SKU target (`{id}`) dibaca lewat fixture BE (TC tidak menyebut caranya). Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- Pengamat UI: sesi web akun yang login di hook `before`; observasi state data (List) mengikuti langkah TC dan bukan perilaku FE atas respons request langsung.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-515: Read Only mencoba menulis lewat API ditolak

1. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `readOnlySku`
2. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `readOnlySku`
3. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `readOnlySku`
4. Verifikasi ketiga request ditolak dengan status 403
5. Muat ulang List Device SKU, ketik Search `TAG-ARC-OBJ`, tekan Enter
6. Verifikasi baris `TAG-ARC-OBJ` tetap ada dengan Model/Type `T-OBJ`
7. Klik `(←)` pada kotak Search
8. Verifikasi tidak ada SKU baru: Pagination menampilkan 13 halaman untuk 129 SKU Principal

### TC-AC-DS-516: Create-Only mencoba Edit dan Delete lewat API ditolak

9. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `manageSkuC`
10. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `manageSkuC`
11. Verifikasi kedua request ditolak dengan status 403
12. Muat ulang List Device SKU, ketik Search `TAG-ARC-OBJ`, tekan Enter
13. Verifikasi baris `TAG-ARC-OBJ` tetap ada dengan Model/Type `T-OBJ`
14. Klik `(←)` pada kotak Search
15. Verifikasi tidak ada SKU baru: Pagination menampilkan 13 halaman untuk 129 SKU Principal

### TC-AC-DS-517: Update-Only mencoba Create dan Delete lewat API ditolak

16. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `manageSkuU`
17. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `manageSkuU`
18. Verifikasi kedua request ditolak dengan status 403
19. Muat ulang List Device SKU, ketik Search `TAG-ARC-OBJ`, tekan Enter
20. Verifikasi baris `TAG-ARC-OBJ` tetap ada
21. Klik `(←)` pada kotak Search
22. Verifikasi tidak ada SKU baru dan tidak ada SKU terhapus: Pagination menampilkan 13 halaman

### TC-AC-DS-518: Delete-Only mencoba Create dan Edit lewat API ditolak

23. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `manageSkuD`
24. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `manageSkuD`
25. Verifikasi kedua request ditolak dengan status 403
26. Muat ulang List Device SKU, ketik Search `TAG-ARC-OBJ`, tekan Enter
27. Verifikasi baris `TAG-ARC-OBJ` tetap ada dengan Model/Type `T-OBJ`
28. Klik `(←)` pada kotak Search
29. Verifikasi tidak ada SKU baru: Pagination menampilkan 13 halaman untuk 129 SKU Principal

## Notes

- `K-1`: TC kelas a (defense-in-depth) dengan Expected respons API (status respons dan state data) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-device-sku-backend.md`; langkah request langsung hanya mengasersi status respons dan state data (8b butir 1). Rujukan ID TC: 515 sampai 518.
- Spec ditulis per blok role karena token dan request tiap role berbeda (bagian 3a, Role Matrix bukan perulangan identik). Langkah penghubung tanpa `Verifikasi`: muat ulang List beserta Search `TAG-ARC-OBJ` untuk menemukan baris target (R-16) dan penutupan Search (S-09).
- Pembagian TC lintas spec (S-05): Expected butir c TC-AC-DS-515 (Changelog, System Log `Rina Wijaya`, dan Activity Log tidak memuat entri baru) diasersi di spec 193, yang mengirim request penolakan sendiri dengan user dan baseline log sendiri; spec ini mengasersi status respons dan state data (Expected butir a dan b). TC 516 sampai 518 tidak memuat Expected log.
- Akun pengamat Total Control Principal (Pre-setup #1) login di hook `before`; TC 515 sampai 518 hanya membaca List.
- Pengecualian S-12 A-11: `TAG-ARC-OBJ` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target request yang ditolak; tidak ada data yang diubah atau dibuat spec ini (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
