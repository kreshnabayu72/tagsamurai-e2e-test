---
id: TC-GS-ACTLOG-E2E-006-guided-tooltip-flag-seen-replay-dan-keluar-tanpa-selesai
title: "Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-19
  - TC-GS-ACTLOG-20
  - TC-GS-ACTLOG-22
coverage:
  web: automated
---

# Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup: tidak ada selain akun aktor. Spec tidak membuat data dan tidak membutuhkan baris log tertentu.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md); spec ini mengatur flag sendiri sesudah hook suite, yaitu menyetel `guided_tooltip_seen_gs-activity-log` ke belum `true` untuk akun penguji sebelum langkah 1. Hook suite `after` memulihkan nilai awal.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client A (Sari Dewi) dan halaman `Global Settings > User` (flag `guided_tooltip_seen_gs-user` bernilai `true` sebelum langkah 7, supaya walkthrough halaman tujuan tidak muncul pada langkah 7 dan 24) (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): (1) menyetel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true` untuk akun penguji dan membacanya; spec memakainya sebelum langkah 1, sebagai langkah penghubung (langkah 17), dan untuk mengasersi nilai flag; tidak ada endpoint yang dikarang di spec ini. (2) Mengubah ukuran jendela browser (resize) dan memulihkannya.
- State global yang diubah: flag Guided Tooltip akun penguji (dipulihkan hook suite `after`) dan ukuran jendela browser (dipulihkan lewat langkah 29 dan hook `after`). Spec tidak mengubah format tanggal atau jam.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-19: Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelahnya

1. Buka Global Settings > Activity Log untuk pertama kali (flag belum `true`)
2. Verifikasi walkthrough muncul otomatis dari Step 1
3. Klik `[Next]`
4. Klik `[Done]`
5. Verifikasi walkthrough tertutup
6. Verifikasi flag `guided_tooltip_seen_gs-activity-log` bernilai `true`
7. Buka halaman lain: Global Settings > User
8. Buka Global Settings > Activity Log lagi
9. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-ACTLOG-20: Replay lewat tombol [?] tidak mereset flag

10. Klik tombol `[?]` di header halaman
11. Verifikasi walkthrough mulai dari Step 1
12. Klik `[Skip]`
13. Verifikasi walkthrough tertutup
14. Verifikasi flag `guided_tooltip_seen_gs-activity-log` tetap `true`
15. Refresh halaman (F5)
16. Verifikasi walkthrough tidak muncul otomatis setelah refresh

### TC-GS-ACTLOG-22: Keluar tanpa menyelesaikan (resize atau pindah halaman) tidak mengatur flag

17. Setel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true` tanpa memuat ulang halaman
18. Klik `[?]`
19. Verifikasi walkthrough tampil dengan Step 1
20. Ubah ukuran jendela browser
21. Verifikasi walkthrough tertutup setelah resize
22. Verifikasi flag `guided_tooltip_seen_gs-activity-log` belum bernilai `true` setelah resize
23. Klik `[?]` lagi
24. Klik menu halaman lain di sidebar: Global Settings > User
25. Verifikasi walkthrough tertutup setelah berpindah halaman
26. Verifikasi flag `guided_tooltip_seen_gs-activity-log` belum bernilai `true` setelah berpindah halaman
27. Kembali ke Global Settings > Activity Log
28. Verifikasi walkthrough muncul otomatis dari Step 1 pada kunjungan kembali
29. Pulihkan ukuran jendela browser ke ukuran awal

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-19, 20, 22). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-GS-ACTLOG-18, 21, dan 23 ada di spec `TC-GS-ACTLOG-E2E-005-guided-tooltip-isi-dan-navigasi`; TC-GS-ACTLOG-24 ada di spec `TC-GS-ACTLOG-E2E-007-mobile-card-session-card-user-action-guided-step-2-dan-download`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 (pindah ke halaman lain, langkah TC-19), 17 (menyetel ulang flag ke belum `true` karena TC-22 mensyaratkan flag belum `true` sedangkan TC-19 dan TC-20 telah menyetelnya ke `true`), 29 (memulihkan ukuran jendela). Halaman lain pada langkah 7 dan 24 adalah Global Settings > User; TC menyebut "halaman lain" dan "menu halaman lain di sidebar" tanpa menyebut nama.
- Walkthrough halaman tujuan `Global Settings > User` sengaja dimatikan lewat flag `gs-user` (Prerequisites) supaya langkah 9 dan 25 hanya mengamati walkthrough Activity Log.
- Langkah 19 adalah `Verifikasi` anchor (walkthrough tampil dengan Step 1) sebelum asersi tertutup di langkah 21; Expected TC-22 tidak memuatnya.
- Temuan untuk QA:
  - TC-19 dan TC-20 menyebut "buka halaman lain" dan "menu halaman lain di sidebar" tanpa menyebut halaman; spec memakai Global Settings > User (status menu `Master Reference` bertentangan antara PRD Brand dan `ui-design-system.md` §4).
  - TC-22 langkah 2 tidak menyebut ukuran jendela baru; spec mengubah ukuran jendela ke ukuran berbeda dari awal (nilai ditetapkan tim FE) dan memulihkannya.
  - TC-22 mensyaratkan flag belum `true` tetapi berdependensi pada TC-18 yang menyetel flag (via `[Done]`); spec menyetel ulang flag di langkah 17.
  - Cara membaca flag `guided_tooltip_seen_gs-activity-log` tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
