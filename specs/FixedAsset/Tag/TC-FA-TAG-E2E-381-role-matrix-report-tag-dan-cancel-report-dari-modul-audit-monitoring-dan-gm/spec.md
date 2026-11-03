---
id: TC-FA-TAG-E2E-381-role-matrix-report-tag-dan-cancel-report-dari-modul-audit-monitoring-dan-gm
title: "Role Matrix: Cancel Report TAG dari Modul Audit untuk Monitoring dan GM"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-187
  - TC-FA-TAG-188
coverage:
  web: automated
---

# Role Matrix: Cancel Report TAG dari Modul Audit untuk Monitoring dan GM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Monitoring | MON | `monitoring_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MON_PASSWORD` |
| 2 | GM | GM | `gm_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_GM_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Task Existence Audit dengan item aset AST-0020 (Excavator 20 Ton - 20, Tag RF-00130) berstatus In Audit; Tag RF-00130 punya laporan terbuka Damaged yang dilaporkan oleh Staff Auditor (dibuat langkah 1); Reason: Tag ternyata terbaca.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): membuat laporan terbuka Damaged untuk Tag RF-00130 sebagai pelaku kedua (sesi API) lewat fixture backend.
- Kemampuan teknis (disediakan tim FE/BE): satu task Existence Audit milik spec dengan item AST-0020.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Monitoring (TC-FA-TAG-187)

1. Buat laporan terbuka Damaged untuk Tag RF-00130 lewat fixture backend hingga laporan tersimpan
2. Buka modul Audit > Task Detail task Existence Audit
3. Buka menu aksi baris Excavator 20 Ton - 20
4. Verifikasi aksi `Cancel Report TAG` Hidden

### GM (TC-FA-TAG-188)

5. Ganti akun: logout dari akun Monitoring [MON], login dengan akun GM [GM], lalu buka Fixed Asset > TAG tab Paired
6. Buka modul Audit > Task Detail task Existence Audit
7. Pilih row action `Cancel Report TAG` pada baris Excavator 20 Ton - 20
8. Isi Reason `Tag ternyata terbaca`
9. Klik `[Cancel Report]`
10. Verifikasi toast `Success, report has been canceled.` tampil
11. Verifikasi dialog menutup

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 dan 5.
- Aksi `Cancel Report TAG` dijalankan dari modul Audit (Task Detail), bukan dari halaman TAG; hook `beforeEach` suite membuka Fixed Asset > TAG dan langkah pembuka tiap blok berpindah ke modul Audit.
- TC-FA-TAG-188 mengubah state laporan sehingga dijalankan terakhir; Expected tiap TC tetap diasersi.
- Laporan terbuka Damaged dibuat lewat fixture backend sebagai pelaku kedua (sesi API) pada langkah penghubung 1.
- TC-FA-TAG-180 sampai 186 ada di spec `TC-FA-TAG-E2E-040-role-matrix-report-tag-dan-cancel-report-dari-modul-audit`.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Kode Tag `RF-00130` dipakai TC untuk aset AST-0220 (TC-144 sampai TC-162) dan untuk aset AST-0020 (TC-174 sampai TC-188); kedua dataset tidak dapat ada bersamaan di registri Global. Spec menulis literal sesuai TC dan fixture backend menyiapkan dataset tiap spec.
  - TC-187 dan TC-188 tidak menyebut tab pada Task Detail; spec tidak menyebut tab.
