---
id: TC-AC-ACC-E2E-202-purchase-history-license-sort-subscription-action-by-tanggal-teks
title: "Purchase History License Client Custom Plan: Sort Kolom Subscription, Action by, Activation Date, Expired Date, dan Kolom Teks"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-939
  - TC-AC-ACC-833
  - TC-AC-ACC-834
  - TC-AC-ACC-835
coverage:
  web: automated
---

# Purchase History License Client Custom Plan: Sort Kolom Subscription, Action by, Activation Date, Expired Date, dan Kolom Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-1 "PT Uji Tabel Detail", Purchase History License: Qty 500 (Professional / Fixed Asset / New / CV Mitra Sejati / Andi Wijaya / Date 01 Jan 2026 08:00 / Activation 01 Jan 2026 / Expired 31 Dec 2026 / Subscription `SUBS-20260101-Q2W3E`); Qty 150 (Professional / Fixed Asset / Additional / CV Mitra Sejati / Andi Wijayanto / 20 Jun 2026 14:00 / 20 Jun 2026 / 31 Dec 2026 / `SUBS-20260101-Q2W3E`); Qty 25 (Growth / Concurrent User / New / PT Distribusi Nusantara / Budi Santoso / 10 Mar 2026 09:30 / 10 Mar 2026 / 09 Apr 2026 / `SUBS-20260310-C7D8E`); Qty 20 (Custom / Addon: Tracking / Additional / PT Distribusi Nusantara / Citra Dewi / 15 May 2026 11:00 / 15 May 2026 / 14 Nov 2026 / `SUBS-20260515-F1G2H`). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-939: Sort kolom Subscription: urutan A-Z berdasarkan Subscription ID dan siklus 3 state

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi urutan awal (default Date terbaru): Qty 150, Qty 20, Qty 25, Qty 500
5. Klik header Subscription
6. Verifikasi urutan ascending: Qty 500 dan Qty 150 (`SUBS-20260101-Q2W3E`) pada posisi 1 dan 2, lalu Qty 25 (`SUBS-20260310-C7D8E`), lalu Qty 20 (`SUBS-20260515-F1G2H`)
7. Klik header Subscription lagi
8. Verifikasi urutan descending: Qty 20 (`SUBS-20260515-F1G2H`), Qty 25 (`SUBS-20260310-C7D8E`), lalu Qty 500 dan Qty 150 (`SUBS-20260101-Q2W3E`) pada posisi 3 dan 4
9. Klik header Subscription ketiga kali
10. Verifikasi indikator sort Subscription nonaktif dan urutan kembali ke default Date terbaru: Qty 150, Qty 20, Qty 25, Qty 500

### TC-AC-ACC-833: Sort kolom Action by mengurutkan berdasarkan nama lengkap

11. Klik header Action by
12. Verifikasi urutan ascending: Qty 500 ("Andi W"), Qty 150 ("Andi W"), Qty 25 ("Budi S"), Qty 20 ("Citra D")
13. Klik header Action by lagi
14. Verifikasi urutan descending: Qty 20, Qty 25, Qty 150, Qty 500
15. Klik header Action by ketiga kali
16. Verifikasi urutan kembali ke default Date terbaru: Qty 150, Qty 20, Qty 25, Qty 500

### TC-AC-ACC-834: Sort kolom Activation Date dan Expired Date

17. Klik header Activation Date
18. Verifikasi Activation Date klik 1 (Oldest First): Qty 500, Qty 25, Qty 20, Qty 150
19. Klik header Activation Date lagi
20. Verifikasi Activation Date klik 2 (Newest First): Qty 150, Qty 20, Qty 25, Qty 500
21. Klik header Activation Date ketiga kali
22. Verifikasi Activation Date klik 3 kembali ke urutan default Date terbaru: Qty 150, Qty 20, Qty 25, Qty 500
23. Klik header Expired Date
24. Verifikasi Expired Date klik 1 (Oldest First): Qty 25, Qty 20, lalu Qty 500 dan Qty 150 pada posisi 3 dan 4
25. Klik header Expired Date lagi
26. Verifikasi Expired Date klik 2 (Newest First): Qty 500 dan Qty 150 pada posisi 1 dan 2, lalu Qty 20, lalu Qty 25

### TC-AC-ACC-835: Sort kolom Plan, Item, Purchase Type, dan Source secara alfabetis

27. Klik header Plan
28. Verifikasi Plan klik 1: Qty 20 (Custom), Qty 25 (Growth), lalu Qty 500 dan Qty 150 (Professional) pada posisi 3 dan 4
29. Klik header Item
30. Verifikasi Item klik 1: Qty 20 (Addon: Tracking), Qty 25 (Concurrent User), lalu Qty 500 dan Qty 150 (Fixed Asset) pada posisi 3 dan 4
31. Klik header Purchase Type
32. Verifikasi Purchase Type klik 1: Qty 150 dan Qty 20 (Additional) pada posisi 1 dan 2, lalu Qty 500 dan Qty 25 (New) pada posisi 3 dan 4
33. Klik header Source
34. Verifikasi Source klik 1: Qty 500 dan Qty 150 (CV Mitra Sejati) pada posisi 1 dan 2, lalu Qty 25 dan Qty 20 (PT Distribusi Nusantara) pada posisi 3 dan 4

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pengurutan satu tabel pada satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Baris bernilai sama pada satu kolom (mis. Qty 500 dan Qty 150 pada Plan Professional) diasersi pada posisi bersama tanpa urutan relatif sesuai Expected TC. Klik header kolom berbeda pada TC-835 memulai sort baru pada kolom itu.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Urutan akhir spec membiarkan sort kolom Source aktif; navigasi berikutnya (spec lain) membuka halaman baru sehingga state sort tidak dipertahankan.
