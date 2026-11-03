---
id: TC-AC-ACC-E2E-183-tab-subscription-license-quota-nilai-dan-sort
title: "Tab Subscription: License Quota per Sub-tab, Nilai Ledger, Tanpa Baris Storage, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-260
  - TC-AC-ACC-261
  - TC-AC-ACC-809
  - TC-AC-ACC-262
coverage:
  web: automated
---

# Tab Subscription: License Quota per Sub-tab, Nilai Ledger, Tanpa Baris Storage, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-01 "PT Sejahtera Abadi": License Quota FAMS (Total/Used/Available) Asset 650/320/330, Concurrent User 25/12/13, Addon: Maintenance 50/50/0; Storage Total 100 GB. Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-260: License Quota per sub-tab: FAMS/SAMS Asset, semua Concurrent User, SIEM Log Source, FAMS Addon

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi License Quota FAMS memuat baris Asset, Concurrent User, dan Addon: [nama] (satu baris per addon term)
5. Klik sub-tab `SAMS`
6. Verifikasi License Quota SAMS memuat baris Asset dan Concurrent User
7. Klik sub-tab `SIEM`
8. Verifikasi License Quota SIEM memuat baris Log Source dan Concurrent User
9. Verifikasi Total, Used, dan Available bernilai angka; kosong tampil "0"

### TC-AC-ACC-261: License Quota nilai ledger term live

10. Klik sub-tab `FAMS`
11. Verifikasi baris Asset menampilkan Total 650, Used 320, Available 330
12. Verifikasi baris Concurrent User menampilkan Total 25, Used 12, Available 13
13. Verifikasi baris Addon: Maintenance menampilkan Total 50, Used 50, Available 0
14. Verifikasi Available = Total − Used pada setiap baris

### TC-AC-ACC-809: License Quota Tab Subscription tidak memuat baris Storage sedangkan Storage ada di Tab Storage

15. Verifikasi License Quota FAMS menampilkan baris Asset, Concurrent User, dan Addon: Maintenance
16. Verifikasi License Quota FAMS tidak memuat baris Storage
17. Klik sub-tab `SAMS`
18. Verifikasi License Quota SAMS menampilkan baris Asset dan Concurrent User
19. Verifikasi License Quota SAMS tidak memuat baris Storage
20. Klik sub-tab `SIEM`
21. Verifikasi License Quota SIEM menampilkan baris Log Source dan Concurrent User
22. Verifikasi License Quota SIEM tidak memuat baris Storage
23. Klik Tab `Storage`
24. Verifikasi Tab `Storage` menampilkan Quota Total (GB) 100

### TC-AC-ACC-262: Sort License Quota: default License Type A-Z dan kolom Total tiga state

25. Klik Tab `Subscription`, sub-tab `FAMS`
26. Verifikasi urutan awal License Quota (License Type A-Z): Addon: Maintenance, Asset, Concurrent User
27. Klik header `Total`
28. Verifikasi urutan setelah klik pertama: Concurrent User (25), Addon: Maintenance (50), Asset (650)
29. Klik header `Total` lagi
30. Verifikasi urutan setelah klik kedua: Asset (650), Addon: Maintenance (50), Concurrent User (25)
31. Klik header `Total` ketiga kali
32. Verifikasi urutan setelah klik ketiga kembali ke urutan awal: Addon: Maintenance, Asset, Concurrent User

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah Klik sub-tab dan Klik Tab adalah langkah penghubung (S-03). Urutan TC-809 sesudah TC-261 memakai sub-tab `FAMS` yang sudah aktif; TC-262 membuka ulang Tab `Subscription` sesudah TC-809 berpindah ke Tab `Storage`.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. TC-260 mencatat "Addon: [nama] (satu baris per addon term)" tanpa nama addon; spec memakai addon Maintenance dari TC-261.
