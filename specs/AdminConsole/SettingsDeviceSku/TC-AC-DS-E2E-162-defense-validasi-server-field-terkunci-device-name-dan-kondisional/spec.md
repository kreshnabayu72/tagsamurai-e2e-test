---
id: TC-AC-DS-E2E-162-defense-validasi-server-field-terkunci-device-name-dan-kondisional
title: "Defense-in-Depth: Server Menolak Field Terkunci, Device Name Category Lain, dan Field Kondisional Tidak Sesuai Ancestry"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-523
  - TC-AC-DS-524
  - TC-AC-DS-525
coverage:
  web: automated
---

# Defense-in-Depth: Server Menolak Field Terkunci, Device Name Category Lain, dan Field Kondisional Tidak Sesuai Ancestry

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30). Token API akun #1 melalui sesi API aktor.
- Data Dinamis: SKU `API-ANC-01` dan `API-ANC-02` (payload TC 525) tidak boleh tersimpan; hook `after` memastikan tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server (multipart/form-data) dengan token sesi API aktor akun yang disebut; ID record SKU target (`{id}`) dibaca lewat fixture BE (TC tidak menyebut caranya). Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- Pengamat UI: sesi web akun yang login di hook `before`; observasi state data (List dan form Edit) mengikuti langkah TC dan bukan perilaku FE atas respons request langsung.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-523: Mengubah field terkunci lewat API pada SKU berstok ditolak seluruhnya

1. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token `totalControlSku` dengan `sku` `HHR-ARC-199`, `model` `H199`, dan `rangeType` `Short Range` (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan kecuali field yang disebut)
2. Verifikasi respons ditolak dengan status 422
3. Ketik Search `HHR-ARC-100`, tekan Enter, klik ⋯ pada baris `HHR-ARC-100` lalu pilih `Edit`
4. Verifikasi field SKU tetap `HHR-ARC-100`
5. Verifikasi field Model/Type tetap `H100`
6. Verifikasi field Range Type tetap `Long Range`
7. Tekan Esc

### TC-AC-DS-524: Memakai Device Name dari Category lain lewat API ditolak

8. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `HHR-ARC-200` lewat klien HTTP dengan token `totalControlSku` dengan `deviceNameId` Device Name `Rugged Handheld Reader` (Category Barcode Handheld) (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan kecuali field yang disebut)
9. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `HHR-ARC-200` lewat klien HTTP dengan token `totalControlSku` dengan `deviceNameId` Device Name `Asset TAG` (Category Asset TAG) (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan kecuali field yang disebut)
10. Verifikasi kedua request ditolak dengan status 422
11. Klik `(←)` pada kotak Search, ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
12. Verifikasi Category tersimpan tetap `UHF Handheld`
13. Verifikasi Device Name tersimpan tetap `UHF Handheld Reader`
14. Tekan Esc

### TC-AC-DS-525: Field kondisional yang tidak sesuai ancestry Category ditolak server

15. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `totalControlSku` dengan SKU `API-ANC-01`, Device Name `Asset TAG` (Category Asset TAG), Port `8080` dan Range Type `Long Range` (payload POST lengkap: `deviceNameId`, `brandId`, `sku`, `model`, `firstImage`, dan `defaultImage` terisi nilai valid kecuali field yang disebut)
16. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `totalControlSku` dengan SKU `API-ANC-02`, Device Name `UHF Handheld Reader` (Category UHF Handheld) tanpa Range Type (payload POST lengkap: `deviceNameId`, `brandId`, `sku`, `model`, `firstImage`, dan `defaultImage` terisi nilai valid kecuali field yang disebut)
17. Verifikasi kedua request ditolak dengan status 422
18. Klik `(←)` pada kotak Search, klik ikon Search, ketik `API-ANC`, tekan Enter
19. Verifikasi Search `API-ANC` menampilkan "No results found" (tidak ada SKU baru)

## Notes

- `K-1`: TC kelas a (defense-in-depth) dengan Expected respons API (status respons dan state data) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-device-sku-backend.md`; langkah request langsung hanya mengasersi status respons dan state data (8b butir 1). Rujukan ID TC: 523, 524, 525.
- Langkah penghubung tanpa `Verifikasi`: Search untuk menemukan baris target `HHR-ARC-100` dan `HHR-ARC-200` beserta penutupan Search (langkah 3, 11, dan 18, R-16, S-09).
- Pembagian TC lintas spec (S-05): Expected butir b TC-AC-DS-523 (Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tidak memuat entri baru untuk `HHR-ARC-100`) diasersi di spec 193, yang mengirim request penolakan sendiri dengan baseline log sendiri; spec ini mengasersi status respons dan state data (Expected butir a). TC 524 dan 525 tidak memuat Expected log.
- Pengecualian S-12 A-11: `HHR-ARC-100` dan `HHR-ARC-200` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target request yang ditolak; tidak ada data Pre-setup yang diubah spec ini (dinyatakan di `suite.md`). `API-ANC-01` dan `API-ANC-02` mengikuti kode literal TC dan tidak pernah tersimpan (permintaan ditolak).
- Temuan untuk QA:
  - TC 523 Expected butir a menggabungkan status 422 dan tiga nilai tersimpan; spec memecahnya per klausa. TC 524 dan 525 tidak mengamati log; spec mengikuti TC.
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
