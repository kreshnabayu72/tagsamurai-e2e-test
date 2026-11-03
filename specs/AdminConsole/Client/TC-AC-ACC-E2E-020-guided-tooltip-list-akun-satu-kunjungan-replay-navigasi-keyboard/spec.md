---
id: TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard
title: "Guided Tooltip Halaman Client List: Kunjungan Pertama, Berikutnya, Replay, Navigasi, dan Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-39
  - TC-AC-ACC-871
  - TC-AC-ACC-872
  - TC-AC-ACC-873
  - TC-AC-ACC-878
coverage:
  web: automated
---

# Guided Tooltip Halaman Client List: Kunjungan Pertama, Berikutnya, Replay, Navigasi, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-AST-2 | Total Control (Principal, akun Guided Tooltip 1) | `guidedTooltipSatu_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GT1_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-AST-2); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` untuk akun uji dalam spec ini (tabel akun) belum ada sebelum spec dimulai atau sesuai precondition tiap TC; reset flag per akun oleh hook `before` spec ini dan pemulihan ke keadaan awal oleh hook `after` memakai kemampuan reset flag yang disediakan tim FE (TC menyebut "dipulihkan lewat akun uji atau reset data").
- Pengecualian atas flag hook suite (bagian 4 konvensi): spec ini menguji flag itu sendiri, sehingga hook `before` suite tidak menyetel flag untuk akun uji ini dan layar awal tidak dibuka hook `beforeEach` suite; halaman dibuka oleh langkah spec karena kunjungan pertama adalah objek uji.
- Satu akun (A-AST-2) dipakai berurutan: TC-AC-ACC-39 menyelesaikan walkthrough lewat `[Done]` sehingga flag `guided_tooltip_seen_ac-client` menjadi true untuk TC-AC-ACC-871, 872, 873, dan 878 (dependensi TC-39).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.

## Test Steps

### TC-AC-ACC-39: Walkthrough halaman Client List muncul otomatis pada kunjungan pertama

1. Buka Admin Console > Client untuk pertama kali
2. Verifikasi walkthrough muncul otomatis dari Step 1 tanpa klik tombol apa pun
3. Verifikasi indikator `Step 1 of 4`
4. Verifikasi spotlight menyorot target Sub-tabs (`Active` / `Suspended` / `Archived`)
5. Verifikasi Title `Client Status Tabs`
6. Verifikasi Description `Browse clients by their status. The actions available change depending on the tab you are on.`
7. Verifikasi `[Skip]` dan `[Next]` tampil
8. Verifikasi `[Back]` Hidden
9. Klik `[Next]`
10. Verifikasi indikator `Step 2 of 4`
11. Verifikasi spotlight menyorot target Toolbar — Search & Filter Bar
12. Verifikasi Title `Search & Filter`
13. Verifikasi Description `Search and filter the client list to find specific clients.`
14. Verifikasi `[Skip]`, `[Back]`, dan `[Next]` tampil
15. Klik `[Next]`
16. Verifikasi indikator `Step 3 of 4`
17. Verifikasi spotlight menyorot target Table — Kolom Produk (FAMS / SAMS / SIEM)
18. Verifikasi Title `Subscription Status`
19. Verifikasi Description `Each product column shows the client's current subscription status for that product.`
20. Verifikasi `[Skip]`, `[Back]`, dan `[Next]` tampil
21. Klik `[Next]`
22. Verifikasi indikator `Step 4 of 4`
23. Verifikasi spotlight menyorot target Table — Kolom Row Action `[⋯]`
24. Verifikasi Title `Client Actions`
25. Verifikasi Description `Access the available actions for this client, depending on its current status and your role.`
26. Verifikasi `[Skip]`, `[Back]`, dan `[Done]` tampil
27. Verifikasi tombol utama berlabel `[Done]`, bukan `[Next]`
28. Klik `[Done]` pada Step 4
29. Verifikasi walkthrough tertutup

### TC-AC-ACC-871: Walkthrough tidak muncul otomatis pada kunjungan berikutnya

30. Buka Admin Console > Client lewat item `Client` pada sidebar
31. Muat ulang halaman (F5)
32. Lihat area halaman dan sisi kanan Breadcrumb
33. Verifikasi tidak ada overlay gelap setelah halaman dibuka maupun dimuat ulang
34. Verifikasi tidak ada tooltip box `Step 1 of 4` setelah halaman dibuka maupun dimuat ulang
35. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb

