---
id: TC-AC-ACC-E2E-200-purchase-history-license-sort-date-qty-duration
title: "Purchase History License: Sort Kolom Date, Qty, dan Duration"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-763
  - TC-AC-ACC-764
  - TC-AC-ACC-765
coverage:
  web: automated
---

# Purchase History License: Sort Kolom Date, Qty, dan Duration

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi". Seed Purchase History (Tabel A3, F6) C-01: License sub-tab FAMS P-L1 (Professional / Fixed Asset / New / 12 months / Qty 500 / CV Mitra Sejati / Andi Wijaya / 01 Jan 2026 08:00), P-L2 (Professional / Fixed Asset / Additional / 12 months / Qty 150 / CV Mitra Sejati / Andi Wijaya / 20 Jun 2026 14:00), P-L3 (Growth / Addon: Maintenance / New / 6 months / Qty 50 / PT Distribusi Nusantara / Budi Santoso / 15 Mar 2026 11:00), P-L4 (Growth / Fixed Asset / New / 24 months / Qty 100 / PT Distribusi Nusantara / Citra Dewi / 02 Jan 2025 09:00); Subscription ID P-L1 dan P-L2 `SUBS-20260101-A1B2C`, P-L3 `SUBS-20260315-K9L0M`, P-L4 `SUBS-20250102-X7Y8Z`. Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-763: Sort kolom Date: urutan awal Newest First dan siklus 3 state

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Ubah ukuran halaman Purchase History License menjadi 100 baris
5. Verifikasi urutan awal (Newest First): P-L2 (Qty 150), P-L3 (Qty 50), P-L1 (Qty 500), P-L4 (Qty 100)
6. Klik header kolom Date satu kali
7. Verifikasi urutan ascending (Oldest First): P-L4 (Qty 100), P-L1 (Qty 500), P-L3 (Qty 50), P-L2 (Qty 150)
8. Klik header kolom Date untuk kedua kali
9. Verifikasi urutan descending (Newest First): P-L2 (Qty 150), P-L3 (Qty 50), P-L1 (Qty 500), P-L4 (Qty 100)
10. Klik header kolom Date untuk ketiga kali
11. Verifikasi indikator sort Date nonaktif dan urutan kembali ke default Newest First

### TC-AC-ACC-764: Sort kolom Qty: urutan numerik, bukan urutan teks

12. Klik header kolom Qty satu kali
13. Verifikasi urutan ascending: P-L3 (Qty 50), P-L4 (Qty 100), P-L2 (Qty 150), P-L1 (Qty 500)
14. Klik header kolom Qty untuk kedua kali
15. Verifikasi urutan descending: P-L1 (Qty 500), P-L2 (Qty 150), P-L4 (Qty 100), P-L3 (Qty 50)
16. Klik header kolom Qty untuk ketiga kali
17. Verifikasi indikator sort Qty nonaktif dan urutan kembali ke default Date Newest First

### TC-AC-ACC-765: Sort kolom Duration: urutan berdasarkan nilai bulan, bukan teks

18. Klik header kolom Duration satu kali
19. Verifikasi urutan ascending: P-L3 (Qty 50) (6 months), lalu P-L1 (Qty 500) dan P-L2 (Qty 150) (12 months) pada posisi 2 dan 3, lalu P-L4 (Qty 100) (24 months)
20. Klik header kolom Duration untuk kedua kali
21. Verifikasi urutan descending: P-L4 (Qty 100) (24 months), lalu P-L1 (Qty 500) dan P-L2 (Qty 150) (12 months) pada posisi 2 dan 3, lalu P-L3 (Qty 50) (6 months)
22. Klik header kolom Duration untuk ketiga kali
23. Verifikasi indikator sort Duration nonaktif dan urutan kembali ke default Date Newest First

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- P-L1 dan P-L2 bernilai sama (12 months) pada sort Duration sehingga urutan antar keduanya tidak dinilai; keduanya diasersi pada posisi 2 dan 3 tanpa urutan relatif.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Sort Date memakai dua nilai Date yang berbeda per baris (dua nilai distinct, S-11).
