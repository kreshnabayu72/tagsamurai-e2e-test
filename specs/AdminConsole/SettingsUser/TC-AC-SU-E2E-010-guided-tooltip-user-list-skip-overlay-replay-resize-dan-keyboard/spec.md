---
id: TC-AC-SU-E2E-010-guided-tooltip-user-list-skip-overlay-replay-resize-dan-keyboard
title: "Guided Tooltip User List: Skip via Overlay, Replay lewat [?], Penutupan karena Resize atau Navigasi, dan Navigasi Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-33
  - TC-AC-SU-34
  - TC-AC-SU-35
  - TC-AC-SU-36
coverage:
  web: automated
---

# Guided Tooltip User List: Skip via Overlay, Replay lewat [?], Penutupan karena Resize atau Navigasi, dan Navigasi Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Pengecualian atas hook suite: spec ini menguji Guided Tooltip sehingga mengatur flag `guided_tooltip_seen_ac-settings-user` sendiri sesudah hook (flag disetel sesuai precondition tiap TC dan dipulihkan oleh hook `after` suite).
- Kemampuan teknis: Fixture BE untuk membaca dan menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` pada akun aktor; disediakan tim FE/BE (lihat `suite.md`).
- Viewport browser diubah pada TC-AC-SU-35 dan dipulihkan ke ukuran awal pada langkah akhir blok itu.
- Tidak ada data dinamis yang dibuat spec.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-33: Guided Tooltip Skip via klik overlay gelap

1. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
2. Muat ulang halaman Settings > User dengan F5
3. Klik area overlay gelap
4. Verifikasi walkthrough tertutup
5. Muat ulang halaman dengan F5
6. Verifikasi halaman Settings > User tampil dengan tabel User List
7. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-AC-SU-34: Guided Tooltip replay via tombol [?]

8. Setel flag Guided Tooltip `seen` (true) untuk akun aktor lewat Fixture BE
9. Muat ulang halaman Settings > User dengan F5
10. Klik tombol `[?]` di kanan Breadcrumb
11. Verifikasi walkthrough mulai dari Step 1 dengan Title `Group Sidebar`
12. Klik `[Skip]`
13. Verifikasi flag Guided Tooltip tetap `seen` (true) lewat Fixture BE

### TC-AC-SU-35: Guided Tooltip ditutup oleh resize atau navigasi keluar

14. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
15. Muat ulang halaman Settings > User dengan F5
16. Verifikasi walkthrough tampil di Step 1
17. Ubah ukuran viewport browser
18. Verifikasi walkthrough tertutup
19. Muat ulang halaman dengan F5
20. Verifikasi walkthrough muncul otomatis lagi dari Step 1
21. Klik item `Privacy Policy` pada sidebar grup Settings
22. Kembali ke Settings > User lewat sidebar
23. Verifikasi walkthrough muncul otomatis lagi dari Step 1
24. Klik `[Skip]` untuk menutup walkthrough, lalu pulihkan ukuran viewport awal

### TC-AC-SU-36: Accessibility Guided Tooltip, navigasi keyboard

25. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
26. Muat ulang halaman Settings > User dengan F5
27. Verifikasi tooltip box menerima keyboard focus
28. Tekan `Enter`
29. Verifikasi walkthrough pindah ke Step 2
30. Tekan `→`
31. Verifikasi walkthrough pindah ke Step 3
32. Tekan `←`
33. Verifikasi walkthrough kembali ke Step 2
34. Tekan `Esc`
35. Verifikasi walkthrough tertutup seperti Skip

## Notes

- Langkah penghubung (S-03): langkah 1 (precondition flag belum `seen`, diulang di awal tiap blok TC), langkah 24 (tutup walkthrough dan pulihkan viewport, S-09).
- Urutan langkah TC-AC-SU-35 mengikuti state (bagian 8b butir 5): walkthrough Step 1 diasersi sebelum resize.
- Temuan untuk QA:
  - TC-AC-SU-35 langkah 4 "klik sidebar menu lain" tidak menyebut menunya; spec memakai item `Privacy Policy` pada grup Settings (langkah 21).
  - TC-AC-SU-35 Post Condition "Flag seen tetap belum true" dan TC-AC-SU-33 serta TC-AC-SU-36 Post Condition "Flag seen = true" tidak punya langkah observasi di TC sehingga tidak diasersi (S-01). TC-AC-SU-34 butir b (flag tetap true) diasersi lewat Fixture BE yang dibaca (S-11).
  - TC-AC-SU-36 butir a "tooltip box menerima keyboard focus" tidak menyebut cara cek; spec mengasersi fokus keyboard pada tooltip box.
