---
id: TC-FA-TAG-E2E-392-modal-changelog-daftar-aset-menampilkan-entri-replace-tag
title: "Modal Changelog Daftar Aset: Entri Changelog TAG Replace Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1501
coverage:
  web: automated
---

# Modal Changelog Daftar Aset: Entri Changelog TAG Replace Tampil

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite, lalu langkah 1 berpindah ke Fixed Asset > Assets > All Assets.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog TAG E3 di bawah; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Entri | Date | Action | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| E3 | 26/10/26 09:20 | Replace | Excavator 20 Ton - 20 | TAG | [RFID] RF-00130 | [RFID] RF-00415 | Budi S. |

  Kunci fixture: `changelogE3`. Aset yang dicari: 'Excavator 20 Ton - 20' (AST-0020).
- State yang diubah: tidak ada; hanya membaca Modal Changelog daftar aset.
- Nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-1501: Entri Changelog TAG juga tampil di Modal Changelog daftar aset

1. Buka Fixed Asset > Assets > All Assets
2. Klik ikon `Changelog` pada toolbar All Assets
3. Cari 'Excavator 20 Ton - 20'
4. Verifikasi entri E3 untuk Excavator 20 Ton - 20 tampil dengan Action `Replace` dan Field `TAG`

## Notes

- Pembagian TC lintas spec: entri E3 yang sama dipakai TC-FA-TAG-976 di spec 234 (Changelog Asset Detail).
- Temuan untuk QA:
  - Expected butir b TC-FA-TAG-1501 (entri yang sama tampil di tab Changelog Asset Detail dan Changelog halaman Tag) tidak punya langkah di TC dan tidak diasersi di spec ini; tampilannya di Changelog Asset Detail diuji TC-FA-TAG-976 di spec 234.
