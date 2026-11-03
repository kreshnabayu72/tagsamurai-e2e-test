---
id: TC-AC-ACC-E2E-187-tab-subscription-term-terakhir-archive-purge-deleted-dan-ditolak
title: "Tab Subscription: Term Terakhir Archive, Purge, Deleted dan Client dengan Term Rejected atau Canceled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-936
  - TC-AC-ACC-937
coverage:
  web: automated
---

# Tab Subscription: Term Terakhir Archive, Purge, Deleted dan Client dengan Term Rejected atau Canceled

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-W3DTL-1 "PT Riwayat Arsip Uji" (Archived; FAMS satu-satunya term Archive SUBS-20240101-J7K8L Plan Growth Start 01 Jan 2024 End 31 Dec 2024; SAMS satu-satunya term Purge SUBS-20230601-P1Q2R Start 01 Jun 2023 End 31 May 2024; SIEM satu-satunya term Deleted SUBS-20230401-D4E5F Start 01 Apr 2023 End 31 Mar 2024), C-LIF-1 "PT Pengajuan Ditolak" (Active; FAMS satu-satunya term Rejected, SAMS satu-satunya term Canceled, SIEM tidak pernah berlangganan). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-936: Subscription Details dan License Quota menampilkan term terakhir bila semua term berstatus Archive, Purge, atau Deleted

1. Klik sub-tab `Archived`, ketik Search `PT Riwayat Arsip Uji`, tekan Enter
2. Klik Company Name "PT Riwayat Arsip Uji" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
4. Verifikasi Section "Subscription Details" memuat satu kartu dengan Subscription ID `SUBS-20240101-J7K8L`, Plan "Growth", Status badge `Archive` (severity dark), Start "01 Jan 2024", End "31 Dec 2024", dan Grace End `—`
5. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0); tidak ada baris Addon
6. Verifikasi empty state "No subscriptions yet" tidak tampil
7. Klik sub-tab `SAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
8. Verifikasi kartu memuat Subscription ID `SUBS-20230601-P1Q2R`, Status badge `Purge` (severity dark), Start "01 Jun 2023", End "31 May 2024", dan Grace End `—`
9. Verifikasi tabel License Quota SAMS memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0); tidak ada baris Addon
10. Klik sub-tab `SIEM`, lalu lihat Section "Subscription Details" dan tabel License Quota
11. Verifikasi kartu memuat Subscription ID `SUBS-20230401-D4E5F`, Status badge `Deleted` (severity dark), Start "01 Apr 2023", End "31 Mar 2024", dan Grace End `—`
12. Verifikasi tabel License Quota SIEM memuat baris Log Source (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0); tidak ada baris Addon

### TC-AC-ACC-937: Client yang term terakhirnya Rejected atau Canceled tanpa term sebelumnya menampilkan empty state

13. Kembali ke List lewat breadcrumb Client
14. Klik sub-tab `Active`, ketik Search `PT Pengajuan Ditolak`, tekan Enter
15. Klik Company Name "PT Pengajuan Ditolak" untuk membuka Detail
16. Klik Tab `Subscription` lalu lihat isinya
17. Verifikasi Tab `Subscription` menampilkan Illustration (package) dengan Title "No subscriptions yet" dan Description "Active and pending subscriptions for this client will appear here."
18. Verifikasi Section "Subscription Details" tidak tampil dan tidak ada Status badge `Rejected` maupun `Canceled`
19. Verifikasi link `Manage in Client Subscription →` (deep-link) tampil
20. Verifikasi strip sub-tab `[FAMS] [SAMS] [SIEM]` tetap tampil dan empty state hanya mengisi area konten sub-tab `FAMS`
21. Klik sub-tab `SAMS`
22. Verifikasi strip sub-tab `[FAMS] [SAMS] [SIEM]` tetap tampil dan area konten sub-tab `SAMS` menampilkan empty state "No subscriptions yet"
23. Klik sub-tab `SIEM`
24. Verifikasi strip sub-tab `[FAMS] [SAMS] [SIEM]` tetap tampil dan area konten sub-tab `SIEM` menampilkan empty state "No subscriptions yet"

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah klik sub-tab List dan Kembali ke List adalah langkah penghubung (S-03). Nilai ledger seed (mis. Asset 100/40/60) tidak diasersi karena TC-936 menyatakan nilai tampil 0 untuk term Archive, Purge, dan Deleted.
- Temuan untuk QA (S-15): TC-937 menyebut Detail dibuka dari sub-tab Active (Client Active); Tabel A3 menyatakan C-LIF-1 Active. Post Condition seluruh TC `-` sehingga tidak diasersi.
