---
id: TC-FA-RP-E2E-236-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-2
title: "Guided Tooltip: langkah, kunjungan pertama, replay, Skip, Back, dan keyboard (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-768
  - TC-FA-RP-769
  - TC-FA-RP-770
  - TC-FA-RP-771
coverage:
  web: automated
---

# Guided Tooltip: langkah, kunjungan pertama, replay, Skip, Back, dan keyboard (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Pengecualian atas pernyataan flag Guided Tooltip di `suite.md`: spec ini menguji flag `guided_tooltip_seen_fa-settings-role-permission` sendiri. Hook suite menyetel flag `seen` sebelum spec; spec menghapus flag pada langkah yang menyatakannya untuk membentuk kunjungan pertama dan membaca flag pada langkah verifikasinya. Kemampuan menghapus dan membaca flag disediakan tim FE/BE; nilai awal flag dipulihkan hook suite `after`.
- Flag Guided Tooltip (selain pengecualian di atas), sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (kolam pengguna Standard) disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data selain flag.
- Kemampuan teknis: mengubah ukuran viewport browser (TC 770).

## Test Steps

### Skip lewat tombol dan lewat klik overlay (TC 768)

1. Hapus flag `guided_tooltip_seen_fa-settings-role-permission` akun aktor.
2. Buka menu Settings > Role & Permission.
3. Klik `[Skip]`.
4. Verifikasi walkthrough tertutup oleh `[Skip]`.
5. Buka halaman lain, lalu kembali ke Settings > Role & Permission.
6. Verifikasi Tab Bar halaman Role & Permission tampil.
7. Verifikasi walkthrough tidak muncul pada kunjungan berikutnya.
8. Hapus flag `guided_tooltip_seen_fa-settings-role-permission` akun aktor.
9. Buka menu Settings > Role & Permission.
10. Klik pada area overlay gelap.
11. Verifikasi walkthrough tertutup.
12. Verifikasi flag seen tersimpan.

### Back kembali ke step sebelumnya (TC 769)

13. Klik tombol `[?]`.
14. Verifikasi Step 1 tidak menampilkan `[Back]`.
15. Klik `[Next]` dua kali.
16. Klik `[Back]`.
17. Verifikasi tampil Step 2 dengan Title `Approval Rules per Group`.
18. Klik `[Skip]`.

### Resize atau navigasi di tengah walkthrough tidak menyimpan flag seen (TC 770)

19. Hapus flag `guided_tooltip_seen_fa-settings-role-permission` akun aktor.
20. Buka menu Settings > Role & Permission.
21. Ubah ukuran viewport browser saat walkthrough tampil.
22. Verifikasi walkthrough tertutup saat viewport diubah.
23. Pulihkan ukuran viewport browser.
24. Buka halaman lain, lalu kembali ke Settings > Role & Permission.
25. Verifikasi walkthrough muncul otomatis lagi dari Step 1.
26. Klik `[Skip]`.

### Aksesibilitas keyboard (TC 771)

27. Klik tombol `[?]`.
28. Verifikasi tooltip box mendapat fokus keyboard.
29. Tekan Enter.
30. Verifikasi Enter memajukan ke Step 2.
31. Tekan panah kiri.
32. Verifikasi panah kiri kembali ke Step 1.
33. Tekan Esc.
34. Verifikasi Esc menutup walkthrough (Skip).
35. Verifikasi flag seen tersimpan.

## Notes

- Langkah penghubung (S-03): langkah 1, 8, dan 19 (membentuk keadaan flag belum ada, sesuai Precondition TC), 18 dan 26 (menutup walkthrough tanpa asersi), serta 23 (memulihkan viewport). Langkah 6 menjadi anchor positif bagi asersi absence walkthrough (bagian 8b butir 2 dan 11).
- Precondition TC 769 dan 771 "flag seen sudah tersimpan" dipenuhi oleh flag yang tersimpan pada langkah 3 sampai 12 dan oleh hook suite.
- Halaman Role & Permission yang membuka walkthrough dibuka ulang lewat menu sidebar pada langkah 2, 9, dan 20, bukan oleh hook `beforeEach`, sebab hook itu membuka halaman saat flag sudah `seen`.
- Temuan untuk QA:
  - TC 768 butir b menyebut "diulang dengan akun lain" tanpa menyebut akunnya; spec memakai akun yang sama dengan flag dihapus ulang (langkah 8) dan tidak membuat akun karangan (S-13).
  - TC 768 sampai 771 tidak menyebut cara memeriksa flag seen; spec memakai kemampuan baca flag yang disediakan tim FE/BE (S-11) pada langkah 12 dan 35.
  - TC 771 butir d ("menyimpan flag seen") berprecondition flag sudah tersimpan, sehingga penyimpanan tidak dapat dibedakan dari keadaan awal; spec mengasersi flag seen tersimpan sesuai Expected.
  - TC 770 menyebut "buka halaman lain" tanpa menyebut halaman; spec mengikuti TC.
