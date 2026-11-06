---
id: TC-FA-TAG-E2E-234-modal-changelog-screening-penutupan-tooltip-dan-read-only-bagian-2
title: "Modal Changelog Paired TAG: Entri Replace Tampil di Changelog Asset Detail (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-976
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Entri Replace Tampil di Changelog Asset Detail (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite, lalu langkah 1 berpindah ke Asset > Asset List.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog Paired TAG E3 dan E4 di bawah; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Entri | Date | Action | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| E3 | 26/10/26 09:20 | Replace | Excavator 20 Ton - 20 | TAG | [RFID] RF-00130 | [RFID] RF-00415 | Budi S. |
| E4 | 26/10/26 09:14 | Replace | Excavator 20 Ton - 42 | TAG | [QR] QR-00230 | [RFID] RF-00412 | Budi S. |

  Kunci fixture: `changelogE3`, `changelogE4`. Aset yang dibuka: 'Excavator 20 Ton - 20' (AST-0020).
- State yang diubah: tidak ada; hanya membaca Changelog Asset Detail.
- Nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Buka Asset > Asset List dari sidebar
2. Ketik Search `Excavator 20 Ton - 20`, tekan Enter
3. Klik baris aset 'Excavator 20 Ton - 20' untuk membuka Asset Detail
4. Klik tombol `Changelog` di Asset Detail
5. Verifikasi entri E3 tampil
6. Verifikasi entri E4 tidak tampil
7. Klik ikon close untuk menutup modal Changelog Asset Detail

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 3 (menuju Asset Detail, karena Precondition b TC-FA-TAG-976 berada di Asset Detail sedangkan hook `beforeEach` suite membuka halaman TAG), Search pada langkah 2 untuk menemukan baris target, dan langkah 7 (menutup modal).
- Pembagian TC lintas spec: TC-FA-TAG-931 sampai TC-FA-TAG-938, TC-FA-TAG-968, dan TC-FA-TAG-975 ada di spec 233.
- A-15: nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-976 Precondition b tidak menyebut cara membuka Asset Detail dari daftar aset; spec memakai Asset > Asset List, Search nama aset, lalu klik baris.
  - Judul TC-FA-TAG-976 menyebut Changelog Asset Detail "hanya memuat entri aset itu", tetapi Expected hanya membahas E3 dan E4. Entri E6 (Report TAG, aset 'Excavator 20 Ton - 20') tidak dibahas; spec tidak mengasersinya.
  - Search `Excavator 20 Ton - 20` pada Asset List dapat mencocokkan lebih dari satu aset (misalnya aset dengan nomor yang diawali 20); spec memilih baris dengan nama persis.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
