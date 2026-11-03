---
id: TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom
title: "Purchase History License: Filter Kolom Dropdown, Range, Date, Kombinasi AND, dan Item serta Action by"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-759
  - TC-AC-ACC-760
  - TC-AC-ACC-761
  - TC-AC-ACC-762
  - TC-AC-ACC-998
coverage:
  web: automated
---

# Purchase History License: Filter Kolom Dropdown, Range, Date, Kombinasi AND, dan Item serta Action by

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

### TC-AC-ACC-759: Filter Purchase History License kolom dropdown: Plan, Purchase Type, dan Source

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Ubah ukuran halaman Purchase History License menjadi 100 baris
5. Klik Filter, pilih Plan "Growth", lalu klik `[Apply]`
6. Verifikasi Plan = Growth: P-L3 (Qty 50) dan P-L4 (Qty 100) tampil
7. Verifikasi Plan = Growth: P-L1 (Qty 500) dan P-L2 (Qty 150) tidak tampil
8. Klik Filter, klik `[Clear Field]`, pilih Purchase Type "Additional", lalu klik `[Apply]`
9. Verifikasi Purchase Type = Additional: P-L2 (Qty 150) tampil
10. Verifikasi Purchase Type = Additional: P-L1 (Qty 500), P-L3 (Qty 50), dan P-L4 (Qty 100) tidak tampil
11. Klik Filter, klik `[Clear Field]`, pilih Source "PT Distribusi Nusantara", lalu klik `[Apply]`
12. Verifikasi Source = PT Distribusi Nusantara: P-L3 (Qty 50) dan P-L4 (Qty 100) tampil
13. Verifikasi Source = PT Distribusi Nusantara: P-L1 (Qty 500) dan P-L2 (Qty 150) tidak tampil

### TC-AC-ACC-760: Filter Purchase History License kolom range: Duration dan Qty

14. Klik Filter, klik `[Clear Field]`, isi Duration Min 12 dan Max 24, lalu klik `[Apply]`
15. Verifikasi Duration 12 sampai 24: P-L1 (Qty 500), P-L2 (Qty 150) (keduanya Duration 12 months), dan P-L4 (Qty 100) (Duration 24 months) tampil
16. Verifikasi Duration 12 sampai 24: P-L3 (Qty 50) (Duration 6 months) tidak tampil
17. Klik Filter, klik `[Clear Field]`, isi Qty Min 100 dan Max 150, lalu klik `[Apply]`
18. Verifikasi Qty 100 sampai 150: P-L2 (Qty 150) dan P-L4 (Qty 100) tampil (batas inklusif)
19. Verifikasi Qty 100 sampai 150: P-L1 (Qty 500) dan P-L3 (Qty 50) tidak tampil

### TC-AC-ACC-761: Filter Purchase History License kolom Date

20. Klik Filter, klik `[Clear Field]`, pilih rentang Date 01 Jan 2026 sampai 15 Mar 2026, lalu klik `[Apply]`
21. Verifikasi Date 01 Jan 2026 sampai 15 Mar 2026: P-L1 (Qty 500) (01 Jan 2026) dan P-L3 (Qty 50) (15 Mar 2026) tampil (batas awal dan batas akhir inklusif)
22. Verifikasi Date 01 Jan 2026 sampai 15 Mar 2026: P-L2 (Qty 150) (20 Jun 2026) dan P-L4 (Qty 100) (02 Jan 2025) tidak tampil

### TC-AC-ACC-762: Filter Plan dan Purchase Type sekaligus menghasilkan irisan AND

23. Klik Filter, klik `[Clear Field]`, pilih Plan "Professional" dan Purchase Type "New", lalu klik `[Apply]`
24. Verifikasi Plan Professional dan Purchase Type New: P-L1 (Qty 500) tampil
25. Verifikasi Plan Professional dan Purchase Type New: P-L2 (Qty 150) (Additional), P-L3 (Qty 50) (Growth), dan P-L4 (Qty 100) (Growth) tidak tampil

### TC-AC-ACC-998: Filter Purchase History License berdasarkan Item dan Action by menyaring baris

26. Klik Filter, klik `[Clear Field]`, pilih Item "Addon: Maintenance", lalu klik `[Apply]`
27. Verifikasi Item = Addon: Maintenance: hanya P-L3 (Qty 50) tampil
28. Verifikasi Item = Addon: Maintenance: P-L1 (Qty 500), P-L2 (Qty 150), dan P-L4 (Qty 100) tidak tampil
29. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
30. Verifikasi seluruh baris seed P-L1 sampai P-L4 tampil kembali
31. Klik Filter, pilih Action by "Citra D", lalu klik `[Apply]`
32. Verifikasi Action by = Citra D: hanya P-L4 (Qty 100) tampil
33. Verifikasi Action by = Citra D: P-L1, P-L2, dan P-L3 tidak tampil
34. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa penyaringan pada satu tabel dan satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Pengosongan filter memakai `[Clear Field]` lalu `[Apply]` (D-003: `[Clear Field]` hanya mengosongkan draft) sehingga tiap blok mulai dari tabel penuh; langkah itu adalah langkah penghubung (S-09). Ukuran halaman 100 baris dipertahankan di seluruh spec.
- Temuan untuk QA (S-15): TC-998 meminta Filter Action by "Citra D" sedangkan Expected TC-281 memakai Search "citra"; pilihan opsi Action by mengikuti teks TC. Opsi filter Plan "Professional" dan Source mengikuti Tabel A3 F6. Post Condition seluruh TC `-`.
