---
id: TC-GS-NLU-E2E-007-guided-tooltip-flag-sudah-dilihat-replay-dan-dismiss-lewat
title: "Guided Tooltip: flag sudah dilihat, replay, dan dismiss lewat navigasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-23
  - TC-GS-NLU-26
  - TC-GS-NLU-27
coverage:
  web: automated
---

# Guided Tooltip: flag sudah dilihat, replay, dan dismiss lewat navigasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: akun First Visit (Total Control tanpa flag Guided Tooltip untuk halaman ini). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password `Spectra.env.GS_FIRSTVISIT_TC_PASSWORD` (nama baru, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan tim FE). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Pengecualian hook suite (Guided Tooltip): spec ini menguji flag `guided_tooltip_seen_gs-non-login-user` sendiri. Akun First Visit dikecualikan dari penyetelan flag true oleh hook suite `before`. Spec mengatur flag untuk akun First Visit: keadaan "belum ada" dicapai lewat langkah penghubung "Hapus flag"; keadaan "sudah ada" dicapai oleh aksi `[Skip]` atau `[Done]` pada spec ini. Hook `after` spec memulihkan flag akun First Visit ke nilai awal.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak tertulis di TC, PRD, atau LLD sehingga tidak dikarang, S-13): menghapus flag, memulihkan nilai awal flag, dan membaca flag untuk satu akun.
- Data Pre-setup No. 9 sampai 12 hanya dibaca. Spec tidak membuat data dan tidak mengubah state global selain flag akun First Visit.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-23: Guided Tooltip Skip menutup walkthrough dan menandai sudah dilihat

1. Hapus flag `guided_tooltip_seen_gs-non-login-user` untuk akun First Visit
2. Buka sub-tab Non-Login User (muat ulang halaman), tunggu Step 1 tampil
3. Klik `[Skip]`
4. Verifikasi walkthrough tertutup
5. Muat ulang halaman
6. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-NLU-26: Guided Tooltip replay lewat tombol bantuan tidak mereset flag sudah dilihat

7. Hover tombol `[?]` di sebelah kanan Breadcrumb
8. Verifikasi Tooltip tombol `Show guide`
9. Klik tombol `[?]`
10. Verifikasi walkthrough dimulai dari Step 1
11. Klik `[Skip]`
12. Muat ulang halaman untuk mengamati kunjungan berikutnya
13. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-NLU-27: Guided Tooltip ditutup tanpa menandai sudah dilihat saat navigasi keluar di tengah jalan

14. Hapus flag `guided_tooltip_seen_gs-non-login-user` untuk akun First Visit
15. Buka sub-tab Non-Login User (muat ulang halaman), Step 1 tampil
16. Klik sub-tab `Login User` tanpa menyelesaikan walkthrough
17. Verifikasi walkthrough tertutup saat berpindah sub-tab
18. Klik sub-tab `Non-Login User`
19. Verifikasi walkthrough muncul lagi otomatis dari Step 1

## Notes

- Langkah penghubung (S-03): langkah 1, 12, 14 (mengembalikan flag ke keadaan belum ada, dan muat ulang untuk mengamati kunjungan berikutnya).
- TC-GS-NLU-26 mensyaratkan flag sudah ada; keadaan itu dicapai oleh `[Skip]` pada TC-GS-NLU-23 di spec ini (urutan 23 lalu 26), tanpa menyetel flag lewat kemampuan teknis.
- Temuan untuk QA:
  - Email akun First Visit tidak tertulis di Tabel Pre-setup TC (precondition hanya "Login sbg Role: Total Control"). Akun dan env var diusulkan penulis dan disediakan tim FE.
  - TC-GS-NLU-26 Expected c ("kunjungan berikutnya tetap tidak memunculkan walkthrough otomatis") tidak memberi langkah kunjungan; spec menambah muat ulang halaman sebagai langkah penghubung untuk mengamatinya.
  - TC-GS-NLU-23 Expected a ("Walkthrough tertutup") diasersi sebelum muat ulang (urutan state).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
