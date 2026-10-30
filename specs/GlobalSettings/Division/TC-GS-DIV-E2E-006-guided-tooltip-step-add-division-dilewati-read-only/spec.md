---
id: TC-GS-DIV-E2E-006-guided-tooltip-step-add-division-dilewati-read-only
title: "Guided Tooltip Tab Division: Step Add Division Dilewati bagi Read Only"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-17
coverage:
  web: automated
---

# Guided Tooltip Tab Division: Step Add Division Dilewati bagi Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_RO_PASSWORD`). Login sekali di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `GS_RO_PASSWORD` dan `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Division (6 Division, data environment tetap; hanya dibaca). Spec tidak membuat atau mengubah data backend.
- Guided Tooltip: precondition TC adalah flag `guided_tooltip_seen_gs-division` belum ada untuk akun Read Only. Hook `before` mencatat nilai awal flag akun Read Only lalu menghapus flag; hook `after` memulihkan nilai awal. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- State global yang diubah: hanya flag Guided Tooltip akun Read Only (dipulihkan seperti di atas).

## Test Steps

### TC-GS-DIV-17: Step Add Division dilewati bagi aktor tanpa capability Create

1. Buka Global Settings > User > Tab Division untuk kunjungan pertama
2. Verifikasi Tombol `[+ Division]` Hidden
3. Verifikasi walkthrough dimulai dari step `Division Table` tanpa step `Add Division`
4. Klik `[Next]`
5. Verifikasi step kedua `Changelog Audit`
6. Klik `[Done]` pada step terakhir
7. Verifikasi walkthrough hanya memuat step `Division Table` dan `Changelog Audit` (tidak ada step lain sesudah `Changelog Audit`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Reset flag ke "belum ada" dilakukan di hook `before` (satu TC, satu akun), bukan di langkah.
- Langkah 1 membuka layar karena kunjungan pertama dengan flag belum ada adalah Langkah Uji TC-GS-DIV-17; hook `beforeEach` tidak membukanya.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6 (menutup walkthrough lewat `[Done]` pada step terakhir).
- Temuan untuk QA:
  - TC-GS-DIV-17 langkah 2 ("Klik `[Next]` pada tiap step sampai selesai") tidak menyebut bahwa tombol pada step terakhir berlabel `[Done]` (`foundation/functions/guided-tooltip.md`); spec mengklik `[Next]` pada step pertama dan `[Done]` pada step terakhir.
  - TC-GS-DIV-17 tidak memberi penanda untuk Expected a selain `[+ Division]` Hidden; spec memeriksa step pertama adalah `Division Table` (langkah 3).
