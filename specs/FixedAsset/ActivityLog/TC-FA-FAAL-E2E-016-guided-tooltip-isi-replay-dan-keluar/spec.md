---
id: TC-FA-FAAL-E2E-016-guided-tooltip-isi-replay-dan-keluar
title: "Guided Tooltip: Isi, Kunjungan Pertama, Replay, dan Keluar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-197
  - TC-FA-FAAL-198
  - TC-FA-FAAL-199
  - TC-FA-FAAL-201
coverage:
  web: automated
---

# Guided Tooltip: Isi, Kunjungan Pertama, Replay, dan Keluar

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-FAAL-197, 198, 201 | Total Control tanpa flag Guided Tooltip | #4 | `totalControlNewGuide_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TCNEWGUIDE_PASSWORD` |
  | TC-FA-FAAL-199 | Total Control (flag halaman ini sudah true) | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
- Login akun aktor pertama (Total Control tanpa flag, Pre-setup #4) di hook `before` spec ini. Pengecualian atas `suite.md`: spec Guided Tooltip dikecualikan dari hook suite flag dan precondition TC adalah Fixed Asset > Dashboard, sehingga hook `beforeEach` membuka Fixed Asset > Dashboard (bukan Activity Log) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Flag Guided Tooltip halaman Activity Log (`guided_tooltip_seen_fa-activity-log`): akun #4 direset ke belum diset oleh langkah penghubung di awal tiap blok TC (kemampuan reset flag disediakan tim FE/BE; mekanisme tidak tertulis di TC) dan dipulihkan ke belum diset di hook `after`. Akun #1 memakai flag true yang diatur hook suite untuk akun aktor default; spec ini tidak mengubahnya.
- Kemampuan teknis disediakan tim FE: pembacaan nilai flag `guided_tooltip_seen_fa-activity-log` untuk Expected TC-FA-FAAL-198 butir b, dan pengaturan ukuran viewport browser untuk TC-FA-FAAL-201 (tanpa endpoint karangan, S-13).
- Env var `FA_TCNEWGUIDE_PASSWORD` dan `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: spec tidak memakai baris log tertentu; tabel boleh berisi log apa pun.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas akun Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-197: Guided Tooltip isi tiga step

1. Reset flag Guided Tooltip halaman Activity Log akun #4 menjadi belum diset
2. Buka Reports & Logs > Activity Log pertama kali
3. Verifikasi step 1 target Table: Title `Activity Log`, Description `This page shows all activity across Fixed Asset — who did what and when. It's read-only and cannot be modified.`
4. Klik `[Next]`
5. Verifikasi step 2 target tombol Filter di toolbar: Title `Filter & Search`, Description `Use filters to narrow down the log. Available filters depend on which tab you're viewing.`
6. Klik `[Next]`
7. Verifikasi step 3 target tombol Download: Title `Download Log`, Description `Export the activity log. The export respects your current filters and search.`

### TC-FA-FAAL-198: Guided Tooltip muncul otomatis hanya pada kunjungan pertama

8. Reset flag Guided Tooltip halaman Activity Log akun #4 menjadi belum diset
9. Buka Activity Log pertama kali
10. Verifikasi kunjungan pertama: walkthrough muncul otomatis dari step 1
11. Klik `[Skip]`
12. Tutup halaman Activity Log dengan membuka Fixed Asset > Dashboard
13. Buka Activity Log lagi
14. Verifikasi kunjungan berikutnya: walkthrough tidak muncul otomatis
15. Verifikasi flag `guided_tooltip_seen_fa-activity-log` bernilai true

### TC-FA-FAAL-201: Guided Tooltip keluar tanpa menyelesaikan tidak menyetel flag

16. Reset flag Guided Tooltip halaman Activity Log akun #4 menjadi belum diset
17. Buka Activity Log pertama kali
18. Klik `[Next]` hingga step 2
19. Ubah ukuran viewport
20. Verifikasi setelah resize: walkthrough tertutup
21. Pulihkan ukuran viewport
22. Buka kembali Activity Log dengan klik menu `Activity Log` pada sidebar Reports & Logs
23. Verifikasi setelah resize: walkthrough muncul lagi otomatis pada kunjungan berikutnya
24. Klik `[Next]` hingga step 2
25. Klik menu lain di sidebar (Fixed Asset > Dashboard)
26. Verifikasi setelah navigasi keluar: walkthrough tertutup
27. Buka kembali Activity Log
28. Verifikasi setelah navigasi keluar: walkthrough muncul lagi pada kunjungan berikutnya

### TC-FA-FAAL-199: Tombol replay mengulang Guided Tooltip tanpa mereset flag

29. Ganti akun: Logout dari akun Total Control tanpa flag, lalu Login sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`) dan buka Fixed Asset > Reports & Logs > Activity Log
30. Arahkan kursor ke tombol `[?]` di kanan Breadcrumb
31. Verifikasi tooltip tombol `Show guide`
32. Klik tombol `[?]`
33. Verifikasi walkthrough mulai dari step 1
34. Klik `[Skip]`
35. Muat ulang halaman
36. Verifikasi setelah muat ulang: walkthrough tidak muncul otomatis (flag tidak direset)

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAL-200 dan 202 ada di spec 017.
- Urutan TC di dalam spec: TC-FA-FAAL-197, 198, 201, lalu 199. TC-FA-FAAL-199 memakai akun #1 (flag sudah true), sehingga ditaruh terakhir agar ganti akun (S-07) hanya terjadi sekali; tiga TC lain memakai akun #4 yang sama.
- Langkah penghubung (S-03): langkah 1, 8, dan 16 (reset flag akun #4 sebelum tiap TC, sesuai catatan Pre-setup TC bahwa flag #4 dipulihkan sebelum tiap TC yang memakainya), langkah 12 (menutup halaman, TC langkah 3 "Tutup halaman lalu buka Activity Log lagi"), langkah 18 dan 24 (menuju step 2 yang dibutuhkan TC langkah 1), langkah 21 (memulihkan viewport), langkah 22 dan 27 (membuka kembali Activity Log), langkah 25 (klik menu lain di sidebar, TC langkah 3), dan langkah 29 (ganti akun, lalu membuka Activity Log).
- Asersi state sementara (bagian 8b butir 5): walkthrough diasersi segera sesudah pemicunya (resize, navigasi) dan sebelum langkah berikutnya. Absence "walkthrough tidak muncul otomatis" (langkah 14 dan 36) memakai halaman Activity Log yang sudah termuat sebagai anchor permukaan (bagian 8b butir 2).
- Langkah 15: nilai flag dalam kurung pada Expected TC-FA-FAAL-198 butir b diasersi karena dapat gagal sendiri; pembacaan flag disediakan tim FE/BE.
- Ukuran spec 36 langkah, melewati sekitar 35 langkah: Expected TC-FA-FAAL-201 butir a dan b masing-masing punya dua klausa yang dipecah satu `Verifikasi` per klausa (S-01) dan reset flag eksplisit di awal tiap blok. Semua blok satu kelas (Guided Tooltip) dan berdiri sendiri lewat reset flag di awal blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; spec tidak dipecah.
- Temuan untuk QA:
  - TC-FA-FAAL-197, 198, 199, dan 201 tidak menyebut env var password dan cara mereset flag; nama env var diusulkan dari butir "Env var" di `suite.md` dan mekanisme reset disediakan tim FE/BE.
  - TC-FA-FAAL-201 langkah 1 menyebut "pada step 2 ubah ukuran viewport" tanpa menyebut ukuran awal dan ukuran baru; spec tidak menetapkan ukuran spesifik dan menyerahkannya ke tim FE.
  - TC-FA-FAAL-201 langkah 3 menyebut "klik menu lain di sidebar" tanpa menyebut menu; spec memakai Fixed Asset > Dashboard.
  - TC-FA-FAAL-198 langkah 3 ("Tutup halaman lalu buka Activity Log lagi") tidak menyebut cara menutup halaman; spec memakai navigasi ke Fixed Asset > Dashboard.
