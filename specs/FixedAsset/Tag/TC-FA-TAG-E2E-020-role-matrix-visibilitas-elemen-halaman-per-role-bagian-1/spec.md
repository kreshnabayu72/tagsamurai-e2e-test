---
id: TC-FA-TAG-E2E-020-role-matrix-visibilitas-elemen-halaman-per-role-bagian-1
title: "Role Matrix: Visibilitas Elemen Halaman TAG per Role (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-91
  - TC-FA-TAG-92
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Halaman TAG per Role (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Total Control (TC-FA-TAG-91)

1. Verifikasi menu `TAG` tampil di sidebar Fixed Asset (Show)
2. Klik menu `TAG`
3. Verifikasi tab `Paired` dan `To Be Returned` keduanya tampil
4. Klik kebab grup Excavator 20 Ton pada baris Plant B
5. Verifikasi aksi `Detail` tampil pada kebab grup
6. Tutup menu kebab (Esc)
7. Verifikasi tombol `Changelog` dan ikon Download tampil
8. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
9. Verifikasi TAG Code pada baris aset berupa link yang dapat diklik (membuka Popup TAG Log)
10. Tutup Popup Detail

### Read Only (TC-FA-TAG-92)

11. Ganti akun: logout dari akun Total Control [TC], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
12. Verifikasi menu `TAG` tampil di sidebar Fixed Asset (Show)
13. Klik menu `TAG`
14. Verifikasi tab `Paired` dan `To Be Returned` keduanya tampil
15. Klik kebab grup Excavator 20 Ton pada baris Plant B
16. Verifikasi aksi `Detail` tampil pada kebab grup
17. Tutup menu kebab (Esc)
18. Verifikasi tombol `Changelog` dan ikon Download tampil
19. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
20. Verifikasi TAG Code pada baris aset berupa link yang dapat diklik (membuka Popup TAG Log)
21. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 6, 10, 11, 17, 21.
- Matriks visibilitas satu daftar elemen untuk banyak role dengan hasil sama (Show); title tanpa kata Positif atau Negatif (bagian 3a).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - TC menyebut "kebab grup Excavator 20 Ton" tanpa menyebut baris group mana; spec memakai baris Plant B (Non-standard 5), sama dengan TC-98.
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
