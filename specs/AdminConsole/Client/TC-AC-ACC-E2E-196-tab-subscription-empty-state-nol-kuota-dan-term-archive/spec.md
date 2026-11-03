---
id: TC-AC-ACC-E2E-196-tab-subscription-empty-state-nol-kuota-dan-term-archive
title: "Tab Subscription: Empty State, Kuota Nol dengan Purchase History Kosong, dan Term Archive Tanpa Aksi Renew"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-272
  - TC-AC-ACC-273
  - TC-AC-ACC-274
coverage:
  web: automated
---

# Tab Subscription: Empty State, Kuota Nol dengan Purchase History Kosong, dan Term Archive Tanpa Aksi Renew

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-04 "PT Karya Abadi" (Archived; FAMS Archive), C-09 "PT Baru Daftar" (tanpa subscription), C-02 "PT Teknologi Maju" (FAMS Grace; tanpa kuota/riwayat). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-272: Aturan Add/Renew/Cancel dimiliki License Allocation: Tab Client tidak menampilkan aksi basi

1. Klik sub-tab `Archived`, ketik Search `PT Karya Abadi`, tekan Enter
2. Klik Company Name "PT Karya Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi Status badge `Archive` tampil pada Section "Subscription Details"
5. Verifikasi tidak ada aksi Renew di tab ini

### TC-AC-ACC-273: Empty state Tab Subscription tanpa subscription

6. Kembali ke List lewat breadcrumb Client
7. Klik sub-tab `Active`, ketik Search `PT Baru Daftar`, tekan Enter
8. Klik Company Name "PT Baru Daftar" untuk membuka Detail
9. Klik Tab `Subscription`
10. Verifikasi Tab `Subscription` menampilkan Illustration (package) dengan Title "No subscriptions yet" dan Description "Active and pending subscriptions for this client will appear here."
11. Verifikasi strip sub-tab `[FAMS] [SAMS] [SIEM]` tetap tampil dan empty state hanya mengisi area konten sub-tab terpilih
12. Verifikasi link `Manage in Client Subscription →` (deep-link) tampil

### TC-AC-ACC-274: License Quota menampilkan nol (tanpa empty state) dan Purchase History empty state

13. Kembali ke List lewat breadcrumb Client
14. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter
15. Klik Company Name "PT Teknologi Maju" untuk membuka Detail
16. Klik Tab `Subscription`, sub-tab `FAMS`
17. Verifikasi License Quota: baris Asset dan Concurrent User menampilkan Total 0, Used 0, Available 0
18. Verifikasi empty state kuota License Quota tidak tampil
19. Verifikasi Purchase History menampilkan "No purchase history yet" dan "License purchase history will appear here."

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Temuan untuk QA (S-15): TC-272 Precondition menyebut Detail "PT Sejahtera Abadi" (Active) padahal Langkah "Buka Tab Subscription term Archive" butuh Client dengan term Archive; spec memakai C-04 "PT Karya Abadi" (FAMS Archive) dari Tabel A2. TC-274 Langkah "Client tanpa quota/riwayat" tidak menyebut sub-tab; spec memakai sub-tab `FAMS` (FAMS Grace pada C-02) dan Expected menyebut baris Asset dan Concurrent User pada sub-tab FAMS. Post Condition seluruh TC `-`.
