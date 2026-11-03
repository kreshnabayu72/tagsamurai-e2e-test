---
id: TC-AC-ACC-E2E-197-purchase-history-license-screening-download-dan-filter-panel
title: "Purchase History License: Screening Kolom, Panel Filter, dan Download Tab Subscription"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-280
  - TC-AC-ACC-282
  - TC-AC-ACC-283
coverage:
  web: automated
---

# Purchase History License: Screening Kolom, Panel Filter, dan Download Tab Subscription

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
- Kemampuan teknis: pembacaan berkas unduhan (nama berkas CSV dan XLSX) oleh browser; tidak memeriksa isi berkas (kelas f tidak diuji di spec ini).

## Test Steps

### TC-AC-ACC-280: Purchase History License: kolom, nilai Subscription ID, sort default Date terbaru, dan format sel

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Ubah ukuran halaman Purchase History License menjadi 100 baris
5. Lihat tabel Purchase History License
6. Verifikasi kolom berurutan Subscription | Plan | Item | Purchase Type | Duration | Activation Date | Expired Date | Qty | Source | Action by | Date | ⋯
7. Verifikasi kolom Subscription menampilkan Subscription ID berformat `SUBS-YYYYMMDD-XXXXX`: baris P-L1 (Qty 500) dan P-L2 (Qty 150) `SUBS-20260101-A1B2C`, baris P-L3 (Qty 50) `SUBS-20260315-K9L0M`, baris P-L4 (Qty 100) `SUBS-20250102-X7Y8Z`
8. Verifikasi urutan awal sort Date terbaru, urutan relatif P-L2 (Qty 150), P-L3 (Qty 50), P-L1 (Qty 500), P-L4 (Qty 100)
9. Verifikasi Duration berformat `[n] months`: P-L1 "12 months", P-L3 "6 months", P-L4 "24 months"
10. Verifikasi Purchase Type baris P-L1 "New" dan baris P-L2 "Additional"
11. Verifikasi tidak ada baris Purchase Type bernilai Renewal
12. Verifikasi Activation Date, Expired Date, dan Date menampilkan tanggal sesuai format General Settings
13. Arahkan kursor ke Action by pada baris P-L1 (Qty 500)
14. Verifikasi sel Action by baris P-L1 "Andi W" dengan tooltip nama lengkap "Andi Wijaya"

### TC-AC-ACC-282: Screening Filter Purchase History License: label, placeholder, dan tipe field

15. Klik Filter pada toolbar Purchase History License
16. Verifikasi Plan: dropdown multi-select searchable, placeholder "All plans"
17. Verifikasi Purchase Type: dropdown multi-select searchable, placeholder "All types"
18. Verifikasi Duration: field range dengan placeholder "Min" dan "Max"
19. Verifikasi Qty: field range dengan placeholder "Min" dan "Max"
20. Verifikasi Source: dropdown multi-select searchable, placeholder "All sources"
21. Verifikasi Date: date range picker satu field, placeholder "Select date"
22. Verifikasi Item: dropdown multi-select searchable, placeholder "All items"
23. Verifikasi Activation Date: date range picker satu field, placeholder "Select date"
24. Verifikasi Expired Date: date range picker satu field, placeholder "Select date"
25. Verifikasi Action by: dropdown multi-select searchable, placeholder "All users"
26. Verifikasi Subscription tidak memiliki field filter
27. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
28. Klik ulang icon Filter untuk menutup panel Filter

### TC-AC-ACC-283: Download ringkasan Subscription Details dan Purchase History: nama file

29. Klik Download Tab Subscription lalu pilih CSV
30. Klik Download Purchase History lalu pilih XLSX
31. Verifikasi tidak ada toast sukses
32. Verifikasi berkas `Client-Subscriptions-PT Sejahtera Abadi` terunduh
33. Verifikasi berkas `Purchase-Subscription-PT Sejahtera Abadi` terunduh

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Pemilihan format CSV dan XLSX pada TC-283 mengikuti redaksi TC; isi berkas tidak diasersi (hanya nama berkas, bagian 3 prinsip 13 butir f). Panel Filter ditutup dengan klik ulang icon Filter (D-001) sebagai langkah penghubung; ukuran halaman 100 baris dipertahankan untuk TC berikutnya di spec ini.
- Temuan untuk QA (S-15): TC-283 menulis nama berkas tanpa ekstensi sedangkan TC-785/786 menulis ekstensi `.csv` dan `.xlsx`; spec mengikuti TC masing-masing. TC-280 Expected butir g menyebut Langkah 4 (hover) sehingga hover diasersi setelah verifikasi tabel. Post Condition seluruh TC `-` sehingga tidak diasersi.
