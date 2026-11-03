---
id: TC-FA-TAG-E2E-038-pemegang-update-return-group-menyelesaikan-receive
title: "Pemegang Update pada Return Group Menyelesaikan Receive"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-171
  - TC-FA-TAG-172
  - TC-FA-TAG-173
coverage:
  web: automated
---

# Pemegang Update pada Return Group Menyelesaikan Receive

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG dengan Update di group Disposal Center | UP_DC | `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_PASSWORD` |
| 2 | Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse | UP_DC_RHQ | `manageAssetTagDenganUpdateDiGroupDisposalCenterDanReadDiGroupHqWarehouse_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_RHQ_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.).
- Data: Note: Tag rusak saat serah terima.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): memindai kode Tag lewat simulator reader RFID/NFC USB (reader tersambung, satu reader, aktif, sudah disinkronkan di Global Settings > Handheld Reader).
- Kemampuan teknis (disediakan tim FE/BE): memulihkan Tag RF-00071 ke daftar To Be Returned lewat fixture backend sebagai pelaku kedua (sesi API).
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Receive TAG (TC-FA-TAG-171)

1. Klik Tab `To Be Returned`
2. Klik tombol `Receive TAG`
3. Pindai Tag RF-00071 dengan simulator reader
4. Klik `[Receive]`
5. Verifikasi dialog `Receive TAG` menutup
6. Verifikasi toast `Success, TAG has been received.` tampil
7. Verifikasi baris RF-00071 hilang dari tabel To Be Returned

### Receive Manually (TC-FA-TAG-172)

8. Pulihkan Tag RF-00071 ke daftar To Be Returned lewat fixture backend hingga baris RF-00071 tersimpan
9. Muat ulang halaman (F5), lalu klik Tab `To Be Returned`
10. Buka menu aksi baris RF-00071, lalu klik `Receive Manually`
11. Isi Note `Tag rusak saat serah terima`
12. Klik `[Submit]`
13. Verifikasi dialog menutup
14. Verifikasi toast `Success, TAG has been received as damaged/missing.` tampil
15. Verifikasi baris RF-00071 hilang dari tabel

### Return Group yang hanya Read (TC-FA-TAG-173)

16. Ganti akun: logout dari akun Manage asset & TAG dengan Update di group Disposal Center [UP_DC], login dengan akun Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse [UP_DC_RHQ], lalu buka Fixed Asset > TAG tab To Be Returned
17. Klik Tab `To Be Returned`
18. Klik tombol `Receive TAG`
19. Pindai Tag NF-00092 (Return Group HQ Warehouse) dengan simulator reader
20. Verifikasi Error inline `You don't have access to this TAG's group.` tampil
21. Verifikasi Tag NF-00092 tidak masuk daftar sesi
22. Verifikasi penghitung tetap `0 TAGs scanned`
23. Tutup dialog `Receive TAG`

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 8, 9, 16, 23.
- Langkah 8 dan 9 memulihkan RF-00071 karena TC-FA-TAG-171 dan TC-FA-TAG-172 sama-sama memakai RF-00071 (TC-FA-TAG-171 menerimanya).
- Simulator reader dipakai sebagai langkah rutin untuk memindai Tag; spec ini tidak menguji kondisi reader.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01). Post Condition TC-171 dan TC-172 (status Tag di registri Global, satu entri Event Log) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-171 dan TC-172 memakai RF-00071 yang sama dan TC tidak menyebut pemulihannya; spec menambah langkah pemulihan lewat fixture backend.
  - Tombol dialog ditulis `[Receive]` dan `[Submit]` mengikuti langkah TC ("Klik Receive", "Klik Submit").
