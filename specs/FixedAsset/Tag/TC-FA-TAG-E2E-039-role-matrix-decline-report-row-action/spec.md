---
id: TC-FA-TAG-E2E-039-role-matrix-decline-report-row-action
title: "Role Matrix: Row Action Decline Report"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-174
  - TC-FA-TAG-175
  - TC-FA-TAG-176
  - TC-FA-TAG-177
  - TC-FA-TAG-178
  - TC-FA-TAG-179
coverage:
  web: automated
---

# Role Matrix: Row Action Decline Report

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Manage asset & TAG (Read) dengan scope group Plant B | MR_SPB | `manageAssetTagReadDenganScopeGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_SPB_PASSWORD` |
| 4 | Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B | UP_PA_RPB | `manageAssetTagDenganUpdateDiGroupPlantADanReadDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_RPB_PASSWORD` |
| 5 | Manage asset & TAG dengan Update di group Plant B | UP_PB | `manageAssetTagDenganUpdateDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PB_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Aset AST-0020 (Excavator 20 Ton - 20, group Plant B) dengan Tag RF-00130 punya laporan terbuka Damaged dari task Existence Audit; aset AST-0011 (Excavator 20 Ton - 11, group Plant B) dengan Tag RF-00101 tanpa laporan terbuka; Reason: Tag masih terbaca.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): membaca status laporan Tag (Declined) lewat kemampuan baca state backend untuk Expected TC-177.
- State global (status Tag dan laporan) dipulihkan lewat fixture; efek log tidak terpulihkan (butir A-15).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 26).

## Test Steps

### Total Control (TC-FA-TAG-174 dan TC-FA-TAG-179)

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Klik kebab baris Excavator 20 Ton - 20
3. Verifikasi menu aksi memuat `Decline Report` setelah `Replace TAG`
4. Verifikasi Ikon `CloseCircleLine` dengan severity danger pada `Decline Report`
5. Klik kebab baris Excavator 20 Ton - 11
6. Verifikasi menu aksi hanya memuat `Replace TAG`
7. Verifikasi `Decline Report` Hidden

### Read Only (TC-FA-TAG-175)

8. Ganti akun: logout dari akun Total Control [TC], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
10. Klik kebab baris Excavator 20 Ton - 20
11. Verifikasi aksi `Decline Report` Hidden

### Manage asset & TAG (Read) dengan scope group Plant B (TC-FA-TAG-176)

12. Ganti akun: logout dari akun Read Only [RO], login dengan akun Manage asset & TAG (Read) dengan scope group Plant B [MR_SPB], lalu buka Fixed Asset > TAG tab Paired
13. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
14. Klik kebab baris Excavator 20 Ton - 20
15. Verifikasi aksi `Decline Report` Hidden

### Update di group Plant A dan Read di group Plant B (TC-FA-TAG-178)

16. Ganti akun: logout dari akun Manage asset & TAG (Read) dengan scope group Plant B [MR_SPB], login dengan akun Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B [UP_PA_RPB], lalu buka Fixed Asset > TAG tab Paired
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
18. Klik kebab baris Excavator 20 Ton - 20
19. Verifikasi aksi `Decline Report` Hidden

### Update di group Plant B (TC-FA-TAG-177)

20. Ganti akun: logout dari akun Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B [UP_PA_RPB], login dengan akun Manage asset & TAG dengan Update di group Plant B [UP_PB], lalu buka Fixed Asset > TAG tab Paired
21. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
22. Klik kebab baris Excavator 20 Ton - 20
23. Verifikasi aksi `Decline Report` tampil pada baris
24. Klik `Decline Report` pada baris Excavator 20 Ton - 20
25. Isi Reason `Tag masih terbaca`
26. Klik `[Submit]`
27. Verifikasi toast `Success, report has been declined.` tampil
28. Verifikasi Laporan RF-00130 berstatus Declined

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 8, 12, 16, 20.
- TC-FA-TAG-179 dijalankan di blok Total Control bersama TC-FA-TAG-174 (akun sama), dan TC-FA-TAG-177 (yang mengubah state) dijalankan terakhir; Expected tiap TC tetap diasersi.
- Menu aksi baris dibuka lewat kebab baris sebagai langkah penghubung karena TC hanya menyebut `Buka menu aksi baris`.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 26).
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-177 butir b ("laporan RF-00130 berstatus Declined") tidak menyebut tempat status laporan teramati; spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE). Post Condition TC-177 ("Tag RF-00130 tetap Paired") tanpa langkah observasi tidak diasersi.
  - TC-175, TC-176, dan TC-178 mengasersi `Decline Report` Hidden pada menu aksi aset dengan laporan terbuka; menu aksi dibuka lewat kebab baris sehingga anchor positifnya adalah popup Plant B yang sudah terbuka.
