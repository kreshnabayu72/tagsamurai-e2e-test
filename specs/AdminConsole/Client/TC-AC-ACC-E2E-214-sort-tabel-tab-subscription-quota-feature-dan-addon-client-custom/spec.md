---
id: TC-AC-ACC-E2E-214-sort-tabel-tab-subscription-quota-feature-dan-addon-client-custom
title: "Tab Subscription Client Custom: Sort License Quota, Fixed Asset Module, dan Addon Features"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-828
  - TC-AC-ACC-829
  - TC-AC-ACC-830
coverage:
  web: automated
---

# Tab Subscription Client Custom: Sort License Quota, Fixed Asset Module, dan Addon Features

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-1 "PT Uji Tabel Detail". License Quota FAMS (Total/Used/Available): Asset 650/320/330; Concurrent User 25/12/13; Addon: Maintenance 50/50/0; Addon: Tracking 20/5/15. Fixed Asset Module: Group hierarchy depth 5, Group count 25, Category count 100, Approval Workflow Available, Scheduled reports Unlimited. Addon Features: Audit 0, Maintenance 50, Tracking 20. Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-828: Sort License Quota kolom Used dan Available

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Klik header Used
5. Verifikasi Used klik 1 (naik): Addon: Tracking (5), Concurrent User (12), Addon: Maintenance (50), Asset (320)
6. Klik header Used lagi
7. Verifikasi Used klik 2 (turun): Asset (320), Addon: Maintenance (50), Concurrent User (12), Addon: Tracking (5)
8. Klik header Used ketiga kali
9. Verifikasi Used klik 3 kembali ke urutan default License Type A-Z: Addon: Maintenance, Addon: Tracking, Asset, Concurrent User
10. Klik header Available
11. Verifikasi Available klik 1 (naik): Addon: Maintenance (0), Concurrent User (13), Addon: Tracking (15), Asset (330)
12. Klik header Available lagi
13. Verifikasi Available klik 2 (turun): Asset (330), Addon: Tracking (15), Concurrent User (13), Addon: Maintenance (0)

### TC-AC-ACC-829: Sort Feature Entitlement Fixed Asset Module: default Feature A-Z dan kolom Value campuran angka dan teks

14. Verifikasi urutan awal tabel Fixed Asset Module (Feature A-Z): Approval Workflow, Category count, Group count, Group hierarchy depth, Scheduled reports dalam urutan relatif tersebut
15. Klik header Value
16. Verifikasi Value klik 1: Group hierarchy depth (5), Group count (25), Category count (100), lalu Approval Workflow (Available), lalu Scheduled reports (Unlimited) dalam urutan relatif tersebut
17. Klik header Value lagi
18. Verifikasi Value klik 2: Scheduled reports (Unlimited), Approval Workflow (Available), lalu Category count (100), Group count (25), Group hierarchy depth (5) dalam urutan relatif tersebut
19. Klik header Value ketiga kali
20. Verifikasi Value klik 3: kembali ke urutan awal Feature A-Z

### TC-AC-ACC-830: Sort Addon Features: default Feature A-Z dan kolom Qty

21. Verifikasi urutan awal tabel Addon Features: Audit, Maintenance, Tracking
22. Klik header Qty
23. Verifikasi Qty klik 1: Audit (0), Tracking (20), Maintenance (50)
24. Klik header Qty lagi
25. Verifikasi Qty klik 2: Maintenance (50), Tracking (20), Audit (0)

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Pembagian TC lintas spec: sort Tab TAG dan Storage Client Custom ada di spec 206, sort Tab Hardware di spec 211; id TC masing-masing tetap satu spec. Sort License Quota Total (TC-262) pada C-01 ada di spec 183.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi.
