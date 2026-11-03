---
id: TC-AC-ACC-E2E-201-purchase-history-license-plan-custom-dan-subscription-id
title: "Purchase History License Client Custom Plan: Badge Plan Custom, Search Custom, dan Subscription ID"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-806
  - TC-AC-ACC-938
  - TC-AC-ACC-807
coverage:
  web: automated
---

# Purchase History License Client Custom Plan: Badge Plan Custom, Search Custom, dan Subscription ID

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-1 "PT Uji Tabel Detail" (FAMS Active Professional; kartu Subscription Details Subscription ID `SUBS-20260101-Q2W3E`; Purchase History License 4 baris: Qty 500 Professional / Fixed Asset / New / Subscription ID `SUBS-20260101-Q2W3E`; Qty 150 Professional / Fixed Asset / Additional / `SUBS-20260101-Q2W3E`; Qty 25 Growth / Concurrent User / New / `SUBS-20260310-C7D8E`; Qty 20 Custom / Addon: Tracking / Additional / `SUBS-20260515-F1G2H`). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-806: Purchase History License kolom Plan menampilkan nama plan standar dan badge Custom

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Lihat kolom Plan pada tabel Purchase History License
5. Verifikasi baris Qty 500 dan Qty 150: Plan "Professional"
6. Verifikasi baris Qty 25: Plan "Growth"
7. Verifikasi baris Qty 20: Plan menampilkan badge `Custom` (bukan nama plan standar)

### TC-AC-ACC-938: Kolom Subscription di Purchase History License sama dengan Subscription ID kartu Subscription Details untuk term yang sama

8. Lihat Subscription ID pada Section "Subscription Details"
9. Verifikasi Subscription ID kartu `SUBS-20260101-Q2W3E`
10. Lihat kolom Subscription pada baris Qty 500 dan Qty 150 di Purchase History License
11. Verifikasi kolom Subscription baris Qty 500 dan baris Qty 150 `SUBS-20260101-Q2W3E` (sama dengan kartu)
12. Lihat kolom Subscription pada baris Qty 25 dan Qty 20 di Purchase History License
13. Verifikasi kolom Subscription baris Qty 25 `SUBS-20260310-C7D8E` dan baris Qty 20 `SUBS-20260515-F1G2H` (berbeda dari kartu)
14. Verifikasi keempat nilai kolom Subscription (baris Qty 500, Qty 150, Qty 25, Qty 20) berformat `SUBS-YYYYMMDD-XXXXX`

### TC-AC-ACC-807: Search Purchase History License menemukan Plan bertipe badge Custom

15. Klik Search pada Purchase History License, ketik `Custom` dan tekan Enter
16. Verifikasi satu baris tampil: Qty 20 dengan Plan badge `Custom`
17. Verifikasi baris Qty 500, Qty 150, dan Qty 25 tidak tampil
18. Klik ikon ✕ pada input Search lalu tekan Enter

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Urutan: TC-806 dan TC-938 (screening) sebelum TC-807 (Search); pengosongan Search di akhir adalah langkah penghubung (S-09).
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Nilai Date baris tidak diasersi pada ketiga TC ini.
