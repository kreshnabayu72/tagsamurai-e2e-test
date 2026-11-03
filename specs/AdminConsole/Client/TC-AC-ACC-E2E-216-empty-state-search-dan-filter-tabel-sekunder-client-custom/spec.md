---
id: TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom
title: "Empty State Hasil Search dan Filter Kosong pada Purchase History dan Hardware List Client Custom"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-847
  - TC-AC-ACC-848
  - TC-AC-ACC-849
  - TC-AC-ACC-850
  - TC-AC-ACC-852
coverage:
  web: automated
---

# Empty State Hasil Search dan Filter Kosong pada Purchase History dan Hardware List Client Custom

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-1 "PT Uji Tabel Detail": Purchase History License 4 baris, Purchase History TAG 3 baris, Hardware List 3 baris, Purchase History Hardware 3 baris, Purchase History Storage 3 baris. Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-847: Empty state hasil search dan filter kosong pada Purchase History License

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Klik Search pada Purchase History License, ketik `zzzz` dan tekan Enter
5. Verifikasi Purchase History License menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
6. Kosongkan isi kotak search, tekan Enter
7. Verifikasi empat baris Purchase History License tampil kembali
8. Klik Filter, isi Qty Min 1000 dan Max 2000, lalu klik `[Apply]`
9. Verifikasi Purchase History License menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
10. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACC-848: Empty state hasil search dan filter kosong pada Purchase History TAG

11. Klik Tab `TAG`
12. Klik Search pada Purchase History TAG, ketik `zzzz` dan tekan Enter
13. Verifikasi Purchase History TAG menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
14. Kosongkan isi kotak search, tekan Enter
15. Verifikasi tiga baris Purchase History TAG tampil kembali
16. Klik Filter, isi Qty Min 1000 dan Max 2000, lalu klik `[Apply]`
17. Verifikasi Purchase History TAG menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
18. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACC-849: Empty state hasil search kosong pada Hardware List

19. Klik Tab `Hardware`
20. Klik Search pada Hardware List, ketik `zzzz` dan tekan Enter
21. Verifikasi Hardware List menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
22. Kosongkan isi kotak search, tekan Enter
23. Verifikasi tiga baris Hardware List tampil kembali

### TC-AC-ACC-850: Empty state hasil search dan filter kosong pada Purchase History Hardware

24. Klik Search pada Purchase History Hardware, ketik `zzzz` dan tekan Enter
25. Verifikasi Purchase History Hardware menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
26. Kosongkan isi kotak search, tekan Enter
27. Verifikasi tiga baris Purchase History Hardware tampil kembali
28. Klik Filter, isi Qty Min 1000 dan Max 2000, lalu klik `[Apply]`
29. Verifikasi Purchase History Hardware menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
30. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACC-852: Empty state hasil search dan filter kosong pada Purchase History Storage

31. Klik Tab `Storage`
32. Klik Search pada Purchase History Storage, ketik `zzzz` dan tekan Enter
33. Verifikasi Purchase History Storage menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
34. Kosongkan isi kotak search, tekan Enter
35. Verifikasi tiga baris Purchase History Storage tampil kembali
36. Klik Filter, isi Qty Min 1000 dan Max 2000, lalu klik `[Apply]`
37. Verifikasi Purchase History Storage menampilkan Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
38. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pencarian dan penyaringan pada satu Client, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Asersi tabel kembali berisi sesudah Search dikosongkan memakai jumlah baris seed; empty state "No results found" menjadi anchor positif untuk hasil kosong (bagian 8b butir 2). Langkah `[Clear Field]` lalu `[Apply]` memenuhi Post Condition TC (Clear Field pada Filter) sebagai langkah penghubung (S-09, D-003).
- Temuan untuk QA (S-15): TC-849 hanya menguji Search karena Hardware List tidak memiliki Filter yang menghasilkan kosong di TC ini. Sub-tab FAMS tidak disebut TC-847 secara eksplisit selain pada Langkah; spec mengikuti Langkah.
