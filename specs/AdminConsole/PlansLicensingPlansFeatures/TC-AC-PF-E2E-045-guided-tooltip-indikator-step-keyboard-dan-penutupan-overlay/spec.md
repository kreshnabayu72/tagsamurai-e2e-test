---
id: TC-AC-PF-E2E-045-guided-tooltip-indikator-step-keyboard-dan-penutupan-overlay
title: Guided Tooltip - Indikator Step, Keyboard, Penutupan Lewat Overlay dan Esc
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-645
coverage:
  web: automated
---

# Guided Tooltip - Indikator Step, Keyboard, Penutupan Lewat Overlay dan Esc

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`). TC membutuhkan akun baru tanpa flag; spec memakai akun #1 dengan flag dihapus (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip: spec ini adalah pengecualian atas pernyataan di `suite.md`. Sesudah hook suite menyetel flag `guided_tooltip_seen_ac-plans-features` true, hook `before` spec ini menghapus flag itu untuk akun #1 sehingga tur tampil; hook `after` memulihkan nilai awal flag.
- Data Pre-setup: Dataset Plan A (kolom Clients tampil dengan konfigurasi kolom default sehingga tur berisi empat step; preferensi kolom browser dihapus di hook `before`).
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk menghapus dan membaca flag Guided Tooltip akun aktor. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: flag Guided Tooltip akun #1; suite berjalan serial (`parallel: false`); dipulihkan di hook `after`.

## Test Steps

### TC-AC-PF-645

1. Pindah ke halaman lain di Admin Console lewat sidebar (tur yang mulai di hook `beforeEach` tertutup tanpa menandai flag).
2. Klik menu Plans & Licensing > Plans & Features di sidebar sehingga tur mulai.
3. Verifikasi Step 1 menampilkan indikator `Step 1 of 4`.
4. Tekan Enter.
5. Verifikasi tur pindah ke Step 2 dengan indikator `Step 2 of 4`.
6. Tekan panah kiri.
7. Verifikasi tur kembali ke Step 1.
8. Tekan panah kanan.
9. Verifikasi tur pindah ke Step 2.
10. Klik area overlay gelap di luar tooltip.
11. Verifikasi tur tertutup.
12. Verifikasi flag `guided_tooltip_seen_ac-plans-features` bernilai true (dibaca lewat fixture BE).
13. Muat ulang halaman.
14. Verifikasi Breadcrumb halaman Plans & Features tampil.
15. Verifikasi tur tidak muncul.
16. Klik tombol `[?]` di sebelah kanan breadcrumb.
17. Tekan Esc.
18. Verifikasi tur tertutup (setara Skip).
19. Muat ulang halaman.
20. Verifikasi Breadcrumb halaman Plans & Features tampil.
21. Verifikasi tur tidak otomatis muncul.

## Notes

- Langkah penghubung (S-03): langkah 1, yang memenuhi precondition TC "User berada di halaman lain di Admin Console".
- Langkah 14 dan 20 adalah anchor positif untuk langkah 15 dan 21 (absence sesudah F5).
- Pembagian TC lintas spec: TC-AC-PF-44 sampai TC-AC-PF-49 ada di spec 026 dan 027.
- Temuan untuk QA:
  - Precondition "akun baru tanpa flag" tidak menyebut identitas akun di Pre-setup #45; spec memakai akun #1 dengan flag dihapus lewat fixture BE (mekanismenya tidak tertulis di TC, PRD, atau LLD).
  - Post Condition flag true tanpa langkah observasi tidak diasersi di luar Expected b (S-01).
