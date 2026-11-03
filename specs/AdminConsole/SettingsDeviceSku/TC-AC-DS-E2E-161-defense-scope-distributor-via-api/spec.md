---
id: TC-AC-DS-E2E-161-defense-scope-distributor-via-api
title: "Defense-in-Depth: Distributor Mengubah atau Menghapus SKU Principal, Detail Distributor Lain, Brand Entitas Lain, dan Usage Lintas Scope"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-520
  - TC-AC-DS-521
  - TC-AC-DS-528
  - TC-AC-DS-605
coverage:
  web: automated
---

# Defense-in-Depth: Distributor Mengubah atau Menghapus SKU Principal, Detail Distributor Lain, Brand Entitas Lain, dan Usage Lintas Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Dewi Lestari, Modified By `Dewi L`): `totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Pendamping (hanya token sesi API pada langkah 23): Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), SKU Distributor (#31) dan Usage by Company (#32).
- Data Dinamis: SKU `API-BRD-01` (payload TC 528) tidak boleh tersimpan; hook `after` memastikan tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server (multipart/form-data) dengan token sesi API aktor akun yang disebut; ID record SKU target (`{id}`) dibaca lewat fixture BE (TC tidak menyebut caranya). Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- Pengamat UI: sesi web akun yang login di hook `before`; observasi state data (List) mengikuti langkah TC dan bukan perilaku FE atas respons request langsung.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-520: Distributor mengubah atau menghapus SKU Principal lewat API ditolak

1. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` (SKU Principal) lewat klien HTTP dengan token `totalControlDist` (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan `TAG-ARC-OBJ`)
2. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` (SKU Principal) lewat klien HTTP dengan token `totalControlDist`
3. Verifikasi kedua request ditolak dengan status 403 karena SKU Principal bukan milik Distributor (kepemilikan baris mengikuti `entity-isolation.md` §18.6)
4. Buka halaman `Settings > Device > Device SKU`, ketik Search `TAG-ARC-OBJ`, tekan Enter
5. Verifikasi SKU `TAG-ARC-OBJ` tetap ada pada List dengan Model/Type `T-OBJ`
6. Klik `(←)` pada kotak Search

### TC-AC-DS-521: Distributor membaca detail SKU milik Distributor lain lewat API tidak mengungkap keberadaannya

7. Kirim request `GET /v2/enterprise-management/device-skus/{id}` untuk Device SKU `NUS-LOC-01` (milik PT Nusantara Mitra) lewat klien HTTP dengan token `totalControlDist`
8. Verifikasi detail `NUS-LOC-01` ditolak dengan status 404 seolah SKU tidak ada
9. Kirim request `POST /v2/enterprise-management/device-skus/list` lewat klien HTTP dengan token `totalControlDist` dengan parameter wajib daftar (`page`, `limit`, `sortBy`, `sortOrder`, `columns`) dan `search` `NUS-LOC-01`
10. Kirim request `GET /v2/enterprise-management/device-skus/{id}` untuk Device SKU `LOC-NOR-01` (milik PT Cakra Distribusi) lewat klien HTTP dengan token `totalControlDist`
11. Verifikasi detail `LOC-NOR-01` milik aktor sukses dengan SKU `LOC-NOR-01` pada respons
12. Kirim request `POST /v2/enterprise-management/device-skus/list` lewat klien HTTP dengan token `totalControlDist` dengan parameter wajib daftar (`page`, `limit`, `sortBy`, `sortOrder`, `columns`) dan `search` `LOC-NOR-01`
13. Verifikasi daftar dengan Search `LOC-NOR-01` memuat `LOC-NOR-01`
14. Verifikasi daftar dengan Search `NUS-LOC-01` tidak memuat `NUS-LOC-01` (hasil kosong berarti SKU lain memang tidak terlihat, anchor: `LOC-NOR-01` termuat)

### TC-AC-DS-528: Brand milik entitas lain lewat API ditolak sebagai referensi stale

15. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `totalControlDist` dengan SKU `API-BRD-01` dan Brand `Arcturus` (Brand Principal) (payload POST lengkap: `deviceNameId`, `brandId`, `sku`, `model`, `firstImage`, dan `defaultImage` terisi nilai valid kecuali field yang disebut)
16. Verifikasi respons ditolak dengan status 422 dan error pada field `brandId` karena Brand harus berasal dari entitas pelaku
17. Buka halaman `Settings > Device > Device SKU`, klik ikon Search, ketik `API-BRD-01`, tekan Enter
18. Verifikasi Search `API-BRD-01` menampilkan "No results found" (tidak ada SKU baru)

### TC-AC-DS-605: Usage Device SKU lewat API tidak melintasi scope entitas

19. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/list` untuk Device SKU `LOC-NOR-01` (milik PT Cakra Distribusi) lewat klien HTTP dengan token `totalControlDist` dengan parameter wajib usage (`page`, `limit`, `sortBy`, `sortOrder`, `columns`)
20. Verifikasi Usage `LOC-NOR-01` oleh Distributor Cakra sukses dengan baris `PT Cakra Distribusi` (9) dan `PT Surya Logistik` (5)
21. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/list` untuk Device SKU `NUS-LOC-01` (milik PT Nusantara Mitra) lewat klien HTTP dengan token `totalControlDist` dengan parameter wajib usage (`page`, `limit`, `sortBy`, `sortOrder`, `columns`)
22. Verifikasi Usage `NUS-LOC-01` oleh Distributor Cakra ditolak dengan status 404 seolah SKU tidak ada
23. Kirim request `POST /v2/enterprise-management/device-skus/{id}/usage/list` untuk Device SKU `LOC-NOR-01` lewat klien HTTP dengan token `totalControlSku` (Principal) dengan parameter wajib usage (`page`, `limit`, `sortBy`, `sortOrder`, `columns`)
24. Verifikasi Usage `LOC-NOR-01` oleh Principal ditolak dengan status 404 karena SKU Distributor tidak terlihat bagi Principal

## Notes

- `K-1`: TC kelas a (defense-in-depth) dengan Expected respons API (status respons dan state data) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-device-sku-backend.md`; langkah request langsung hanya mengasersi status respons dan state data (8b butir 1). Rujukan ID TC: 520, 521, 528, 605.
- Langkah penghubung tanpa `Verifikasi`: Search `TAG-ARC-OBJ` untuk menemukan baris target dan penutupannya (langkah 4 dan 6, R-16, S-09).
- Pembagian TC lintas spec (S-05): Expected butir c TC-AC-DS-520 (Changelog Principal, System Log `Dewi Lestari`, dan Activity Log tidak memuat entri baru) diasersi di spec 193, yang mengirim request penolakan sendiri dengan user dan baseline log sendiri; spec ini mengasersi status respons dan state data (Expected butir a dan b).
- Pengecualian S-12 A-11: `TAG-ARC-OBJ`, `LOC-NOR-01`, dan `NUS-LOC-01` adalah SKU Pre-setup bernama literal tanpa suffix (dinyatakan di `suite.md`); tidak ada data Pre-setup yang diubah spec ini. `API-BRD-01` mengikuti kode literal TC dan tidak pernah tersimpan (permintaan ditolak).
- Temuan untuk QA:
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
