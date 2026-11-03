---
id: TC-AC-ACC-E2E-306-selection-limit-mengikuti-system-limits-terbaru
title: "Selection Limit Client List Mengikuti System Limits Terbaru Tanpa Muat Ulang List (Volume Lebih dari 121 Baris)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-448
coverage:
  web: automated
---

# Selection Limit Client List Mengikuti System Limits Terbaru Tanpa Muat Ulang List (Volume Lebih dari 121 Baris)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-SEL-1 sampai C-SEL-130 `PT Seleksi Uji 001` sampai `PT Seleksi Uji 130` (Active, Direct, Group Regional Timur, tanpa subscription) sehingga sub-tab Active memuat lebih dari 121 baris (kelas e, >= 100 baris).
- State global: Selection Limit (System Limits, Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits) diubah ke 100 lalu 120 oleh Sesi B (Total Control, sesi API aktor yang sama dengan sesi UI Sesi A; dinyatakan di `suite.md`) dan dipulihkan ke nilai awal (default 1000) di hook `after`; suite berjalan serial.
- Kemampuan teknis: mengubah System Limits lewat sesi API (disediakan tim FE/BE; tanpa endpoint yang dikarang).

## Test Steps

### Selection Limit mengikuti System Limits terbaru (TC-AC-ACC-448)

1. [Sesi A] Klik sub-tab Active, lalu ubah jumlah baris per halaman menjadi 100
2. [Sesi B, sesi API] Ubah Selection Limit menjadi 100 hingga tersimpan
3. Tunggu aksi selesai
4. [Sesi A] Tanpa muat ulang, centang 100 baris pertama, pindah ke halaman 2, lalu arahkan kursor ke checkbox baris pertama halaman 2 (baris ke-101)
5. Verifikasi checkbox baris ke-101 disabled
6. Verifikasi tooltip checkbox baris ke-101 `You've reached the maximum selection of 100 rows.`
7. [Sesi B, sesi API] Ubah Selection Limit menjadi 120 hingga tersimpan
8. Tunggu aksi selesai
9. [Sesi A] Tanpa muat ulang, centang baris ke-101 sampai ke-120, lalu arahkan kursor ke checkbox baris ke-121
10. Verifikasi baris ke-101 sampai ke-120 dapat dicentang
11. Verifikasi counter `120 clients selected`
12. Verifikasi checkbox baris ke-121 disabled
13. Verifikasi tooltip checkbox baris ke-121 `You've reached the maximum selection of 120 rows.`
14. [Sesi A] Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi

## Notes

- Kelas e (volume data khusus) dan state global (Selection Limit); Sesi B lewat sesi API (P-2 keputusan 2026-10-30), jadi spec bukan kelas c. Label `Manual Only (d) dua sesi paralel` pada TC bukan alasan skip.
- Langkah penghubung (S-03): pembersihan seleksi lewat ikon `×`; Post Condition TC (`Kembalikan Selection Limit ke nilai awal (default 1000)`) dipenuhi hook `after`.
- Temuan untuk QA
  - TC-AC-ACC-448: Langkah TC menulis `Sesi B ... ubah Selection Limit` lewat halaman Plans & Licensing; spec memicu lewat sesi API karena sesi B hanya memicu state.
