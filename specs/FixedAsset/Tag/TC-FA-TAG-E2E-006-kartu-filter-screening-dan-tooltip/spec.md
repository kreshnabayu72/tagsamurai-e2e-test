---
id: TC-FA-TAG-E2E-006-kartu-filter-screening-dan-tooltip
title: "Screening Kartu Filter Tab Paired dan Tooltip Ikon Info Tiap Kartu"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-25
  - TC-FA-TAG-26
  - TC-FA-TAG-27
  - TC-FA-TAG-28
coverage:
  web: automated
---

# Screening Kartu Filter Tab Paired dan Tooltip Ikon Info Tiap Kartu

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

  Nilai kartu turunan: `Reported` 3, `Non-standard` 8, `Not Paired Yet` 4.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-25: Screening kartu filter tab Paired

1. Amati area kartu di atas tabel grup
2. Verifikasi tiga kartu Clickable tampil berurutan: `Reported`, `Non-standard`, `Not Paired Yet`
3. Verifikasi nilai `Reported` = 3, `Non-standard` = 8, `Not Paired Yet` = 4 (jumlah aset atas seluruh baris grup dalam scope)
4. Verifikasi setiap kartu memuat ikon info di samping judul
5. Verifikasi tidak ada kartu aktif
6. Verifikasi tabel menampilkan empat baris grup

### TC-FA-TAG-26: Tooltip ikon info kartu Reported

7. Arahkan pointer ke ikon info di samping judul kartu `Reported`
8. Verifikasi tooltip `Assets with a TAG that has an open report (damaged, missing, or unreadable).` tampil saat hover
9. Pindahkan fokus keyboard ke ikon info kartu `Reported`
10. Verifikasi tooltip yang sama tampil saat fokus keyboard

### TC-FA-TAG-27: Tooltip ikon info kartu Non-standard

11. Arahkan pointer ke ikon info di samping judul kartu `Non-standard`
12. Verifikasi tooltip `Assets with a TAG type that the asset name does not require. Replace these TAGs to bring the assets back to standard.` tampil saat hover
13. Pindahkan fokus keyboard ke ikon info kartu `Non-standard`
14. Verifikasi tooltip yang sama tampil saat fokus keyboard

### TC-FA-TAG-28: Tooltip ikon info kartu Not Paired Yet

15. Arahkan pointer ke ikon info di samping judul kartu `Not Paired Yet`
16. Verifikasi tooltip `Assets that should carry TAGs but have none paired yet. Use Pair TAG to attach them.` tampil saat hover
17. Pindahkan fokus keyboard ke ikon info kartu `Not Paired Yet`
18. Verifikasi tooltip yang sama tampil saat fokus keyboard

## Notes

- Langkah 1 adalah langkah penghubung (mengamati area kartu), tanpa asersi (S-03).
- Langkah 5 adalah asersi absence atas state kartu; anchor positif adalah Verifikasi tiga kartu tampil (langkah 2) (bagian 8b butir 2).
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut asersi nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-25 Expected b menyebut nilai kartu sebagai "jumlah aset atas seluruh baris grup dalam scope"; nilai 3, 8, dan 4 adalah jumlah dari kolom Reported, Non-standard, dan Not Paired Yet empat baris Pre-setup. Spec mengasersi nilai itu apa adanya.
