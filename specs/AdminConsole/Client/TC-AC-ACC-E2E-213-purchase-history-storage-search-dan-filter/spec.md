---
id: TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter
title: "Purchase History Storage: Search dan Filter per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-776
  - TC-AC-ACC-777
  - TC-AC-ACC-778
  - TC-AC-ACC-779
  - TC-AC-ACC-780
coverage:
  web: automated
---

# Purchase History Storage: Search dan Filter per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi". Seed Purchase History Storage (F6): Storage P-S1 (Qty 60 GB / CV Mitra Sejati / Andi Wijaya / 01 Jan 2026 08:00), P-S2 (25 GB / PT Distribusi Nusantara / Budi Santoso / 10 Apr 2026 13:00), P-S3 (15 GB / CV Mitra Sejati / Citra Dewi / 25 Sep 2026 09:00). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-776: Search Purchase History Storage kolom teks: Source, Action by

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Storage`
4. Ubah ukuran halaman Purchase History Storage menjadi 100 baris
5. Klik ikon Search pada toolbar Purchase History Storage, ketik `distribusi` lalu tekan Enter
6. Verifikasi Source "distribusi": P-S2 (Qty 25) tampil
7. Verifikasi Source "distribusi": P-S1 (Qty 60) dan P-S3 (Qty 15) tidak tampil
8. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `citra` dan tekan Enter
9. Verifikasi Action by "citra": P-S3 (Qty 15) tampil
10. Verifikasi Action by "citra": P-S1 (Qty 60) tidak tampil

### TC-AC-ACC-777: Search Purchase History Storage kolom numerik: Qty (GB)

11. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `60` dan tekan Enter
12. Verifikasi Qty "60": P-S1 (Qty 60) tampil
13. Verifikasi Qty "60": P-S2 (Qty 25) dan P-S3 (Qty 15) tidak tampil
14. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-778: Filter Purchase History Storage kolom dropdown: Source

15. Klik Filter, pilih Source "PT Distribusi Nusantara", lalu klik `[Apply]`
16. Verifikasi Source = PT Distribusi Nusantara: P-S2 (Qty 25) tampil
17. Verifikasi Source = PT Distribusi Nusantara: P-S1 (Qty 60) dan P-S3 (Qty 15) tidak tampil

### TC-AC-ACC-779: Filter Purchase History Storage kolom range: Qty

18. Klik Filter, klik `[Clear Field]`, isi Qty Min 15 dan Max 25, lalu klik `[Apply]`
19. Verifikasi Qty 15 sampai 25: P-S2 (Qty 25) dan P-S3 (Qty 15) tampil (batas inklusif)
20. Verifikasi Qty 15 sampai 25: P-S1 (Qty 60) tidak tampil

### TC-AC-ACC-780: Filter Purchase History Storage kolom Date

21. Klik Filter, klik `[Clear Field]`, pilih rentang Date 01 Jan 2026 sampai 10 Apr 2026, lalu klik `[Apply]`
22. Verifikasi Date 01 Jan 2026 sampai 10 Apr 2026: P-S1 (Qty 60) dan P-S2 (Qty 25) tampil (batas awal dan batas akhir inklusif)
23. Verifikasi Date 01 Jan 2026 sampai 10 Apr 2026: P-S3 (Qty 15) tidak tampil
24. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Pengosongan Search dan `[Clear Field]` lalu `[Apply]` di antara kasus dan di akhir adalah langkah penghubung (S-09, D-003).
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi.
