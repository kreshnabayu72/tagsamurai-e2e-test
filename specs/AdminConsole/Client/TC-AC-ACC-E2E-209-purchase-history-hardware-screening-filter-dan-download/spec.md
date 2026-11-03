---
id: TC-AC-ACC-E2E-209-purchase-history-hardware-screening-filter-dan-download
title: "Purchase History Hardware: Screening Filter dan Download CSV serta XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-296
  - TC-AC-ACC-785
coverage:
  web: automated
---

# Purchase History Hardware: Screening Filter dan Download CSV serta XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi". Seed Purchase History Hardware (F6): Hardware P-H1 (Handheld Reader / RFID / Qty 12 / CV Mitra Sejati / Andi Wijaya / 05 Feb 2026 09:00), P-H2 (Handheld Reader / NFC / Qty 3 / PT Distribusi Nusantara / Budi Santoso / 20 May 2026 14:00), P-H3 (Smart Fixed Reader / RFID / Qty 4 / CV Mitra Sejati / Citra Dewi / 18 Jul 2026 10:30). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: pembacaan berkas unduhan (nama berkas CSV dan XLSX) oleh browser; tidak memeriksa isi berkas.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-296: Screening Filter Purchase History Hardware: label, placeholder, dan urutan awal Date Newest First

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Hardware`
4. Lihat urutan awal baris Purchase History Hardware
5. Verifikasi urutan awal (Newest First): P-H3 (Qty 4), P-H2 (Qty 3), P-H1 (Qty 12)
6. Klik Filter pada toolbar Purchase History Hardware
7. Verifikasi Category: dropdown multi-select searchable, placeholder "All categories"
8. Verifikasi Type: dropdown multi-select searchable, placeholder "All types"
9. Verifikasi Qty: field range dengan placeholder "Min" dan "Max"
10. Verifikasi Source: dropdown multi-select searchable, placeholder "All sources"
11. Verifikasi Date: date range picker satu field, placeholder "Select date"
12. Verifikasi Action by: dropdown multi-select searchable, placeholder "All users"
13. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
14. Klik ulang icon Filter untuk menutup panel Filter

### TC-AC-ACC-785: Download Purchase History Hardware: toolbar Download dan nama file untuk CSV dan XLSX

15. Lihat toolbar Section Purchase History Hardware
16. Verifikasi toolbar Section Purchase History Hardware memuat Search, Filter, dan Download
17. Klik Download pada toolbar Purchase History Hardware
18. Verifikasi overlay memuat opsi "Download as CSV" dan "Download as XLSX"
19. Klik "Download as CSV"
20. Verifikasi tidak ada toast sukses
21. Verifikasi berkas `Purchase-Hardware-PT Sejahtera Abadi.csv` terunduh
22. Klik Download pada toolbar Purchase History Hardware lagi, lalu klik "Download as XLSX"
23. Verifikasi berkas `Purchase-Hardware-PT Sejahtera Abadi.xlsx` terunduh

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Klik ulang icon Filter untuk menutup panel (D-001) adalah langkah penghubung (S-03). Hanya nama berkas yang diasersi (bagian 3 prinsip 13 butir f).
- Temuan untuk QA (S-15): Post Condition kedua TC `-` sehingga tidak diasersi.
