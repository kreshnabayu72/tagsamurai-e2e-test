---
id: TC-FA-TAG-E2E-026-role-matrix-negatif-aksi-tulis-read-only-bagian-2
title: "Role Matrix Negatif: Pemicu Report TAG Tidak Ada bagi Read Only"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-123
coverage:
  web: automated
---

# Role Matrix Negatif: Pemicu Report TAG Tidak Ada bagi Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan AST-0011 (Excavator 20 Ton - 11), AST-0020 (Excavator 20 Ton - 20), AST-0021 (Excavator 20 Ton - 21), AST-0043 (Excavator 20 Ton - 43), AST-0044 (Excavator 20 Ton - 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

1. Verifikasi Table Tools tab Paired tampil dengan `Search`, `Filter`, `Download`, dan `Changelog`
2. Klik kebab baris Excavator 20 Ton / Plant B (Non-standard 5)
3. Tutup menu kebab (Esc)
4. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
5. Klik kebab baris aset dengan laporan terbuka AST-0020
6. Tutup menu kebab (Esc)
7. Tutup Popup Detail
8. Klik Tab `To Be Returned`
9. Klik kebab baris RF-00071
10. Verifikasi tidak ada pemicu `Report TAG` pada Table Tools, kebab grup, row action Popup Detail, dan row action tab To Be Returned

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 3, 6, 7.
- Langkah 1 adalah anchor positif untuk asersi Hidden (bagian 8b butir 2); tidak ada di Expected TC dan dicatat sebagai asersi tambahan (S-03).
- Pembagian TC lintas spec: TC-FA-TAG-103 sampai 108 ada di spec `TC-FA-TAG-E2E-025-role-matrix-negatif-aksi-tulis-read-only-bagian-1`.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - TC-123 ("Periksa seluruh Table Tools dan row action") tidak menyebut elemen yang diperiksa satu per satu; spec memeriksa Table Tools tab Paired, kebab grup, row action Popup Detail Plant B, dan row action tab To Be Returned.
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
