---
id: TC-FA-TAG-E2E-018-screening-halaman-tag-tab-paired-breadcrumb-dan-tooltip-toolbar-bagian-3
title: "Screening Halaman TAG: Badge Tab To Be Returned, Pindah Tab, Table Tools Tab To Be Returned, dan Placeholder Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-4
  - TC-FA-TAG-5
  - TC-FA-TAG-6
  - TC-FA-TAG-7
coverage:
  web: automated
---

# Screening Halaman TAG: Badge Tab To Be Returned, Pindah Tab, Table Tools Tab To Be Returned, dan Placeholder Search

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): tab To Be Returned memuat sedikitnya 3 Tag (`RF-00071`, `RF-00088`, `NF-00092`; himpunan minimum, jumlah total dibaca sebagai N dan tidak diasumsikan tepat 3); tab Paired memuat dataset grup Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A (dipakai sebagai latar, isinya tidak diasersi).
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada kode; jumlah total Tag To Be Returned dibaca sebagai N (suite.md).
- Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah Tag To Be Returned dalam scope (N) lewat kemampuan baca BE di hook `before`, bukan dari badge (bagian 8b butir 10; A-18); spec ini tidak mengubah data sehingga N tidak perlu dibaca ulang.
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.
- Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-4: Badge pada tab To Be Returned menampilkan jumlah Tag

1. Amati Tab `To Be Returned`
2. Verifikasi Badge pada Tab `To Be Returned` bernilai N (jumlah Tag To Be Returned dalam scope yang dibaca di hook `before`, sedikitnya 3) dengan `severity="secondary"`

### TC-FA-TAG-5: Pindah ke tab To Be Returned mengubah Breadcrumb dan menyembunyikan tombol khusus tab Paired

3. Klik Tab `To Be Returned`
4. Amati Breadcrumb dan Table Tools
5. Verifikasi Breadcrumb `Fixed Asset > TAG > To Be Returned`
6. Verifikasi segmen terakhir Breadcrumb bukan link
7. Verifikasi Table Tools tab To Be Returned memuat `Search`, `Filter`, `Download`, `Event Log`, `Receive TAG`
8. Verifikasi Table Tools tab To Be Returned tidak memuat `Changelog`, `Print QR`, maupun `Replace TAG`
9. Klik Tab `Paired`
10. Verifikasi Breadcrumb kembali `Fixed Asset > TAG > Paired`
11. Verifikasi Table Tools tab Paired kembali tampil

### TC-FA-TAG-6: Tab To Be Returned tidak memiliki tombol Changelog

12. Klik Tab `To Be Returned`
13. Amati Table Tools
14. Verifikasi Table Tools memuat `Search`, `Filter`, `Download`, `Event Log`, `Receive TAG`
15. Verifikasi tombol `Changelog` tidak ada di Table Tools tab To Be Returned
16. Klik Tab `Paired`

### TC-FA-TAG-7: Placeholder Search tab Paired

17. Klik ikon Search pada Table Tools
18. Verifikasi Input Search terbuka dengan placeholder `Search TAG code, asset ID, asset name...`
19. Klik `(←)` pada kotak Search

## Notes

- Langkah 16 dan 19 adalah langkah penghubung (kembali ke tab Paired; menutup input Search dan mereset tabel), tanpa asersi (S-03).
- Langkah 8 dan 15 adalah asersi absence atas elemen UI; anchor positif berupa Verifikasi daftar tombol yang tampil di Table Tools tab yang sama (langkah 7 dan 14) (bagian 8b butir 2).
- TC-FA-TAG-1 sampai 3 ada di spec 001 dan TC-FA-TAG-8 sampai 13 ada di spec 002.
- Langkah 2 mengasersi Badge terhadap N yang dibaca di hook `before` (relatif, bukan literal `3`; keputusan user 2026-11-04, bagian 8b butir 10).
- A-15: nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`) dipakai tanpa suffix `{runId}` karena TC menuntut asersi kode; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-4 Expected hanya menyebut nilai N (jumlah Tag To Be Returned dalam scope, sedikitnya 3) dan `severity="secondary"`; tidak ada cara pengamatan severity di UI selain gaya visual Badge, sehingga pengamatannya diserahkan ke tahap script.
