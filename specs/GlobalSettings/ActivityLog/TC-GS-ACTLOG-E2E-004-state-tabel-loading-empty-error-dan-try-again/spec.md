---
id: TC-GS-ACTLOG-E2E-004-state-tabel-loading-empty-error-dan-try-again
title: "State Tabel: Loading, Empty, Error, dan Try Again"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-04
  - TC-GS-ACTLOG-05
  - TC-GS-ACTLOG-08
  - TC-GS-ACTLOG-09
coverage:
  web: automated
---

# State Tabel: Loading, Empty, Error, dan Try Again

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor yang dimodelkan lewat payload izin mock: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`. Tidak ada login nyata dan tidak ada password yang dipakai. Seluruh mock dipasang di hook `before`.
- Endpoint yang dipanggil halaman pada kondisi tes (rujukan `global-settings/activity-log/API/openapi.yaml`) dan jawaban mock:
  - `POST /v2/analytics-reporting/session-logs/list` dan `POST /v2/analytics-reporting/change-logs/list`: jawaban normal berisi minimal 10 baris sehingga tabel dan pagination ter-render (`Fixture.activityLog.mockListSession` dan `Fixture.activityLog.mockListUserAction`; fixture baru, isi respons ditetapkan tim FE: minimal 10 baris, entitas aktif); TC-GS-ACTLOG-04 jawaban ditahan (loading lambat) lalu dilepas dan dijawab normal; TC-GS-ACTLOG-05 jawaban 0 baris untuk entitas aktif; TC-GS-ACTLOG-08 jawaban 5xx; TC-GS-ACTLOG-09 jawaban 5xx pada permintaan pertama tiap tab, lalu normal pada permintaan berikutnya.
  - `GET /v2/analytics-reporting/session-logs/stream` dan `GET /v2/analytics-reporting/change-logs/stream` (SSE `session_logs.created` dan `change_logs.created`): koneksi dijawab terbuka tanpa event pada seluruh TC supaya halaman tidak memuat ulang sendiri.
  - Endpoint `session-logs/options`, `change-logs/options`, `session-logs/export`, dan `change-logs/export` tidak dipanggil pada kondisi tes spec ini (Filter Panel dan Download tidak dibuka).
- API pendukung di luar sumber modul disediakan tim FE: identitas pengguna dan payload izin Total Control (akses Global Settings > Activity Log), menu, dan flag Guided Tooltip `guided_tooltip_seen_gs-activity-log` yang dijawab seen agar walkthrough otomatis tidak menutupi layar.
- Tidak ada data backend atau state global yang diubah; pemulihan: semua mock dilepas di hook `after` walau spec gagal di tengah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-04: Loading state tabel, kedua tab

1. Tahan respons List log kedua tab
2. Buka Global Settings > Activity Log > Session
3. Verifikasi tab Session: skeleton loader tampil di area tabel, bukan tabel kosong tanpa indikator
4. Klik tab "User Action"
5. Verifikasi tab User Action: skeleton loader tampil di area tabel, bukan tabel kosong tanpa indikator
6. Lepaskan penahanan respons List log kedua tab dengan jawaban normal
7. Verifikasi tab User Action: skeleton diganti tabel normal
8. Verifikasi tab User Action: pagination tampil
9. Klik tab "Session"
10. Verifikasi tab Session: skeleton diganti tabel normal
11. Verifikasi tab Session: pagination tampil

### TC-GS-ACTLOG-05: Empty state genuinely kosong, kedua tab

12. Ganti mock List log kedua tab ke respons 0 baris, lalu muat ulang Global Settings > Activity Log > Session
13. Verifikasi tab Session: ilustrasi empty state tampil
14. Verifikasi tab Session: Title `No activity yet`
15. Verifikasi tab Session: Description `Activities will appear here as actions are performed.`
16. Verifikasi tab Session: tanpa tombol aksi
17. Klik tab "User Action"
18. Verifikasi tab User Action: ilustrasi empty state tampil
19. Verifikasi tab User Action: Title `No activity yet`
20. Verifikasi tab User Action: Description `Activities will appear here as actions are performed.`
21. Verifikasi tab User Action: tanpa tombol aksi

### TC-GS-ACTLOG-08: Error load tabel, kedua tab (bukan empty state)

22. Ganti mock List log kedua tab ke respons 5xx, lalu muat ulang Global Settings > Activity Log > Session
23. Verifikasi tab Session: alert error `Unable to load this data.`
24. Verifikasi tab Session: tombol `[Try Again]` pada alert
25. Verifikasi tab Session: empty state `No activity yet` tidak tampil
26. Klik tab "User Action"
27. Verifikasi tab User Action: alert error `Unable to load this data.`
28. Verifikasi tab User Action: tombol `[Try Again]` pada alert
29. Verifikasi tab User Action: empty state `No activity yet` tidak tampil

### TC-GS-ACTLOG-09: Klik [Try Again] memuat ulang data setelah error load, kedua tab

30. Ganti mock List log kedua tab ke respons 5xx pada permintaan pertama lalu normal pada permintaan berikutnya, lalu muat ulang Global Settings > Activity Log > Session
31. Tunggu alert error tampil pada tab Session
32. Klik `[Try Again]`
33. Verifikasi tab Session: alert error hilang
34. Verifikasi tab Session: tabel normal tampil
35. Verifikasi tab Session: pagination tampil
36. Klik tab "User Action"
37. Tunggu alert error tampil pada tab User Action
38. Klik `[Try Again]`
39. Verifikasi tab User Action: alert error hilang
40. Verifikasi tab User Action: tabel normal tampil
41. Verifikasi tab User Action: pagination tampil

## Notes

- Mode: mock. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-04, 5, 8, 9). Tidak ada TC hanya-BE.
- Kelas harness b (fault injection / resilience) untuk TC-8 dan TC-9; TC-4 (menahan respons hanya untuk mengamati loading) dan TC-5 (respons kosong) memakai mock yang sama sehingga seluruh spec satu mode mock.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (menahan respons), 6 (lepas penahanan, butir Expected TC-4 c), 9 (kembali ke tab Session untuk mengamati hasil pelepasan pada tab itu), 12, 22, dan 30 (mengganti mock dan memuat ulang halaman sebelum tiap TC), 31 dan 37 (menunggu alert).
- Pada langkah 33 dan 39 asersi alert error hilang (state sementara) ditaruh segera setelah pemicu `[Try Again]` dan sebelum asersi tabel; alert yang tampil pada langkah 31 dan 37 menjadi anchor positifnya.
- Spec di atas smell 35 langkah (41 langkah). Alasan: seluruh blok satu kelas dan satu mode (state tabel dengan mock), empat TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-4 mensyaratkan loading pada kedua tab dengan respons ditahan; TC tidak menyebut apakah penahanan berlaku untuk permintaan tab User Action yang baru dipicu saat tab diklik. Spec menahan respons kedua tab sejak awal.
  - TC-4 Expected c menyebut "pagination (S-05)" sebagai rujukan state PRD §7; spec mengasersi pagination tampil.
  - TC-9 tidak menyebut apakah "permintaan pertama" dihitung per tab atau global; spec memakai respons 5xx pada permintaan pertama tiap tab.
