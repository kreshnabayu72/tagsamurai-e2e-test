---
id: TC-AC-ACC-E2E-185-tab-subscription-feature-entitlement-source-plan
title: "Tab Subscription: Source Feature Entitlement Plan Default dan Custom Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-264
  - TC-AC-ACC-808
coverage:
  web: automated
---

# Tab Subscription: Source Feature Entitlement Plan Default dan Custom Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Professional, tanpa override), C-DTL-1 "PT Uji Tabel Detail" (Professional, Default Plan; Approval Workflow Available; Borrowing, Assignment, Transfer, Disposal Full; Accounting & Depreciation Single Depreciation), C-W3DTL-2 "PT Grace Kustom Uji" (FAMS Grace berplan Custom; di-seed ulang tiap putaran eksekusi karena status Grace bergantung waktu). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1 (spec TC-238 dan TC-800 memakai salinan bersuffix).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-264: Value sub-level dan Available serta Source Plan Default tanpa badge pada term Default Plan

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat tabel Fixed Asset Module dan Feature Suites
4. Verifikasi Approval Workflow Value "Available"
5. Verifikasi Borrowing, Assignment, Transfer, dan Disposal Value "Full"
6. Verifikasi Accounting & Depreciation Value "Single Depreciation"
7. Verifikasi seluruh Source "Plan Default" tanpa badge
8. Kembali ke List lewat breadcrumb Client
9. Ganti isi Search dengan `PT Uji Tabel Detail`, tekan Enter
10. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
11. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat tabel Fixed Asset Module dan Feature Suites
12. Verifikasi Approval Workflow Value "Available"
13. Verifikasi Borrowing, Assignment, Transfer, dan Disposal Value "Full"
14. Verifikasi Accounting & Depreciation Value "Single Depreciation"
15. Verifikasi seluruh Source "Plan Default" tanpa badge

### TC-AC-ACC-808: Source Feature Entitlement term Custom Plan berbadge primary

16. Verifikasi "PT Uji Tabel Detail" (plan Professional, Default Plan): Source seluruh baris tabel Fixed Asset Module dan Feature Suites "Plan Default" tanpa badge
17. Kembali ke List lewat breadcrumb Client
18. Ganti isi Search dengan `PT Grace Kustom Uji`, tekan Enter
19. Klik Company Name "PT Grace Kustom Uji" untuk membuka Detail
20. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat kolom Source pada tabel Fixed Asset Module dan Feature Suites
21. Verifikasi "PT Grace Kustom Uji" (Custom Plan): Source seluruh baris tabel Fixed Asset Module dan Feature Suites "Custom Plan" dengan badge severity primary
22. Verifikasi tidak ada baris yang Source-nya berbeda dari baris lain dalam satu term

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- TC-808 butir a memakai halaman "PT Uji Tabel Detail" yang sudah terbuka pada TC-264 (S-10); langkah Search/Kembali adalah langkah penghubung (S-03).
- Temuan untuk QA (S-15): TC-264 menyebut fixture baru C-DTL-1 "dipulihkan" oleh TC-238 dan melarang TC-264 berjalan bersamaan dengan TC-238; spec ini hanya membaca C-DTL-1 residen dan TC-238/TC-800 memakai salinan bersuffix. Seed "PT Grace Kustom Uji" perlu di-seed ulang tiap putaran (status Grace bergantung waktu). Post Condition seluruh TC `-`.
