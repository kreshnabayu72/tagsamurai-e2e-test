---
id: TC-AC-ACC-E2E-203-hover-nama-lengkap-action-by-dan-modified-by
title: "Hover Action by dan Modified By Menampilkan Nama Lengkap pada Tabel Detail dan Modal Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-812
  - TC-AC-ACC-813
coverage:
  web: automated
---

# Hover Action by dan Modified By Menampilkan Nama Lengkap pada Tabel Detail dan Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-DTL-1 "PT Uji Tabel Detail" (Action by: Purchase History License Qty 500 Andi Wijaya dan Qty 150 Andi Wijayanto; TAG Qty 100 Andi Wijaya; Hardware Qty 20 Andi Wijaya; Storage Qty (GB) 50 Andi Wijaya) dan C-01 "PT Sejahtera Abadi" (Changelog Client memuat baris Create dengan Modified By Andi Wijaya; Changelog Subscription dan Changelog Asset Control masing-masing memuat minimal satu baris Modified By Andi Wijaya). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-812: Hover Action by di Purchase History License, TAG, Hardware, dan Storage menampilkan nama lengkap

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Arahkan kursor ke Action by pada baris Qty 500 di Purchase History License
5. Verifikasi License Qty 500: sel "Andi W", tooltip "Andi Wijaya"
6. Arahkan kursor ke Action by pada baris Qty 150 di Purchase History License
7. Verifikasi License Qty 150: sel "Andi W", tooltip "Andi Wijayanto"
8. Klik Tab `TAG`
9. Arahkan kursor ke Action by pada baris Qty 100 di Purchase History TAG
10. Verifikasi TAG Qty 100: sel "Andi W", tooltip "Andi Wijaya"
11. Klik Tab `Hardware`
12. Arahkan kursor ke Action by pada baris Qty 20 di Purchase History Hardware
13. Verifikasi Hardware Qty 20: sel "Andi W", tooltip "Andi Wijaya"
14. Klik Tab `Storage`
15. Arahkan kursor ke Action by pada baris Qty (GB) 50 di Purchase History Storage
16. Verifikasi Storage Qty (GB) 50: sel "Andi W", tooltip "Andi Wijaya"

### TC-AC-ACC-813: Hover Modified By di modal Changelog: Client, Subscription, dan Asset Control menampilkan nama lengkap

17. Kembali ke List lewat breadcrumb Client
18. Klik `[Changelog]` di toolbar List
19. Ketik Search modal `PT Sejahtera Abadi`, tekan Enter
20. Arahkan kursor ke Modified By pada baris Action Create "PT Sejahtera Abadi"
21. Verifikasi Changelog Client: sel "Andi W", tooltip "Andi Wijaya"
22. Tutup modal Changelog
23. Ganti isi Search dengan `PT Sejahtera Abadi`, tekan Enter
24. Buka Detail "PT Sejahtera Abadi", klik Tab `Subscription`, lalu klik `[Changelog]`
25. Arahkan kursor ke Modified By pada baris dengan Modified By "Andi W"
26. Verifikasi Changelog Subscription: sel "Andi W", tooltip "Andi Wijaya"
27. Tutup modal Changelog
28. Klik Tab `Asset Control`, lalu klik ikon Changelog
29. Arahkan kursor ke Modified By pada baris dengan Modified By "Andi W"
30. Verifikasi Changelog Asset Control: sel "Andi W", tooltip "Andi Wijaya"
31. Tutup modal Changelog

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah Search modal Changelog untuk menemukan baris Create target, penutupan modal, dan Kembali ke List adalah langkah penghubung (S-03). Tooltip diasersi segera setelah hover (bagian 8b butir 5).
- Pembagian TC lintas spec: viewer dan modal Changelog lain (screening, Search, Filter, Sort, Setup Column) ada di spec slice lain; id TC-813 tetap satu spec.
- Temuan untuk QA (S-15): TC-813 menyebut baris Changelog Client Action Create "PT Sejahtera Abadi" tanpa menyebut cara menemukannya di modal; spec memakai Search modal. Post Condition kedua TC `-`.
