---
id: TC-AC-ACC-E2E-219-loading-state-tabel-tab-detail
title: "Loading State saat Data Tabel Tab Subscription, TAG, Hardware, Asset Control, dan Storage Diambil"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-857
coverage:
  web: automated
---

# Loading State saat Data Tabel Tab Subscription, TAG, Hardware, Asset Control, dan Storage Diambil

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-01 "PT Sejahtera Abadi". Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: menahan response data tiap tabel (network throttling atau intercept yang menunda response) untuk License Quota, Quota TAG, Hardware List, Station List, dan Quota Storage; endpoint tidak disebut TC sehingga disediakan tim FE (S-13). Penahanan hanya untuk mengamati state Loading (bukan kegagalan) dan dilepas segera sesudah asersi (S-09); hook `after` melepas tahanan yang tersisa.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-857: Loading state saat data tabel diambil

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Tahan response data tabel License Quota, lalu klik Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi Loading component tampil pada tabel License Quota selama data diambil
5. Lepaskan tahanan response tabel License Quota
6. Verifikasi baris tabel License Quota tampil setelah response
7. Tahan response data tabel Quota TAG, lalu klik Tab `TAG`
8. Verifikasi Loading component tampil pada tabel Quota TAG selama data diambil
9. Lepaskan tahanan response tabel Quota TAG
10. Verifikasi baris tabel Quota TAG tampil setelah response
11. Tahan response data tabel Hardware List, lalu klik Tab `Hardware`
12. Verifikasi Loading component tampil pada tabel Hardware List selama data diambil
13. Lepaskan tahanan response tabel Hardware List
14. Verifikasi baris tabel Hardware List tampil setelah response
15. Tahan response data tabel Station List, lalu klik Tab `Asset Control`
16. Verifikasi Loading component tampil pada tabel Station List selama data diambil
17. Lepaskan tahanan response tabel Station List
18. Verifikasi baris tabel Station List tampil setelah response
19. Tahan response data tabel Quota Storage, lalu klik Tab `Storage`
20. Verifikasi Loading component tampil pada tabel Quota Storage selama data diambil
21. Lepaskan tahanan response tabel Quota Storage
22. Verifikasi baris tabel Quota Storage tampil setelah response

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Lepaskan tahanan response" adalah langkah penghubung (S-03). Loading diasersi sebelum tahanan dilepas (bagian 8b butir 5).
- Temuan untuk QA (S-15): Post Condition TC-857 `-` sehingga tidak diasersi. TC tidak menyebut waktu tahanan; tahanan dilepas segera sesudah asersi.