### TC-AC-ACC-872: Replay lewat tombol [?] mulai dari Step 1 tanpa mereset flag seen

36. Buka Admin Console > Client lewat item `Client` pada sidebar
37. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
38. Verifikasi tooltip `Show guide` tampil
39. Klik `[?]`
40. Verifikasi walkthrough dimulai dari Step 1 dengan indikator `Step 1 of 4`
41. Verifikasi Title `Client Status Tabs`
42. Ubah URL di address bar ke halaman Admin Console > Dashboard sebelum walkthrough selesai (tanpa mengklik area halaman)
43. Kembali ke Admin Console > Client lewat menu `Client` di Sidebar
44. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
45. Verifikasi walkthrough tidak muncul otomatis (flag seen tidak ter-reset oleh replay)

### TC-AC-ACC-873: Siklus navigasi: [Back] Hidden di Step 1, [Next] berubah menjadi [Done] di Step terakhir

46. Buka Admin Console > Client lewat item `Client` pada sidebar
47. Klik `[?]`
48. Lihat Step 1
49. Verifikasi indikator `Step 1 of 4`
50. Verifikasi `[Back]` Hidden
51. Verifikasi `[Skip]` dan `[Next]` tampil
52. Klik `[Next]`
53. Verifikasi indikator `Step 2 of 4` dengan Title `Search & Filter`
54. Verifikasi `[Back]` tampil
55. Klik `[Back]`
56. Verifikasi kembali ke `Step 1 of 4` dengan Title `Client Status Tabs`
57. Klik `[Next]` tiga kali berturut-turut sampai Step 4
58. Verifikasi indikator `Step 4 of 4`
59. Verifikasi tombol utama berlabel `[Done]` (bukan `[Next]`)
60. Klik `[Done]`
61. Verifikasi walkthrough tertutup

### TC-AC-ACC-878: Accessibility keyboard: Esc, Enter, panah kanan, dan panah kiri

62. Buka Admin Console > Client lewat item `Client` pada sidebar
63. Klik `[?]`
64. Verifikasi keyboard focus berada di tooltip box Step 1
65. Tekan tombol panah kanan
66. Verifikasi walkthrough pindah ke `Step 2 of 4`
67. Tekan tombol panah kiri
68. Verifikasi walkthrough kembali ke `Step 1 of 4`
69. Tekan Enter
70. Verifikasi walkthrough pindah ke `Step 2 of 4`
71. Tekan Esc
72. Verifikasi walkthrough tertutup (setara `[Skip]`)

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Urutan TC-AC-ACC-39, 871, 872, 873, 878 mengikuti dependensi TC (871, 872, 873, dan 878 bergantung pada 39). Satu spec mencakup lima TC pada satu akun karena kunjungan pertama membangun flag yang dipakai TC berikutnya (P-3: state dibangun berurutan, tidak dapat diulang tanpa biaya besar).
- Pembagian TC lintas spec: skenario Skip, klik overlay, berpindah halaman, dan resize (akun Guided Tooltip 2 sampai 4) ada di spec 021; walkthrough halaman Detail ada di spec 022 dan 023.
- Ukuran spec (72 langkah, melewati sekitar 35 langkah): semua blok satu kelas (Guided Tooltip List, satu akun), kegagalan blok kunjungan pertama menggagalkan blok sesudahnya sesuai dependensi TC (P-3), dan urutan mengikuti kolom Dependensi TC; langkah membengkak karena tiap klausa Expected Step 1 sampai Step 4 menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-39: Expected butir b sampai e menyebut "target" sebagai nama elemen (mis. "Sub-tabs (Active / Suspended / Archived)"); spec mengasersi spotlight menyorot elemen itu tanpa menebak selektor.
  - TC-AC-ACC-871 dan 872: langkah "Buka Admin Console > Client" sesudah TC-39 dibuka lewat item `Client` pada sidebar; TC tidak menyebut cara membuka halaman.
  - A-AST-2…A-AST-5: mekanisme reset flag `guided_tooltip_seen_*` per akun tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE (S-13).
