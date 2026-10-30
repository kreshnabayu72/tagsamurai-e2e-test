---
id: TC-GS-ROLE-E2E-011-guided-tooltip-skip-back-replay-exit-dan-keyboard
title: "Guided Tooltip Role & Permission: Skip, Back, Replay, Navigasi Keluar, dan Keyboard"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-29
  - TC-GS-ROLE-30
  - TC-GS-ROLE-31
coverage:
  web: automated
---

# Guided Tooltip Role & Permission: Skip, Back, Replay, Navigasi Keluar, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Ahmad Fauzi) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Data: memakai data Pre-setup (Pre-setup #1); spec tidak membuat, mengubah, atau menghapus data.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-role`, sehingga flag dihapus ("belum diset") lewat API sebelum tiap TC (langkah reset eksplisit) dan menjadi pengecualian atas pernyataan hook suite di `suite.md`. TC-GS-ROLE-30 berpindah ke halaman User; flag Guided Tooltip halaman User disetel true oleh hook `before` spec supaya walkthrough halaman itu tidak muncul (kunci flag halaman User disediakan tim FE/BE). Hook `before` spec mencatat nilai awal kedua flag sesudah hook suite; hook `after` memulihkan nilai awal walau spec gagal di tengah.
- Kemampuan teknis: menghapus dan menyetel nilai flag Guided Tooltip akun aktor lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); muat ulang halaman (F5); mengirim keystroke Enter, `←`, dan Esc ke halaman.
- State global yang diubah: flag Guided Tooltip halaman Role & Permission dan halaman User (dipulihkan seperti di atas).

## Test Steps

### TC-GS-ROLE-29: Skip, Back, dan replay lewat [?]

1. Hapus flag `guided_tooltip_seen_gs-role` lewat API sehingga flag belum diset
2. Muat ulang Global Settings > Role & Permission untuk kunjungan pertama
3. Klik `[Next]` ke Step 2
4. Klik `[Back]`
5. Verifikasi `[Back]` kembali ke Step 1
6. Klik `[Skip]`
7. Verifikasi `[Skip]` menutup walkthrough
8. Muat ulang halaman (F5)
9. Verifikasi walkthrough tidak muncul otomatis
10. Klik trigger `[?]` di header halaman
11. Verifikasi `[?]` memulai walkthrough dari Step 1

### TC-GS-ROLE-30: Walkthrough ditutup tanpa selesai saat navigasi keluar

12. Hapus flag `guided_tooltip_seen_gs-role` lewat API sehingga flag belum diset
13. Muat ulang Global Settings > Role & Permission untuk kunjungan pertama
14. Klik `[Next]` ke Step 2
15. Klik menu sidebar User saat Step 2 tampil
16. Verifikasi halaman User tampil
17. Verifikasi walkthrough tertutup saat navigasi keluar
18. Klik menu sidebar Role & Permission untuk kembali
19. Verifikasi walkthrough muncul otomatis lagi dari Step 1

### TC-GS-ROLE-31: Walkthrough dikendalikan dengan keyboard

20. Hapus flag `guided_tooltip_seen_gs-role` lewat API sehingga flag belum diset
21. Muat ulang Global Settings > Role & Permission untuk kunjungan pertama
22. Tekan Enter
23. Verifikasi Enter berpindah ke Step 2
24. Tekan `←`
25. Verifikasi `←` kembali ke Step 1
26. Tekan Esc
27. Verifikasi Esc menutup walkthrough (setara Skip)

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 12, dan 20 (hapus flag lewat API untuk memenuhi precondition "flag belum diset"), serta langkah 2, 13, dan 21 (muat ulang agar kunjungan pertama berikutnya terpenuhi).
- Langkah 16 (halaman User tampil) menjadi anchor positif bahwa navigasi keluar selesai sebelum asersi walkthrough tidak tampil pada langkah 17.
- Langkah 3 dan 14 (`[Next]` ke Step 2) tidak punya `Verifikasi` karena Expected TC tidak memuat isi Step 2; hanya Step 2 yang dipakai sebagai precondition.
- Pindah antar blok dilakukan lewat reset flag dan muat ulang; walkthrough yang masih terbuka dari blok sebelumnya (langkah 11) ditutup oleh muat ulang pada langkah 13.
- Temuan untuk QA:
  - TC-GS-ROLE-26 sampai TC-GS-ROLE-31 menyebut flag `gs-role-permission` atau "flag guided tooltip", sedangkan `suite.md` memakai `guided_tooltip_seen_gs-role`; spec memakai nama dari `suite.md`.
  - TC-GS-ROLE-30 berpindah ke halaman User yang punya walkthrough sendiri; TC tidak menyatakan flag halaman User, sehingga spec menyetelnya true dan kunci flag disediakan tim FE/BE.
  - TC-GS-ROLE-29 Expected d tidak menyatakan apakah `[?]` menyimpan atau tidak menyimpan flag; tidak diasersi.
