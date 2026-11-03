---
id: TC-AC-ACC-E2E-303-pagination-dan-seleksi-manual-bertahan
title: "Client List: Pagination, Seleksi Manual Bertahan Saat Pindah Halaman, Berganti Search, dan Apply-Clear Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-415
  - TC-AC-ACC-718
  - TC-AC-ACC-719
  - TC-AC-ACC-720
coverage:
  web: automated
---

# Client List: Pagination, Seleksi Manual Bertahan Saat Pindah Halaman, Berganti Search, dan Apply-Clear Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Sub-tab Active memuat 30 baris `PT Uji Halaman 01` sampai `PT Uji Halaman 30` (C-14) selain C-01 sampai C-13 (lebih dari 30 baris); fixture residen yang hanya dibaca.
- Seleksi baris hanya state UI (tidak ada aksi bulk dijalankan); seleksi dibersihkan lewat ikon `×` di akhir tiap blok. Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Pagination (TC-AC-ACC-415)

1. Lihat Pagination di footer tabel
2. Verifikasi page size default `10`
3. Buka Overlay Page Size
4. Verifikasi opsi page size `10`, `25`, `50`, dan `100`
5. Ubah page size ke `25`
6. Verifikasi page size `25` terpilih
7. Ubah page size ke `50`
8. Verifikasi page size `50` terpilih
9. Ubah page size ke `100`
10. Verifikasi page size `100` terpilih
11. Ubah page size ke `10`, lalu ketik nomor halaman `2` langsung pada input nomor halaman
12. Verifikasi halaman 2 aktif
13. Klik next
14. Verifikasi halaman 3 aktif
15. Klik prev
16. Verifikasi halaman 2 aktif

### Seleksi bertahan saat pindah halaman (TC-AC-ACC-718)

17. Centang dua baris pertama di halaman 1 (ukuran halaman 10)
18. Verifikasi counter `2 clients selected`
19. Pindah ke halaman 2 lalu centang baris pertama halaman 2
20. Verifikasi counter `3 clients selected`
21. Kembali ke halaman 1
22. Verifikasi dua baris pertama halaman 1 tetap tercentang
23. Verifikasi counter `3 clients selected`
24. Pindah ke halaman 2
25. Verifikasi baris pertama halaman 2 tetap tercentang
26. Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi, lalu kembali ke halaman 1

### Seleksi bertahan saat Search diubah dan dikosongkan (TC-AC-ACC-719)

27. Ketik Search `Baru Daftar`, tekan Enter
28. Centang `PT Baru Daftar`
29. Verifikasi counter `1 client selected`
30. Klik ikon `✕` pada input Search, ketik `Uji Halaman 01`, tekan Enter
31. Verifikasi sedikitnya satu baris hasil Search tampil (mis. `PT Uji Halaman 01`)
32. Verifikasi `PT Baru Daftar` tidak tampil di tabel hasil Search `Uji Halaman 01`
33. Centang `PT Uji Halaman 01`
34. Verifikasi counter `2 clients selected` (baris yang tidak tampil tetap dihitung)
35. Klik ikon `✕` pada input Search, tekan Enter
36. Ketik Search `Baru Daftar`, tekan Enter
37. Verifikasi `PT Baru Daftar` tercentang
38. Verifikasi counter `2 clients selected`
39. Klik ikon `✕` pada input Search, ketik `Uji Halaman 01`, tekan Enter
40. Verifikasi `PT Uji Halaman 01` tercentang
41. Verifikasi counter `2 clients selected`
42. Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi, lalu klik `(←)` pada kotak Search

### Seleksi bertahan saat Filter di-Apply dan di-Clear (TC-AC-ACC-720)

43. Ketik Search `Cahaya Baru`, tekan Enter
44. Centang `PT Cahaya Baru` (FAMS Waiting for Approval)
45. Verifikasi counter `1 client selected`
46. Klik ikon `✕` pada input Search, tekan Enter
47. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
48. Verifikasi counter tetap `1 client selected`
49. Ketik Search `Cahaya Baru`, tekan Enter
50. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (`PT Cahaya Baru` tidak tampil)
51. Verifikasi counter tetap `1 client selected`
52. Klik ikon `✕` pada input Search, ketik `Sejahtera Abadi`, tekan Enter, lalu centang `PT Sejahtera Abadi`
53. Verifikasi `PT Sejahtera Abadi` tampil dan tercentang
54. Verifikasi counter `2 clients selected`
55. Klik ikon `✕` pada input Search, tekan Enter
56. Klik Filter, klik [Clear Field], lalu klik [Apply]
57. Ketik Search `Cahaya Baru`, tekan Enter
58. Verifikasi `PT Cahaya Baru` tercentang
59. Verifikasi counter `2 clients selected`
60. Klik ikon `✕` pada input Search, ketik `Sejahtera Abadi`, tekan Enter
61. Verifikasi `PT Sejahtera Abadi` tercentang
62. Verifikasi counter `2 clients selected`
63. Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi, lalu klik `(←)` pada kotak Search

## Notes

- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness dan dataset (pagination dan state seleksi List) dan blok berurutan tanpa state bersama (seleksi dibersihkan di akhir tiap blok, S-09).
- Langkah penghubung (S-03): pembersihan seleksi lewat ikon `×` (Post Condition TC), `(←)` pada kotak Search, kembali ke halaman 1.
- Temuan untuk QA
  - TC-AC-ACC-415: Data Uji `30+ baris` tidak menyebut sub-tab; spec memakai sub-tab Active (C-01 sampai C-14 memberi lebih dari 30 baris).
  - TC-AC-ACC-719 dan TC-AC-ACC-720: Expected `Langkah 4` dan sebagainya merujuk nomor langkah lokal TC; spec menyusunnya sebagai `Verifikasi` tepat setelah aksinya (R-04).
