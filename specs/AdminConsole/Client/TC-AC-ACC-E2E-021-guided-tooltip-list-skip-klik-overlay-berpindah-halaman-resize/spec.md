---
id: TC-AC-ACC-E2E-021-guided-tooltip-list-skip-klik-overlay-berpindah-halaman-resize
title: "Guided Tooltip Halaman Client List: Skip, Klik Overlay, Berpindah Halaman, dan Resize Viewport"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-874
  - TC-AC-ACC-875
  - TC-AC-ACC-876
  - TC-AC-ACC-877
coverage:
  web: automated
---

# Guided Tooltip Halaman Client List: Skip, Klik Overlay, Berpindah Halaman, dan Resize Viewport

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-AST-3 | Total Control (Principal, akun Guided Tooltip 2) | `guidedTooltipDua_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GT2_PASSWORD` |
| A-AST-4 | Total Control (Principal, akun Guided Tooltip 3) | `guidedTooltipTiga_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GT3_PASSWORD` |
| A-AST-5 | Total Control (Principal, akun Guided Tooltip 4) | `guidedTooltipEmpat_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GT4_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-AST-3); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` untuk akun uji dalam spec ini (tabel akun) belum ada sebelum spec dimulai atau sesuai precondition tiap TC; reset flag per akun oleh hook `before` spec ini dan pemulihan ke keadaan awal oleh hook `after` memakai kemampuan reset flag yang disediakan tim FE (TC menyebut "dipulihkan lewat akun uji atau reset data").
- Pengecualian atas flag hook suite (bagian 4 konvensi): spec ini menguji flag itu sendiri, sehingga hook `before` suite tidak menyetel flag untuk akun uji ini dan layar awal tidak dibuka hook `beforeEach` suite; halaman dibuka oleh langkah spec karena kunjungan pertama adalah objek uji.
- Tiap akun hanya dipakai untuk TC-nya (A-AST-3 untuk `[Skip]`, A-AST-4 untuk klik overlay, A-AST-5 untuk berpindah halaman dan resize yang tidak menandai sudah dilihat). Ganti akun memakai langkah Logout dan Login eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Kemampuan teknis: mengubah ukuran viewport browser saat Step 1 tampil dan memulihkannya (TC-AC-ACC-877); mengubah URL di address bar.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.

## Test Steps

### TC-AC-ACC-874: [Skip] menutup walkthrough dan menandai sudah dilihat

1. Buka Admin Console > Client untuk pertama kali
2. Klik `[Skip]` pada Step 1
3. Verifikasi walkthrough tertutup pada Step 1
4. Muat ulang halaman
5. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
6. Verifikasi walkthrough tidak muncul otomatis setelah halaman dimuat ulang
7. Logout dari akun Guided Tooltip 2
8. Login sebagai Total Control akun Guided Tooltip 3 (A-AST-4)

### TC-AC-ACC-875: Klik overlay gelap menutup walkthrough dan menandai sudah dilihat

9. Buka Admin Console > Client untuk pertama kali
10. Klik area overlay gelap di luar spotlight dan tooltip box pada Step 1
11. Verifikasi walkthrough tertutup pada Step 1
12. Muat ulang halaman
13. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
14. Verifikasi walkthrough tidak muncul otomatis setelah halaman dimuat ulang
15. Logout dari akun Guided Tooltip 3
16. Login sebagai Total Control akun Guided Tooltip 4 (A-AST-5)

### TC-AC-ACC-876: Berpindah halaman di tengah walkthrough menutup walkthrough tanpa menandai sudah dilihat

17. Buka Admin Console > Client untuk pertama kali
18. Klik `[Next]` sekali sampai Step 2
19. Ubah URL di address bar ke halaman Admin Console > Dashboard (tanpa mengklik area halaman)
20. Verifikasi walkthrough tertutup saat berpindah halaman
21. Kembali ke Admin Console > Client lewat menu `Client` di Sidebar
22. Verifikasi walkthrough muncul otomatis lagi mulai dari Step 1 dengan indikator `Step 1 of 4`

### TC-AC-ACC-877: Resize viewport di tengah walkthrough menutup walkthrough tanpa menandai sudah dilihat

23. Ubah URL di address bar ke halaman Admin Console > Dashboard
24. Buka Admin Console > Client lewat menu `Client` di Sidebar (kunjungan pertama menurut precondition TC: flag belum ada)
25. Ubah ukuran viewport browser saat Step 1 tampil
26. Verifikasi walkthrough tertutup saat viewport diubah ukurannya
27. Muat ulang halaman
28. Verifikasi walkthrough muncul otomatis lagi mulai dari Step 1 dengan indikator `Step 1 of 4`
29. Pulihkan ukuran viewport browser

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 23, 29. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: kunjungan pertama, kunjungan berikutnya, replay, navigasi, dan keyboard (akun Guided Tooltip 1) ada di spec 020.
- Langkah 7–8 dan 15–16 (Logout dan Login ganti akun) adalah langkah ganti akun eksplisit (S-07); login akun pertama (A-AST-3) dilakukan hook `before`.
- Pada TC-AC-ACC-877 langkah 1 TC ("Buka Admin Console > Client untuk pertama kali") dipenuhi dengan keluar dari halaman lalu membuka halaman lagi, karena flag akun A-AST-5 masih belum ada setelah TC-AC-ACC-876 (TC-876 tidak menandai sudah dilihat).
- Temuan untuk QA:
  - TC-AC-ACC-876 dan 877 memakai akun yang sama (A-AST-5) dan sama-sama mensyaratkan flag belum ada; TC-877 tidak menyebut kunjungan ulang setelah TC-876; spec membuka halaman kembali lewat sidebar.
  - TC-AC-ACC-877: Expected "viewport diubah ukurannya" tidak menyebut ukuran viewport baru; spec tidak menebak nilai ukuran dan menyerahkannya ke skrip.
