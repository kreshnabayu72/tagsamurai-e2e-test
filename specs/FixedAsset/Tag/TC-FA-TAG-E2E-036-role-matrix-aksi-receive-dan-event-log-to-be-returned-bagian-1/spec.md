---
id: TC-FA-TAG-E2E-036-role-matrix-aksi-receive-dan-event-log-to-be-returned-bagian-1
title: "Role Matrix: Aksi Receive dan Event Log To Be Returned per Role (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-163
  - TC-FA-TAG-164
  - TC-FA-TAG-165
  - TC-FA-TAG-166
  - TC-FA-TAG-167
coverage:
  web: automated
---

# Role Matrix: Aksi Receive dan Event Log To Be Returned per Role (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Manage asset & TAG (Read) dengan scope group Disposal Center | MR_SDC | `manageAssetTagReadDenganScopeGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_SDC_PASSWORD` |
| 4 | Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse | UP_DC_RHQ | `manageAssetTagDenganUpdateDiGroupDisposalCenterDanReadDiGroupHqWarehouse_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_RHQ_PASSWORD` |
| 5 | Manage asset & TAG (Read) dengan assign group Disposal Center | MR_ADC | `manageAssetTagReadDenganAssignGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_ADC_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup Tag To Be Returned (himpunan minimum; jumlah total tidak diasersi): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.).
- Data: Untuk blok 5: Tag RF-00071 (Return Group Disposal Center), Tag RF-00099 (Return Group anak dari Disposal Center), Tag NF-00092 (Return Group HQ Warehouse, di luar scope).
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### Total Control (TC-FA-TAG-163)

1. Klik Tab `To Be Returned`
2. Verifikasi tombol scan `Receive TAG` dan `Event Log` tampil (Show)
3. Klik kebab baris RF-00071
4. Verifikasi menu aksi baris memuat `Receive Manually`
5. Centang baris RF-00071
6. Verifikasi Bulk Action Bar tampil dengan aksi `Receive Manually`

### Read Only (TC-FA-TAG-164)

7. Ganti akun: logout dari akun Total Control [TC], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
8. Klik Tab `To Be Returned`
9. Verifikasi tombol `Receive TAG` Hidden (tidak dirender)
10. Klik kebab baris RF-00071
11. Verifikasi menu aksi baris tidak memuat `Receive Manually` (Hidden)
12. Centang baris RF-00071
13. Verifikasi Bulk Action `Receive Manually` tidak tersedia
14. Verifikasi Search, Filter, Download, dan `Event Log` tampil serta aktif
15. Verifikasi sedikitnya baris Tag RF-00071, RF-00088, dan NF-00092 terlihat (seluruh scope client)
16. Klik tombol `Event Log`
17. Verifikasi modal `Event Log: To Be Returned` terbuka
18. Tutup modal Event Log

### Manage asset & TAG (Read) dengan scope group Disposal Center (TC-FA-TAG-165)

19. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read) dengan scope group Disposal Center [MR_SDC], lalu buka Fixed Asset > TAG tab Paired
20. Klik Tab `To Be Returned`
21. Verifikasi tombol `Receive TAG` Hidden
22. Klik kebab baris RF-00071
23. Verifikasi aksi `Receive Manually` Hidden pada baris RF-00071
24. Centang baris RF-00071
25. Verifikasi aksi `Receive Manually` tidak tersedia sebagai Bulk Action
26. Verifikasi tombol `Event Log` tampil (Show)
27. Klik tombol `Event Log`
28. Verifikasi modal `Event Log: To Be Returned` terbuka
29. Tutup modal Event Log

### Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse (TC-FA-TAG-166)

30. Ganti akun: logout dari akun Manage asset & TAG (Read) dengan scope group Disposal Center [MR_SDC], login dengan akun Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse [UP_DC_RHQ], lalu buka Fixed Asset > TAG tab Paired
31. Klik Tab `To Be Returned`
32. Verifikasi tombol scan `Receive TAG` tampil (Show)
33. Klik kebab baris RF-00071 (Return Group Disposal Center)
34. Verifikasi baris RF-00071 menampilkan aksi `Receive Manually`
35. Klik kebab baris NF-00092 (Return Group HQ Warehouse)
36. Verifikasi baris NF-00092 tidak menampilkan aksi `Receive Manually` (Hidden)

### Manage asset & TAG (Read) dengan assign group Disposal Center (TC-FA-TAG-167)

37. Ganti akun: logout dari akun Manage asset & TAG dengan Update di group Disposal Center dan Read di group HQ Warehouse [UP_DC_RHQ], login dengan akun Manage asset & TAG (Read) dengan assign group Disposal Center [MR_ADC], lalu buka Fixed Asset > TAG tab Paired
38. Klik Tab `To Be Returned`
39. Verifikasi baris RF-00071 dan RF-00099 tampil
40. Verifikasi baris NF-00092 tidak tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 7, 18, 19, 29, 30, 37.
- Pembagian TC lintas spec: TC-FA-TAG-168 sampai 170, 1489, dan 1490 ada di spec `TC-FA-TAG-E2E-037-role-matrix-aksi-receive-dan-event-log-to-be-returned-bagian-2`.
- Spec di atas smell 35 langkah (40 langkah). Alasan: semua blok satu topik (aksi Receive dan Event Log di tab To Be Returned) dengan dataset yang sama; tiap blok role berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-164 butir c ("Search, Filter, Download, dan Event Log Show serta aktif") tidak menyebut cara menilai aktif; spec mengasersi tampil dan aktif tanpa interaksi tambahan.
  - TC-165 dan TC-167 memakai Role `Manage asset & TAG (Read)` dengan catatan `scope group` dan `assign group` (Disposal Center) yang masing-masing punya baris Pre-setup sendiri; spec memakai baris itu.
  - TC-167 menyebut Tag RF-00099 (Return Group anak dari Disposal Center) yang tidak ada di Pre-setup Tag To Be Returned TC lain; spec membuatnya lewat seeding. Karena RF-00099 di-seed untuk blok 5, himpunan Tag To Be Returned saat run dapat memuat lebih dari tiga baris; langkah 15 (TC-FA-TAG-164) mengasersi sedikitnya tiga baris Pre-setup, bukan jumlah total (keputusan user 2026-11-04, bagian 8b butir 10).
