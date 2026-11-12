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
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; hook `beforeEach` suite tidak membuka halaman Fixed Asset > TAG untuk spec ini (akun NOMENU tidak punya akses menu TAG; spec dikecualikan di `suite.md` bagian Hook): sidebar pada langkah 1 dan 2 diamati pada halaman awal setelah login di hook `before`, dan halaman TAG dibuka langsung lewat URL pada langkah 3 dan 7. Hook `after` mengembalikan sesi ke akun default suite.

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
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

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
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-96 butir b ("Pengambilan data ... ditolak server") menyebut penolakan server tanpa status atau kode respons; spec mengasersi penolakan tanpa kode tertentu.
