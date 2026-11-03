---
id: TC-FA-TAG-E2E-040-role-matrix-report-tag-dan-cancel-report-dari-modul-audit
title: "Role Matrix: Report TAG dan Cancel Report dari Modul Audit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-180
  - TC-FA-TAG-181
  - TC-FA-TAG-182
  - TC-FA-TAG-183
  - TC-FA-TAG-184
  - TC-FA-TAG-185
  - TC-FA-TAG-186
coverage:
  web: automated
---

# Role Matrix: Report TAG dan Cancel Report dari Modul Audit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Staff Auditor (tidak memegang Manage asset & TAG) | SA_NOTAG | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |
| 2 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 3 | Manage asset & TAG dengan Update di group Plant B | UP_PB | `manageAssetTagDenganUpdateDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PB_PASSWORD` |
| 4 | Manage asset & TAG (Read) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |
| 5 | Approver | APR | `approver_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_APR_PASSWORD` |
| 6 | Staff Auditor | SA | `staffAuditor_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Task Existence Audit dengan item aset AST-0020 (Excavator 20 Ton - 20, Tag RF-00130 tanpa laporan terbuka) berstatus In Audit; untuk TC-185 dan TC-186 Tag RF-00130 punya laporan terbuka Damaged yang dilaporkan oleh Staff Auditor; task Condition Audit dengan item AST-0020 (TC-186).
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): membuat laporan terbuka Damaged untuk Tag RF-00130 sebagai pelaku kedua (sesi API) lewat fixture backend.
- Kemampuan teknis (disediakan tim FE/BE): dua task Audit (Existence Audit dan Condition Audit) milik spec dengan item AST-0020.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Staff Auditor (tidak memegang Manage asset & TAG) (TC-FA-TAG-180)

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action `Report TAG` pada baris Excavator 20 Ton - 20
3. Verifikasi dialog `Report TAG` terbuka
4. Verifikasi dialog memuat Checkbox `TAG to report`, Radio `Report Type`, Textarea `Note`, dan footer `[Cancel]` `[Submit]`
5. Klik `[Cancel]` pada dialog `Report TAG`

### Total Control (TC-FA-TAG-181)

6. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], login dengan akun Total Control [TC], lalu buka Fixed Asset > TAG tab Paired
7. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
8. Pilih row action `Report TAG` pada baris Excavator 20 Ton - 20
9. Verifikasi dialog `Report TAG` Show (terbuka)
10. Klik `[Cancel]` pada dialog `Report TAG`

### Update di group Plant B (TC-FA-TAG-182)

11. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG dengan Update di group Plant B [UP_PB], lalu buka Fixed Asset > TAG tab Paired
12. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
13. Buka menu aksi baris Excavator 20 Ton - 20 dan coba pilih aksi `Report TAG`
14. Verifikasi dialog `Report TAG` Hidden (tidak dapat dibuka oleh pemegang Manage asset & TAG)

### Manage asset & TAG (Read) (TC-FA-TAG-183)

15. Ganti akun: logout dari akun Manage asset & TAG dengan Update di group Plant B [UP_PB], login dengan akun Manage asset & TAG (Read) [MR], lalu buka Fixed Asset > TAG tab Paired
16. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
17. Buka menu aksi baris Excavator 20 Ton - 20 dan coba pilih aksi `Report TAG`
18. Verifikasi dialog `Report TAG` Hidden

### Approver (TC-FA-TAG-184)

19. Ganti akun: logout dari akun Manage asset & TAG (Read) [MR], login dengan akun Approver [APR], lalu buka Fixed Asset > TAG tab Paired
20. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
21. Buka menu aksi baris Excavator 20 Ton - 20
22. Verifikasi aksi `Report TAG` Hidden pada baris item
23. Buat laporan terbuka Damaged untuk Tag RF-00130 lewat fixture backend hingga laporan tersimpan

### Staff Auditor (TC-FA-TAG-185 dan TC-FA-TAG-186)

24. Ganti akun: logout dari akun Approver [APR], login dengan akun Staff Auditor [SA], lalu buka Fixed Asset > TAG tab Paired
25. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
26. Pilih row action `Cancel Report TAG` pada baris Excavator 20 Ton - 20
27. Verifikasi dialog `Cancel Report` terbuka
28. Verifikasi dialog memuat Summary, Checkbox `TAG to cancel`, Textarea `Reason`, dan footer `[Keep Report]` `[Cancel Report]`
29. Klik `[Keep Report]`
30. Buka modul Audit > Task Detail task Condition Audit
31. Buka menu aksi baris Excavator 20 Ton - 20
32. Verifikasi aksi `Cancel Report TAG` Hidden pada task Condition Audit

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 5, 6, 10, 11, 15, 19, 23, 24, 29.
- Aksi `Report TAG` dan `Cancel Report TAG` dijalankan dari modul Audit (Task Detail), bukan dari halaman TAG; hook `beforeEach` suite membuka Fixed Asset > TAG dan langkah pembuka tiap blok berpindah ke modul Audit.
- TC-FA-TAG-186 dijalankan bersama TC-FA-TAG-185 (akun Staff Auditor sama); Expected tiap TC tetap diasersi.
- Laporan terbuka Damaged untuk TC-FA-TAG-185 dan 186 dibuat lewat fixture backend sebagai pelaku kedua (sesi API) pada langkah penghubung sebelum blok Staff Auditor.
- Pembagian TC lintas spec: TC-FA-TAG-187 dan 188 ada di spec 381.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Kode Tag `RF-00130` dipakai TC untuk aset AST-0220 (TC-144 sampai TC-162) dan untuk aset AST-0020 (TC-174 sampai TC-188); kedua dataset tidak dapat ada bersamaan di registri Global. Spec menulis literal sesuai TC dan fixture backend menyiapkan dataset tiap spec.
  - TC-185 dan TC-186 tidak menyebut tab pada Task Detail; spec memakai tab In Audit hanya pada TC yang menyebutnya (TC-180 sampai TC-184).
  - TC-182 dan TC-183 menyebut "Coba membuka" Dialog Report TAG dari aksi yang tidak tersedia; spec menulis langkah membuka menu aksi lalu mengasersi dialog Hidden.
  - TC-180 menyebut Dialog `Report TAG` dengan footer `[Cancel] [Submit]`; label tombol mengikuti TC (tidak ada langkah submit).
