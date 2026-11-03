---
id: TC-AC-ACC-E2E-188-license-quota-dan-quota-qr-nol-pada-term-tidak-hidup
title: "License Quota dan Quota QR Bernilai 0 pada Term Expired, Archive, Waiting for Approval, Pending, dan Trial"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1005
  - TC-AC-ACC-1009
  - TC-AC-ACC-1034
  - TC-AC-ACC-1037
coverage:
  web: automated
---

# License Quota dan Quota QR Bernilai 0 pada Term Expired, Archive, Waiting for Approval, Pending, dan Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-FX15-6 "PT Kuota QR Expired Archive" (Active; FAMS Expired asset license 100, SAMS Archive asset license 60), C-FX16-2 "PT Kuota Menunggu" (Active; FAMS Waiting for Approval asset license 80, SAMS Pending asset license 40), C-FX18-2 "PT Trial Habis Tanpa Paid" (SAMS Trial Expired satu-satunya term; Group Area Jakarta), C-FX18-11 "PT Trial Menunggu Saja" (Active; SAMS Trial Waiting for Approval satu-satunya term; Group Area Jakarta). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-1005: Total Quota QR dan License Quota bernilai 0 pada term Expired dan Archive

1. Klik sub-tab `Active`, ketik Search `PT Kuota QR Expired Archive`, tekan Enter
2. Klik Company Name "PT Kuota QR Expired Archive" untuk membuka Detail
3. Klik Tab `TAG`, lalu lihat baris QR pada tabel Quota
4. Verifikasi baris QR tampil dengan Total Quota 0, Used 0, Available 0 (term Expired dan Archive dihitung 0)
5. Verifikasi empty state kuota tidak tampil
6. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
7. Verifikasi Status badge `Expired`
8. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0)
9. Klik sub-tab `SAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
10. Verifikasi Status badge `Archive`
11. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0)

### TC-AC-ACC-1009: License Quota bernilai 0 pada term Waiting for Approval dan Pending

12. Kembali ke List lewat breadcrumb Client
13. Klik sub-tab `Active`, ganti isi Search dengan `PT Kuota Menunggu`, tekan Enter
14. Klik Company Name "PT Kuota Menunggu" untuk membuka Detail
15. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
16. Verifikasi Status badge `Waiting for Approval`
17. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0)
18. Verifikasi tabel License Quota tidak memuat baris Addon
19. Klik sub-tab `SAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
20. Verifikasi Status badge `Pending`
21. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0)
22. Verifikasi tabel License Quota tidak memuat baris Addon
23. Klik Tab `TAG`, lalu lihat baris QR pada tabel Quota
24. Verifikasi baris QR tampil dengan Total Quota 0, Used 0, Available 0 (term Pending dan Waiting for Approval dihitung 0)
25. Verifikasi empty state kuota tidak tampil

### TC-AC-ACC-1034: Kartu License Quota term Trial Expired menampilkan baris Asset dan Concurrent User bernilai 0

26. Kembali ke List lewat breadcrumb Client
27. Klik sub-tab `Active`, ganti isi Search dengan `PT Trial Habis Tanpa Paid`, tekan Enter
28. Klik Company Name "PT Trial Habis Tanpa Paid" untuk membuka Detail
29. Klik Tab `Subscription`, sub-tab `SAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
30. Verifikasi Status badge `Expired`
31. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0)

### TC-AC-ACC-1037: Kartu License Quota term Trial Waiting for Approval menampilkan baris Asset dan Concurrent User bernilai 0, dan Client tetap di sub-tab Active

32. Kembali ke List lewat breadcrumb Client
33. Klik sub-tab `Active`, ganti isi Search dengan `PT Trial Menunggu Saja`, tekan Enter
34. Verifikasi baris "PT Trial Menunggu Saja" tampil di sub-tab `Active` (Trial Waiting for Approval tidak dihitung untuk Auto-Archive)
35. Klik Company Name "PT Trial Menunggu Saja" untuk membuka Detail
36. Klik Tab `Subscription`, sub-tab `SAMS`, lalu lihat Section "Subscription Details" dan tabel License Quota
37. Verifikasi Status badge `Waiting for Approval`
38. Verifikasi tabel License Quota memuat baris Asset (Total 0, Used 0, Available 0) dan Concurrent User (Total 0, Used 0, Available 0)

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu role pada satu surface, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Temuan untuk QA (S-15): TC-1034 Precondition dan Langkah menyebut "PT Trial Habis Tanpa Paid" berstatus Active dan memakai sub-tab Active, sedangkan Tabel A3 (C-FX18-2) menyatakan Client berstatus Archived ("Client otomatis Archived"); spec mengikuti Langkah TC (sub-tab `Active`) dan kontradiksi ini perlu dikonfirmasi QA. Post Condition seluruh TC `-` sehingga tidak diasersi.
