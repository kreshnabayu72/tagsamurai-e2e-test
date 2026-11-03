---
id: TC-AC-ACC-E2E-217-pagination-purchase-history-license
title: "Pagination Purchase History License: Page Size, Next, Previous, dan Input Nomor Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-859
  - TC-AC-ACC-860
coverage:
  web: automated
---

# Pagination Purchase History License: Page Size, Next, Previous, dan Input Nomor Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-3 "PT Uji Paginasi Detail" (Direct, Group Cabang Menteng; FAMS Active Professional; Purchase History License 30 baris dengan Qty 1 sampai 30; baris ber-Qty lebih besar memiliki Date lebih baru, Qty 30 paling baru). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-859: Pagination Purchase History License: default 10 baris, opsi page size 10/25/50/100, dan hasil tiap page size

1. Ketik Search `PT Uji Paginasi Detail`, tekan Enter
2. Klik Company Name "PT Uji Paginasi Detail" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Lihat Pagination tabel Purchase History License
5. Verifikasi default 10 baris per halaman
6. Verifikasi baris pertama Qty 30 dan baris kesepuluh Qty 21
7. Buka Overlay Page Size
8. Verifikasi opsi page size 10, 25, 50, 100
9. Pilih 25
10. Verifikasi halaman 1 memuat Qty 30 sampai Qty 6 (25 baris)
11. Klik halaman 2
12. Verifikasi halaman 2 memuat Qty 5 sampai Qty 1 (5 baris)
13. Pilih 50 pada Overlay Page Size
14. Verifikasi 30 baris tampil pada satu halaman
15. Pilih 100 pada Overlay Page Size
16. Verifikasi 30 baris tampil pada satu halaman
17. Pilih 10 pada Overlay Page Size untuk mengembalikan page size ke 10

### TC-AC-ACC-860: Pagination Purchase History License: next, previous, dan input nomor halaman

18. Klik next pada Pagination Purchase History License
19. Verifikasi halaman 2 memuat Qty 20 sampai Qty 11
20. Klik next
21. Verifikasi halaman 3 memuat Qty 10 sampai Qty 1 (10 baris)
22. Klik previous
23. Verifikasi halaman 2 memuat Qty 20 sampai Qty 11
24. Ketik nomor halaman 3 pada input halaman lalu tekan Enter
25. Verifikasi halaman 3 memuat Qty 10 sampai Qty 1
26. Ketik nomor halaman 1 pada input halaman lalu tekan Enter
27. Verifikasi halaman 1 memuat Qty 30 sampai Qty 21

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Pilih 10 pada Overlay Page Size" mengembalikan page size sesuai Post Condition TC-859 dan menjadi prasyarat TC-860 (page size 10); langkah penghubung (S-09).
- Temuan untuk QA (S-15): Post Condition TC-860 `-`. TC-860 Data menyebut page size 10 tanpa langkah mengatur; dipenuhi pemulihan TC-859.
