---
id: TC-FA-TAG-E2E-015-guided-tooltip-replay-dan-flag-seen-true
title: "Guided Tooltip fa-tag: Tombol Replay Show Guide dan Walkthrough Tidak Muncul Otomatis Bila Flag Seen Sudah True"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-71
  - TC-FA-TAG-72
coverage:
  web: automated
---

# Guided Tooltip fa-tag: Tombol Replay Show Guide dan Walkthrough Tidak Muncul Otomatis Bila Flag Seen Sudah True

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-tag` sendiri sehingga mengecualikan pernyataan hook suite. Hook `before` spec ini menyetel flag itu true untuk akun Total Control (kondisi TC-FA-TAG-71 dan TC-FA-TAG-72) dan hook `after` memulihkannya ke nilai awal akun yang dicatat di hook `before`.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak didefinisikan di TC maupun PRD yang dibaca, S-13): menyetel flag `guided_tooltip_seen_fa-tag` untuk akun Total Control dan membaca nilainya (langkah 5).
- Data Pre-setup (dipakai sebagai latar; hanya dibaca, tidak diubah): dataset tab Paired (Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A).
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena data Pre-setup yang sama dipakai spec lain (suite.md).
- State global yang diubah: flag Guided Tooltip akun Total Control (dipulihkan di hook `after`); suite berjalan serial.

## Test Steps

### TC-FA-TAG-71: Tombol replay dengan tooltip Show guide memulai walkthrough dari langkah 1

1. Arahkan pointer ke tombol `[?]` di sebelah kanan Breadcrumb
2. Verifikasi tooltip `Show guide` tampil pada hover
3. Klik tombol `[?]`
4. Verifikasi walkthrough dimulai dari Step 1 of 4 dengan judul `Tabs`
5. Verifikasi flag `guided_tooltip_seen_fa-tag` tidak di-reset (tetap bernilai true)
6. Klik `[Skip]`

### TC-FA-TAG-72: Walkthrough tidak muncul otomatis bila flag seen sudah true

7. Buka menu Fixed Asset > TAG lewat sidebar
8. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired` tampil
9. Verifikasi tidak ada overlay maupun Tooltip box

## Notes

- Langkah 6 adalah langkah penghubung (menutup walkthrough hasil replay), tanpa asersi (S-03). Skip menetapkan flag true, yang sama dengan kondisi awal TC-FA-TAG-72.
- Langkah 9 adalah asersi absence atas overlay dan Tooltip box; anchor positif adalah Verifikasi Breadcrumb tampil pada halaman yang sama (langkah 8) (bagian 8b butir 2).
- TC-FA-TAG-62 sampai 70 dan 74 ada di spec 013 dan 014; TC-FA-TAG-73 dan 75 ada di spec 019.
- Temuan untuk QA:
  - TC-FA-TAG-71 Expected c ("Flag seen tidak di-reset") tidak punya langkah observasi di TC; spec membacanya lewat kemampuan baca flag yang mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut data yang sama dengan spec lain, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
