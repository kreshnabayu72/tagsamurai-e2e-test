---
id: TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter
title: "Purchase History TAG: Search dan Filter per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-766
  - TC-AC-ACC-767
  - TC-AC-ACC-768
  - TC-AC-ACC-769
  - TC-AC-ACC-770
coverage:
  web: automated
---

# Purchase History TAG: Search dan Filter per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi". Seed Purchase History TAG (F6): TAG P-T1 (Type RFID / Qty 100 / CV Mitra Sejati / Andi Wijaya / 10 Feb 2026 09:00), P-T2 (NFC / 50 / PT Distribusi Nusantara / Budi Santoso / 12 Apr 2026 10:00), P-T3 (RFID / 25 / CV Mitra Sejati / Citra Dewi / 30 Jun 2026 13:00). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-766: Search Purchase History TAG kolom teks: Type, Source, Action by

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `TAG`
4. Ubah ukuran halaman Purchase History TAG menjadi 100 baris
5. Klik ikon Search pada toolbar Purchase History TAG, ketik `nfc` lalu tekan Enter
6. Verifikasi Type "nfc": P-T2 (Qty 50) tampil
7. Verifikasi Type "nfc": P-T1 (Qty 100) tidak tampil
8. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `distribusi` dan tekan Enter
9. Verifikasi Source "distribusi": P-T2 (Qty 50) tampil
10. Verifikasi Source "distribusi": P-T1 (Qty 100) tidak tampil
11. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `citra` dan tekan Enter
12. Verifikasi Action by "citra": P-T3 (Qty 25) tampil
13. Verifikasi Action by "citra": P-T1 (Qty 100) tidak tampil

### TC-AC-ACC-767: Search Purchase History TAG kolom numerik: Qty

14. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `100` dan tekan Enter
15. Verifikasi Qty "100": P-T1 (Qty 100) tampil
16. Verifikasi Qty "100": P-T2 (Qty 50) dan P-T3 (Qty 25) tidak tampil
17. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-768: Filter Purchase History TAG kolom dropdown: Type, Source

18. Klik Filter, pilih Type "NFC", lalu klik `[Apply]`
19. Verifikasi Type = NFC: P-T2 (Qty 50) tampil
20. Verifikasi Type = NFC: P-T1 (Qty 100) dan P-T3 (Qty 25) tidak tampil
21. Klik Filter, klik `[Clear Field]`, pilih Source "PT Distribusi Nusantara", lalu klik `[Apply]`
22. Verifikasi Source = PT Distribusi Nusantara: P-T2 (Qty 50) tampil
23. Verifikasi Source = PT Distribusi Nusantara: P-T1 (Qty 100) tidak tampil

### TC-AC-ACC-769: Filter Purchase History TAG kolom range: Qty

24. Klik Filter, klik `[Clear Field]`, isi Qty Min 25 dan Max 50, lalu klik `[Apply]`
25. Verifikasi Qty 25 sampai 50: P-T2 (Qty 50) dan P-T3 (Qty 25) tampil (batas inklusif)
26. Verifikasi Qty 25 sampai 50: P-T1 (Qty 100) tidak tampil

### TC-AC-ACC-770: Filter Purchase History TAG kolom Date

27. Klik Filter, klik `[Clear Field]`, pilih rentang Date 01 Mar 2026 sampai 30 Jun 2026, lalu klik `[Apply]`
28. Verifikasi Date 01 Mar 2026 sampai 30 Jun 2026: P-T2 (Qty 50) dan P-T3 (Qty 25) tampil (batas akhir inklusif)
29. Verifikasi Date 01 Mar 2026 sampai 30 Jun 2026: P-T1 (Qty 100) tidak tampil
30. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pencarian dan penyaringan satu tabel pada satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah mengosongkan Search (✕, Enter) dan `[Clear Field]` lalu `[Apply]` di antara kasus serta di akhir adalah langkah penghubung (S-09, D-003). TC-768 mengawali filter pertama pada tabel yang sudah dikosongkan Search.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Batas inklusif Date 30 Jun 2026 diasersi terhadap baris P-T3 (30 Jun 2026 13:00).
