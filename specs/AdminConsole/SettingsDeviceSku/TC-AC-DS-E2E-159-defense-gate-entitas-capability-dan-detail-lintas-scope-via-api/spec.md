---
id: TC-AC-DS-E2E-159-defense-gate-entitas-capability-dan-detail-lintas-scope-via-api
title: "Defense-in-Depth: Partner, Principal Tanpa Capability, Local Registration Nonaktif, dan Detail SKU Distributor Ditolak lewat API"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-512
  - TC-AC-DS-513
  - TC-AC-DS-514
  - TC-AC-DS-519
  - TC-AC-DS-522
  - TC-AC-DS-603
  - TC-AC-DS-604
coverage:
  web: automated
---

# Defense-in-Depth: Partner, Principal Tanpa Capability, Local Registration Nonaktif, dan Detail SKU Distributor Ditolak lewat API

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Token API (sesi API aktor) dan ganti akun: Total Control Partner CV Karya Mandiri: `totalControlPartner_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_PARTNER_PASSWORD` (Pre-setup #15); Principal tanpa capability Manage device master data: `noCapabilitySku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_NOCAP_PASSWORD` (Pre-setup #8); Total Control Distributor PT Mandala Niaga, Local Registration nonaktif: `totalControlDistOff_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTOFF_PASSWORD` (Pre-setup #17) (ganti akun UI pada langkah 35); Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1) (pengamat).
- Data Pre-setup (hanya dibaca kecuali disebut lain): SKU inti dan seed (#29, #30), file foto (#37). SKU Distributor (#31).
- Data Dinamis: SKU `API-LR-OFF` (payload TC 519) tidak boleh tersimpan; hook `after` memastikan tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server (multipart/form-data) dengan token sesi API aktor akun yang disebut; ID record SKU target (`{id}`) dibaca lewat fixture BE (TC tidak menyebut caranya). Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- Pengamat UI: sesi web akun yang login di hook `before`; observasi state data (List, Changelog, System Log, Activity Log) mengikuti langkah TC dan bukan perilaku FE atas respons request langsung.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-512: Partner membuat SKU lewat API ditolak oleh entity gate

1. Catat jumlah total baris List Principal (Pagination) sebagai baseline N_SKU
2. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token Partner CV Karya Mandiri dengan payload valid
3. Verifikasi respons ditolak dengan status 403
4. Muat ulang List Device SKU pada akun Principal
5. Verifikasi tidak ada SKU baru pada List Principal: jumlah total baris sama dengan baseline N_SKU

### TC-AC-DS-513: Partner membaca daftar dan detail SKU lewat API ditolak

6. Kirim request `POST /v2/enterprise-management/device-skus/list` lewat klien HTTP dengan token Partner CV Karya Mandiri
7. Kirim request `GET /v2/enterprise-management/device-skus/{id}` untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token Partner CV Karya Mandiri
8. Verifikasi kedua request ditolak dengan status 403
9. Verifikasi respons kedua request tidak memuat data SKU

### TC-AC-DS-514: Principal tanpa capability mengakses semua endpoint Device SKU ditolak

10. Kirim request `POST /v2/enterprise-management/device-skus/list` lewat klien HTTP dengan token `noCapabilitySku`
11. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `noCapabilitySku`
12. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `noCapabilitySku`
13. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `noCapabilitySku`
14. Verifikasi keempat request ditolak dengan status 403
15. Muat ulang List Device SKU pada sesi pengamat Total Control Principal PT Arunika Prima, ketik Search `TAG-ARC-OBJ`, tekan Enter
16. Verifikasi baris `TAG-ARC-OBJ` tampil dengan Model/Type `T-OBJ`
17. Klik `(←)` pada kotak Search
18. Verifikasi Pagination menampilkan 13 halaman untuk 129 SKU Principal (tidak ada SKU baru)

### TC-AC-DS-522: Principal membaca detail SKU milik Distributor lewat API tidak ditemukan

19. Kirim request `GET /v2/enterprise-management/device-skus/{id}` untuk Device SKU `LOC-NOR-01` (milik PT Cakra Distribusi) lewat klien HTTP dengan token `totalControlSku`
20. Verifikasi detail `LOC-NOR-01` ditolak dengan status 404 karena SKU Distributor tidak terlihat bagi Principal
21. Kirim request `GET /v2/enterprise-management/device-skus/{id}` untuk Device SKU `HHR-ARC-100` (milik PT Arunika Prima) lewat klien HTTP dengan token `totalControlSku`
22. Verifikasi detail `HHR-ARC-100` milik Principal sukses dengan SKU `HHR-ARC-100` pada respons

### TC-AC-DS-603: Partner membaca daftar export, Usage, dan export Usage lewat API ditolak

23. Kirim request `POST /v2/enterprise-management/device-skus/export` lewat klien HTTP dengan token Partner CV Karya Mandiri dengan parameter wajib daftar dan `format` `csv`
24. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/list` untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token Partner CV Karya Mandiri dengan parameter wajib usage (`page`, `limit`, `sortBy`, `sortOrder`, `columns`)
25. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/export` untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token Partner CV Karya Mandiri dengan parameter wajib usage dan `format` `csv`
26. Verifikasi ketiga request ditolak dengan status 403
27. Verifikasi respons tidak memuat baris file export maupun baris Usage

### TC-AC-DS-604: Principal tanpa capability membaca daftar export, Usage, dan export Usage lewat API ditolak

28. Kirim request `POST /v2/enterprise-management/device-skus/export` lewat klien HTTP dengan token `noCapabilitySku` dengan parameter wajib daftar dan `format` `csv`
29. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/list` untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token `noCapabilitySku` dengan parameter wajib usage (`page`, `limit`, `sortBy`, `sortOrder`, `columns`)
30. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/export` untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token `noCapabilitySku` dengan parameter wajib usage dan `format` `csv`
31. Verifikasi ketiga request ditolak dengan status 403
32. Verifikasi respons tidak memuat baris file export maupun baris Usage

### TC-AC-DS-519: Distributor dengan Local Registration nonaktif membuat SKU lewat API ditolak

33. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `totalControlDistOff` dengan payload valid (SKU `API-LR-OFF`)
34. Verifikasi respons ditolak dengan status 403
35. Logout lalu login sebagai Total Control Distributor PT Mandala Niaga (`totalControlDistOff_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTOFF_PASSWORD`)
36. Buka halaman `Settings > Device > Device SKU`, klik ikon Search, ketik `API-LR-OFF`, tekan Enter
37. Verifikasi Search `API-LR-OFF` pada List Distributor menampilkan "No results found" (tidak ada SKU baru)

## Notes

- `K-1`: TC kelas a (defense-in-depth) dengan Expected respons API (status respons dan state data) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-device-sku-backend.md`; langkah request langsung hanya mengasersi status respons dan state data (8b butir 1). Rujukan ID TC: 512, 513, 514, 519, 522, 603, 604.
- Langkah penghubung tanpa `Verifikasi`: pencatatan baseline N_SKU, muat ulang List, penghapusan Search, dan langkah 35 (ganti akun eksplisit; sesi dikembalikan ke akun default suite di hook `after`).
- Urutan TC 519 dipindah ke akhir karena satu-satunya blok yang mengganti akun UI; alasannya mencegah ganti akun berulang (S-05 urutan, S-07).
- Spec ini melebihi sekitar 35 langkah; alasan: semua blok satu kelas harness (a, `K-1`) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna (Smell, bagian 3 prinsip 13). Jumlah langkah 37.
- Temuan untuk QA:
  - TC 512 Expected butir b tidak menyebut jumlah awal; spec memakai baseline N_SKU yang dicatat sebelum request. Plan menyebut akun UI #15, #8, #17, #1; akun #15 dan #8 hanya dipakai sebagai token API karena Partner dan Principal tanpa capability tidak membuka Device SKU.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
