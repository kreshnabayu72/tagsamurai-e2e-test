---
id: TC-FA-TAG-E2E-056-overlay-scan-pemblokiran-dialog-d-01-d-06-d-08-dan-urutan-bagian-3
title: "Overlay Scan Replace TAG: Dialog Blok D-06 Aset di Luar Scope dan Group Read-Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-242
  - TC-FA-TAG-243
  - TC-FA-TAG-261
coverage:
  web: automated
---

# Overlay Scan Replace TAG: Dialog Blok D-06 Aset di Luar Scope dan Group Read-Only

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Kode | Email (Pre-setup TC) | Env password | Blok |
|---|---|---|---|---|
| Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | MU_UPA | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` | TC-FA-TAG-242 dan TC-FA-TAG-261 |
| Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B | UP_PA_ROPB | `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD` | TC-FA-TAG-243 |

- Nama env password usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`. Login MU_UPA di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dalam keadaan satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin. Seed idempotent aset, Tag, dan Asset Status lewat fixture backend.
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis):
  - AST-0011 'Excavator 20 Ton - 11' (Group Plant B, TAG Type Asset Name RFID): satu Tag RFID `RF-00101` berstatus Paired.
  - AST-0012 'Excavator 20 Ton - 12' (Group Plant B, Asset Status In Disposal Process): masih punya Tag RFID `RF-00102` berstatus Paired.
  - Stok Global: Tag RFID `RF-00412` dan `RF-00415` berstatus Available, Tag NFC `NF-00500` berstatus Available (dipakai sebagai precondition TC, tidak diasersi).
- Pemulihan di hook `after`: kembalikan data aset, Tag, dan Asset Status di atas ke keadaan awal bila seeding mengubahnya. Spec ini tidak menekan `[Submit]`.
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

### Blok MU_UPA (Update pada Group Plant A)

TC-FA-TAG-242:

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00101` milik aset di Group Plant B dengan simulator reader
3. Verifikasi dialog judul `Access Restricted`, body `You don't have access to this asset.`, tombol `[OK]`
4. Verifikasi teks dialog tidak memuat Asset ID AST-0011
5. Verifikasi Dialog Replace TAG tidak terbuka
6. Klik `[OK]`

TC-FA-TAG-261:

7. Klik tombol scan `Replace TAG` di toolbar tab Paired
8. Pindai Tag `RF-00102` dengan simulator reader
9. Verifikasi dialog judul `Access Restricted`, body `You don't have access to this asset.`, tombol `[OK]`
10. Verifikasi dialog dengan body `This asset is in disposal process or already disposed.` tidak tampil
11. Klik `[OK]`

### Blok UP_PA_ROPB (Update pada Group Plant A, hanya Read pada Group Plant B)

12. Ganti akun: Logout dari akun MU_UPA, login sebagai UP_PA_ROPB, lalu buka Fixed Asset > TAG tab Paired

TC-FA-TAG-243:

13. Klik tombol scan `Replace TAG` di toolbar tab Paired
14. Pindai Tag `RF-00101` dengan simulator reader
15. Verifikasi dialog judul `Access Restricted`, body `You don't have access to this asset.`, tombol `[OK]`
16. Verifikasi Dialog Replace TAG tidak terbuka

## Notes

- Mode: FE+BE. Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a). TC-FA-TAG-240, TC-FA-TAG-241, TC-FA-TAG-244, dan TC-FA-TAG-262 ada di spec 052.
- Perubahan urutan (S-05): urutan TC sumber 242, 243, 261 menjadi 242, 261, 243. Alasan: TC-FA-TAG-242 dan TC-FA-TAG-261 memakai akun MU_UPA sehingga ganti akun terjadi sekali.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6 dan 11 (menutup dialog blok lewat `[OK]`), 12 (ganti akun).
- Absence (langkah 4, 5, 10, dan 16): didahului Verifikasi dialog `Access Restricted` yang tampil (langkah 3, 9, dan 15) sebagai anchor positif (bagian 8b butir 2). Dialog D-01 pada langkah 10 dikenali dari teks body yang disebut TC-FA-TAG-240.
- Temuan untuk QA:
  - TC-FA-TAG-261 memakai AST-0012 dengan Asset Status In Disposal Process tanpa menyebut cara mengaturnya; spec menuliskannya sebagai seed lewat fixture BE.
  - TC-FA-TAG-243 menyebut aset AST-0011 di Group Plant B yang "hanya Read" untuk user; hak parsial per group diasumsikan dari Role di Pre-setup TC dan tidak diatur ulang oleh spec.
  - Tidak ada Post Condition TC yang punya langkah observasi pada spec ini ("Tidak ada data yang berubah" tidak diasersi).
  - Role UP_PA_ROPB (Pre-setup 102) hampir kembar dengan "Update di group Plant A dan Read di group Plant B" (UP_PA_RPB); spec memakai UP_PA_ROPB sesuai teks Role di TC-FA-TAG-243.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
