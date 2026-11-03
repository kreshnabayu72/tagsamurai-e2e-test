---
id: TC-AC-ACC-E2E-190-total-quota-qr-tab-tag-dari-asset-license-term
title: "Tab TAG: Total Quota QR dari Asset License Term Active dan Grace"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-285
  - TC-AC-ACC-996
  - TC-AC-ACC-997
coverage:
  web: automated
---

# Tab TAG: Total Quota QR dari Asset License Term Active dan Grace

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (FAMS dan SAMS Active), C-FX14-5 "PT Kuota QR Multi Term" (Active; FAMS Active asset license 100 dan Renewal Pending asset license 30; SAMS Grace asset license 50; Used 0), C-FX14-6 "PT Kuota QR Terminal" (Archived; FAMS Purge asset license 100, SAMS Deleted asset license 60). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-285: Quota QR = SUM asset license term paid Active dan Grace; QR tidak muncul di Purchase History

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu catat Total pada baris Asset License Quota
4. Klik sub-tab `SAMS`, lalu catat Total pada baris Asset License Quota
5. Klik Tab `TAG`, lalu lihat baris QR pada tabel Quota
6. Verifikasi Total Quota baris QR sama dengan jumlah asset license term berstatus Active dan Grace yang dicatat dari License Quota (term Expired, Pending, Waiting for Approval, Archive, Purge, dan Deleted dihitung 0)
7. Verifikasi Available = Total − Used pada baris QR
8. Lihat tabel Purchase History TAG
9. Verifikasi tabel Purchase History TAG memuat baris Type RFID dan baris Type NFC (baris seed P-T1 dan P-T2)
10. Verifikasi tipe QR tidak pernah muncul di Purchase History TAG

### TC-AC-ACC-996: Total Quota QR menjumlah asset license term Active dan Grace; term Pending tidak ikut dihitung

11. Kembali ke List lewat breadcrumb Client
12. Klik sub-tab `Active`, ganti isi Search dengan `PT Kuota QR Multi Term`, tekan Enter
13. Klik Company Name "PT Kuota QR Multi Term" untuk membuka Detail
14. Klik Tab `TAG`, lalu lihat baris QR pada tabel Quota
15. Verifikasi baris QR menampilkan Total Quota 150 (FAMS Active 100 + SAMS Grace 50), Used 0, Available 150
16. Verifikasi Total Quota bukan 180 (alokasi Renewal berstatus Pending tidak ikut dihitung)

### TC-AC-ACC-997: Total Quota QR bernilai 0 pada Client dengan term terminal (Purge dan Deleted)

17. Kembali ke List lewat breadcrumb Client
18. Klik sub-tab `Archived`, ketik Search `PT Kuota QR Terminal`, tekan Enter
19. Klik Company Name "PT Kuota QR Terminal" untuk membuka Detail
20. Klik Tab `TAG`, lalu lihat baris QR pada tabel Quota
21. Verifikasi baris QR tetap tampil dengan Total Quota 0, Used 0, Available 0 (term Purge dan Deleted dihitung 0)
22. Verifikasi empty state kuota tidak tampil

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah 9 (comparator positif) memastikan tabel Purchase History TAG sudah termuat sebelum asersi absence tipe QR; baris seed P-T1 (RFID) dan P-T2 (NFC) berasal dari Tabel A3 F6 milik C-01 (baca-saja).
- Langkah "catat Total pada baris Asset License Quota" (TC-285) adalah langkah penghubung: nilai dicatat untuk membandingkan jumlah, bukan Verifikasi.
- Pembagian TC lintas spec: kuota QR bernilai 0 pada term Expired/Archive dan Pending/Waiting for Approval (TC-1005, TC-1009) serta kuota Trial yang tidak dijumlahkan (TC-1024) diasersi di spec lain; id TC masing-masing tetap satu spec.
- Temuan untuk QA (S-15): TC-285 tidak menyebut angka Total Quota QR pada C-01 (Tabel A2 hanya menyatakan "TAG dan Hardware quota terisi"); spec menurunkan nilai dari License Quota Asset FAMS dan SAMS sebagai jumlah term Active dan Grace. Post Condition seluruh TC `-`.
