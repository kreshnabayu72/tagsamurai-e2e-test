---
id: TC-FA-TAG-E2E-037-role-matrix-aksi-receive-dan-event-log-to-be-returned-bagian-2
title: "Role Matrix: Aksi Receive dan Event Log To Be Returned per Role (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-168
  - TC-FA-TAG-169
  - TC-FA-TAG-170
  - TC-FA-TAG-1489
  - TC-FA-TAG-1490
coverage:
  web: automated
---

# Role Matrix: Aksi Receive dan Event Log To Be Returned per Role (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 2 | Manage asset & TAG (Read) dengan assign group Disposal Center | MR_ADC | `manageAssetTagReadDenganAssignGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_ADC_PASSWORD` |
| 3 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 4 | Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse | UP_DC_RHQ | `manageAssetTagDenganUpdateDiGroupDisposalCenterDanReadDiGroupHqWarehouse_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_RHQ_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.).
- Data: Event Log berisi entri RF-00071 (Return Group Disposal Center) dan entri NF-00093 (Return Group HQ Warehouse) sebagai entri terbaru.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Read Only (TC-FA-TAG-168)

1. Klik Tab `To Be Returned`
2. Verifikasi baris RF-00071, RF-00088, dan NF-00092 semuanya tampil

### Manage asset & TAG (Read) dengan assign group Disposal Center (TC-FA-TAG-169)

3. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read) dengan assign group Disposal Center [MR_ADC], lalu buka Fixed Asset > TAG tab Paired
4. Klik Tab `To Be Returned`
5. Klik tombol `Event Log`
6. Verifikasi entri RF-00071 tampil
7. Verifikasi entri NF-00093 tidak tampil
8. Tutup modal Event Log

### Total Control (TC-FA-TAG-170)

9. Ganti akun: logout dari akun Manage asset & TAG (Read) dengan assign group Disposal Center [MR_ADC], login dengan akun Total Control [TC], lalu buka Fixed Asset > TAG tab Paired
10. Klik Tab `To Be Returned`
11. Klik tombol `Event Log`
12. Verifikasi entri RF-00071 dan NF-00093 keduanya tampil
13. Tutup modal Event Log

### Update di Disposal Center dan Read di HQ Warehouse (TC-FA-TAG-1489 dan TC-FA-TAG-1490)

14. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse [UP_DC_RHQ], lalu buka Fixed Asset > TAG tab Paired
15. Klik Tab `To Be Returned`
16. Klik checkbox baris NF-00092 (Return Group HQ Warehouse)
17. Verifikasi checkbox baris NF-00092 tetap tidak tercentang
18. Verifikasi Bulk Action Bar tidak tampil
19. Klik checkbox baris RF-00071 (Return Group Disposal Center)
20. Verifikasi checkbox baris RF-00071 tercentang
21. Verifikasi Bulk Action Bar tampil dengan aksi `Receive Manually`
22. Hapus centang baris RF-00071
23. Klik checkbox header tabel
24. Verifikasi baris RF-00071 dan RF-00088 tercentang
25. Verifikasi baris NF-00092 (Return Group HQ Warehouse) tidak tercentang
26. Verifikasi Bulk Action Bar menampilkan `2 TAGs selected`
27. Klik Bulk Action `Receive Manually`
28. Verifikasi dialog `Receive Manually` terbuka dengan ringkasan `2 TAGs`
29. Verifikasi dialog tidak memuat NF-00092

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 3, 8, 9, 13, 14, 22.
- Pembagian TC lintas spec: TC-FA-TAG-163 sampai 167 ada di spec `TC-FA-TAG-E2E-036-role-matrix-aksi-receive-dan-event-log-to-be-returned-bagian-1`.
- TC-FA-TAG-1490 dijalankan sesudah TC-FA-TAG-1489 dengan akun yang sama; langkah 22 menghapus centang baris RF-00071 supaya klik checkbox header berangkat dari seleksi kosong.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Event Log di TC-170 memakai NF-00093 sedangkan Pre-setup Tag To Be Returned memuat NF-00092; spec mengikuti TC (TC-169 dan TC-170 memakai NF-00093).
