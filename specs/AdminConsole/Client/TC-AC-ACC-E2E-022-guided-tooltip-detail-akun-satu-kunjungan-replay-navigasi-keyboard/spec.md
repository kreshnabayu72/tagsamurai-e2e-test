---
id: TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard
title: "Guided Tooltip Halaman Client Detail: Kunjungan Pertama, Berikutnya, Replay, Navigasi, dan Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-879
  - TC-AC-ACC-880
  - TC-AC-ACC-881
  - TC-AC-ACC-882
  - TC-AC-ACC-887
coverage:
  web: automated
---

# Guided Tooltip Halaman Client Detail: Kunjungan Pertama, Berikutnya, Replay, Navigasi, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-AST-2 | Total Control (Principal, akun Guided Tooltip 1) | `guidedTooltipSatu_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GT1_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-AST-2); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client-detail` untuk akun uji dalam spec ini (tabel akun) belum ada sebelum spec dimulai atau sesuai precondition tiap TC; reset flag per akun oleh hook `before` spec ini dan pemulihan ke keadaan awal oleh hook `after` memakai kemampuan reset flag yang disediakan tim FE (TC menyebut "dipulihkan lewat akun uji atau reset data").
- Pengecualian atas flag hook suite (bagian 4 konvensi): spec ini menguji flag itu sendiri, sehingga hook `before` suite tidak menyetel flag untuk akun uji ini dan layar awal tidak dibuka hook `beforeEach` suite; halaman dibuka oleh langkah spec karena kunjungan pertama adalah objek uji.
- Satu akun (A-AST-2) dipakai berurutan: TC-AC-ACC-879 menyelesaikan walkthrough lewat `[Done]` sehingga flag `guided_tooltip_seen_ac-client-detail` menjadi true untuk TC-AC-ACC-880, 881, 882, dan 887 (dependensi TC-879).
- ID Client `PT Sejahtera Abadi` (C-01) untuk URL Detail (UUID opaque) diambil dari keluaran skrip seed atau respons API; kemampuan itu disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.

## Test Steps

### TC-AC-ACC-879: Walkthrough halaman Client Detail muncul otomatis pada kunjungan pertama

1. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung untuk pertama kali
2. Verifikasi walkthrough muncul otomatis dari Step 1 tanpa klik tombol apa pun
3. Verifikasi indikator `Step 1 of 4`
4. Verifikasi spotlight menyorot target Section Company Information (header)
5. Verifikasi Title `Company Information`
6. Verifikasi Description `View and edit this client's company details, PIC contact, and registration status.`
7. Verifikasi `[Skip]` dan `[Next]` tampil
8. Verifikasi `[Back]` Hidden
9. Klik `[Next]`
10. Verifikasi indikator `Step 2 of 4`
11. Verifikasi spotlight menyorot target Tab Subscription
12. Verifikasi Title `Subscription`
13. Verifikasi Description `See this client's product subscriptions and their current status. Subscriptions are managed from Client Subscription.`
14. Verifikasi `[Skip]`, `[Back]`, dan `[Next]` tampil
15. Klik `[Next]`
16. Verifikasi indikator `Step 3 of 4`
17. Verifikasi spotlight menyorot target area konten Tab Subscription (Tab Subscription — content area)
18. Verifikasi Title `License Quota`
19. Verifikasi Description `Shows how much of each licensed quota is allocated and used.`
20. Verifikasi `[Skip]`, `[Back]`, dan `[Next]` tampil
21. Klik `[Next]`
22. Verifikasi indikator `Step 4 of 4`
23. Verifikasi spotlight menyorot target navigasi tab (Tab navigation)
24. Verifikasi Title `Detail Tabs`
25. Verifikasi Description `Switch between the areas of this client's licensing and devices.`
26. Verifikasi `[Skip]`, `[Back]`, dan `[Done]` tampil
27. Verifikasi tombol utama berlabel `[Done]`, bukan `[Next]`
28. Klik `[Done]` pada Step 4
29. Verifikasi walkthrough tertutup

### TC-AC-ACC-880: Walkthrough tidak muncul otomatis pada kunjungan berikutnya

30. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
31. Muat ulang halaman (F5)
32. Lihat area halaman dan sisi kanan Breadcrumb
33. Verifikasi tidak ada overlay gelap setelah halaman dibuka maupun dimuat ulang
34. Verifikasi tidak ada tooltip box `Step 1 of 4` setelah halaman dibuka maupun dimuat ulang
35. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb

### TC-AC-ACC-881: Replay lewat tombol [?] mulai dari Step 1 tanpa mereset flag seen

36. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
37. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
38. Verifikasi tooltip `Show guide` tampil
39. Klik `[?]`
40. Verifikasi walkthrough dimulai dari Step 1 dengan indikator `Step 1 of 4`
41. Verifikasi Title `Company Information`
42. Ubah URL di address bar ke halaman Admin Console > Dashboard sebelum walkthrough selesai (tanpa mengklik area halaman)
43. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
44. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
45. Verifikasi walkthrough tidak muncul otomatis (flag seen tidak ter-reset oleh replay)

### TC-AC-ACC-882: Siklus navigasi: [Back] Hidden di Step 1, [Next] berubah menjadi [Done] di Step terakhir

46. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
47. Klik `[?]`
48. Lihat Step 1
49. Verifikasi indikator `Step 1 of 4`
50. Verifikasi `[Back]` Hidden
51. Verifikasi `[Skip]` dan `[Next]` tampil
52. Klik `[Next]`
53. Verifikasi indikator `Step 2 of 4` dengan Title `Subscription`
54. Verifikasi `[Back]` tampil
55. Klik `[Back]`
56. Verifikasi kembali ke `Step 1 of 4` dengan Title `Company Information`
57. Klik `[Next]` tiga kali berturut-turut sampai Step 4
58. Verifikasi indikator `Step 4 of 4`
59. Verifikasi tombol utama berlabel `[Done]` (bukan `[Next]`)
60. Klik `[Done]`
61. Verifikasi walkthrough tertutup

### TC-AC-ACC-887: Accessibility keyboard: Esc, Enter, panah kanan, dan panah kiri

62. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
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
- Urutan TC-AC-ACC-879, 880, 881, 882, 887 mengikuti dependensi TC (880, 881, 882, dan 887 bergantung pada 879); satu spec pada satu akun karena kunjungan pertama membangun flag yang dipakai TC berikutnya (P-3).
- Pembagian TC lintas spec: Guided Tooltip halaman List ada di spec 020 dan 021; skenario Skip, klik overlay, berpindah halaman, dan resize halaman Detail ada di spec 023.
- Ukuran spec (72 langkah, melewati sekitar 35 langkah): semua blok satu kelas (Guided Tooltip Detail, satu akun), kegagalan blok kunjungan pertama menggagalkan blok sesudahnya sesuai dependensi TC (P-3), dan urutan mengikuti kolom Dependensi TC; langkah membengkak karena tiap klausa Expected Step 1 sampai Step 4 menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-879 Expected butir d menyebut target "Tab Subscription — content area" dan butir e "Tab navigation" sebagai nama elemen; spec tidak menebak selektor.
  - TC-AC-ACC-879 sampai 887: URL Detail dibuka dengan ID yang diambil dari seed; mekanisme itu disediakan tim FE/BE.
