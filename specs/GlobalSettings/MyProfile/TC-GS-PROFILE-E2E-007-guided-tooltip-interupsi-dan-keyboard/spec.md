---
id: TC-GS-PROFILE-E2E-007-guided-tooltip-interupsi-dan-keyboard
title: "Guided Tooltip: resize viewport, navigasi keluar, dan operasi keyboard"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-39
  - TC-GS-PROFILE-40
  - TC-GS-PROFILE-41
coverage:
  web: automated
---

# Guided Tooltip: resize viewport, navigasi keluar, dan operasi keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Pre-setup #20 Tono Prasetyo (`freshGuideProfile_automated_{namaCompany}@qwertysystem.net`), Total Control, flag `guided_tooltip_seen_gs-my-profile` belum ada sebelum tiap TC; password `Spectra.env.GS_PROFILE_FRESHGUIDE_PASSWORD`.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #20) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Pengecualian Hook suite 3: spec ini menguji flag `guided_tooltip_seen_gs-my-profile` sendiri. Hook `before` spec menyetel flag akun Pre-setup #20 menjadi true sesudah hook suite supaya pembukaan awal oleh `beforeEach` tidak memunculkan walkthrough; langkah 1, 10, dan 18 menghapus flag itu sebelum tiap TC. Hook `after` spec memulihkan flag ke keadaan awal (belum ada). Mekanisme menyetel dan menghapus flag disediakan tim FE/BE.
- Kemampuan teknis: mengubah ukuran viewport browser di tengah spec dan memulihkannya (langkah 4 dan 6).
- Data Dinamis: tidak ada.

## Test Steps

### Resize viewport menutup walkthrough tanpa menyimpan flag (TC-GS-PROFILE-39)

1. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
2. Buka My Profile dari account menu navbar
3. Klik [Next]
4. Ubah ukuran viewport browser menjadi lebih kecil dari ukuran awal
5. Verifikasi walkthrough tertutup setelah resize
6. Pulihkan ukuran viewport browser ke ukuran awal
7. Buka ulang My Profile dari account menu navbar
8. Verifikasi walkthrough muncul otomatis lagi dari Step 1 pada kunjungan berikutnya
9. Klik [Skip]

### Navigasi keluar menutup walkthrough tanpa menyimpan flag (TC-GS-PROFILE-40)

10. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
11. Buka My Profile dari account menu navbar
12. Klik [Next]
13. Klik logo atau menu navbar untuk pindah ke halaman lain
14. Verifikasi walkthrough tertutup saat pindah halaman
15. Buka ulang My Profile dari account menu navbar
16. Verifikasi walkthrough muncul otomatis lagi dari Step 1 pada kunjungan berikutnya
17. Klik [Skip]

### Operasi keyboard (TC-GS-PROFILE-41)

18. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
19. Buka My Profile dari account menu navbar
20. Tekan panah kanan
21. Verifikasi walkthrough berpindah ke Step 2
22. Tekan panah kiri
23. Verifikasi walkthrough kembali ke Step 1
24. Tekan Enter
25. Verifikasi walkthrough berpindah ke step berikutnya
26. Tekan Esc
27. Verifikasi walkthrough tertutup (setara Skip)

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-39, 40, 41).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1, 10, dan 18 menghapus flag (precondition TC); langkah 6 memulihkan viewport sebelum membuka ulang halaman, karena resize juga menutup walkthrough yang tampil (S-09); langkah 9 dan 17 menutup walkthrough yang tampil otomatis sebelum TC berikutnya mereset flag.
- Langkah 7 dan 15 membuka ulang My Profile; walkthrough yang muncul otomatis adalah objek `Verifikasi` langkah 8 dan 16.
- Temuan untuk QA:
  - TC-GS-PROFILE-39 menulis "Ubah ukuran viewport browser" tanpa ukuran target; spec memakai ukuran lebih kecil dari ukuran awal.
  - TC-GS-PROFILE-40 menulis "Klik logo/menu navbar untuk pindah ke halaman lain" tanpa menetapkan elemen dan halaman tujuan yang pasti; spec menulisnya apa adanya.
  - TC-GS-PROFILE-41 menulis "Enter ke step berikutnya" tanpa menyebut step tujuan yang diharapkan sesudah panah kiri kembali ke Step 1; spec mengasersi berpindah ke step berikutnya (Step 2).
