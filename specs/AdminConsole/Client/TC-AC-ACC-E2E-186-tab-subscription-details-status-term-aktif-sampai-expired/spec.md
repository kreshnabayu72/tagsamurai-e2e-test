---
id: TC-AC-ACC-E2E-186-tab-subscription-details-status-term-aktif-sampai-expired
title: "Tab Subscription: Subscription Details untuk Status Active, Waiting for Approval, Pending, Grace, dan Expired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-268
  - TC-AC-ACC-661
coverage:
  web: automated
---

# Tab Subscription: Subscription Details untuk Status Active, Waiting for Approval, Pending, Grace, dan Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-07 "PT Cahaya Baru" (FAMS Waiting for Approval), C-08 "PT Mulai Esok" (FAMS Pending; Start dan End terisi), C-W3DTL-2 "PT Grace Kustom Uji" (FAMS satu-satunya term Grace berplan Custom, Subscription ID SUBS-20250301-G6H7J; tanggal relatif terhadap waktu seed, di-seed ulang tiap putaran), C-03 "PT Wahana Nusantara" (Suspended; FAMS Expired), C-01 "PT Sejahtera Abadi" (FAMS Active). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-268: Subscription Details Start, End, dan Grace End untuk Waiting for Approval, Pending, dan Grace

1. Klik sub-tab `Active`, ketik Search `PT Cahaya Baru`, tekan Enter
2. Klik Company Name "PT Cahaya Baru" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details"
4. Verifikasi Status badge `Waiting for Approval` berseverity warning
5. Verifikasi Start, End, dan Grace End menampilkan `—`
6. Kembali ke List lewat breadcrumb Client
7. Ganti isi Search dengan `PT Mulai Esok`, tekan Enter
8. Klik Company Name "PT Mulai Esok" untuk membuka Detail
9. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details"
10. Verifikasi Status badge `Pending` berseverity warning
11. Verifikasi Start dan End menampilkan tanggal sesuai format General Settings
12. Verifikasi Grace End menampilkan `—`
13. Kembali ke List lewat breadcrumb Client
14. Ganti isi Search dengan `PT Grace Kustom Uji`, tekan Enter
15. Klik Company Name "PT Grace Kustom Uji" untuk membuka Detail
16. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details"
17. Verifikasi Status badge `Grace` berseverity warning
18. Verifikasi Plan menampilkan badge `Custom` (bukan nama plan standar)
19. Verifikasi Start, End, dan Grace End menampilkan tanggal sesuai format General Settings (Grace End bukan `—`)

### TC-AC-ACC-661: Grace End terisi untuk status Expired dan `—` untuk status Active

20. Kembali ke List lewat breadcrumb Client
21. Klik sub-tab `Suspended`, ketik Search `PT Wahana Nusantara`, tekan Enter
22. Klik Company Name "PT Wahana Nusantara" untuk membuka Detail
23. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details"
24. Verifikasi Status badge `Expired` berseverity danger
25. Verifikasi Start, End, dan Grace End menampilkan tanggal sesuai format General Settings (Grace End bukan `—`)
26. Kembali ke List lewat breadcrumb Client
27. Klik sub-tab `Active`, ganti isi Search dengan `PT Sejahtera Abadi`, tekan Enter
28. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
29. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat Section "Subscription Details"
30. Verifikasi Status badge `Active` berseverity success
31. Verifikasi Grace End menampilkan `—`

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu role pada satu surface, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah klik sub-tab dan Kembali ke List adalah langkah penghubung (S-03).
- Temuan untuk QA (S-15): TC-268 Langkah 1 menyebut "sub-tab Active" untuk "PT Cahaya Baru"; TC-661 menyebut sub-tab Suspended untuk "PT Wahana Nusantara". TC-268 Expected untuk Grace menyebut Plan `Custom` yang tidak ada di Langkah; spec mengikuti Expected. Post Condition seluruh TC `-`.
