---
id: TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link
title: "Tab Subscription: Screening FAMS, Banner Read-only, Tanpa Aksi Write, dan Link Manage in Client Subscription"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-256
  - TC-AC-ACC-259
  - TC-AC-ACC-257
  - TC-AC-ACC-802
  - TC-AC-ACC-258
coverage:
  web: automated
---

# Tab Subscription: Screening FAMS, Banner Read-only, Tanpa Aksi Write, dan Link Manage in Client Subscription

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-01 "PT Sejahtera Abadi" (FAMS Active, Professional). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).

## Test Steps

### TC-AC-ACC-256: Screening Tab Subscription sub-tab FAMS

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi sub-tab produk `FAMS (aktif) | SAMS | SIEM`
5. Verifikasi info banner "This tab is read-only. To add, renew, or cancel a subscription, use Manage in Client Subscription."
6. Verifikasi toolbar `Manage in Client Subscription → | Download | Changelog`
7. Verifikasi Section Subscription Details menampilkan Subscription ID `SUBS-YYYYMMDD-XXXXX` | Plan | Status badge | Start | End (tampil bila terisi) | Grace End (terisi hanya untuk status Expired/Grace, selain itu `—`)
8. Verifikasi Section Subscription Details tanpa elipsis aksi
9. Verifikasi tabel License Quota menampilkan kolom `License Type | Total | Used | Available` dengan baris Asset, Concurrent User, dan Addon: [nama addon]
10. Verifikasi tabel License Quota tanpa ikon Search dan tanpa tombol Filter
11. Verifikasi Section Feature Entitlement menampilkan Fixed Asset Module, Feature Suites, dan Addon Features (Feature | Qty), dengan Platform Core hanya jika Client Free
12. Verifikasi catatan "Feature entitlements are configured in Plans & Features." tampil
13. Verifikasi tabel Feature Entitlement tanpa ikon Search dan tanpa tombol Filter
14. Verifikasi Section Purchase History License menampilkan Search dengan placeholder "Search by subscription, plan, or item...", Filter, dan Download
15. Verifikasi tabel Purchase History License berkolom 11 kolom + ⋯ dengan kolom Subscription berisi Subscription ID
16. Verifikasi Pagination default 10
17. Verifikasi opsi page size 10/25/50/100

### TC-AC-ACC-259: Teks info banner Tab Subscription

18. Baca info banner pada Tab `Subscription`
19. Verifikasi teks info banner "This tab is read-only. To add, renew, or cancel a subscription, use Manage in Client Subscription."

### TC-AC-ACC-257: Tab Subscription tidak memiliki aksi write

20. Periksa seluruh Tab `Subscription`
21. Verifikasi tidak ada tombol Add/Renew/Cancel/edit; tidak ada elipsis aksi pada ringkasan

### TC-AC-ACC-802: Subscription Details tampil sebagai kartu ringkas tanpa kolom dan tanpa Column Visibility

22. Lihat Section "Subscription Details"
23. Verifikasi Section "Subscription Details" menampilkan satu kartu berisi Subscription ID (format `SUBS-YYYYMMDD-XXXXX`), Plan, Status badge, Start, dan End
24. Verifikasi kartu tidak memiliki header kolom dan tidak memiliki ikon ⋯ Column Visibility
25. Lihat header tabel License Quota
26. Verifikasi tabel License Quota memiliki ikon ⋯ pada header kolom paling kanan

### TC-AC-ACC-258: Link Manage in Client Subscription navigasi ter-filter ke Client

27. Klik link `Manage in Client Subscription →`
28. Verifikasi halaman Admin Console > Client Subscription > List Subscriptions terbuka
29. Verifikasi List Subscriptions ter-filter ke "PT Sejahtera Abadi"

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Urutan: TC-258 (navigasi keluar halaman) diletakkan paling akhir agar TC lain tetap pada Tab `Subscription`; TC-259 dan TC-257 dijalankan sesudah screening tanpa membuka ulang halaman (S-10).
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. TC-256 menyebut "tabel 11 kolom + ⋯" tanpa menyebut nama kolom lengkap pada butir itu (nama kolom diverifikasi di TC-280 spec lain); spec memverifikasi jumlah kolom sesuai Expected.
