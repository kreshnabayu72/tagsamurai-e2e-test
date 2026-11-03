---
id: TC-AC-DS-E2E-188-edit-saving-state-dan-klik-ganda-save
title: "Edit SKU: Saving State pada Tombol Save dan Klik Ganda Cepat Menghasilkan Satu Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-250
  - TC-AC-DS-251
coverage:
  web: automated
---

# Edit SKU: Saving State pada Tombol Save dan Klik Ganda Cepat Menghasilkan Satu Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke nilai Pre-setup #29 (Device Name `UHF Handheld Reader`, SKU `HHR-ARC-200`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0, 1 foto, Last Modified `28/09/26 14:40`). Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen; Last Modified baris `HHR-ARC-200` berubah.
- Kemampuan teknis: `Spectra.intercept()` menahan respons API update SKU di atas backend nyata (bagian 6); intercept dilepas segera setelah asersi (S-09).
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-250: Saving state

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Ubah Model/Type menjadi `H-SV`
3. Tahan respons API update SKU dengan intercept
4. Klik `[Save]`
5. Verifikasi tombol `[Save]` menampilkan loading
6. Verifikasi tombol `[Save]` disabled
7. Verifikasi kontrol input, `[Clear Field]`, dan ikon `✕` disabled
8. Lepas tahanan respons API update SKU
9. Tunggu aksi selesai (popup Edit tertutup)

### TC-AC-DS-251: klik ganda cepat Save

10. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
11. Ubah Model/Type menjadi `H-DB`
12. Tunggu toast lama hilang otomatis
13. Klik `[Save]` dua kali dengan cepat
14. Verifikasi tombol `[Save]` disabled segera setelah klik pertama
15. Verifikasi muncul toast sukses "Success, device SKU has been updated."
16. Verifikasi hanya satu toast sukses yang tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah 8 melepas intercept segera setelah asersi state sementara (S-09). Asersi state sementara (loading, disabled) ditulis sebelum langkah yang melepas tahanan (bagian 8b butir 5).
- Temuan untuk QA: TC-250 tidak menyatakan hasil setelah respons dilepas; spec menunggu aksi selesai sebagai langkah penghubung tanpa asersi (bagian 8b butir 8). TC-251 menyebut "hanya satu toast sukses" tanpa langkah menunggu toast lama; toast TC-250 dianggap sudah hilang oleh langkah penghubung.
- Post Condition TC-251 (satu perubahan Model/Type `H-DB`, satu entri Edit Model/Type pada tiap surface log) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
