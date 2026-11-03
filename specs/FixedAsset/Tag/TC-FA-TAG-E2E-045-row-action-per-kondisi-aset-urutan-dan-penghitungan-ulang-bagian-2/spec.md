---
id: TC-FA-TAG-E2E-045-row-action-per-kondisi-aset-urutan-dan-penghitungan-ulang-bagian-2
title: "Row Action Dihitung Ulang Setelah Laporan Ditutup dan Urutan Aksi Dark Sebelum Danger"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-197
  - TC-FA-TAG-198
coverage:
  web: automated
---

# Row Action Dihitung Ulang Setelah Laporan Ditutup dan Urutan Aksi Dark Sebelum Danger

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Aset acuan grup Excavator 20 Ton / Plant B: AST-0020 (Excavator 20 Ton - 20, laporan terbuka pada RF-00130) dan AST-0043 (Excavator 20 Ton - 43, Tag QR-00231 Non-standard dan laporan terbuka).
- Data precondition TC-FA-TAG-197 (dipakai sebagai precondition TC, tidak diasersi): laporan terbuka AST-0020 ditutup Declined (data persisted) lewat fixture BE di hook `before`.
- Kemampuan teknis (disediakan tim FE/BE): seed idempotent dan pemulihan aset, Tag, dan laporan Tag lewat fixture backend (lihat `suite.md`).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): buka kembali laporan AST-0020 pada RF-00130 dan kembalikan data Pre-setup tab Paired ke keadaan awal (Last Updated dan hitungan Reported grup Plant B berubah selama spec ini).
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B

### TC-FA-TAG-197: row action dihitung ulang setelah laporan ditutup

2. Klik kebab baris AST-0020
3. Verifikasi kebab hanya memuat `Replace TAG`
4. Verifikasi `Decline Report` tidak ada di kebab karena tidak ada laporan terbuka
5. Tutup kebab

### TC-FA-TAG-198: urutan row action

6. Klik kebab baris AST-0043
7. Verifikasi urutan aksi pada kebab: `Replace TAG` (dark), lalu `Decline Report` (danger)
8. Tutup kebab, lalu tutup Popup Detail

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5 dan 8 (menutup kebab dan Popup Detail). Langkah 1 membuka Popup Detail yang dipakai kedua TC.
- Langkah 4 absence didahului langkah 3 (aksi `Replace TAG` tampil pada kebab yang sama) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-197 precondition d menyebut laporan AST-0020 "sudah ditutup Declined (data persisted)" tanpa menyebut cara menutupnya; spec menuliskannya sebagai kemampuan fixture BE yang disediakan tim FE/BE.
  - TC-FA-TAG-197 dan TC-FA-TAG-191 memakai AST-0020 dengan keadaan laporan berlawanan (terbuka di TC-FA-TAG-191, ditutup di TC-FA-TAG-197); keduanya di spec berbeda (TC-FA-TAG-191 ada di spec 044) sehingga tiap spec menyiapkan keadaannya sendiri.
  - Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
