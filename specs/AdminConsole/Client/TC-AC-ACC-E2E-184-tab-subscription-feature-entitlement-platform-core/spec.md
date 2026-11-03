---
id: TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core
title: "Tab Subscription: Feature Entitlement per Sub-tab, Platform Core Client Free, dan Column Visibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-265
  - TC-AC-ACC-805
  - TC-AC-ACC-804
  - TC-AC-ACC-263
  - TC-AC-ACC-266
  - TC-AC-ACC-803
  - TC-AC-ACC-267
coverage:
  web: automated
---

# Tab Subscription: Feature Entitlement per Sub-tab, Platform Core Client Free, dan Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Client Paid; FAMS, SAMS, SIEM Active); C-DTL-2 "PT Uji Free" (Direct, Group Cabang Menteng, SAMS Active berplan Free (rank=0), FAMS dan SIEM No Subscription; Status Client Free). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### Client Paid "PT Sejahtera Abadi": TC-AC-ACC-265, TC-AC-ACC-805, TC-AC-ACC-804 (dan Paid TC-AC-ACC-263), TC-AC-ACC-266

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Addon Features
4. Verifikasi Addon Features hanya memuat kolom Feature dan Qty
5. Verifikasi addon yang belum dialokasikan tampil "0"
6. Klik ⋯ pada header tabel Fixed Asset Module
7. Verifikasi panel Column Visibility Fixed Asset Module memuat kolom Feature, Value, Source
8. Verifikasi baris data Fixed Asset Module tanpa ikon ⋯
9. Tutup panel Column Visibility
10. Klik ⋯ pada header tabel Feature Suites
11. Verifikasi panel Column Visibility Feature Suites memuat kolom Feature, Value, Source
12. Verifikasi baris data Feature Suites tanpa ikon ⋯
13. Tutup panel Column Visibility
14. Klik ⋯ pada header tabel Addon Features
15. Verifikasi panel Column Visibility Addon Features memuat kolom Feature, Qty
16. Verifikasi baris data Addon Features tanpa ikon ⋯
17. Tutup panel Column Visibility
18. Klik sub-tab `SIEM`, lalu klik ⋯ pada header tabel SIEM Module
19. Verifikasi panel Column Visibility SIEM Module memuat kolom Feature, Value, Source
20. Verifikasi baris data SIEM Module tanpa ikon ⋯
21. Verifikasi tidak ada tombol Add, Edit, atau Remove pada keempat tabel (Fixed Asset Module, Feature Suites, Addon Features, SIEM Module)
22. Tutup panel Column Visibility
23. Verifikasi sub-tab `SIEM` hanya memuat section SIEM Module (Log Source cap, Concurrent User cap, Source Plan Default) (TC-266)
24. Verifikasi sub-tab `SIEM` tanpa Platform Core, Fixed Asset Module, Feature Suites, dan Addon Features (TC-266)
25. Klik sub-tab `SAMS`, lalu lihat tabel License Quota dan Section "Feature Entitlement"
26. Verifikasi tabel License Quota sub-tab `SAMS` memuat baris Asset dan Concurrent User (TC-804)
27. Verifikasi section Platform Core tidak tampil pada Client Paid, disembunyikan total (TC-804, TC-263)
28. Verifikasi section Fixed Asset Module, Feature Suites, dan Addon Features tidak tampil pada sub-tab `SAMS` (TC-804)

### Client Free "PT Uji Free": TC-AC-ACC-803 (dan Free TC-AC-ACC-263), TC-AC-ACC-267

29. Kembali ke List lewat breadcrumb Client
30. Ganti isi Search dengan `PT Uji Free`, tekan Enter
31. Klik Company Name "PT Uji Free" untuk membuka Detail
32. Klik Tab `Subscription`, lalu klik sub-tab `SAMS`
33. Lihat Section "Feature Entitlement"
34. Verifikasi section Platform Core tampil dengan tabel berkolom Feature, Value, Source yang memuat baris "Supplier" (TC-803, TC-263)
35. Verifikasi catatan "Feature entitlements are configured in Plans & Features." tampil di bagian bawah Section Feature Entitlement (TC-803)
36. Verifikasi section Fixed Asset Module, Feature Suites, dan Addon Features tidak tampil (TC-803)
37. Klik sub-tab `FAMS`
38. Verifikasi area konten sub-tab `FAMS` menampilkan ilustrasi (package) dengan Title "No subscriptions yet" dan Description "Active and pending subscriptions for this client will appear here." (anchor sub-tab FAMS Client "PT Uji Free" sudah termuat)
39. Verifikasi baris Supplier tidak tampil di sub-tab `FAMS` (TC-267)

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu role pada satu surface, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Pembagian TC lintas spec: TC-263 (Free tampil, Paid disembunyikan) dipenuhi oleh Verifikasi bertanda (TC-263) di blok Client Paid dan Client Free spec ini; id TC-263 tetap satu spec.
- Temuan untuk QA (S-15): TC-263 dan TC-267 menyebut "Client Free" tanpa nama fixture. Satu-satunya Client Free di Tabel A3 adalah C-DTL-2 "PT Uji Free" dengan SAMS Free dan FAMS No Subscription, sehingga TC-267 ("baris Supplier tidak tampil di FAMS" pada Client Free) pada fixture ini hanya mengasersi empty state sub-tab FAMS; tidak ada fixture Client Free dengan term FAMS berplan Free. Precondition TC-263, TC-265, TC-266, TC-267 menunjuk Detail "PT Sejahtera Abadi" (Paid) sedangkan Langkah memakai Client Free; spec mengikuti fixture A3. Post Condition seluruh TC `-` sehingga tidak diasersi.
