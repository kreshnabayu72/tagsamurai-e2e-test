---
id: TC-FA-RP-E2E-235-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-1
title: "Guided Tooltip: langkah, kunjungan pertama, replay, Skip, Back, dan keyboard (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-765
  - TC-FA-RP-766
  - TC-FA-RP-767
coverage:
  web: automated
---

# Guided Tooltip: langkah, kunjungan pertama, replay, Skip, Back, dan keyboard (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Pengecualian atas pernyataan flag Guided Tooltip di `suite.md`: spec ini menguji flag `guided_tooltip_seen_fa-settings-role-permission` sendiri. Hook suite menyetel flag `seen` sebelum spec; spec menghapus flag pada langkah yang menyatakannya untuk membentuk kunjungan pertama dan membaca flag pada langkah verifikasinya. Kemampuan menghapus dan membaca flag disediakan tim FE/BE; nilai awal flag dipulihkan hook suite `after`.
- Flag Guided Tooltip (selain pengecualian di atas), sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (kolam pengguna Standard) disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data selain flag.

## Test Steps

### Konten tiga step (TC 765)

1. Hapus flag `guided_tooltip_seen_fa-settings-role-permission` akun aktor.
2. Buka menu Settings > Role & Permission (kunjungan pertama).
3. Verifikasi Step 1 of 3 menyorot Tab Bar (spotlight menyorot elemen target).
4. Verifikasi Title `Manage Access` dan Description `Each tab manages a different part of access control. Pick a tab to see and change who can do what.`
5. Verifikasi tombol `[Back]` Hidden pada Step 1.
6. Klik `[Next]`.
7. Verifikasi Step 2 of 3 menyorot header Tab Transaction Role tanpa berpindah tab.
8. Verifikasi Title `Approval Rules per Group` dan Description `Set the approval rule and assign roles per group for each transaction type.`
9. Klik `[Next]`.
10. Verifikasi Step 3 of 3 menyorot header Tab System tanpa berpindah tab.
11. Verifikasi Title `System Capabilities` dan Description `Manage the detailed permission matrix for a specific capability.` (tanpa penjelasan menu kolom Actions).
12. Verifikasi tombol `[Next]` berubah menjadi `[Done]`.
13. Verifikasi tidak ada Step 4 dan tidak ada step yang menyorot header kolom Actions.
14. Klik `[Done]`.
15. Verifikasi `[Done]` pada Step 3 menutup walkthrough.

### Kunjungan pertama dan tidak muncul lagi setelah selesai (TC 766)

16. Hapus flag `guided_tooltip_seen_fa-settings-role-permission` akun aktor.
17. Buka menu Settings > Role & Permission (kunjungan pertama).
18. Verifikasi walkthrough muncul otomatis dari Step 1 dan dimulai di tab yang sedang aktif.
19. Klik `[Next]` dua kali, lalu klik `[Done]`.
20. Verifikasi walkthrough tertutup.
21. Verifikasi flag `seen` tersimpan.
22. Buka halaman lain, lalu kembali ke Settings > Role & Permission.
23. Verifikasi Tab Bar halaman Role & Permission tampil.
24. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya.

### Replay lewat tombol `[?]` tanpa mereset flag seen (TC 767)

25. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb.
26. Verifikasi tooltip tombol `Show guide`.
27. Klik tombol `[?]`.
28. Verifikasi walkthrough mulai dari Step 1.
29. Klik `[Skip]`.
30. Verifikasi Skip menutup walkthrough.
31. Muat ulang halaman (F5).
32. Verifikasi Tab Bar halaman Role & Permission tampil.
33. Verifikasi walkthrough tidak muncul otomatis: flag seen tidak di-reset oleh replay.

## Notes

- Langkah penghubung (S-03): langkah 1 dan 16 (membentuk keadaan flag belum ada, sesuai Precondition TC 765, 766), 14 dan 19 (menyelesaikan walkthrough sesuai TC), serta 22 (kunjungan lagi sesuai TC). Langkah 23 dan 32 menjadi anchor positif bagi asersi absence walkthrough (bagian 8b butir 2 dan 11).
- Precondition TC 767 "flag seen sudah tersimpan" dipenuhi oleh flag yang tersimpan pada TC 766 (langkah 19 sampai 21) dan oleh hook suite; langkah halaman Role & Permission dibuka dari `beforeEach` suite.
- Halaman Role & Permission yang membuka walkthrough dibuka ulang oleh langkah 2 dan 17 (menu sidebar), bukan oleh hook `beforeEach`, sebab hook itu membuka halaman saat flag sudah `seen`.
- Copy bertanda `copy usulan, PRD 12 #1` (Description Step 3 Guided Tooltip) diasersi literal sesuai TC; asersi itu bergantung pada persetujuan PM atas copy tersebut.
- Temuan untuk QA:
  - TC 766 butir b ("flag seen tersimpan") tidak menyebut cara memeriksa flag; spec memakai kemampuan baca flag yang disediakan tim FE/BE (S-11).
  - TC 765 sampai 767 mencantumkan #15 pada Precondition tanpa menyebut data yang dipakai; spec tidak memakai data #15 pada langkah.
  - TC 766 menyebut "buka halaman lain" tanpa menyebut halaman; spec mengikuti TC.
