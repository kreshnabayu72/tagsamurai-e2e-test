---
id: TC-FA-TAG-E2E-022-role-matrix-negatif-menu-tag-dan-event-log-role-lain
title: "Role Matrix: Menu TAG dan Event Log Tidak Tersedia bagi Role Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-95
  - TC-FA-TAG-96
  - TC-FA-TAG-121
coverage:
  web: automated
---

# Role Matrix: Menu TAG dan Event Log Tidak Tersedia bagi Role Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Role lain (tanpa akses menu TAG) | NOMENU | `roleLainTanpaAksesMenuTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_NOMENU_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Akun role lain tanpa akses menu TAG; tidak ada data bisnis yang diubah.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): membaca respons jaringan yang dipicu halaman (status penolakan server) bila Expected menyebutnya.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

1. Verifikasi sedikitnya satu item menu lain pada sidebar Fixed Asset tampil
2. Verifikasi menu `TAG` tidak tampil di sidebar (Hidden)
3. Buka URL halaman Fixed Asset > TAG langsung di address bar
4. Verifikasi elemen lain pada halaman (sidebar atau header) tampil
5. Verifikasi halaman TAG tidak menampilkan data grup, kartu, maupun Table Tools
6. Verifikasi pengambilan data tab Paired dan To Be Returned ditolak server
7. Buka ulang URL halaman Fixed Asset > TAG langsung di address bar
8. Verifikasi tombol `Event Log` tidak tersedia karena halaman TAG tidak dapat diakses (Hidden)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah 1 dan 4 adalah anchor positif untuk asersi absence (bagian 8b butir 2); tidak ada di Expected TC dan dicatat sebagai asersi tambahan (S-03).
- TC-FA-TAG-96 dan TC-FA-TAG-121 sama-sama membuka URL langsung; langkah 7 mengulang pembukaan URL untuk TC-FA-TAG-121.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - TC-96 butir b ("Pengambilan data ... ditolak server") menyebut penolakan server tanpa status atau kode respons; spec mengasersi penolakan tanpa kode tertentu.
