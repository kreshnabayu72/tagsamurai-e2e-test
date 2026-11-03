---
id: TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter
title: "Purchase History Hardware: Search dan Filter per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-771
  - TC-AC-ACC-772
  - TC-AC-ACC-773
  - TC-AC-ACC-774
  - TC-AC-ACC-775
coverage:
  web: automated
---

# Purchase History Hardware: Search dan Filter per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi". Seed Purchase History Hardware (F6): Hardware P-H1 (Handheld Reader / RFID / Qty 12 / CV Mitra Sejati / Andi Wijaya / 05 Feb 2026 09:00), P-H2 (Handheld Reader / NFC / Qty 3 / PT Distribusi Nusantara / Budi Santoso / 20 May 2026 14:00), P-H3 (Smart Fixed Reader / RFID / Qty 4 / CV Mitra Sejati / Citra Dewi / 18 Jul 2026 10:30). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-771: Search Purchase History Hardware kolom teks: Type, Source, Action by

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Hardware`
4. Ubah ukuran halaman Purchase History Hardware menjadi 100 baris
5. Klik ikon Search pada toolbar Purchase History Hardware, ketik `nfc` lalu tekan Enter
6. Verifikasi Type "nfc": P-H2 (Qty 3) tampil
7. Verifikasi Type "nfc": P-H1 (Qty 12) dan P-H3 (Qty 4) tidak tampil
8. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `distribusi` dan tekan Enter
9. Verifikasi Source "distribusi": P-H2 (Qty 3) tampil
10. Verifikasi Source "distribusi": P-H1 (Qty 12) tidak tampil
11. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `citra` dan tekan Enter
12. Verifikasi Action by "citra": P-H3 (Qty 4) tampil
13. Verifikasi Action by "citra": P-H1 (Qty 12) tidak tampil

### TC-AC-ACC-772: Search Purchase History Hardware kolom numerik: Qty

14. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `12` dan tekan Enter
15. Verifikasi Qty "12": P-H1 (Qty 12) tampil
16. Verifikasi Qty "12": P-H2 (Qty 3) dan P-H3 (Qty 4) tidak tampil
17. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-773: Filter Purchase History Hardware kolom dropdown: Type, Source

18. Klik Filter, pilih Type "NFC", lalu klik `[Apply]`
19. Verifikasi Type = NFC: P-H2 (Qty 3) tampil
20. Verifikasi Type = NFC: P-H1 (Qty 12) dan P-H3 (Qty 4) tidak tampil
21. Klik Filter, klik `[Clear Field]`, pilih Source "PT Distribusi Nusantara", lalu klik `[Apply]`
22. Verifikasi Source = PT Distribusi Nusantara: P-H2 (Qty 3) tampil
23. Verifikasi Source = PT Distribusi Nusantara: P-H1 (Qty 12) dan P-H3 (Qty 4) tidak tampil

### TC-AC-ACC-774: Filter Purchase History Hardware kolom range: Qty

24. Klik Filter, klik `[Clear Field]`, isi Qty Min 4 dan Max 12, lalu klik `[Apply]`
25. Verifikasi Qty 4 sampai 12: P-H1 (Qty 12) dan P-H3 (Qty 4) tampil (batas inklusif)
26. Verifikasi Qty 4 sampai 12: P-H2 (Qty 3) tidak tampil

### TC-AC-ACC-775: Filter Purchase History Hardware kolom Date

27. Klik Filter, klik `[Clear Field]`, pilih rentang Date 01 Feb 2026 sampai 20 May 2026 pada Section Purchase History Hardware, lalu klik `[Apply]`
28. Verifikasi Date 01 Feb 2026 sampai 20 May 2026: P-H1 (Qty 12) dan P-H2 (Qty 3) tampil (batas akhir inklusif)
29. Verifikasi Date 01 Feb 2026 sampai 20 May 2026: P-H3 (Qty 4) tidak tampil
30. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pencarian dan penyaringan satu tabel pada satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Pengosongan Search dan `[Clear Field]` lalu `[Apply]` di antara kasus dan di akhir adalah langkah penghubung (S-09, D-003).
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Batas inklusif Date 20 May 2026 diasersi terhadap P-H2 (20 May 2026 14:00).
